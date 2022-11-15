def factorial(n):
  # print(f"* At first, n is {n}")
  product = 1
  # print(f"* We set the  product to {product}")
  # print(f"* While loop starts")
  while n > 1:
    # print(f"* Loop iteration starts")
    # print(f" * product is {product}")
    original_product = product
    product *= n
    # print(f"* n starts off as {n}")
    n -= 1
    # print(f" * Decrease n by 1 to {n}")
    # print(f"* we multiply ({original_product}) by ({n}), making {product}")
    # print("Loop iteration ends")
  # print(f"The final product is {product}")
  return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")

print(f"""
 Running: factorial(3)
Expected: 6
  Actual: {factorial(3)}
""")


print(f"""
 Running: factorial(7)
Expected: 5040
  Actual: {factorial(7)}
""")