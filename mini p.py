import mysql.connector
import datetime

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="movie_booking"
    )
    cursor = conn.cursor()
    print("Connected to the database successfully!")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

# Booking program
print("OFF on Wednesdays")
date = str(input("Enter the date of booking (DD MM YYYY): "))
print("Type the date in format DD MM YYYY")
print("Available movies with ticket prices:")
y = [
    "Monday = 170", 
    "Tuesday = 170", 
    "Wednesday = Off Day", 
    "Thursday = 220", 
    "Friday = 300", 
    "Saturday = 300", 
    "Sunday = 320"
]
for w in y:
    print(w)

def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))
    date_obj = datetime.datetime(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]

day_of_week = findDay(date)
print(f"The day of the week for {date} is: {day_of_week}")

name = str(input("Enter Your Name: "))
contact_no = int(input("Enter Your Mobile No.: "))
print("Select the movie: \n1. Bhool Bhulaiyaa 3D\n2. Ghazini 2\n3. Higher\n4. Raone 2")
movie_choice = int(input("Enter the SR.No. of Movie: "))

movies = {1: "Bhool Bhulaiyaa 3D", 2: "Ghazini 2", 3: "Higher", 4: "Raone 2"}
movie = movies.get(movie_choice, "Unknown")
duration = {1: 2.5, 2: 1.5, 3: 2, 4: 2.5}
u = duration.get(movie_choice, 0)

if u == 0:
    print("Invalid movie selection!")
    exit()

quantity = int(input("No. of People: "))

ticket_prices = {
    "Monday": 170,
    "Tuesday": 170,
    "Thursday": 220,
    "Friday": 300,
    "Saturday": 300,
    "Sunday": 320
}

if day_of_week in ticket_prices:
    ticket_price = ticket_prices[day_of_week]
    amount = quantity * ticket_price * u
    print(f"Ticket price = {ticket_price * u}")
    print(f"Total Amount = {amount}")
else:
    print("Sorry, no bookings allowed on Wednesdays.")
    exit()

# Confirm booking
confirm = int(input("For Confirm Booking Press 1 else 0: "))
if confirm == 1:
    print(f"Congrats {name}, your tickets have been booked! Enjoy your movie!")
    
    # Insert booking details into the database
    try:
        cursor.execute(
            "INSERT INTO bookings (name, contact_no, movie, booking_date, day_of_week, quantity, amount) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, contact_no, movie, datetime.datetime.strptime(date, '%d %m %Y').date(), day_of_week, quantity, amount)
        )
        conn.commit()
        print("Booking saved to the database successfully!")

    except mysql.connector.Error as e:
        print(f"Error saving booking to database: {e}")
        conn.rollback()

elif confirm == 0:
    print("Sorry, your booking is cancelled.")
else:
    print("Invalid input. Booking process terminated.")

# Close the database connection
cursor.close()
conn.close()

