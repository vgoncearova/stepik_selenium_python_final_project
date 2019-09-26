__author__ = "victoria"

from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "id_login-password")
    LOGIN_REDIRECT = (By.CSS_SELECTOR, "#id_login-redirect_url")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, '[name="login_submit"]')

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')
