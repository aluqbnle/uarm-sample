# picking-tools-by-uArm
## ローカルへuArmのSDKをダウンロードする
[uArm-Python-SDK](https://github.com/uArm-Developer/uArm-Python-SDK)のsubmoduleを取り入れるためには、`git clone`後に
```sh
git submodule update --init
```
を実行する。

### 依存パッケージ
[uArm-Python-SDK](https://github.com/uArm-Developer/uArm-Python-SDK)は[pySerial](https://github.com/pyserial/pyserial)の3.0.0以上に依存しているため、[pySerial](https://github.com/pyserial/pyserial)の無い環境では
```sh
pip3 install pyserial
```
などを実行して依存を解決する。
