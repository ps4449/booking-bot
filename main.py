from Bot.booking import Booking

try:
    with Booking() as bot:
        bot.first_page()
        bot.change_currency(currency='USD')
        bot.select_place("New York")
        bot.select_dates(checkin='2021-12-12', checkout='2021-12-14')
        bot.select_members(5)
        bot.click_search()
        bot.apply_filtration()

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
