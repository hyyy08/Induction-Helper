#Generate a CSV file with random user data
import csv
import random

def generate_csv(filename, num_rows):

    headers = ['barcode', 'email', 'firstname', 'surname']
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        # Generate random data for each row
        for i in range(num_rows):
            # Create a unique barcode
            barcode = 100000 + i

            # Generate names
            firstname = random.choice(['Valtteri', 'Lewis', 'Daniel', 'Michael', 'Pierre', 'Alexander', 'Yuki', 'Max', 'Fernando', 'Lando' ])
            surname = random.choice(['Sainz', 'Russell', 'Leclerc', 'Perez', 'Stroll', 'Hulkenberg', 'Magnussen', 'Ocon', 'Gasly'])

            # Generate email
            email = f"{firstname.lower()}@student.curtin.edu.au"

            # Write the row to the CSV file.
            writer.writerow([barcode, email, firstname, surname])

if __name__ == "__main__":
    generate_csv('large_test_data.csv', 10000)  # 10000 rows