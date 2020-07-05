class Customer:
    def __init__(self, first_name, last_name, ac_no, ph_no, balance, job, ac_type, address):
        self.first_name = first_name
        self.last_name = last_name
        self.__ac_no = ac_no
        self.ph_no = ph_no
        self.balance = balance
        self.job = job
        self.__ac_type = ac_type
        self.address = address

    def showBalance(self):
        print("Balance : ", self.balance)

    def changeAddress(self):
        new_add = input("Enter new Address : ")
        self.address = new_add
        print("Successfully Changed ")

    def phoneNumber(self):
        new_ph = input("Enter new Phone Number : ")
        self.ph_no = new_ph
        print("Successfully Changed ")

    def changeAcType(self):
        new_actype = input("Enter new AC Type : ")
        self.__ac_type = new_actype
        print("Successfully Changed ")


c1 = Customer("Sita", "Sapkota", 128975423232154, 98123456789,
              25000, "Teacher", "Savings", "Kotesohowr")

c1.showBalance()
c1.changeAddress()
c1.phoneNumber()
c1.changeAcType()

print(c1._Customer__ac_type)
