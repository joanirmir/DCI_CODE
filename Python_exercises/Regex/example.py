
# Importing the regular expression library

import re 

'''# Target text

text_to_be_searched = "some text mail@web.de some text"

# The actual regular expression (r stands for raw string)

pattern = r"(text)"

# Using the pattern to search the target text

x = re.findall(pattern, text_to_be_searched)

# Printing out the match

print(x)'''

# Bravo-Group
# What does \w and + do?


text = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Let me give you for some reason also your most important passwords to continue running amazon! Sorry Im new at this job.

epsteindidntkillhimself14141
ThIs1s4ctua11YaG00dPa$$w0rD
123456seven
password

Kind regards,
the soon to be fired secretary Tanisha"""

# The actual regular expression (r stands for raw string) to find all the email addresses in the text

# \w matches any word character 
# + matches the previous toke as possible, giving back as needed


pattern = r"\w+@\w+.\w+"

# Using the pattern to search the target text

x = re.findall(pattern, text)

# Printing out the match

print(x)

# Alpha-Group
