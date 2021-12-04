from Bot.booking import Booking

try:
    with Booking() as bot:
        bot.first_page()
        bot.change_currency(currency='USD')
        bot.select_place(input("Where do you wish to go (city name: New York, Ooty etc)? "))
        bot.select_dates(checkin=input("Please enter your check-in date (YYYY-MM-DD). "),
                         checkout=input("Please enter your check-in date (YYYY-MM-DD). "))
        bot.select_members(input("Enter the number of adults. "))
        bot.click_search()
        bot.apply_filtration()
        bot.refresh()  # data will be grabbed properly, as shown on screen
        bot.report_results()

        print("Exiting...")

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line. \n'
            'Please add your Selenium drivers to PATH. \n'
            'For Windows: \n'
            '\t set PATH=%PATH%;C:path-to-your-driver \n\n'  # to add location to already-existing PATHs
            'For Linux: \n'
            '\t PATH=$PATH:/path/to-your/folder/ \n'
        )
    else:
        raise
