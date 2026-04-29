from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthorizationLocators
from data import Urls, UserData

#4. Login пользователя
class TestLogin:
    def test_user_login(self, driver):
        wait = WebDriverWait(driver, 10)
    
        driver.get(Urls.BASE_URL)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthorizationLocators.ENTER_FORM))

        wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.EMAIL_INPUT)).send_keys(UserData.VALID_EMAIL)
        driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*AuthorizationLocators.ENTER_BUTTON).click()

        avatar = wait.until(EC.visibility_of_element_located(AuthorizationLocators.USER_AVATAR))
    
        assert avatar.is_displayed()
        assert "User" in avatar.text
        assert driver.find_element(*AuthorizationLocators.POST_AD_BUTTON).is_displayed()


    #5. Logout пользователя
    def test_user_logout(self, driver):
        wait = WebDriverWait(driver, 10)
    
        driver.get(Urls.BASE_URL)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthorizationLocators.ENTER_FORM))

        wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.EMAIL_INPUT)).send_keys(UserData.VALID_EMAIL)
        driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*AuthorizationLocators.ENTER_BUTTON).click()

        avatar = wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.USER_AVATAR))
        assert avatar.is_displayed()
    
        driver.find_element(*AuthorizationLocators.EXIT_BUTTON).click()
        wait.until(EC.invisibility_of_element_located(AuthorizationLocators.USER_AVATAR))

        avatars = driver.find_elements(*AuthorizationLocators.USER_AVATAR)
        assert len(avatars) == 0
   
        login_button = wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.LOGIN_BUTTON))
        assert login_button.is_displayed()
    
        post_button = driver.find_element(*AuthorizationLocators.POST_AD_BUTTON)
        assert post_button.is_displayed()
    