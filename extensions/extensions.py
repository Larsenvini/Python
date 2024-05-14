mediatype = input("File name: ")
def main():
    match mediatype:
        case ".gif":
            print("image/gif")

        case ".jpg" | ".jpeg":
            print("image/jpeg")

        case ".png":
            print("image/png")

        case ".pdf":
            print("image/pdf")

        case ".txt":
            print("image/txt")

        case ".zip":
            print("image/zip")

        case _:
            print("application/octet-stream")

main()
