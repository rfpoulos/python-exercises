first_name = raw_input('What is your first name? ')
last_name = raw_input('%s!  What is your last name? ' % first_name)

full_name = '%s %s' % (first_name, last_name)
print full_name

#Below is a qualitative analysis
if first_name == 'Rachel':
    print "That's a great name!"
elif first_name == 'Rachael':
    print "That's the devil's spelling. . ."
else:
    print "That's a fine name, but not the BEST name."

print (full_name.upper() + "!  Your full name is " + str(len(full_name)) + " character's long")