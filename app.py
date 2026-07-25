import streamlit as st


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Text Encryption Tool",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
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

st.markdown(
"""
<div style="
text-align:center;
padding:45px;
">

<h1 style="
font-size:55px;
color:#38BDF8;
">
🔐 Text Encryption Tool
</h1>


<h2 style="
color:#E2E8F0;
">
Advanced Cryptography & File Security Platform
</h2>


<p style="
color:#CBD5E1;
font-size:20px;
">
A cybersecurity application implementing encryption,
hashing, encoding and secure file protection techniques.
</p>


</div>
""",
unsafe_allow_html=True
)



st.divider()



# ==================================================
# SECURITY DASHBOARD
# ==================================================

st.subheader("📊 Security Dashboard")


c1,c2,c3,c4 = st.columns(4)


dashboard = [

("🔐","20+","Algorithms"),

("🛡","AES + RSA","Encryption"),

("🔍","SHA-256","Hashing"),

("⚡","ACTIVE","Status")

]


for col,item in zip(
    [c1,c2,c3,c4],
    dashboard
):

    with col:

        st.markdown(
        f"""
        <div style="
        background:#111827;
        padding:25px;
        border-radius:18px;
        border:1px solid #334155;
        text-align:center;
        ">

        <h2 style="
        color:#38BDF8;
        ">
        {item[0]}
        </h2>

        <h2 style="
        color:white;
        ">
        {item[1]}
        </h2>

        <p style="
        color:#CBD5E1;
        ">
        {item[2]}
        </p>


        </div>
        """,
        unsafe_allow_html=True
        )


st.divider()



# ==================================================
# SECURITY CAPABILITIES
# ==================================================

st.subheader("🛡 Security Capabilities")


col1,col2,col3 = st.columns(3)


