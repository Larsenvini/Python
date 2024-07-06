from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4

    assert square(3) == 9

    assert square(10) == 100


if __name__ == '__main__':
    main()
