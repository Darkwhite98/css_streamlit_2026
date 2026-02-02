import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Mr. Junior Netshipise"
field = "MSc Medicine Physiology"
institution = "Sefako Makgatho Health Sciences University"

# ===============================
# Personal Summary Section
# ===============================

st.header("Personal Summary")

st.markdown(
    """
    I am a life sciences graduate with a strong academic foundation in **physiology, molecular biology,
    zoology, and botany**, supported by hands-on exposure to laboratory-based research and scientific
    data handling. My training has equipped me with the ability to interpret biological data,
    follow structured research protocols, and maintain high standards of accuracy and documentation.

    I have experience working within **research and clinical environments**, where attention to detail,
    data integrity, and regulatory awareness are essential. Through academic projects, laboratory work,
    and participation in scientific forums, I have developed a growing interest in biomedical research,
    clinical studies, and translational science.

    This dashboard serves as a personal showcase of how I organize, explore, and interpret life sciences
    data—reflecting both my technical skills and my commitment to continuous learning within the
    biological and health sciences.
    """
)

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Physiology Data
physiology_data = pd.DataFrame({
    "Parameter": [
        "Resting Heart Rate",
        "Blood Glucose Level",
        "Systolic Blood Pressure",
        "Oxygen Saturation",
        "Respiratory Rate"
    ],
    "Measured Value": [72, 5.4, 118, 98, 16],
    "Unit": ["bpm", "mmol/L", "mmHg", "%", "breaths/min"],
    "Measurement Date": pd.date_range(start="2024-01-01", periods=5),
})

# Molecular Biology Data
molecular_biology_data = pd.DataFrame({
    "Assay": [
        "DNA Concentration",
        "RNA Purity (A260/280)",
        "Protein Expression Level",
        "ELISA Cytokine Level",
        "PCR Ct Value"
    ],
    "Result": [85.3, 2.01, 1.8, 340, 22.5],
    "Unit": ["ng/µL", "Ratio", "Fold Change", "pg/mL", "Ct"],
    "Analysis Date": pd.date_range(start="2024-01-01", periods=5),
})

# Zoology Data
zoology_data = pd.DataFrame({
    "Species": [
        "Xenopus laevis",
        "Mus musculus",
        "Rattus norvegicus",
        "Panthera leo",
        "Loxodonta africana"
    ],
    "Observation Type": [
        "Developmental Study",
        "Metabolic Assessment",
        "Behavioural Analysis",
        "Population Survey",
        "Habitat Monitoring"
    ],
    "Sample Size": [30, 25, 20, 15, 10],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

# Botany Data
botany_data = pd.DataFrame({
    "Plant Species": [
        "Zea mays",
        "Arabidopsis thaliana",
        "Solanum lycopersicum",
        "Vigna unguiculata",
        "Helianthus annuus"
    ],
    "Study Focus": [
        "Growth Rate Analysis",
        "Gene Expression Study",
        "Stress Response",
        "Nitrogen Fixation",
        "Photosynthetic Efficiency"
    ],
    "Measured Value": [45.2, 2.4, 38.7, 76.1, 89.3],
    "Unit": ["cm", "Fold Change", "%", "%", "%"],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# -------------------------------
# Dataset Selection
# -------------------------------

st.subheader("Life Sciences Data Viewer")

data_option = st.selectbox(
    "Choose a life sciences dataset to explore",
    [
        "Physiology",
        "Molecular Biology",
        "Zoology",
        "Botany"
    ]
)

# -------------------------------
# Physiology View
# -------------------------------

if data_option == "Physiology":
    st.write("### Physiology Measurements")
    st.dataframe(physiology_data)

    value_filter = st.slider(
        "Filter by Measured Value",
        float(physiology_data["Measured Value"].min()),
        float(physiology_data["Measured Value"].max()),
        (
            float(physiology_data["Measured Value"].min()),
            float(physiology_data["Measured Value"].max())
        )
    )

    filtered_physiology = physiology_data[
        physiology_data["Measured Value"].between(value_filter[0], value_filter[1])
    ]

    st.write(f"Filtered Results for Value Range {value_filter}:")
    st.dataframe(filtered_physiology)

# -------------------------------
# Molecular Biology View
# -------------------------------

elif data_option == "Molecular Biology":
    st.write("### Molecular Biology Assay Results")
    st.dataframe(molecular_biology_data)

    result_filter = st.slider(
        "Filter by Result Value",
        float(molecular_biology_data["Result"].min()),
        float(molecular_biology_data["Result"].max()),
        (
            float(molecular_biology_data["Result"].min()),
            float(molecular_biology_data["Result"].max())
        )
    )

    filtered_molecular = molecular_biology_data[
        molecular_biology_data["Result"].between(result_filter[0], result_filter[1])
    ]

    st.write(f"Filtered Results for Result Range {result_filter}:")
    st.dataframe(filtered_molecular)

# -------------------------------
# Zoology View
# -------------------------------

elif data_option == "Zoology":
    st.write("### Zoological Observations")
    st.dataframe(zoology_data)

    sample_filter = st.slider(
        "Filter by Sample Size",
        int(zoology_data["Sample Size"].min()),
        int(zoology_data["Sample Size"].max()),
        (
            int(zoology_data["Sample Size"].min()),
            int(zoology_data["Sample Size"].max())
        )
    )

    filtered_zoology = zoology_data[
        zoology_data["Sample Size"].between(sample_filter[0], sample_filter[1])
    ]

    st.write(f"Filtered Results for Sample Size {sample_filter}:")
    st.dataframe(filtered_zoology)

# -------------------------------
# Botany View
# -------------------------------

elif data_option == "Botany":
    st.write("### Botanical Study Data")
    st.dataframe(botany_data)

    value_filter = st.slider(
        "Filter by Measured Value",
        float(botany_data["Measured Value"].min()),
        float(botany_data["Measured Value"].max()),
        (
            float(botany_data["Measured Value"].min()),
            float(botany_data["Measured Value"].max())
        )
    )

    filtered_botany = botany_data[
        botany_data["Measured Value"].between(value_filter[0], value_filter[1])
    ]

    st.write(f"Filtered Results for Value Range {value_filter}:")
    st.dataframe(filtered_botany)

# Add a contact section
st.header("0626880751")
email = "201707104@swave.smu.ac.za"
st.write("You can reach me at 201707104@swave.smu.ac.za.")