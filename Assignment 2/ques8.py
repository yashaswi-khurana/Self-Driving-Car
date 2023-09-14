sq= ['soup','dog','cat','great','salad']
fil=filter(lambda word: word.startswith("s" or "S"),sq)
print(list(fil))