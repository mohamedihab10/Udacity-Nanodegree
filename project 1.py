import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = { 'january': 1,
                'february': 2,
                'march': 3,
                'april': 4,
                'may': 5,
                'june': 6}

DAY_DATA = { 'monday': 0,
                'tuesday': 1,
                'wednesday': 2,
                'thursday': 3,
                'friday': 4,
                'saturday': 5,
                'sunday':6}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        print("which city you want to look for")
        city = input('chicago / new york city / washington ').lower()
        while city not in ['chicago' , 'new york city' , 'washington']:
            city = input ('kindly enter a valid choice ')
            
        city= CITY_DATA[city]
        break
    #ask if use want to filter the data 
    while 1:        
         filter= input("you can filter by month / day / both / none ").lower()
         print()
    # TO DO: get user input for month (all, january, february, ... , june)
         if filter == "month":
            month= input('January, February, March, April, May, June ').lower()
            if month not in MONTH_DATA:
                print("kindly enter a valid choice")
                continue
            month= MONTH_DATA[month]
            day='all'
   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
         elif filter=='day':
                print('Which day\'s data to look at? ')
                day = input('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ').lower()
                print()
                if day not in DAY_DATA:
                    print('kindly enter a valid choice')
                    continue
                day = DAY_DATA[day]
                month='all'
         elif filter=='both':
                print('Which month\'s data to look at?')
                month = input('January, February, March, April, May, June ').lower()
                print()
                if month not in MONTH_DATA:
                    print('kindly enter a valid choice')
                    continue
                month = MONTH_DATA[month]
                print('And day of the week?')
                day = input('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ').lower()
                print()
                if day not in DAY_DATA:
                    print('kindly enter a valid choice')
                    continue
                day = DAY_DATA[day]
         elif filter=='none':
            day='all'
            month='all'
         else:
                print('kindly enter a valid choice')
                continue
         break     
    print("your data will be filtered by {} city  ,{} month ,{} day".format(city, month ,day))
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
    df = pd.read_csv(city)
    df['day_of_week']=pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month']=pd.to_datetime(df['Start Time']).dt.month
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    if day != 'all':
        df= df[df['day_of_week']==day]
    if month != 'all':
        df = df[df['month'] == month]
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    freq_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num] == freq_month:
         freq_month = num.title()
    print('the most common month for travel is {}'.format(freq_month))
    # TO DO: display the most common day of week
    freq_day = df['day_of_week'].mode()[0]
    print('The most common day of week for travel is {}'.format(freq_day))
    
    # TO DO: display the most common start hour
    freq_hour= df['hour'].mode()[0]
    df.drop('hour' ,axis=1 , inplace= True)
    df.drop('day_of_week' ,axis=1 , inplace= True)
    df.drop('month' ,axis=1 , inplace= True)
    df.unique()
    df
    print('The most common day of week for travel is {}'.format(freq_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print()
    print("the most start station is {}".format(df["Start Station"].mode()[0]))
    

    # TO DO: display most commonly used end station
    print()
    print("the most start station is {}".format(df["End Station"].mode()[0]))
    
    
    # TO DO: display most frequent combination of start station and end station trip
    freq_station_comb = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequnt combination of start station and end station trip was {}'.format(freq_station_comb.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    print()
    print('trip duration total {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print()
    print('trip duration average {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print()
    types_of_users = df.groupby('User Type',as_index=False).count()
    print('Number of types of users are {}'.format(len(types_of_users)))
    for i in range(len(types_of_users)):
        print('{}s - {}'.format(types_of_users['User Type'][i], types_of_users['Start Time'][i]))

    # TO DO: Display counts of gender
    print()
    if 'Gender' not in df:
        print('no gender data for this city')
    else:
        print('the count of the gender type {}'.format(df['Gender'].value_counts()))
    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    if 'Birth Year' not in df:
        print('no birth data for this city')
    else:
        print('Earliest year of birth was {}.'.format(int(df['Birth Year'].min())))
        print('Most recent year of birth was {}.'.format(int(df['Birth Year'].max())))
        print('Most common year of birth year was {}.'.format(int(df['Birth Year'].mode().values[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    choice = input('Would you like to read some of the raw data? Yes/No ').lower()
    print()
    if choice=='yes':
        choice=True
    elif choice=='no':
        choice=False
    else:
        print('kindly enter a valid choice. ')
        display_data(df)
        return

    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('Another five? Yes/No ').lower()
            if choice=='yes':
                continue
            elif choice=='no':
                break
            else:
                print('kindly enter a valid choice.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        print()
        if restart != 'yes' :
            break

if __name__ == "__main__":
	main()