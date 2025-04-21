# TuyenSinhGPT_web

## Tổng Quan

Dự án "TuyenSinhGPT_web" là một ứng dụng web toàn diện được phát triển nhằm cung cấp thông tin chính xác và cập nhật về điểm chuẩn đại học năm 2024 tại Việt Nam. Hệ thống được thiết kế với giao diện thân thiện, dễ sử dụng, giúp học sinh, phụ huynh và các cơ sở giáo dục dễ dàng truy cập, tìm kiếm và phân tích thông tin điểm chuẩn từ các trường đại học trên toàn quốc.

Ứng dụng kết hợp công nghệ cơ sở dữ liệu MongoDB với framework Flask của Python, tạo nên một hệ thống tra cứu thông tin hiệu quả và nhanh chóng. Đặc biệt, dự án còn tích hợp công nghệ trí tuệ nhân tạo thông qua một chatbot thông minh, sẵn sàng hỗ trợ và tư vấn người dùng về các vấn đề liên quan đến điểm chuẩn và tuyển sinh đại học.

## Tính Năng Chính

### 1. Hệ Thống Tìm Kiếm Đa Năng

- **Tìm Kiếm Cơ Bản**: Cho phép người dùng nhanh chóng tìm kiếm thông tin điểm chuẩn bằng từ khóa
- **Tìm Kiếm Nâng Cao**: Hỗ trợ lọc kết quả theo nhiều tiêu chí như trường, ngành, nhóm ngành, tổ hợp môn và khoảng điểm
- **Phân Trang và Sắp Xếp**: Tối ưu hóa trải nghiệm người dùng với các tùy chọn phân trang và sắp xếp kết quả

### 2. Thống Kê Và Phân Tích Dữ Liệu

- **Biểu Đồ Phân Bố Điểm**: Trực quan hóa phân bố điểm chuẩn qua các khoảng điểm khác nhau
- **Thống Kê Theo Nhóm Ngành**: Phân tích điểm chuẩn trung bình và số lượng ngành theo từng nhóm ngành
- **Xu Hướng Điểm Chuẩn**: Cung cấp thông tin về xu hướng điểm chuẩn qua các năm (nếu có dữ liệu)

### 3. Công Cụ So Sánh

- **So Sánh Đa Tiêu Chí**: Cho phép người dùng so sánh điểm chuẩn giữa các trường, ngành hoặc nhóm ngành
- **Biểu Đồ So Sánh**: Trực quan hóa kết quả so sánh thông qua các biểu đồ

### 4. Danh Mục Thông Tin Ngành và Trường

- **Danh Mục Phân Cấp**: Tổ chức thông tin theo nhóm ngành, ngành học và trường đào tạo
- **Trang Chi Tiết**: Cung cấp thông tin chi tiết về từng ngành và trường đào tạo

### 5. Trợ Lý Ảo Thông Minh (Chatbot)

- **Tư Vấn Điểm Chuẩn**: Trả lời trực tiếp các câu hỏi liên quan đến điểm chuẩn
- **Gợi Ý Ngành Học**: Dựa trên điểm số và sở thích của người dùng
- **Hỗ Trợ 24/7**: Sẵn sàng tư vấn mọi lúc mọi nơi

## Kiến Trúc Hệ Thống

Dự án được xây dựng dựa trên kiến trúc MVC (Model-View-Controller) với các thành phần chính:

- **Backend**: Sử dụng Flask framework (Python) để xây dựng REST API và phục vụ các trang web
- **Cơ Sở Dữ Liệu**: MongoDB - cơ sở dữ liệu NoSQL linh hoạt, phù hợp với dữ liệu có cấu trúc đa dạng
- **Frontend**: HTML, CSS, JavaScript
- **AI & Machine Learning**: Kết hợp SentenceTransformer, FAISS và Groq API (LLaMA3) để xây dựng chatbot thông minh

## Cấu Trúc Dự Án Chi Tiết

