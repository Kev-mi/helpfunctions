factorial <- function(upper_bound){
  factorial = 1
  for (x in 1:upper_bound){
    factorial = factorial * x
  }
  return (factorial)
}

n_choose_k <- function(n, k){
  factorial(n)/(factorial(k)*(factorial(n-k)))
}

print(n_choose_k(7,3))