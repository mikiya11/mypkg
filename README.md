# mypkg

このプログラムは、count.pyで出された値をtwice.pyでランダムで１～５倍にするもので、Raspberry Pi 4 Model B上のubuntuにおいて動作できる。

パブリッシャノード：count.py

サブスクライバノード：twice.py

## 使い方
端末１
	`roscore &`

	`chmod +x count.py`
	
	`rosrun mypkg count.py`

端末を変える必要有

端末２	

	`rosrun mypkg twice.py`

端末を変える必要有

端末３

	`rostopic echo /twice`

数倍になった値が端末上に表示される。

## デモ動画

## LICENCE
BSD 2-Clause "Simplified" License
