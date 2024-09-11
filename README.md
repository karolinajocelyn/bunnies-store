# 🐰bunnies-store🐰

hi! welcome to my repository~
this is my first web-based store where i sell multiple k-pop merch and albums. initially, this was supposed to sell only new jeans stuff but it expanded to other groups as well. we sell **authentic** products at a lower price rate. our motto? **from fans, to fans**. hope you enjoy shopping here!

deployment url: karolina-jocelyn-bunniesstore3.pbp.cs.ui.ac.id

====================

## QnA's

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Pertama, saya membuat proyek Django baru dengan cara yang cukup sederhana (naif) dengan cara meng-*copy* dan *paste* repository lokal dari aplikasi *mental-health-tracker* yang telah dibuat pada tutorial sebelumnya. Tentunya, saya memastikan untuk **delete** file-file yang seharusnya belum dibuat seperti aplikasi main, urls.py, tests.py, folder migrations, dan lainnya.
- Setelah itu, saya membuat aplikasi main yang di dalamnya ada template main.html ini. Webpage utama dari main.html saya rencanakan sebagai tempat input pencarian nama album, nama artist, price, dan deskripsi produk yang ingin dicari. Karena belum belajar mengenai forms, saya *mostly* melihat dari webiste ini: https://www.w3schools.com/html/html_forms.asp.
- Selain itu, saya menggunakan suatu background static sehingga saya menambahkan {% load static %} di bagian teratas html saya, lalu menambahkan folder static pada direktori proyek/utama saya. 
- Selanjutnya, saya mengedit models.py agar terdapat class Product yang memiliki atribut/field dengan tipe data sesuai, yakni IntegerFiled untuk price, CharField untuk nama album dan artist, serta TextField untuk deskripsi.
- Next, saya mencoba membuka file lain 1-1 dan mengganti seluruh nama *mental-health-tracker* menjadi *bunnies-store* seperti pada wsgi.py, asgi.py, manage.py, dan settings.py pada directory main.
- Lalu, saya membuat migrasi model yang berisi sebuah folder yang akan melacak perubahan pada model aplikasi berdasarkan kode terbaru saya dan saya runserver dengan manage.py
- Lalu, saya membuat fungsi bernama `show_main` pada views.py yang mengembalikan render dari main.html
- Setelah itu, saya membuat routing pada urls.py di dalam direktori main dan di direktori proyek sama seperti pada tutorial 1.
- Next, saya mendeploy project tersebut pada PWS dengan melakukan git remote add origin [URL] di terminal sehingga project saya dapat dilihat melalui internet.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Client Browser ---> urls.py (routing URL) ---> models.py (database query) ---> views.py (logika bisnis) ---> HTML

- Client akan mengakses web dengan mengirim permintaan HTTP ke server Django
- Django menerima request dan menggunakan urls.py untuk memeriksa pola URL yang cocok dengan request
- Jika sesuai, Django akan meneruskan ke class di views.py
- views.py akan menangani request dan memproses logika bisnis. Kalau perlu data dari database, views.py akan menggunakan models.py untuk query.
- fungsi dalam views.py akan menggunakan model pada models.py untuk mengakses data
- setelah diproses di views.py, akan kembali dikirimkan ke template HTML untuk ditampilkan kepada user.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
   
Git adalah sebuah alat software development yang berfungsi sebagai sistem kontrol untuk menyimpan, mengelola, dan membagikan *source code* secara lebih efisien dan kolaboratif. Git termasuk sebagai software yang open source dan mampu melacak perubahan dari *source code* suatu software serta membantu dalam manajemen *source code* sehingga lebih kolaboratif untuk suatu tim. Fungsi dari git adalah:
- memungkinkan setiap *developer* untuk melacak setiap perubahan pada *source code* yang telah di commit dan di push ke github repo.
- memungkinkan beberapa *developer* untuk bekerja secara bersamaan di proyek yang sama dengan fitur merge dan pull request.
- memungkinkan branching sehingga *developer* bisa mengembangkan fitur baru di luar branch/proyek utama.
- bisa digunakan sebagai backup karena ada history dari commit

sumber: https://dcloud.co.id/blog/apa-itu-git.html#:~:text=Git%20adalah%20alat%20software%20development,code)%20secara%20efisien%20dan%20kolaboratif

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   
Berdasarkan pengetahuan saya dari apa yang dipelajari di tutorial 0 dan 1, Django cukup komprehensif, terstruktur, dan mudah dipahami karena banyaknya komponen dalam pembuatan web seperti templates, views, models, dan routing. Dengan fitur-fitur Django yang sudah built-in, saya menjadi lebih mudah mempelajari Django tanpa merasa *overwhelmed* dengan banyaknya komponen teknis. Django juga memiliki dokumentasi yang kuat sehingga mudah dipelajari.

5. Mengapa model pada Django disebut sebagai ORM?
   
Model pada Django disebut sebagai ORM (Object-Relational Mapper) karena memungkinkan kita untuk berinteraksi dengan database seperti SQL, tetapi dalam bahasa Python sehingga kita mampu mengambil dan memanipulasi data pada database kita. Django memetakan antara objek python dan tabel database relasional.
