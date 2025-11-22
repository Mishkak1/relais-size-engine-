import streamlit as st

st.set_page_config(page_title="Le Relais Size Engine")

st.title("Le Relais Size Engine")
st.write("Guide de tailles basé sur mesures réelles et profil client.")

# Compare values
def compare(a, b):
    diff = abs(a - b)
    if diff <= 2:
        return "OK"
    elif diff <= 5:
        return "DIFF"
    else:
        return "NO"

# 1) Profil de l'article
st.header("1. Profil de l'article")

genre = st.radio("Genre :", ["homme", "femme"])

if genre == "homme":
    categories = ["tshirt", "sweat", "jacket", "chemise", "jean"]
else:
    categories = ["haut", "robe", "jupe", "sweat", "jacket", "jean"]

categorie = st.selectbox("Catégorie :", categories)

article = {}

st.subheader("Mesures du vêtement (cm)")

if categorie in ["tshirt", "sweat", "jacket", "chemise", "haut"]:
    article["epaules"] = st.number_input("Épaules (cm)", 0.0)
    article["poitrine"] = st.number_input("Poitrine (cm)", 0.0)
    article["longueur"] = st.number_input("Longueur (cm)", 0.0)

elif categorie == "robe":
    article["poitrine"] = st.number_input("Poitrine (cm)", 0.0)
    article["taille"] = st.number_input("Taille (cm)", 0.0)
    article["longueur"] = st.number_input("Longueur robe (cm)", 0.0)

elif categorie == "jupe":
    article["taille"] = st.number_input("Tour de taille (cm)", 0.0)
    article["hanches"] = st.number_input("Hanches (cm)", 0.0)
    article["longueur"] = st.number_input("Longueur jupe (cm)", 0.0)

elif categorie == "jean":
    article["taille"] = st.number_input("Tour de taille (cm)", 0.0)
    article["hanches"] = st.number_input("Hanches (cm)", 0.0)
    article["longueur"] = st.number_input("Longueur jambe (cm)", 0.0)

# 2) Profil client
st.header("2. Profil client")

profil = {}

if categorie in ["tshirt", "sweat", "jacket", "chemise", "haut"]:
    profil["epaules"] = st.number_input("Épaules client (cm)", 0.0)
    profil["poitrine"] = st.number_input("Poitrine client (cm)", 0.0)
    profil["longueur"] = st.number_input("Longueur client (cm)", 0.0)

elif categorie == "robe":
    profil["poitrine"] = st.number_input("Poitrine client (cm)", 0.0)
    profil["taille"] = st.number_input("Taille client (cm)", 0.0)
    profil["longueur"] = st.number_input("Longueur robe client (cm)", 0.0)

elif categorie == "jupe":
    profil["taille"] = st.number_input("Tour de taille client (cm)", 0.0)
    profil["hanches"] = st.number_input("Hanches client (cm)", 0.0)
    profil["longueur"] = st.number_input("Longueur jupe client (cm)", 0.0)

elif categorie == "jean":
    profil["taille"] = st.number_input("Tour de taille client (cm)", 0.0)
    profil["hanches"] = st.number_input("Hanches client (cm)", 0.0)
    profil["longueur"] = st.number_input("Longueur jambe client (cm)", 0.0)

# 3) Recommandation
st.header("3. Recommandation")

def recommander(article, profil, categorie):
    verdict = ""
    tech = ""
    style = ""

    # HAUTS
    if categorie in ["tshirt", "sweat", "jacket", "chemise", "haut"]:
        ep = compare(article["epaules"], profil["epaules"])
        po = compare(article["poitrine"], profil["poitrine"])
        lo = compare(article["longueur"], profil["longueur"])

        if ep == "OK" and po == "OK":
            verdict = "OK pour vous"
        elif ep == "NO" or po == "NO":
            verdict = "Pas recommandé"
        else:
            verdict = "Coupe différente"

        tech = f"Épaules: {ep}, Poitrine: {po}, Longueur: {lo}"

        if categorie == "sweat":
            style = "Tombé relax et confortable."
        else:
            style = "Coupe classique."

    # ROBE
    elif categorie == "robe":
        po = compare(article["poitrine"], profil["poitrine"])
        ta = compare(article["taille"], profil["taille"])
        lo = compare(article["longueur"], profil["longueur"])

        if po == "OK" and ta == "OK":
            verdict = "OK pour vous"
        elif po == "NO" or ta == "NO":
            verdict = "Pas recommandé"
        else:
            verdict = "Coupe différente"

        tech = f"Poitrine: {po}, Taille: {ta}, Longueur: {lo}"
        style = "Silhouette élégante."

    # JUPE
    elif categorie == "jupe":
        ta = compare(article["taille"], profil["taille"])
        ha = compare(article["hanches"], profil["hanches"])
        lo = compare(article["longueur"], profil["longueur"])

        if ta == "OK" and ha == "OK":
            verdict = "OK pour vous"
        elif ta == "NO" or ha == "NO":
            verdict = "Pas recommandé"
        else:
            verdict = "Coupe différente"

        tech = f"Taille: {ta}, Hanches: {ha}, Longueur: {lo}"
        style = "Tombé féminin."

    # JEAN
    elif categorie == "jean":
        ta = compare(article["taille"], profil["taille"])
        ha = compare(article["hanches"], profil["hanches"])
        lo = compare(article["longueur"], profil["longueur"])

        if ta == "OK" and ha == "OK":
            verdict = "OK pour vous"
        elif ta == "NO" or ha == "NO":
            verdict = "Pas recommandé"
        else:
            verdict = "Coupe différente"

        tech = f"Taille: {ta}, Hanches: {ha}, Longueur: {lo}"
        style = "Coupe unisexe, silhouette propre."

    return verdict, tech, style

if st.button("Lancer la recommandation"):
    v, t, s = recommander(article, profil, categorie)
    st.subheader("Verdict")
    st.write(v)
    st.subheader("Technique")
    st.write(t)
    st.subheader("Style")
    st.write(s)