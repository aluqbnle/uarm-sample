"""現在のuArmのxyz座標を取得して終了する。"""
from time import sleep
from uArmSDK.uarm.wrapper import SwiftAPI


swift = SwiftAPI(timeout=5000)
sleep(2)
print(swift.get_position(timeout=5000))
