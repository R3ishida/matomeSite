from crypt import methods
from email.policy import default
import os
from re import S
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.sql import func
import sqlite3


UPLOAD_FOLDER = './static/image/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'heic'}

app = Flask(__name__, static_folder='static/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'secret key'

# db作成

"""
cur.execute(
    'CREATE TABLE photos(id INTEGER PRIMARY KEY, user_id INTEGER, genre TEXT, genre_num INTEGER, file_path TEXT, title TEXT, memo TEXT);'
)
"""


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            conn = sqlite3.connect('photo.db')
            cur = conn.cursor()
            cur.execute(
                'select max(id) from photos'
            )
            number_list = cur.fetchone()
            if number_list[0] is None:
                photo_id = 1
            else:
                photo_id = number_list[0] + 1
            new_filename = f"image{photo_id}." + file.filename.rsplit('.', 1)[1]

            filename = secure_filename(new_filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(file_path)
            file.save(file_path)

            genre = "建築"
            genre_num = request.form.get('genre_num')
            title = request.form.get('title')
            memo = request.form.get('memo')
            print("------------------------")
            print(request.form.get('genre_num'))
            user_id = 1
            sql_str = f'insert into photos values({photo_id}, {user_id}, "{genre}", {genre_num}, "{filename}", "{title}", "{memo}")'
            cur.execute(sql_str)
            conn.commit()
           
            cur.execute(
                "select * from photos"
            )
            
            for row in cur:
                print(row)
    
            return redirect('/')
    else:  #getリクエストの時
        conn = sqlite3.connect('photo.db')
        cur = conn.cursor()
        cur.execute(
            'select * from genre'
        )
        genre_list = cur.fetchall()
        print(genre_list)
        genre_id = len(genre_list)
        print(genre_id)
        print("---------------------------")
        photo_list = []
        for i in range(genre_id):
            n = i+1
            print(n)
            sql_str = f'select * from photos where genre_num = {n}'
            cur.execute(sql_str)
            photo_sublist = cur.fetchall()
            gridname = "grid"+str(i+1)
            for j in range(len(photo_sublist)):
                photo_sublist[j] = list(photo_sublist[j])
                link = f"static/image/{photo_sublist[j][4]}"
                print(type(photo_sublist[j]))
                photo_sublist[j].insert(0, gridname)
                photo_sublist[j].append(link)
            photo_list.append(photo_sublist)
        print(photo_list)
            
        
        return render_template("index.html", genres = photo_list, genre_list = genre_list, genre_id = genre_id)

@app.route('/delete_photo', methods=['GET', 'POST'])
def delete_data():
    print("unko!!!!!!!!")
    photo_id = request.form.get('photo_id')
    print(photo_id)
    print("---------------------------------")
    conn = sqlite3.connect('photo.db')
    cur = conn.cursor()
    sql_str = f'select file_path from photos where id = { photo_id }'
    cur.execute(sql_str)
    filename = cur.fetchone()[0]
    sql_str = f'delete from photos where id = { photo_id }'
    cur.execute(sql_str)
    conn.commit()
    new_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    os.remove(new_filename)
    return redirect('/')

@app.route('/add_genre', methods=['GET', 'POST'])
def add_genre():
    genre = request.form.get('genre')
    conn = sqlite3.connect('photo.db')
    cur = conn.cursor()
    sql_str = f'select max(genre_num) from genre'
    cur.execute(sql_str)
    genre_num = cur.fetchone()[0]
    if genre_num != None:
        print("noneではない")
        genre_num += 1
    else:
        print("none")
        genre_num = 1
    print(genre_num, genre)
    sql_str = f'insert into genre values ({ genre_num }, "{ genre }")'
    cur.execute(sql_str)
    conn.commit()
    return redirect('/')

@app.route('/delete_genre', methods=['GET', 'POST'])
def delete_genre():
    genre = request.form.get('genre')
    conn = sqlite3.connect('photo.db')
    cur = conn.cursor()
    sql_str = f'delete from genre where genre = "{ genre }"'
    cur.execute(sql_str)
    conn.commit()
    sql_str = f'delete from photos where genre = "{ genre }"'
    cur.execute(sql_str)
    conn.commit()
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)