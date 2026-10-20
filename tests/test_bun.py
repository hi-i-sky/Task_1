class TestBun:


    def test_get_name_set_name_and_get_name(self, bun):

        assert bun.get_name() == "red bun"


    def test_get_price_set_price_and_get_price(self, bun):

        assert bun.get_price() == 300