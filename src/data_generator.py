import pandas as pd
import random
from faker import Faker

fake = Faker()

routes = [
    ("Delhi","Jaipur"),
    ("Mumbai","Ahmedabad"),
    ("Chennai","Bangalore"),
    ("Hyderabad","Vijayawada"),
    ("Kolkata","Patna"),
    ("Delhi","Lucknow")
]

data = []

for i in range(10000):

    source, dest = random.choice(routes)

    train_id = random.randint(12000,13000)

    date = fake.date_between(start_date="-60d", end_date="today")

    hour = random.randint(0,23)

    time = f"{hour}:00"

    coaches = random.randint(10,16)

    passenger_count = random.randint(500,1200)

    platform = random.randint(1,10)

    delay = random.randint(0,30)

    holiday = random.choice([0,1])

    data.append([
        train_id, source, dest, date, time,
        passenger_count, coaches, platform, delay, holiday
    ])

columns = [
    "Train_ID","Source","Destination","Date","Time",
    "Passenger_Count","Coaches","Platform","Delay","Holiday"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/railway_data.csv", index=False)

print("Dataset generated successfully!")