# Regular Expressions (sometimes shortened to regexp, regex, or re) are a tool for matching patterns in text.
# In Python, we have the re module

# An example regex is r"^(From|To|Cc).*?python-list@python.org"
# Now for an explanation: the caret ^ matches text at the beginning of a line.
# The following group, the part with (From|To|Cc) means that the line has to start with one of the words that are separated by the pipe |.
# That is called the OR operator, and the regex will match if the line starts with any of the words in the group.
# The .*? means to un-greedily match any number of characters, except the newline \n character.
# The . character means any non-newline character,
# the * means to repeat 0 or more times,
# the ? character makes it un-greedy.
# The un-greedy part means to match as few repetitions as possible.

# So, the following lines would be matched by that regex:
# From: python-list@python.org To: !asp]<,. python-list@python.org

# Example:
import re
pattern = re.compile(r"\[(on|off)\]") # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example

# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "v iktor@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")

# pattern = r"^(v|k|m)"
pattern = r".*?(@example.com|@python.org|@email.com)"
test_email(pattern)