"""Single source of truth for all three Pathfinder AI streams.
Each stream has: 10 fields, 14 questions and a scoring rubric used to build the synthetic dataset."""

STREAMS = {}

# ---------------------------------------------------------------- SCIENCE
STREAMS["Science"] = {
    "slug": "science",
    "icon": "🔬",
    "fields": [
        ("Computer Science and AI", "score_computer_science_ai", "Combines programming, algorithms, software development and artificial intelligence to build digital tools and solve computational problems."),
        ("Robotics and Automation", "score_robotics_automation", "Combines mechanical design, electronics, sensors and programming to create machines that can perform tasks automatically."),
        ("Aerospace and Aviation", "score_aerospace_aviation", "Explores aircraft, spacecraft, flight systems, propulsion and the physics behind vehicles in the air and space."),
        ("Medicine and Surgery", "score_medicine_surgery", "Focuses on human health, anatomy, disease diagnosis, treatment and clinical care. Entry requirements vary by course and institution."),
        ("Psychology and Neuroscience", "score_psychology_neuroscience", "Examines behaviour, emotion, cognition and the nervous system. Professional clinical roles may require further approved study."),
        ("Biotech and Genetics", "score_biotech_genetics", "Applies biology, microbiology, molecular science and genetics in laboratories, research, healthcare, agriculture and industry."),
        ("Data Science and Finance", "score_data_science_finance", "Uses mathematics, statistics, computing and analysis to interpret data and support financial or business decisions."),
        ("Forensic Science", "score_forensic_science", "Applies scientific methods to biological, chemical and physical evidence to support investigations and legal processes."),
        ("Architecture and Design", "score_architecture_design", "Combines spatial reasoning, geometry, creativity and technical planning to develop buildings and designed environments."),
        ("Smart Agriculture and Ecology", "score_smart_agriculture_ecology", "Combines plant and environmental sciences with technology to improve food systems and support sustainability."),
    ],
    "questions": [
        ("Q1_Computer_Coding", "I enjoy solving logical problems, writing code, or figuring out how software and applications work."),
        ("Q2_Robotics_Hardware", "I would enjoy building, assembling, or programming physical machines, electronic circuits, or robots."),
        ("Q3_Aerospace_Physics", "I am fascinated by aircraft, spacecraft, flight mechanics, engines, or the physics of moving objects."),
        ("Q4_Medicine_Anatomy", "I am interested in human anatomy, diseases, medical treatments, and how doctors diagnose and treat patients."),
        ("Q5_Psychology_Behaviour", "I enjoy understanding human emotions, behaviour, memory, mental health, and how the brain works."),
        ("Q6_Biotech_Genetics", "I would enjoy laboratory experiments involving cells, microorganisms, DNA, genes, or biological discoveries."),
        ("Q7_Math_Statistics", "I enjoy advanced mathematics, statistics, analysing numerical patterns, and using data to make decisions."),
        ("Q8_Forensic_Investigation", "I am curious about analysing chemical or biological evidence to investigate how an incident occurred."),
        ("Q9_Architecture_Design", "I enjoy visualising objects and buildings in three dimensions, working with geometry, and creating designs."),
        ("Q10_Ecology_Agriculture", "I would enjoy studying plants, ecosystems, agriculture, and technologies that protect the environment or make food production more sustainable."),
        ("Q11_Hands_On_Problem_Solving", "When something goes wrong, I like investigating the cause and testing solutions hands-on with equipment, labs, machinery, or field sites."),
        ("Q12_Research_Discovery", "I enjoy asking scientific questions, examining evidence, conducting experiments, and discovering explanations."),
        ("Q13_People_Care", "I would be comfortable working closely with people, listening to their concerns, and making careful decisions that affect their well-being."),
        ("Q14_Creativity_Innovation", "I like turning new ideas into useful inventions, designs, technologies, or practical solutions."),
    ],
    "rubric": {
        "score_computer_science_ai":       {"Q1_Computer_Coding": 10, "Q7_Math_Statistics": 3.5, "Q2_Robotics_Hardware": 2, "Q14_Creativity_Innovation": 2.5, "Q12_Research_Discovery": 1.5},
        "score_robotics_automation":       {"Q2_Robotics_Hardware": 10, "Q1_Computer_Coding": 3, "Q3_Aerospace_Physics": 3, "Q11_Hands_On_Problem_Solving": 3.5, "Q14_Creativity_Innovation": 2.5},
        "score_aerospace_aviation":        {"Q3_Aerospace_Physics": 10, "Q2_Robotics_Hardware": 3, "Q7_Math_Statistics": 3.5, "Q11_Hands_On_Problem_Solving": 2, "Q12_Research_Discovery": 1.5},
        "score_medicine_surgery":          {"Q4_Medicine_Anatomy": 10, "Q13_People_Care": 4, "Q6_Biotech_Genetics": 3, "Q5_Psychology_Behaviour": 2.5, "Q12_Research_Discovery": 1.5},
        "score_psychology_neuroscience":   {"Q5_Psychology_Behaviour": 10, "Q13_People_Care": 4, "Q4_Medicine_Anatomy": 2.5, "Q12_Research_Discovery": 2, "Q7_Math_Statistics": 1.5},
        "score_biotech_genetics":          {"Q6_Biotech_Genetics": 10, "Q12_Research_Discovery": 3.5, "Q4_Medicine_Anatomy": 3, "Q11_Hands_On_Problem_Solving": 2.5, "Q10_Ecology_Agriculture": 1.5},
        "score_data_science_finance":      {"Q7_Math_Statistics": 10, "Q1_Computer_Coding": 3.5, "Q12_Research_Discovery": 2, "Q14_Creativity_Innovation": 1.5, "Q8_Forensic_Investigation": 1},
        "score_forensic_science":          {"Q8_Forensic_Investigation": 10, "Q12_Research_Discovery": 3.5, "Q6_Biotech_Genetics": 3, "Q11_Hands_On_Problem_Solving": 3, "Q4_Medicine_Anatomy": 1},
        "score_architecture_design":       {"Q9_Architecture_Design": 10, "Q14_Creativity_Innovation": 4, "Q11_Hands_On_Problem_Solving": 2, "Q2_Robotics_Hardware": 1.5, "Q3_Aerospace_Physics": 1.5},
        "score_smart_agriculture_ecology": {"Q10_Ecology_Agriculture": 10, "Q11_Hands_On_Problem_Solving": 3.5, "Q6_Biotech_Genetics": 2.5, "Q12_Research_Discovery": 2, "Q14_Creativity_Innovation": 1.5},
    },
}

