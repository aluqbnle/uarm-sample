"""AKAZEの動作テスト"""
import cv2

# 画像１
img1 = cv2.imread("image/target4.jpg")
# 画像２
img2 = cv2.imread("image/field_env.jpg")

# A-KAZE検出器の生成
akaze = cv2.AKAZE_create()

# 特徴量の検出と特徴量ベクトルの計算
kp1, des1 = akaze.detectAndCompute(img1, None)
kp2, des2 = akaze.detectAndCompute(img2, None)

# Brute-Force Matcher生成
bf = cv2.BFMatcher()

# 特徴量ベクトル同士をBrute-Force＆KNNでマッチング
matches = bf.knnMatch(des1, des2, k=2)

# データを間引きする
ratio = 0.75
good = []
for m, n in matches:
    if m.distance < ratio * n.distance:
        good.append([m])

# 対応する特徴点同士を描画
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

# 画像表示
cv2.imwrite('result_env4.jpg', img3)

# キー押下で終了
cv2.waitKey(0)
cv2.destroyAllWindows()
