#!/usr/bin/env python3
        
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    #Convert the number of years to months
    months = years * 12

    # calculate future value
    future_value = 0.0
    #Loop through each month to calculate the future value
    for i in range(0, months):
        #Add the monthly investment to the future value
        future_value += monthly_investment
        #Calculate the interest earned for the current month
        monthly_interest = future_value * monthly_interest_rate
        #Add the monthly interest to the future value
        future_value += monthly_interest

#Return the calculated future value after all the months are processed
    return future_value

def main():
    #Initialize the loop control variable to 'y' to start the loop
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t"))
        #Get the yearly interest rate from the user
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        #Get the number of years for the investment from the user
        years = int(input("Enter number of years:\t\t"))

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

#Display the calculated future value, rounded to two decimal places
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()
#Print a goodbyw message when the user chooses to stop
    print("Bye!")
    #If the script is run directly, execute the main function
if __name__ == "__main__":
    main()
