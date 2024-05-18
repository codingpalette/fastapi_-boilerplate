from dotenv import load_dotenv
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def conf():
    load_dotenv(ROOT_DIR+"/.env")
    config = {
        "TOKEN_KEY": os.getenv('TOKEN_KEY'),

        "DB_HOST": os.getenv('DB_HOST'),
        "DB_PORT": os.getenv('DB_PORT'),
        "DB_USER": os.getenv('DB_USER'),
        "DB_PASS": os.getenv('DB_PASS'),
        "DB_NAME": os.getenv('DB_NAME'),
    }

    return config
