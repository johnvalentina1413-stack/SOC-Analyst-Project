#SOC AI SYSTEM
import streamlit as st
import pandas as pd
import joblib

# PAGE CONFIG

st.set_page_config(
    page_title="SOC AI Dashboard",
    page_icon="🛡️",
    layout="wide"
)


# UI STYLES

st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #121826;
    color: #E6E6E6;
}

/*BLINKING MAIN TITLE */
@keyframes blinkTitle {
    0% { color: #D6FB61; text-shadow: 0 0 5px #D6FB61; }
    50% { color: #FF1E1E; text-shadow: 0 0 15px #FF1E1E; }
    100% { color: #D6FB61; text-shadow: 0 0 5px #D6FB61; }
}

/* MAIN TITLE (BRIGHT YELLOW) */
h1 {
    color: #D6FB61 !important;
    text-align: center;
    font-size: 55px !important;
    font-family: "Times New Roman";
    font-weight: 900;
    text-shadow: 0 0 10px #D6FB61, 0 0 20px #39B1D1;
    animation: glowPulse 2s infinite ease-in-out;
}

@keyframes glowPulse {
    0% {
        text-shadow: 0 0 5px #D6FB61, 0 0 10px #39B1D1;
    }
    50% {
        text-shadow: 0 0 20px #D6FB61, 0 0 40px #39B1D1;
    }
    100% {
        text-shadow: 0 0 5px #D6FB61, 0 0 10px #39B1D1;
    }
}
/* MARQUEE */
.marquee {
    color: cyan;
    font-size: 26px;
    font-weight: bold;
    letter-spacing: 2px;
    text-shadow:
        0 2px 15px cyan;
}

/* Select Mode label */
h3 {
    font-family: "Times New Roman";
    color:#C9BEFF!important;
    background-color: #1E3A5F;
    font-size: 28px;
    padding: 12px;
    border-radius: 10px;
    font-weight: bold;
    margin-bottom: 15px;
}
/* LABEL NAME */
h2 {
    font-family: "Times New Roman";
    color: #F6FA70!important;
    font-style:Italic;
    font-size:30px;
    text-shadow: 0 2px 10px #F6FA70;
}
    
/* RADIO BUTTON STYLE */

/* Radio text */
.stRadio [role="radiogroup"] label p {
    color: #AEE2FF!important;
    font-size: 22px !important;
    font-weight: 500 !important;
}

/* Hover */
.stRadio [role="radiogroup"] label:hover p {
    color: #FFDE42 !important;
    text-shadow: 0 0 10px #FEEC41;
}

/* Radio dot */
.stRadio input[type="radio"] {
    accent-color:#D62828  !important;
}



/* INPUT NAMES*/
.label-protocol {
             color:#39B1D1; font-weight:bold;
             }
.label-service{ 
            color:#00ff88; font-weight:bold;
             }
.label-flag{
             color:#FEEE91; font-weight:bold;
             }

.label-src {
             color:#FF1E1E; font-weight:bold;
             }
.label-count{
             color:#FF8C00; font-weight:bold;
             }

.label-dst{
             color:#4DA3FF; font-weight:bold;
             }
.label-srv{
             color:#9B59B6; font-weight:bold; 
            }

.label-login{
             color:#00ffcc; font-weight:bold;
             }
.label-serror{
             color:#ff4d4d; font-weight:bold;
             }
.label-rerror{
             color:#ff9966; font-weight:bold;
             }            
     
/* File uploader note */
.upload-note {
    color: #FEEAC9;
    font-weight: bold;
}

/* Buttons */
.stButton>button {
    background-color: #1E90FF;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}
        

.note-box {
    background-color: #3a2a12;
    padding: 14px;
    border-radius: 12px;
    border-left: 6px solid #ff8c00;
    color: #ffd08a;
    font-weight: 600;
    font-size: 14px;
    line-height: 1.5;
    animation: pulseGlow 2s infinite;
}

/* Attack Type */
.attack {
    background-color: #1f3b2c;
    padding: 10px;
    border-radius: 10px;
    color: #00ff88;
    font-weight: bold;
}

/* Explanation */
.explain {
    background-color: #1a2a4a;
    padding: 10px;
    border-radius: 10px;
    color: #4DA3FF;
}

/* Recommendation */
.reco {
    background-color: #3a2a12;
    padding: 10px;
    border-radius: 10px;
    color: orange;
}

/* Risk box */
.risk-box {
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


#LOAD MODEL

model = joblib.load("notebooks/soc_model.pkl")
protocol_enc = joblib.load("notebooks/protocol_encoder.pkl")
service_enc = joblib.load("notebooks/service_encoder.pkl")
flag_enc = joblib.load("notebooks/flag_encoder.pkl")


#TITLE
st.markdown("""

<h1>🛡️ AI SOC ANALYST SYSTEM 🛡️</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class="marquee">
<marquee scrollamount="8">
🌐 Multi-Mode Intrusion Detection System |
📊 Threat Analysis |
🔍 Probe Detection |
🚨 DoS Attack Monitoring |
🔐 Unauthorized Access Detection |
⚡ Privilege Escalation Alerts |
🧠 AI-Powered SOC Recommendation |
</marquee>
</div>
""", unsafe_allow_html=True)

# ADDED NOTE 
st.markdown("""
<div class="note-box">
⚠ NOTE:<br><br>
This is a prototype AI-based SOC Analyst system developed for academic purposes.  
It demonstrates machine learning-based intrusion detection using the NSL-KDD dataset.  
It can be extended into a real-time enterprise SOC system with live network monitoring.
Prediction results may vary depending on the input data and dataset limitations.
 Future improvements can be achieved through additional training on larger and more diverse cybersecurity datasets.
</div>
""", unsafe_allow_html=True)

st.divider()


# MODE
st.markdown("<h3>⚙️ Choose Analysis Method</h3>",unsafe_allow_html=True)

mode = st.radio(
    "",
    ["Manual Analysis", "Upload CSV Log File", "Paste Log Entry"]
)


# MAPS

risk_map = {
    "Normal": "Low",
    "Probe": "Medium",
    "DoS": "High",
    "Unauthorized Access": "High",
    "Privilege Escalation": "Critical"
}

recommendation_map = {
    "Normal": "No action required.",
    "DoS": "Block traffic spikes, enable rate limiting.",
    "Probe": "Investigate scanning activity.",
    "Unauthorized Access": "Reset credentials, enable MFA.",
    "Privilege Escalation": "CRITICAL: isolate system immediately."
}

attack_explanation_map = {
    "Normal": "Normal network activity.",
    "DoS": "Denial of Service attack.",
    "Probe": "Scanning activity detected.",
    "Unauthorized Access": "Login attack attempt.",
    "Privilege Escalation": "Admin access attempt."
}


#RISK FUNCTION
def show_risk(level):
    if level == "Low":
        st.success("🟢 LOW RISK")
    elif level == "Medium":
        st.info("🟡 MEDIUM RISK")
    elif level == "High":
        st.warning("🟠 HIGH RISK")
    else:
        st.error("🔴 CRITICAL RISK")


#OUTPUT FUNCTION
def show_results(pred, risk):

    st.markdown(f"<div class='attack'>🧠 Attack Type: {pred}</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='explain'>📖 Explanation: {attack_explanation_map.get(pred)}</div>", unsafe_allow_html=True)

    show_risk(risk)

    st.markdown(f"<div class='reco'>📋 SOC Recommendation: {recommendation_map.get(pred)}</div>", unsafe_allow_html=True)


#MANUAL MODE
if mode == "Manual Analysis":
    
    st.markdown("<h2>🧪 Manual SOC Analysis</h2>",unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='label-protocol'>Protocol</div>", unsafe_allow_html=True)
        protocol = st.selectbox("", list(protocol_enc.classes_), key="protocol")

        st.markdown("<div class='label-service'>Service</div>", unsafe_allow_html=True)
        service = st.selectbox("", list(service_enc.classes_), key="service")

        st.markdown("<div class='label-flag'>Flag</div>", unsafe_allow_html=True)
        flag = st.selectbox("", list(flag_enc.classes_), key="flag")

        st.markdown("<div class='label-src'>Src Bytes</div>", unsafe_allow_html=True)
        src_bytes = st.number_input("", 0, value=100, key="src_bytes")

        st.markdown("<div class='label-count'>Count</div>", unsafe_allow_html=True)
        count = st.number_input("", 0, value=10, key="count")

    with col2:
        st.markdown("<div class='label-dst'>Dst Bytes</div>", unsafe_allow_html=True)
        dst_bytes = st.number_input("", 0, value=200, key="dst_bytes")

        st.markdown("<div class='label-srv'>Srv Count</div>", unsafe_allow_html=True)
        srv_count = st.number_input("", 0, value=5, key="srv_count")

        st.markdown("<div class='label-login'>Logged In</div>", unsafe_allow_html=True)
        logged_in = st.selectbox("", [0, 1], key="logged_in")

        st.markdown("<div class='label-serror'>Serror Rate</div>", unsafe_allow_html=True)
        serror_rate = st.slider("", 0.0, 1.0, 0.0, key="serror_rate")

        st.markdown("<div class='label-rerror'>Rerror Rate</div>", unsafe_allow_html=True)
        rerror_rate = st.slider("", 0.0, 1.0, 0.0, key="rerror_rate")
        

    if st.button("Analyze"):

        input_df = pd.DataFrame([[
            protocol_enc.transform([protocol])[0],
            service_enc.transform([service])[0],
            flag_enc.transform([flag])[0],
            src_bytes,
            dst_bytes,
            count,
            srv_count,
            logged_in,
            serror_rate,
            rerror_rate
        ]], columns=[
            "protocol_type","service","flag","src_bytes","dst_bytes",
            "count","srv_count","logged_in","serror_rate","rerror_rate"
        ])

        pred = model.predict(input_df)[0]
        risk = risk_map.get(pred, "Unknown")

        show_results(pred, risk)


#CSV MODE

elif mode == "Upload CSV Log File":

    st.markdown("<p class='upload-note'>📁 Max file size: 200MB per file</p>",
                 unsafe_allow_html=True)
    
    st.markdown("<h2> ⬆️Upload A CSV file</h2>",unsafe_allow_html=True)

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.dataframe(df.head())

        df["protocol_type"] = protocol_enc.transform(df["protocol_type"])
        df["service"] = service_enc.transform(df["service"])
        df["flag"] = flag_enc.transform(df["flag"])

        features = df[[
            "protocol_type","service","flag",
            "src_bytes","dst_bytes","count",
            "srv_count","logged_in",
            "serror_rate","rerror_rate"
        ]]

        preds = model.predict(features)
        df["prediction"] = preds
        df["risk"] = df["prediction"].map(risk_map)

        st.bar_chart(df["prediction"].value_counts())

        show_results(df["prediction"].iloc[0], df["risk"].iloc[0])


# PASTE MODE

elif mode == "Paste Log Entry":

    st.markdown("<h2>📥 Paste SOC Log Entry</h2>",unsafe_allow_html=True)

    log_text = st.text_area(
        "Paste log here",
        height=250,
        value="""protocol_type=tcp
service=http
flag=S0
src_bytes=0
dst_bytes=0
count=150
srv_count=120
logged_in=0
serror_rate=1.0
rerror_rate=0.0"""
    )

    if st.button("Analyze"):

        data = {}

        for line in log_text.split("\n"):
            if "=" in line:
                k, v = line.split("=", 1)
                data[k.strip()] = v.strip()

        input_df = pd.DataFrame([{
            "protocol_type": protocol_enc.transform([data["protocol_type"]])[0],
            "service": service_enc.transform([data["service"]])[0],
            "flag": flag_enc.transform([data["flag"]])[0],
            "src_bytes": float(data["src_bytes"]),
            "dst_bytes": float(data["dst_bytes"]),
            "count": float(data["count"]),
            "srv_count": float(data["srv_count"]),
            "logged_in": int(data["logged_in"]),
            "serror_rate": float(data["serror_rate"]),
            "rerror_rate": float(data["rerror_rate"])
        }])

        pred = model.predict(input_df)[0]
        risk = risk_map.get(pred, "Unknown")

        show_results(pred, risk)