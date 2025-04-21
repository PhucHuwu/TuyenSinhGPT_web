from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
import json
from bson import json_util
import os
from import_data import import_data_to_mongodb

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/diem_chuan_db"
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/thong-ke')
def thong_ke():
    return render_template('thong-ke.html')


@app.route('/tim-kiem-nang-cao')
def tim_kiem_nang_cao():
    return render_template('tim-kiem-nang-cao.html')


@app.route('/so-sanh')
def so_sanh():
    return render_template('so-sanh.html')


@app.route('/danh-muc')
def danh_muc():
    return render_template('danh-muc.html')


@app.route('/nhom-nganh/<nhom_nganh>')
def nhom_nganh_detail(nhom_nganh):
    return render_template('nhom-nganh.html', nhom_nganh=nhom_nganh)


@app.route('/nganh/<nganh>')
def nganh_detail(nganh):
    return render_template('nganh.html', nganh=nganh)


@app.route('/truong-dao-tao/<nganh>')
def truong_dao_tao_nganh(nganh):
    return render_template('truong-dao-tao.html', nganh=nganh)


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json
    question = data.get('question', '')

    if not question:
        return jsonify({'error': 'Vui lòng nhập câu hỏi'}), 400

    try:
        from chatbot import get_chatbot_response, initialize_chatbot

        answer = get_chatbot_response(question)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/import-data')
def import_data():
    success = import_data_to_mongodb()
    if success:
        return jsonify({"status": "success", "message": "Dữ liệu đã được import thành công!"})
    else:
        return jsonify({"status": "error", "message": "Có lỗi xảy ra khi import dữ liệu!"})


@app.route('/api/diem-chuan', methods=['GET'])
def get_diem_chuan():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    search = request.args.get('search', '')
    sort_by = request.args.get('sort_by', 'Điểm chuẩn 2024')
    sort_order = int(request.args.get('sort_order', -1))

    truong = request.args.get('truong', '')
    nhom_nganh = request.args.get('nhom_nganh', '')
    to_hop_mon = request.args.get('to_hop_mon', '')
    diem_min = request.args.get('diem_min', '')
    diem_max = request.args.get('diem_max', '')
    nganh = request.args.get('nganh', '')

    query = {}

    if search:
        query['$or'] = [
            {'Nhóm ngành': {'$regex': search, '$options': 'i'}},
            {'Ngành': {'$regex': search, '$options': 'i'}},
            {'Trường đào tạo': {'$regex': search, '$options': 'i'}},
            {'Mã ngành': {'$regex': search, '$options': 'i'}},
            {'Tên ngành': {'$regex': search, '$options': 'i'}}
        ]

    if truong:
        query['Trường đào tạo'] = {'$regex': truong, '$options': 'i'}

    if nhom_nganh:
        query['Nhóm ngành'] = {'$regex': nhom_nganh, '$options': 'i'}

    if nganh:
        query['Ngành'] = {'$regex': nganh, '$options': 'i'}

    if to_hop_mon:
        query['Tổ hợp môn'] = {'$regex': to_hop_mon, '$options': 'i'}

    diem_query = {}
    if diem_min:
        try:
            diem_query['$gte'] = float(diem_min)
        except ValueError:
            pass

    if diem_max:
        try:
            diem_query['$lte'] = float(diem_max)
        except ValueError:
            pass

    if diem_query:
        query['Điểm chuẩn 2024'] = diem_query

    total = mongo.db.diem_chuan.count_documents(query)

    skip = (page - 1) * limit
    cursor = mongo.db.diem_chuan.find(query).sort(sort_by, sort_order).skip(skip).limit(limit)

    data = json.loads(json_util.dumps(list(cursor)))

    return jsonify({
        'data': data,
        'total': total,
        'page': page,
        'limit': limit,
        'total_pages': (total + limit - 1) // limit
    })


@app.route('/api/truong-dao-tao', methods=['GET'])
def get_truong_dao_tao():
    truong_list = mongo.db.diem_chuan.distinct('Trường đào tạo')
    return jsonify(json.loads(json_util.dumps(truong_list)))


@app.route('/api/nhom-nganh', methods=['GET'])
def get_nhom_nganh():
    nhom_nganh_list = mongo.db.diem_chuan.distinct('Nhóm ngành')
    return jsonify(json.loads(json_util.dumps(nhom_nganh_list)))


@app.route('/api/nganh', methods=['GET'])
def get_nganh():
    nhom_nganh = request.args.get('nhom_nganh', '')

    if nhom_nganh:
        query = {'Nhóm ngành': nhom_nganh}
        nganh_list = mongo.db.diem_chuan.distinct('Ngành', query)
    else:
        nganh_list = mongo.db.diem_chuan.distinct('Ngành')

    return jsonify(json.loads(json_util.dumps(nganh_list)))


@app.route('/api/to-hop-mon', methods=['GET'])
def get_to_hop_mon():
    to_hop_mon_list = mongo.db.diem_chuan.distinct('Tổ hợp môn')
    unique_to_hop = set()
    for to_hop in to_hop_mon_list:
        if to_hop:
            parts = to_hop.replace(' ', '').split(';')
            for part in parts:
                if part:
                    unique_to_hop.add(part)

    return jsonify(json.loads(json_util.dumps(sorted(list(unique_to_hop)))))


@app.route('/api/thong-ke/phan-bo-diem', methods=['GET'])
def get_phan_bo_diem():
    pipeline = [
        {
            '$group': {
                '_id': {
                    '$concat': [
                        {'$substr': [{'$toString': {'$toDouble': '$Điểm chuẩn 2024'}}, 0, 2]},
                        '-',
                        {'$cond': [
                            {'$gte': [{'$toDouble': '$Điểm chuẩn 2024'}, 10]},
                            {'$substr': [{'$toString': {'$add': [{'$toDouble': '$Điểm chuẩn 2024'}, 1]}}, 0, 2]},
                            {'$substr': [{'$toString': {'$add': [{'$toDouble': '$Điểm chuẩn 2024'}, 1]}}, 0, 1]}
                        ]}
                    ]
                },
                'count': {'$sum': 1},
                'avg_score': {'$avg': {'$toDouble': '$Điểm chuẩn 2024'}}
            }
        },
        {
            '$sort': {'_id': 1}
        }
    ]

    result = list(mongo.db.diem_chuan.aggregate(pipeline))
    return jsonify(json.loads(json_util.dumps(result)))


@app.route('/api/thong-ke/nhom-nganh', methods=['GET'])
def get_thong_ke_nhom_nganh():
    pipeline = [
        {
            '$group': {
                '_id': '$Nhóm ngành',
                'count': {'$sum': 1},
                'avg_score': {'$avg': {'$toDouble': '$Điểm chuẩn 2024'}}
            }
        },
        {
            '$sort': {'_id': 1}
        }
    ]

    result = list(mongo.db.diem_chuan.aggregate(pipeline))
    return jsonify(json.loaFds(json_util.dumps(result)))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
