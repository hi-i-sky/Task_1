from unittest.mock import Mock
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_init_without_bun():
    burger = Burger()
    assert burger.bun is None


def test_init_without_ingredients():
    burger = Burger()
    assert len(burger.ingredients) == 0


def test_set_buns_set_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "black bun"
    mock_bun.get_price.return_value = 100

    burger = Burger()
    burger.set_buns(mock_bun)

    assert burger.bun is mock_bun


def test_add_ingredient_add_two_ingregients():
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_price.return_value = 100
    mock_ingredient_sauce.get_name.return_value = "hot sauce"
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE

    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_price.return_value = 200
    mock_ingredient_filling.get_name.return_value = "dinosaur"
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING

    burger = Burger()
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)

    assert len(burger.ingredients) == 2
    assert burger.ingredients[0] is mock_ingredient_sauce
    assert burger.ingredients[1] is mock_ingredient_filling


def test_get_price_get_burger_price_with_two_buns_and_two_ingredients():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "black bun"
    mock_bun.get_price.return_value = 100

    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_price.return_value = 100
    mock_ingredient_sauce.get_name.return_value = "hot sauce"
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE

    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_price.return_value = 200
    mock_ingredient_filling.get_name.return_value = "dinosaur"
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)

    assert burger.get_price() == 500


def test_get_receipt_get_burger_receipt_with_two_buns_and_two_ingredients():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "black bun"
    mock_bun.get_price.return_value = 100

    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_price.return_value = 100
    mock_ingredient_sauce.get_name.return_value = "hot sauce"
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE

    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_price.return_value = 200
    mock_ingredient_filling.get_name.return_value = "dinosaur"
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)

    expected_receipt = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "= filling dinosaur =\n"
        "(==== black bun ====)\n\n"
        "Price: 500"
    )

    assert burger.get_receipt() == expected_receipt