import streamlit as st

# Seite konfigurieren (Dark Mode Look)
st.set_page_config(page_title="Raffanus Holding", page_icon="🚀")

# Header wie im Original
st.title("RAFFANUS HOLDING")
st.caption("VORSITZENDER: MISTERY_MAN | EXECUTIVE TERMINAL")

# CSS für den "Sci-Fi" Look (optional, macht es hübscher)
st.markdown("""
    <style>
    .main { background-color: #0b1622; }
    div[data-testid="stMetricValue"] { color: #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# Input Bereich
st.subheader("System Inputs")
col1, col2 = st.columns(2)

with col1:
    pp = st.number_input("PRODUCTION POWER (PP)", value=25.0)
    energy = st.number_input("MAX ENERGY (E-MAX)", value=70.0)

with col2:
    loyalty = st.number_input("FIDELITY LEVEL (1-20%)", value=5.0)
    tax_rate = st.number_input("SECTOR TAX RATE (%)", value=9.0)

# Berechnung (Deine Logik bleibt 1:1 gleich)
if st.button("GENERATE PAYROLL"):
    base_lohn = 0.11
    qpy_base = (pp / 2500) + (energy / 10000)
    fy_extra = qpy_base * (loyalty / 100)
    final_lohn = base_lohn + qpy_base + fy_extra
    
    # FSI Logik
    h_pay = tax_rate if tax_rate <= 18 else (tax_rate * 0.9 if tax_rate <= 25 else tax_rate * 0.7)

    # Output Bereich
    st.divider()
    st.subheader("Payroll Results")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Base Credit", f"{base_lohn:.4f}")
    c2.metric("Performance", f"{qpy_base:.4f}")
    c3.metric("Fidelity Bonus", f"{fy_extra:.4f}")

    st.success(f"TOTAL NET: {final_lohn:.4f} Credits")
    
    if tax_rate > 0:
        st.info(f"FSI SHIELD: {h_pay:.1f}% übernommen")