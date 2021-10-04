from Bot.booking import Booking

with Booking() as bot:
    bot.first_page()
    bot.change_currency(currency='USD')
    bot.select_place("New York")
    bot.select_dates(checkin='2021-10-07', checkout='2021-10-10')
    bot.select_members(5)
    bot.click_search()
    bot.apply_filtration()

    print("Exiting...")
