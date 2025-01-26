from scala_option import some

class TestSomeOptionBool:
    def test_get(self):
        option = some(True)
        assert option.get() is True

    def test_is_empty(self):
        option = some(True)
        assert not option.is_empty()

    def test_non_empty(self):
        option = some(True)
        assert option.non_empty()

    def test_get_or_else(self):
        option = some(False)
        assert option.get_or_else(True) is False
        assert option.get_or_else(lambda: True) is False  # Test lazy evaluation

    def test_or_else(self):
        option = some(True)
        assert option.or_else(lambda: some(False)).get() is True

    def test_map(self):
        option = some(True)
        result = option.map(lambda x: not x)
        assert result.get() is False

    def test_flat_map(self):
        option = some(False)
        result = option.flat_map(lambda x: some(not x))
        assert result.get() is True

    def test_fold(self):
        option = some(True)
        result = option.fold(lambda: False, lambda x: not x)
        assert result is False

    def test_filter(self):
        option = some(True)
        result = option.filter(lambda x: x)
        assert result.get() is True

        result = option.filter(lambda x: not x)
        assert result.is_empty()

    def test_exists(self):
        option = some(False)
        assert not option.exists(lambda x: x)

    def test_contains(self):
        option = some(True)
        assert option.contains(True)
        assert not option.contains(False)

    def test_to_list(self):
        option = some(True)
        assert option.to_list() == [True]

    def test_factory(self):
        assert some(True).get() is True
