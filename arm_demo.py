"""決め打ち座標で「掴む」「移動」「離す」のデモをする。"""
from uArmSDK.uarm.wrapper import SwiftAPI
from time import sleep

INIT_XYZA = (200, 0, 100, 90)
SRC_XYZA = (260, 85, -28, 95)
DST_XYZA = (200, -90, 20, 35)


def xyz_pos(xyza_coord):
    return (xyza_coord[0], xyza_coord[1], xyza_coord[2])


def above_xyz_pos(xyza_coord):
    return (xyza_coord[0], xyza_coord[1], INIT_XYZA[2])


def angle(xyza_coord):
    return xyza_coord[3]


def catch(obj, target_xyza_coord):
    obj.set_position(above_xyz_pos(target_xyza_coord))
    obj.set_wrist(angle(target_xyza_coord))
    obj.set_position(xyz_pos(target_xyza_coord))
    obj.set_gripper(True)
    sleep(2)


def init_uarm():
    '''
    uArm操作用のインスタンスを返す
    '''
    swift = SwiftAPI()
    swift.waiting_ready()
    return swift


def main():
    uarm = init_uarm()
    uarm.set_position(xyz_pos(INIT_XYZA))

    uarm.set_position(above_xyz_pos(SRC_XYZA))
    uarm.set_wrist(angle(SRC_XYZA))
    uarm.set_position(xyz_pos(SRC_XYZA))
    uarm.set_gripper(True)
    sleep(2)
    uarm.set_position(above_xyz_pos(SRC_XYZA))

    uarm.set_position(above_xyz_pos(DST_XYZA))
    uarm.set_wrist(angle=85)
    sleep(0.05)
    uarm.set_wrist(angle=75)
    sleep(0.05)
    uarm.set_wrist(angle=65)
    sleep(0.05)
    uarm.set_wrist(angle=55)
    sleep(0.05)
    uarm.set_wrist(angle=45)
    sleep(0.05)
    uarm.set_wrist(angle(DST_XYZA))
    uarm.set_position(xyz_pos(DST_XYZA))
    uarm.set_gripper(False)
    sleep(2)
    uarm.set_position(above_xyz_pos(DST_XYZA))

    uarm.set_position(xyz_pos(INIT_XYZA))
    uarm.set_wrist(angle(INIT_XYZA))

    uarm.disconnect()
    return


if __name__ == "__main__":
    main()
