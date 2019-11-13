"""カメラ座標とアーム座標のキャリブレーションをする。"""
import cv2
import numpy as np


def get_cam_arm_combo():
    yield (628, 384), (318, 150)  # LT
    yield (624, 142), (119, 135)  # LB
    yield (287, 393), (318, -115)  # RT
    yield (279, 152), (119, -105)  # RB
    yield (447, 363), (297, 20.0)  # 1
    yield (524, 319), (254, 76.4)  # 2
    yield (371, 315), (260, -33.3)  # 3
    yield (610, 257), (213, 129)  # 4
    yield (448, 269), (214, 20.4)  # 5
    yield (300, 268), (212, -106)  # 6
    yield (524, 215), (171, 72.9)  # 7
    yield (371, 219), (170, -36.6)  # 8
    yield (444, 166), (124, 18.8)  # 9


def calc_W():
    C = []
    A = []
    for cam, arm in get_cam_arm_combo():
        C.append((cam[0], cam[1], 1))
        A.append((arm[0], arm[1], 1))

    C = np.array(C).T
    A = np.array(A).T
    print("C.shape: ", C)
    print("A.shape: ", A)

    C_t = C.T

    W = np.dot(np.dot(A, C_t), np.linalg.inv(np.dot(C, C_t)))
    print(W)

    return W


def cam_to_arm(cam_coord, W):
    return np.dot(W, np.array((cam_coord[0], cam_coord[1], 1)))


def main():
    W = calc_W()

    for cam, arm in get_cam_arm_combo():
        print(f"cam: {cam}, true: {arm}, predict{np.dot(W, np.array((cam[0], cam[1], 1)))}")


if __name__ == '__main__':
    main()
