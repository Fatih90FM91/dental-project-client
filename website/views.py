from django.shortcuts import render
from django.core.mail import send_mail
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

from .models import Register
from .forms import RegisterForm
from django.views.generic import CreateView 
from django.urls import reverse_lazy ,reverse


class RegisterView(CreateView):
    model = Register
    form_class = RegisterForm
    template_name='register.html'
    success_url = reverse_lazy('home')
    



def home(request):
    trans = translate(language= 'tr')
    trans_nav_info = translate(language= 'tr')
    trans_nav_info_2 = translate(language= 'tr')
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    host_email = "frank9091.johansen@gmail.com"  # Enter your address
    password = "fbcvmtolxvptahcy" #//fbcvmtolxvptahcy
    if request.method == 'POST':
        examination_selection = request.POST['examination-selection']
        name = request.POST['name']
        email = request.POST['email']
        # date = request.POST['date']
        # time = request.POST['time']
        phone = request.POST['phone']
     
        data = {
            'examination_selection' : examination_selection,
            'name' : name,
            'email' :email,
            # 'date' : date,
            # 'time' : time,
            'phone' : phone
        }
        
       
        message = MIMEMultipart("alternative")
        message["Subject"] = "Make an Apponintment"
        message["From"] = email
        message["To"] =host_email

        # Create the plain-text and HTML version of your message

        # for article in formatted_articles: + f"<p>Date : {date} </p> \n" + f"<p>Time : {time} </p> \n"
        article = f"<h3>Patient Name : {name} </h3> \n" + f"<p>Patient Email : {email} </p> \n" + f"<p>Phone : {phone} </p> \n" + f"<p>examination_selection : {examination_selection} </p> \n"
            
        text = """\

                   Blue Tulip!!

                  """

        html = """\
                      <html>
                        <body>
                         <h1>
                         Appointment was Requested!!
                          </h1>

                        </body>
                      </html>
                      """ + f'{article}'

            # Turn these into plain/html MIMEText objects

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(host_email, password)
            server.sendmail(email, host_email, message.as_string())
       

        return render(request, 'appointment.html', {'message_appointment' : data})
    else:
        return render(request, "home.html")
    #, {'trans' : trans, 'nav_info' : trans_nav_info, 'nav_info_2' : trans_nav_info_2}



   

def service(request):
    return render(request, "services.html", {})

def about(request):
    return render(request, "about.html", {})

def doctor(request):
    return render(request, "doctors.html", {})

def contact(request):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    host_email = "frank9091.johansen@gmail.com"  # Enter your address
    password = "fbcvmtolxvptahcy" #//fbcvmtolxvptahcy
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_contact = request.POST['message']

      
        
        # send_mail(
        #     name,
        #     email,
        #     subject,
        #     message,
        #     ['jonsnow9091.fs@gmail.com']
        # )

        message = MIMEMultipart("alternative")
        message["Subject"] = "Make an Apponintment"
        message["From"] = email
        message["To"] =host_email

        # Create the plain-text and HTML version of your message

        # for article in formatted_articles:
        article = f"<h3>Patient Name : {name} </h3> \n" + f"<p>Patient Email : {email} </p> \n" + f"<p>Patient Subject : {subject} </p> \n" + f"<p>Patient Message : {message_contact} </p> \n"
            
        text = """\

                   Blue Tulip!!

                  """

        html = """\
                      <html>
                        <body>
                         <h1>
                         Appointment was Requested!!
                          </h1>

                        </body>
                      </html>
                      """ + f'{article}'

            # Turn these into plain/html MIMEText objects

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(host_email, password)
            server.sendmail(email, host_email, message.as_string())
       

        return render(request, 'contact.html', {'message_contact' : message_contact, 'name' : name})
    else:
        return render(request, "contact.html", {})

def blog(request):
    return render(request, "blog.html", {})


def appointment(request):
    return render(request, "appointment.html", {})


def blogComment(request):
    return render(request, "blog-single.html", {})







def map(request):
    return render(request, "google_map.html", {})



