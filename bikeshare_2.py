"""
    This project is coded in Python. It provides statistical analysis about bike share systems for 3 cities in United States; Chicago, New York City and Washington.
    In addition to providing descriptive statistical values code also provides interactive experience to the user where he/she can focus on particular city.
    Also user has an option to view raw data 5 roes at a time.

    Iteration count = 2
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city='chii'
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        global city
        city=input('Enter city choice from chicago, new york city, washington=')
        city=city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Invalid city entered, please try again. Valid options are chicago, new york city, washington')






    # get user input for month (all, january, february, ... , june)
    while(True):
        month=input('Enter month (all, january, february, ... , june)=')
        month=month.lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print('Invalid month option entered. Please try again.')



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        day=input('Enter day of week (all, monday, tuesday, ... sunday)')
        day=day.lower()
        if day in ['all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print('Invalid day entered, please try again')

    print('Details entered are ',city,' ',month,' ',day)



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour
    #print(df.head())
    if(month != 'all'):
        #Do needed filtering to get data for that month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        print('converted integer month is ',month)

        # filter by month to create the new dataframe
        df = df[df['month']==month]


    if(day != 'all'):
        #Do needed filtering for specified day
        days_of_the_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('most common month is ',df['month'].mode()[0])

    # display the most common day of week
    print('most common day of week is ',df['day_of_week'].mode()[0])


    # display the most common start hour
    print('most common start hour is ',df['start hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('most commonly used start station is ',df['Start Station'].mode()[0])


    # display most commonly used end station
    print('most commonly used end station is ',df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    #print('most frequent combinatin of start and end station is= ',type(df[['Start Station','End Station']].mode()))
    print('most frequent combinatin of start and end station is= ',df[['Start Station','End Station']].mode().iat[0,0],' & ',df[['Start Station','End Station']].mode().iat[0,1])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total ttrip duration is =',(df['Trip Duration'].sum())/60,' minutes ')
    print('-'*40)



    # display mean travel time
    print('Average ttrip duration is =',(df['Trip Duration'].mean())/60,' minutes')
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('-'*40)
    print('Count of Customer type is ',len(df[df['User Type']=='Subscriber']))
    print('Count of Customer type is ',len(df[df['User Type']=='Customer']))
    print('Count of Dependent type is ',len(df[df['User Type']=='Dependent']))
    print('-'*40)


    if 'Gender' in df:
        # Display counts of gender
        print('-'*40)
        print('Count of Male members is ',len(df[df['Gender']=='Male']))
        print('Count of Female members is ',len(df[df['Gender']=='Female']))
        print('-'*40)

    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth

        #Display Recent year of birth
        print('-'*40)
        print('Recent birth year is ',int(df['Birth Year'].max()))
        #Display ealiest year of birth
        print('-'*40)
        print('Earliest birth year is ',int(df['Birth Year'].min()))
        #Display most common year of birth
        print('-'*40)
        print('Most common birth year is ',int(df['Birth Year'].median()))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        #print('City being analyzed is ',city)

def display_raw_data(df):
    i=0
    while True:
        raw_data_choice=input('\nWould you like to see 5 lines of raw data? Enter yes or no\n')
        if raw_data_choice.lower() == 'yes':
            print(df[i:i+5])
            i += 5
            print('-'*20)
            continue
        elif raw_data_choice.lower() == 'no':
            break;


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if len(df) > 0:

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)
        else:
            print('There is no data for those parameters')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            break


if __name__ == "__main__":
	main()
