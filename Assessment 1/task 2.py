
continue_program = "Y"

while continue_program == "Y":

    gross_fee = 0
    discount = 0
    surcharge = 0
    eco_discount = 0
    net_payable = 0

    # 1. input
    user_id = input("Please Input User ID: ")
    vehicle_number = input("Please Input Vehicle Number: ")
    member_type = input("Please Input Member Type(Student/Staff): ").title()
    charger_type = input("Please Input Charger Type (AC/DC): ").upper()
    hours_charged = float(input("Please Input Hours Charged: "))

    # Special conditions
    first_time_user = input("Are You First-Time User? (Y/N): ").upper()
    eco_pass = input("Are You Green Eco-Pass Holder? (Y/N): ").upper()
    peak_hour = input("Peak Hour Charging? (Y/N): ").upper()
    idle_parking = input("Idle Parking? (Y/N): ").upper()
    lost_rfid = input("Do You Lost RFID Card? (Y/N): ").upper()

    # 2.Charging Fee Calculation
    # AC
    if charger_type == "AC":

        if   hours_charged <=2:
            gross_fee = hours_charged * 4

        elif hours_charged <=4:
            gross_fee = hours_charged * 6

        elif hours_charged <=6:
            gross_fee = hours_charged * 8

        else:
            gross_fee = hours_charged * 12

            if gross_fee > 80:
                gross_fee = 80
    # DC
    elif  charger_type == "DC":

        if   hours_charged <=2:
            gross_fee = hours_charged * 10

        elif hours_charged <=4:
            gross_fee = hours_charged * 15

        elif  hours_charged <=6:
            gross_fee = hours_charged * 20

        else:
            gross_fee = hours_charged * 30

            if  gross_fee > 150:
                 gross_fee = 150

       # 3. Discount and Waiver Evaluation
    if first_time_user == "Y":
        discount = gross_fee

    elif member_type == "Staff":
        discount = gross_fee * 0.50

    elif member_type == "Student" and charger_type == "AC":
        discount = gross_fee * 0.25

    else:
        discount = 0

    # 4.Surcharge & Fee Addition
    if peak_hour == "Y":
        surcharge = surcharge + 5
    if idle_parking == "Y":
        surcharge = surcharge + 15
    if lost_rfid == "Y":
        surcharge = surcharge + 30

    if eco_pass == "Y":
        eco_discount = 2
    else:
        eco_discount = 0

    net_payable = gross_fee - discount + surcharge - eco_discount
    if net_payable < 0:
        net_payable = 0

    print("==================================")
    print("  BILL  ")
    print("==================================")

    print(f"User ID: {user_id}")
    print(f"Vehicle Number: {vehicle_number}")
    print(f"Member Type: {member_type}")
    print(f"Charger Type: {charger_type}")
    print(f"Hours Charged: {hours_charged}")
    print("\n==================================\n")

    print("------------------------------")

    print(f"Your Gross Charging Fee: {gross_fee}RM")
    print(f"Your Discount / Waiver: {discount}RM")
    print(f"Your Surcharge and Fees: {surcharge}RM")
    print(f"Your Eco-Pass Discount: {eco_discount}RM")
    print(f"Your Net Payable: {net_payable}RM")

    continue_program = input("Continue the program?(Y/N): ")
print("Finished")