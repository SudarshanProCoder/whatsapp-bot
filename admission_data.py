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
    "top_college": {
        "patterns": ["top 10 computer science engineering colleges in maharashtra", "top 10"],
        "response": """1.Indian Institute of Technology (IIT) Bombay - Mumbai
2.College of Engineering, Pune (COEP) - Pune
3.Veermata Jijabai Technological Institute (VJTI) - Mumbai
4.Institute of Chemical Technology (ICT) - Mumbai
5.Visvesvaraya National Institute of Technology (VNIT) - Nagpur
6.Maharashtra Institute of Technology (MIT) - Pune
7.Sardar Patel Institute of Technology (SPIT) - Mumbai
8.Bharati Vidyapeeth Deemed University College of Engineering - Pune
9.Dr. D. Y. Patil Institute of Engineering, Management & Research - Pune
10.Fr. Conceicao Rodrigues College of Engineering (CRCE) - Mumbai"""
    },

    "college_brochure": {
        "patterns": ["cs syllabus for 3rd year", "college pdf 3rd", "3rd year syllabus"],
        "response": "Sure! Here's the college brochure PDF:",
        "media": "https://www.sakec.ac.in/wp-content/uploads/2022/06/6.TE_Syllabus_R2019-July9-1-2-min.pdf"
    },
    "college_brochure_2nd_year": {
        "patterns": ["college pdf 2nd", "cs syllabus for 2nd year"],
        "response": "Sure! Here's the college brochure PDF:",
        "media": "https://www.sakec.ac.in/wp-content/uploads/2022/06/3.CMPN_SE_2019-min.pdf"
    },
    "college_brochure_4th_year": {
        "patterns": ["4th year CS syllabus", "cs syllabus for 4th year"],
        "response": "Sure! Here's the college brochure PDF:",
        "media": "https://www.sakec.ac.in/wp-content/uploads/2022/12/6.41_BE_Comp_Engg_R2019-SemVII_compressed.pdf"
    },
    
    
    "college_images_sakec": {
        "patterns": ["shah and anchor college some images"],
        "response": "Here are some images of the college:",
        "media": [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwBbrylt_c5A3mFSXRiyeOty4Vb2JMXS3ct1Fsq6yA4g&s",
            "https://shahandanchor.com/metsmartcampus/Images/College.JPG",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNy3HAXToUxQqnDt7Bww1huuuGTEqyle7Ak37t4kJuXg&s",
            "https://www.collegebatch.com/static/clg-gallery/shah-anchor-kutchhi-engineering-college-mumbai-255920.jpg",
            "https://www.sakec.ac.in/wp-content/uploads/2022/06/cs-banner1.jpg",
            "https://shahandanchor.com/metsmartcampus/Images/prog_21-22.jpg"
        ]
    },
    "college_images_vjti": {
        "patterns": ["vjti college some images"],
        "response": "Here are some images of the college:",
        "media": [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe2onkI-3aPqdhZgWXw9HdwGqEp13KUYSgEaNcoq5qUQ&s",
            "https://images.shiksha.com/mediadata/images/1601280545phpx65J3D.png",
            "https://upload.wikimedia.org/wikipedia/commons/0/0e/VJTI_College_Quadrangle.jpg",
            "https://upload.wikimedia.org/wikipedia/en/6/6c/VJTI-Mumbai-Logo.png"
        ]
    },
       "college_images_swami": {
        "patterns": ["swami vivekanand college some images"],
        "response": "Here are some images of the college:",
        "media": [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEVdhmakE6jLu1JW1u4NbcLpksfjpkhpjvmpGiVVJjIQ&s",
            "https://images.shiksha.com/mediadata/images/1553752427phpvP6G9K.png",
            
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
   
    "c_programming":{
        "patterns": ["c programming youtube video"],
        "response": "c programming youtube video",
        "links": [
           "https://youtu.be/irqbmMNs2Bo?si=LEO_tFa1foJ6W-j1"
        ]
    },
    
    "java_programming":{
        "patterns": ["java programming youtube video"],
        "response": "java programming youtube video",
        "links": [
           "https://youtu.be/UmnCZ7-9yDY?si=7jLN7eorqOLpO4gW"
        ]
    },
    "python_programming":{
        "patterns": ["python programming youtube video"],
        "response": "python programming youtube video",
        "links": [
           "https://youtu.be/ERCMXc8x7mc?si=2J83GVhL5b-EMIXB"
        ]
    },
     "DSA":{
        "patterns": ["dsa in cpp youtube video"],
        "response": "DSA in cpp youtube video",
        "links": [
           "https://youtu.be/z9bZufPHFLU?si=zKTV_L76Fkm2a17v"
        ]
    },
    "coder":{
        "patterns": ["any linkedin profile"],
        "response": "linkedin profile",
        "links": [
           "https://www.linkedin.com/sudarshan-date"
        ]
    },
    
    "github":{
        "patterns": ["any github profile"],
        "response": "linkedin profile",
        "links": [
           "https://github.com/SudarshanProCode"
        ]
    },
    "EWS":{
        "patterns": ["How can I get qualified  for EWS? What is the criteria?, Am I EWS Candidate?"],
        "response": "To be eligible for EWS your annual family income should be below 8 lakh rupees, applicants should belong to the general category and the resident should be of Maharashtra.",
    },
    "Management Quota":{
        "patterns": ["Can I get admission through management quota using my CET score?"],
        "response": "Some colleges may offer admission through management quota, which usually requires a separate application process and higher fees.",
    },
    
        "greeting":{
        "patterns": [ "Hi there"],
        "response":"how can I help?"
    },
          "goodbye":{
        "patterns": ["bye","see you later"],
        "response":"Bye! Come back again soon."
    },
    "options":{
        "patterns": [ "how you could help me?",
                "what you can do?",
                "what help you provide?"],
        
        "response":"I can assist you with queries related to admission in engineering colleges in Maharashtra after 12th standard. Whether you need information about eligibility criteria, application process, important dates, or any other aspect of admission, feel free to ask!"
    },
        "After allocation of Seat":{
        "patterns": ["what is the process after you get allocated in any college?"],
        
        "response": "Candidates will have the option to freeze, slide, or float their allotted seats. Freeze: Students who are satisfied with the allotted seats and do not want to participate in other rounds of MHT CET 2024 counselling will needs to login to the MHT CET candidate portal and choose the “Accept and Freeze” option. After the option is selected, the candidate will be issued a provisional seat allotment letter with details of college and branch with details of seat confirmation fee to be paid. Candidates will need to pay the fees online through credit/debit card or internet banking. Once the fee payment is done, the seat allotment will be confirmed. Slide: Students who want to accept the allotted seat but also are open to upgrading to the higher preferred course in the same institute should choose the option “Slide”. However, it must be noted that if the candidate is allotted a higher preferred course, the previously allotted seat will be canceled.Float: Students who have been allotted a seat in previous seat allotment rounds and now wish to upgrade to any course at any college/institute will have to select the option “Float”. If they are upgraded to another course or institute, the previously allotted seat will be canceled."
    },
        "Documents":{
        "patterns": ["documents required?"],
        
        "response":  "To participate in the MHT CET counselling, candidates will need to upload the following documents at the time of registration. [1].Class 10 Pass Certificate & Mark Sheet [2].Class 12 Pass Certificate & Mark Sheet [3].Copy of MHT CET Result/Scorecard [4].Character Certificate [5].Migration Certificate [6].Category Certificate (if applicable) [7].School Leaving Certificate [8].Domicile Certificate of Maharashtra (if applicable) [9].MHT CET Admit Card The original copy of all the above listed documents will have to be uploaded while filling the counselling registration form and must be submitted to the institute for verification at the time of admission to the allotted institute. "
    },
    
    
}