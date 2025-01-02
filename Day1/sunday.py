import pandas as pd

def sundays_of_year(year):
    """
    Return a Pandas DatetimeIndex containing all the Sundays of the specified year.

    Parameters:
    year (int): The year for which to generate the Sundays.

    Returns:
    pd.DatetimeIndex: A DatetimeIndex containing all the Sundays of the specified year.
    """
   
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    all_dates = pd.date_range(start=start_date, end=end_date)

    
    sundays = all_dates[all_dates.dayofweek == 6]

    return sundays

if __name__ == "__main__":
    year = 2024
    sundays = sundays_of_year(year)
    print(f"Sundays in the year {year}:\n{sundays}")
