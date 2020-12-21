import pytest
import allure

@allure.feature("模块测试demo")
class TestOne:

    @allure.story("case01 测试add")
    @pytest.mark.parametrize(("a","b"),((1,2),(2,3)))
    def test_add(self,a,b):
        with allure.step("a与b相加"):
            print('测试a+b')
            sum = a + b
            assert sum == a + b

    @allure.story("case02 测试product")
    @pytest.mark.parametrize(("a", "b"), ((1, 2), (2, 3)))
    def test_product(self,a,b):
        with allure.step("a与b相乘"):
            print('测试a*b')
            p = a * b
            assert p == a * b


if __name__ =='__main__':
    pass