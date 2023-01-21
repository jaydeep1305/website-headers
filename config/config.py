import os
from dotenv import load_dotenv


class Config:

    load_dotenv()

    HASURA_URL = os.getenv('HASURA_URL')
    HASURA_ADMIN_SECRET = os.getenv('HASURA_ADMIN_SECRET')

