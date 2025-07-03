#Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2
def finding_nth_fibo(n):
    term_1 = 1
    term_2 = 2
    for i in range(2, n):
        next_term = term_1 + term_2
        term_1 = term_2
        term_2 = next_term
        print(next_term)
number_of_terms = int(input('Enter number of terms:'))
print('Fibo Series for',number_of_terms,'terms :\n1\n2')
finding_nth_fibo(number_of_terms)