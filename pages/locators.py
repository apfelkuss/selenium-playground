from selenium.webdriver.common.by import By


class BasePageLocators:
    
    SEARCH_BAR = (By.ID, "SearchText")
    SEARCH_BUTTON = (By.CLASS_NAME, "eMainSearchBlock_ButtonWrap")
    MY_OZON = (By.CLASS_NAME, "ePanelLinks_Label")
    HOME = (By.CSS_SELECTOR, "[itemprop='logo']")
    

class HomePageLocators:
    
    LOGIN_PANEL = (By.CSS_SELECTOR, "[class='ePanelLinks_term jsOption  jsClearTilesFromStorage jsLoginPanel jsBottomPart']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class='bFlatButton mMedium jsLoginWindowButton']")
    LOGIN_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "Password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[class='eLoginWindow_registerButton jsRegister']")
    
    
class SearchResultsLocators:
    
    ITEMS = (By.CSS_SELECTOR, "[class='eOneTile_tileLink jsUpdateLink']") 
    SORTING_DROPDOWN_MENU = (By.CSS_SELECTOR, "[class='bFacetSorting jsFacetSorting'") 


class ItemPageLocators:
    
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "eSaleBlock_buttons")
    PLUS_ONE_BUTTON = (By.CSS_SELECTOR, "[class='bSaleBlockButton mPlusOne jsAddOneItem']")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "[class='bSaleBlockButton mTwoLines mActive']")


class CartPageLocators:
    
    REMOVE_ALL = (By.CSS_SELECTOR, "[class='bIconButton mRemove mGray jsRemoveAll']")
    RESTORE_ALL = (By.CSS_SELECTOR, "[class='bIconButton mRestore mGray jsRestoreAll']")
    PLUS_ONE = (By.CSS_SELECTOR, "[class='eCartCount_button mPlus jsPlus ']")
    MINUS_ONE = (By.CSS_SELECTOR, "[class='eCartCount_button mMinus jsMinus']")
    ITEM_QUANTITY = (By.CSS_SELECTOR, "[class='bTextInput jsInputField']")
    TOTAL_QUANTITY = (By.CLASS_NAME, "eCartTotal_infoCount")


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
    

class LoggedInPageLocators:
    
    LOG_OFF = (By.CSS_SELECTOR, "[class='ePanelLinks_term jsOption  jsClearTilesFromStorage jsLogOff jsBottomPart']")
