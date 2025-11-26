from faker import Faker
import random
import pandas as pd

fake = Faker()

def transaction_generation(id):
    sender = fake.uuid4()
    receiver = fake.uuid4()
    amount = round(random.uniform(5, 5000), 2)

    timestamp = fake.date_time_this_year()
    tx_type = random.choice(['p2p','merchant','salary','bills','others'])
    city = fake.city()
    channel = random.choice(["mobile", "web", "offline", "bank_app"])

    is_international = random.choice([0, 1])
    country = random.choice([
        "Germany", "France", "Italy", "Spain", "Netherlands",
        "Belgium", "Austria", "Finland", "Portugal", "Ireland"
    ])

    risk_score = round(random.uniform(0, 1), 2)

    return {
        "transaction_id": id,
        "timestamp": timestamp,
        "sender": sender,
        "receiver": receiver,
        "location": city,
        "country": country,
        "amount": amount,
        "type": tx_type,
        "channel": channel,
        "is_international": is_international,
        "risk_score": risk_score
    }

def generate_dataset(n=5000):
    data = []
    for i in range(n):
        data.append(transaction_generation(i+1))

    df = pd.DataFrame(data)
    df.to_csv("data/transactions.csv", index=False)

if __name__ == "__main__":
    generate_dataset()
