import pytest
import allure

class TestOne:

    @pytest.mark.parametrize(("a","b"),((1,2),(2,3)))
    def test_add(self,a,b):
        print('测试a+b')
        sum = a + b
        assert sum == a + b

    @pytest.mark.parametrize(("a", "b"), ((1, 2), (2, 3)))
    def test_product(self,a,b):
        print('测试a*b')
        p = a * b
        assert p == a * b


if __name__ =='__main__':
    pass