def get_start_of_packet_marker(s: str) -> int:
    for i in range(len(s) - 4):
        if len(set(s[i:i + 4])) == 4:
            return i + 4
    raise EOFError


def get_start_of_message_marker(s: str) -> int:
    for i in range(len(s) - 14):
        if len(set(s[i:i + 14])) == 14:
            return i + 14
    raise EOFError


def get_start_of_something_marker(s: str, offset: int) -> int:
    return min([i + offset if len(set(s[i:i + offset])) == offset else len(s) for i in range(len(s) - offset)])


def main():
    with open("res/input_6") as f:
        print(get_start_of_packet_marker(content := f.read()), get_start_of_message_marker(content))
        print(get_start_of_something_marker(content, 4), get_start_of_something_marker(content, 14))


if __name__ == '__main__':
    main()
