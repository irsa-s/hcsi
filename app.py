import streamlit as st
from utils import (
    apply_global_css,
    load_case_data,
    load_manpower_data,
    load_medical_claim_data,
    load_overtime_data,
    load_recruitment_data,
    load_vehicle_data,
)

st.set_page_config(
    page_title="HC Executive Reporting System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_global_css()

# Preload all domain datasets into session state
if "df_raw" not in st.session_state:
  st.session_state["df_raw"] = load_manpower_data()

if "df_fptk" not in st.session_state or "df_candidate" not in st.session_state:
  st.session_state["df_fptk"], st.session_state["df_candidate"] = (
      load_recruitment_data()
  )

if (
    "veh_df" not in st.session_state
    or "upc_df" not in st.session_state
    or "drv_df" not in st.session_state
):
  (
      st.session_state["veh_df"],
      st.session_state["upc_df"],
      st.session_state["drv_df"],
  ) = load_vehicle_data()

if "case_df" not in st.session_state:
  st.session_state["case_df"] = load_case_data()

if "ot_df" not in st.session_state:
  st.session_state["ot_df"] = load_overtime_data()

if "claim_df" not in st.session_state:
  st.session_state["claim_df"] = load_medical_claim_data()

# Refresh Data Button in Sidebar
st.sidebar.markdown("---")
if st.sidebar.button("🔄 Refresh Data", use_container_width=True):
  st.cache_data.clear()
  st.session_state["df_raw"] = load_manpower_data()
  st.session_state["df_fptk"], st.session_state["df_candidate"] = (
      load_recruitment_data()
  )
  (
      st.session_state["veh_df"],
      st.session_state["upc_df"],
      st.session_state["drv_df"],
  ) = load_vehicle_data()
  st.session_state["case_df"] = load_case_data()
  st.session_state["ot_df"] = load_overtime_data()
  st.session_state["claim_df"] = load_medical_claim_data()
  st.sidebar.success("Data reloaded from Excel!")
  st.rerun()

# Defined Grouped Navigation Hierarchy
# Add inside pages dictionary in app.py

pages = {
    "Overview": [
        st.Page("pages/1_Demographic.py", title="Demographic", icon="👥"),
    ],
    "HCBP": [
        st.Page("pages/2_Turnover.py", title="Turnover", icon="📈"),
        st.Page("pages/3_Join_Resign.py", title="Join Resign", icon="🚪"),
        st.Page("pages/4_Fulfillment.py", title="Fulfillment", icon="📋"),
        st.Page("pages/5_Recruitment_SLA.py", title="Recruitment SLA", icon="⏱️"),
        st.Page("pages/6_Driver_Need.py", title="Driver Need", icon="🚚"),
    ],
    "IRER": [
        st.Page(
            "pages/7_Case_Category_Trend.py",
            title="Case Category Trend",
            icon="⚖️",
        ),
        st.Page(
            "pages/8_IRER_Driver_Ratio.py", title="Driver Case Ratio", icon="📊"
        ),
    ],
    "HCSS": [
        st.Page("pages/9_Overtime.py", title="Overtime Analytics", icon="⏰"),
        st.Page(
            "pages/10_Medical_Claim.py",
            title="Medical Claim Analytics",
            icon="🏥",
        ),
    ],
    "TOD": [
        st.Page(
            "pages/11_TOD_Plan_Vs_Actual.py",
            title="Plan vs Actual Trend",
            icon="🎯",
        ),
        st.Page(
            "pages/12_TOD_Training_Metrics.py",
            title="Training Metrics",
            icon="🎓",
        ),
    ],
}

pg = st.navigation(pages)
pg.run()