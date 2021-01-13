# Final Project Intrusi Deteksi Sistem 
#### Agnes Lesmono 05311840000044
-------------
### Deteksi Penggunaan Internet pada Linux

Pada project ini, menggunakan python dan shell untuk mendapatkan data penggunaan internet. Sistem penggunaan internet ini lebih ke perhitungan dalam jangka waktu bulanan. 

Penggunaan dapat dimulai dengan menginstall terlebih dahulu
` bash installer.sh `

Kemudian akan muncul perintah perintah untuk memasukkan data, sehingga tidak perlu mengatur cron secara manual:
- waktu dimulai perhitungan
- waktu diakhiri perhitungan
- tanggal dalam sebulan untuk reset

![](https://github.com/lumbricina/FP_IDS_Agnes-Lesmono_05311840000044/blob/main/installer.png)

User perlu memasukkan berdasarkan petunjuk yang ada. 
Kemudian, untuk dapat mulai bekerja, perlu dilakukan reboot dari OSnya terlebih dahulu.

Setelah reboot selesai, maka akan dapat menggunakan perintah-perintah yang telah di set pada program ini 

> Eusage -c   untuk mengubah settingan
Eusage -r   untuk mereset
Eusage -u   untuk menunjukkan yang data penggunaan current
Eusage -h   untuk help
Eusage -H   untuk menunjukkan history yang ada dengan memasukkan tahun dan bulan yang ingin dicari `

----------------------
### Penjelasan Koding
`Installer.sh` adalah awal untuk menginstall aplikasi.

Yang pertama, membuat direktori di `$HOME` bernamakan `.usage`. Pada direktori ini terdapat data-data dari penggunaan network monitor ini. 

Kemudian, menginstall cron tab, sehingga harus di reboot terlebih dahulu untuk cron dapat terinstall. 

Tampilan setelah menjalankan `Installer.sh ` adalah `Initial.py`

Pada `Initial.py` ditentukan bahwa `HOME=/home/honeysweetpotato` dimana ini merupakan home dari ubuntu saya.

Kemudian menggunakan library `os` dan `pickle` dimana library `pickle` ini yang digunakan untuk mengambil packet penggunaan internetnya.

Berikutnya mengeset waktu dan hari dengan meminta input dari pengguna, sesuai dengan gambar yang ada di atas.

Pada file `Eusage` menggunakan bahasa python dengan mengimport lib `sys`, `os`, `pickle`, dan `time`. Pada `Reset()`, adalah untuk mereset aplikasi, mengembalikan ke state sebelum adanya perubahan. Pada `Settime()`, seperti pada `initial.py`, untuk mengeset jam dan hari, namun ini digunakan setelah aplikasi telah terinstall. Pada `Usage()`, memangggil penggunaan kuota yang telah digunakan. Pada `Format_usage()`, mengeset supaya bisa lebih mudah dimengerti kuota yang digunakannya (dalam bentuk Byte, KiloByte, MegaBytem GigaByte). Pada `History(month,year)` digunakan untuk menunjukkan history yang ada sebelumnya. `Help()` untuk menunjukkan perintah yang tersedia. Berikutnya dibawahnya adalah setting untuk perintah-perintah, `-r` memanggil `Reset()`, `-u` memanggil `Usage()`, `-c` memanggil `Settime()`, dan `-H` memanggil `History()`, dan `-h` memanggil `Help()`. Pada `iusaged` disini mengambil data dari `/proc/net/dev`

Pada `Reset` digunakan untuk mereset semua data yang ada. Data-data yang sudah ada dijadikan kembali kosong atau `0`. `ResetCron` digunakan untuk mereset cron atau setingan waktu