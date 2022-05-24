import cv2
import time


wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


while True:
    # 1. nhận dạng cái bàn tay
    success, img = cap.read()

    # 2. Tìm ra đầu ngón trỏ và ngón giữa

    # 3. Kiểm tra xem ngón tay có đang chỉ lên

    # 4. Chỉ ngón tay trỏ: Di chuyển chuột ( Moing mode )
    
    # 5. Convert coordinates

    # 6. Smoothen values (làm mượt các giá trị)

    # 7. Move mouse

    # 8. Chỉ cả 2 ngón trỏ và ngón giữa lên => Click chuột (Clicking mode)

    # 9. Tìm khoảng cách giữa các ngón tay

    # 10. Click chuột nếu khoảng cách gần (short distance)

    # 11. Chỉnh Frame rate

    # 12. Hiển thị (Display)

    cv2.imshow("Camera 1 - Open CV", img)
    cv2.waitKey(1)

