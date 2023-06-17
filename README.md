# MassMail

MassMail is a web application built using Django that allows users to send mass emails to a list of recipients using CSV files. This project is intended as a practice project and serves as a basic version 1 implementation.

## Features

- User-friendly Interface: MassMail provides a simple and intuitive user interface where users can upload a CSV file containing the recipient's email addresses and other relevant information.
    
- CSV File Integration: The application supports importing recipient data from CSV files, allowing users to easily manage and update their mailing lists.
    
- Email Composition: Users can compose personalized emails using a rich text editor, including the ability to add attachments and customize the email content.
    
- Batch Sending: The application is designed to handle large email lists by sending emails in batches, ensuring efficient and reliable delivery.
    
- Email Status Tracking: MassMail keeps track of the email delivery status, providing users with information on sent, delivered, and bounced emails.
    

## Installation

1. Clone the repository:

bashCopy code

`git clone https://github.com/NagiPragalathan/MassMail.git` 

2. Navigate to the project directory:

bashCopy code

`cd MassMail` 

3. Create and activate a virtual environment:

bashCopy code

`python3 -m venv venv
source venv/bin/activate` 

4. Install the required dependencies:

bashCopy code

`pip install -r requirements.txt` 

5. Set up the database:

bashCopy code

`python manage.py migrate` 

6. Start the development server:

bashCopy code

`python manage.py runserver` 

7. Access the application in your web browser at `http://localhost:8000`.

Please note that this is a practice project and should not be used for sending mass emails without proper consent and compliance with applicable laws and regulations.

## Contributing

Contributions to MassMail are welcome! If you would like to contribute to this project, please follow the [contribution guidelines]().

## License

This project is licensed under the [MIT License](https://chat.openai.com/LICENSE).

## Contact

If you have any questions or suggestions, please feel free to reach out to us at [email@example.com](mailto:nagipragalathan@gmail.com).

Enjoy using MassMail to simplify your mass email sending process!

Hashtags: #massmail #django #webapplication #emailmarketing #csvintegration #emailcommunication
