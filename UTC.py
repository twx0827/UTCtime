from datetime import datetime, timedelta, timezone

def utc_to_local(utc_time_str):
    utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%SZ')
    local_tz = timezone(timedelta(hours=8))
    local_time = utc_time.replace(tzinfo=timezone.utc).astimezone(local_tz)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')
