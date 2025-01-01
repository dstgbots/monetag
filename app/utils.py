import re
from datetime import datetime

def round_money(value):
    return round(float(value), 3)

def round_cpm(value):
    return round(float(value), 2)

def validate_date_range(date_range):
    if date_range in ['total', 'today1', 'yesterday1', 'past7', 'past30']:
        return True
        
    # Check custom date range format (yyyy-mm-dd/yyyy-mm-dd)
    date_pattern = r'^\d{4}-\d{2}-\d{2}/\d{4}-\d{2}-\d{2}$'
    if re.match(date_pattern, date_range):
        try:
            start_date, end_date = date_range.split('/')
            datetime.strptime(start_date, '%Y-%m-%d')
            datetime.strptime(end_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    return False

