from scala_option import some

class TestSomeOptionDict:
    # SomeOption[dict]
    def test_get(self):
        option = some({"a": 1, "b": 2})
        assert option.get() == {"a": 1, "b": 2}

    def test_is_empty(self):
        option = some({"a": 1, "b": 2})
        assert not option.is_empty()

    def test_non_empty(self):
        option = some({"a": 1, "b": 2})
        assert option.non_empty()

    def test_get_or_else(self):
        option = some({"a": 1, "b": 2})
        assert option.get_or_else({}) == {"a": 1, "b": 2}
        assert option.get_or_else(lambda: {"c": 3}) == {"a": 1, "b": 2}  # Test lazy evaluation

    def test_or_else(self):
        option = some({"a": 1, "b": 2})
        assert option.or_else(lambda: some({"c": 3})).get() == {"a": 1, "b": 2}

    def test_map(self):
        option = some({"a": 1, "b": 2})
        result = option.map(lambda x: {k: v * 2 for k, v in x.items()})
        assert result.get() == {"a": 2, "b": 4}

    def test_flat_map(self):
        option = some({"a": 1, "b": 2})
        result = option.flat_map(lambda x: some({k: v * 2 for k, v in x.items()}))
        assert result.get() == {"a": 2, "b": 4}

    def test_fold(self):
        option = some({"a": 1, "b": 2})
        result = option.fold(lambda: {}, lambda x: {k: v * 2 for k, v in x.items()})
        assert result == {"a": 2, "b": 4}

    def test_filter(self):
        option = some({"a": 1, "b": 2})
        result = option.filter(lambda x: len(x) > 1)
        assert result.get() == {"a": 1, "b": 2}

        result = option.filter(lambda x: len(x) > 2)
        assert result.is_empty()

    def test_exists(self):
        option = some({"a": 1, "b": 2})
        assert option.exists(lambda x: "a" in x)
        assert not option.exists(lambda x: "c" in x)

    def test_contains(self):
        option = some({"a": 1, "b": 2})
        assert option.contains({"a": 1, "b": 2})
        assert not option.contains({"c": 3})

    def test_to_list(self):
        option = some({"a": 1, "b": 2})
        assert option.to_list() == [{"a": 1, "b": 2}]

    def test_factory(self):
        assert some({"a": 1, "b": 2}).get() == {"a": 1, "b": 2}
