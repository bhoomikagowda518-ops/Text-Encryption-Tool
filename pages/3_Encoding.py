import streamlit as st

from algorithms.base64_encode import base64_encode
from algorithms.base64_decode import base64_decode
from algorithms.hex_encode import hex_encode
from algorithms.hex_decode import hex_decode

# ==================================================
# SESSION STATE
# ==================================================

if "encoding_output" not in st.session_state:
    st.session_state.encoding_output= ""

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Encoding",
    page_icon="🔤",
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

st.title("🔤 Encoding Center")

st.markdown("""
Encode and decode text using common encoding algorithms.
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
        <div class="stats-value">4</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Category</div>
        <div class="stats-value">Encoding</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">Reversible</div>
        <div class="stats-value">Yes</div>
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

st.subheader("🚀 Choose an Encoding Algorithm")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🔤 Base64 Encode",
        use_container_width=True
    ):
        st.session_state.encoding_algorithm = "Base64 Encode"

with col2:
    if st.button(
        "🔓 Base64 Decode",
        use_container_width=True
    ):
        st.session_state.encoding_algorithm = "Base64 Decode"

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🔢 Hex Encode",
        use_container_width=True
    ):
        st.session_state.encoding_algorithm = "Hex Encode"

with col2:
    if st.button(
        "🔄 Hex Decode",
        use_container_width=True
    ):
        st.session_state.encoding_algorithm = "Hex Decode"

if "encoding_algorithm" not in st.session_state:
    st.session_state.encoding_algorithm = "Base64 Encode"

algorithm = st.session_state.encoding_algorithm

st.success(
    f"✅ Selected Algorithm: {algorithm}"
)

# ==================================================
# ALGORITHM INFORMATION
# ==================================================

st.subheader("📘 Algorithm Information")

algorithm_info = {

    "Base64 Encode": {
        "description": "Encodes plain text into Base64 format.",
        "key": "No Key Required",
        "security": "⭐☆☆☆☆"
    },

    "Base64 Decode": {
        "description": "Decodes Base64 text back to its original form.",
        "key": "No Key Required",
        "security": "⭐☆☆☆☆"
    },

    "Hex Encode": {
        "description": "Converts text into hexadecimal representation.",
        "key": "No Key Required",
        "security": "⭐☆☆☆☆"
    },

    "Hex Decode": {
        "description": "Converts hexadecimal text back to normal text.",
        "key": "No Key Required",
        "security": "⭐☆☆☆☆"
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

st.caption(f"Required Input : {info['key']}")

st.divider()

# ==================================================
# INPUT
# ==================================================

st.subheader("📝 Input Text")

plaintext = st.text_area(
    "",
    height=180,
    placeholder="Enter text here..."
)

st.info(
    "Encoding algorithms do not require a secret key."
)

st.divider()
# ==================================================
# Action Buttons
# ==================================================

col1, col2 = st.columns(2)

with col1:
    encode = st.button(
        "🔐 Encode",
        use_container_width=True
    )

with col2:
    decode = st.button(
        "🔓 Decode",
        use_container_width=True
    )

st.divider()

# ==============================
# ENCODING
# ==============================

if encode:

    if not plaintext:

        st.warning("Please enter text first")

    else:

        try:

            if algorithm == "Base64 Encode":

                st.session_state.encoding_output = base64_encode(
                    plaintext
                )

            elif algorithm == "Hex Encode":

                st.session_state.encoding_output= hex_encode(
                    plaintext
                )

            else:

                st.warning(
                    "Please select an Encode algorithm."
                )

            if st.session_state.encoding_output:

                st.success(
                    f"{algorithm} Successful 🔐"
                )

        except Exception as e:

            st.error(
                f"Encoding Error: {e}"
            )

# ==============================
# DECODING
# ==============================

if decode:

    if not plaintext:

        st.warning("Please enter encoded text first")

    else:

        try:

            if algorithm == "Base64 Decode":

                st.session_state.encoding_output = base64_decode(
                    plaintext
                )

            elif algorithm == "Hex Decode":

                st.session_state.encoding_output = hex_decode(
                    plaintext
                )

            else:

                st.warning(
                    "Please select a Decode algorithm."
                )

            if st.session_state.encoding_output:

                st.success(
                    f"{algorithm} Successful 🔓"
                )

        except Exception as e:

            st.error(
                f"Decoding Error: {e}"
            )
# ==================================================
# Output
# ==================================================

st.subheader("📄 Output")

st.text_area(
    "Result",
    value=st.session_state.encoding_output,
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
    navigator.clipboard.writeText(`{st.session_state.encoding_output}`);
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
        data=st.session_state.encoding_output,
        file_name="encoded_output.txt",
        mime="text/plain",
        use_container_width=True
    )