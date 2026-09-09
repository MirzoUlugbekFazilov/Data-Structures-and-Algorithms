# =========================
# HASH TABLE / DICTIONARY
# =========================

table = {
    "a": 10,
    "b": 20
}

# Access
print(table["a"])

# Safe access
print(table.get("a"))

# Insert
table["c"] = 30

# Update
table["a"] = 100

# Delete
del table["b"]

# Pop
value = table.pop("c")

# Check key
print("a" in table)

# Length
print(len(table))

# Keys
print(table.keys())

# Values
print(table.values())

# Items
print(table.items())

# Loop
for key, value in table.items():
    print(key, value)

# Clear
table.clear()


# =========================
# SET
# =========================

s = {1, 2, 3}

# Add
s.add(4)

# Remove
s.remove(4)

# Safe remove
s.discard(5)

# Search
print(2 in s)

# Length
print(len(s))

# Union
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

# Intersection
print(a & b)

# Difference
print(a - b)

# Symmetric difference
print(a ^ b)

# Subset
print({1, 2}.issubset(a))

# Superset
print(a.issuperset({1, 2}))

# Clear
s.clear()


# =========================
# COUNTING WITH HASH TABLE
# =========================

numbers = [1, 2, 2, 3, 3, 3]

count = {}

for number in numbers:
    count[number] = count.get(number, 0) + 1

print(count)


# =========================
# REMOVE DUPLICATES WITH SET
# =========================

numbers = [1, 2, 2, 3, 3, 4]

unique = set(numbers)

print(unique)


HASH TABLE / DICTIONARY

Access          O(1) average
Search          O(1) average
Insert          O(1) average
Update          O(1) average
Delete          O(1) average
Pop             O(1) average
Length          O(1)
Loop            O(n)
Clear           O(n)


SET

Add             O(1) average
Search          O(1) average
Remove          O(1) average
Discard         O(1) average
Length          O(1)
Union           O(n + m)
Intersection    O(min(n, m))
Difference      O(n)
Symmetric diff  O(n + m)
Subset          O(n)
Superset        O(n)
Loop            O(n)
Clear           O(n)


COUNTING

Time            O(n)
Space           O(k)


REMOVE DUPLICATES

Time            O(n) average
Space           O(n)