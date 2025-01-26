from scala_option import some

class TestSomeOptionRange:
    def test_get(self):
        option = some(range(1, 4))
        assert list(option.get()) == [1, 2, 3]

    def test_is_empty(self):
        option = some(range(1, 4))
        assert not option.is_empty()

    def test_non_empty(self):
        option = some(range(1, 4))
        assert option.non_empty()

    def test_get_or_else(self):
        option = some(range(1, 4))
        assert list(option.get_or_else(range(0))) == [1, 2, 3]
        assert list(option.get_or_else(lambda: range(0))) == [1, 2, 3]  # Test lazy evaluation

    def test_or_else(self):
        option = some(range(1, 4))
        assert list(option.or_else(lambda: some(range(0))).get()) == [1, 2, 3]

    def test_map(self):
        option = some(range(1, 4))
        result = option.map(lambda x: range(1, 7))
        assert list(result.get()) == [1, 2, 3, 4, 5, 6]

    def test_flat_map(self):
        option = some(range(1, 4))
        result = option.flat_map(lambda x: some(range(1, 7)))
        assert list(result.get()) == [1, 2, 3, 4, 5, 6]

    def test_fold(self):
        option = some(range(1, 4))
        result = option.fold(lambda: range(0), lambda x: range(1, 7))
        assert list(result) == [1, 2, 3, 4, 5, 6]

    def test_filter(self):
        option = some(range(1, 4))
        result = option.filter(lambda x: len(list(x)) > 2)
        assert list(result.get()) == [1, 2, 3]

        result = option.filter(lambda x: len(list(x)) > 3)
        assert result.is_empty()

    def test_exists(self):
        option = some(range(1, 4))
        assert option.exists(lambda x: 2 in x)
        assert not option.exists(lambda x: 5 in x)

    def test_contains(self):
        option = some(range(1, 4))
        assert list(option.get()) == [1, 2, 3]

    def test_to_list(self):
        option = some(range(1, 4))
        assert option.to_list() == [range(1, 4)]

    def test_factory(self):
        assert list(some(range(1, 4)).get()) == [1, 2, 3]
