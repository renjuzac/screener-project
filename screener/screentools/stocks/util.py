import datetime
import pytz


def is_update_required(last_updated_at):

	utc_now = pytz.utc.localize(datetime.datetime.utcnow())
	pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))

	today = datetime.date.today ()
	afternoon3pm = datetime.time(hour=15, minute=00)
	today3pm = datetime.datetime.combine(today, afternoon3pm,pytz.timezone("America/Los_Angeles"))

	# print(today3pm)
	# print(report.last_update -pst_now)



	if today.weekday() < 6 :   # Monday - Friday
		if last_updated_at < today3pm:
			return True

	if today.weekday() in [6,7] :   # Saturday - Sunday 
		last_friday = datetime.date.today () - datetime.timedelta (days= today.weekday() -5)
		friday3pm = datetime.datetime.combine(last_friday, afternoon3pm,pytz.timezone("America/Los_Angeles"))
		if last_updated_at < friday3pm:
			return True

	return False

# https://stackoverflow.com/questions/23642676/python-set-datetime-hour-to-be-a-specific-time
# https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python