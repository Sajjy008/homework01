annual_salary = float (input("Enter your annual salary"))
portion_saved = float (input("Enter the percent of your salary to save, as a decimal"))
total_cost = float (input("Enter the cost of your dream home"))
save_all = 0
portion_down_payment = 0.25 * total_cost
r = 0.04
sarmaye = (save_all * r )/12
hoghogh_mahame = annual_salary /12
portion_saved = portion_saved * hoghogh_mahame
time = 0
while (save_all <= portion_down_payment):
    time += 1
    save_all += (save_all * r / 12) + portion_saved
print('Number of months: %d' % time)



