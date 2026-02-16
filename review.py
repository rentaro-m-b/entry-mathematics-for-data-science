from sympy import symbols
from sympy.plotting import plot3d
from scipy import stats

def sympy_example():
    x, y = symbols('x y')
    f = x * ((3 + y * 2) ** 2 / 5) - 4
    plot3d(f)

def bayes_example():
    p_coffee_drinker = 0.65
    p_cancer = 0.005
    p_coffee_drinker_given_cancer = 0.85

    # P(CANCER | COFFEE) = P(COFFEE | CANCER) * P(CANCER) / P(COFFEE)
    p_cancer_given_coffee_drinking = p_coffee_drinker_given_cancer * p_cancer / p_coffee_drinker
    print(p_cancer_given_coffee_drinking)

def binomial_distribution_example():
    n = 10
    p = 0.9
    for k in range(n + 1):
        probability = stats.binom.pmf(k, n, p)
        print("{0} - {1}".format(k, probability))

def beta_distribution_example():
    alpha = 8
    beta = 2
    p = 1.0 - stats.beta.cdf(0.90, alpha, beta)
    print(p)

def mean_example():
    sample = [1, 3, 2, 5, 7, 0, 2, 3]
    mean = sum(sample) / len(sample)
    print(mean)
