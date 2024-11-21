---
nav_title: Critère de sortie 
article_title: Critère de sortie 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Cet article de référence décrit la fonctionnalité Critère de sortie pour Canvas Flow."
tool: Canvas
---

# Critère de sortie

> En ajoutant des [événements d'exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) directement aux règles d'entrée de votre Canvas, vos utilisateurs peuvent quitter votre Canvas dès que l'événement se produit à la fin de l'étape. Ceci permet une approche plus ciblée de l'envoi de messages Canvas à votre audience.

À l'étape **Audience cible** du générateur de canvas, vous pouvez définir des critères de sortie pour identifier les utilisateurs que vous souhaitez voir sortir de votre canvas. Ajoutez votre événement d'exception, puis sélectionnez **Ajouter un déclencheur**. 

Vous pouvez également inclure des segments et des filtres dans les critères de sortie, ce qui signifie que les utilisateurs qui correspondent au segment ou au filtre quitteront le Canvas et ne recevront plus d'envoi de messages. Si la première étape d’un Canvas est une étape de Délai avec un délai de cinq jours, les critères de sortie s’appliqueront à la fin de cette étape. Ainsi, si un utilisateur répond aux critères de sortie, il sortira à la fin des cinq jours.

{% alert note %}
Les attributs de tableau ne sont pas actuellement pris en charge en tant que critères de sortie pour les événements d'exception.
{% endalert %}

## Événements d'exception

Des événements d’exception supplémentaires comprennent :
- Faire un achat
- Démarrer une session
- Réalisation d'un événement personnalisé
- Exécution d'un événement de conversion
- Ajouter une adresse e-mail
- Changer une valeur d'attribut personnalisé
- Mise à jour du statut d'abonnement
- Mise à jour du statut d'un groupe d'abonnement
- Interagir avec une campagne
- Saisir une localisation
- Déclencher un géorepérage
- Envoyer un message SMS entrant
- Envoi d'un message entrant WhatsApp
- Envoi d'un message entrant LINE
- Exécution d'un événement de mise à jour du panier
- Exécution d'un événement de fin de paiement
- Exécution d'un événement de démarrage de la caisse

## Cas d’utilisation

Imaginons que vous souhaitiez cibler les utilisateurs qui n'ont pas encore effectué d'achats dans votre entreprise. Tout d'abord, sélectionnez **Faire un achat** comme événement d'exception. Sélectionnez ensuite **Ajouter un déclencheur**. Lors du lancement de votre Canvas, votre audience exclura les utilisateurs ayant effectué des achats grâce aux paramètres de **critères de sortie** suivants. 

Dans l'exemple suivant, ces critères de sortie sont également appliqués au segment « Utilisé au cours de la dernière journée » pour tout utilisateur ayant effectué exactement un achat.

![Configuration de critère de sortie avec « Effectue un achat quelconque » en tant qu’événement d’exception de sorte que, si un utilisateur effectue un achat, il sortira alors de ce Canvas.][1]

[1]: {% image_buster /assets/img_archive/exit_criteria_example.png %} 
