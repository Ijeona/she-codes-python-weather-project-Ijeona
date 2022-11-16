import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
   
#     """Takes a temperature and returns it in string format with the degrees
#         and celcius symbols.

#     Args:
#         temp: A string representing a temperature.
#     Returns:
#         A string contain the temperature and "degrees celcius."
#     """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    formatted_date = date.strftime ("%A %d %B %Y")
    return formatted_date 

    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    # pass


def convert_f_to_c(temp_in_farenheit):
    celsius = (float(temp_in_farenheit)-32)*(5/9)
    return (round(celsius,1))

    # """Converts an temperature from farenheit to celcius.

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
    # pass


def calculate_mean(weather_data):
    total = 0 
    for temp in weather_data:
        total += float(temp) 
    mean = total / len(weather_data) 
    return mean
    # """Calculates the mean value from a list of numbers.
    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    # pass

def load_data_from_csv(csv_file_location):
    weather = [] #creating empty list
    with open (csv_file_location) as csv_file: #opening csv file
        reader = csv.reader(csv_file) #reading
        next (reader) #skipping headers
        for line in reader: #for loop for each row in csv
            if len(line) > 0: #if the row is not empty
                weather.append([line[0], int(line[1]), int(line[2])]) #run the following. Appending data from empty row to list. A list within a list. Turned some strings into integers and making sure we are returning the right type of data
    return weather #return the list


def find_min(weather_data):

    if len(weather_data)==0:
        return() 

    min_index = 0
    min_value = float(weather_data[0])
    for item in range(len(weather_data)):
        value = float(weather_data [item])
        if value <= min_value:
            min_value = value 
            min_index = item

    return (min_value,min_index)
    
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    
    if len(weather_data)==0:
        return() 

    max_index = 0
    max_value = float(weather_data[0])
    for item in range(len(weather_data)):
        value = float(weather_data [item])
        if value >= max_value:
            max_value = value 
            max_index = item

    return (max_value,max_index)

def generate_summary(weather_data):
    mins=[]
    max=[]
    for item in weather_data :
       # print(item)
        mins.append(convert_f_to_c(item[1]))
        max.append(convert_f_to_c(item[2]))

    min_temp=find_min(mins)  
    formatted_min_temp = format_temperature(min_temp[0])
    formatted_min_date = convert_date(weather_data[min_temp[1]][0])
    max_temp=find_max(max)
    formatted_max_temp = format_temperature(max_temp[0])
    formatted_max_date= convert_date(weather_data[max_temp[1]][0])
    
    avg_low_temp=calculate_mean (mins)
    formatted_avg_low_temp=format_temperature(round(avg_low_temp,1))
    avg_high_temp= calculate_mean(max)
    formatted_avg_high_temp=format_temperature (round(avg_high_temp,1))
    summary=(f"{len(weather_data)} Day Overview\n\
  The lowest temperature will be {formatted_min_temp}, and will occur on {formatted_min_date}.\n\
  The highest temperature will be {formatted_max_temp}, and will occur on {formatted_max_date}.\n\
  The average low this week is {formatted_avg_low_temp}.\n\
  The average high this week is {formatted_avg_high_temp}.\n\
")
    print (summary)
    return (summary)
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
  
    daily_summary = "" #don't put into list because will still need to convert it into string anyways#
    for item in weather_data:
        formatted_date = convert_date(item[0])
        min_temp_c = convert_f_to_c(item[1])
        formatted_min_temp = format_temperature(min_temp_c)
        max_temp_c = convert_f_to_c(item[2])
        formatted_max_temp = format_temperature(max_temp_c)
        daily_summary+=(f"---- {formatted_date} ----\n  Minimum Temperature: {formatted_min_temp}\n  Maximum Temperature: {formatted_max_temp}\n\n")
    print(daily_summary)
    return daily_summary