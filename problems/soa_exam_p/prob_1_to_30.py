"""Questions 1 to 30."""
from sympy import symbols, Eq, solve


def solve_question_3():
    r"""
    Solve question 3.

    Given that :math:`P(A \cup B) = 0.7` and :math:`P(A \cup B') = 0.9`.
    Calculate :math:`P(A)`.
    """
    # Define the symbols
    prob_a = symbols('Pr(A)')
    prob_b = symbols('Pr(B)')

    # Given equations
    # P(A ∪ B) = PA + PB - P(A ∩ B)
    equation1 = Eq(prob_a + prob_b - prob_a * prob_b, 0.7)
    # P(A ∪ B') = PA + (1 - PB) - P(A ∩ B')
    equation2 = Eq(prob_a + (1 - prob_b) - prob_a * (1 - prob_b), 0.9)

    # Solve the equations
    solution = solve((equation1, equation2), (prob_a, prob_b))

    # Extracting the value of prob_a
    pr_a = solution[0][0]

    return pr_a
