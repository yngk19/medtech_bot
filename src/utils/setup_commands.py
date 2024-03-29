from aiogram.types.bot_command import BotCommand
from typing import List


def setup_commands() -> List:
	start_command = BotCommand(command='start', description='Начать работу с ботом')
	cancel_command = BotCommand(command='cancel', description='Отменить действие')
	help_command = BotCommand(command='help', description='Помощь')
	#menu_command = BotCommand(command='menu', description='Меню')
	#lk_command = BotCommand(command='lk', description='Личный кабинет')
	#auth_command = BotCommand(command='auth', description='Авторизация')
	#register_command = BotCommand(command='register', description='Регистрация')
	return [start_command, help_command, cancel_command]