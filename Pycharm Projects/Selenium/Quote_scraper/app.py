from selenium import webdriver

from pages.quotes_page import QuotesPage

chrome = webdriver.Firefox()
chrome.get("https://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

author_name = input("Enter the author name : ")

page.select_author(author_name)

tags = page.get_available_tags()
print("Select one of the given tags : [{}]".format("|".join(tags)))

selected_tag = input("Enter your tag : ")
page.select_tag(selected_tag)

page.search_button.click()

print(page.quotes)

