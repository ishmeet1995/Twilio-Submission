from flask import Flask, request, json
from twilio.rest import Client
from configparser import ConfigParser
import logging
from News_API_Interactor import News
from Database_Interactor import DatabaseInteractor


app = Flask(__name__)


@app.route('/whatsapp', methods=['POST'])
def route():
    # Print the JSON String of input
    print(request.form)
    # Print the message sent by user
    sender_msg = request.form['Body']
    print(request.form['Body'])
    news = news_obj.top_headlines()

    # Print the number of person who received the message
    sender_num = request.form['From']
    receiver_num = request.form['To']

    # Initializing Twilio Client Object for sending a message
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=receiver_num,
                                     body=f"Today's News \n {news}",
                                     to=sender_num)
    print(message.sid)

    return '200 OK'




def custom_log_setup():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    return logging

if __name__ == '__main__':
    # Reading Config file
    parser = ConfigParser()
    parser.read('config.ini')
    account_sid = parser.get('Twilio_Credentials', 'Account_SID')
    auth_token = parser.get('Twilio_Credentials', 'Auth_Token')
    news_api = parser.get("News_Credentials", "API_Key")
    database_host = parser.get("Database_Credentials", "Host")
    database_user = parser.get("Database_Credentials", "User")
    database_password = parser.get("Database_Credentials", "Password")
    database_name = parser.get("Database_Credentials", "Database")
    database_port = parser.get("Database_Credentials", "Port")

    # Setting up logs
    log = custom_log_setup()
    log.info("Process Started")

    # Creating Database and News Objects
    db_obj = DatabaseInteractor(host=database_host, port=database_port, user=database_user, password=database_password,
                                database=database_name)
    news_obj = News(news_api)

    app.run(debug=True, port=5000)



