from base.base_methods import BaseMethods


class ApiMainPage:

    @staticmethod
    def get_main_page(url):
        return BaseMethods.get_method(url)

    @staticmethod
    def get_uz_local(url):
        return BaseMethods.get_method(f"{url}/uz")

    @staticmethod
    def get_ru_local(url):
        return BaseMethods.get_method(f"{url}/ru")
