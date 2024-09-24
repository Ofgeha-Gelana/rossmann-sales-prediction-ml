import pandas as pd
import numpy as np

def create_datetime_features(df):
    # Convert 'Date' column to datetime type
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract relevant datetime features
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['DayOfWeek'] = df['Date'].dt.dayofweek

    # Weekends: Create binary weekend feature
    df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)

    # Days to next holiday (using Christmas as an example)
    df['DaysToNextHoliday'] = (pd.to_datetime('2015-12-25') - df['Date']).dt.days
    df['DaysToNextHoliday'] = df['DaysToNextHoliday'].apply(lambda x: np.nan if x < 0 else x)

    # Days since last holiday (using New Year's Day as an example)
    df['DaysAfterLastHoliday'] = (df['Date'] - pd.to_datetime('2015-01-01')).dt.days
    df['DaysAfterLastHoliday'] = df['DaysAfterLastHoliday'].apply(lambda x: np.nan if x < 0 else x)

    # Segmenting the month into 'beginning', 'middle', and 'end'
    def month_segment(day):
        if day <= 10:
            return 'beginning'
        elif day <= 20:
            return 'middle'
        else:
            return 'end'

    df['MonthSegment'] = df['Day'].apply(month_segment)

    # One-hot encoding for 'MonthSegment'
    df = pd.get_dummies(df, columns=['MonthSegment'], drop_first=True)

    # Create additional features such as week of the year and quarter
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week
    df['Quarter'] = df['Date'].dt.quarter

    # Flag for month start and month end
    df['IsMonthEnd'] = df['Date'].dt.is_month_end.astype(int)
    df['IsMonthStart'] = df['Date'].dt.is_month_start.astype(int)

    return df
