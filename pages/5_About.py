import streamlit as st


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="About Text Encryption Tool",
    page_icon="📖",
    layout="wide"
)


# ==================================================
# LOAD CSS
# ==================================================

def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()


# ==================================================
# HERO SECTION
# ==================================================

st.title("📖 About Text Encryption Tool")

st.markdown(
"""
## 🔐 Advanced Cryptography & File Security Toolkit

**Text Encryption Tool** is a cybersecurity application built using
**Python and Streamlit** that demonstrates practical implementation
of cryptography concepts.

The application provides hands-on experience with:

🔒 Encryption  
🔐 Hashing  
🔤 Encoding  
📂 File Security  
🗝️ Key Management  

Built with the goal of understanding how real-world security
systems protect sensitive information.
"""
)


st.divider()


# ==================================================
# PROJECT STATISTICS
# ==================================================

st.subheader("📊 Project Statistics")


col1, col2, col3, col4 = st.columns(4)


stats = [
    ("🔐", "20+", "Security Algorithms"),
    ("🛡️", "5", "Security Modules"),
    ("🐍", "Python", "Development"),
    ("📅", "2026", "Project Year")
]


for col, stat in zip(
    [col1, col2, col3, col4],
    stats
):

    with col:

        st.markdown(
        f"""
        <div style="
            background:#1E293B;
            padding:20px;
            border-radius:15px;
            text-align:center;
            border:1px solid #334155;
        ">

        <div style="
            font-size:30px;
        ">
        {stat[0]}
        </div>

        <div style="
            color:#38BDF8;
            font-size:28px;
            font-weight:bold;
        ">
        {stat[1]}
        </div>

        <div style="
            color:#CBD5E1;
            font-size:14px;
        ">
        {stat[2]}
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )
st.divider()



# ==================================================
# PROJECT OVERVIEW
# ==================================================

st.subheader("🚀 Project Overview")


st.write(
"""
Text Encryption Tool was developed to bridge the gap between
cybersecurity theory and practical implementation.

The project focuses on understanding how different security
mechanisms work by implementing encryption algorithms, hashing
functions, encoding techniques and file protection systems.

Through this project, concepts like confidentiality, integrity,
secure storage and cryptographic operations are explored.
"""
)


st.divider()


# ==================================================
# FEATURES
# ==================================================

st.subheader("⚡ Key Features")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.info(
"""
🔒 Encryption Center

• AES Encryption
• RSA Encryption
• Fernet
• Classical Ciphers
"""
)


with col2:

    st.info(
"""
🔐 Hashing Center

• SHA-256
• BCrypt
• Password Verification
"""
)


with col3:

    st.info(
"""
🔤 Encoding Center

• Base64
• Hex Encoding
• Data Conversion
"""
)


with col4:

    st.info(
"""
📂 File Security

• File Hashing
• File Encryption
• File Decryption
"""
)


st.divider()


# ==================================================
# TECHNOLOGIES
# ==================================================

st.subheader("🛠 Technologies Used")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.success(
"""
🐍 Python

Core programming language

Used for:
• Logic
• Algorithms
• Security operations
"""
)


with col2:

    st.success(
"""
🎨 Streamlit

Frontend framework

Used for:
• Interactive UI
• Dashboard
• Web application
"""
)


with col3:

    st.success(
"""
🔐 Cryptography

Security library

Used for:
• Encryption
• Key management
"""
)


with col4:

    st.success(
"""
🔑 BCrypt

Password security

Used for:
• Secure hashing
• Verification
"""
)


st.divider()


# ==================================================
# DEVELOPER SECTION
# ==================================================

st.subheader("👩‍💻 Developer")


st.markdown(
"""
### Bhoomika B C

**B.E Computer Science Engineering (Cybersecurity)**


Passionate about:

🔹 Cybersecurity  
🔹 Python Development  
🔹 Secure Applications  
🔹 Cryptography  
🔹 Ethical Hacking  


This project represents my journey of learning cybersecurity
through practical implementation and building real-world tools.
"""
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
    """
    <a href="https://github.com/bhoomikagowda518-ops" target="_blank">

    <button style="
    width:100%;
    padding:12px;
    background:#1E293B;
    color:white;
    border-radius:10px;
    border:1px solid #38BDF8;
    font-size:16px;
    ">
    💻 GitHub
    </button>

    </a>
    """,
    unsafe_allow_html=True
    )


with col2:

    st.markdown(
    """
    <a href="https://www.linkedin.com/in/bhoomikabc2008" target="_blank">

    <button style="
    width:100%;
    padding:12px;
    background:#1E293B;
    color:white;
    border-radius:10px;
    border:1px solid #38BDF8;
    font-size:16px;
    ">
    🔗 LinkedIn
    </button>

    </a>
    """,
    unsafe_allow_html=True
    )


with col3:

    st.markdown(
"""
<a href="mailto:bhoomikagowda518@gmail.com">

<button style="
width:100%;
padding:12px;
background:#1E293B;
color:white;
border-radius:10px;
border:1px solid #38BDF8;
font-size:16px;
cursor:pointer;
">
📧 Email
</button>

</a>
""",
unsafe_allow_html=True
)
st.divider()


# ==================================================
# LEARNING OBJECTIVES
# ==================================================

st.subheader("🎯 Learning Objectives")


objectives = [

    "Understanding encryption and decryption techniques",

    "Implementing modern and classical cryptographic algorithms",

    "Learning secure key management practices",

    "Understanding hashing and data integrity",

    "Working with file security concepts",

    "Developing cybersecurity applications using Python"

]


for item in objectives:

    st.write("✅ " + item)


st.divider()


# ==================================================
# FUTURE ROADMAP
# ==================================================

st.subheader("🚀 Future Enhancements")


future = [

    "Digital Signature Implementation",

    "Password Strength Analyzer",

    "Security Logging Dashboard",

    "Web Security Scanner",

    "Database Integration"

]


for item in future:

    st.write("🔜 " + item)



st.divider()


# ==================================================
# FOOTER
# ==================================================

st.caption(
"""
Built with ❤️ and curiosity by Bhoomika B C

B.E CSE (Cybersecurity) | Python | Cybersecurity | Cryptography
"""
)