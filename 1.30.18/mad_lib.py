print """Please fill in the blanks below:
____(name)____'s favorite subject in school is ____(subject)____."""
input_name = raw_input("What is your name? ")
input_subject = raw_input("What is your favorite subject? ")

print "%s's favorite subject in school is %s." % (input_name, input_subject)