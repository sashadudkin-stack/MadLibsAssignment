#############################################
# Name: Sasha Dudkin
# Class: ICS3C
# Date: Friday Sept 18
# Project Name: MadLibs
#
# Project Description
# You will read in multiple entries from the user and store the results in variables
# You will then insert those variables into the following story to create a MadLib style result

# A recent survey informs us that one out of every PLURALNOUN1 owns a/an ADJECTIVE1 phone.
# Fortunately, VERB_ENDING_IN_ING1 over a mobile NOUN1 in recent years has improved ADVERB1.
# Today, BODYPART1-held PLURALNOUN2 are all the rage.
# In restaurants, you find many PLURALNOUN3 talking ADVERB2 into their ADJECTIVE2 phones as they eat their NOUN2.
# NUMBER1 percent of American PLURALNOUN4 place their NOUN3 calls from their cars as they are VERB_ENDING_IN_ING2 to and from their home, office, or NOUN4.
# Walking and talking are now the "in" NOUN5 to do.
# Over NUMBER2 percent of Americans walk our ADJECTIVE3 streets with a handheld PLURALNOUN5 pressed against their BODYPART2.

# Ask for the capitalized words in the input. Print out the full story in the output.
# See https://www.thewordfinder.com/wordlibs/story/41/ for an example.
#############################################

# THIS IS WHERE YOU CODE
print("Give me a plural noun: ")
pluralNoun = input()
print("Now, give me an abjective: ")
nonobjective = input()
print("Why? (do not say 'because' please)")
reason = input()
print("My friend said that" ,pluralNoun, "is" ,nonobjective, "because" ,reason,"!")
print("That was fun!")
print("See you later!")