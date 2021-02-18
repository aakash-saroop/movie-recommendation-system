import csv
import numpy as np
import re
from random import shuffle

def normalisation(a, i):
    #a is a 2D array
    #i is the column to be normalised
    temp = a[0][i]
    # temp is to store title of column
    a[0][i] = float(0)
    avg = np.average(a[:, i].astype('float'))
    sd = np.std(a[:, i].astype('float'))
    #print("average",avg)
    #print("sd",sd)
    a[:, i] = ((a[:, i].astype('float') - float(avg)) / float(sd)).astype('float')
    a[0][i] = temp
    return a


def normalisation_list(x):
    x = np.array(x)
    avg = np.average(x)
    sd = np.std(x)
    #print("average",avg)
    #print("sd",sd)
    x = (x - avg) / sd
    return x

def random_intialisation(dim1, dim2):
    matrix = np.random.randn(dim1, dim2)
    #matrix*= 0.01
    return matrix

def fixing_values_X(X, result1, train_set):
    # year corrosponding to movie_id-1
    year = []
    for i in range(result1.shape[0]):
        if i==0:
            continue

        strings = re.findall("([0-9]+)",result1[i][1])
        #Only one movie did not specify its year
        try:
            string = strings[len(strings)-1]
        except:
            string = "1990"
        if string=="":
            string = "1990"
        year.append(string)

    year = list(map(int, year))
    year = normalisation_list(year)

    for i in range(X.shape[0]):
        X[i][0] = year[i]
        X[i][1] = len(result1[i+1][1].split()) - 1
        X[i][2] = 0


    X = normalisation(X, 1)
    for i in range(train_set.shape[0]):
        X[int(train_set[i,1]) - 1][2] +=1

    X = normalisation(X, 2)
    return X

def fixing_values_theta(theta, train_set):
    theta[:, 3] = 0
    for i in range(train_set.shape[0]):
        theta[int(train_set[i,0])][3] += 1

    theta = normalisation(theta, 3)
    return theta




def forming_matrix_r(data_set):
    # i is movie 1st dimension = 1682 i b/w 1 and 1682
    # j is user 2nd dimension = 944
    r = np.zeros((1682, 944))
    for i in range(data_set.shape[0]):
        r[int(data_set[i][1]) - 1][int(data_set[i][0])] = 1
    return r



def forming_matrix_y(data_set):
    y = np.zeros((1682, 944))
    for i in range(data_set.shape[0]):
        y[int(data_set[i][1]) - 1][int(data_set[i][0])] = int(data_set[i][2])
    return y


#def new_user:
    # theta x + ui

def algorithm(X, theta, y, r, lambda1):
    J = 0
    theta /= 100
    X /=100
    alpha = 0.01
    beta = 0.9
    beta2 = 0.999
    # Size of X = 1682,10
    # Size of theta = 944, 10
    # Size of r = 1682, 944
    # Size of y = 1682, 944
    y_norm = np.zeros((y.shape[0] ,1))
    print(y_norm.shape)
    assert(y_norm.shape==(1682,1))
    y_norm = np.average(y, axis=1) # confirmed that it should be 1
    y_norm = np.reshape(y_norm, (y.shape[0], 1))
    print(y_norm.shape)
    assert(y_norm.shape==(1682,1))
    y = y - y_norm
    Vx = 0
    Vtheta = 0
    Sx = 0
    Stheta = 0
    for i in range(2000):
        errors = np.multiply((np.dot(X, np.transpose(theta)) - y) , r)

        J1 = 0.5 * (np.sum(np.multiply(errors, errors)))
        J2 = lambda1 / 2 * (np.sum(np.multiply(theta, theta)) )
        J3 = lambda1 / 2 * (np.sum(np.multiply(X, X)))
        #J2 = 0
        #J3 = 0

        J = J1 + J2 + J3
        X_grad = np.dot(errors, theta) + lambda1* X
        Theta_grad = np.dot(np.transpose(errors), X) + lambda1* theta

        Vx = beta*Vx + (1-beta)*X_grad
        Vtheta = beta*Vtheta +(1-beta)*Theta_grad
        Sx = beta2*Sx +(1-beta2)*np.multiply(X_grad, X_grad)
        Stheta = beta2*Stheta + (1-beta2)*np.multiply(Theta_grad, Theta_grad)

        X[:, 3:] = (X - alpha*Vx/(np.sqrt(Sx + 1e-8)))[:, 3:]
        theta[:, :3] = (theta - alpha*Vtheta/(np.sqrt(Stheta + 1e-8)))[:, :3]
        theta[:, 4:] = (theta - alpha*Vtheta/(np.sqrt(Stheta + 1e-8)))[:, 4:]

        if(i%100==0):
            #if(i%100==0):
            #    alpha = alpha - 0.0000003
            print("cost after iteration",i,"=",J1)
        dict = {}
    final_cost = np.sum(np.multiply(np.absolute(np.dot(X, np.transpose(theta)) - y ), r))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("final cost:", final_cost)
    dict = {"X": X, "theta":theta, "y_norm":y_norm}
    return dict

