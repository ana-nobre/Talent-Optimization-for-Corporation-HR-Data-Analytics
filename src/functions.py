import os
import pandas as pd
import numpy as np
import mysql.connector

# Exploratory Data Analysis (EDA) automation pipeline

def files():
    df = pd.read_csv('/Users/ananobre/Adalab_Bootcamp/Projetos Pessoais para Git/Talent-Optimization-for-Corporation-HR-Data-Analytics-1/Data-Analytics-and-Vizualization/hr_data_cleaned.csv', on_bad_lines='skip')
    return df

def exploracion(df):
    for df_i, name in zip([df], ['employees']):  # mantém a estrutura original, agora com 1 df
        print(f"INFORMATION ABOUT {name.upper()}")
        print(f"Shape:")
        print(f"{df_i.shape}\n")
        print(f"Columns:")
        print(f"{df_i.columns}\n")
        print(f"Data types:")
        print(f"{df_i.dtypes}\n")
        print(f"Missing values:")
        print(f"{df_i.isnull().sum()}\n")
        print(f"Duplicated rows:")
        print(f"{df_i.duplicated().sum()}\n")
        print(f"Main statistics:")
        print(f"{df_i.describe().T}\n")

        # Show the mode of categorical columns only for 'employees' if there are nulls
        if name == 'employees':
            print("Modes of the categorical columns (only where there are nulls):\n")
            categorical_cols = df_i.select_dtypes(include='object')
            for column in categorical_cols:
                if df_i[column].isnull().any():
                    print(f"Checking {column}")
                    print(df_i[column].value_counts())
                    print("")
        print("\n-----------------------------\n")

    return

# SQL Schema Creation Automation Pipeline

import mysql.connector

def create_schema_and_tables(query, password):
    """
    Connects to MySQL without selecting a database,
    executes the provided SQL script to create the schema and its tables.
    """
    cnx = mysql.connector.connect(
        user="root",
        password=password,
        host="127.0.0.1"
    )
    mycursor = cnx.cursor()

    try:
        # Allow execution of multiple SQL statements (CREATE SCHEMA + CREATE TABLES)
        for _ in mycursor.execute(query, multi=True):
            pass
        cnx.commit()
        print("Schema and tables created successfully.")
    except mysql.connector.Error as err:
        if err.errno == 1045:  # wrong password
            print("Access denied: check your password.")
        else:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE:", getattr(err, 'sqlstate', None))
            print("Message:", err.msg)
    finally:
        cnx.close()
