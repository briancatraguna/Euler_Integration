#Intro
while True:
    cont = input("Please read the README for instructions. \n Continue? y/n: ")
    if cont == "y":
        break

#Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Inputting the 
error = "ERROR \nPlease insert appropriate values! \nRead README again."
#Initial x
while True:
    try:
        print("Please insert initial x1: ")
        x1_0 = float(input())
        print("Please insert initial x2: ")
        x2_0 = float(input())
    except:
        print(error)
        continue
    else:
        break

#A Matrix        
while True:
    print("Please insert the A matrix (4 by 4 size): ")
    try:
        A11 = float(input("A11: "))
        A12 = float(input("A12: "))
        A21 = float(input("A21: "))
        A22 = float(input("A22: "))
    except:
        print(error)
        continue
    else:
        break

A = np.array([[A11,A12],[A21,A22]])
print("A matrix: \n",A)

#B Matrix        
while True:
    print("Please insert the A matrix (2 by 1 size): ")
    try:
        B1 = float(input("B1: "))
        B2 = float(input("B2: "))
    except:
        print(error)
        continue
    else:
        break

B = np.array([[B1],[B2]])
print("B matrix: \n",B)

#Input file
while True:
    print("Please insert the name of the input array: ")
    inputarray = str(input())
    if inputarray[len(inputarray)-4:len(inputarray)] != ".csv":
        print("Insert a CSV file!")
        continue
    else:
        break

#Initialize the list to be plotted later on
x1 = [x1_0]
x2 = [x2_0]
x1_dot = []
x2_dot = []

#Importing the doublet
data = pd.read_csv(inputarray)
data_numpy = data.to_numpy()
t = data_numpy[:,0]

#Do the looping for Euler's integration Method
for i,data in enumerate(data_numpy):
    if len(x1) and len(x2) == len(t):
        break
    u = float(data[1])
    x1_dot.append((A11*x1[i]+A12*x2[i]+B1*u)*0.1)
    x2_dot.append((A21*x1[i]+A22[i]+B2*u)*0.1)
    x1.append(x1[i]+(A11*x1[i]+A12*x2[i]+B1*u)*0.1)
    x2.append(x2[i]+(A21*x1[i]+A22[i]+B2*u)*0.1)

#Plotting the results
plt.title("X1")
plt.plot(t,x1)
plt.xlabel("Time (s)")
plt.ylabel("X1")
plt.show()

plt.title("X2")
plt.plot(t,x2)
plt.xlabel("Time (s)")
plt.ylabel("X2")
plt.show()
