from telegram.ext import Updater
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='5091123162:AAHBysF8mVfpg-Nry8ufd-bFGks0RK-CnXM', use_context=True)
