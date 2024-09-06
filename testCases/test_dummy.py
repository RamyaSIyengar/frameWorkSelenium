import pytest


class Test1:

    @pytest.fixture(scope='class', autouse=True)
    def fixture1(self):
        print("my fixture")

    def test_method1(self):
        print('method1')

    def test_method2(self):
        print('method1')
