# Final Project Intrusi Deteksi Sistem 
#### Agnes Lesmono 05311840000044
-------------
### Deteksi Penggunaan Internet pada Linux

Pada project ini, menggunakan python dan shell untuk mendapatkan data penggunaan internet. Sistem penggunaan internet ini lebih ke perhitungan dalam jangka waktu bulanan. 

Penggunaan dapat dimulai dengan menginstall terlebih dahulu
``` bash installer.sh ```

Kemudian akan muncul perintah perintah untuk memasukkan data, sehingga tidak perlu mengatur cron secara manual:
- waktu dimulai perhitungan
- waktu diakhiri perhitungan
- tanggal dalam sebulan untuk reset

![](https://github.com/lumbricina/FP_IDS_Agnes-Lesmono_05311840000044/blob/main/installer.png)

User perlu memasukkan berdasarkan petunjuk yang ada. 
Kemudian, untuk dapat mulai bekerja, perlu dilakukan reboot dari OSnya terlebih dahulu.

Setelah reboot selesai, maka akan dapat menggunakan perintah-perintah yang telah di set pada program ini 

``` Eusage -c   untuk mengubah settingan
Eusage -r   untuk mereset
Eusage -u   untuk menunjukkan yang data penggunaan current
Eusage -h   untuk help
Eusage -H   untuk menunjukkan history yang ada dengan memasukkan tahun dan bulan yang ingin dicari ```

----------------------
### Penjelasan Koding
