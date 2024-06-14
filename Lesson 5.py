# def get_user_info():
#
#     name = input("Enter name: ")
#     surname = input("Enter surname: ")
#     while True:
#         try:
#             age = int(input("Enter age: "))
#             if age < 0:
#                 raise ValueError("Age cannot be negative.")
#             break
#         except ValueError:
#             print("Invalid age. Please enter a non-negative integer.")
#     return [name, surname, age]
#
# def main():
#
#     consumer_info = []
#     user_lists = []
#     for i in range(3):
#         print(f"\nEnter information for user {i+1}:")
#         user_data = get_user_info()
#         user_lists.append(user_data)
#         consumer_info.append(user_data)
#
#     while True:
#         try:
#             user_index = int(input("\nEnter user index (0-2) to view information, or -1 to exit: "))
#             if user_index == -1:
#                 print("Exiting...")
#                 break
#             elif 0 <= user_index < 3:
#                 user = consumer_info[user_index]
#                 print(f"\nName: {user[0]}")
#                 print(f"Lastname: {user[1]}")
#                 print(f"Age: {user[2]}")
#             else:
#                 print("Invalid user index. Please enter a value between -1 and 2.")
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#
# if __name__ == "__main__":
#     main()

# 2.
#
# famous_actors = {
#     "Tom Hanks": {
#         "bio": "American actor and filmmaker. Known for roles in Forrest Gump, Cast Away, Saving Private Ryan, etc.",
#         "filmography": ["Forrest Gump", "Cast Away", "Saving Private Ryan", "Toy Story (voice)"],
#         "awards": ["2 Academy Awards for Best Actor"]
#     },
#     "Meryl Streep": {
#         "bio": "American actress. Holds the record for most Academy Award nominations for Best Actress.",
#         "filmography": ["The Devil Wears Prada", "Kramer vs. Kramer", "Sophie's Choice"],
#         "awards": ["3 Academy Awards for Best Actress"]
#     },
# }
#
#
# def find_actor(name):
#
#     for actor_name, info in famous_actors.items():
#         if name.lower() in actor_name.lower():
#             return info
#     return None
#
#
# def print_actor_summary(actor_info):
#
#     print(f"Name: {actor_info['name']}")
#     print(f"Bio: {actor_info['bio']}")
#     print(f"Filmography: {', '.join(actor_info['filmography'])}")
#     print(f"Awards: {', '.join(actor_info['awards'])}")
#
#
# user_input = input("Enter actor's first or last name: ")
# actor_info = find_actor(user_input)
#
# if actor_info:
#     print_actor_summary(actor_info)
# else:
#     print(f"Actor '{user_input}' not found.")
#

# 3.
# def unique_list(data):
#
#   return list(set(data))
#
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_data = unique_list(my_list)
# print(unique_data)

# 4.
# def sets_to_tuple(set1, set2):
#
#   combined_set = set1.union(set2)
#   return tuple(combined_set)
#
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# combined_tuple = sets_to_tuple(set1, set2)
# print(combined_tuple)

# 5.
# def is_empty(my_dict):
#
#   return not bool(my_dict)
#
# my_dict = {}
# print(is_empty(my_dict))
#
# my_dict = {"key": "value"}
# print(is_empty(my_dict))

# 6.
# def char_count(string):
#
#   char_dict = {}
#   for char in string:
#     if char in char_dict:
#       char_dict[char] += 1
#     else:
#       char_dict[char] = 1
#   return char_dict
#
# string = "w3schools"
# char_frequency = char_count(string)
# print(char_frequency)