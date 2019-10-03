## EXPORT this to your PATH: export PATH="/Users/hugoVendetta/spare_projects/test_driven_development/tdd_with_python:$PATH"


from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://localhost:8000")

assert 'Django' in browser.title

