import pickle
from pathlib import Path

import streamlit_authenticator as slauth

names = ["Osama Khan", "Dev Admin"]

username = ["admin", "Dev"]
password = ["admin", "Dev_123"]

hashed_password = slauth.Hasher(password).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_password, file)