# --------------------------------------------------------------- COMMERCE
STREAMS["Commerce"] = {
    "slug": "commerce",
    "icon": "📈",
    "fields": [
        ("Accounting and Auditing", "score_accounting_auditing", "Covers financial records, taxation, audits and reporting. Professional routes such as Chartered Accountancy involve further approved exams and training."),
        ("Investment and Financial Markets", "score_investment_markets", "Focuses on stock markets, portfolio management, investment analysis and how capital is grown and managed."),
        ("Economics and Public Policy", "score_economics_policy", "Studies how economies, markets and governments work, using theory and data to understand inflation, trade, growth and policy."),
        ("Business Management and Entrepreneurship", "score_business_entrepreneurship", "Develops skills to plan, launch and lead a business or manage the operations and strategy of an organisation."),
        ("Marketing and Brand Strategy", "score_marketing_brand", "Combines consumer psychology, advertising, communication and creativity to promote products, brands and ideas."),
        ("Banking and Insurance", "score_banking_insurance", "Covers lending, risk assessment, payment systems, insurance and regulation within the financial services sector."),
        ("Corporate Law and Company Secretaryship", "score_corporate_law", "Deals with company law, contracts, compliance and governance to help organisations follow regulations. Professional routes need further approved study."),
        ("International Trade and Logistics", "score_trade_logistics", "Focuses on import-export, global supply chains, shipping and the movement of goods across borders."),
        ("Human Resources and Organisational Behaviour", "score_hr_organisational", "Focuses on recruitment, training, motivation, workplace culture and managing relationships between people in organisations."),
        ("Business Analytics and E-commerce", "score_analytics_ecommerce", "Uses data and digital platforms to understand customer behaviour, improve online businesses and support business decisions."),
    ],
    "questions": [
        ("Q1_Accounting_Auditing", "I would enjoy maintaining financial records, preparing accounts, checking figures for errors, or working with taxation and audits."),
        ("Q2_Investing_Markets", "I am interested in stock markets, investing, mutual funds, and how money can be grown or managed."),
        ("Q3_Economics_Policy", "I enjoy understanding how economies work, including inflation, government budgets, unemployment, and economic policy."),
        ("Q4_Entrepreneurship_Business", "I would enjoy starting my own business or running a company, from planning the idea to managing the operations."),
        ("Q5_Marketing_Branding", "I enjoy thinking about how products are advertised, what makes customers choose a brand, and how to promote an idea."),
        ("Q6_Banking_Insurance", "I am interested in how banks, loans, insurance and payment systems work and how they keep people's money safe."),
        ("Q7_Corporate_Law", "I am curious about company law, contracts, business regulations, and making sure organisations follow the rules."),
        ("Q8_Global_Trade", "I am interested in international trade, imports and exports, supply chains, and how goods move around the world."),
        ("Q9_People_Management", "I would enjoy recruiting, training, motivating, and resolving conflicts among people in an organisation."),
        ("Q10_Analytics_Ecommerce", "I enjoy using data, spreadsheets, or online platforms to understand customer behaviour and improve online business."),
        ("Q11_Detail_Accuracy", "I am careful and precise, and I like checking details so that nothing in my work is wrong."),
        ("Q12_Communication_Persuasion", "I enjoy presenting ideas, negotiating, and convincing others to agree with my point of view."),
        ("Q13_Leadership_Risk", "I am comfortable taking leadership, making bold decisions, and accepting some risk to achieve bigger goals."),
        ("Q14_Numbers_Comfort", "I am comfortable working with numbers, percentages, calculations, and financial figures for long periods."),
    ],
    "rubric": {
        "score_accounting_auditing":       {"Q1_Accounting_Auditing": 10, "Q11_Detail_Accuracy": 4, "Q14_Numbers_Comfort": 3.5, "Q6_Banking_Insurance": 2, "Q7_Corporate_Law": 1.5},
        "score_investment_markets":        {"Q2_Investing_Markets": 10, "Q14_Numbers_Comfort": 3.5, "Q13_Leadership_Risk": 3.5, "Q3_Economics_Policy": 2.5, "Q10_Analytics_Ecommerce": 1.5},
        "score_economics_policy":          {"Q3_Economics_Policy": 10, "Q14_Numbers_Comfort": 3, "Q8_Global_Trade": 2.5, "Q2_Investing_Markets": 2.5, "Q10_Analytics_Ecommerce": 2},
        "score_business_entrepreneurship": {"Q4_Entrepreneurship_Business": 10, "Q13_Leadership_Risk": 4, "Q12_Communication_Persuasion": 3, "Q5_Marketing_Branding": 2.5, "Q9_People_Management": 1.5},
        "score_marketing_brand":           {"Q5_Marketing_Branding": 10, "Q12_Communication_Persuasion": 4, "Q4_Entrepreneurship_Business": 2.5, "Q10_Analytics_Ecommerce": 2.5, "Q9_People_Management": 1},
        "score_banking_insurance":         {"Q6_Banking_Insurance": 10, "Q11_Detail_Accuracy": 3.5, "Q14_Numbers_Comfort": 3, "Q1_Accounting_Auditing": 2, "Q2_Investing_Markets": 2},
        "score_corporate_law":             {"Q7_Corporate_Law": 10, "Q11_Detail_Accuracy": 3.5, "Q12_Communication_Persuasion": 3, "Q1_Accounting_Auditing": 2, "Q4_Entrepreneurship_Business": 1.5},
        "score_trade_logistics":           {"Q8_Global_Trade": 10, "Q13_Leadership_Risk": 3, "Q11_Detail_Accuracy": 2.5, "Q3_Economics_Policy": 2.5, "Q4_Entrepreneurship_Business": 2},
        "score_hr_organisational":         {"Q9_People_Management": 10, "Q12_Communication_Persuasion": 4, "Q13_Leadership_Risk": 2.5, "Q4_Entrepreneurship_Business": 2, "Q7_Corporate_Law": 1.5},
        "score_analytics_ecommerce":       {"Q10_Analytics_Ecommerce": 10, "Q14_Numbers_Comfort": 3.5, "Q5_Marketing_Branding": 2.5, "Q11_Detail_Accuracy": 1.5, "Q3_Economics_Policy": 1.5},
    },
}

