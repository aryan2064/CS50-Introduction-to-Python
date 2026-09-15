import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    video_id_pattern = re.compile(
        r"""<iframe src="https?://(?:www\.)?youtube\.com/embed/(?P<video_id>\w+)"""
    )
    video_id_match = re.search(video_id_pattern, s)

    return (
        f"https://youtu.be/{video_id_match.group("video_id")}"
        if video_id_match
        else None
    )


if __name__ == "__main__":
    main()