with col1:

    st.markdown(
    """
    <div style="
    background:#111827;
    padding:25px;
    border-radius:18px;
    border:1px solid #334155;
    height:220px;
    ">

    <h3 style="color:#38BDF8;">
    🔒 Encryption Engine
    </h3>

    <p style="color:#CBD5E1;">

    • AES-256 GCM
    <br>
    • RSA-2048
    <br>
    • Fernet
    <br>
    • Classical Ciphers

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



with col2:

    st.markdown(
    """
    <div style="
    background:#111827;
    padding:25px;
    border-radius:18px;
    border:1px solid #334155;
    height:220px;
    ">

    <h3 style="color:#38BDF8;">
    🔍 Integrity Engine
    </h3>

    <p style="color:#CBD5E1;">

    • SHA-256 Hashing
    <br>
    • BCrypt Security
    <br>
    • Password Verification

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



with col3:

    st.markdown(
    """
    <div style="
    background:#111827;
    padding:25px;
    border-radius:18px;
    border:1px solid #334155;
    height:220px;
    ">

    <h3 style="color:#38BDF8;">
    📂 File Security
    </h3>

    <p style="color:#CBD5E1;">

    • File Encryption
    <br>
    • File Decryption
    <br>
    • File Hash Verification

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


st.divider()



# ==================================================
# SECURITY WORKFLOW
# ==================================================

st.subheader("🔄 Security Workflow")


st.markdown(
"""
<div style="
background:#111827;
padding:30px;
border-radius:20px;
border:1px solid #334155;
text-align:center;
">

<h3 style="color:#38BDF8;">
INPUT DATA
</h3>

⬇️

<h3 style="color:#38BDF8;">
CRYPTO PROCESSING
</h3>

⬇️

<h3 style="color:#38BDF8;">
SECURE OUTPUT
</h3>


</div>
""",
unsafe_allow_html=True
)



st.divider()



# ==================================================
# SYSTEM STATUS
# ==================================================

st.subheader("💻 System Status")


st.markdown(
"""
<div style="
background:#020617;
padding:25px;
border-radius:18px;
border:1px solid #334155;
font-family:monospace;
">

<p style="color:#22C55E;">
✓ Encryption Engine Loaded
</p>

<p style="color:#22C55E;">
✓ Hash Module Active
</p>

<p style="color:#22C55E;">
✓ File Security Enabled
</p>

<p style="color:#22C55E;">
✓ Key Management Ready
</p>


<h4 style="color:#38BDF8;">
>>> System Ready...
</h4>


</div>
""",
unsafe_allow_html=True
)



st.divider()



# ==================================================
# QUICK ACCESS
# ==================================================

st.subheader("🚀 Quick Access")


st.markdown(
"""
<style>

[data-testid="stPageLink"] a {

background:#111827 !important;
border:1px solid #38BDF8 !important;
border-radius:15px !important;

padding:18px !important;

color:#38BDF8 !important;

font-weight:bold !important;

}


[data-testid="stPageLink"] a:hover {

background:#1E293B !important;

}

</style>
""",
unsafe_allow_html=True
)



q1,q2,q3,q4 = st.columns(4)


with q1:

    st.page_link(
        "pages/1_Encryption.py",
        label="🔒 Encryption",
        use_container_width=True
    )


with q2:

    st.page_link(
        "pages/2_Hashing.py",
        label="🔐 Hashing",
        use_container_width=True
    )


with q3:

    st.page_link(
        "pages/3_Encoding.py",
        label="🔤 Encoding",
        use_container_width=True
    )


with q4:

    st.page_link(
        "pages/4_File_Encryption.py",
        label="📂 File Security",
        use_container_width=True
    )



st.divider()



# ==================================================
# DEVELOPER
# ==================================================

st.subheader("👩‍💻 Developer")


st.markdown(
"""
<div style="
background:#111827;
padding:30px;
border-radius:20px;
border:1px solid #334155;
text-align:center;
">

<h2 style="color:#38BDF8;">
Bhoomika B C
</h2>


<p style="color:#CBD5E1;">

B.E Computer Science Engineering
<br>
Cybersecurity Student

</p>


<p style="color:#CBD5E1;">

Building practical cybersecurity
applications using Python and cryptography.

</p>


</div>
""",
unsafe_allow_html=True
)



# ==================================================
# SOCIAL LINKS
# ==================================================

st.markdown(
"""
<style>

.social-link {

text-decoration:none;

}


.social-card {

background:#111827;
border:1px solid #334155;
border-radius:15px;

padding:18px;

text-align:center;

height:140px;

transition:0.3s;

}


.social-card:hover {

border:1px solid #38BDF8;
transform:translateY(-5px);

}


.icon {

font-size:32px;

}


.title {

color:#38BDF8;
font-size:18px;
font-weight:bold;

}


.desc {

color:#CBD5E1;
font-size:14px;

}


</style>
""",
unsafe_allow_html=True
)


s1,s2,s3 = st.columns(3)


with s1:

    st.markdown(
    """
    <a class="social-link"
    href="YOUR_GITHUB_LINK"
    target="_blank">

    <div class="social-card">

    <div class="icon">
    🐙
    </div>

    <div class="title">
    GitHub
    </div>

    <div class="desc">
    View my projects
    </div>

    </div>

    </a>
    """,
    unsafe_allow_html=True
    )



with s2:

    st.markdown(
    """
    <a class="social-link"
    href="YOUR_LINKEDIN_LINK"
    target="_blank">

    <div class="social-card">

    <div class="icon">
    💼
    </div>

    <div class="title">
    LinkedIn
    </div>

    <div class="desc">
    Professional profile
    </div>

    </div>

    </a>
    """,
    unsafe_allow_html=True
    )



with s3:

    st.markdown(
    """
    <a class="social-link"
    href="mailto:bhoomikagowda518@gmail.com">

    <div class="social-card">

    <div class="icon">
    ✉️
    </div>

    <div class="title">
    Email
    </div>

    <div class="desc">
    Contact me directly
    </div>

    </div>

    </a>
    """,
    unsafe_allow_html=True
    )
st.divider()



# ==================================================
# FOOTER
# ==================================================

st.markdown(
"""
<div style="
text-align:center;
color:#94A3B8;
padding:20px;
">

<h4>
TEXT ENCRYPTION TOOL v1.0
</h4>

<p>
Python | Cryptography | Streamlit
</p>

<p>
Engineered by Bhoomika B C
</p>

</div>
""",
unsafe_allow_html=True
)