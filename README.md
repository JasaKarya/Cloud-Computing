Untuk membuat API Documentation pada `README.md`, Anda perlu menjelaskan endpoint-endpoint yang telah Anda buat, metode HTTP yang digunakan, serta format respons yang dihasilkan. Berikut adalah contoh dokumentasi untuk API yang Anda berikan:

---

# API Documentation for app.py

## Deskripsi

API ini menyediakan fungsi dasar untuk mengelola data pengguna dengan beberapa operasi CRUD (Create, Read, Update, Delete).

## Base URL

Semua endpoint dapat diakses melalui base URL berikut:

```
http://localhost:5000
```

## Endpoint

### 1. **GET Data Pengguna**

Mengambil semua data pengguna yang tersimpan.

- **URL**
  ```
  /api
  ```

- **Metode HTTP**
  ```
  GET
  ```

- **Response**
  ```json
  {
      "msg": "Query data sukses",
      "code": 200,
      "data": [
          {
              "id": 1,
              "nama": "John Doe",
              "umur": 25,
              "alamat": "123 Jalan ABC"
          },
          ...
      ]
  }
  ```

### 2. **Tambah Data Pengguna**

Menambahkan data pengguna baru.

- **URL**
  ```
  /api
  ```

- **Metode HTTP**
  ```
  POST
  ```

- **Form Data**
  ```
  nama: [string],
  umur: [integer],
  alamat: [string]
  ```

- **Response**
  ```json
  {
      "msg": "Data berhasil dimasukkan",
      "code": 200
  }
  ```

### 3. **Edit Data Pengguna**

Mengubah data pengguna berdasarkan ID.

- **URL**
  ```
  /api/<id>
  ```

- **Metode HTTP**
  ```
  PUT
  ```

- **URL Parameters**
  ```
  id: [integer]
  ```

- **Form Data**
  ```
  nama: [string],
  umur: [integer],
  alamat: [string]
  ```

- **Response**
  ```json
  {
      "msg": "Edit Data Berhasil",
      "code": 200
  }
  ```

### 4. **Hapus Data Pengguna**

Menghapus data pengguna berdasarkan ID.

- **URL**
  ```
  /api/<id>
  ```

- **Metode HTTP**
  ```
  DELETE
  ```

- **URL Parameters**
  ```
  id: [integer]
  ```

- **Response**
  ```json
  {
      "msg": "Delete Data Berhasil",
      "code": 200
  }
  ```

---

Dengan dokumentasi di atas, pengguna dapat memahami bagaimana cara menggunakan API saya, termasuk endpoint yang tersedia, metode yang digunakan, serta format respons yang dihasilkan.



# API Documentation for auth.py

Dokumentasi ini menjelaskan tentang API yang telah dibuat dengan menggunakan Flask. API ini memiliki beberapa endpoint yang memungkinkan pengguna untuk login, mengakses halaman dashboard yang memerlukan autentikasi, dan mengakses halaman umum.

## Endpoint

### 1. Login

- **Metode:** POST
- **URL:** `/api/login`
- **Deskripsi:** Endpoint ini digunakan untuk proses login pengguna.
  
#### Parameter Body:

| Parameter  | Deskripsi        |
|------------|------------------|
| `username` | Username pengguna|
| `password` | Kata sandi       |

#### Respon:

- Jika login berhasil:
  ```json
  {
      "token": "TOKEN_JWT",
      "msg": "Anda berhasil login !"
  }
  ```

- Jika login gagal:
  ```json
  {
      "msg": "Silahkan login !"
  }
  ```

### 2. Dashboard

- **Metode:** GET
- **URL:** `/api/dashboard`
- **Deskripsi:** Endpoint ini merupakan halaman dashboard yang memerlukan autentikasi.

#### Respon:

- Jika pengguna telah login:
  ```json
  {
      "msg": "ini adalah halaman dashboard, butuh login untuk mengaksesnya"
  }
  ```

### 3. Halaman Umum

- **Metode:** GET
- **URL:** `/api`
- **Deskripsi:** Endpoint ini merupakan halaman umum yang dapat diakses oleh semua pengguna.

#### Respon:

- ```json
  {
      "msg": "ini adalah halaman umum/public"
  }
  ```
