from test.conftest import *


class ConfiguratorModel:
    browser = setup_browser

    def check_configurator(self):
        browser.element('[title="configurator"]').click()
        return self

    def check_model_bmw(self):
        browser.element('[title="BMW X6"]').click()
        return self
