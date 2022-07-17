import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import path_fix
from db_urlconfig import get_db_url
from models import WinningNumber


def write():
    conn = MyConnection()
    st.write("Welcome to my app")
    st.table(make_numbers_df(conn.get_winning_numbers()))


class MyConnection:
    def __init__(self):
        db_url = get_db_url()
        self.session_maker = sessionmaker(bind=create_engine(db_url))

    def get_winning_numbers(self):
        with self.session_maker() as session:
            numbers = session.query(WinningNumber.number, WinningNumber.bonus).all()
            session.commit()

        return numbers


def make_numbers_df(numbers):
    return pd.DataFrame(numbers)


write()
