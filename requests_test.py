import requests

url_request = "http://0.0.0.0:12332/get_form"
# UserRegistrationForm
# standartnaya forma
data_user = {'date_create': '2017-10-11', 'email_user': 'user@gmail.com',
             'about_user': 'some text about user', 'phone_user': '+74995069928'}
a = requests.post(url_request, data=data_user)
print('1', a.text)

# data drugogo vida
data_user_changed = {'date_create': '11.12.2018', 'email_user': 'user@gmail.com',
                     'about_user': 'some text about user2', 'phone_user': '+74995069928'}
b = requests.post(url_request, data=data_user_changed)
print('2', b.text)

# CreatePostForm
# otlichaetsya imenem odnogo polya ot UserRegistrationForm
data_post = {'date_create': '2015-11-03', 'email_user': 'email@email.kz',
             'post_text': 'some text in post', 'phone_user': '+74995069928'}
c = requests.post(url_request, data=data_post)
print('3', c.text)

# OrderForm
data_order = {'order_date': '01.01.1999', 'email_customer': 'customer123@gmail.com',
              'order_text': 'some order text', 'phone_customer': '+74911111111'}
d = requests.post(url_request, data=data_order)
print('4', d.text)

# polei menshe shem v forme
data_worker = {'birthday_date': '01.01.1950', 'worker_email': 'worker@mail.ru', 'about_worker': 'some about worker', }
f = requests.post(url_request, data=data_worker)
print('5', f.text)

# net takoi formi
data_empty_form = {'date_bd': '11.12.2018', 'emai_boss': 'totsamy@gmail.com',
                   'some_text': 'privet12312sadasdasda', 'phone_boss': '+74995069928'}
g = requests.post(url_request, data=data_empty_form)
print('6', g.text)
