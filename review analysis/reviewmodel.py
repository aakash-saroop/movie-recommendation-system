import pickle


model1 = pickle.load(open("nlpmodel", 'rb'))
print("this is bad movie : ",model1.predict(["this is bad movie"]))
text = "MIB is good film : "
if model1.predict([text])[0] == 'positive':
	print("MIB is good film : ",1)
else:
	print("MIB is good film : ",0)


print("this is good film : ",type(model1.predict(["this is good film"])[0]))