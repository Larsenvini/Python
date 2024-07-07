from hello import hello

def main():
    assert hello("Vini") == "Hello, Vini"
    assert hello() == "Hello, World"

if __name__ == "__main__":
    main()
