from flask import Flask, jsonify, request
from tinydb import TinyDB, Query, where
from re import match

app = Flask(__name__)
db = TinyDB('db.json')
table = db.table('table_eCom')


@app.route('/get_form', methods=['POST'])
def index():
    # get data from post request and validation
    data = request.form
    data_dict = {}
    for key, value in data.items():
        if match(r'^[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])$', value) or \
                match(r'(0[1-9]|1[0-9]|2[0-9]|3[01]).(0[1-9]|1[012]).[0-9]{4}$', value):
            data_dict[key] = 'date'
        elif match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', value):
            data_dict[key] = 'phone'
        elif match(r'^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$', value):
            data_dict[key] = 'email'
        elif value == 'name_form':
            pass
        else:
            data_dict[key] = 'text'

    # form check
    for row in table:
        for key, value in data_dict.items():
            if key in row and value == row[key]:
                check = True
            else:
                check = False
                break
        if check:
            name_form = row['name_form']
            return jsonify({'name_form': name_form})
    return jsonify(data_dict)


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', debug=True, port=12332, use_reloader=True)
