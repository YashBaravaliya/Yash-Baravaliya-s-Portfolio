import streamlit as st
from PIL import Image
import base64
from streamlit_autorefresh import st_autorefresh



def load_image(image_file):
    img = Image.open(image_file)
    return img

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def main():
    st.set_page_config(page_title="Yash Baravaliya's Portfolio", layout="wide")


    with st.sidebar:
        st.title("Navigation")
        st.write("Use the links below to navigate through sections:")
        
        st.markdown("[About Me](#about-me)")
        st.markdown("[Skills](#skills)")
        st.markdown("[Certificates](#certificates)")
        st.markdown("[Projects](#projects)")
        st.markdown("[Education](#education)")
        st.markdown("[Blogs](#my-medium-blogs)")
        st.markdown("[Experience](#experience)")

        st.write("---")
        st.title("Contact Information")
        st.write("Email: yashbaravaliya206@gmail.com")
        st.write("Location: Surat, India")

        st.write("---")
        st.title("Quick Links")
        st.markdown("[LinkedIn Profile](https://linkedin.com/in/yash-baravaliya)")
        st.markdown("[Medium Articles](https://medium.com/@yashbaravaliya206)")


    
    # Set background image
    # set_background('images\yash.png')  # Replace with your background image path
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>Yash Baravaliya's Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Shaping the Future with AI & Data Science</h2>", unsafe_allow_html=True)

    st.write("---")


    col1, col2 = st.columns([1, 2])

    with col1:
        image = load_image('images\yash.png')  # Replace with your photo path
        st.image(image, use_column_width=True)
    # Include FontAwesome CSS
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """, unsafe_allow_html=True)
    with col2:
        st.markdown("<h1>Yash Baravaliya</h1>", unsafe_allow_html=True)
        st.write("Aspiring Data Scientist | AI Enthusiast")
        
        st.markdown('<p><i class="fas fa-envelope"></i> Email: yashbaravaliya206@gmail.com</p>', unsafe_allow_html=True)
        # st.markdown('<p><i class="fas fa-phone"></i> Phone: 9724799722</p>', unsafe_allow_html=True)
        st.markdown('<p><i class="fas fa-map-marker-alt"></i> Location: Surat, India</p>', unsafe_allow_html=True)
        st.markdown('<p><i class="fab fa-linkedin"></i> LinkedIn: <a href="https://linkedin.com/in/yash-baravaliya" target="_blank">Yash Baravaliya</a></p>', unsafe_allow_html=True)
        st.markdown('<p><i class="fab fa-medium"></i> Medium: <a href="https://medium.com/@yashbaravaliya206" target="_blank">@yashbaravaliya206</a></p>', unsafe_allow_html=True)


    st.write("---")
    st.header("About Me")
    st.write("""
    I'm a dedicated computer engineering student with a strong focus on AI and data science. 
    Certified in data science, I'm actively applying machine learning, deep learning, and computer vision skills 
    through academic projects and internships. I'm passionate about translating complex data into actionable 
    insights and eager to contribute to innovative data-driven solutions.
    """)

    st.write("---")
    st.header("Skills")

    # Define skills for each category
    ds_skills = [
        ("Python", "🐍"), ("Statistical Analysis", "📊"), ("Machine Learning", "🤖"), 
        ("Deep Learning", "🧠"), ("Computer Vision", "👁️"), ("NLP", "🗣️"), 
        ("Generative AI", "🎨"), ("MLOps", "🛠️"), ("Data Visualization", "📈"),
        ("Data Cleaning & Preprocessing", "🧹"), ("Big Data", "💾")
    ]

    programming_skills = [
        ("Python", "🐍"), ("C", "💻"), 
        ("JavaScript", "🟨"), ("SQL", "🗄️"), ("Git & Version Control", "🔧")
    ]

    backend_skills = [
        ("Flask", "🍶"), ("Django", "🌐"), ("APIs", "🔗"), 
        ("FastAPI", "⚡"), ("MySQL", "🐬")
    ]

    frontend_skills = [
        ("HTML", "📄"), ("CSS", "🎨"), ("JavaScript", "🟨"), 
        ("Streamlit", "📊"), ("Bootstrap", "💅")
    ]

    soft_skills = [
        ("Quick Learner", "🚀"), ("Project Management", "📋"), 
        ("Time Management", "⏰"), ("Communication", "💬"), 
        ("Problem Solving", "🧩"), ("Collaboration", "🤝")
    ]

    # Display the skills in a 3-column layout
    def display_skills_in_columns(skills):
        col1, col2, col3 = st.columns(3)
        for i, (skill, icon) in enumerate(skills):
            if i % 3 == 0:
                col1.write(f"{icon} {skill}")
            elif i % 3 == 1:
                col2.write(f"{icon} {skill}")
            else:
                col3.write(f"{icon} {skill}")

    # Display each skill category in columns
    st.subheader("Data Science & AI Skills")
    display_skills_in_columns(ds_skills)

    st.subheader("Programming & Frameworks")
    display_skills_in_columns(programming_skills)

    st.subheader("Backend Development")
    display_skills_in_columns(backend_skills)

    st.subheader("Frontend Development")
    display_skills_in_columns(frontend_skills)

    st.subheader("Soft Skills")
    display_skills_in_columns(soft_skills)

    # Sample certificates
    st.write("---")
    st.header("Certificates")
    certificates = [
        {
            "title": "Data Science Master at PW SKILLS",
            "image": "Certificates\pw.png"  # Replace with actual path
        },
        {
            "title": "Complete Generative AI Course With Langchain and Huggingface",
            "image": "Certificates\gen-ai.jpg"  # Replace with actual path
        },
        {
            "title": "Python for Data Scrence Master Course (2022)",
            "image": "Certificates\ds-master-2022.jpg"  # Replace with actual path
        },
        {
            "title": "Full Stack Web Application Development with Django Framework",
            "image": "Certificates\\full stack.jpg"  # Replace with actual path
        },
    ]

    # Automatically refresh the app every few seconds
    refresh_rate = 5  # Refresh every 5 seconds

    # Use session state to track the current index
    if "cert_index" not in st.session_state:
        st.session_state.cert_index = 0

    # Increment certificate index
    st.session_state.cert_index = (st.session_state.cert_index + 1) % len(certificates)

    # Display the current certificate
    cert = certificates[st.session_state.cert_index]
    st.markdown(f"<h3 style='text-align: center;'>{cert['title']}</h3>", unsafe_allow_html=True)
    st.image(cert["image"], use_column_width=True)
    # st.subheader(cert["title"])
    # st.write(f"Date: {cert['date']}")
    # st.write(cert["description"])

    # Auto-refresh after a specified interval (in milliseconds)
    st_autorefresh(interval=refresh_rate * 1000)  # refresh_rate is in seconds, multiplied by 1000 to convert to milliseconds

    st.write("---")
    st.header("Projects")

    # Create a function to display project details and video
    def display_project(title, date, description, video_url):
        col1, col2 = st.columns([1, 3])  # 80% for text, 20% for video
        with col1:
            st.video(video_url)
        with col2:
            st.subheader(title + f" ({date})")
            st.write(description)

    # Project 1
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("images/p1.jpg")
    with col2:
        st.subheader("MedGuide-AI " + "(06/2024 - Present)",)
        st.write("""
         - Developed a comprehensive healthcare AI application integrating NLP, computer vision, and generative AI technologies
         - Created an AI-powered chatbot for medical information and a medicine information system with image recognition capabilities
         - Implemented geolocation-based medicine availability and Ayurvedic plant identification using computer vision
         - Designed a chemical bond generator utilizing SMILES notation, showcasing versatility in AI applications
         """,)
    # display_project(
    #     "MedGuide-AI",
    #     "06/2024 - Present",
    #     """\
    #     - Developed a comprehensive healthcare AI application integrating NLP, computer vision, and generative AI technologies
    #     - Created an AI-powered chatbot for medical information and a medicine information system with image recognition capabilities
    #     - Implemented geolocation-based medicine availability and Ayurvedic plant identification using computer vision
    #     - Designed a chemical bond generator utilizing SMILES notation, showcasing versatility in AI applications
    #     """,
    #     "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_1"  # Replace with actual video URL
    # )

    # Project 2
    display_project(
        "VisionVault-Check-In",
        "01/2024 - 05/2024",
        """\
        - Developed a user-friendly interface with rapid image capture, model management, and one-click training
        - Implemented efficient face embedding technique, enabling fast training and prediction on CPU for 4+ people simultaneously
        - Designed a lightweight yet powerful model, ensuring lag-free performance and smooth real-time identification
        - Integrated automatic entry and exit logging based on facial recognition predictions, streamlining attendance tracking
        """,
        "https://www.youtube.com/watch?v=btnX4zlrzkQ"  # Replace with actual video URL
    )

    # Project 3
    display_project(
        "SnapSearch",
        "04/2024 - 04/2024",
        """\
        - Created and deployed an advanced image search tool utilizing facial recognition technology
        - Improved image retrieval accuracy by 85% and reduced search time for users by 70%
        - Implemented a user-friendly system that trains on user selfies and efficiently searches personal image collections
        """,
        "https://www.youtube.com/watch?v=HU06ZZOpv4A"  # Replace with actual video URL
    )

    # Project 4
    display_project(
        "PDF Chatbot",
        "03/2024 - 03/2024",
        """\
        - PDF Content Interaction: Allows users to upload PDF documents and ask questions, with the chatbot providing answers based on the document's content.
        - Natural Language Processing (NLP): Utilizes advanced NLP algorithms to understand user queries and extract relevant information from the PDF.
        - User-Friendly Interface: Simple interface for uploading documents and interacting with the chatbot in real-time.
        """,
        "https://www.youtube.com/watch?v=C_z-gbKGmdI"  # Replace with actual video URL
    )

    # Project 5
    display_project(
        "SignVision",
        "01/2024 - 03/2024",
        """\
        - User-Trainable Models: Users can quickly train the system with just a few hand sign images, making it adaptable to personalized sign languages.
        - Custom Sign Recognition: The system recognizes custom hand gestures after minimal training.
        - User-Friendly Interface: Designed with a simple and intuitive UI, allowing easy interaction and fast training of models for hand gesture recognition.
        - https://www.youtube.com/watch?v=npphMmMrXO8
        """,
        "https://www.youtube.com/watch?v=Ho39Tx434Rk"  # Replace with actual video URL
    )
    # Add a section for new projects
    # st.write("---")
    st.header("many more Projects")

    # Create a function to display project cards
    def display_project_card(project_name):
        st.markdown(f"""
        <div style="
            background-color: #f0f0f0;
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        ">
            <h4>{project_name}</h4>
        </div>
        """, unsafe_allow_html=True)

    # List of new project names
    new_projects = [
        "Dimon Price Prediction",
        "Project Report Generator",
        "Fire Forest Prediction",
        "Blog Application using django"
    ]

    # Display each new project in a card
    for project in new_projects:
        display_project_card(project)


    st.write("---")
    st.header("Education")
    
    col1, col2, col3= st.columns(3)
    
    with col1:
        st.subheader("Bachelor of Technology")
        st.write("Computer Engineering with Specialization in AI")
        st.write("Ganpat University")
        st.write("08/2021 - 05/2025")
        st.write("CGPA: 8.15")
    
    with col2:
        st.subheader("HSC GSEB")
        st.write("ASADEEP IIT")
        st.write("2021")
        st.write("Percentage: 75.06%")

    with col3:
        
        st.subheader("SSC GSEB")
        st.write("Sanskartirth Gyanpeeth")
        st.write("2019")
        st.write("Percentage: 77.00%")

    # add blogs-----------------------------------------------------------------------------------------------------------

    blog_posts = [
        {
            "title": "Simple linear regression",
            "link": "https://medium.com/@yashbaravaliya206/simple-linear-regression-4735a601c1ba",
            "description": "Simple linear regression is a statistical technique used to model the relationship between.......",
            "image": "https://miro.medium.com/v2/resize:fit:720/format:webp/1*TQ8CUtDF8cT0XFRB8UcOUQ.png"  # Replace with actual image URL
        },
        {
            "title": "Understanding Variance, Bias, Overfitting, and Underfitting in Machine Learning",
            "link": "https://medium.com/@yashbaravaliya206/understanding-variance-bias-overfitting-and-underfitting-in-machine-learning-dd245118d2ad",
            "description": "Bias refers to the error introduced by approximating a real-world problem with a simplified model.....",
            "image": "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rgKKH5YnauHv7HNgxmImTw.png"  # Replace with actual image URL
        },
        {
            "title": "Feature Scaling and Normalization",
            "link": "https://medium.com/@yashbaravaliya206/feature-scaling-and-normalization-ca484a16882a",
            "description": "Feature scaling and normalization are preprocessing techniques used in Feature Engineering to.......",
            "image": "https://miro.medium.com/v2/resize:fit:828/format:webp/1*9j33xl7N74uvn2uy1xqG7A.png"  # Replace with actual image URL
        },
    ]

    st.write("---")
    st.header("My Medium Blogs")

    for post in blog_posts:
        st.markdown(f"""
        <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 15px; margin-bottom: 20px; display: flex; align-items: center;">
            <div style="flex: 1;">
                <h4 style="margin: 0;">{post['title']}</h4>
                <p>{post['description']}</p>
                <a href="{post['link']}" target="_blank" style="text-decoration: none; color: #4A90E2;">Read More</a>
            </div>
            <img src="{post['image']}" style="width: 150px; height: auto; border-radius: 8px; margin-left: 15px;" />
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.header("Experience")

    st.header("Robocon Internship Experience")

    # Embed the YouTube video using the iframe
    iframe_code = """
    <iframe width="560" height="315" src="https://www.youtube.com/embed/5suAvMmV0ho?start=26160&amp;end=26482" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """

    # Display the iframe in Streamlit
    st.markdown(iframe_code, unsafe_allow_html=True)

    # st.write("U. V. Patel College of Engineering")
    st.write("01/2024 - 08/2024")


    st.markdown("""
    During my internship with the Robocon team, I gained invaluable experience in a real-world project that enhanced my technical skills and fostered collaboration across various engineering disciplines, including electrical, mechanical, and mechatronics.

    ### Key Technical Skills Acquired:
    - **Developed and implemented** computer vision algorithms using OpenCV and TensorFlow.
    - **Integrated software with hardware systems** via Raspberry Pi and Arduino, improving robot autonomous navigation.
    - **Collaborated with mechanical and electrical teams** to ensure seamless software-hardware integration.
    - **Managed control algorithm implementation** on Arduino, enhancing the robot's precision, efficiency, and responsiveness.

    ### Impact of the Experience:
    This internship was instrumental in my personal and professional development. I honed my communication and collaboration skills while navigating challenges with a multidisciplinary team. The experience also provided essential life lessons in time management and problem-solving, significantly shaping my approach to teamwork and project management.

    By the conclusion of my internship, I emerged not only with technical expertise but also with a deeper understanding of effective collaboration in a team-oriented environment.
    """)

    st.video("https://www.youtube.com/watch?v=OKSBI6gRhRo")
    
    # st.subheader("Robocon Internship")
    # st.write("U. V. Patel College of Engineering")
    # st.write("01/2024 - 08/2024")
    # st.write("""
    # - Developed and implemented computer vision algorithms using OpenCV and TensorFlow
    # - Integrated software with hardware systems using Raspberry Pi and Arduino, enhancing robot autonomous navigation
    # - Collaborated with mechanical and electrical teams, aligning software with hardware capabilities
    # - Managed control algorithm implementation on Arduino, improving robot precision, efficiency, and responsiveness
    # """)
    
    # st.subheader("GDSC Data Science Lead")
    # st.write("U. V. Patel College of Engineering")
    # st.write("08/2023 - 08/2024")
    # st.write("""
    # - Facilitated knowledge sharing by coordinating guest lectures and study groups
    # - Managed event logistics, including scheduling, venue booking, and coordination with speakers
    # """)

if __name__ == "__main__":
    main()