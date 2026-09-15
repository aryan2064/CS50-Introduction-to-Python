import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_pattern = re.compile(
        r"""
        ^
        #   0-99 100-199 200-249 250-255  (no leading zeros)
        ([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.  # First byte + dot
        ([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.  # Second byte + dot
        ([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.  # Third byte + dot
        ([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])    # Fourth byte
        $
    """,
        re.VERBOSE,
    )

    return bool(re.search(ip_pattern, ip))


if __name__ == "__main__":
    main()
