from boolean_model import Boolean_model

bm = Boolean_model()

result =  bm.load_query("house and the dragon or wood fruits meat".split())

print(result)