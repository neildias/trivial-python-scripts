def disclaimer2(message, spaces=60):
    # ensure the message is even
    message = message if len(message) % 2 == 0 else message + " "

    # ensure spaces is even
    spaces = spaces if spaces % 2 == 0 else spaces + 1
    if len(message) + 2 > spaces:
        spaces = len(message) + 4
    adjusted_spaces = (spaces - len(message)) // 2 - 1

    # print disclaimer
    print()
    print("#" * spaces)
    # spaces - 2 to account for two hash symbols
    print(f'#{" " * (spaces - 2)}#')
    # spaces - 1 to account for hash symbol at the beginning and the end
    print(f'#{" "*adjusted_spaces}{message}{" "*adjusted_spaces}#')
    print(f'#{" " * (spaces - 2)}#')
    print("#" * spaces)
    print()


def disclaimer3(message, spaces=60, style="#"):
    # ensure the message is even
    def fix_message(msg):
        return msg if len(msg) % 2 == 0 else msg + " "

    if not isinstance(message, list):
        message = [message]

    max_message_len = max([len(msg) for msg in message])

    if max_message_len + 2 > spaces:
        spaces = max_message_len + 4
    # ensure spaces is even
    spaces = spaces if spaces % 2 == 0 else spaces + 1

    # print disclaimer
    print()
    print(style * spaces)
    # spaces - 2 to account for two hash symbols
    print(f'{style}{" " * (spaces - 2)}{style}')
    for msg in message:
        msg = fix_message(msg)
        # spaces - 1 to account for hash symbol at the beginning and the end
        adjusted_spaces = (spaces - len(msg)) // 2 - 1
        print(f'{style}{" "*adjusted_spaces}{msg}{" "*adjusted_spaces}{style}')
    print(f'{style}{" " * (spaces - 2)}{style}')
    print(style * spaces)
    print()

def disclaimer(message: str, spaces: int= 60, style:str ="#") -> None:
    """Prints message inside a box contain formatting
    :param message: str
    :param spaces: int
    :param style: str
    :return: None
    """

    # ensure the message is even
    def fix_message(msg):
        # ensure that the message len is an even number
        return msg if len(msg) % 2 == 0 else msg + " "

    if not isinstance(message, list):
        # ensure message is a list
        message = [message]

    # adjust the space if space provided is less than message len
    max_message_len = max([len(msg) for msg in message])

    if max_message_len + 2 > spaces:
        spaces = max_message_len + 4

    # ensure spaces is even
    spaces = spaces if spaces % 2 == 0 else spaces + 1

    # below ensure same width of printing
    # spaces - 2 to account for two hash symbols
    max_print_reference = second_line_print = f'{style}{" " * (spaces - 2)}{style}'
    start_print = end_print = (style * spaces)[:len(max_print_reference)]

    # print disclaimer
    print()
    print(start_print)
    print(second_line_print)

    # print message
    for msg in message:
        msg = fix_message(msg)
        # spaces - 1 to account for hash symbol at the beginning and the end
        adjusted_spaces = (spaces - len(msg)) // 2 - 1
        print(f'{style}{" "*adjusted_spaces}{msg}{" "*adjusted_spaces}{style}')

    print(second_line_print)
    print(end_print)
    print()


if __name__ == "__main__":
    option = input("1 for disclaimer 1, 2 for disclaimer 2 and 3... :: ")
    message = input("type your message here :: ")
    max_width = input("Max message width? :: ")
    if not max_width:
        max_width = 60
    else:
        max_width = int(max_width)
    if option == "1":
        disclaimer(message, max_width)
    if option == "2":
        disclaimer2(message, max_width)
    if option == "3":
        disclaimer3(message, max_width)