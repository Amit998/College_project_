from typing import Mapping
from neuralintents import GenericAssistant
import pandas_datareader as web
import sys

from pandas_datareader import data

stock_tickers=[
    'AAPL',
    'FB',
    'GS',
    'TSLA'
]
todos=['Wash Car','Watch NeuralNine Videos','Go Shopping']

def stock_function():
    for ticker in stock_tickers:
        data=web.DataReader(ticker,'yahoo')
        print(f"The Last Price Of {ticker} was {data['Close'].iloc[-1]}")

def todo_show():
    print("Your Todod list:")
    for todo in todos:
        print(todo)

def todos_add():
    todo=input("What TODO do you want to add:")
    todos.append(todo)

def todo_remove():
    idx=int(input("Which TODO to remove (number): "))-1

    if idx < len(todos):
        print(f"Remoing Todo {todos[idx]}")

    else:
        print("There is no Todo at this postion")


def bye():
    print("Bye")
    sys.exit()


mapping_={
    'stocks':stock_function,
    'todo':todo_show,
    'todoadd':todos_add,
    'todoremove':todo_remove,
    'goodbye':bye
}

assitant=GenericAssistant("intents.json",mapping_)

assitant.train_model()
assitant.save_model()

while True:
    message=input("Message:")
    assitant.request(message)