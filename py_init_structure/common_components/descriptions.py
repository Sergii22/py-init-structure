from enum import Enum


class Descriptions(Enum):
    CONFIG_EXAMPLE = """# store here all  environment variables. Refer to example below: here is var USERNAME that
        # could be loaded from
        # .env file, or John will be used as a default one
        # import os
        # from os.path import join, dirname
        # from dotenv import load_dotenv
        
        # dotenv_path = join(dirname(__file__), ".env")
        # load_dotenv(dotenv_path)
        
        # USERNAME = os.environ.get("USERNAME", "John")
    """

    BASE_POPUP_EXAMPLE = """# Store here common locators and methods for popups of target APP to build Page Object
            # structure. 
            # From this class, all other popups classes will be inherited. NOTE: in example below imports
            # are ignored for simplicity 
             
            # class BasePopup:
            #  POPUP_MODAL = (By.CSS_SELECTOR, "some.css.locator")
            
            #  def __init__(self, driver):
            #      self.driver = driver
            
            #  def is_popup_displayed(self):
            #     pass """

    BASE_PAGE_EXAMPLE = """# Store here common locators and methods for pages of target APP to build
            # Page Object structure. 
            # From this class, all other page classes will be inherited. NOTE: in example below imports
            # are ignored for simplicity 
        
            # class BasePage:
            #   MENU_LIST = (By.CSS_SELECTOR, "some.css.locator.on.page")
            
            #   def __init__(self, driver):
            #       self.driver = driver
        
            #  def is_main_menu_displayed(self):
            #      pass
    """

    BASE_TEST = """# Create here base class for tests, from which every test will be inherited. 
            # Example: @pytest.mark.usefixtures('preconditions', 'postconditions', 'report_generation')
            # class BaseTest:
            #       pass
    """

    TOOLS_DESCRIPTION = """# Put here any scripts, emulators, stubs other useful staff, that required 
        # for test environment or test
        # execution, but not directly related to target app
        """

