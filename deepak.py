import cmath  # Use cmath to handle complex roots

# Input coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check if it's a quadratic equation
if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    # Calculate the discriminant
    D = b**2 - 4*a*c

    # Calculate the two roots using quadratic formula
    root1 = (-b + cmath.sqrt(D)) / (2*a)
    root2 = (-b - cmath.sqrt(D)) / (2*a)

    # Display the results
    print(f"\nThe roots of the equation {a}x² + {b}x + {c} = 0 are:")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
