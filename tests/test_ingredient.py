from constants.data_set import INGREDIENT_NAME, INGREDIENT_PRICE


class TestIngredient:


    def test_get_price_set_price_and_get_price(self, ingredient):

        assert ingredient.get_price() == INGREDIENT_PRICE


    def test_get_name_set_name_and_get_name(self, ingredient):

        assert ingredient.get_name() == INGREDIENT_NAME