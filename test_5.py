# characters = ["Ahmed", "Ali", "Omar"]

# for index, character in enumerate(characters):
#     print(index, character)

# -----------------------------
# store index positions of duplicate items 
    
characters = ["Ahmed", "Ali", "Omar","Ahmed", "Ali", "Omar","Ahmed", "Ali", "Omar","Ahmed", "Ali", "Omar"]

character_map = {character:[] for character in set(characters)}
print(character_map)

# use enumerate to store the index for each occurence 
# append

for index, character in enumerate(characters):
    character_map[character].append(index)
print(character_map)