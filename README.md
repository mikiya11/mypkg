# mypkg

このプログラムは、count.pyで出された値をtwice.pyで二倍してそれをrand.pyでランダムに１～４倍にするもので、Raspberry Pi 4 Model B上のubuntuにおいて動作できる。

パブリッシャノード１：count.py

サブスクライバノード１：twice.py


パブリッシャノード２：twice.py

サブスクライバノード２：rand.py

## 使い方
### 端末１
`chmod +x [ファイル名]`でそれぞれ実行できるようにしておく。
ROSをインストールしておき、`roscore &`でROSを起動しておく。
	
	rosrun mypkg count.py

端末を変える必要有。

### 端末２	
	rosrun mypkg twice.py

端末を変える必要有。

### 端末３
	rosrun mypkg rand.py

数倍になった値が端末上に表示される。

## デモ動画
[youtube]https://youtu.be/OvMjLec0xNs
## LICENCE
BSD 2-Clause "Simplified" License
