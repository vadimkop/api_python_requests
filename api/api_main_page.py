from base.base_methods import BaseMethods


class ApiMainPage:

    @staticmethod
    def get_main_page(url):
        return BaseMethods.get_method(url)
