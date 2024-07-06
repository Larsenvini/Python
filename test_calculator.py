from calculator import square

def test_square():
    if square(2) != 4:
        print("2 squared did not equal 4")
    if square(3) != 9:
        print("3 squared did not equal 9")
    if square(10) != 100:
        print("10 squared did not equal 100")

