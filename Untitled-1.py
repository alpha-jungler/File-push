print("my name is rikesh")
print ("i am 16 years old")
print("i live in dhobidhara")
if 5>2:
    print("true")
else:
    print("false")

print(1)
print(2)
print(12)


x="Rikesh"
print(x)
y=("Dhobidhara, ktm")
print(y)
z=16
print(z)

A="Rikesh"
print(type(A))
B=16
print(type(B))
C=6.91
print(type(C))


M=str("My name is")
N=str("My name is"  "Rikesh")
print(M,N)

if 10>5:
    print("True")
else:
    print("false")


# Get input from user
score = float(input("Enter your score (0-100): "))

# Check and print grade
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
elif 0 <= score < 60:
    print("Grade: F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")



M=["Apple", "Banana", "Cherry", "Date"],["Fig", "Grape", "Honeydew", "Kiwi"],["Lemon", "Mango", "Nectarine", "Orange"],["Papaya", "Quince", "Raspberry", "Strawberry"],["Tomato", "Ugli fruit", "Watermelon", "Xigua"]
print(M)


x={"Apple", "Banana", "Cherry", "Date"},{"Fig", "Grape", "Honeydew", "Kiwi"},{"Lemon", "Mango", "Nectarine", "Orange"},{"Papaya", "Quince", "Raspberry", "Strawberry"},{"Tomato", "Ugli fruit", "Watermelon", "Xigua"}
print(x)


U=("Apple", "Banana", "Cherry", "Date"),("Fig", "Grape", "Honeydew", "Kiwi"),("Lemon", "Mango", "Nectarine", "Orange"),("Papaya", "Quince", "Raspberry", "Strawberry"),("Tomato", "Ugli fruit", "Watermelon", "Xigua")
print(U)


def marks(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Score: {score}, Grade: {grade}")



