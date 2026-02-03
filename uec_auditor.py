file = open("Daily_Audit_Report.txt", "w")

file.write("         Daily details          \n")

all_uec = []
all_units = []
all_productions = []

for i in range(1, 11):
    
    file.write(f"Information Machine Number: {i}\n")
    
    unit = float(input(f"Enter the unit of machine {i}: "))
    production = int(input(f"Enter the production of machine {i}: "))
    
    uec_vlue = unit / production
    
    file.write(f"The Machine {i}: Unit={unit}, Production={production}\n")
    file.write(f"The uec is: UEC={uec_vlue:.2f}\n")
    all_uec.append(uec_vlue)
    all_units.append(unit)
    all_productions.append(production)

    
    if uec_vlue > 0.5:
        print(f"🚨 Machine {i} High Energy Waste!")
    else:
        print(f"Machine {i} Energy Efficient")


file.write(f"All UEC today: {all_uec}\n")
file.write(f"The maximum unit: {max(all_units)}\n")
file.write(f"The maximum UEC: {max(all_uec)}\n")
file.write(f"The maximum production of single day: {max(all_productions)}\n")
file.write(f"The minimum production of single day: {min(all_productions)}\n")
file.write(f"The sum of uec: {sum(all_uec)}\n")

file.close()           

print("\n--- Summary ---")
print("The total number of scanned machines:", len(all_uec))
