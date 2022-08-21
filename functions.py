import math
import numpy as np


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


def arithmetic_series_recursion_3(arithmetic_series_list):
    iterations = 0
    for x in range(0, len(arithmetic_series_list) - 1):
        arithmetic_series_list, recursion = arithmetic_series_recursion_2(arithmetic_series_list)
        if not recursion:
            break
        iterations += 1
    return iterations, arithmetic_series_list[0]


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


def arithmetic_series_solver(arithmetic_series_list):
    solution_coefficients = []
    iterations, coefficient = arithmetic_series_recursion(arithmetic_series_list)
    arithmetic_series_list, solution_coefficients = arithmetic_series_2_generator(arithmetic_series_list[0:iterations+1], coefficient/np.math.factorial(iterations), solution_coefficients)
    for x in range(0, iterations):
        iterations, coefficient = arithmetic_series_recursion_3(arithmetic_series_list)
        arithmetic_series_list, solution_coefficients = arithmetic_series_2_generator(arithmetic_series_list[0:iterations + 1], coefficient / np.math.factorial(iterations), solution_coefficients)
    return solution_coefficients



#from helpfunctions.functions import *
#examples below
#print(polynomial_arithmetic_series_eval([3, 5, 8, 9], 10))
# n degree polynomial requires at least n+1 number of numbers in a list
#arithmetic_series_solver([25, 77, 187, 379])
#lcm(20)
#prime_finder(20)