import streamlit as st

from algorithms.sha256 import sha256_hash
from algorithms.bcrypt_hash import bcrypt_hash
from algorithms.bcrypt_verify import bcrypt_verify

# PAGE CONFIG
st.set_page_config(
    page_title="Hashing",
    page_icon="🔐",
    layout="wide"
)

# LOAD CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# SESSION OUTPUT
if "hash_output" not in st.session_state:
    st.session_state.hash_output = ""

# PAGE
st.title("🔐 Hashing Center")

st.markdown("""
Generate secure hashes using modern hashing algorithms.
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Algorithms</div>
        <div class="stats-value">3</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Modern</div>
        <div class="stats-value">SHA</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Password</div>
        <div class="stats-value">Bcrypt</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Status</div>
        <div class="stats-value">Ready</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ALGORITHM SELECTION
st.subheader("🚀 Choose Hash Algorithm")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔐 SHA-256", use_container_width=True):
        st.session_state.algorithm = "SHA-256"

with col2:
    if st.button("🔑 BCrypt Hash", use_container_width=True):
        st.session_state.algorithm = "BCrypt Hash"

with col3:
    if st.button("✅ BCrypt Verify", use_container_width=True):
        st.session_state.algorithm = "BCrypt Verify"

if "algorithm" not in st.session_state:
    st.session_state.algorithm = "SHA-256"

algorithm = st.session_state.algorithm

st.success(f"✅ Selected Algorithm: {algorithm}")

# ==================================================
# Algorithm Information
# ==================================================

st.subheader("📘 Algorithm Information")

algorithm_info = {
    "SHA-256": {
        "description": "Secure cryptographic hash algorithm.",
        "key": "No Key Required",
        "security": "⭐⭐⭐⭐☆"
    },
    "BCrypt Hash": {
        "description": "Password hashing algorithm with automatic salt.",
        "key": "Password",
        "security": "⭐⭐⭐⭐⭐"
    },
    "BCrypt Verify": {
        "description": "Verifies a password against an existing BCrypt hash.",
        "key": "Password + Stored Hash",
        "security": "⭐⭐⭐⭐⭐"
    }
}

info = algorithm_info[algorithm]

col1, col2 = st.columns([3, 2])

with col1:
    st.info(info["description"])

with col2:
    st.markdown(
        f"""
### Security
<p style="color:#FFD700;font-size:32px;letter-spacing:3px;">
{info["security"]}
</p>
""",
        unsafe_allow_html=True
    )

st.caption(f"Required Input : {info['key']}")

st.divider()

# INPUT
st.subheader("📝 Input Text")

plaintext = st.text_area(
    "",
    height=180,
    placeholder="Enter text to hash or enter a hash for verification..."
)

st.info(
    "💡 Enter text to generate a hash. For hash verification, enter the original text and the corresponding hash when prompted."
)

stored_hash = ""

# BUTTONS
col1, col2 = st.columns(2)

with col1:
    generate = st.button(
        "🔐 Generate Hash",
        use_container_width=True
    )

with col2:
    verify = st.button(
        "✅ Verify Hash",
        use_container_width=True
    )

# HASH GENERATION
if generate:

    if not plaintext:

        st.warning("Please enter text first")

    else:

        try:

            if algorithm == "SHA-256":

                st.write("Running SHA256")
                st.session_state.hash_output = sha256_hash(plaintext)

            elif algorithm == "BCrypt Hash":

                st.write("Running BCrypt")
                st.session_state.hash_output = bcrypt_hash(plaintext)

            st.success("Operation Completed ✅")

        except Exception as e:

            st.error(f"Error: {e}")

# VERIFY
if algorithm == "BCrypt Verify":

    stored_hash = st.text_input(
        "Enter Stored Hash"
    )

if verify:

    if algorithm != "BCrypt Verify":

        st.warning(
            "Select BCrypt Verify algorithm first"
        )

    elif not plaintext:

        st.warning(
            "Enter password first"
        )

    elif not stored_hash:

        st.warning(
            "Enter stored hash"
        )

    else:

        result = bcrypt_verify(
            plaintext,
            stored_hash
        )

        if result:

            st.session_state.hash_output = "✅ Password Verified"

        else:

            st.session_state.hash_output = "❌ Password Incorrect"

        st.success("Verification Completed ✅")

st.divider()

# OUTPUT
st.subheader("📄 Output")

st.text_area(
    "Result",
    value=st.session_state.hash_output,
    height=180
)

col1, col2 = st.columns(2)

with col1:

    copy_button = f"""
<style>
.copy-btn {{
width:100%;
height:42px;
background:#262730;
color:white;
border-radius:8px;
border:1px solid #555;
font-size:16px;
margin-top:-5px;
}}
</style>

<button class="copy-btn" onclick="
navigator.clipboard.writeText(`{st.session_state.hash_output}`);
alert('Copied to clipboard ✅');
">
📋 Copy Output
</button>
"""

    st.components.v1.html(
        copy_button,
        height=45
    )

with col2:

    st.download_button(
        label="⬇ Download Output",
        data=st.session_state.hash_output,
        file_name="hash_output.txt",
        mime="text/plain",
        use_container_width=True
    )