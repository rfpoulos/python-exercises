more_coins = raw_input("Would you like a coin? (yes/no): ")
coin_count = 0

while more_coins == "yes":
    coin_count += 1
    print coin_count
    more_coins =raw_input("Would you like another coin? (yes/no): ")

print "Bye!"
