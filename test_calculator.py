from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("boo")
    try:
        assert square(3) == 9
    except AssertionError:
        print("boo")
    try:
        assert square(10) == 100
    except AssertionError:
        print("boo")


if __name__ == '__main__':
    main()