```
.
├── app.py                              # Điểm khởi đầu của ứng dụng Flask, định nghĩa routes và API endpoints
├── chatbot.py                          # Module xử lý logic và trí tuệ nhân tạo cho chatbot
├── import_data.py                      # Script tự động để nhập và làm sạch dữ liệu từ CSV vào MongoDB
├── requirements.txt
├── README.md
├── data/
│   ├── data_diem_chuan_cleaned.csv     # Dữ liệu điểm chuẩn đã qua xử lý và làm sạch
│   ├── dataset.json                    # Tập dữ liệu câu hỏi-đáp cho chatbot
│   └── vector_db.faiss                 # Vector database cho tìm kiếm ngữ nghĩa nhanh
├── static/
│   ├── css/
│   │   └── style.css                   # File CSS chính
│   └── js/
│       └── main.js                     # File JS chính cho các tính năng client-side
│
└── templates/
    ├── chat.html                       # Giao diện chatbot
    ├── danh-muc.html                   # Trang danh mục các nhóm ngành, ngành và trường
    ├── index.html                      # Trang chủ
    ├── layout.html                     # Template layout chung
    ├── nganh.html                      # Thông tin chi tiết về ngành học
    ├── nhom-nganh.html                 # Thông tin chi tiết về nhóm ngành
    ├── so-sanh.html                    # Công cụ so sánh điểm chuẩn
    ├── thong-ke.html                   # Trang thống kê và phân tích
    ├── tim-kiem-nang-cao.html          # Trang tìm kiếm nâng cao
    └── truong-dao-tao.html             # Thông tin về các trường đào tạo
```

## Công Nghệ Sử Dụng

### Backend

- **Flask**: Framework web Python nhẹ và linh hoạt
- **PyMongo**: Driver MongoDB cho Python
- **FAISS**: Thư viện tìm kiếm tương đồng hiệu suất cao (Facebook AI Similarity Search)
- **SentenceTransformer**: Thư viện tạo vector nhúng (embeddings) cho văn bản
- **Pandas**: Xử lý và phân tích dữ liệu

### Trí Tuệ Nhân Tạo

- **LLaMA3-70B**: Mô hình ngôn ngữ lớn (Large Language Model) thông qua Groq API
- **Vector Embeddings**: Chuyển đổi văn bản thành vector để tìm kiếm ngữ nghĩa
- **Groq API**: Dịch vụ AI cloud cung cấp khả năng truy cập đến các mô hình ngôn ngữ lớn

### Frontend

- **HTML5/CSS3**: Nền tảng cơ bản cho giao diện người dùng
- **JavaScript**: Xử lý tương tác phía client
- **Responsive Design**: Thiết kế tương thích với nhiều thiết bị

### Database

- **MongoDB**: Cơ sở dữ liệu NoSQL linh hoạt, dễ mở rộng

## Yêu Cầu Hệ Thống

### Phần Mềm

- Python 3.7 hoặc cao hơn
- MongoDB 4.0 hoặc cao hơn
- pip (trình quản lý gói Python)
- Virtual environment (khuyến nghị)

### Phần Cứng (Khuyến nghị)

- CPU: 2 cores trở lên
- RAM: Tối thiểu 4GB
- Dung lượng ổ cứng: 500MB cho code và dependencies

### Môi Trường

- Hỗ trợ: Windows, macOS, Linux
- Kết nối internet (cần thiết cho Groq API)

## Hướng Dẫn Cài Đặt

### 1. Chuẩn Bị Môi Trường

```bash
# Clone repository từ GitHub
git clone https://github.com/PhucHuwu/TuyenSinhGPT_web.git
cd TuyenSinhGPT_web

# Tạo và kích hoạt môi trường ảo (khuyến nghị)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 2. Cài Đặt Dependencies

```bash
# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

### 3. Cấu Hình Cơ Sở Dữ Liệu

```bash
# Đảm bảo MongoDB đang chạy
# MongoDB mặc định chạy trên port 27017
# Có thể kiểm tra trạng thái MongoDB với:
mongod --version
```

### 4. Import Dữ Liệu Mẫu

```bash
# Import dữ liệu mẫu vào MongoDB
python import_data.py

# Kết quả mong đợi: "Đã import thành công X bản ghi vào MongoDB!"
```

### 5. Cấu Hình API Key (cho Chatbot)

- Cấu hình Groq API key trong file `chatbot.py` hoặc thông qua biến môi trường

### 6. Khởi Động Ứng Dụng

```bash
# Khởi động server Flask
python app.py

# Ứng dụng sẽ chạy tại: http://localhost:8000
```

## API Documentation

Dự án cung cấp các RESTful API endpoints để tương tác với dữ liệu:

### Điểm Chuẩn

