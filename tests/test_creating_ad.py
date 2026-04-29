from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthorizationLocators, NewAd, UserProfile
from data import Urls, UserData, CreatingAd

class TestCreateAd:
    #6.Создание объявления неавторизованным пользователе
    def test_creating_ad_unauthorized_user(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get(Urls.BASE_URL)
        driver.find_element(*AuthorizationLocators.POST_AD_BUTTON).click()

        modal_window = wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.MODAL_WINDOW))
        assert modal_window.is_displayed()
    
        authorization_text = wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.AUTHORIZATION_TEXT))
        assert authorization_text.is_displayed()


    #7.Создание объявления авторизованным пользователе
    def test_creating_ad_authorized_user(self, driver):
        wait = WebDriverWait(driver, 10)
    
        driver.get(Urls.BASE_URL)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthorizationLocators.ENTER_FORM))

        wait.until(EC.visibility_of_element_located(
            AuthorizationLocators.EMAIL_INPUT)).send_keys(UserData.VALID_EMAIL)
        driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*AuthorizationLocators.ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthorizationLocators.USER_AVATAR))

        driver.find_element(*AuthorizationLocators.POST_AD_BUTTON).click()
        wait.until(EC.element_to_be_clickable(NewAd.NAME_AD)).send_keys(CreatingAd.NEW_NAME_AD)
        wait.until(EC.element_to_be_clickable(NewAd.DESCRIPTION_AD)).send_keys(CreatingAd.NEW_DESCRIPTION_AD)
        wait.until(EC.element_to_be_clickable(NewAd.PRICE_AD)).send_keys(CreatingAd.NEW_PRICE_AD)

        driver.find_element(*NewAd.DROPDOWN_CATEGORIES).click()
        driver.find_element(*NewAd.SELECT_CATEGORIES).click()
        driver.find_element(*NewAd.DROPDOWN_CITY).click()
        driver.find_element(*NewAd.SELECT_CITY).click()

        radio_button = wait.until(EC.presence_of_element_located(NewAd.RADIO_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView(true);", radio_button)
        driver.execute_script("arguments[0].click();", radio_button)

        driver.find_element(*NewAd.SUBMIT_BUTTON).click()

        try:
            wait.until(EC.invisibility_of_element_located(NewAd.SUBMIT_BUTTON))
        except TimeoutException:
            pass

        wait.until(EC.element_to_be_clickable(NewAd.USER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(UserProfile.MY_PROFILE))

        created_ad_title = wait.until(EC.visibility_of_element_located(UserProfile.TEST_NAME_AD))

        assert CreatingAd.NEW_NAME_AD == created_ad_title.text
