# IoT_2_relay

## WTF is this

1. push.py

	`Untuk mengirim value ke field yang sudah di buat pada thingspeak`
2. get.py

	```
	Untuk mendapatkan nilai akhir dari field dan melakukan respon dengan mengirim nilai 0 atau 1 ke gpio
	```

## How To Use

a. copykan folder `get` ke dalam folder `/opt/`

b. copykan file `bot` kedalam folder `/etc/init.d/`

c. ubah permissionnya `chmod +x /etc/init.d/bot`

d. enable scriptnya `/etc/init.d/bot enable`

e. buat symlinknya `ls -lh /etc/rc.d | grep bot`

## Note

Tested on OpenWrt AA, with python installed
