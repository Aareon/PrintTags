from os import getenv

# TODO: Correct colors

# Print tags
info_tag: str = '[info] '
success_tag: str = '[success] '
notice_tag: str = '[notice] '
timeout_tag: str = '[timeout] '
warn_tag: str = '[warn] '
exit_tag: str = '[exit] '
error_tag: str = '[error] '

# ANSI color codes
black_code: int = 30
red_code: int = 31
green_code: int = 32
yellow_code: int = 33
blue_code: int = 34
magenta_code: int = 35
cyan_code: int = 36
white_code: int = 37

# ANSI string format
base_string: str = '\033[0;{}m{}\033[0m'


def colorize(message, color=30):
    if getenv('ANSI_COLORS_DISABLED') is None:
        message = base_string.format(color, message)
    return message


# Basic color printouts

class Colors(object):

    """
    Contains all the base methods responsible for wrapping 
    input strings in the correct ANSI string formatting
    """

    @staticmethod
    def black(string):
        """
        Colorizes a string to black

        Args:
            string: The string to colorize
        """
        return colorize(string, color=black_code)

    @staticmethod
    def red(string):
        """
        Colorizes a string to red

        Args:
            string: The string to colorize
        """
        return colorize(string, color=red_code)

    @staticmethod
    def green(string):
        """
        Colorizes a string to green

        Args:
            string: The string to colorize
        """
        return colorize(string, color=green_code)

    @staticmethod
    def yellow(string):
        """
        Colorizes a string to yellow

        Args:
            string: The string to colorize
        """
        return colorize(string, color=yellow_code)

    @staticmethod
    def blue(string):
        """
        Colorizes a string to blue

        Args:
            string: The string to colorize
        """
        return colorize(string, color=blue_code)

    @staticmethod
    def magenta(string):
        """
        Colorizes a string to magenta

        Args:
            string: The string to colorize
        """
        return colorize(string, color=magenta_code)

    @staticmethod
    def cyan(string):
        """
        Colorizes a string to cyan

        Args:
            string: The string to colorize
        """
        return colorize(string, color=cyan_code)

    @staticmethod
    def white(string):
        """
        Colorizes a string to white

        Args:
            string: The string to colorize
        """
        return colorize(string, color=white_code)


def black(*args, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in black
    black(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.black(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        pass


def red(*args, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in red
    red(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.red(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        pass


def green(*args, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in green
    green(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.green(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        pass


def yellow(*args, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in yellow
    yellow(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.yellow(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        pass


def blue(*args, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in blue
    blue(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.blue(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        pass


def magenta(*args, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in magenta
    magenta(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.magenta(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        pass


def cyan(*args, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in cyan
    cyan(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.cyan(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        pass


def white(*args, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in white
    white(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.white(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        pass

# Tagged color printouts


def info(message, tag=True):
    """
    Used for printing basic information.

    Color:
        Cyan
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(info_tag, message) if tag else message
    cyan(message)


def success(message, tag=True):
    """
    Used to indicate the successful execution of a process.

    Color:
        Green
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(success_tag, message) if tag else message
    green(message)


def notice(message, tag=True):
    """
    Used as means of printing important information.

    Color:
        Blue
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(notice_tag, message) if tag else message
    blue(message)


def timeout(message, tag=True):
    """
    Used to indicate the timeout of a process.

    Color:
        Cyan
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(timeout_tag, message) if tag else message
    yellow(message)


def warn(message, tag=True):
    """
    Used to highlight that there may be an issue, or that a process has failed.

    Color:
        Magenta
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(warn_tag, message) if tag else message
    magenta(message)


def error(message, tag=True):
    """
    Can be used to print the description or message associated with an exception.

    Color:
        Red
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(error_tag, message) if tag else message
    red(message)


if __name__ == "__main__":
    pass
