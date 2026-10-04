def test_init_without_bun(empty_burger):

    assert empty_burger.bun is None


def test_init_without_ingredients(empty_burger):

    assert len(empty_burger.ingredients) == 0


def test_set_buns_set_buns(empty_burger, mock_bun):
    empty_burger.set_buns(mock_bun)

    assert empty_burger.bun is mock_bun


def test_add_ingredient_add_two_ingredients(empty_burger, mock_sauce, mock_filling):
    empty_burger.add_ingredient(mock_sauce)
    empty_burger.add_ingredient(mock_filling)

    assert len(empty_burger.ingredients) == 2
    assert empty_burger.ingredients[0] is mock_sauce
    assert empty_burger.ingredients[1] is mock_filling


def test_get_price_get_burger_price_with_two_buns_and_two_ingredients(mock_full_burger, mock_bun, mock_sauce, mock_filling):
    expected_price = (
        mock_bun.get_price() * 2 +
        mock_sauce.get_price() +
        mock_filling.get_price()
    )

    assert mock_full_burger.get_price() == expected_price


def test_get_receipt_get_burger_receipt_with_two_buns_and_two_ingredients(mock_full_burger, mock_bun, mock_sauce, mock_filling):
    expected_receipt = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "= filling dinosaur =\n"
        "(==== black bun ====)\n\n"
        "Price: 500"
    )

    assert mock_full_burger.get_receipt() == expected_receipt