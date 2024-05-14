mediatype = input("File name: ").lower().strip()
def main():
    if mediatype.endswith("gif"):
        print("image/gif")

    elif mediatype.endswith(".jpg"):
        print("image/jpeg")

    elif mediatype.endswith(".jpeg"):
        print("image/jpeg")

    elif mediatype.endswith(".png"):
        print("image/png")

    elif mediatype.endswith(".pdf"):
        print("application/pdf")

    elif mediatype.endswith(".txt"):
        print("text/plain")

    elif mediatype.endswith(".zip"):
        print("application/zip")

    else:
        print("application/octet-stream")

main()
