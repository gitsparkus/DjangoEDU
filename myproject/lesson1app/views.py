from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)

def index(request):

    logger.info('Открыта главная страница')

    html = """
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Мой первый сайт на джанге</title>
    </head>
    <body>
    <nav>
        <div class="pl-4 row">
        <p>Это главная страница без дизайна</p>
        </div>
        <a href="/about">О себе</a>
        <hr>
    </nav>
    <section>
        Страница не заполнена
    </section>
    <footer>
        <hr/>
        Все права правильные
    </footer>
    </body>
    </html>
    """

    return HttpResponse(html)


def about(request):

    logger.info('Открыта страница about')

    html = """
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Мой первый сайт на джанге</title>
    </head>
    <body>
    <nav>
        <div class="pl-4 row">
        <p>Это страница про автора тоже без дизайна</p>
        </div>
        <a href="/">На главную</a>
        <hr>
    </nav>
    <section>
        Страница об авторе этого сайта пока не заполнена
    </section>
    <footer>
        <hr/>
        Все права правильные
    </footer>
    </body>
    </html>
    """

    return HttpResponse(html)
