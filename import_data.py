import pandas as pd
from pymongo import MongoClient
import os


def import_data_to_mongodb():
    # Kết nối đến MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['diem_chuan_db']
    collection = db['diem_chuan']

    # Kiểm tra xem file CSV có tồn tại không
    csv_path = 'data/data_diem_chuan_cleaned.csv'
    if not os.path.exists(csv_path):
        print(f"File {csv_path} không tồn tại!")
        return False

    try:
        # Đọc file CSV
        df = pd.read_csv(csv_path)

        # Kiểm tra cấu trúc dữ liệu
        expected_columns = [
            'Nhóm ngành', 'Ngành', 'Trường đào tạo', 'Mã ngành',
            'Tên ngành', 'Tổ hợp môn', 'Điểm chuẩn 2024', 'Ghi chú'
        ]

        # Kiểm tra và thêm các cột còn thiếu
        for col in expected_columns:
            if col not in df.columns:
                df[col] = ''

        # Xóa dữ liệu cũ (nếu có)
        collection.delete_many({})

        # Chuyển đổi DataFrame thành danh sách các dictionary
        records = df.to_dict('records')

        # Thêm dữ liệu mới
        collection.insert_many(records)

        print(f"Đã import thành công {len(records)} bản ghi vào MongoDB!")
        return True

    except Exception as e:
        print(f"Lỗi khi import dữ liệu: {str(e)}")
        return False


if __name__ == "__main__":
    import_data_to_mongodb()
