"""Web Routes."""

from masonite.routes import Get, Post, Put, Patch, Delete, RouteGroup

from app.http.controllers.PdfController import PdfController

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    RouteGroup([
        Get('/index', PdfController.index),
        Get('/create', PdfController.create),
        Post('/store', PdfController.store),
        Get('/download/@filename', PdfController.show),
    ], prefix='/pdfs', name='pdfs.')
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show').name('login'),
    Get().route('/logout', 'LoginController@logout').name('logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show').name('register'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show').name('home'),
    Get().route('/email/verify', 'ConfirmController@verify_show').name('verify'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    Get().route('/password', 'PasswordController@forget').name('forgot.password'),
    Post().route('/password', 'PasswordController@send'),
    Get().route('/password/@token/reset', 'PasswordController@reset').name('password.reset'),
    Post().route('/password/@token/reset', 'PasswordController@update'),
]
