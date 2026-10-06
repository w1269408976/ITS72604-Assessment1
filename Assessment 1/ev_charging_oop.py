class ChargingSession:
    def __init__(self, user_id, vehicle_number, hours_charged):
        self.__user_id = user_id
        self.__vehicle_number = vehicle_number
        self.__hours_charged = hours_charged
    # Getter 和 Setter
    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_vehicle_number(self):
        return self.__vehicle_number

    def set_vehicle_number(self, vehicle_number):
        self.__vehicle_number = vehicle_number

    def get_hours_charged(self):
        return self.__hours_charged

    def set_hours_charged(self, hours):
        if hours > 0:
            self.__hours_charged = hours
        else:
            print("Charging hours must more than 0")
    # 父类方法
    def calculate_fee(self):
        pass

    # 子类
class ACCharging(ChargingSession):

    def __init__(self, user_id, vehicle_number, hours_charged):
        super().__init__(user_id, vehicle_number, hours_charged)
        self.__max_fee = 80
    # 子类方法   Overriding
    def calculate_fee(self):
        hours = self.get_hours_charged()

        if hours <= 2:
            fee = hours * 4
        elif hours <= 4:
            fee = hours * 6
        elif hours <= 6:
            fee = hours * 8
        else:
            fee = hours * 12

            if fee > self.__max_fee:
                fee = self.__max_fee

        return fee

    # 子类
class DCCharging(ChargingSession):
    def __init__(self, user_id, vehicle_number, hours_charged):
        super().__init__(user_id, vehicle_number, hours_charged)
        self.__max_fee = 150

    # 子类方法  Overriding
    def calculate_fee(self):
        hours = self.get_hours_charged()

        if hours <= 2:
            fee = hours * 10
        elif hours <= 4:
            fee = hours * 15
        elif hours <= 6:
            fee = hours * 20
        else:
            fee = hours * 30

            if fee > self.__max_fee:
                fee = self.__max_fee

        return fee

class Bill:
    def __init__(self, charging_session):
        self.__charging_session = charging_session  #Composition Has-A
        self.__discount = 0
        self.__surcharge = 0
        self.__eco_discount = 0
        self.__net_payable = 0

    def calculate_total(
            self,
            first_time_user,
            member_type,
            eco_pass,
            peak_hour,
            idle_parking,
            lost_rfid
    ):
        gross_fee = self.__charging_session.calculate_fee()

        # Discount and waiver
        if first_time_user == "Y":
            self.__discount = gross_fee

        elif member_type == "Staff":
            self.__discount = gross_fee * 0.50

        elif (
                member_type == "Student"
                and isinstance(self.__charging_session, ACCharging)
        ):
            self.__discount = gross_fee * 0.25

        else:
            self.__discount = 0

        # Surcharge and additional fees
        self.__surcharge = 0

        if peak_hour == "Y":
            self.__surcharge += 5

        if idle_parking == "Y":
            self.__surcharge += 15

        if lost_rfid == "Y":
            self.__surcharge += 30

        # Green Eco-Pass
        if eco_pass == "Y":
            self.__eco_discount = 2
        else:
            self.__eco_discount = 0

        self.__net_payable = gross_fee - self.__discount + self.__surcharge - self.__eco_discount

        if self.__net_payable < 0:
            self.__net_payable = 0

        return self.__net_payable
    # Display
    def display_bill(self):
        gross_fee = self.__charging_session.calculate_fee()

        print("==================================")
        print("      BILL      ")
        print("----------------------------------")

        print(
            f"User ID: "
            f"{self.__charging_session.get_user_id()}"
        )
        print(
            f"Vehicle Number: "
            f"{self.__charging_session.get_vehicle_number()}"
        )
        print(
            f"Hours Charged: "
            f"{self.__charging_session.get_hours_charged()}"
        )

        print("----------------------------------")
        print(f"Gross Charging Fee: RM {gross_fee:.2f}")
        print(f"Discount / Waiver: RM {self.__discount:.2f}")
        print(f"Surcharge and Fees: RM {self.__surcharge:.2f}")
        print(f"Eco-Pass Discount: RM {self.__eco_discount:.2f}")
        print("----------------------------------")
        print(f"Net Payable: RM {self.__net_payable:.2f}")
        print("==================================")

    # Object 1
ac_session = ACCharging("A001", "A123", 5)
ac_bill = Bill(ac_session)
ac_bill.calculate_total(
    first_time_user="N",
    member_type="Student",
    eco_pass="Y",
    peak_hour="Y",
    idle_parking="N",
    lost_rfid="N"
)
ac_bill.display_bill()

print()

    # Object 2
dc_session = DCCharging("B001", "B123", 7)
dc_bill = Bill(dc_session)
dc_bill.calculate_total(
    first_time_user="N",
    member_type="Staff",
    eco_pass="N",
    peak_hour="Y",
    idle_parking="Y",
    lost_rfid="Y"
)

dc_bill.display_bill()