def test_algorithm(dict, y_test, r_test, lambda1):
    theta = dict["theta"]
    X = dict["X"]
    y_norm = dict["y_norm"]

    y_test = y_test - y_norm

    errors = np.multiply((np.dot(X, np.transpose(theta)) - y_test) , r_test)

    J1 = 0.5 * (np.sum(np.multiply(errors, errors)))
    J2 = lambda1 / 2 * (np.sum(np.multiply(theta, theta)) )
    J3 = lambda1 / 2 * (np.sum(np.multiply(X, X)))
    J = J1 + J2 + J3
    #for i in range(r_test.shape[0]):
        #for j in range(r_test.shape[1]):
            #if(r_test[i][j]==1):
                #print(np.dot(X[i,:], np.transpose(theta[j,:])) - y_test[i][j])
    #print("Cost=", J)
    final_cost = np.sum(np.multiply(np.absolute(np.dot(X, np.transpose(theta)) - y_test ), r_test))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("final cost:", final_cost)





################################################################################
# open the csv file conatining movie titles
reader1 = csv.reader(open("movie_titles.csv", "r"), delimiter=",")
x1 = list(reader1)
result1 = np.array(x1).astype("str")

# open the csv file containing the ratings provided by users corrosponding to movies
reader2 = csv.reader(open("Recommendation System.csv", "r"), delimiter=",")
x2 = list(reader2)
result2 = np.array(x2).astype("str")

# splitting the data into train, dev and test set
result2 = result2.astype('float')
train_set = result2[10000:, :]
dev_set = result2[5000:10000, :]
test_set = result2[:5000, :]

# Calculating the average of all the ratings
average_rating = np.average(train_set[:, 2])
print("The average movie rating is", average_rating)

# Baselines error is the error we get if we predict the average rating
# in each case without using any ML algorithm
print("Baseline error:")

baseline_error = np.average(np.abs(train_set[:, 2] - average_rating))
print(baseline_error)



#initialising matrices
# randomly initialising values of theta(matrix for users)
theta = random_intialisation(944, 10) # user id b/w 0 and 943
# randomly  initialising values of X(matrix for movies)
X = random_intialisation(1682, 10) # movie id b/w 1 and 1682
# including no. of words in title, year of release and no. of ratings as a part of X
# also normalising the values
X = fixing_values_X(X, result1, train_set)
# Including no. of ratings given by user in theta
# also normalising the values
theta = fixing_values_theta(theta, train_set)
# r(i,j)=1 if ith movie has been rated by jth user
# otherwise r(i,j)=0
r = forming_matrix_r(train_set)
# y is the actual rating given by a paticular user to a paticuar movie
y =forming_matrix_y(train_set)
lambda1 = 3.5

print("_____________________________________________________________")
# algorithm is performing the collabarative filtering algorithm
dict = algorithm(X, theta, y, r, lambda1)
# r_dev(i,j)=1 if ith movie has been rated by jth user
# otherwise r_dev(i,j)=0
# y_dev is the actual rating given by a paticular user to a paticuar movie
r_dev = forming_matrix_r(dev_set)
y_dev =forming_matrix_y(dev_set)
# test_algorithm is performing the collabarative filtering algorithm
test_algorithm(dict, y_dev, r_dev, lambda1)
# r_test(i,j)=1 if ith movie has been rated by jth user
# otherwise r_test(i,j)=0
# y_test is the actual rating given by a paticular user to a paticuar movie
r_test = forming_matrix_r(test_set)
y_test =forming_matrix_y(test_set)
# test_algorithm is performing the collabarative filtering algorithm
test_algorithm(dict, y_test, r_test, lambda1)
