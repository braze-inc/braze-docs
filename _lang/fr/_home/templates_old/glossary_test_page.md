---
page_order: 2

nav_title: Glossaire
layout: glossary_page
glossary_top_header: "Modèle de glossaire"
glossary_top_text: "Ceci est un test de page de glossaire."

#Required
description: "Il s’agit de la description Google Search. Les phrases de plus de 160 caractères seront tronquées… soyez concis !"
page_type: glossary
#À utiliser, si applicable

tool:
  - Tableau de bord
  - Docs
  - Canvas
  - Campagnes
  - Segments
  - Modèles
  - Médias
  - Localisation
  - Currents
  - Rapports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - cartes de contenu
  - E-mail
  - Fil d’actualité
  - Messages in-app
  - Notification push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: supprimer le noindex et l’alerte de ce modèle

glossary_tag_name: Balises
glossary_filter_text: "Sélectionnez des balises pour affiner les résultats du glossaire :"

# canal à icône/fa ou mappage d’image
glossary_tags:
  - name: Balise 1
  - name: Balise 2
  - name: Balise 3

glossaries:
  - name: Terme 1
    image: /docs/assets/img_archive/weeklyreport.png
    description: Définition du terme 1.
    calculation: Calcul / Du terme 1
    tags:
      - Tous
  - name: Terme 2
    description: Définition du terme 2.
    calculation: (Nombre de termes) / (Termes uniques)
    tags:
      - Balise 1
  - name: Terme 3
    description: Définition du terme 3.
    calculation: Total
    tags:
      - Balise 2
  - name: Terme 4
    description: Définition du terme 4.
    calculation: Total
    tags:
      - Balise 1
      - Balise 3
---
