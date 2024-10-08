# 🐰bunnies-store🐰

hi! welcome to my repository~
this is my first web-based store where i sell multiple k-pop merch and albums!
deployment url: http://karolina-jocelyn-bunniesstore.pbp.cs.ui.ac.id

## QnA's

### Tugas 2
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

### Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam membuat suatu platform, data delivery dengan menggunakan file data berbentuk .xml dan .json sangatlah penting karena memampukan komponen-komponen web untuk berkomunikasi satu dengan lainnya. Misalkan, ketika kita mengisi form yang terdapat pada web, data dari komponen *front-end* harus bisa mengirimkan data tersebut ke *back-end* sehingga dapat disimpan di *database*. Hal ini tujuannya agar data yang ditampilkan pada *front-end* tersebut sinkron dengan apa yang ditampilkan pada *back-end*. 

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Ada beberapa perbedaan yang membuat JSON yang lebih baik dan populer dibandingkan dengan XML, yakni:
- XML adalah *markup language*, sedangkan JSON adalah *data format*. JSON menyimpan seperti *map*, dengan key dan value pairs, sedangkan XML menyimpan dengan tags.
- JSON memiliki file size yang lebih kecil sehingga transfer data dengan file JSON akan lebih cepat.
- format dari JSON lebih *compact* dan mudah dibaca dibandingkan dengan XML karena minimal sintaks dan strukturnya, sedangkan XML dinilai lebih *old-fashioned* dengan struktur tag yang sulit dibaca.
- JSON dinilai terkadang lebih aman, kecuali saat JSONP (JSON dengan Padding) dipakai karena bisa terjadi CSRF attack.
- JSON lebih mudah di-*parse* dengan JavaScript function, sedangkan XML harus dengan XML *parser*.

