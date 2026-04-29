from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthorizationLocators
from data import Urls, UserData
from helpers import Helpers


class TestRegistration:

    #1. Регистрация пользователя
    def test_registration(self, driver):
        wait = WebDriverWait(driver, 10)
        unique_email = Helpers.generate_unique_email()
    
        driver.get(Urls.BASE_URL)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthorizationLocators.ENTER_FORM))
        driver.find_element(*AuthorizationLocators.REGISTRATION_BUTTON).click()
    
        wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.EMAIL_INPUT)).send_keys(unique_email)
        driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*AuthorizationLocators.SUBMIT_PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()
    
        avatar = wait.until(EC.visibility_of_element_located(AuthorizationLocators.USER_AVATAR))
    
        assert avatar.is_displayed()
        assert "User" in avatar.text
        assert driver.find_element(*AuthorizationLocators.POST_AD_BUTTON).is_displayed()


    #2. Регистрация пользователя c email не по маске  *******@*******.*** 
    def test_registration_invalid_email(self, driver):
        wait = WebDriverWait(driver, 10)
        invalid_email = "test.test.ru"
    
        driver.get(Urls.BASE_URL)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthorizationLocators.ENTER_FORM))
        driver.find_element(*AuthorizationLocators.REGISTRATION_BUTTON).click()

        email_field = wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.EMAIL_INPUT))
        email_field.send_keys(invalid_email)
    
        driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()

        email_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizationLocators.EMAIL_FIELD_ERROR))
        password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizationLocators.PASSWORD_FIELD_ERROR))
        confirm_password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizationLocators.SUBMIT_PASSWORD_ERROR))

        error = wait.until(EC.visibility_of_element_located(AuthorizationLocators.ERROR_MESSAGE))
        assert error.is_displayed()
        assert email_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert confirm_password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
    
    
    #3. Регистрация уже существующего пользователя
    def test_registering_existing_user(self, driver):
        wait = WebDriverWait(driver, 10)
    
        driver.get(Urls.BASE_URL)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthorizationLocators.ENTER_FORM))
        driver.find_element(*AuthorizationLocators.REGISTRATION_BUTTON).click()
    
        wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.EMAIL_INPUT)).send_keys(UserData.VALID_EMAIL)
        driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*AuthorizationLocators.SUBMIT_PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()
    
        email_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizationLocators.EMAIL_FIELD_ERROR))
        password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizationLocators.PASSWORD_FIELD_ERROR))
        confirm_password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizationLocators.SUBMIT_PASSWORD_ERROR))

        error = wait.until(EC.visibility_of_element_located(AuthorizationLocators.ERROR_MESSAGE))
        assert error.is_displayed()
        assert email_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert confirm_password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        