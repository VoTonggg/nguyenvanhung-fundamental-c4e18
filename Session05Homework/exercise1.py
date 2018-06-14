inventory = {
    "gold" : 500,
    "pouchd" : ["flint", "twine", "genstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["pocket"] = ["seashell", "strange berry", "lint"]

inventory["backpack"].remove("dagger")
print(inventory["pocket"])

inventory["gold"] = [inventory["gold"], 50]
print(inventory["gold"])