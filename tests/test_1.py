from playwright.sync_api import Page, expect

BASE_URL = 'https://spring-petclinic-clone-2024.azurewebsites.net/'


def test_1(page: Page):
    page.goto(BASE_URL)
    assert page.inner_text('h2') == 'Welcome'
