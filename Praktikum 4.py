import random

#Daftar ini memberikan gambaran tentang waktu acara.
Kalimat_starter = random.randint(1, 3)
if Kalimat_starter == 1 :
    kalimat_1 = ("Pada pagi hari, ")
if Kalimat_starter == 2 :
    kalimat_1 = ("Pada siang hari, ")
if Kalimat_starter == 3 :
    kalimat_1 = ("Pada sore hari, ")

#Daftar ini menceritakan tentang karakter utama dari cerita ini.
karakter = random.randint(1, 3)
if karakter == 1 :
    kalimat_2 = ("Yatno sedang tidur ")
if karakter == 2 :
    kalimat_2 = ("Yatno sedang mandi ")
if karakter == 3 :
    kalimat_2 = ("Yatno sedang gosok gigi ")

#Daftar ini menentukan hari yang tepat di mana beberapa insiden telah terjadi.
waktu = random.randint(1, 3)
if waktu == 1 :
    kalimat_3 = ("dan pada hari sabtu hari ini ia bersantai")
if waktu == 2 :
    kalimat_3 = ("dan pada hari jumat hari ini ia sedang mengepel ")
if waktu == 3 :
    kalimat_3 = ("dan pada hari kamis ini sedang mengerjakan artikel ")

#Daftar ini mendefinisikan plot cerita.
story_plot = random.randint(1, 3)
if story_plot == 1 :
    kalimat_4 = ("karena hari libur, ")
if story_plot == 2 :
    kalimat_4 = ("karena ia sedang tidak sibuk, ")
if story_plot == 3 :
    kalimat_4 = ("karena tidak ada hal yang dilakukan, ")

#Daftar ini mendefinisikan tempat di mana insiden itu terjadi.
tempat = random.randint(1, 3)
if tempat == 1 :
    kalimat_5 = ("ia mengerjakanya di halaman depan, ")
if tempat == 2 :
    kalimat_5 = ("ia mengerjakan di balkon, ")
if tempat == 3 :
    kalimat_5 = ("ia mengerjakan di kamar, ")

#Daftar ini mendefinisikan karakter kedua dari cerita.
second_character = random.randint(1, 3)
if second_character == 1 :
    kalimat_6 = ("sedangkan ayah membaca berita ")
if second_character == 2 :
    kalimat_6 = ("sedangkan ibu sedang merebus mi ")
if second_character == 3 :
    kalimat_6 = ("sedangkan paman sedang bermain bersama anaknya ")

#Daftar ini mendefinisikan usia karakter kedua.
usia = random.randint(1, 3)
if usia == 1 :
    kalimat_7 = ("karena usianya sudah 70 tahun ")
if usia == 2 :
    kalimat_7 = ("karena usianya sudah 45 tahun ")
if usia == 3 :
    kalimat_7 = ("karena usianya sudah 32 tahun ")

#Daftar ini menceritakan tentang pekerjaan yang dilakukan karakter kedua.
pekerjaan = random.randint(1, 3)
if pekerjaan == 1 :
    kalimat_8 = ("karena ia sudah tidak bekerja lagi.")
if pekerjaan == 2 :
    kalimat_8 = ("karenanya ia hanya membuka toko didepan rumah ")
if pekerjaan == 3 :
    kalimat_8 = ("karenanya ia tidak lagi melanjutkan pekerjaan kantornya ")

print (kalimat_1, kalimat_2, kalimat_3, kalimat_4, kalimat_5, kalimat_6, kalimat_7, kalimat_8)