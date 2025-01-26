from scala_option import some

class TestSomeOptionList:
    def test_get(self):
        option = some([1, 2, 3])
        assert option.get() == [1, 2, 3]

    def test_is_empty(self):
        option = some([1, 2, 3])
        assert not option.is_empty()

    def test_non_empty(self):
        option = some([1, 2, 3])
        assert option.non_empty()

    def test_get_or_else(self):
        option = some([1, 2, 3])
        assert option.get_or_else([]) == [1, 2, 3]
        assert option.get_or_else(lambda: [0]) == [1, 2, 3]  # Test lazy evaluation

    def test_or_else(self):
        option = some([1, 2, 3])
        assert option.or_else(lambda: some([0])).get() == [1, 2, 3]

    def test_map(self):
        option = some([1, 2, 3])
        result = option.map(lambda x: [i * 2 for i in x])
        assert result.get() == [2, 4, 6]

    def test_flat_map(self):
        option = some([1, 2, 3])
        result = option.flat_map(lambda x: some([i * 2 for i in x]))
        assert result.get() == [2, 4, 6]

    def test_fold(self):
        option = some([1, 2, 3])
        result = option.fold(lambda: [], lambda x: [i * 2 for i in x])
        assert result == [2, 4, 6]

    def test_filter(self):
        option = some([1, 2, 3])
        result = option.filter(lambda x: len(x) > 2)
        assert result.get() == [1, 2, 3]

        result = option.filter(lambda x: len(x) > 3)
        assert result.is_empty()

    def test_exists(self):
        option = some([1, 2, 3])
        assert option.exists(lambda x: 2 in x)
        assert not option.exists(lambda x: 5 in x)

    def test_contains(self):
        option = some([1, 2, 3])
        assert option.contains([1, 2, 3])
        assert not option.contains([4, 5])

    def test_to_list(self):
        option = some([1, 2, 3])
        assert option.to_list() == [[1, 2, 3]]  # SomeOption of list becomes a list inside a list

    def test_factory(self):
        assert some([1, 2, 3]).get() == [1, 2, 3]
