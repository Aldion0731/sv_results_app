import os

from dotenv import load_dotenv

load_dotenv()


def get_db_url():
    variables = ["DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME"]
    vals = [os.environ.get(var) for var in variables]
    db_url = f"postgresql://{vals[0]}:{vals[1]}@{vals[2]}:{vals[3]}/{vals[4]}"
    return db_url
