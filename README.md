# mypkg

このプログラムは、count.pyで出された値をtwice.pyで二倍してそれをrandom.pyでランダムに１～４倍にするもので、Raspberry Pi 4 Model B上のubuntuにおいて動作できる。

パブリッシャノード１：count.py

サブスクライバノード１：twice.py


パブリッシャノード２：twice.py

サブスクライバノード２：random.py

## 使い方
### 端末１
	roscore &

	chmod +x count.py
	
	rosrun mypkg count.py

端末を変える必要有

### 端末２	
	rosrun mypkg twice.py

端末を変える必要有

### 端末３
	rosrun mypkg random.py

数倍になった値が端末上に表示される。

## デモ動画

## LICENCE
BSD 2-Clause "Simplified" License
