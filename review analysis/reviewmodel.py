import pickle


model1 = pickle.load(open("nlpmodel", 'rb'))
print("this is bad movie : ",model1.predict(["this is bad movie"]))
print("MIB is good film : ",model1.predict(["MIB is good film"]))
print("this is good film : ",model1.predict(["this is good film"]))