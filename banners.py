import shutil


class Banner:
    black   = '\033[30m'
    red     = '\033[31m'
    green   = '\033[32m'
    yellow  = '\033[33m'
    blue    = '\033[34m'
    magenta = '\033[35m'
    cyan    = '\033[36m'
    white   = '\033[37m'
    reset   = '\033[0m'

    def __init__(self, style:str='-'):
        self.style = style

    def _fill_term(self, message:str) -> str:
        term_size = shutil.get_terminal_size((80, 20)).columns
        style_count = (term_size - len(message))
        formatted_msg = message.center(style_count, ' ')
        lines = self.style * style_count 

        return lines, formatted_msg

    def _format(func):
        def wrapper(self, message=None):
            if message is None:
                message = func.__defaults__[0]
            color = Banner.get_color(func.__name__)
            lines, msg = self._fill_term(message=message)
            formatted_lines = f'{color}{lines}{Banner.reset}'
            formatted_msg = f'{color}{msg}{Banner.reset}'
            print(f'{formatted_lines}\n{formatted_msg}\n{formatted_lines}')
        return wrapper
    
    @staticmethod
    def get_color(func_name):
        if func_name == 'success':
            return Banner.green
        elif func_name == 'error':
            return Banner.red
        elif func_name == 'info':
            return Banner.yellow
        else:
            return Banner.white



    @_format
    def success(self, message='SUCCESS'):
        return message

    @_format
    def error(self, message='ERROR'):
        return message
    
    @_format
    def info(self, message='INFO'):
        return message
        


         