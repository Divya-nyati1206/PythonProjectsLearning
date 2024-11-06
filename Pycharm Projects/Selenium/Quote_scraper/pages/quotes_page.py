from typing import List
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from Quote_scraper.locators.quotes_page_locator import QuotePageLocator
from Quote_scraper.parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [QuoteParser(e)
                for e in self.browser.find_elements(
                By.CSS_SELECTOR, QuotePageLocator.QUOTE)]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotePageLocator.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotePageLocator.TAG_DROPDOWN)
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotePageLocator.SEARCH_BUTTON)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options]

    def select_tag(self, selected_tag: str):
        self.tag_dropdown.select_by_visible_text(selected_tag)
