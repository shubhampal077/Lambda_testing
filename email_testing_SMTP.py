import json
import smtplib as s
def lambda_handler(event, context):
    # TODO implement
    
    server=s.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("shubhampalmanit@gmail.com","Password-encrypted")
    subject="Hi Lambda from Shubham!"
    body="This e-mail is for test purpose only"
    message="Subject:{}\n\n{}".format(subject,body)
    # print(message)
    listOfAddress=["shubhampalggps@gmail.com","sauravpal@gmail.com","harshil@gmail.com"]
    server.sendmail("shubhampalmanit",listOfAddress,message)
    print("Send Successfully!")
    server.quit()
    print('Hi Shubham how are you!')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
