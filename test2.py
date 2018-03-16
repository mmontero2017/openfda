import string
string.ascii_letters[26:-1]
genome_id = "H34092735"
for character in genome_id:
    if character[0] == string.ascii_letters[26:-1]:
        print ("The sequence is correct.")
    else:
        print ("The sequence is incorrect.")
        break

        