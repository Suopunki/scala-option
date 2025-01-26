import pytest
from scala_option import NoSuchElementException, none, some

class TestNoneOption:
    def test_get(self):
        option = none
        with pytest.raises(NoSuchElementException, match="Called get on NoneOption"):
            option.get()

    def test_is_empty(self):
        option = none
        assert option.is_empty()

    def test_non_empty(self):
        option = none
        assert not option.non_empty()

    def test_get_or_else(self):
        option = none
        assert option.get_or_else(0) == 0
        assert option.get_or_else(lambda: 0) == 0

    def test_or_else(self):
        option = none
        assert option.or_else(lambda: some(0)).get() == 0

    def test_map(self):
        option = none
        result = option.map(lambda x: x * 2)
        assert result.is_empty()

    def test_flat_map(self):
        option = none
        result = option.flat_map(lambda x: option.some(x * 2))
        assert result.is_empty()

    def test_fold(self):
        option = none
        result = option.fold(lambda: 0, lambda x: x * 2)
        assert result == 0

    def test_filter(self):
        option = none
        result = option.filter(lambda x: x > 5)
        assert result.is_empty()

    def test_exists(self):
        option = none
        assert not option.exists(lambda x: x == 10)

    def test_contains(self):
        option = none
        assert not option.contains(10)

    def test_to_list(self):
        option = none
        assert option.to_list() == []
    
    def test_singelton(self):
        assert none.is_empty()
