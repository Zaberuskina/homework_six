from datetime import time
def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # Переключение темной темы в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    is_dark_theme = current_time.hour >= 22 or current_time.hour < 6
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    is_dark_theme = dark_theme_enabled_by_user if dark_theme_enabled_by_user is not None else (current_time.hour >= 22 or current_time.hour < 6)
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # Пользователя с именем "Olga"
    suitable_users = next(user for user in users if user["name"] == "Olga")
    assert suitable_users == {"name": "Olga", "age": 45}

    #Все пользователей младше 20 лет
    suitable_users = [user for user in users if user["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def print_function_info(func, *args, **kwargs):
    func_name = func.__name__.replace('_', ' ').title()
    arguments = [str(arg) for arg in args] + [f"{k}={v}" for k, v in kwargs.items()]
    result = f"{func_name} [{', '.join(arguments)}]"
    print(result)
    return result


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(
        page_url="https://companyname.com/login",
        button_text="Register"
    )


def open_browser(browser_name):
    actual_result = print_function_info(open_browser, browser_name=browser_name)
    assert actual_result == "Open Browser [browser_name=Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_info(go_to_companyname_homepage, page_url=page_url)
    assert actual_result == "Go To Companyname Homepage [page_url=https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_info(
        find_registration_button_on_login_page,
        page_url=page_url,
        button_text=button_text
    )
    assert actual_result == "Find Registration Button On Login Page [page_url=https://companyname.com/login, button_text=Register]"