Namun, XML juga memiliki beberapa kelebihan dibandingkan dengan JSON, salah satunya adalah kemampuan untuk menambahkan *comments, metadata*, dan *namespaces*, serta menggunakan tipe data seperti *images* dan *charts*, sedangkan JSON hanya mampu memiliki tipe data strings, objects, numbers, dan boolean arrays.
sumber: https://www.imaginarycloud.com/blog/json-vs-xml

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` digunakan untuk memvalidasi input yang diisi oleh user pada form web sesuai dengan field peminta input, contohnya adalah `IntegerField` harus berupa bilangan bulat. Method ini mereturn True apabila datanya valid dan menaruh data pada atribut `cleaned_data`.
sumber: https://www.javatpoint.com/django-form-validation

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? 

Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF attack atau *Cross-Site Request Forgery* merupakan suatu serangan yang tujuannya adalah mengubah *submission* input dari user, seperti mengubah/menghapus record, submit transaksi, pembelian produk, pengubahan *password*, dan lainnya. CSRF attack akan terjadi pada web yang tidak mampu membedakan antara *request* yang valid dan yang tidak valid (*forged*) yang dikontrol oleh penyerang.

Untuk mengatasi hal tersebut, harus ada CSRF Token, yaitu sebuah *random secure* token sebagai lapisan validasi tambahan yang unik per sesi pengisian form dan terdiri dari nilai yang besar agar sulit ditebak oleh penyerang. Jika kita tidak menambahkan CSRF token, maka penyerang dapat memanfaatkan sesi login dari pengguna yang sah untuk melakukan penyerangan tanpa sepengetahuan dari pengguna. Contohnya adalah ketika login bank tanpa token CSRF, penyerang bisa mengirim *request* ke bank untuk transfer uang ke akun penyerang.
sumber: https://www.synopsys.com/glossary/what-is-csrf.html#:~:text=A%20CSRF%20token%20is%20a,token%20for%20every%20user%20session.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Melanjutkan dari apa yang dilakukan pada tugas 2, 
- Saya mengimplementasi bentuk form dengan membuat main.html dan create_product.html. Saya membuat page baru untuk membuat produk dan mengatur tampilan produk yang telah didaftarkan pada main.html. Selain itu, saya juga menambahkan base.html pada directory bunnies-store/templates (root folder).
- Saya mengubah primary key dari integer menjadi UUID agar setiap object yang didaftarkan memiliki ID sendiri, bukan hanya integer pada models.py.
- Saya membuat migrations baru dengan perintah ini:
`python3 manage.py makemigrations
python3 manage.py migrate`
- Saya membuat forms.py untuk mengisi struktur form yang dapat menerima product baru.
- Pada views.py, saya membuat function create_product sehingga dapat menambahkan form yang telah diisi user dengan valid. Selain itu, saya juga mengubah fungsi show_main agar mampu menampilkan semua object yang telah terdaftar.
- Function-function baru ini ditambahkan ke urls.py dan saya juga membuat path baru ke page creat_product.html
- Saya membuat function show_xml, show_json, show_xml_by_id, dan show_json_by_id pada views.py dan juga menambahkan URL menuju page masing-masing pada `urlpatterns` di urls.py
- Untuk memastikan semuanya berjalan dengan lancar, saya juga `runserver` dan membuat *request* baru dengan method `GET` pada URL-URL yang telah didaftarkan.

6. Berikut adalah *screenshot* dari Postman untuk URL dari xml dan json.
![Alt text](<show XML.png>)
![Alt text](<show XML by ID.png>)
![Alt text](<show JSON.png>)
![Alt text](<show JSON by ID.png>)

### Tugas 4
1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?

`HttpResponseRedirect()` merupakan suatu class dalam Django yang digunakan untuk me-redirect ke URL tertentu sehingga kita harus menyediakan URL secara explicit dalam argumen/parameternya. Contohnya seperti `return HttpResponseRedirect('/home/')`. 

`redirect()` merupakan shortcut dari Django untuk melakukan redirect dengan lebih fleksibel sehingga kita bisa memberikan URL atau nama dari view sebagai argumen. Contohnya seperti `redirect('home')`.

2. Jelaskan cara kerja penghubungan model Product dengan User!
Dengan menggunakan `django.contrib.auth.models.User`, kita bisa menghubungkan Product dengan User dengan foreign key sehingga setiap produk itu terhubung dengan satu pengguna. Dengan menambahkan kode:

`user = models.ForeignKey(User, on_delete=models.CASCADE)`

kita menunjukkan relasi dari banyak-ke-satu antara Product dengan User.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah proses verifikasi identitas pengguna, yaitu mengecek apakah pengguna benar-benar sesuai dengan data yang diinput dalam suatu form. Contohnya seperti mencocokkan username dan password yang diberikan di database. Django juga menyediakan middleware untuk menyimpan status login sehingga detail login bisa diakses melalui request.user. 

Authorization adalah proses memeriksa hak akses pengguna setelah identitas mereka diverifikasi. Ini menentukan apakah pengguna yang terautentikasi memiliki izin untuk mengakses sumber daya tertentu. Contohnya seperti memeriksa apakah pengguna ini memiliki izin untuk mengedit atau mengubah suatu fitur. Django menggunakan decorators seperti @login_required untuk menambahkan permissions fitur yang bisa diakses pengguna.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan menggunakan mekanisme session. Setiap kali pengguna login, Django membuat ID sesi yang disimpan sebagai cookie pada browser pengguna. Saat pengguna melakukan request, cookie ini dikirimkan kembali ke server, memungkinkan Django mengenali pengguna yang sedang login. Informasi ini bisa diakses melalui request.user. Maka, Django dapat melacak dan mengelola sesi pengguna yang telah login.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Saya menghubungkan Product dengan User dengan membuat ForeignKey sehingga setiap Product terkait dengan User tertentu.
- Saya melakukan makemigrations dan migrate untuk membuat tabel database.
- Mengimplementasikan login logout dengan sistem autentikasi Django dengan decorator @login_required
- Memastikan agar pengguna yang login bisa dikenali di seluruh halaman melalui request.user.

### Tugas 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Jika ada beberapa CSS selector yang diterapkan pada elemen yang sama, prioritas ditentukan oleh spesifisitasnya. Selector ID (#) memiliki prioritas tertinggi, diikuti oleh class (.) dan kemudian elemen HTML biasa. Jika dua selector memiliki spesifisitas yang sama, urutan penulisan dalam CSS juga berpengaruh, di mana selector yang ditulis terakhir akan diterapkan.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design memastikan tampilan dan fungsi aplikasi web tetap optimal di berbagai perangkat dan ukuran layar, baik di desktop maupun perangkat mobile. Hal ini penting untuk meningkatkan user experience dan aksesibilitas. Contoh aplikasi yang sudah menerapkan responsive design adalah YouTube, sementara beberapa situs web lama yang hanya didesain untuk desktop belum sepenuhnya responsive.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin adalah jarak luar elemen yang memisahkan elemen tersebut dari elemen lain, border adalah garis pembatas yang mengelilingi elemen, sedangkan padding adalah ruang di dalam elemen antara konten dan border. Ketiga elemen ini bisa diatur secara terpisah menggunakan properti CSS untuk memperbaiki tata letak halaman.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox adalah layout satu dimensi yang memungkinkan elemen diatur secara fleksibel dalam baris atau kolom, memudahkan penyesuaian tata letak pada berbagai ukuran layar. Grid layout adalah layout dua dimensi yang memungkinkan elemen disusun dalam baris dan kolom secara bersamaan, berguna untuk tata letak yang lebih kompleks dan terstruktur.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Saya membuat navigation bar yang isinya adalah logout, home, see products, dan hello "username"
- Saya menambahkan functions pada views.py untuk delete_product, edit_product, dan sebagainya serta menghubungkannya dengan url tertentu di urls.py
- Membuat template html dengan tailwind.
- Melakukan git push dan deploy

### Tugas 6
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

Dalam pengembangan aplikasi berbasis web, JavaScript memungkinkan pengembangan website lebih interaktif dengan konten dinamis yang memperbarui tanpa reload, seperti pada Google Maps. JavaScript juga biasanya dijalankan di sisi client/browser sehingga dapat memproses data langsung di komputer user tanpa harus mengirimkan kembali ke server. JavaScript juga mendukung validasi input pengguna di browser sebelum data dikirimkan ke server sehingga mengurangi beban server. JavaScript juga mendukung penggunaan AJAX (*Asynchronous JavaScript dan XML*) yang membuat aplikasi web memuat data dari server tanpa harus *reload* ulang seluruh halaman. Selain itu, JavaScript dapat digunakan untuk aplikasi mobile, game berbasis web, dan menjalankan server dengan Node.js. Ini membuatnya fleksibel, ringan di server, serta didukung komunitas aktif​.

Sumber: https://www.niagahoster.co.id/blog/javascript-adalah/

2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

`await` dalam penggunaan `fetch()` berfungsi untuk menunggu sampai operasi pengambilan data sudah selesai sebelum melanjutkan eksekusi kode berikutnya. Jika `await` tidak digunakan, maka kode setelah `fetch()` akan berjalan sebelum data berhasil diambil, sehingga bisa saja terjadi akses ke data yang belum tersedia dan memicu error saat memproses data yang belum selesai diambil.

3. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST?

Decorator csrf_exempt digunakan untuk menonaktifkan mekanisme CSRF (Cross-Site Request Forgery) pada view tertentu, misalnya pada AJAX POST. Secara default, Django mewajibkan setiap permintaan POST untuk menyertakan token CSRF demi alasan keamanan. Namun, untuk endpoint tertentu yang tidak membutuhkan verifikasi CSRF (seperti API yang diakses melalui AJAX), decorator ini dapat diterapkan untuk menghindari error dan memungkinkan permintaan AJAX POST berjalan tanpa token CSRF.

Sumber: https://docs.djangoproject.com/id/5.1/howto/csrf/

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Pembersihan data input pengguna tidak hanya dilakukan pada frontend karena validasi input di frontend mudah dihindari dan dimanipulasi oleh user, contohnya seperti menonaktifkan JavaScript. Maka dari itu, dilakukanlah validasi input di backend yang lebih aman karena backend adalah tempat kontrol penuh yang dapat mencegah data berbahaya atau tidak valid masuk ke sistem. Backend juga dapat memberikan perlindungan dari serangan seperti XSS (*Cross-Site Scripting*) yang dilakukan pada tutorial.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Menambahkan @csrf_exempt dalam views.py untuk function `add_product_entry_ajax` untuk menghindari masalah token CSRF pada POST.
- Mempersiapkan template HTML seperti pada tutorial 5 dimana kita membuat button yang akan mengirimkan data input ProductForm menggunakan AJAX.
- Menggunakan event klik, `fetch()` dan `await` untuk mengirimkan data ke backend dan menunggu.
- Menambahkan pembersihan dengan `strip_tags` pada views.py ke function `add_product_entry_ajax()` agar bisa melindungi dari input yang menghasilkan XSS.
- Menambahkan function-function di <script> main.html agar dapat menambahkan produk, refresh halaman, dan lainnya.