# Kimberley Gitau
# 12/02/2026
# String formatting

# Get string length
sentence = "I watch horror"
string_length = len(sentence)

print(f"The length is: {string_length}")

# spliting a string
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is: ", split[0])

# Make everything CAPS
mpesa_code = "ub21ddsfhg"

capitalized = mpesa_code.upper()

print("New mpesa code:", capitalized)

# Make everything lower
mpesa_code = "UF34FFDTREG"

lowercase = mpesa_code.lower()

print("New mpesa code:", lowercase)

# Replacing characters in a string

balance = "100Kes"
amount_added = "50Kes"

cleaned_balance = balance.replace("Kes", "")

print("Cleaned balance:",cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes","")

print("cleaned amount added: ", cleaned_amount_added)

# Kimmys answer
new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print("The new balance is:", new_balance)

# Assignment
sentence_1 = "CONFIRMED you have received 40KES from Phillip"
split1 = sentence_1.split(" ")
print(sentence_1)
print("The amount is: ", split1[4])

