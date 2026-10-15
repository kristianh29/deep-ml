import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    polynomial_g = np.poly1d(g_coeffs)
    polynomial_h = np.poly1d(h_coeffs)

    derived_g = polynomial_g.deriv()
    derived_h = polynomial_h.deriv()

    evaluated_g = polynomial_g(x)
    evaluated_h = polynomial_h(x)

    evaluated_derived_g = derived_g(x)
    evaluated_derived_h = derived_h(x)

    return ((evaluated_derived_g*evaluated_h) - (evaluated_g*evaluated_derived_h))/(evaluated_h**2)
