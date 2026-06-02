"""
1. Các hàm chức năng chính
- Hàm display_students(student_list):
    + Input: Danh sách học viên
    + Output: In ra màn hình hoặc thông báo danh sách rỗng nếu không có dữ liệu
- Hàm add_student(student_list):
    + Input: Danh sách học viên
    + Output: Thông báo thêm thành công hoặc báo lỗi (tên để trống, tên chỉ chứa khoảng trắng, mã đã tồn tại)
- Hàm update_score(student_list):
    + Input: Danh sách học viên
    + Output: Thông báo cập nhật thành công hoặc báo không tìm thấy nếu mã không tồn tại
- Hàm evaluate_students(student_list):
    + Input: Danh sách học viên
    + Output: In danh sách kèm điểm trung bình, xếp loại
2. Các hàm phụ trợ
- Hàm validate_score(score_input):
    + Input: Chuỗi nhập từ bàn phím
    + Output: True nếu có thể chuyển thành số thực và nằm trong khoảng từ 0 đến 10, ngược lại trả về False
- Hàm find_student_by_id(student_list, student_id):
    + Input: Danh sách học viên hiện tại và mã học viên cần cập nhật (đã chuẩn hóa)
    + Output: Trả về index của học viên trong list hoặc chính dictionary của học viên đó, nếu không thấy trả về None hoặc -1
- Hàm get_rank(average_score):
    + Input: Điểm trung bình (số thực)
    + Output: Chuỗi xếp loại ("Giỏi", "Khá", "Trung bình", "Yếu")
"""

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def validate_score(score_input):
    """
    Kiểm tra điểm nhập vào phải là số thực hợp lệ và từ 0 đến 10.
    Trả về True nếu hợp lệ, False nếu không hợp lệ.
    """
    normalization_score = score_input.replace(".", "", 1)
    if normalization_score.isdigit() and score_input.count(".") <= 1:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        
    return False
    
def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student["student_id"] == student_id:
            return student
        
    return None

def get_rank(average_score):
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"
    
def input_safe_score(subject_name):
    while True:
        score_input = input(f"Nhập Điểm {subject_name}: ").strip()
        if validate_score(score_input):
            return float(score_input)
        print("Điểm không hợp lệ, phải là số từ 0 đến 10. Vui lòng nhập lại!")

def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")

def display_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống")
        return
    
    print("\n--- DANH SÁCH HỌC VIÊN ---")
    for index, student in enumerate(student_list, start = 1):
        print(f"{index}. Mã: {student['student_id']} | Tên: {student['name']:<15} | Toán: {student['math_score']:<4} | Anh: {student['english_score']}")

def add_student(student_list):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if student_id == "":
            print("Mã học viên không được để trống!")
            continue
        
        if find_student_by_id(student_list, student_id) is not None:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        else:
            break

    while True:
        student_name = input("Nhập tên học viên: ").strip()
        if student_name == "":
            print("Tên học viên không được để trống!")
        else:
            student_name = student_name.title()
            break

    math_score = input_safe_score("Toán")
    english_score = input_safe_score("Anh")

    new_student = {
        "student_id": student_id,
        "name": student_name,
        "math_score": math_score,
        "english_score": english_score
    }
    student_list.append(new_student)
    print("Thêm học viên thành công!")

def update_score(student_list):
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(student_list, student_id)
    if student is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return
    
    new_math = input_safe_score("Toán mới")
    new_english = input_safe_score("Anh mới")

    student["math_score"] = new_math
    student["english_score"] = new_english
    print("Cập nhật điểm thi thành công!")

def evaluate_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống")
        return
    
    print("\n--- ĐÁNH GIÁ HỌC LỰC ---")
    for student in student_list:
        avg_score = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(avg_score)
        print(f"Mã: {student['student_id']} | Tên: {student['name']:<15} | ĐTB: {avg_score:.2f} | Xếp loại: {rank}")


while True:
    display_menu()
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
        
    if choice == "1":
        display_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        evaluate_students(students)
    elif choice == "5":
        print("\nCảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")