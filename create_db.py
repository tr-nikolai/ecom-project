from tinydb import TinyDB, Query, where


db = TinyDB('db.json')
table = db.table('table_eCom')


table.insert({'name_form': 'UserRegistrationForm', 'date_create': 'date', 'email_user': 'email',
              'about_user': 'text', 'phone_user': 'phone'})

table.insert({'name_form': 'OrderForm', 'order_date': 'date', 'email_customer': 'email',
             'order_text': 'text', 'phone_customer': 'phone'})

table.insert({'name_form': 'WorkerForm', 'birthday_date': 'date', 'worker_email': 'email', 'about_worker': 'text',
              'worker_phone_1': 'phone', 'worker_phone_2': 'phone'})

table.insert({'name_form': 'CreatePostForm', 'date_create': 'date', 'email_user': 'email',
              'post_text': 'text', 'phone_user': 'phone'})

