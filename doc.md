# Medical Record Service

در این سرویس خدمات نگه داری و ایجاد پرونده پزشکی کلاینت های وب سایت انجام می شود.

## تکنولوژی‌های استفاده شده

- python
- django
- drf
- swagger

## ای‌پی‌آی‌ها

- list medical record
- retrieve medical record
- create medical record

### create record service
با استفاده از این ای پی آی پرونده پزشکی ایجاد می شود

### retrieve record service
بااستفاده از این ای پی آی جزپیات یک پرونده پزشکی اراپه می شود

### list record service
با استفاده از این ای پی آی لیستی از مدارک پزشکی موجود داده می شود

#### ریز مشخصات فنی

OPTIONS /api/records/retrieve_record/1

HTTP 200 OK Allow: GET, HEAD, OPTIONS Content-Type: application/json Vary: Accept


### retrieve record service
#### نحوه‌ی استفاده
```bash
$ curl: (6) Could not resolve host: GET
{"id":1,"user":"یاسمن","data":"1126","create_date_time":"2022-02-22T10:13:49.110947+03:30"}%   
```
#### خروجی مورد انتظار

```json
{
  "name": "Retrieve Record Model",
  "description": "",
  "renders": [
    "application/json",
    "text/html"
  ],
  "parses": [
    "application/json",
    "application/x-www-form-urlencoded",
    "multipart/form-data"
  ]
}
```

### list record service
#### نحوه‌ی استفاده

```bash
$ curl: (6) Could not resolve host: GET
{"count":3,"next":null,"previous":null,"results":[{"id":1,"user":"یاسمن","data":"1126","create_date_time":"2022-02-22T10:13:49.110947+03:30"},{"id":2,"user":"سیمین","data":"0730","create_date_time":"2022-02-22T10:14:14.493795+03:30"},{"id":3,"user":"changiz","data":"1111","create_date_time":"2022-02-22T10:21:52.800648+03:30"}]}%   
```

#### خروجی مورد انتظار

```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": "یاسمن",
            "data": "1126",
            "create_date_time": "2022-02-22T10:13:49.110947+03:30"
        },
        {
            "id": 2,
            "user": "سیمین",
            "data": "0730",
            "create_date_time": "2022-02-22T10:14:14.493795+03:30"
        },
        {
            "id": 3,
            "user": "changiz",
            "data": "1111",
            "create_date_time": "2022-02-22T10:21:52.800648+03:30"
        }
    ]
}
```

### create record service
#### نحوه‌ی استفاده

```bash
$ / curl -X POST -F 'user=test' -F 'data=test' 'http://127.0.0.1:8000/api/records/create_record'
{"id":4,"user":"test","data":"test","create_date_time":"2022-02-22T11:39:06.217166+03:30"}%  
```
#### خروجی مورد انتظار
```json
{
    "id": 5,
    "user": "test",
    "data": "test",
    "create_date_time": "2022-02-22T11:40:47.696499+03:30"
}


```
