from logic import *
import termcolor

onKitchenTable = Symbol("My glasses are on the kitchen table.")
sawAtBreakfast = Symbol("I saw glasses at breakfast.")
readNewsInLivingRoom = Symbol("I was reading the newspaper in the living room.")
readnewsInKitchen = Symbol("I was reading the newspaper in the kitchen.")
onCoffeeTable = Symbol("My glasses are on the coffee table.")
readBookInBed = Symbol("I was reading my book in bed.")
onBedTable = Symbol("My glasses are on the bed table.")

knowledge = And(
    Implication(onKitchenTable, sawAtBreakfast),
    Or(readNewsInLivingRoom, readnewsInKitchen),
    Implication(readNewsInLivingRoom, onCoffeeTable),
    Not(sawAtBreakfast),
    Implication(readBookInBed, onBedTable),
    Implication(readnewsInKitchen, onKitchenTable)
)

symbols = [onKitchenTable, onBedTable, onCoffeeTable]

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}", "green")
        #elif not model_check(knowledge, Not(symbol)):
        #    print(f"{symbol}: False")

check_knowledge(knowledge)