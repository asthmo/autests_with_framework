from selene.browser import open_url
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s

class KinopoiskSearchPage:
    def __init__(self):
        self.input_film_title = s('input#find_film')
        self.select_country = s('select#country')
        self.select_genre = s('select#m_act[genre]')
        self.submit = s('input.nice_button')

        self.film_title = s('p.name')

    def open(self):
        open_url('https://www.kinopoisk.ru/s/')
        return self