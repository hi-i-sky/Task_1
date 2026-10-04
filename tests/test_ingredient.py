def test_get_price_set_price_and_get_price(ingredient):

    assert ingredient.get_price() == 300

def test_get_name_set_name_and_get_name(ingredient):

    assert ingredient.get_name() == "sausage"