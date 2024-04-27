from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from admission_data import admission_doubts
app = Flask(__name__)

# Define the help options
help_options = [
    ("Admission Doubts", "Send 'admission' to get help with admission-related queries."),
    ("Study Tips", "Send 'study tips' to receive study tips."),
    ("College Information", "Send 'college info' to get information about the college."),
    # Add more help options as needed
]



@app.route('/webhook', methods=['POST'])
def webhook():
    
    incoming_msg = request.values.get('Body', '').strip().lower()
   
    response = process_message(incoming_msg)
    
    
    return str(response)

def process_message(message):
    # Check if the message is for help
    if message == 'help':
        return create_help_response()
    
    # Check if the message is related to admission doubts
    for intent, data in admission_doubts.items():
        for pattern in data["patterns"]:
            if pattern in message:
                return create_response(data)
    
    # If no match found, return a default response
    return create_default_response()

def create_response(data):
    twilio_response = MessagingResponse()
    twilio_response.message(data["response"])
   
    if "media" in data:
        if isinstance(data["media"], list):
            for media_url in data["media"]:
                twilio_response.message().media(media_url)
        else:
            twilio_response.message(data["media"]).media(data["media"])
    
   
    if "links" in data:
        message = "Links:\n"
        for link in data["links"]:
            message += f"{link}\n"
        twilio_response.message(message)
    
    return twilio_response

def create_help_response():
    help_text = "Here are some options to get help:\n\n"
    for option in help_options:
        help_text += f"{option[0]}: {option[1]}\n"
    return MessagingResponse().message(help_text)

def create_default_response():
    return MessagingResponse().message("I'm sorry, I couldn't understand your request. Please type 'help' for assistance.")

if __name__ == "__main__":
    app.run(debug=True)
