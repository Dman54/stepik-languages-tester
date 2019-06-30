link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_cart_button(browser):
    browser.get(link)
    import time
    # time.sleep(30)
    assert browser.find_element_by_css_selector(
        "button[type='submit'].btn.btn-lg.btn-primary.btn-add-to-basket"), 'there is no cart button'
