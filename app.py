from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Define the help options
help_options = [
    ("Admission Doubts", "Send 'admission' to get help with admission-related queries."),
    ("Study Tips", "Send 'study tips' to receive study tips."),
    ("College Information", "Send 'college info' to get information about the college."),
    # Add more help options as needed
]

# Define the intents for admission doubts
admission_doubts = {
    "eligibility_criteria": {
        "patterns": ["eligibility criteria", "eligible for admission"],
        "response": "To be eligible for admission, you need to have completed your high school education with a certain minimum percentage. Specific eligibility criteria may vary depending on the course and university. It's best to check the official admission guidelines of the institution you're interested in."
    },
    "application_process": {
        "patterns": ["apply for admission", "application process"],
        "response": "The application process typically involves filling out an online application form, providing necessary documents such as transcripts and certificates, and paying the application fee. You should visit the official website of the university or college you're applying to for detailed instructions."
    },
    "important_dates": {
        "patterns": ["important admission dates", "last date to apply"],
        "response": "Important admission dates, including application deadlines, entrance exam dates (if applicable), and announcement of merit lists, are usually published on the official website of the university or college. Make sure to regularly check their website for updates."
    },
    "counselling_process": {
        "patterns": ["counselling process", "how does counselling work"],
        "response": "The counselling process involves various stages such as registration, document verification, choice filling, seat allotment, and admission confirmation. It's conducted either online or in-person, depending on the institution. You'll receive detailed instructions from the university or college regarding the counselling process."
    },
    "seat_acceptance": {
        "patterns": ["procedure to accept allotted seat in counselling"],
        "response": "Once a candidate is allotted a seat, he/she needs to login to the MHT CET candidate portal and choose the 'Accept and Freeze' option. After the option is selected, the candidate will be issued a provisional seat allotment letter with details of college and branch with details of seat confirmation fee to be paid. Candidates will need to pay the fees online through credit/debit card or internet banking. Once the fee payment is done, the seat allotment will be confirmed."     
    },
    
    "cet_website": {
        "patterns": ["where to check MHT CET counselling dates", "website"],
        "response": "MHT CET portal: https://cetcell.mahacet.org/"
    },

    "college_brochure": {
        "patterns": ["college brochure", "college pdf", "3rd year syllabus"],
        "response": "Sure! Here's the college brochure PDF:",
        "media": "https://www.sakec.ac.in/wp-content/uploads/2022/06/6.TE_Syllabus_R2019-July9-1-2-min.pdf"
    },
    "college_images": {
        "patterns": ["college pic", "college image", "images of the college"],
        "response": "Here are some images of the college:",
        "media": [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwBbrylt_c5A3mFSXRiyeOty4Vb2JMXS3ct1Fsq6yA4g&s",
            "https://shahandanchor.com/metsmartcampus/Images/College.JPG",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNy3HAXToUxQqnDt7Bww1huuuGTEqyle7Ak37t4kJuXg&s"
        ]
    },
   "study_tips": {
        "patterns": ["study tips"],
        "response": "Here are some study tips for you:",
        "links": [
            "https://youtu.be/Zff3rUY0iGg?si=SB4CbjnjPLKI9Lst",
            "https://www.youtube.com/watch?v=BfkzMyMdfSI"
        ]
    },
}

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
