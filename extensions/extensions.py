mediatype = input("File name: ")
def main():
    if mediatype.endswith("gif"):
        print("image/gif")

    elif mediatype.endswith(".jpg", ".jpeg"):
        print("image/jpeg")

    elif mediatype.endswith(".png"):
        print("image/png")

    elif mediatype.endswith(".pdf"):
        print("image/pdf")

    elif mediatype.endswith(".txt"):
        print("image/txt")

    elif mediatype.endswith(".zip"):
        print("image/zip")

    else:
        print("application/octet-stream")

main()
