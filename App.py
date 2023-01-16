import streamlit as st
from faker import Faker
import pandas as pd

def create_data():
  # Initialize the Faker object
  fake = Faker()

  # Create an empty dataframe to store the customer data
  columns = ["name", "email", "gender", "age", "occupation", "account_opening_date", "account_opening_channel"]
  data = pd.DataFrame(columns=columns)

  # Generate the customer data
  for _ in range(1000):
      name = fake.name()
      email = fake.email()
      gender = fake.random_element(elements=("male", "female"))
      age = fake.random_int(min=18, max=100)
      occupation = fake.job()
      account_opening_date = fake.date_between(start_date='-10y', end_date='today')
      account_opening_channel = fake.random_element(elements=("Online", "Retail Store", "Phone"))
      customer = pd.DataFrame([[name, email, gender, age, occupation, account_opening_date, account_opening_channel]], columns=columns)
      data = data.append(customer, ignore_index=True)
  return data

st.title("Data created by Faker")
df = create_data()
st.write('Faker Data', df)
