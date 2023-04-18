from datetime import datetime, timedelta

def generate_time_list(exchange, date_time, begin_time, stop_time):
    
    if exchange in ['DEUR']:
        start_time = datetime.combine(datetime.strptime(date_time, "%Y.%m.%d").date(), datetime.strptime(begin_time, "%H%M%S").time())
        end_time = datetime.combine(datetime.strptime(date_time, "%Y.%m.%d").date(), datetime.strptime(stop_time, "%H%M%S").time())
        interval = timedelta(minutes=1)
        
        # Create list to store the times and load times 
        time_list = []
        current_time = start_time
    
        while current_time <= end_time:
            formatted_time = ""  
            formatted_time = current_time.strftime("%Y-%m-%dT%H:%M")
            time_list.append(formatted_time)
            current_time += interval
            
        return time_list


def generate_url_list(exchange, date, begin_time, stop_time):
    
    # Get list of times to put into Links
    time_list = generate_time_list(exchange, date, begin_time, stop_time)
    
    # Initialize and append the appropriate link to list
    links_to_download = []
            
    # The other files come in the form of multiple links
    for timestamp in time_list:
        if exchange == 'DEUR':
            links_to_download.append(f"https://mifid2-apa-data.deutsche-boerse.com/{exchange}-pretradeMDOptions/{exchange}-pretradeMDOptions-{timestamp}.json.gz")
    
    return links_to_download 