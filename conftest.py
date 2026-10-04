import os
import sys
import pytest

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)


from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from database import Database
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

@pytest.fixture
def empty_burger():
    return Burger()

@pytest.fixture
def bun():
    bun = Bun("red bun", 300)
    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
    return ingredient

@pytest.fixture
def db():
    return Database()

@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "black bun"
    mock.get_price.return_value = 100
    return mock

@pytest.fixture
def mock_sauce():
    mock = Mock()
    mock.get_name.return_value = "hot sauce"
    mock.get_price.return_value = 100
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock

@pytest.fixture
def mock_filling():
    mock = Mock()
    mock.get_name.return_value = "dinosaur"
    mock.get_price.return_value = 200
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock

@pytest.fixture
def mock_full_burger(mock_bun, mock_sauce, mock_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    return burger