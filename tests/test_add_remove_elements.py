from playwright.sync_api import Page, expect
import random


def test_has_title(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    expect(page.locator("h3")).to_have_text("Add/Remove Elements")

def test_add_element(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    page.get_by_role("button", name="Add Element").click()
    expect(page.get_by_role("button", name="Delete")).to_have_count(1)

def test_remove_element(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    page.get_by_role("button", name="Add Element").click()
    expect(page.get_by_role("button", name="Delete")).to_have_count(1)
    page.get_by_role("button", name="Delete").click()
    expect(page.get_by_role("button", name="Delete")).to_have_count(0)

def test_add_remove_element_many(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    value = random.randint(2,5)
    count = 0
    for _ in range(1, 1 + value):
        page.get_by_role("button", name="Add Element").click()
        count = count + 1
        expect(page.get_by_role("button", name="Delete")).to_have_count(count)

    count = 0
    for _ in range(1, 1 + value):
        page.get_by_role("button", name="Delete").nth(0).click()
        count = count + 1
        expect(page.get_by_role("button", name="Delete")).to_have_count(value-count)

    expect(page.get_by_role("button", name="Add Element")).to_have_count(1)
    expect(page.get_by_role("button", name="Delete")).to_have_count(0)