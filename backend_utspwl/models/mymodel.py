# from tugaspwl4 import db_connect
import pymysql

def init_db():
    conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE user_login (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
    """)
    cursor.execute("""
    CREATE TABLE user_register (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        confirm_password VARCHAR(255) NOT NULL
    );
""")
    cursor.execute("""
    CREATE TABLE produk (
        id INT AUTO_INCREMENT PRIMARY KEY,
        gambar VARCHAR(255) NOT NULL,
        nama VARCHAR(255) NOT NULL,
        harga INT (255) NOT NULL
    );
""")
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    init_db()