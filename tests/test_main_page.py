import pytest
from qaseio.pytest import qase
from api.api_main_page import ApiMainPage
from base.asserts import Asserts


@pytest.mark.prod_web
@pytest.mark.master_web
@qase.layer("api")
class TestMainPage:

    @qase.id(0)
    @qase.title("Get main page")
    @qase.description("Get request for main page")
    @qase.severity("normal")
    def test_get_main_page(self, base_url):
        with qase.step("Step 1. Sending GET for main page", "Code: 200"):
            response = ApiMainPage.get_main_page(url=base_url)

            Asserts.status_code(response, 200)

        with qase.step("Step 2. Sending GET for UZ local", "Code: 200"):
            response = ApiMainPage.get_uz_local(url=base_url)

            Asserts.status_code(response, 200)

        with qase.step("Step 3. Sending GET for RU local", "Code: 200"):
            response = ApiMainPage.get_ru_local(url=base_url)

            Asserts.status_code(response, 200)
