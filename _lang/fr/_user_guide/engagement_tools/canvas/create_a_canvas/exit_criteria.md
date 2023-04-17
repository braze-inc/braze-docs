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

> Dans l’étape d’**Audience cible** du générateur de Canvas, vous pouvez définir un critère de sortie pour identifier les utilisateurs que vous voulez voir sortir de votre Canvas. 

Pour ajouter un critère de sortie, cliquez sur le menu déroulant pour sélectionner votre événement d’exception, puis cliquez sur **Ajouter un déclencheur**.

En ajoutant des [événements d’exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) directement dans les règles d’entrée de votre Canvas, vous pouvez en faire sortir les utilisateurs dès que l’événement se produit à la fin de l’étape. Ces utilisateurs ne recevront plus aucune communication, ce qui entraînera une approche plus ciblée de l’envoi de messages Canvas avec votre audience.

Pour cibler les utilisateurs qui n’ont pas encore effectué d’achats, cliquez sur la liste déroulante pour sélectionner **Make Purchase (Effectue un achat)** comme événement d’exception. Cliquez ensuite sur **Ajouter un déclencheur**. Lors du lancement de votre Canvas, votre audience exclura donc les utilisateurs qui n’ont pas encore réalisé d’achats avec les critères de sortie suivants.

![Paramétrage de critère de sortie avec « Effectue un achat quelconque » en tant qu’événement d’exception de sorte que, si un utilisateur effectue un achat, il sortira alors de ce Canvas.][1]

Si la première étape d’un Canvas est une étape de Délai avec un délai de cinq jours, les critères de sortie s’appliqueront à la fin de cette étape. Ainsi, si un utilisateur répond aux critères de sortie, il sortira à la fin des cinq jours.

Des événements d’exception supplémentaires comprennent :
* Démarrer une session
* Effectuer un événement personnalisé ou un événement de conversion
* Ajouter une adresse e-mail
* Modifier la valeur d’attribut personnalisé
* Mettre à jour le statut d’abonnement ou le statut du groupe d’abonnement
* Interagir avec une campagne
* Saisir un emplacement
* Déclencher un geofence
* Envoyer un message SMS entrant
* Appartenance à un segment
* Ajout de filtres

[1]: {% image_buster /assets/img_archive/exit_criteria_example.png %} 
