class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        self.y = "hello"
        assert hasattr(self, 'y')
