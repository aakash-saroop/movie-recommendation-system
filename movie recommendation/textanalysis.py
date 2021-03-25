import pickle

def returnlabel(text):
    model1 = pickle.load(open("nlpmodel", 'rb'))
    if model1.predict([text])[0] == 'positive':
    	return(int(1))
    else:
    	return(int(0))