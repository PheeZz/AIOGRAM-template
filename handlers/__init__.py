from distutils.cmd import Command
from .user import *
from .admin import *

# DON'T TOUCH THIS IMPORT
from loader import dp


def setup(dp):
    """setup handlers for users and moders in one place and add throttling in 5 seconds

    Args:
        dp (Dispatcher): Dispatcher object
    """

    """user handlers"""
    dp.register_message_handler(
        cmd_start,
        commands=['start'],
        state=None)

    """moder handlers"""
    dp.register_message_handler(
        cmd_info,
        commands=["info"],
        state=None)
