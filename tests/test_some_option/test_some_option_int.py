from scala_option import some

class TestSomeOptionInt:
    def test_get(self):
        option = some(10)
        assert option.get() == 10

    def test_is_empty(self):
        option = some(10)
        assert not option.is_empty()

    def test_non_empty(self):
        option = some(10)
        assert option.non_empty()

    def test_get_or_else(self):
        option = some(10)
        assert option.get_or_else(0) == 10
        assert option.get_or_else(lambda: 0) == 10  # Test lazy evaluation

    def test_or_else(self):
        option = some(10)
        assert option.or_else(lambda: option.some(0)).get() == 10

    def test_map(self):
        option = some(10)
        result = option.map(lambda x: x * 2)
        assert result.get() == 20

    def test_flat_map(self):
        option = some(10)
        result = option.flat_map(lambda x: some(x * 2))
        assert result.get() == 20

    def test_fold(self):
        option = some(10)
        result = option.fold(lambda: 0, lambda x: x * 2)
        assert result == 20

    def test_filter(self):
        option = some(10)
        result = option.filter(lambda x: x > 5)
        assert result.get() == 10

        result = option.filter(lambda x: x < 5)
        assert result.is_empty()

    def test_exists(self):
        option = some(10)
        assert option.exists(lambda x: x == 10)
        assert not option.exists(lambda x: x == 5)

    def test_contains(self):
        option = some(10)
        assert option.contains(10)
        assert not option.contains(5)

    def test_to_list(self):
        option = some(10)
        assert option.to_list() == [10]

    def test_factory(self):
        assert some(10).get() == 10
