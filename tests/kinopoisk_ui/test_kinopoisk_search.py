import allure
import pytest
import time
from framework.ui_pages.search_page import KinopoiskSearchPage


@pytest.mark.usefixtures('allure_screen')
class TestKinopoiskSearchFilm:

    @pytest.mark.usefixtures("close_driver_after_test")
    def test_find_film(self):
        search_page = KinopoiskSearchPage().open()
        time.sleep(10)
