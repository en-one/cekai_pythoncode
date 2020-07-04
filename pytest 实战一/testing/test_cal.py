from pytestCode.cal import Calculator
import pytest
import yaml

cal = Calculator()


class TestCal:

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("../datas/cal.yml")))
    def test_add1(self,a, b, result):
        assert result == cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("../datas/cal_sub.yml")))
    def test_sub(self, a, b, result):
        assert result == cal.sub(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("../datas/cal_mul.yml")))
    def test_mul(self, a, b, result):
        assert result == cal.mul(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("../datas/cal_div.yml")))
    def test_div(self, a, b, result):
        assert result == cal.div(a, b)