import time

import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import path_fix
from db_urlconfig import get_db_url
from models import WinningNumber


class MyConnection:
    def __init__(self):
        db_rl = get_db_url()
        self.session_maker = sessionmaker(bind=create_engine(db_rl))

    def add_to_winning_numbers(self, scores):
        scores = WinningNumber(number=scores[0], bonus=scores[1])
        with self.session_maker() as session:
            session.add(scores)

            session.commit()


conn = MyConnection()
print("Conection Established")
while True:
    num1, num2 = np.random.randint(1, 36), np.random.randint(1, 36)
    conn.add_to_winning_numbers((num1, num2))
    print("Record added")
    time.sleep(15)
