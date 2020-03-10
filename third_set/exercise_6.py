friends = ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]
# friends = ["Joe", "Zoe", "Sam", "Zuki", "Thandi", "Paris"]

trigger_word = "Sam"
count_up_to_trigger = 0
for friend in friends:
    if friend == trigger_word:
        break
    else:
        count_up_to_trigger += 1

print("Number of friends before", trigger_word, count_up_to_trigger)