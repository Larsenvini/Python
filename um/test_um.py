from um import count

def main():
    test_okstr()




def test_okstr():
    assert count("um opa um") == 2
    assert count(" so i was thinking um umm maybe um we could um go out") == 3
    assert count("umopaum i like cs50 a lot") == 0
    assert count("umumumumumumumumumuummmummmummumumumumum") == 0
    assert count("umumumumumumumumumuummmummmummumumumumum um") == 1




