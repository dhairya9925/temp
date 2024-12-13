# import random
import register_user

register_user.read()

# # List of common Indian first names and surnames (Expanded)
# indian_first_names = [
#     "rohit", "priya", "amit", "rahul", "neha", "manish", "ankit", "arun", "deepak", "suresh", "rajesh", "ashok",
#     "pankaj", "jatin", "kapil", "anita", "komal", "vikash", "santosh", "manoj", "varun", "shivam", "yogesh", "tanvi", "nidhi",
#     "suraj", "pooja", "ravi", "rani", "chandan", "mohan", "tushar", "sneha", "harshit", "vinay", "pradeep", "vijay",
#     "ravi", "tanvi", "deepali", "geeta", "neeraj", "rekha", "jaspreet", "rohit", "payal", "himanshu", "shruti", "kavita",
#     "bhavesh", "manju", "subham", "naveen", "ram", "pallavi", "krishna", "nikhil", "anjali", "puneet", "sonal", "divya",
#     "shubham", "mukesh", "madhavi", "sanjay", "reena", "poornima", "sonia", "shivendra", "kritika", "udit", "pratibha", "bhavya",
#     "alok", "surabhi", "siddharth", "poonam", "seema", "simran", "kamlesh", "pradeep", "falguni", "dinesh", "raghu", "nisha"
# ]

# indian_surnames = [
#     "kumar", "sharma", "verma", "singh", "patel", "gupta", "raj", "jadhav", "yadav", "mishra", "chauhan", "gupta",
#     "ravi", "nair", "bhatt", "bansal", "malhotra", "bhat", "pandey", "tyagi", "bhushan", "agarwal", "kapoor", "tandon", "rawat",
#     "shukla", "jain", "deshmukh", "thakur", "chopra", "sharma", "mehta", "rajan", "bose", "saxena", "sri", "patil", "shukla",
#     "agarwal", "bhargava", "jha", "suri", "bhatt", "rathore", "garg", "puri", "khatri", "yadav", "prasad", "shukla", "tandon",
#     "misra", "singhal", "gupta", "mittal", "shekhar", "panwar", "saini", "chaturvedi", "mahajan", "bhalla", "dixit", "tulsi",
#     "sodhi", "bajpai", "trivedi", "paul", "saraf", "gupta", "kanwar", "kailash", "jindal", "mehra", "gill", "bajwa", "rana"
# ]

# # Function to generate random passwords
# def generate_password():
#     return ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*", k=12))

# # Function to generate usernames, emails, and passwords
# def generate_user_data():
#     user_data = []

#     for _ in range(150):  # Generate 150 Indian usernames
#         first_name = random.choice(indian_first_names)
#         surname = random.choice(indian_surnames)
#         username = f"{first_name}_{surname}"
#         email = f"{username}@example.com"
#         password = generate_password()
#         user_data.append({"username": username, "email": email, "password": password})

#     return user_data

# # Generate the user data and save it to a JSON file
# user_data = generate_user_data()
# file_path = 'indian_user_data.json'

# # Save to JSON file
# with open(file_path, 'w') as json_file:
#     json.dump(user_data, json_file, indent=4)

# print(f"JSON file 'indian_user_data.json' with 150 entries has been created.")
