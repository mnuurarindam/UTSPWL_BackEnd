from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes')
        
        # Ini menambahkan rute untuk produk
        config.add_route('get_products', '/get/products', request_method='GET')
        config.add_route('add_product', '/add/product', request_method='POST')
        config.add_route('get_product_specific', '/get/product/{id}', request_method='GET')
        config.add_route('delete_product', '/delete/product/{id}', request_method='DELETE')
        config.add_route('update_product', '/update/product/{id}', request_method='PUT')
        
        # Ini menambahkan rute untuk user_register
        config.add_route('get_users', '/get/users', request_method='GET')
        config.add_route('add_user', '/add/user', request_method='POST')
        config.add_route('get_user_specific', '/get/user/{id}', request_method='GET')
        config.add_route('delete_user', '/delete/user/{id}', request_method='DELETE')
        config.add_route('update_user', '/update/user/{id}', request_method='PUT')
        
        # Ini menambahkan rute untuk user_login
        config.add_route('login', '/login', request_method='POST')
        
        config.scan('.views')
    return config.make_wsgi_app()
