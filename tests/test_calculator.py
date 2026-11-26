def add(a, b):
    return a + b


def test_add():
    assert add(10, 20) == 30
    print("Addition test passed!")


def test_add_negative():
    assert add(-5, 5) == 0
    print("Negative number test passed!")


if __name__ == "__main__":
    test_add()
    test_add_negative()
    print("All tests passed!")
