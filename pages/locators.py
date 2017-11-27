from selenium.webdriver.common.by import By


class BasePageLocators:
    
    SEARCH_BAR = (By.ID, "SearchText")
    SEARCH_BUTTON = (By.CLASS_NAME, "eMainSearchBlock_ButtonWrap")
    MY_OZON = (By.CLASS_NAME, "ePanelLinks_Label")
    HOME = (By.CSS_SELECTOR, "[itemprop='logo']")


class GuestPageLocators:
    
    LOG_IN_PANEL = (By.CSS_SELECTOR,"[class*='jsLoginPanel']")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[class='bFlatButton mMedium jsLoginWindowButton']")
    LOGIN_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "Password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[class='eLoginWindow_registerButton jsRegister']")


class SearchResultsPageLocators:

    ITEMS = (By.CLASS_NAME, "bOneTile")
    SORTING_DROPDOWN_MENU = (By.CLASS_NAME, "bFacetSorting")
    SORT_BY_POPULARITY = (By.CSS_SELECTOR, "[class*=Select_Item][data-value=bests]")
    SORT_BY_NEWNESS = (By.CSS_SELECTOR, "[class*=Select_Item][data-value=new]")
    SORT_BY_RATING = (By.CSS_SELECTOR, "[class*=Select_Item][data-value=rate]")
    SORT_BY_PRICE = (By.CSS_SELECTOR, "[class*=Select_Item][data-value=price]")
    SORT_BY_PRICE_DESC = (By.CSS_SELECTOR, "[class*=Select_Item][data-value=price_rev]")


class ItemPageLocators:

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "eSaleBlock_buttons")
    PLUS_ONE_BUTTON = (By.CSS_SELECTOR, "[class='bSaleBlockButton mPlusOne jsAddOneItem']")
    PLUS_ONE_BUTTON = (By.CSS_SELECTOR, "[class*='bSaleBlockButton mPlusOne']")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "[class*='bSaleBlockButton mTwoLines']")
    IMAGES = (By.CLASS_NAME, "eMicroGallery_fullWrap")


class CartPageLocators:

    REMOVE_ALL = (By.CSS_SELECTOR, "[class='bIconButton mRemove mGray jsRemoveAll']")
    RESTORE_ALL = (By.CSS_SELECTOR, "[class='bIconButton mRestore mGray jsRestoreAll']")
    PLUS_ONE = (By.CSS_SELECTOR, "[class='eCartCount_button mPlus jsPlus ']")
    MINUS_ONE = (By.CSS_SELECTOR, "[class='eCartCount_button mMinus jsMinus']")
    ITEM_QUANTITY = (By.CSS_SELECTOR, "[class='bTextInput jsInputField']")
    TOTAL_QUANTITY = (By.CLASS_NAME, "eCartTotal_infoCount")
    LOADING_INDICATOR = (By.CLASS_NAME, "bCartPage mBlockActions")


class RegistrationPageLocators:

    FIRST_NAME = (By.ID, "PageFooter_ctl01_FirstName")
    LAST_NAME = (By.ID, "PageFooter_ctl01_LastName")
    EMAIL = (By.ID, "PageFooter_ctl01_EMail")
    PASSWORD = (By.ID, "PageFooter_ctl01_Password")
    CONFIRM_PASSWORD = (By.ID, "PageFooter_ctl01_ConfirmPassword")
    SUBSCRIPTION = (By.ID, "ActionSubscription")
    CAPABILITY_CONFIRMATION = (By.ID, "PageFooter_ctl01_CapabilityConfirmation")
    PRIVATE_INDIVIDUAL = (By.ID, "PageFooter_ctl01_PrivateIndividualRadioButton")
    LEGAL_PERSON = (By.ID, "PageFooter_ctl01_LegalPersonRadioButton")
    REGISTRATION_BUTTON = (By.ID, "PageFooter_ctl01_Registration")


class UserPageLocators:
    LOG_OFF_BUTTON = (By.CSS_SELECTOR, "[class*='jsLogOff']")
