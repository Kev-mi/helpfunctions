factorial <- function(upper_bound){
    factorial = 1
    for (x in 1:upper_bound){
        factorial = factorial * x
    }
    if (factorial == 0) {
  factorial = 1
} 
    return (factorial)
}

n_choose_k <- function(n, k){
  factorial(n)/(factorial(k)*(factorial(n-k)))
}

binomial_distribution_sum <- function(n, prob, upper_bound){
    individual_prob = 0
    for (x in 0:upper_bound)
    {individual_prob <- individual_prob + ((1-prob)**(n-x)*(choose(n, x))*(prob)**(x))}
    return (individual_prob)
}

print(binomial_distribution_sum(12, 0.4, 6))

print(n_choose_k(7,3))
