from datetime import datetime, timezone
from ics import Calendar
from typing import Dict

from core.lib import write_links_to_file
from lib import (
    load_calendar_from_file,
    filter_events_by_name,
    save_calendars,
    filter_events_by_date_range,
)

from lib_noyau import get_noyau_calendars
from lib_pscr import get_pscr_calendars

# URL of the CalDAV resource
url = 'https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR'

# Replace 'username' and 'password' with your correct credentials
username = 'student.master'
password = 'guest'

# Base URL
host = 'https://obnitram.github.io/sorbonne_calendar/'
link_file = 'link.md'


# Main logic
def main() -> None:
    # Load the calendar from a file or a URL
    raw_calendar = load_calendar_from_file('data/evenement.ics')
    # raw_calendar = load_calendar_from_url(url, username, password)

    # Filter events by date range
    start_date = datetime(2024, 9, 1, tzinfo=timezone.utc)
    end_date = datetime(2024, 12, 31, tzinfo=timezone.utc)
    raw_calendar = filter_events_by_date_range(raw_calendar, start_date, end_date)

    with open(link_file, 'w') as file:
        pass

    filters = ["NOYAU", "PSCR"]
    filtered_calendars: Dict[str, Calendar] = filter_events_by_name(raw_calendar, filters)

    paths = save_calendars(get_noyau_calendars(filtered_calendars["NOYAU"]), "m1/sar/noyau")
    write_links_to_file(paths, link_file, host, "NOYAU")

    paths = save_calendars(get_pscr_calendars(filtered_calendars["PSCR"]), "m1/sar/pscr")
    write_links_to_file(paths, link_file, host, "PSCR")





if __name__ == '__main__':
    main()
