"""カメラで取得した画像を`cv2.imshow`で連続表示する。「q」キーで終了。"""
import cv2


def main():
    cap = cv2.VideoCapture(0)

    while True:
        is_valid, img_src = cap.read()
        if is_valid == False:
            continue
        img_src = cv2.flip(img_src, flipCode=1)
        img_dst = cv2.resize(img_src, None, fx=0.5, fy=0.5)

        cv2.imshow('dst', img_dst)
        key = cv2.waitKey(250)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
