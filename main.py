from Bot.booking import Booking

with Booking() as bot:
    bot.first_page()
    bot.change_currency(currency='USD')
    bot.select_place("New York")
    bot.select_dates(checkin='2021-09-22', checkout='2021-09-25')
    print("Exiting...")
