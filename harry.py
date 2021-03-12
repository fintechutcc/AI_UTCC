from logic import *

rain = Symbol("It rained.")
hagrid = Symbol("Harry visted Hagrid.")
dumbledore = Symbol("Harry visisted Dumbledore")

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))
