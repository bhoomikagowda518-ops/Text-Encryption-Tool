import streamlit as st
import tempfile
import os

from algorithms.file_sha256 import file_sha256
from algorithms.file_encrypt import file_encrypt
from algorithms.file_decrypt import file_decrypt
# ==================================================
# FILE PREVIEW FUNCTION
# ==================================================

def preview_file(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        st.subheader("📄 File Preview")

        st.text_area(
            "Decrypted Content",
            content,
            height=250
        )

    except UnicodeDecodeError:

        st.warning(
            "⚠️ This file cannot be previewed as text."
        )


# ==================================================
# SESSION STATE
# ==================================================

if "file_output" not in st.session_state:
    st.session_state.file_output = ""

if "download_file" not in st.session_state:
    st.session_state.download_file = None


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="File Security",
    page_icon="📂",
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
# PAGE
# ==================================================

st.title("📂 File Security Center")

st.markdown("""
Secure your files using hashing and encryption.
""")

st.divider()


# ==================================================
# STATS
# ==================================================

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
        <div class="stats-title">Category</div>
        <div class="stats-value">Files</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Supported</div>
        <div class="stats-value">All</div>
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


# ==================================================
# ALGORITHM SELECTION
# ==================================================

st.subheader("🚀 Choose a File Algorithm")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📄 File SHA-256", use_container_width=True):
        st.session_state.file_algorithm = "File SHA-256"

with col2:
    if st.button("🔒 File Encrypt", use_container_width=True):
        st.session_state.file_algorithm = "File Encrypt"

with col3:
    if st.button("🔓 File Decrypt", use_container_width=True):
        st.session_state.file_algorithm = "File Decrypt"


if "file_algorithm" not in st.session_state:
    st.session_state.file_algorithm = "File SHA-256"

algorithm = st.session_state.file_algorithm

st.success(f"✅ Selected Algorithm: {algorithm}")
# ==================================================
# Algorithm Information
# ==================================================

st.subheader("📘 Algorithm Information")

algorithm_info = {

    "File SHA-256": {
        "description": "Generate a SHA-256 hash of any uploaded file.",
        "key": "Upload File",
        "security": "★★★★★"
    },

    "File Encrypt": {
        "description": "Encrypt files securely using the Fernet symmetric encryption algorithm.",
        "key": "Upload File",
        "security": "★★★★☆"
    },

    "File Decrypt": {
        "description": "Decrypt files that were previously encrypted using Fernet.",
        "key": "Encrypted File",
        "security": "★★★★☆"
    }

}

info = algorithm_info[algorithm]

col1, col2 = st.columns([3,2])

with col1:

    st.info(
        info["description"]
    )

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

st.caption(
    f"Required Input : {info['key']}"
)

st.divider()


# ==================================================
# Upload File
# ==================================================

st.subheader("📂 Upload File")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=None
)

if uploaded_file:

    st.success(
        f"Selected File : {uploaded_file.name}"
    )

st.divider()
# ==================================================
# Process Button
# ==================================================

process = st.button(
    "⚙ Process File",
    use_container_width=True
)

st.divider()

# ==================================================
# File Processing
# ==================================================

if process:

    if uploaded_file is None:

        st.warning(
            "Please upload a file first."
        )

    else:

        try:

            # Save uploaded file temporarily

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=os.path.splitext(uploaded_file.name)[1]
            ) as temp_file:

                temp_file.write(
                    uploaded_file.getbuffer()
                )

                temp_path = temp_file.name


            # ===========================
            # FILE SHA256
            # ===========================

            if algorithm == "File SHA-256":

                st.session_state.file_output = file_sha256(
                    temp_path
                )

                st.session_state.download_file = None

                st.success(
                    "SHA-256 Hash Generated Successfully ✅"
                )


            # ===========================
            # FILE ENCRYPT
            # ===========================

            elif algorithm == "File Encrypt":

                encrypted_path = file_encrypt(
                    temp_path
                )

                st.session_state.file_output = (
                    "File Encrypted Successfully"
                )

                st.session_state.download_file = encrypted_path

                st.success(
                    "File Encryption Successful 🔒"
                )


            # ===========================
            # FILE DECRYPT
            # ===========================

            elif algorithm == "File Decrypt":
                decrypted_path = file_decrypt(temp_path)
                st.session_state.file_output = ("File Decrypted Successfully")
                st.session_state.download_file = decrypted_path
                st.success("File Decryption Successful 🔓")
                preview_file(decrypted_path)


        except Exception as e:

            st.error(
                f"Error : {e}"
            )
# ==================================================
# Output
# ==================================================

st.subheader("📄 Output")

st.text_area(
    "Result",
    value=st.session_state.file_output,
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
    navigator.clipboard.writeText(`{st.session_state.file_output}`);
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

    if st.session_state.download_file:

        with open(st.session_state.download_file, "rb") as file:

            st.download_button(
                "⬇ Download Processed File",
                data=file,
                file_name=os.path.basename(st.session_state.download_file),
                use_container_width=True
            )

    else:

        st.download_button(
            "⬇ Download Hash",
            data=st.session_state.file_output,
            file_name="file_hash.txt",
            mime="text/plain",
            use_container_width=True
        )