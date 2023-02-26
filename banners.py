from typing import Tuple
import shutil

class Colors:
    black   = '\033[30m'
    red     = '\033[31m'
    green   = '\033[32m'
    yellow  = '\033[33m'
    blue    = '\033[34m'
    magenta = '\033[35m'
    cyan    = '\033[36m'
    white   = '\033[37m'
    reset   = '\033[0m'


    @staticmethod
    def get_color(func_name):
        if func_name in Banner._registered_methods:
            return Banner._registered_methods[func_name]['color']
        if func_name == 'success':
            return Colors.green
        elif func_name == 'error':
            return Colors.red
        elif func_name == 'info':
            return Colors.yellow
        else:
            return Colors.white




class Banner:
    '''Simple, colored terminal banners to point out the events of your processes.'''
    _registered_methods = {}

    def __init__(self, style:str='-'):
        self.style = style

    def _fill_term(self, message:str) -> Tuple[str,str]:
        term_size = shutil.get_terminal_size((80, 20)).columns
        style_count = (term_size - len(message))
        formatted_msg = message.center(style_count, ' ')
        lines = self.style * style_count 

        return lines, formatted_msg

    def _format(func):
        def wrapper(self, message: str=None):
            if message is None:
                message = func.__defaults__[0]
            color = Colors.get_color(func.__name__)
            lines, msg = self._fill_term(message=message)
            formatted_lines = f'{color}{lines}{Colors.reset}'
            formatted_msg = f'{color}{msg}{Colors.reset}'
            print(f'{formatted_lines}\n{formatted_msg}\n{formatted_lines}')
        return wrapper
    

    def register(self, func_name: str, color: str, message: str):
        if not hasattr(Colors, color): color = Colors.white
        print('the color is', getattr(Colors, color) + 'abc' + Colors.reset)
        Banner._registered_methods[func_name] = {
            'color': color,
            'message': message
        }

        def registered_func(self, message=None):
            if message is None:
                message = message or Banner._registered_methods[func_name]['message']
            color = getattr(Colors, (Colors.get_color(func_name=func_name)))
            lines, msg = self._fill_term(message=message)
            formatted_lines = f'{color}{lines}{Colors.reset}'
            formatted_msg = f'{color}{msg}{Colors.reset}'
            print(f'{formatted_lines}\n{formatted_msg}\n{formatted_lines}')
        setattr(Banner, func_name, Banner._format(registered_func))
    

    @_format
    def success(self, message='SUCCESS'):
        return message

    @_format
    def error(self, message='ERROR'):
        return message
    
    @_format
    def info(self, message='INFO'):
        return message
        