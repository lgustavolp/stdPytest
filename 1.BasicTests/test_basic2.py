def somar(a,b):
        return a + b

def comprimento(list):
        return len(list)

def test_sum_and_len():
        assert somar (3,2) == 5
        assert comprimento([1,2,3,4,5]) == 5