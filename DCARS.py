import time



def main():
   registration()
   price_list()
   payment()


#Registering a patient
def registration():
    print("Welcome to Safreen Diagnostic Center")
    time.sleep(3)
    global surname, name, age, gender, phone_number
    surname = input("Enter your surname: ")
    name = input("Enter your name: ")

    # Validate age
    while True:
        age = input("How old are you? ")
        if age.isdigit() and int(age) > 0:
            break
        else:
            print("Please enter a valid Age")

    # Validate gender
    while True:
        gender = input("Male or Female: ")
        if gender.lower() in ['male', 'female','m','f']:
            break
        else:
            print("Invalid gender. Please enter either 'Male' or 'Female'.")

    # Validate phone number
    while True:
        phone_number = input("Enter your phone number: ")
        if phone_number.isdigit() and len(phone_number) == 11:
            break
        else:
            print("Invalid phone number. Please enter a 11-digit numeric value.")
    print("Registration Successful")
    time.sleep(3)

#center price list
def price_list():
    print(f"Good Day {surname.capitalize()}, below is our Price List: ")
    diagnosis_list = {
        "SEMEN ANALYSIS": {"price": 5000, "time": 120},
        "WIDAL": {"price": 1000, "time": 30},
        "MP": {"price": 1000, "time": 30},
        "BLOOD GROUP": {"price": 500, "time": 20},
        "GENOTYPE": {"price": 2000, "time": 60},
        "URINE MCS": {"price": 2500, "time": 4320},
        "LIVER FUNCTION TEST": {"price": 4000, "time": 1440},
        "LIPID PROFILE": {"price": 5000, "time": 1440},
        "H.PYLORI": {"price": 1500, "time": 20}
    }
    total_price = 0
    total_test_time_mins = 0
    # printing price list
    global scan
    for diagnosis, data in diagnosis_list.items():
            print(f"{diagnosis} = {data['price']}")
    #Validating Diagnosis Choice & calculating test time
    while True:
        try:
            diagnosis_choice = input("Choose the diagnosis you want to undergo (Enter 'done' when finished): ").upper()
            if diagnosis_choice in diagnosis_list:
                total_price += diagnosis_list[diagnosis_choice]['price']
                total_test_time_mins += diagnosis_list[diagnosis_choice]['time']

            elif diagnosis_choice == 'DONE':
                break
            else:
                print("Enter a valid Diagnosis")
        except ValueError:
            break
    time.sleep(2)
    # printing total bill of the patient
    print(f"Your total price is {total_price}")
    time.sleep(2)
    test_time_hour = total_test_time_mins/60
    if test_time_hour < 2:
        print(f"Your Result will be ready in {test_time_hour} hour time")
    elif 2 < test_time_hour < 6:
        print("Your result will be ready later in the day.")
    elif 6 < test_time_hour < 23:
        print("Your result will be ready tomorrow, by these time")
    else:
        test_time_days = test_time_hour / 24
        print(f"Your test will be ready in {test_time_days} days, you can come back on the day for your result.")
    time.sleep(2)
# Payment Method
def payment():
    payment_method = input("Enter your payment method (Cash, Card): ").lower()
    if payment_method == 'cash':
       print("Drop your cash on top of the counter")
    elif payment_method == 'card':
       card_number = input("Enter your card number: ")
       expiry_date = input("Enter the expiry date (MM/YY): ")
       cvv = input("Enter the CVV: ")
    time.sleep(3)
    print("Payment successful! Thank you.")
    time.sleep(2)
    print("Go to sample collection room.")






if __name__ == "__main__":
    main()
