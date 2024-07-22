"""
madlibs.py
Implementation of a madlibs game.
"""

# prompt the user for an adjective noun and verb-> input
adj = input("Give me an adjective")
noun = input("Give me a noun")
verb = input("Give me a verb ending in -ing")
adj1 = input("Give me an adjective")
noun1 = input("Give me a noun")
verb1 = input("Give me a verb ending in -ing")

# output a pre-defined sentence with the input words -> print
print("The", adj, noun, "was", verb, "before going to python class, and the",
      adj1, noun1, "was", verb1, ".")

