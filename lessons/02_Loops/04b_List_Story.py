"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = words[0] +" " +words[2] + " " + words[7] +" " + words[9] + " " + words[1] + " " + words[5] + " " + words[7] + " " + words[13] + " " + words[11] + " " + words[16] + " " + words[7] + " " + words[12]

# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))