def translate(language):
    current_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
        text_navbar = gettext('Services')
        text_navbar_2 = gettext('Doctors')
        text_navbar_3 = gettext('About')
        text_navbar_4 = gettext('Contact')
        text_navbar_5 = gettext('Make an Appointment')
        text_nav_info = gettext('Modern Dentistry in a Calm and Relaxed Environment')
        text_nav_info_2 = gettext('Modern Achieve Your Desired Perfect Smile')
        text_nav_info_3 = gettext('Transform Your Smile with Modern Dentistry: Achieve Your Desired Perfect Smile through Innovative Techniques and Expert Care')

        text_emergency_head = gettext('Emergency Cases')  
        text_emergency_expl = gettext('Please do not hesitate to contact me for any additional information or assistance required.')

        text_opening_hours = gettext('Opening Hours')
        text_opening_monday_friday = gettext('Monday - Friday')
        text_opening_saturday = gettext('Saturday')
        text_opening_sunday = gettext('Sunday')

        
        text_opening_depart = gettext('Department')
        text_opening_depart_alt_1 = gettext('Teeth Whitening')
        text_opening_depart_alt_2 = gettext('Teeth Cleaning')
        text_opening_depart_alt_3 = gettext('Quality Brackets')
        text_opening_depart_alt_4 = gettext('Modern Anesthetic')
        text_opening_depart_alt_5 = gettext('Dental Checkup')
        text_opening_depart_alt_6 = gettext('Fillings')
        text_opening_depart_alt_7 = gettext('Dental Bridges')
        text_opening_depart_alt_8 = gettext('Modern Anesthetic')
        text_opening_depart_alt_9 = gettext('Dental Implants')
        text_opening_depart_alt_10 = gettext('Root Canal Treatment')
        text_opening_depart_alt_11 = gettext('Extractions')
        text_opening_depart_alt_12 = gettext('Pediatric Dentistry')
        text_opening_depart_alt_13 = gettext('Orthodontic Treatment')
        text_opening_depart_alt_14 = gettext('Dental Crowns')
       


      
        text_opening_name = gettext('Name')
        text_opening_date = gettext('Date')
        text_opening_time = gettext('Time')
        text_opening_phone = gettext('Phone')

        text_our_service = gettext('Our Service Keeps you Smile')
        alt_head =  'At Blue Tulip, we take pride in providing top-notch services that are not just about oral health but also about keeping your smile radiant and confident.' \
        'Our commitment to your well-being goes beyond the dental chair.We understand that a healthy smile is not just about regular check-ups and treatments; it s about the overall experience and care you receive.' \
        'That s why we have designed our services to ensure your comfort, convenience, and satisfaction every step of the way.From the moment you walk through our doors, our friendly and skilled team is dedicated to making your visit a pleasant one.' \
        'We offer a wide range of dental treatments and procedures, all delivered with the utmost professionalism and using the latest technology.But its not just about the treatments; it s about personalized care.' \
        'We take the time to listen to your concerns and answer your questions, ensuring that you are well-informed and comfortable with every aspect of your dental care journey.We believe that a healthy smile is a confident smile, and we are here to help you achieve and maintain that confidence. Our goal is simple: to keep you smiling, because your smile is our ultimate success.'  
        text_our_service_alt_1 = gettext("We believe that a healthy smile is a confident smile; We're here to help you earn and keep that trust. Our vision: without compromising scientific, ethical, conscientious and humanitarian principles; modern treatments; To present it to you with our honest, reliable and experienced team.")
        text_our_service_alt_2 = gettext("At Blue Tulip, we pride ourselves on providing world-class services that will not only restore your oral health, but will also get you back to your radiant smile.")
        text_our_service_alt_3 = gettext("With our friendly and experienced team, we restore your oral health in the comfort of your home. It protects your dental health with regular check-ups and treatments; We offer you a bright smile.")
				 
        text_dental_services_teeth_cleaning = gettext('A routine dental cleaning involves the removal of plaque and tartar buildup from your teeth. It helps prevent gum disease and keeps your smile fresh and healthy.')
        text_dental_services_teeth_whitening = gettext("Teeth whitening is a cosmetic procedure to brighten discolored or stained teeth, enhancing your smile's aesthetics.")
        text_dental_services_teeth_fillings = gettext("Dental fillings are used to repair cavities and restore damaged teeth. They can be made from materials like composite resin, amalgam, or porcelain.")
        text_dental_services_teeth_extractions = gettext("Dental extractions involve the removal of damaged or non-restorable teeth, often due to severe decay, infection, or crowding.")
        text_dental_services_teeth_orthodontic_treatment = gettext("Orthodontic procedures, including braces and aligners, are used to correct misaligned teeth and bite issues for improved oral health and aesthetics.")
        text_dental_services_teeth_root_canal_treatment = gettext("Root canal therapy involves removing infected or damaged pulp from a tooth, preserving the tooth and relieving pain caused by infection.")
        text_dental_services_teeth_dental_implants = gettext("Dental implants are titanium posts surgically placed in the jawbone to support artificial teeth. They provide a durable, long-term solution for missing teeth.")
        text_dental_services_teeth_pediatric_dentistry = gettext("Pediatric dentists specialize in children's dental care, offering services tailored to young patients' unique needs.")
        text_dental_services_teeth_dental_checkup = gettext("Regular dental checkups are essential for maintaining oral health. Dentists examine your teeth, gums, and mouth for signs of issues, allowing for early intervention.")
        text_dental_services_teeth_dental_Bridges = gettext("Bridges are used to replace missing teeth by anchoring artificial teeth to adjacent natural teeth, improving both function and appearance.")
        text_dental_services_teeth_dental_crowns = gettext("Crowns are tooth-shaped caps that are placed over damaged or weakened teeth to restore their strength, shape, and appearance.")
        text_dental_services_teeth_quality_brackets = gettext("Quality brackets in the context of dentistry typically refer to orthodontic brackets used in braces. These brackets play a crucial role in orthodontic treatment as they are attached to the patient's teeth and serve as the anchor points for the archwires that guide the movement of teeth into their proper positions.")
      
        
        
        text_dental_dentcare_section = gettext("Blue Tulip with a personal touch")
        text_dental_dentcare_section_sub_head = gettext("Join us in creating a world where every smile shines with confidence. Your smile's best friend is just a call away welcome to Blue Tulip.")
        text_dental_dentcare_section_sub_head_1 = gettext("Well Experience Dentist")
        text_dental_dentcare_section_sub_head_1_sub = gettext("when you choose a well-experienced dentist, you're not just choosing a healthcare provider; you're choosing a partner in your oral health journey. You're choosing confidence, empathy, and a commitment to excellence.")
        text_dental_dentcare_section_sub_head_2 = gettext("High Technology Facilities")
        text_dental_dentcare_section_sub_head_2_sub = gettext("high-technology facilities have truly transformed the landscape of dentistry. They offer a glimpse into the future of oral healthcare, one that is characterized by precision, convenience, and patient-centric care. As we continue to embrace these advancements, we can look forward to even greater innovations that will further elevate the field of dentistry and keep our smiles healthy and radiant.")
        text_dental_dentcare_section_sub_head_3 = gettext("Comfortable Clinics")
        text_dental_dentcare_section_sub_head_3_sub = gettext("comfortable dental clinics are more than just places of treatment; they are sanctuaries of care and compassion. They reflect a commitment to patient well-being and a dedication to making dental visits not only painless but genuinely comfortable. As these clinics continue to redefine the dental experience, we can look forward to a future where oral healthcare is embraced with confidence and peace of mind.")
      
        
        text_dental_dentcare_section_meet_dentists = gettext("Meet Our Experience Dentist")
        text_dental_dentcare_section_meet_dentists_sub_head = gettext("Meet our experienced dentist, a dedicated professional committed to providing top-notch and ensuring your oral health is in the best hands.")
        text_dental_dentcare_section_meet_dentist_1 = gettext("Dentist")
        text_dental_dentcare_section_meet_dentist_1_sub_head = gettext("A dentist is a healthcare professional dedicated to preserving and enhancing oral health, ensuring patients' smiles radiate confidence and well-being.")
        text_dental_dentcare_section_meet_assistant = gettext("Assistant")
        text_dental_dentcare_section_meet_dentist_2_sub_head = gettext("A dentist assistant is a crucial part of the dental team, offering support and ensuring the smooth operation of the practice, while also assisting in patient care.")
        text_dental_dentcare_section_meet_reception_employer = gettext("Reception Employee")
        text_dental_dentcare_section_meet_dentist_3_sub_head = gettext("A reception employee serves as the welcoming face of an organization, adeptly managing inquiries, appointments, and the flow of visitors to create a positive and efficient experience.")
        text_dental_dentcare_section_meet_IT_expert = gettext("IT Expert")
        text_dental_dentcare_section_meet_dentist_4_sub_head = gettext("An IT expert possesses the technical prowess to troubleshoot, optimize, and innovate in the digital realm, ensuring that technology empowers and enables seamless operations across various domains.")
        text_dental_dentcare_section_meet_last_speech = gettext("Today, I have the distinct pleasure of introducing you to the heart of our dental practice - our experienced dentist. Our dentist isn't just a professional; they are a dedicated healthcare provider with a wealth of expertise and a genuine commitment to your oral health and overall well-being.")
           
                  
        text_dental_dentcare_section_Achievements = gettext("Achievements")
        text_dental_dentcare_section_Achievements_sub_title = gettext("Achievements are the tangible results of dedication, effort, and perseverance, showcasing our potential and progress.")
        text_dental_dentcare_section_years_of_experience = gettext("Years of Experience")
        text_dental_dentcare_section_qualified_dentist = gettext("Qualified Dentist")
        text_dental_dentcare_section_smiling_customer = gettext("Happy Smiling Customer")
        text_dental_dentcare_section_patients_per_year = gettext("Patients Per Year")

        text_dental_dentcare_section_patients_Subcribe = gettext("Subcribe to our Newsletter")
        text_dental_dentcare_section_patients_Subcribe_sub_title = gettext("Subscribe to our newsletter to stay informed and receive regular updates, exclusive content, and valuable insights delivered directly to your inbox.")
        text_dental_dentcare_section_patients_Subcribe_email = gettext("Enter email address")
        text_dental_dentcare_section_patients_Subcribe_btn = gettext("Subscribe")

        text_dental_dentcare_section_Testimony = gettext("Testimony")
        text_dental_dentcare_section_patients_Customer_Says = gettext("Our Happy Customer Says")
        text_dental_dentcare_section_patients_1 = gettext("Taking my kids to the dentist used to be a struggle until we discovered Blue Tulip Dental Clinic. The staff is fantastic with children, and they create a welcoming atmosphere that makes dental visits enjoyable for my kids.")
        text_dental_dentcare_section_patients_position_1 = gettext("Marketing Manager")
        text_dental_dentcare_section_patients_2 = gettext("As an adult considering braces, I was hesitant, but the team at Blue Tulip Dental Clinic put me at ease. They explained the entire orthodontic process, and now, my smile is straighter than ever. I couldn't be happier!")
        text_dental_dentcare_section_patients_position_2 = gettext("Interface Designer")
        text_dental_dentcare_section_patients_3 = gettext("I had a dental emergency over the weekend, and I was in excruciating pain. I called Blue Tulip Dental Clinic, and they were able to see me right away. The dentist provided prompt and expert care, and I'm so grateful for their responsiveness.")
        text_dental_dentcare_section_patients_position_3 = gettext("UI Designer")
        text_dental_dentcare_section_patients_4 = gettext("Taking my kids to the dentist used to be a struggle until we discovered Blue Tulip Dental Clinic. The staff is fantastic with children, and they create a welcoming atmosphere that makes dental visits enjoyable for my kids.")
        text_dental_dentcare_section_patients_position_4 = gettext("Web Developer")
        text_dental_dentcare_section_patients_5 = gettext("I had my teeth whitened at Blue Tulip Dental Clinic, and the results are incredible. My smile is noticeably brighter, and the procedure was quick and comfortable. I can't stop smiling!")
        text_dental_dentcare_section_patients_position_5 = gettext("System Analytics")

        text_dental_dentcare_section_Blogs = gettext("I encourage you to explore the world of dental blogs. Dive into the articles, absorb the knowledge, and empower yourself with the information needed to maintain a healthy, radiant smile. Your oral health journey begins with the click of a button, and the possibilities are endless.")
        text_dental_dentcare_section_Blogs_message_1 = gettext("Explore the connection between your diet and your dental health. Discover which foods are smile-friendly and which ones to consume in moderation.")
        text_dental_dentcare_section_Blogs_message_2 = gettext("Parents, learn how to establish good oral hygiene habits early, find the right toothbrush for your child, and make dental visits a positive experience.")
        text_dental_dentcare_section_Blogs_message_3 = gettext("Explore practical and effective tips for maintaining a dazzling smile, from proper brushing and flossing techniques to the benefits of mouthwash.")
        text_dental_dentcare_section_Blogs_message_4 = gettext("Discover why routine dental checkups are your best defense against oral health issues and how they can save you time, money, and discomfort in the long run.")

        text_dental_dentcare_section_quality_services_1 = gettext("Blue Tulip Procedure")
        text_dental_dentcare_section_quality_services_2 = gettext("High Quality Services")
        text_dental_dentcare_section_quality_services_3 = gettext("I'm delighted to introduce you to the Blue Tulip Procedure and the exceptional high-quality services it represents. Blue Tulip is not just a dental treatment; it's a testament to our unwavering commitment to your oral health and well-being.")
        text_dental_dentcare_section_quality_services_4 = gettext("innovation")
        text_dental_dentcare_section_quality_services_5 = gettext("dedication")
        text_dental_dentcare_section_quality_services_6 = gettext("cutting-edge technology")

        text_free_quote = gettext('Get a Free Quote')
        text_get_quote = gettext('Get Quote')

        text_footer_left_section_1 = gettext('Explore the exciting world of teledentistry and how virtual consultations and remote monitoring are changing the way we access dental care')
        text_footer_right_section_1 = gettext('Recent Blog')
        text_footer_right_section_2 = gettext('helping others make informed choices about their oral healthcare providers.')
        text_footer_right_section_3 = gettext('I found the dental blog incredibly informative and engaging')

        text_about_us = gettext('About Us')
        text_about_head_1 = gettext('What we do')
        text_about_head_2 = gettext('Our mission')
        text_about_head_3 = gettext('Our goal')

        text_about_1 = gettext('We Offer High Quality Services')
        text_about__offer_1 = gettext("Today, I am thrilled to share with you the essence of what we stand for in the world of dentistry: 'We Offer High-Quality Services.' These words are not just a statement but a promise that we uphold with unwavering commitment and dedication.")
        text_about__offer_2 = gettext('When you step into our dental practice, you are stepping into an environment where excellence is the standard. From the moment you walk through our doors, you will experience the difference that high-quality dental services can make.')
        text_about__offer_3 = gettext('Our team of skilled and compassionate professionals is dedicated to providing you with the finest care. Whether you seek routine check-ups, cosmetic enhancements, or restorative treatments, rest assured that your smile is in the hands of experts who prioritize your well-being.')
        text_about__offer_4 = gettext("In conclusion, when we say, 'We Offer High-Quality Services,' we mean that your smile, your comfort, and your satisfaction are our top priorities. We are dedicated to providing you with dental care that not only meets but exceeds your expectations. We invite you to experience the difference for yourself and join us on a journey towards a healthier, more radiant smile.")
        text_about__offer_5 = gettext('Thank you for considering us as your partners in oral health, and we look forward to serving you with the utmost care and expertise.')
        text_about_accomoate_1 = gettext('To Accomodate All Patients')
        text_about_accomoate_2 = gettext('We believe that quality dental care should be accessible to everyone, regardless of their unique needs, backgrounds, or circumstances. Our commitment to accommodating all patients is at the heart of everything we do.')
        text_about_accomoate_3 = gettext("When you choose our dental practice, you're not just choosing a healthcare provider; you're choosing an inclusive and compassionate environment where your individuality is respected and valued.")
        text_about_accomoate_4 = gettext('But our commitment to accommodating all patients extends beyond the services we offer. We take pride in creating a welcoming and comfortable atmosphere where everyone feels at home. Our team is trained to provide care with sensitivity and empathy, ensuring that your experience is as stress-free as possible.')
        text_about_accomoate_5 = gettext("Our dedication to accommodating all patients is not just about the here and now; it's about fostering long-term relationships built on trust and mutual respect. We want to be your partners in oral health, supporting you on your journey to a healthier and more radiant smile.")
        text_about_accomoate_6 = gettext('Thank you for considering us as your dental care provider, and we look forward to welcoming you into our inclusive and caring dental family.')
        text_about_help_customers_1 = gettext('Help Our Customers Needs')
        text_about_help_customers_2 = gettext("Today, I want to shed light on a fundamental aspect of our dental practice: our unwavering commitment to 'Help Our Customers Needs.' At the heart of everything we do is a deep understanding that our patients are unique individuals with specific dental needs, and it is our privilege and responsibility to assist them in achieving optimal oral health.")
        text_about_help_customers_3 = gettext('Our team of experienced professionals is committed to providing you with the highest standard of care. We take the time to listen to your concerns, answer your questions, and involve you in decisions regarding your dental health. Your active participation in your treatment is essential to us.')
        text_about_help_customers_4 = gettext("Moreover, our commitment to 'Help Our Customers Needs' extends beyond the chair. We are here to provide guidance and education, empowering you with the knowledge and tools to make informed decisions about your oral health. We believe that a well-informed patient is an empowered patient.")
        text_about_help_customers_5 = gettext("In conclusion, when we say, 'Help Our Customers Needs,' we mean that your needs are at the forefront of our practice. Your smile is our mission, and we are dedicated to assisting you in achieving and maintaining optimal oral health. We are not just your dental care providers; we are your partners in a journey toward a healthier, happier smile")
        
       
        text_contact_us = gettext('Contact Us')
        text_contact_info = gettext('Contact Information')
        text_contact_address = gettext('Address')
        text_contact_name = gettext('Your Name')
        text_contact_email = gettext('Your Email')
        text_contact_subject = gettext('Subject')
        text_contact_message = gettext('Message')
        text_contact_send_message = gettext('Send Message')

        text_blog = gettext('Read Our Blog')
        text_blog_page_1 = gettext('Unlocking the Secrets to a Beautiful Smile: Cosmetic Dentistry Explained')
        text_blog_page_sub_1 = gettext("Today, let's embark on a journey together, a journey to unlock the secrets to a beautiful smile through the captivating world of cosmetic dentistry. In a world where confidence and self-assurance often begin with a smile, understanding the art and science behind a stunning smile is not just enlightening; it's empowering")
        text_blog_page_2 = gettext('The Power of Prevention: How Daily Habits Impact Your Dental Health')
        text_blog_page_sub_2 = gettext("Preventing dental issues starts with the basics: our daily oral hygiene habits. Something as simple as brushing and flossing can be the frontline defense against tooth decay and gum disease. These daily rituals are more than just tasks; they're acts of self-care that set the foundation for a lifetime of strong, healthy teeth and gums.")
        text_blog_page_3 = gettext('Behind the Scenes: What Really Happens During a Dental Checkup')
        text_blog_page_sub_3 = gettext("A dental checkup is not just a brief appointment; it's a comprehensive assessment of your oral health, a thorough examination that goes beyond what meets the eye. When you step into the dental chair, you're not just sitting down for a quick peek at your teeth; you're taking a proactive step towards maintaining your oral well-being")
        text_blog_page_4 = gettext('Oral Health at Every Age: A Guide to Pediatric to Geriatric Dentistry')
        text_blog_page_sub_4 = gettext("Let's begin with the youngest members of our community: our children. Pediatric dentistry is not just about baby teeth; it's about setting the foundation for a lifetime of healthy smiles. Early dental visits, education about proper oral hygiene, and preventive measures like sealants are crucial in ensuring that our children grow up with strong, cavity-free teeth")
        text_blog_page_5 = gettext('The Connection Between Oral and Overall Health: What You Need to Know')
        text_blog_page_sub_5 = gettext('The connection between oral health and overall health is a powerful one, often underestimated and overlooked. Yet, research and medical studies continually reveal the intricate relationship between the two. Our mouths are not isolated entities but rather gateways to our bodies, and what happens in our mouths can profoundly impact our overall health')
        text_blog_page_6 = gettext('From Braces to Invisalign: A Comprehensive Guide to Orthodontic Options')
        text_blog_page_sub_6 = gettext('Orthodontics is a field that has evolved significantly over the years, offering a wide spectrum of treatments to address various dental misalignments. Gone are the days when metal braces were the only option. Today, the choice is not just about straightening teeth but also about doing so comfortably, discreetly, and efficiently')
        text_blog_sec_read = gettext('Read more')
        text_blog_sec_parag = gettext('Paragraph')
        text_blog_sec_parag_sub = gettext("A dental care blog is more than just a collection of articles; it's a trusted resource that empowers individuals to take charge of their oral health. It serves as a beacon of knowledge, shedding light on the importance of dental hygiene, the latest advancements in dentistry, and practical tips for maintaining a radiant smile")


       
        text_blog_single_page_2 = gettext("Cosmetic dentistry is more than just a branch of dentistry; it's a form of artistry that has the power to transform lives. It's the magic wand that can turn dental imperfections into a symphony of radiance, boosting not just our appearance but also our self-esteem.")
        text_blog_single_page_3 = gettext("When we delve into the realm of cosmetic dentistry, we encounter a fascinating world where science meets aesthetics. It's a world where the skills of dental professionals are akin to those of artists, sculpting and crafting smiles that radiate beauty and confidence.")
        text_blog_single_page_4 = gettext("But what exactly is cosmetic dentistry? It's a field that encompasses a wide array of treatments and procedures designed to enhance the aesthetics of our teeth and smile. From teeth whitening and veneers to dental implants and orthodontics, the possibilities are endless.")
        text_blog_single_page_5 = gettext("One of the most enchanting aspects of cosmetic dentistry is its ability to cater to the unique needs and desires of each patient. Your dream smile is not a one-size-fits-all concept; it's a personalized masterpiece that takes into account your facial structure, skin tone, and individual preferences.")
        text_blog_single_page_6 = gettext("Cosmetic dentistry is not merely about aesthetics; it's about function and health as well. Procedures like dental implants not only restore missing teeth but also improve oral health and overall well-being. A beautiful smile should not just look good; it should feel good and function perfectly.")
        text_blog_single_page_7 = gettext("Furthermore, the impact of cosmetic dentistry goes beyond the surface. A transformed smile has the power to boost confidence, enhance social interactions, and even positively affect professional opportunities. It's a testament to the profound connection between our oral and emotional well-being.")
        text_blog_single_page_8 = gettext("In conclusion, unlocking the secrets to a beautiful smile through cosmetic dentistry is not just about enhancing appearances; it's about embracing a new level of self-confidence and well-being. It's about understanding that a radiant smile is within reach, and it's achievable through the expertise and artistry of cosmetic dentistry.")
        text_blog_single_page_9 = gettext("So, I invite each of you to explore this captivating world, to consider the possibilities, and to envision the smile of your dreams. It's not just a journey to a beautiful smile; it's a journey to a more confident, radiant, and empowered you.")
        text_blog_single_page_10 = gettext("Thank you for joining me on this journey of discovery, and I hope that cosmetic dentistry continues to inspire and empower you to unlock the secrets to a beautiful smile.")


        text_register_1 = gettext('Register at Blue Tulip')
        text_register_2  = gettext('You are welcome to register with us. Please fill out the information below and we will contact you within two working days.Do you want to register more than one person such as your partner or children? After submitting the completed registration form, this page will automatically refresh to allow you to complete another registration form if necessary.Would you please bring your health care card on your first visit? Thanks in advance!')
        text_register_3 = gettext('First Name')
        text_register_4  = gettext('Last Name')
        text_register_5 = gettext('Gender')
        text_register_6  = gettext('House Number')
        text_register_7 = gettext('City')
        text_register_8  = gettext('State')
        text_register_9 = gettext('Zipcode')
        text_register_10  = gettext('Street')
        text_register_11  = gettext('How Do you hear about Us?')
        text_register_12  = gettext('Question')
        text_register_13  = gettext('Are you member?')
        text_register_14  = gettext('Register')
        text_register_15  = gettext('Date of birth')

    finally:
        activate(current_language)

    return text , text_nav_info, text_nav_info_2, text_nav_info_3, text_navbar, text_navbar_2, text_navbar_3, text_navbar_4, text_navbar_5, text_emergency_head , text_emergency_expl, text_opening_hours,  text_opening_monday_friday, text_opening_saturday, text_opening_sunday, text_opening_depart, text_opening_depart_alt_1, text_opening_depart_alt_2, text_opening_depart_alt_3, text_opening_depart_alt_4, text_opening_name, text_opening_date, text_opening_time, text_opening_phone, text_our_service, text_our_service_alt_1, text_our_service_alt_2, text_our_service_alt_3, text_dental_services_teeth_cleaning, text_dental_services_teeth_whitening, text_dental_services_teeth_fillings, text_dental_services_teeth_extractions, text_dental_services_teeth_orthodontic_treatment, text_dental_services_teeth_root_canal_treatment, text_dental_services_teeth_dental_implants, text_dental_services_teeth_pediatric_dentistry, text_dental_services_teeth_dental_checkup, text_dental_services_teeth_dental_Bridges, text_opening_depart_alt_5, text_opening_depart_alt_6, text_opening_depart_alt_7, text_opening_depart_alt_8, text_opening_depart_alt_9, text_opening_depart_alt_10, text_opening_depart_alt_11, text_opening_depart_alt_12, text_opening_depart_alt_13, text_opening_depart_alt_14, text_dental_services_teeth_dental_crowns, text_dental_services_teeth_quality_brackets, text_dental_dentcare_section, text_dental_dentcare_section_sub_head, text_dental_dentcare_section_sub_head_1, text_dental_dentcare_section_sub_head_1_sub, text_dental_dentcare_section_sub_head_2, text_dental_dentcare_section_sub_head_2_sub, text_dental_dentcare_section_sub_head_3, text_dental_dentcare_section_sub_head_3_sub,  text_dental_dentcare_section_meet_dentists, text_dental_dentcare_section_meet_dentists_sub_head, text_dental_dentcare_section_meet_dentist_1, text_dental_dentcare_section_meet_dentist_1_sub_head, text_dental_dentcare_section_meet_assistant, text_dental_dentcare_section_meet_dentist_2_sub_head, text_dental_dentcare_section_meet_reception_employer, text_dental_dentcare_section_meet_dentist_3_sub_head, text_dental_dentcare_section_meet_IT_expert, text_dental_dentcare_section_meet_dentist_4_sub_head, text_dental_dentcare_section_meet_last_speech, text_dental_dentcare_section_Achievements, text_dental_dentcare_section_Achievements_sub_title, text_dental_dentcare_section_years_of_experience, text_dental_dentcare_section_qualified_dentist, text_dental_dentcare_section_smiling_customer, text_dental_dentcare_section_patients_per_year, text_dental_dentcare_section_patients_Subcribe, text_dental_dentcare_section_patients_Subcribe_sub_title, text_dental_dentcare_section_patients_Subcribe_email, text_dental_dentcare_section_patients_Subcribe_btn, text_dental_dentcare_section_Testimony, text_dental_dentcare_section_patients_Customer_Says, text_dental_dentcare_section_patients_1, text_dental_dentcare_section_patients_position_1, text_dental_dentcare_section_patients_2, text_dental_dentcare_section_patients_position_2, text_dental_dentcare_section_patients_3, text_dental_dentcare_section_patients_position_3, text_dental_dentcare_section_patients_4, text_dental_dentcare_section_patients_position_4, text_dental_dentcare_section_patients_5, text_dental_dentcare_section_patients_position_5, text_dental_dentcare_section_Blogs, text_dental_dentcare_section_Blogs_message_1, text_dental_dentcare_section_Blogs_message_2, text_dental_dentcare_section_Blogs_message_3, text_dental_dentcare_section_Blogs_message_4, text_dental_dentcare_section_quality_services_1, text_dental_dentcare_section_quality_services_2, text_dental_dentcare_section_quality_services_3, text_dental_dentcare_section_quality_services_4, text_dental_dentcare_section_quality_services_5, text_dental_dentcare_section_quality_services_6, text_free_quote, text_get_quote, text_footer_left_section_1, text_footer_right_section_1, text_footer_right_section_2, text_footer_right_section_3, text_about_us, text_about_head_1, text_about_head_2, text_about_head_3, text_about_1, text_about__offer_1, text_about__offer_2, text_about__offer_3, text_about__offer_4, text_about__offer_5, text_about_accomoate_1, text_about_accomoate_2, text_about_accomoate_3, text_about_accomoate_4, text_about_accomoate_5, text_about_accomoate_6, text_about_help_customers_1, text_about_help_customers_2, text_about_help_customers_3, text_about_help_customers_4, text_about_help_customers_5, text_contact_us, text_contact_info, text_contact_address, text_contact_name, text_contact_email, text_contact_subject, text_contact_message, text_contact_send_message, text_blog, text_blog_page_1, text_blog_page_2, text_blog_page_3, text_blog_page_4, text_blog_page_5, text_blog_page_6 , text_blog_page_sub_1, text_blog_page_sub_2, text_blog_page_sub_3, text_blog_page_sub_4, text_blog_page_sub_5, text_blog_page_sub_6, text_blog_sec_read, text_blog_sec_parag, text_blog_sec_parag_sub, text_blog_single_page_2, text_blog_single_page_3, text_blog_single_page_4, text_blog_single_page_5, text_blog_single_page_5, text_blog_single_page_6, text_blog_single_page_7, text_blog_single_page_8, text_blog_single_page_9, text_blog_single_page_10, text_register_1, text_register_2, text_register_3, text_register_4, text_register_5, text_register_6, text_register_7, text_register_8, text_register_9, text_register_10, text_register_11, text_register_12, text_register_13, text_register_14, text_register_15
       
           
     