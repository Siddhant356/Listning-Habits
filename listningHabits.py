from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.set_headless()
assert opts.headless
browser = Chrome(options=opts)
browser.get('https://duckduckgo.com')
search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real pyton')
search_form.submit()
results = browser.find_elements_by_class_name('result')
print(results[0].text)
browser.close()
quit()
