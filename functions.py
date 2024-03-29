import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import comb

def standard_deviation_random_variable(size):
    expected_value = (1+size)/2
    standard_deviation = 0
    for x in range(1, size + 1):
        standard_deviation += (1/size)*(x-expected_value)**2
    return math.sqrt(standard_deviation)


def poisson_distribution_summation(expected_value, upper_bound):
    summation = 0
    for x in range(0, upper_bound + 1):
        summation += ((expected_value**x)*(math.e**-expected_value))/(math.factorial(x))
    return summation


def binomial_distribution(n, prob, upper_bound):
    individual_prob = []
    for x in range(0, upper_bound+1):
        individual_prob.append(((1-prob)**(n-x)*(comb(n,x))*(prob)**(x)))
    print(individual_prob)
    return sum(individual_prob)


def variance(prob_1, prob_2, upper_bound):
    summation = 0
    summation_2 = 0
    for x in range(0, upper_bound+1):
        summation +=(x)*comb(upper_bound, x) * prob_1**x * prob_2**(upper_bound-x)
    for x in range(0, upper_bound+1):
        summation_2 +=(x-summation)**2*comb(upper_bound, x) * prob_1**x * prob_2**(upper_bound-x)
    return summation_2
        

def expected_value_calc(prob_1, prob_2, upper_bound):
    summation = 0
    for x in range(0, upper_bound+1):
        summation +=x*comb(upper_bound, x) * prob_1**x * prob_2**(upper_bound-x)


def probability_distribution(prob_1, prob_2, upper_bound):
    for x in range(0, upper_bound+1):
        print(comb(upper_bound, x) * prob_1**x * prob_2**(upper_bound-x))        


def normal_distribution(mean, std, samples):
    norm_dist = np.random.normal(mean, std, samples)
    return normal_distribution


def polynomial_arithmetic_series_eval(coeff_list, iterations):
    sums = []
    coeff_list.reverse()
    for x in range(1, iterations+1):
        total = 0
        for power, coeff in enumerate(coeff_list):
            total += (x ** power) * coeff
        sums.append(total)
    return sums


def prime_finder(number):
    prime_list = [2]
    prime = [True] * (number+1)
    for y in range(3, int(np.sqrt(number)+1), 2):
        if prime[y]:
            prime_list.append(y)
            for x in range(y**2, number + 1, y+y):
                prime[x] = False
    for x in range(y+2, number+1, 2):
        if prime[x]:
            prime_list.append(x)
    return prime_list


def smallest_multiple(upper_bound, prime_list):
    lcm = 1
    for x in prime_list:
        y = 1
        while upper_bound > y*x:
            y = y*x
            lcm *= x
    return lcm


def lcm(number):
    prime_list = prime_finder(number)
    lcm_result = smallest_multiple(number, prime_list)
    return lcm_result


def arithmetic_series_2_generator(arithmetic_series_list, coefficient, solution_coefficients):
    arithmetic_series_list_2 = [coefficient]
    for x in range(1, len(arithmetic_series_list)):
        arithmetic_series_list_2.append(0)
    solution_coefficients.append(arithmetic_series_list_2[0])
    arithmetic_series_list_2 = polynomial_arithmetic_series_eval(arithmetic_series_list_2, len(arithmetic_series_list))
    for x in range(0, len(arithmetic_series_list_2)):
        arithmetic_series_list_2[x] = arithmetic_series_list[x] - arithmetic_series_list_2[x]
    return arithmetic_series_list_2, solution_coefficients


def arithmetic_series_recursion(arithmetic_series_list):
    iterations = 0
    for x in range(0, len(arithmetic_series_list) - 1):
        arithmetic_series_list, recursion = arithmetic_series_recursion_2(arithmetic_series_list)
        if not recursion:
            break
        iterations += 1
    return iterations, arithmetic_series_list[0]


def arithmetic_series_recursion_2(series_list):
    new_series = []
    for x in range(1, len(series_list)):
        if series_list[x]-series_list[x-1] != 0:
            new_series.append(series_list[x] - series_list[x - 1])
        else:
            return series_list, False
    return new_series, True


def convert_to_polynomial(polynomial_list):
    polynomial = str(polynomial_list[0])
    for term in range(1, len(polynomial_list)):
        if str(polynomial_list[term])[0] != "-":
            polynomial += " +" + str(polynomial_list[term])[0] + "x^" + str(term)
        else:
            polynomial += " -" + str(polynomial_list[term])[0] + "x^" + str(term)
    return polynomial


def arithmetic_series_solver(arithmetic_series_list):
    solution_coefficients = []
    iterations, coefficient = arithmetic_series_recursion(arithmetic_series_list)
    arithmetic_series_list, solution_coefficients = arithmetic_series_2_generator(arithmetic_series_list[0:iterations+1], coefficient/np.math.factorial(iterations), solution_coefficients)
    for x in range(0, iterations):
        iterations, coefficient = arithmetic_series_recursion(arithmetic_series_list)
        arithmetic_series_list, solution_coefficients = arithmetic_series_2_generator(arithmetic_series_list[0:iterations + 1], coefficient / np.math.factorial(iterations), solution_coefficients)
    if len(solution_coefficients) > 1:
        polynomial = convert_to_polynomial(solution_coefficients)
        return polynomial
    else:
        return solution_coefficients[0]

def standard_deviation(values):
    summation = 0
    mean = sum(values)/len(values)
    for x in values:
        summation += (x-mean)**2
    return math.sqrt(summation/len(values))


def z_score(value, mean, standard_deviation):
    return (value - mean)/standard_deviation


def mean(values):
    return sum(values)/len(values)


def r_value_plot(independent_variable, dependent_variable):
    if type(independent_variable) == list:
        independent_variable = np.array(independent_variable)
    if type(dependent_variable) == list:
        dependent_variable = np.array(dependent_variable)
    independent_variable = independent_variable.reshape((-1, 1))
    model = LinearRegression().fit(independent_variable, dependent_variable)
    r_squared = model.score(independent_variable, dependent_variable)
    print("r squared value is", r_squared)
    plt.scatter(independent_variable, dependent_variable)
    plt.show()


print(z_score(185, 285, 50))
print(z_score(100, 140, 20))
#from helpfunctions.functions import *
#examples below
#print(polynomial_arithmetic_series_eval([3, 5, 8, 9], 10))
# n degree polynomial requires at least n+1 number of numbers in a list
#print(arithmetic_series_solver([25, 69, 159, 313, 549, 885, 1339, 1929, 2673, 3589]))
#lcm(20)
#prime_finder(20)
#values = [6, 8, 12, 14]
#print(standard_deviation(values))
#stan_dev = standard_deviation(values)
#mean = mean(values)
#print(mean)
#print(z_score(3, mean, stan_dev))
#x_val = [35.56, 43.44, 73.17, 113, 265.18]
#y_val = [44.78, 53.98, 92.14, 135.99, 326.89]
#r_value_plot(x_val, y_val)
