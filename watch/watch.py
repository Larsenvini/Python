import re
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python watch.py <html.address>")
    html = sys.argv[1]
    print(parse(html))

def parse(s):

    match = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/[\w-]+)"', s)

    if match:
        embed_url = match.group(1)
        video_id = embed_url.split('/'[-1])
        return f"




...


if __name__ == "__main__":
    main()
