# HW 1 Ayad Masud 733009045 Source code, a pdf is attached with all outputs and code

# Question 1:
def str_cmp(str_1, str_2):
    # YOUR CODE HERE
    str_1 = str_1.lower().replace(" ", "")
    str_2 = str_2.lower().replace(" ", "")

    return str_1 == str_2

# Question 2:
def power_list(arr):
    ## YOUR CODE HERE
    return sum([pow(arr[i], i) for i in range(len(arr))])

# Question 3:
import numpy as np
def create_stats(universities):
    """
    Return a tuple of (mean students enrolled, median students enrolled, mean tuition, median tuition)
    Return a tuple of (mean cars sold, median cars sold, mean MSRP, median MSRP)
    """
    
    # YOUR CODE HERE
    mean_students = 0
    median_students = []
    mean_tuition = 0
    median_tuition = []
    for i in range(len(universities)):
        mean_students += universities[i][1]
        median_students.append(universities[i][1])

        mean_tuition += universities[i][2]
        median_tuition.append(universities[i][2])
    
    mean_students = mean_students / len(universities)
    mean_tuition = mean_tuition / len(universities)

    median_students = np.median(median_students)
    median_tuition = np.median(median_tuition)

    return (mean_students, median_students, mean_tuition, median_tuition)    

# Question 4:
def matrix_reshape(mat, n_rows, n_cols):
    # YOUR CODE HERE
    return mat.reshape(n_rows, n_cols)
    
# Question 5:
def dot_product(mat_1, mat_2):
    # YOUR CODE HERE
    return np.dot(mat_1, mat_2)
    
# Question 6:
def cross_product(mat_1, mat_2):
    # YOUR CODE HERE
    return np.cross(mat_1, mat_2)
    
# Question 7:
def inverse(mat):
    # YOUR CODE HERE
    return np.linalg.inv(mat)

# Question 8:
def subtract_mean(mat):
    ## YOUR CODE HERE
    row_avg = np.mean(mat, axis=1, keepdims=True) # use keepdims to make sure the dimension of matrix is correct
    return mat - row_avg
    
# Question 9:
def moving_average(arr, window_size):
    # YOUR CODE HERE
    avg = []

    for i in range(len(arr) + 1 - window_size):
        window_avg = sum(arr[i:i+window_size]) / window_size
        avg.append(window_avg)

    return avg
    
# Question 10:
## YOUR CODE HERE
from_cities = list(df["From"])
to_cities = list(df["To"])

print("There are", len(set(from_cities + to_cities)), "unique cities.")

# Question 11:
## YOUR CODE HERE
print("There are", len(df[df["From"] == "London"]), "flights flying out from London")

# Question 12:
## YOUR CODE HERE
airline = df[df["Airline"] == "Air France"]
cities = list(airline["From"]) + list(airline["To"])
print("These are the cities served by Air France:", cities)

# Question 13:
## YOUR CODE HERE
print("There are", df.isna().sum().sum() , "NaN in df")

# Question 14:
# YOUR CODE HERE
sum_delay = df["Delay_1"].sum() + df["Delay_2"].sum() + df["Delay_3"].sum()
length_delay = df["Delay_1"].notna().sum() + df["Delay_2"].notna().sum() + df["Delay_3"].notna().sum()
avg = sum_delay / length_delay
print("The average delay for all flights is:", avg)

# now replacing NaN
df["Delay_1"] = df["Delay_1"].fillna(avg)
df["Delay_2"] = df["Delay_2"].fillna(avg)
df["Delay_3"] = df["Delay_3"].fillna(avg)

# Question 15:
## YOUR CODE HERE
col = pd.Series(range(10045, 10095, 10)).astype(int)
df["FlightNumber"] = col


