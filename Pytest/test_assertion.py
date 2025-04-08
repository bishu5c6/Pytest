def test_assertions():
    assert 4==5
    assert 4<5
    assert 4>5

def test_one():
    a = "arun"
    b = "varun"
    assert a.__eq__(b), "a and b are not equal"

# if you want to print something along with the assertions
# write something in doublw quotes