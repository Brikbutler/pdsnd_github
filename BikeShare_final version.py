import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
cities_data = ['chicago', 'new york city', 'washington']

months_data = ['january', 'february', 'march', 'april', 'may', 'june']

days_data = ['sunday', 'monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday']


def get_filters():
    """
    Prompts user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! Including data from Chicago, Washington, and New York City')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please choose a city you want to learn more about from the following: Chicago, New York City or Washington. \n> ").lower(
        ).replace(" ", "")
        if city in cities_data:
            break
        else:
            print("\n\t" + city + " isn't valid, please enter a valid city.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose a month or type 'all' to apply no month filter.\n (Choices: all, january, february, march, april, may or june)\n>").lower(
        ).replace(" ", "")
        if month in months_data or month == "all":
            break
        else:
            print("\n\t ERROR: " + month + " isn't valid, please enter a month or 'all'.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please choose a day of the week or type 'all' to apply no day filter.\n (Choices: all, monday, tuesday, wednesday, thursday, friday, saturday or sunday)\n>").lower().replace(" ", "")
        if day in days_data or day == "all":
            break
        else:
            print("\n\t ERROR: " + day + " isn't valid, please enter a week day name or 'all'.")

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    most_common_month_name = months_data[most_common_month - 1].title()
    print(most_common_month_name + " is the most common month.")

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print(most_common_day_of_week, " is the most common day of the week.")

    # display the most common start hour

    most_common_start_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print(most_common_start_hour, " is the most common hour to start.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print(common_start_station, " is most commonly used start station.")

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print(common_end_station, " is most commonly used end station.")

    # display most frequent combination of start station and end station trip
    common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used combinations of start station and end station is {} and {}."
          .format(common_start_end_station[0], common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time, " is the total travel time.")

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("{:.2f} is the mean travel time.".format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    # printing out the total numbers of user types
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))

    # Display counts of gender
<<<<<<< HEAD
    print("\nCounts of Gender:\n")

||||||| merged common ancestors
    print("\nCounts of Gender:\n")
  
=======
    print("\nCount for each Gender:\n")

>>>>>>> refactoring
    found_gender = False
    found_birthyear = False

    for column in df:
        if column == 'Gender':
            found_gender = True
            gender_counts = df['Gender'].value_counts()
            # printing out the total numbers of genders
            for index, gender_count in enumerate(gender_counts):
                print("  {}: {}".format(gender_counts.index[index], gender_count))
        if column == 'Birth Year':
            found_birthyear = True
            # Display earliest, most recent, and most common year of birth
            birth_year = df['Birth Year']
            # earliest birth year
            earliest_year = birth_year.min()
            print(int(earliest_year), " is the earliest birth year.")
            # most recent birth year
            most_recent = birth_year.max()
            print(int(most_recent), " is the most recent birth year.")
            # most common birth year
            most_common_year = birth_year.value_counts().idxmax()
            print(int(most_common_year), " is the most common birth year.")
    if found_gender == False and found_birthyear == False:
        print('Neither found.')
    elif found_gender == False:
        print('Gender not found.')
    elif found_birthyear == False:
        print('Birth year not found.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
<<<<<<< HEAD


def display_raw(df):
||||||| merged common ancestors
 
def display_raw(df):
=======


def display_raw_data(df):
>>>>>>> refactoring
    """
    Displays only five rows of the data at a time.
    Input:
        the dataframe with all the bikeshare data
    Returns:
       none
    """
    # increment_value = 5 #number of rows to increment by
    #low_index = 0
    #high_index = increment_value
    # while True:
    #    show_more_data = input('\nWould you like to view individual trip data?'' Type \'yes\' or \'no\'.\n').lower()
    #    if show_more_data == 'yes':
    #        print(df.iloc[low_index,high_index])
    #        low_index += increment_value
    #        high_index += increment_value
    #        show_more_data = input('\nWould you like to view individual trip data?'' Type \'yes\' or #\'no\'.\n').lower()
    #    else:
    #        break

    # show_row_data = input('\nWould you like to view individual trip data?'' Type \'yes\' or #\'no\'.\n').lower()

    # print(row_index)
    row_index = 0
    while True:
        show_row_data = input(
            '\nWould you like to view individual trip data?'' Type \'yes\' or #\'no\'.\n').lower()
        if show_row_data == 'no':
            break
        else:
            print(df.iloc[row_index: row_index+5])
            row_index += 5


#    current_line = df.head()
#    while True:
#        show_row_data = input('\nWould you like to view individual trip data?'' Type \'yes\' or #\'no\'.\n').lower()
#        if show_row_data == 'yes':
           #current_line = print(df.head())
 #          print(df.head[current_line:current_line+5])
 #          current_line = current_line + 5
 #       return display_raw(df, current_line)
 #       if show_row_data == 'no':
 #           return
  #      else:
  #          print("\nNot a valid answer.")
   #         return display_raw(df, str(current_line))

   # show_row_data = input('\nWould you like to view individual trip data?'' Type \'yes\' or #\'no\'.\n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
<<<<<<< HEAD
        display_raw(df)

||||||| merged common ancestors
        display_raw(df)
        
=======
        display_raw_data(df)

>>>>>>> refactoring
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
