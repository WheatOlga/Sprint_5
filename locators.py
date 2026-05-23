from selenium.webdriver.common.by import By

class AuthorizationLocators:
    LOGIN_BUTTON = By.XPATH, '//*[text()="Вход и регистрация"]'
    ENTER_FORM = By.XPATH, '//form[.//h1[text()="Войти"]]'
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'
    REGISTRATION_BUTTON = By.XPATH, '//*[text()="Нет аккаунта"]'
    CREATE_ACCOUNT_BUTTON = By.XPATH, '//*[text()="Создать аккаунт"]'
    HAVE_ACCOUNT = By.XPATH, '//*[text()="Уже есть аккаунт"]'
    EXIT_BUTTON = By.XPATH, '//*[text()="Выйти"]'
    
    EMAIL_INPUT = By.XPATH, '//input[@name="email"]' 
    PASSWORD_INPUT = By.XPATH, '//input[@name="password"]'
    SUBMIT_PASSWORD_INPUT = By.XPATH,  '//input[@name="submitPassword"]'

    ERROR_MESSAGE = By.XPATH, '//*[text()="Ошибка"]'

    USER_AVATAR = By.CLASS_NAME, "profileText.name"
    POST_AD_BUTTON = By.XPATH, '//*[text()="Разместить объявление"]'
    MODAL_WINDOW = By.CLASS_NAME, "popUp_shell__LuyqR"
    AUTHORIZATION_TEXT = By.XPATH, '//*[text()="Чтобы разместить объявление, авторизуйтесь"]'

    EMAIL_FIELD_ERROR = By.XPATH, "(//div[contains(@class, 'input_inputError__fLUP9')])"
    PASSWORD_FIELD_ERROR = By.XPATH, "(//div[contains(@class, 'input_inputError__fLUP9')])"
    SUBMIT_PASSWORD_ERROR = By.XPATH, "(//div[contains(@class, 'input_inputError__fLUP9')])"

class NewAd:
    NAME_AD = By.XPATH, '//input[@name="name"]'
    DESCRIPTION_AD = By.XPATH, '//textarea[@name="description"]'
    PRICE_AD = By.XPATH, '//input[@name="price"]'
    DROPDOWN_CATEGORIES = By.XPATH, '//input[@name="category"]/following-sibling::button[contains(@class, "dropDownMenu_arrowDown__pfGL1")]'
    SELECT_CATEGORIES = By.XPATH, "//span[text()='Садоводство']"
    DROPDOWN_CITY = By.XPATH, '//input[@name="city"]/following-sibling::button[contains(@class, "dropDownMenu_arrowDown__pfGL1")]'
    SELECT_CITY = By.XPATH, "//span[text()='Новосибирск']"
    RADIO_BUTTON = By.XPATH, '//input[@type="radio" and @value="Б/У"]'
    SUBMIT_BUTTON = By.XPATH, '//*[text()="Опубликовать"]'
    USER_BUTTON = By.XPATH, '//*[@class="circleSmall"]'

class UserProfile:    
    MY_PROFILE = By.XPATH, '//*[text()="Мой профиль"]'
    TEST_NAME_AD = By.XPATH, "//h2[text()='Фикус Сибирский']"