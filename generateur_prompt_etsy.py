
import streamlit as st
import random

st.set_page_config(page_title="Générateur de Prompt Etsy IA", page_icon="🛒")
st.title("🧠 Générateur de Promptes Etsy avec IA")

st.markdown("Crée des idées de business prêtes à lancer sur Etsy en un clic. ✨")

niches = [
    "Développement personnel", "Mariage", "Éducation enfants", "Fitness & Yoga",
    "Décoration scandinave", "Spiritualité & ésotérisme", "Organisation & Productivité",
    "Photographie & Retouche", "Digital planner", "Business templates"
]

produits = [
    "Affiches murales minimalistes", "Templates Notion", "Planners interactifs",
    "Cartes de vœux digitales", "Worksheets éducatives", "eBooks thématiques",
    "Fonds d’écran esthétiques", "Checklists d'organisation", "Calendriers marketing", 
    "Kits de lancement pour freelance"
]

outils_ia = [
    "ChatGPT", "Midjourney", "Canva", "DALL·E", "Notion AI", "Leonardo AI", "Tome AI"
]

if st.button("🎯 Générer un prompt business Etsy"):
    niche = random.choice(niches)
    produit = random.choice(produits)
    outil = random.choice(outils_ia)

    prompt = f"Crée un(e) {produit.lower()} dans la niche '{niche}', à l'aide de {outil}. " \
             f"Optimise pour une clientèle Etsy à la recherche de produits tendance et esthétiques."

    st.success("💡 Prompt généré :")
    st.write(prompt)
