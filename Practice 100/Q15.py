# --- Problem Setup ---
# We are solving for side 'x' (DE) in a nested triangle problem.
#
# Given values:
# AD = 4
# DB = 2 (the segment from D to B)
# BC = 9 (the base of the large triangle)
# DE = x (the base of the small triangle, which we need to find)

ad = 4
db = 2
bc = 9

# --- Calculations ---

# 1. Find the full length of the corresponding side AB
ab = ad + db

# 2. Use the proportion to solve for 'de' (x)
# The proportion is: AD / AB = DE / BC
#
# Rearranging to solve for DE:
# DE = (AD * BC) / AB

de = (ad * bc) / ab

# --- Output ---
print(f"Given values:")
print(f"  AD = {ad}")
print(f"  DB = {db}")
print(f"  BC = {bc}")
print(f"--------------------------------")
print(f"First, calculate the full side AB (AD + DB):")
print(f"  AB = {ad} + {db} = {ab}")
print(f"--------------------------------")
print(f"Now, solve the proportion (AD / AB) = (DE / BC):")
print(f"  DE = (AD * BC) / AB")
print(f"  DE = ({ad} * {bc}) / {ab}")
print(f"  DE = {ad * bc} / {ab}")
print(f"--------------------------------")
print(f"The length of the missing side x (DE) is: {de}")