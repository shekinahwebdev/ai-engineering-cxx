"""Practice exercise: remove duplicate values while preserving order."""

# First Approach
def remove_duplicates(users):
    actual_list = []
    for user in users:
        if user not in actual_list:
            actual_list.append(user)
    return actual_list



def remove_duplicates_(users):
    new_list = list(set(users))
    return new_list

users = [
    "Ama",
    "John",
    "Ama",
    "Shekinah",
    "John",
    "Kofi"
]

if __name__ == "__main__":
    print(remove_duplicates(users))
    print(remove_duplicates_(users))
