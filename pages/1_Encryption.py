import streamlit as st
from algorithms.aes_encrypt import aes_encrypt
from algorithms.aes_decrypt import aes_decrypt
from algorithms.caesar_encrypt import caesar_encrypt
from algorithms.vigenere_encrypt import vigenere_encrypt
from algorithms.fernet_encrypt import fernet_encrypt
from algorithms.fernet_decrypt import fernet_decrypt
from algorithms.rsa_encrypt import rsa_encrypt
from algorithms.rsa_decrypt import rsa_decrypt
if "output" not in st.session_state:
    st.session_state.output = ""

st.set_page_config(
    page_title="Encryption",
    page_icon="🔒",
    layout="wide"
)

# ---------- Load CSS ----------

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------- Page ----------

st.title("🔒 Encryption Center")

st.markdown("""
Encrypt and decrypt messages using modern and classical cryptographic algorithms.
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Algorithms</div>
        <div class="stats-value">6</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Modern</div>
        <div class="stats-value">AES</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Public Key</div>
        <div class="stats-value">RSA</div>
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

st.subheader("🚀 Choose an Encryption Algorithm")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔐 AES-256 GCM", use_container_width=True):
        st.session_state.encryption_algorithm = "AES-256 GCM"

with col2:
    if st.button("🔑 RSA-2048", use_container_width=True):
        st.session_state.encryption_algorithm= "RSA-2048"

with col3:
    if st.button("🛡 Fernet", use_container_width=True):
        st.session_state.encryption_algorithm= "Fernet"


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏛 Caesar Cipher", use_container_width=True):
        st.session_state.encryption_algorithm = "Caesar Cipher"

with col2:
    if st.button("🔄 ROT13", use_container_width=True):
        st.session_state.encryption_algorithm= "ROT13"

with col3:
    if st.button("🔤 Vigenère Cipher", use_container_width=True):
        st.session_state.encryption_algorithm= "Vigenère Cipher"

if "encryption_algorithm" not in st.session_state:
    st.session_state.encryption_algorithm = "AES-256 GCM"

algorithm = st.session_state.encryption_algorithm

algorithm = st.session_state.encryption_algorithm
st.success(f"✅ Selected Algorithm: {algorithm}")

# ==================================================
# Algorithm Information
# ==================================================

st.subheader("📘 Algorithm Information")

algorithm_info = {
    "AES-256 GCM": {
        "description": "Industry-standard symmetric encryption.",
        "key": "256-bit Secret Key",
        "security": "★★★★★"
    },

    "RSA-2048": {
        "description": "Public-Key Encryption",
        "key": "Public & Private Keys",
        "security": "★★★★★"
    },

    "Fernet": {
        "description": "Authenticated Symmetric Encryption",
        "key": "Fernet Key",
        "security": "★★★★☆"
    },

    "Caesar Cipher": {
        "description": "Classical Shift Cipher",
        "key": "Shift Value",
        "security": "★☆☆☆☆"
    },

    "ROT13": {
        "description": "Fixed Rotation Cipher",
        "key": "No Key Required",
        "security": "★☆☆☆☆"
    },

    "Vigenère Cipher": {
        "description": "Polyalphabetic Cipher",
        "key": "Keyword",
        "security": "★★☆☆☆"
    }
}

info = algorithm_info[algorithm]

col1, col2 = st.columns([3,2])

with col1:
    st.info(info["description"])

with col2:
    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            padding:15px;
            border-radius:12px;
            text-align:center;
            border:1px solid #334155;
        ">
            <div style="color:#94A3B8;font-size:14px;">
                Security
            </div>
            <div style="color:#FACC15;font-size:28px;font-weight:bold;">
                {info["security"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.caption(f"Required Key : {info['key']}")
if algorithm == "AES-256 GCM":

    st.success(
        "🔑 AES Key Status: Available (Managed Securely)"
    )

st.divider()

# ==================================================
# Input
# ==================================================

st.subheader("📝 Input Text")

plaintext = st.text_area(
    "",
    height=180,
    placeholder="Enter plain text to encrypt or encrypted text to decrypt..."
)
st.info(
    "💡 Enter plain text to encrypt, or paste encrypted text here to decrypt. For Caesar and Vigenère, use the same key that was used during encryption."
)

# Dynamic Input

if algorithm == "Caesar Cipher":

    key = st.slider(
        "Shift Value",
        1,
        25,
        3
    )


elif algorithm == "ROT13":

    key = None

    st.info(
        "ROT13 does not require a key."
    )


elif algorithm == "AES-256 GCM":

    key = None

    st.info(
        "🔑 AES key is managed securely by the application."
    )

elif algorithm == "Fernet":

    key = None

    st.info(
        "🔑 Fernet key is managed securely by the application."
    )
elif algorithm == "RSA-2048":

    key = None

    st.info(
        "🔑 RSA keys are managed securely using public/private key pairs."
    )

else:
    key = st.text_input(
        "Encryption Key",
        type="password"
    )

st.divider()

# ==================================================
# Action Buttons
# ==================================================

col1, col2 = st.columns(2)

with col1:
    encrypt = st.button(
        "🔐 Encrypt",
        use_container_width=True
    )

with col2:
    decrypt = st.button(
        "🔓 Decrypt",
        use_container_width=True
    )

st.divider()
# ==============================
# AES ENCRYPTION CONNECTION
# ==============================

if encrypt:

    if not plaintext:
        st.warning("Please enter text first")

    else:

        try:

            if algorithm == "AES-256 GCM":

                with st.spinner("🔐 Applying AES-256 GCM encryption..."):
                    st.session_state.output = aes_encrypt(plaintext)


            elif algorithm == "Caesar Cipher":
                with st.spinner("🏛 Applying Caesar cipher..."):
                    st.session_state.output = caesar_encrypt(plaintext,key)


            elif algorithm == "ROT13":

                from algorithms.rot13 import rot13

                st.session_state.output = rot13(
                    plaintext
                )


            elif algorithm == "Vigenère Cipher":
                with st.spinner("🔤 Applying Vigenère cipher..."):
                    st.session_state.output = vigenere_encrypt(plaintext,key)
            elif algorithm == "Fernet":
                with st.spinner("🔐 Applying Fernet encryption..."):
                    st.session_state.output = fernet_encrypt(plaintext)
            elif algorithm == "RSA-2048":
                with st.spinner("🔑 Encrypting using RSA public key..."):
                    st.session_state.output = rsa_encrypt(plaintext)
            st.success(
                f"{algorithm} Encryption Successful 🔐"
            )


        except Exception as e:

            st.error(
                f"Encryption Error: {e}"
            )

# ==============================
# AES DECRYPTION CONNECTION
# ==============================

if decrypt:

    if not plaintext:
        st.warning("Please enter encrypted text first")

    else:

        try:

            if algorithm == "AES-256 GCM":

                st.session_state.output = aes_decrypt(
                    plaintext
                )


            elif algorithm == "Caesar Cipher":

                from algorithms.caesar_decrypt import caesar_decrypt

                st.session_state.output = caesar_decrypt(
                    plaintext,
                    key
                )


            elif algorithm == "ROT13":

                from algorithms.rot13 import rot13
                with st.spinner("🔄 Applying ROT13 transformation..."):
                    st.session_state.output = rot13(plaintext)

                

            elif algorithm == "Vigenère Cipher":

                from algorithms.vigenere_decrypt import vigenere_decrypt

                st.session_state.output = vigenere_decrypt(
                    plaintext,
                    key
                )
            elif algorithm == "Fernet":
                st.session_state.output = fernet_decrypt(
                    plaintext
                )
            elif algorithm == "RSA-2048":
                st.session_state.output = rsa_decrypt(
                    plaintext
                    )


            st.success(
                f"{algorithm} Decryption Successful 🔓"
            )


        except Exception as e:

            st.error(
                f"Decryption Error: {e}"
            )
# Output
# ==================================================

st.subheader("📄 Output")

st.text_area(
    "Result",
    value=st.session_state.output,
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
    navigator.clipboard.writeText(`{st.session_state.output}`);
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
        data=st.session_state.output,
        file_name="encrypted_output.txt",
        mime="text/plain",
        use_container_width=True
    )