import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    expect(page.locator("h2")).to_have_text("Login Page")

def test_login_success(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator('button[type="submit"]').click()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

def test_login_wrong_username(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("Jack")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator('button[type="submit"]').click()
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")

def test_login_wrong_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("Password")
    page.locator('button[type="submit"]').click()
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

def test_login_empty_all_fields(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").clear()
    page.locator("#password").clear()
    page.locator('button[type="submit"]').click()
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")

def test_login_empty_username(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").clear()
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator('button[type="submit"]').click()
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")

def test_login_empty_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").clear()
    page.locator('button[type="submit"]').click()
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

def test_login_sql_injection_passowrd(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("' OR '1'='1")
    page.locator('button[type="submit"]').click()
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")
