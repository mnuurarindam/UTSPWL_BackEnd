import jwt
from pyramid.view import view_config
from pyramid.response import Response
from passlib.hash import pbkdf2_sha256
from pyramid.httpexceptions import HTTPNotFound
import pymysql

# Validasi data produk
def validate_product(request):
    data = request.json_body
    if not isinstance(data.get('nama'), str) or not isinstance(data.get('harga'), int):
        request.response.status = 400
        return {'error': 'Invalid data type'}

# Validasi data pengguna
def validate_user(request):
    data = request.json_body
    if not isinstance(data.get('email'), str) or not isinstance(data.get('password'), str):
        request.response.status = 400
        return {'error': 'Invalid data type'}

@view_config(route_name='get_products', request_method='GET', renderer='json')
def get_products(request):
    conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
    cursor = conn.cursor()

    select_query = "SELECT * FROM produk"
    cursor.execute(select_query)
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return {'products': products}

@view_config(route_name='add_product', request_method='POST', renderer='json')
def add_product(request):
    validation_result = validate_product(request)
    if validation_result:
        return validation_result

    conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
    cursor = conn.cursor()

    data = request.json_body
    insert_query = """
    INSERT INTO produk (nama, harga) VALUES (%s, %s)
    """
    cursor.execute(insert_query, (data['nama'], data['harga']))
    conn.commit()

    cursor.close()
    conn.close()

    return {'status': 'success', 'product': {'nama': data['nama'], 'harga': data['harga']}}

@view_config(route_name='get_product_specific', request_method='GET', renderer='json')
def get_product_specific(request):
    conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
    cursor = conn.cursor()

    product_id = int(request.matchdict['id'])
    select_query = "SELECT * FROM produk WHERE id = %s"
    import pymysql
    from pyramid.view import view_config
    from passlib.hash import pbkdf2_sha256

    @view_config(route_name='get_product', request_method='GET', renderer='json')
    def get_product(request):
        conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
        cursor = conn.cursor()

        product_id = int(request.matchdict['id'])
        select_query = "SELECT * FROM produk WHERE id = %s"
        cursor.execute(select_query, (product_id,))
        product = cursor.fetchone()

        cursor.close()
        conn.close()

        return {'product': product}

    @view_config(route_name='delete_product', request_method='DELETE', renderer='json')
    def delete_product(request):
        conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
        cursor = conn.cursor()

        product_id = int(request.matchdict['id'])
        delete_query = "DELETE FROM produk WHERE id = %s"
        cursor.execute(delete_query, (product_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return {'status': 'deleted', 'id': product_id}

    @view_config(route_name='update_product', request_method='PUT', renderer='json')
    def update_product(request):
        conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
        cursor = conn.cursor()

        product_id = int(request.matchdict['id'])
        updated_data = request.json_body

        update_query = """
        UPDATE produk
        SET nama = %s, harga = %s
        WHERE id = %s
        """
        cursor.execute(update_query, (updated_data['nama'], updated_data['harga'], product_id))
        conn.commit()

        cursor.close()
        conn.close()

        return {'status': 'updated', 'product': {'nama': updated_data['nama'], 'harga': updated_data['harga']}}

    @view_config(route_name='register_user', request_method='POST', renderer='json')
    def register_user(request):
        conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
        cursor = conn.cursor()

        data = request.json_body
        hashed_password = pbkdf2_sha256.hash(data['password'])
        insert_query = """
        INSERT INTO user_register (nama, email, password, confirm_password) VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (data['nama'], data['email'], hashed_password, hashed_password))
        conn.commit()

        cursor.close()
        conn.close()

        return {'status': 'success', 'user': {'nama': data['nama'], 'email': data['email']}}

    @view_config(route_name='get_user_specific', request_method='GET', renderer='json')
    def get_user_specific(request):
        conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
        cursor = conn.cursor()

        user_id = int(request.matchdict['id'])
        select_query = "SELECT * FROM user_register WHERE id = %s"
        cursor.execute(select_query, (user_id,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return {'user': user}

    @view_config(route_name='delete_user', request_method='DELETE', renderer='json')
    def delete_user(request):
        conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
        cursor = conn.cursor()

        user_id = int(request.matchdict['id'])
        delete_query = "DELETE FROM user_register WHERE id = %s"
        cursor.execute(delete_query, (user_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return {'status': 'deleted', 'id': user_id}

    @view_config(route_name='update_user', request_method='PUT', renderer='json')
    def update_user(request):
        conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
        cursor = conn.cursor()

        user_id = int(request.matchdict['id'])
        updated_data = request.json_body

        update_query = """
        UPDATE user_register
        SET nama = %s, email = %s, password = %s, confirm_password = %s
        WHERE id = %s
        """
        cursor.execute(update_query, (updated_data['nama'], updated_data['email'], pbkdf2_sha256.hash(updated_data['password']), pbkdf2_sha256.hash(updated_data['confirm_password']), user_id))
        conn.commit()

        cursor.close()
        conn.close()

        return {'status': 'updated', 'user': {'nama': updated_data['nama'], 'email': updated_data['email']}}

    @view_config(route_name='login', request_method='POST', renderer='json')
    def login(request):
        data = request.json_body
        email = data.get('email')
        password = data.get('password')

        conn = pymysql.connect(host='localhost', user='root', password='', db='utspwl_lbwk')
        cursor = conn.cursor()

        select_query = "SELECT id, password FROM user_register WHERE email = %s"
        cursor.execute(select_query, (email,))
        user = cursor.fetchone()

        if not user:
            cursor.close()
            conn.close()
            return {'error': 'Invalid email or password'}
        else:
            user_id, hashed_password = user
            if pbkdf2_sha256.verify(password, hashed_password):
                cursor.close()
                conn.close()
                return {'user_id': user_id}
            else:
                cursor.close()
                conn.close()
                return {'error': 'Invalid email or password'}
