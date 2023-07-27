
Penerapan Algoritma Huffman dan 
Quantization dalam 
Kompresi Gambar Monokrom
Rizky Rahmat Nugraha1* ,  Zakki Mubarrok2 ,  Eva Nurlatifah3
Dapartement of Informatics, UIN Sunan Gunung Djati Bandung , Indonesia
Email: rizkyrahmat292@gmail.com , 1207050131@student.uinsgd.ac.id , evanurlatifah@uinsgd.ac.id 

 
 
 
 
Abstract— Penelitian ini mempresentasikan metode kompresi gambar yang menggabungkan  algoritma Huffman dan Quantization , dengan  mengoptimalkan ukuran file gambar dengan sedikit pengorbanan dari kualitas gambar, tidak begitu berpengaruh tetapi akan terlihat . Gambar skala abu-abu atau yang sering disebut monokrom adalah gambar yang kami uji dalam penelitian ini. Teknik Quantization diandalkan untuk mengurangi presisi tingkat ke abuan terhadap setiap gambar . Untuk mengkompresi tingkat keabuan yang telah dikuantisasi adalah peran algorima Huffman di penelitian ini , selain itu algoritma Huffman akan menghasilkan table kode biner yang memetakan tingkat keabuan ke kode kode yang lebih pendek bahkan bisa jadi lebih panjang. Dengan menggabungkan dua algoritma berbeda ini maka penelitian ini sangat berkontribusi terhadap bidang kompresi gambar , yaitu algoritma Huffman dan Quantization terlebih pada gambar skala abu-abu atau lebih dikenali dengan monokrom.
Keywords—Kompresi gambar, Huffman Coding , Quantization, Monokrom
I.	INTRODUCTION
Tidak bisa disangkal bahwa kemajuan dalam perkembangan komputer dan telekomunikasi telah mengubah cara masyarakat di seluruh dunia menjalankan aktivitas sehari-hari[1].Salah satunya kompresi file , kompresi file memiliki manfaat dalam konteks keamanan. Misalnya, penggunaan perangkat lunak kompresi file seperti WinZip dapat memberikan kontribusi dalam melindungi keamanan file dengan cara mengamankan data melalui proses enkripsi sebelum diunggah ke penyimpanan cloud[2]. Semakin besar kapasitas suatu data, maka proses pertukaran data akan memakan waktu yang lebih lama[3].
Ada dua jenis algoritma kompresi gambar, yaitu kompresi lossy dan kompresi lossless[4]. Metode kompresi Lossy adalah suatu metode kompresi data yang menghilangkan sebagian informasi, sedangkan metode kompresi Lossless adalah suatu metode kompresi data di mana tidak ada informasi yang hilang atau berkurang jumlahnya selama proses kompresi[5]. Kompresi data, juga dikenal sebagai pemadatan data, adalah teknik yang digunakan untuk mengurangi ukuran data atau mengubahnya menjadi bentuk data lain yang menggunakan simbol yang lebih sederhana [6].
Sedangkan algoritma Huffman ini sendiri menggunakan metode lossy compression[7] ,yang didukung oleh algoritma quatization yang akan menyempurnakan penelitian kali ini.
	Warna adalah elemen yang penting dalam kehidupan sehari-hari. Dalam perkembangan dan kemajuan teknologi, warna dapat diklasifikasikan menjadi dua jenis yaitu unsur aditif (additive) yang terkait dengan warna cahaya dan disebut spektrum, dan unsur subtraktif (subtractive) yang terkait dengan warna bahan seperti pigmen atau warna yang terdapat pada material[8].Sedang kan pada penilitian kali ini akan berfokus pada object yang hanya memiliki dua warna yaitu hitam dan putih atau akrab menganlnya dengan sebutan monokrom.
	Kembali pada algortima Quantization , Dengan menggunakan metode Quantization, kita dapat mengklasifikasikan data berdasarkan kedekatan jaraknya dengan bobot yang telah ditentukan. Hal ini membuat LVQ menjadi alat yang berguna dalam berbagai aplikasi seperti dalam bidang medis dan analisis data[9]. Tujuan dari metode Quantization adalah mencari nilai bobot yang sesuai untuk mengelompokkan vektor-vektor ke dalam kelas tujuan yang telah diinisialisasi saat pembentukan jaringan Learning Vector Quantization. Metode ini telah diterapkan dalam berbagai masalah praktis, termasuk dalam bidang medis dan analisis data[9].


II.	METODE PENELITIAN
A.	Bahasa Pemograman dan alat
Disini kami memutuskan untuk menggunakan bahasa python untuk penelitian kali ini, Python memiliki dukungan untuk berbagai paradigma pemrograman, termasuk namun tidak terbatas pada pemrograman berorientasi objek, pemrograman imperatif, dan pemrograman fungsional[10].Maka dari itu kami memutuskan untuk memakai bahasa pemograman ini untuk melanjutkan penelitian ini.
Didukung oleh alat yang bernama Visual Studio Code VSC ,dengan berbagai extensi yang kami install dan beberapa package yang kami pakai untuk mendukung penelitian kali ini.
B.	Menyiapkan bahan dan data
 
