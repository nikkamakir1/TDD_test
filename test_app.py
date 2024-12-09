from app import soup


def test_soup():
    assert soup(0) == 'Soy Sauce Egg'  # 今日のスープ
    assert soup(-2) == 'Soy Sauce Seaweed'  # 負の値
    assert soup(1) == 'Salt Egg!!!'  # 正の値
    assert soup(365) == 'Salt Egg!!!'  # 大きな正の値
    assert soup(-365) == 'Salt Seaweed!!!'  # 負の大きな値
