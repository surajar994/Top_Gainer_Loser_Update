from nsetools import Nse
import addTopers
import getTopersFromDB
from datetime import date, datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')
now = datetime.now(IST)
nse = Nse()
gainers = nse.get_top_gainers()
losers = nse.get_top_losers()
gainer_list = []
loser_list = []

if now < now.replace(hour=15, minute=30, second=0):
    # Exchange already closed. So adding the top loser&gainer to DB if not done already
    today = date.today()
    existing_records_for_today = getTopersFromDB.get_existing_records_count(today)
    if existing_records_for_today == 0:
        # Top loser and gainer not add. So adding
        gainer_list=addTopers.format_list(gainers, "G")
        loser_list=addTopers.format_list(losers, "L")
        addTopers.add_to_db(gainer_list)
        addTopers.add_to_db(loser_list)
    else:
        print("Data Already existing")

else:
    # trading ongoing. Look for a stock
    print("Open")