Gambar 1 object color full
Pada tahap ini kami mencari data atau gambar berupa monokrom atau pun yang berwarna , tidak masalah bagi kami untuk menggambil data yang berwarna karna nanti kami menyiapkan tools untuk memastikan bahwa warna dari object benar benar monokrom.
 
Gambar 2. Mengubah object menjadi monokrom
Pada tahap diatas adalah proses pengambilan data dari penyimpanan lokal dan langsung di proses menjadi gambar yang monokrom. Pada beberapa kasus gambar bisa saja tidak perlu untuk di kompresi menjadi monokrom terlebih dahulu.
 
Gambar 3. Hasil pengubahan object menjadi monokrom
C.	Memproses Menggunakan Huffman Coding
Pada tahap ini algoritma Huffman coding bekerja , pada tahap ini kami serahkan sepenuh nya kepada teknologi algoritma ini , mengingat sudah banyak sekali penelitian yang menggunakanan metode ini.
 
Gambar 4.Algoritma Huffman Coding

D.	Menentukan Tingkat Quantization 
 
Gambar 5 . Menentukan tingkat Quantization
 
Gambar 6 . kuantisasi gambar
	Pada tahap ini kami melakukan eksperimen dengan menggunakan tingkat quantization awal nya 10 , namun pada hasilnya gambar gelap gulita hampir tak terlihat , maka kami memutuskan untuk meningkatkan tingkan quantization menjadi 100.
E.	Hasil
 
Gambar 7. Experimen tingkat quntization 100
 
Gambar 8 . Expreimen tingkat quantization 10.

III.	KESIMPULAN
Berdasarkan metode dan hasil yang telah kami lakukan diatas , kami menyimpulkan bahwa teknik quantization dan algoritma Huffman sangat bisa untuk melakukan eksperimen ini hanya saja ada beberapa catatan dalam eksperimen yang kami lakukan.
Hal pertama yang menjadi acuan dari hasil adalah peneliti harus benar benar memastikan bahwa object tersebut hanya memilliki 2 warna saja atau monokrom , karena akan memiliki perbedaan signifikan ketika object mempunyai structure warna lain.
Kemudian metode quantization menentukan seberapa jelas object akan terlihat , semakin besar tingkat quantization semakin terlihat object pada hasil , kemudian semakin kecil tingkat quantization pada penelitian ini maka akan semakin kecil pula tingkat kecerahan dan kejelasan pada hasil object tersebut.
REFERENCES


[1]	Ismai, “Teknologi Informasi dan Sistem Informasi Manajemen,” Kita menulis, p. 57, 2020, [Online]. Available: https://www.google.co.id/books/edition/Teknologi_Informasi_dan_Sistem_Informasi/L5gQEAAAQBAJ?hl=en&gbpv=0&kptab=overview
[2]	J. G. Hasintongan, “Pemanfaatan Algoritma JPEG untuk Kompresi Gambar Digital,” 2021, [Online]. Available: https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/2020-2021/Makalah/Makalah-Matdis-2020 (20).pdf
[3]	E. Hariska, “Perancangan Aplikasi Kompresi File Gambar Menggunakan Algoritma Additive Code,” Nas. Teknol. Inf. dan Komputer), vol. 5, no. 1, pp. 193–202, 2021, doi: 10.30865/komik.v5i1.3671.
[4]	I. K. Adi Bayu Adnyana, I. M. Oka Widyantara, and N. Dewi Wirastuti, “Analisa Metode Shannon Entropy Dan Differential Evolution Untuk Kompresi Gambar,” J. SPEKTRUM, vol. 8, no. 2, p. 221, 2021, doi: 10.24843/spektrum.2021.v08.i02.p25.
[5]	W. E. Pangesti, G. Widagdo, D. Riana, and S. Hadianti, “Implementasi Kompresi Citra Digital Dengan Membandingkan Metode Lossy Dan Lossless Compression Menggunakan Matlab,” J. Khatulistiwa Inform., vol. 8, no. 1, 2020.
[6]	R. Y. Tanjung and M. Mesran, “Perancangan Aplikasi Kompresi File Dokumen Menggunakan Algoritma Adiitive Code,” JURIKOM (Jurnal Ris. Komputer), vol. 8, no. 4, pp. 108–113, 2021.
[7]	R. Krasmala, A. Budimansyah, and U. T. Lenggana, “Kompresi Citra Dengan Menggabungkan Metode Discrete Cosine Transform (DCT) dan Algoritma Huffman,” J. Online Inform., vol. 2, no. 1, pp. 1–9, 2017.
[8]	D. N. Fajar Paksi, “Warna Dalam Dunia Visual,” IMAJI Film. Fotogr. Telev. Media Baru, vol. 12, no. 2, pp. 90–97, 2021, doi: 10.52290/i.v12i2.49.
[9]	R. Hariyanto, A. Basuki, and R. N. Hasanah, “Klasifikasi penyakit mata katarak berdasarkan kelainan patologis dengan menggunakan algoritma Learning Vector Quantization,” Netw. Eng. Res. Oper., vol. 2, no. 3, pp. 177–182, 2016.
[10]	A. N. Syahrudin and T. Kurniawan, “Input dan output pada bahasa pemrograman python,” J. Dasar Pemograman Python STMIK, vol. 20, pp. 1–7, 2018.
 

