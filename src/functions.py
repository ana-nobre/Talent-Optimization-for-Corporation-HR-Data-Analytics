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

def create_tables_schema(query, password, db_name=None):
    """
    If db_name is None -> connect without selecting a database and run the script
    If db_name is provided -> connect to that database and run the script (if db_name is not None)
    """
    if db_name is None:
        cnx = mysql.connector.connect(
            user="root",
            password=password,
            host="127.0.0.1")
        cur = cnx.cursor()
        try:
            for _ in cur.execute(query, multi=True):
                pass
            cnx.commit()
            print("Query executed successfully.")
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", getattr(err, "sqlstate", None))
            print("Message", err.msg)
        finally:
            cnx.close()
    else:
        # Use existing database to create tables
        cnx = mysql.connector.connect(
            user="root",
            password=password,
            host="127.0.0.1",
            database=db_name
        )
        cur = cnx.cursor()
        try:
            for _ in cur.execute(query, multi=True):
                pass
            cnx.commit()
            print("Query executed successfully.")
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", getattr(err, "sqlstate", None))
            print("Message", err.msg)
        finally:
            cnx.close()


# SQL Schema and Data Insertion Automation Pipeline

def insert_data(query, password, db_name, rows_list):
    
    cnx = mysql.connector.connect(
        user="root",
        password=password,
        host="127.0.0.1",
        database=db_name
    )
    
    mycursor = cnx.cursor()
    
    try:
        mycursor.executemany(query, rows_list)
        cnx.commit()
        print(mycursor.rowcount, "record(s) inserted.")
        cnx.close()
        
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()
