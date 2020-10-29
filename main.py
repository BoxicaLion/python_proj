# This is a sample Python script.
import requests


def currencyConverter():
    currency_arr = ["EUR", "USD", "GBP", "RUB"]  # New populated array with Currency name
    rate_arr = [1, 1.17, 0.90, 92.45]  # New populated array witch Currency Rates.
    flag = False  # Flag For while loop

    while not flag:
        currencyToConvert = input("What currency you have? Choose from the list: "
                                  "\n| 1: EUR | 2: USD | 3: GBP | 4: RUB |\n ")  # User chose

        if int(currencyToConvert) > 4:  # Checking the preconditions
            print("Wrong choice! Please select available currency!")
            continue

        print(f"Your chose is:", currency_arr[int(currencyToConvert) - 1])  # Display the user's choice.

        convertToCurrency = input("What currency would you like to convert? Choose from the list: "
                                  "\n| 1: EUR | 2: USD | 3: GBP | 4: RUB |\n  ")  # User choice.

        if int(convertToCurrency) > 4:  # Checking the preconditions
            print("Wrong choice! Please select available currency!")
            continue

        print(f"Your chose is:", currency_arr[int(convertToCurrency) - 1])  # Display the user's choice.

        the_amount = input("How much money you would you like to to convert? \n")  # Colect he user's amount

        convertedCurrency = int(the_amount) * rate_arr[int(currencyToConvert) - 1] * rate_arr[
            int(convertToCurrency) - 1]  # Calculate the conversion.

        flag = True  # stop while loop

        print(f"Your total amount after conversion is:", convertedCurrency,
              currency_arr[int(convertToCurrency) - 1])
        # display the results


class Currency_Converter:
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = Currency_Converter()
    currencyConverter()

