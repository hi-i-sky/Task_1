import pytest
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_init_buns_count(db):
    buns = db.available_buns()

    assert len(buns) == 3


def test_init_ingredients_count(db):
    ingredients = db.available_ingredients()

    assert len(ingredients) == 6


@pytest.mark.parametrize(
    "expected_name,expected_price",
    [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ],
)
def test_available_buns_initialization_list_of_buns(db, expected_name, expected_price):
    buns = db.available_buns()

    matching_buns = []

    for item in buns:
        if item.get_name() == expected_name:
            matching_buns.append(item)

            assert len(matching_buns) == 1
            assert matching_buns[0].get_price() == expected_price


@pytest.mark.parametrize(
    "expected_type,expected_name,expected_price",
    [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ],
)
def test_available_ingredients_initialization_list_of_ingredients(db, expected_type, expected_name, expected_price):
    ingredients = db.available_ingredients()

    matching_ingredients = []

    for item in ingredients:
        if item.get_name() == expected_name:
            matching_ingredients.append(item)

            assert len(matching_ingredients) == 1
            assert matching_ingredients[0].get_price() == expected_price
            assert matching_ingredients[0].get_type() == expected_type