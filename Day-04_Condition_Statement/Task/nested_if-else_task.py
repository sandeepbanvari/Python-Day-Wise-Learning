# # Practice Task: Bank Loan Eligibility
# Age >= 18?
# │
# ├── No → Loan Rejected due to age requirement
# │
# └── Yes
#     │
#     ├── Salary >= 25000?
#     │   │
#     │   ├── No → Loan Rejected due to low salary
#     │   │
#     │   └── Yes
#     │       │
#     │       ├── Credit Score = yes?
#     │       │   ├── Yes → Loan Approved
#     │       │   └── No → Loan Rejected due to poor credit score

age = int(input("Enter your age: "))

if age >= 18:
    salary = int(input("Enter your monthly salary: "))

    if salary >= 25000:
        credit_score = input("Do you have a good credit score? (yes/no): ")

        if credit_score == "yes":
            print("Loan Approved")
        else:
            print("Loan Rejected due to poor credit score")

    else:
        print("Loan Rejected due to low salary")

else:
    print("Loan Rejected due to age requirement")