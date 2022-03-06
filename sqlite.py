import sqlite3

conn = sqlite3.connect('photo.db')

# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

# テーブルの作成
cur.execute(
    'select max(genre_num) from photos'
)
genre_list = cur.fetchone()
genre_id = genre_list[0]
for i in range(genre_id):
    sql_str = f'select * from photos where genre_num = {genre_id}'
    cur.execute(sql_str)
    photo_list = cur.fetchall()
    print(photo_list)
    


conn.close()