# ------------------------------------------------------------- HUMANITIES
STREAMS["Humanities"] = {
    "slug": "humanities",
    "icon": "📚",
    "fields": [
        ("Law and Legal Studies", "score_law_legal", "Studies laws, rights, courts and legal reasoning to argue cases, advise clients and uphold justice. Practice requires further approved study."),
        ("Political Science and Public Administration", "score_political_science", "Examines governments, policy-making and public administration, and is a common route towards civil services and public policy roles."),
        ("Psychology and Counselling", "score_psychology_counselling", "Explores human behaviour, emotion and mental well-being. Professional counselling or clinical roles require further approved study."),
        ("Sociology and Social Work", "score_sociology_social_work", "Studies societies, communities and social issues, and prepares people to support social change and community development."),
        ("History and Archaeology", "score_history_archaeology", "Investigates the past through records, artefacts and sites to understand how civilisations and cultures developed."),
        ("Journalism and Mass Communication", "score_journalism_media", "Covers reporting, storytelling, media production and communication across print, broadcast and digital platforms."),
        ("Literature and Languages", "score_literature_languages", "Focuses on literature, creative and critical writing, linguistics and language skills, with routes into writing, editing and translation."),
        ("Education and Teaching", "score_education_teaching", "Prepares people to teach, mentor and design learning experiences. Teaching roles usually require approved teacher-training qualifications."),
        ("Fine Arts, Film and Performing Arts", "score_arts_performance", "Develops creative expression through visual art, design, music, theatre and film, building both technique and a personal style."),
        ("International Relations and Diplomacy", "score_international_relations", "Studies global politics, foreign cultures, diplomacy and international organisations, linking to careers in global affairs."),
    ],
    "questions": [
        ("Q1_Law_Legal_Debate", "I enjoy debating, building logical arguments, and am curious about laws, rights, courts, and how justice works."),
        ("Q2_Politics_Governance", "I am interested in how governments work, how policies are made, and how public administration serves citizens."),
        ("Q3_Psychology_Counselling", "I enjoy understanding why people think and behave the way they do, and would like to help others with personal struggles."),
        ("Q4_Society_Community", "I care about social issues such as inequality, and would enjoy working to improve the lives of communities."),
        ("Q5_History_Culture", "I am fascinated by the past, ancient civilisations, historical sites, and how cultures and traditions developed."),
        ("Q6_Journalism_Media", "I would enjoy reporting news, interviewing people, producing media content, or investigating stories for the public."),
        ("Q7_Literature_Languages", "I enjoy reading literature, writing stories or essays, and learning about languages and how they work."),
        ("Q8_Teaching_Mentoring", "I would enjoy teaching, explaining ideas to others, and helping students learn and grow."),
        ("Q9_Arts_Performance", "I would enjoy painting, design, music, theatre, or filmmaking as a way to express ideas and emotions."),
        ("Q10_Global_Affairs", "I am curious about other countries, international relations, diplomacy, and global events."),
        ("Q11_Communication_Persuasion", "I am confident speaking or writing in front of others and explaining my views clearly and convincingly."),
        ("Q12_Empathy_People_Care", "I easily understand other people's feelings and like to support those who are struggling."),
        ("Q13_Research_Critical_Thinking", "I enjoy researching a topic in depth, questioning sources, and forming my own reasoned opinions."),
        ("Q14_Creativity_Imagination", "I like using imagination and original ideas to create stories, designs, or new ways of looking at things."),
    ],
    "rubric": {
        "score_law_legal":              {"Q1_Law_Legal_Debate": 10, "Q11_Communication_Persuasion": 4, "Q13_Research_Critical_Thinking": 3.5, "Q2_Politics_Governance": 2.5, "Q4_Society_Community": 1.5},
        "score_political_science":      {"Q2_Politics_Governance": 10, "Q10_Global_Affairs": 3, "Q13_Research_Critical_Thinking": 3, "Q11_Communication_Persuasion": 3, "Q4_Society_Community": 2},
        "score_psychology_counselling": {"Q3_Psychology_Counselling": 10, "Q12_Empathy_People_Care": 4, "Q13_Research_Critical_Thinking": 3, "Q4_Society_Community": 2.5, "Q8_Teaching_Mentoring": 1.5},
        "score_sociology_social_work":  {"Q4_Society_Community": 10, "Q12_Empathy_People_Care": 3.5, "Q13_Research_Critical_Thinking": 3, "Q3_Psychology_Counselling": 2, "Q5_History_Culture": 2},
        "score_history_archaeology":    {"Q5_History_Culture": 10, "Q13_Research_Critical_Thinking": 4, "Q7_Literature_Languages": 2.5, "Q10_Global_Affairs": 2, "Q4_Society_Community": 1.5},
        "score_journalism_media":       {"Q6_Journalism_Media": 10, "Q11_Communication_Persuasion": 3.5, "Q13_Research_Critical_Thinking": 3, "Q7_Literature_Languages": 2.5, "Q2_Politics_Governance": 2},
        "score_literature_languages":   {"Q7_Literature_Languages": 10, "Q14_Creativity_Imagination": 4, "Q5_History_Culture": 2.5, "Q11_Communication_Persuasion": 2, "Q6_Journalism_Media": 1.5},
        "score_education_teaching":     {"Q8_Teaching_Mentoring": 10, "Q12_Empathy_People_Care": 4, "Q11_Communication_Persuasion": 3, "Q3_Psychology_Counselling": 2, "Q7_Literature_Languages": 1.5},
        "score_arts_performance":       {"Q9_Arts_Performance": 10, "Q14_Creativity_Imagination": 4.5, "Q7_Literature_Languages": 2, "Q12_Empathy_People_Care": 1.5, "Q6_Journalism_Media": 1.5},
        "score_international_relations": {"Q10_Global_Affairs": 10, "Q2_Politics_Governance": 3.5, "Q11_Communication_Persuasion": 3, "Q5_History_Culture": 2.5, "Q13_Research_Critical_Thinking": 1.5},
    },
}

def question_columns(stream):  return [c for c, _ in STREAMS[stream]["questions"]]
def target_columns(stream):    return [c for _, c, _ in STREAMS[stream]["fields"]]
def field_names(stream):       return [n for n, _, _ in STREAMS[stream]["fields"]]
def primary_question(stream, target):
    w = STREAMS[stream]["rubric"][target]
    return max(w, key=w.get)
