from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

# Define the intents for admission doubts
admission_doubts = {
     "eligibility_criteria": {
        "patterns": ["What are the eligibility criteria?", "Am I eligible for admission?"],
        "response": "To be eligible for admission, you need to have completed your high school education with a certain minimum percentage. Specific eligibility criteria may vary depending on the course and university. It's best to check the official admission guidelines of the institution you're interested in."
    },
    "application_process": {
        "patterns": ["How do I apply for admission?", "What is the application process?"],
        "response": "The application process typically involves filling out an online application form, providing necessary documents such as transcripts and certificates, and paying the application fee. You should visit the official website of the university or college you're applying to for detailed instructions."
    },
    "important_dates": {
        "patterns": ["What are the important admission dates?", "When is the last date to apply?"],
        "response": "Important admission dates, including application deadlines, entrance exam dates (if applicable), and announcement of merit lists, are usually published on the official website of the university or college. Make sure to regularly check their website for updates."
    },
    "counselling_process": {
        "patterns": ["What is the counselling process?", "How does the counselling process work?"],
        "response": "The counselling process involves various stages such as registration, document verification, choice filling, seat allotment, and admission confirmation. It's conducted either online or in-person, depending on the institution. You'll receive detailed instructions from the university or college regarding the counselling process."
    },
    "Seat Acceptance":{
		"patterns": [
                "What Is the procedure to accept the allotted Seat in counselling?",
            ],
            "response": "Once a candidate is allotted a seat, he/she needs to login to the MHT CET candidate portal and choose the “Accept and Freeze” option. After the option is selected, the candidate will be issued a provisional seat allotment letter with details of college and branch with details of seat confirmation fee to be paid. Candidates will need to pay the fees online through credit/debit card or internet banking. Once the fee payment is done, the seat allotment will be confirmed."     
	},
    
    "CET Website" : {
		"patterns": [
                "Where can I check MHT CET counselling dates?",
            ],
		 "response": "MHT CET portal: https://cetcell.mahacet.org/"
	},

    "college_brochure": {
        "patterns": ["college brochure", "college pdf", "send me 3rd year syllabus"],
        "response": "Sure! Here's the college brochure PDF:",
        "media": "https://www.sakec.ac.in/wp-content/uploads/2022/06/6.TE_Syllabus_R2019-July9-1-2-min.pdf"
    },
    "college_images": {
        "patterns": ["college pic", "college image", "show me images of the college"],
        "response": "Here are some images of the college:",
        "media": [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwBbrylt_c5A3mFSXRiyeOty4Vb2JMXS3ct1Fsq6yA4g&s",
            "https://shahandanchor.com/metsmartcampus/Images/College.JPG",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNy3HAXToUxQqnDt7Bww1huuuGTEqyle7Ak37t4kJuXg&s"
        ]
    },
   "study_tips": {
        "patterns": ["how to study", "study tips"],
        "response": "Here are some study tips for you:",
        "links": [
            "https://youtu.be/Zff3rUY0iGg?si=SB4CbjnjPLKI9Lst",
            "https://www.youtube.com/watch?v=BfkzMyMdfSI"
        ]
    },
}

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the incoming message from Twilio
    incoming_msg = request.values.get('Body', '').lower()
    
    # Process the incoming message and generate a response
    response = process_message(incoming_msg)
    
    # Send the response back to Twilio
    return str(response)

def process_message(message):
    # Match the incoming message with known patterns
    for intent, data in admission_doubts.items():
        for pattern in data["patterns"]:
            
            if pattern in message:
                if intent == "college_brochure":
                        return send_media(data["response"], data["media"], is_pdf=True)
                elif intent == "college_images":
                        return send_media(data["response"], data["media"])
                elif intent == "study_tips":
                    response = data["response"] + "\n"
                    for link in data["links"]:
                        response += link + "\n"
                    return create_twilio_response(response)
                else:
                    return create_twilio_response(data["response"])
            
    return create_twilio_response("I'm sorry, I couldn't understand your question. Please ask something else or visit the admission section of the university website for more information.")
       
    
       
    

def create_twilio_response(message):
    twilio_response = MessagingResponse()
    twilio_response.message(message)
    return twilio_response

def send_media(response_text, media_urls, is_pdf=False):
    # Create Twilio response with media attachments
    twilio_response = MessagingResponse()
    twilio_response.message(response_text)
    
    if is_pdf:
        twilio_response.message(media_urls)
    else:
        for media_url in media_urls:
            twilio_response.message().media(media_url)
    
    return twilio_response


if __name__ == "__main__":
    app.run(debug=True)
