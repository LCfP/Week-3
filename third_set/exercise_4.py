friends = ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]

count_name_length_5 = 0
for friend in friends:
    if len(friend) == 5:
        count_name_length_5 += 1

print("Friends with name length 5", count_name_length_5)