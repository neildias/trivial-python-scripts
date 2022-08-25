SPACES = 5


def prnt(func):
    def execute(args):
        print("\n"*SPACES)
        func(args)
        print("\n"*SPACES)
    return execute


@prnt
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


def scheduler(cycles):
    bias = 20
    weight = 4 # mins

    if cycles > bias:
        disclaimer(f'Entertainment Time Earned :: {int(cycles * weight)} minutes' )
    elif cycles % 3 == 0:
        disclaimer("Practice Guitar for 10 mins, THEN BACK TO WORK") 
    elif cycles < 24:
        disclaimer("YOU SHOULD BE WORKING!" )


if __name__ == "__main__":
    print()
    pomodoros = int(float(input("Please input the number of Pomodoros completed :: ")))
    print()
    scheduler(pomodoros)
    print()
    