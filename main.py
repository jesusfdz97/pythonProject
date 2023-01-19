# Let's create an mile pace calculator
lap = float(input('What is your current 400m?'))
half_lap = float(input('What is your current 200m?'))
your_name = input('What is your name?')
mile = (lap*4 + half_lap*8)/2
mile_in_min = (mile/60)
m, s = divmod(mile_in_min, 1)
seconds = (s*.6)
print('Hello ' + your_name + ', your calculated mile pace is ' + str(m) + ' minutes and ' + str(s) + ' seconds per mile.')