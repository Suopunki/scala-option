from scala_option import some

class TestSomeOptionStr:
    def test_get(self):
        option = some("hello")
        assert option.get() == "hello"

    def test_is_empty(self):
        option = some("hello")
        assert not option.is_empty()

    def test_non_empty(self):
        option = some("hello")
        assert option.non_empty()

    def test_get_or_else(self):
        option = some("world")
        assert option.get_or_else("default") == "world"
        assert option.get_or_else(lambda: "default") == "world"  # Test lazy evaluation

    def test_or_else(self):
        option = some("hello")
        assert option.or_else(lambda: some("default")).get() == "hello"

    def test_map(self):
        option = some("hello")
        result = option.map(lambda x: x.upper())
        assert result.get() == "HELLO"

    def test_flat_map(self):
        option = some("hello")
        result = option.flat_map(lambda x: some(x.upper()))
        assert result.get() == "HELLO"

    def test_fold(self):
        option = some("hello")
        result = option.fold(lambda: "default", lambda x: x.upper())
        assert result == "HELLO"

    def test_filter(self):
        option = some("hello")
        result = option.filter(lambda x: x == "hello")
        assert result.get() == "hello"

        result = option.filter(lambda x: x == "world")
        assert result.is_empty()

    def test_exists(self):
        option = some("hello")
        assert option.exists(lambda x: x == "hello")
        assert not option.exists(lambda x: x == "world")

    def test_contains(self):
        option = some("hello")
        assert option.contains("hello")
        assert not option.contains("world")

    def test_to_list(self):
        option = some("hello")
        assert option.to_list() == ["hello"]

    def test_factory(self):
        assert some("hello").get() == "hello"
