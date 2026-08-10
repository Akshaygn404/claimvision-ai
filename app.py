import streamlit as st
from ultralytics import YOLO
from PIL import Image
from nlp_extractor import extract_claim_info
from report_generator import generate_report
import tempfile


st.title(" ClaimVision AI — Phase 1 + Phase 2")

model = YOLO("runs/detect/claimvision_damage/weights/best.pt")


uploaded = st.file_uploader(
    "Upload a vehicle image",
    type=["jpg", "png", "jpeg"]
)

if uploaded:
    image = Image.open(uploaded)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

   
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp:

        image.save(tmp.name)

       
        results = model(tmp.name)

    plotted = results[0].plot()

    st.image(
        plotted,
        caption="Detected Damage",
        use_container_width=True
    )

    st.subheader("Detected Parts")

    detected_parts = []

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])

        part_name = model.names[cls_id]
        detected_parts.append(part_name)

        st.write(f"• **{part_name}** ({conf:.2f})")

st.subheader("Claim Description")

claim_text = st.text_area(
    "Describe what happened",
    placeholder="I hit a wall while reversing. The rear bumper is dented..."
)

if claim_text:
    info = extract_claim_info(claim_text)

    st.subheader("Extracted Claim Information")
    st.json(info)


    if uploaded:
        st.subheader("🔍 CV vs NLP Comparison")

        st.write("**Detected from image:**")
        st.write(detected_parts)

        st.write("**Mentioned in text:**")
        st.write(info["mentioned_parts"])

if claim_text and uploaded:
    cv_output = {
        "detected_parts": detected_parts
    }

    consistency_output = {
        "consistent": True
    }

    report = generate_report(
        cv_output,
        info,
        consistency_output
    )

    st.subheader("AI Claim Assessment Report")
    st.text(report)

    st.download_button(
        label="Download Report",
        data=report,
        file_name="claimvision_report.txt",
        mime="text/plain"
    )