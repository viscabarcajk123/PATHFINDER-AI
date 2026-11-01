"""Top 3 courses for every Pathfinder AI field.
Keys must match the field names in streams.py exactly.
Each course is (course name, where to study / how to get in). Indian options first.
Admissions, seat counts and entrance exams change every year, so always confirm on the official websites."""

COURSES = {
    # ------------------------------------------------------------ SCIENCE
    "Computer Science and AI": [
        ("B.Tech Computer Science and Engineering", "IITs, NITs, IIITs · JEE Advanced / JEE Main"),
        ("B.Tech Artificial Intelligence / AI and Data Science", "IIT Hyderabad, IIT Jodhpur · JEE Advanced"),
        ("B.Sc (Hons) Computer Science", "University of Delhi · CUET-UG"),
    ],
    "Robotics and Automation": [
        ("B.Tech Robotics and Automation Engineering", "Offered by several universities; check current availability"),
        ("B.Tech Mechatronics Engineering", "MIT Manipal, SRM Institute of Science and Technology"),
        ("B.Tech Electronics and Communication Engineering", "NITs, IIITs · JEE Main"),
    ],
    "Aerospace and Aviation": [
        ("B.Tech Aerospace Engineering", "IIT Bombay, IIT Madras, IIT Kanpur, IIT Kharagpur · JEE Advanced"),
        ("B.Tech Aerospace Engineering", "Indian Institute of Space Science and Technology (IIST), Thiruvananthapuram · JEE Advanced"),
        ("B.Tech Aeronautical Engineering", "Madras Institute of Technology (Anna University), Punjab Engineering College"),
    ],
    "Medicine and Surgery": [
        ("MBBS", "AIIMS, JIPMER, government and private medical colleges · NEET-UG"),
        ("BDS (Bachelor of Dental Surgery)", "Government and private dental colleges · NEET-UG"),
        ("BAMS (Ayurvedic Medicine and Surgery)", "AYUSH-recognised colleges · NEET-UG"),
    ],
    "Psychology and Neuroscience": [
        ("B.A. / B.Sc (Hons) Psychology", "University of Delhi, Christ University, Fergusson College"),
        ("B.Sc Applied Psychology", "Christ University, Amity University"),
        ("BS-MS (Biology) for a neuroscience route", "IISERs · IISER Aptitude Test (IAT)"),
    ],
    "Biotech and Genetics": [
        ("B.Tech Biotechnology", "IIT Madras, IIT Kharagpur, NITs · JEE"),
        ("B.Sc (Hons) Biotechnology / Genetics", "University of Delhi, Jamia Millia Islamia · CUET-UG"),
        ("BS-MS (Biology)", "IISERs · IISER Aptitude Test (IAT)"),
    ],
    "Data Science and Finance": [
        ("B.Stat (Hons) Statistics", "Indian Statistical Institute (ISI) · ISI Admission Test"),
        ("BS in Data Science and Applications", "IIT Madras (online degree) · qualifier process"),
        ("B.Tech Mathematics and Computing", "IIT Kharagpur, IIT Delhi, NITs · JEE"),
    ],
    "Forensic Science": [
        ("B.Sc Forensic Science", "National Forensic Sciences University (NFSU), Gandhinagar and campuses"),
        ("Integrated B.Sc-M.Sc Forensic Science", "National Forensic Sciences University (NFSU)"),
        ("B.Sc Forensic Science", "Amity University, Lovely Professional University"),
    ],
    "Architecture and Design": [
        ("B.Arch (Bachelor of Architecture)", "SPA Delhi, IIT Kharagpur, IIT Roorkee, NITs · JEE Main Paper 2 / NATA"),
        ("B.Des (Bachelor of Design)", "IDC IIT Bombay · UCEED; NID · NID DAT"),
        ("B.Planning (Bachelor of Planning)", "SPA Delhi, CEPT University · JEE Main Paper 3"),
    ],
    "Smart Agriculture and Ecology": [
        ("B.Sc (Hons) Agriculture", "ICAR-accredited agricultural universities · CUET-UG (ICAR)"),
        ("B.Tech Agricultural Engineering", "IIT Kharagpur, TNAU Coimbatore"),
        ("B.Sc Environmental Science", "University of Delhi, Christ University"),
    ],

    # ----------------------------------------------------------- COMMERCE
    "Accounting and Auditing": [
        ("Chartered Accountancy (CA)", "ICAI · CA Foundation after Class 12"),
        ("B.Com (Hons)", "SRCC and other University of Delhi colleges · CUET-UG"),
        ("Cost and Management Accountancy (CMA)", "ICMAI · CMA Foundation after Class 12"),
    ],
    "Investment and Financial Markets": [
        ("Bachelor of Financial Markets (BFM)", "University of Mumbai affiliated colleges"),
        ("BBA (Financial Investment Analysis)", "Shaheed Sukhdev College of Business Studies, University of Delhi · CUET-UG"),
        ("CFA Program (alongside a degree)", "CFA Institute"),
    ],
    "Economics and Public Policy": [
        ("B.A. (Hons) Economics", "University of Delhi colleges · CUET-UG"),
        ("B.Sc Economics", "Presidency University, Kolkata"),
        ("B.A. (Hons) Economics", "Ashoka University"),
    ],
    "Business Management and Entrepreneurship": [
        ("Integrated Programme in Management (IPM)", "IIM Indore, IIM Rohtak · IPMAT"),
        ("BBA / BMS", "Narsee Monjee (NMIMS), Shaheed Sukhdev College of Business Studies · NPAT / CUET-UG"),
        ("BBA", "Symbiosis International University · SET"),
    ],
    "Marketing and Brand Strategy": [
        ("BBA (Marketing specialisation)", "Symbiosis, Christ University"),
        ("Bachelor of Mass Media (BMM) with Advertising", "University of Mumbai affiliated colleges"),
        ("B.Com (Hons) with Marketing", "Christ University, SRCC"),
    ],
    "Banking and Insurance": [
        ("B.Com (Banking and Insurance)", "University of Mumbai affiliated colleges"),
        ("BBA (Banking, Finance and Insurance)", "NMIMS, Christ University"),
        ("Graduation followed by bank exams", "IBPS PO / SBI PO after any degree"),
    ],
    "Corporate Law and Company Secretaryship": [
        ("Company Secretary (CS)", "ICSI · CSEET after Class 12"),
        ("B.B.A. LL.B (Hons)", "Symbiosis Law School · SLAT; Jindal Global Law School · LSAT-India"),
        ("B.A. LL.B (Hons)", "National Law Universities (NLSIU, NALSAR) · CLAT-UG"),
    ],
    "International Trade and Logistics": [
        ("BBA Logistics, Port and Shipping Management", "Indian Maritime University (IMU)"),
        ("BBA (International Business)", "Christ University, Amity University"),
        ("Short courses in Export-Import management", "Indian Institute of Foreign Trade (IIFT)"),
    ],
    "Human Resources and Organisational Behaviour": [
        ("BBA (Human Resource Management)", "Symbiosis, NMIMS"),
        ("B.A. (Hons) Psychology, then HR at postgraduate level", "University of Delhi, then XLRI Jamshedpur or TISS"),
        ("BBA", "Christ University, Shaheed Sukhdev College of Business Studies"),
    ],
    "Business Analytics and E-commerce": [
        ("BBA (Business Analytics)", "Shaheed Sukhdev College of Business Studies · CUET-UG"),
        ("BCA (Data Science)", "Christ University, Symbiosis"),
        ("BS in Data Science and Applications", "IIT Madras (online degree)"),
    ],

    # ---------------------------------------------------------- HUMANITIES
    "Law and Legal Studies": [
        ("B.A. LL.B (Hons)", "NLSIU Bangalore, NALSAR Hyderabad, WBNUJS Kolkata · CLAT-UG"),
        ("B.B.A. LL.B (Hons)", "Symbiosis Law School · SLAT; Jindal Global Law School · LSAT-India"),
        ("B.A. LL.B (5-year)", "Government Law College, Mumbai · MH CET Law"),
    ],
    "Political Science and Public Administration": [
        ("B.A. (Hons) Political Science", "University of Delhi colleges · CUET-UG"),
        ("B.A. (Hons) Political Science", "Banaras Hindu University, Jamia Millia Islamia · CUET-UG"),
        ("B.A. (Hons) Political Science", "Ashoka University"),
    ],
    "Psychology and Counselling": [
        ("B.A. (Hons) Psychology", "Lady Shri Ram College, University of Delhi · CUET-UG"),
        ("B.A. / B.Sc Psychology", "Christ University"),
        ("B.A. Psychology", "Fergusson College, Pune"),
    ],
    "Sociology and Social Work": [
        ("B.A. (Hons) Sociology", "University of Delhi colleges · CUET-UG"),
        ("B.A. in Social Sciences", "Tata Institute of Social Sciences (TISS) · TISS-BAT"),
        ("Bachelor of Social Work (BSW)", "Delhi School of Social Work, University of Delhi"),
    ],
    "History and Archaeology": [
        ("B.A. (Hons) History", "St. Stephen's College, Hindu College, University of Delhi · CUET-UG"),
        ("B.A. (Hons) Ancient Indian History, Culture and Archaeology", "Banaras Hindu University"),
        ("B.A. History", "Presidency University, Kolkata"),
    ],
    "Journalism and Mass Communication": [
        ("B.A. (Hons) Journalism", "Delhi University colleges (e.g. Kalindi, Gargi) · CUET-UG"),
        ("Bachelor of Journalism and Mass Communication (BJMC)", "Symbiosis Institute of Media and Communication, Manipal"),
        ("Bachelor of Mass Media (BMM)", "University of Mumbai affiliated colleges"),
    ],
    "Literature and Languages": [
        ("B.A. (Hons) English", "St. Stephen's College, Miranda House, University of Delhi · CUET-UG"),
        ("B.A. English", "English and Foreign Languages University (EFLU), Hyderabad"),
        ("B.A. English Literature", "Christ University, Presidency University"),
    ],
    "Education and Teaching": [
        ("Integrated Teacher Education Programme (ITEP, 4-year B.Ed)", "Selected institutions · NCET (NTA)"),
        ("B.El.Ed (Elementary Education)", "Delhi University colleges (e.g. Gargi, Lady Shri Ram) · CUET-UG"),
        ("B.A. B.Ed / B.Sc B.Ed", "Regional Institutes of Education (NCERT) · NCET"),
    ],
    "Fine Arts, Film and Performing Arts": [
        ("Bachelor of Fine Arts (BFA)", "Sir J.J. School of Art Mumbai, College of Art Delhi, BHU"),
        ("B.A. in Filmmaking", "Whistling Woods International, Mumbai"),
        ("Bachelor of Performing Arts (Music / Dance)", "Faculty of Music and Fine Arts, University of Delhi"),
    ],
    "International Relations and Diplomacy": [
        ("B.A. (Hons) International Relations", "Jindal School of International Affairs, Sonipat"),
        ("B.A. (Hons) International Relations", "Jadavpur University, Kolkata · entrance test"),
        ("B.A. (Hons) Political Science with IR focus", "University of Delhi · CUET-UG"),
    ],
}
