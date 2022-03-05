count = 0
string = "Killimanjaroi"
for letter in string:
    if letter == "i":
        count += 1
print(count, " letters found")


# union() method

a = {
    1,
    2,
    3,
}
b = {3, 5, 6}
result = a | b
# or result = b.union(a)
print(result)  # result = { 1,2,3,5,6 }

# intersection = &

c = {1, 2, 3, 4, 5}
d = {3, 5, 1, 4, 5, 6, 7}
result2 = c & d
# or result2 = c.intersection(d)

print(result2)


# difference()

e = {1, 2, 3}
f = {7, 6, 5}

result3 = e - f

print("result3 = ", result3)


# symmetric_difference  ^

g = {1, 2, 7}
h = {2, 3, 7}
print(g ^ h)

for item in set("apple"):
    print(item)
