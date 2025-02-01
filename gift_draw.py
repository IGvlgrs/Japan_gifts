import streamlit as st
import random
import time
import pandas as pd

# Initialiser l'état des numéros disponibles si ce n'est pas déjà fait
if 'remaining_numbers' not in st.session_state:
    st.session_state.remaining_numbers = list(range(1, 36))
if 'drawn_results' not in st.session_state:
    st.session_state.drawn_results = []

st.title("🎮🎁 Lucky Japan Gift Draw 🎁🎮")
st.markdown("### Tourne la roue et découvre ton numéro de cadeau !")

# Entrée du prénom
ame = st.text_input("Entre ton prénom pour participer :", "")

def spin_wheel():
    if not st.session_state.remaining_numbers:
        st.warning("Tous les cadeaux ont été attribués !")
        return
    if name.strip() == "":
        st.warning("Merci d'entrer ton prénom avant de tourner la roue !")
        return
    
    st.session_state.spin_result = random.choice(st.session_state.remaining_numbers)
    st.session_state.remaining_numbers.remove(st.session_state.spin_result)
    st.session_state.drawn_results.append((name, st.session_state.spin_result))
    
    st.success(f"Bravo {name} ! Ton numéro de cadeau est : {st.session_state.spin_result}")
    
    time.sleep(1)

display_wheel = st.button("🎡 Tourner la roue ! 🎡", on_click=spin_wheel)

st.markdown("## Numéros restants :")
st.write(sorted(st.session_state.remaining_numbers))

st.markdown("## Résultats des tirages :")
results_df = pd.DataFrame(st.session_state.drawn_results, columns=["Prénom", "Numéro de Cadeau"])
st.dataframe(results_df)
