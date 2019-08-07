import factorialmemoization


def sine_of_radians(radians, degree):

    """
    Calculate sine of given angle (in radians) using Taylor Polynomial to given degree.

    The degree argument refers to the number of terms of the polynomial
    calculated and has nothing to do with the degree as a unit of angle.
    """

    if degree < 3 or degree > 63:

        raise ValueError("degree must be between 3 and 63")

    multiplier = -1.0
    sine = radians

    fm = factorialmemoization.FactorialMemoization(degree)

    for currentdegree in range(3, (degree + 1), 2):

         sine += ( (radians ** currentdegree) / fm.get(currentdegree) * multiplier )

         multiplier *= -1

    return sine