- **Endpoint**: `/api/diem-chuan`
- **Method**: GET
- **Parameters**:
  - `page`: Số trang (mặc định: 1)
  - `limit`: Số kết quả trên mỗi trang (mặc định: 10)
  - `search`: Từ khóa tìm kiếm
  - `sort_by`: Trường để sắp xếp (mặc định: 'Điểm chuẩn 2024')
  - `sort_order`: Thứ tự sắp xếp (1: tăng dần, -1: giảm dần, mặc định: -1)
  - `truong`: Lọc theo trường
  - `nhom_nganh`: Lọc theo nhóm ngành
  - `to_hop_mon`: Lọc theo tổ hợp môn
  - `diem_min`: Điểm chuẩn tối thiểu
  - `diem_max`: Điểm chuẩn tối đa
  - `nganh`: Lọc theo ngành
- **Response**: Danh sách điểm chuẩn và thông tin phân trang

### Danh Sách Trường Đào Tạo

- **Endpoint**: `/api/truong-dao-tao`
- **Method**: GET
- **Response**: Danh sách tất cả các trường đào tạo

### Danh Sách Nhóm Ngành

- **Endpoint**: `/api/nhom-nganh`
- **Method**: GET
- **Response**: Danh sách tất cả các nhóm ngành

### Danh Sách Ngành

- **Endpoint**: `/api/nganh`
- **Method**: GET
- **Parameters**:
  - `nhom_nganh`: Lọc ngành theo nhóm ngành (tùy chọn)
- **Response**: Danh sách các ngành

### Danh Sách Tổ Hợp Môn

- **Endpoint**: `/api/to-hop-mon`
- **Method**: GET
- **Response**: Danh sách tất cả các tổ hợp môn

### Thống Kê Phân Bố Điểm

- **Endpoint**: `/api/thong-ke/phan-bo-diem`
- **Method**: GET
- **Response**: Thống kê phân bố điểm chuẩn theo khoảng điểm

### Thống Kê Theo Nhóm Ngành

- **Endpoint**: `/api/thong-ke/nhom-nganh`
- **Method**: GET
- **Response**: Thống kê điểm chuẩn trung bình và số lượng ngành theo nhóm ngành

### API Chatbot

- **Endpoint**: `/api/chat`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "question": "Điểm chuẩn ngành Công nghệ thông tin tại ĐH Bách Khoa Hà Nội năm 2024 là bao nhiêu?"
  }
  ```
- **Response**: Câu trả lời từ chatbot

## Tính Năng Chatbot

Hệ thống chatbot thông minh được xây dựng dựa trên mô hình ngôn ngữ lớn LLaMA3-70B thông qua Groq API, kết hợp với kỹ thuật tìm kiếm ngữ nghĩa vector. Quy trình xử lý bao gồm:

1. **Chuyển Đổi Câu Hỏi**: Câu hỏi của người dùng được chuyển đổi thành vector embeddings sử dụng SentenceTransformer
2. **Tìm Kiếm Tương Đồng**: Sử dụng FAISS để tìm kiếm nhanh các context liên quan nhất trong cơ sở dữ liệu
3. **Sinh Câu Trả Lời**: Kết hợp câu hỏi và context tìm được để tạo prompt cho LLaMA3-70B
4. **Phản Hồi**: Câu trả lời được gửi về cho người dùng

Chatbot được thiết kế để hoạt động bằng tiếng Việt và cung cấp thông tin chính xác về điểm chuẩn đại học năm 2024, đồng thời có khả năng mở rộng để hỗ trợ tư vấn hướng nghiệp.

## Bảo Mật và Hiệu Suất

### Bảo Mật

- Dữ liệu người dùng không được lưu trữ lâu dài
- API key được bảo vệ và không được hardcode trong mã nguồn công khai
- Kiểm tra đầu vào để ngăn chặn các tấn công injection

### Hiệu Suất

- Sử dụng FAISS để tìm kiếm vector nhanh chóng
- Tối ưu hóa truy vấn MongoDB
- Phân trang để tải dữ liệu hiệu quả
- Caching để giảm thời gian phản hồi

## Lộ Trình Phát Triển

### Phiên Bản Hiện Tại (1.0)

- Tìm kiếm, thống kê và hiển thị thông tin điểm chuẩn
- Chatbot trả lời câu hỏi về điểm chuẩn
