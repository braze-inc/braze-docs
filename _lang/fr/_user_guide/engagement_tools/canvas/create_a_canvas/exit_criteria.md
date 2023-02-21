---
nav_title: Critère de sortie 
article_title: Critère de sortie 
hidden: true
alias: /exit_criteria/
page_type: reference
description: "Cet article de référence décrit la fonctionnalité Critère de sortie pour Canvas Flow."
tool: Canvas
---

# Critère de sortie

Dans l’étape d’**Audience cible** du générateur de Canvas, vous pouvez définir un critère de sortie pour identifier les utilisateurs que vous voulez voir sortir de votre Canvas. Pour ajouter un critère de sortie, cliquez sur le menu déroulant pour sélectionner votre événement d’exception, puis cliquez sur **Ajouter un déclencheur**.

{% alert important %}
Les critères de sortie pour Canvas Flow sont actuellement en accès anticipé. Contactez votre CSM Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

En ajoutant des [événements d’exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) directement dans les règles d’entrée de votre Canvas, vous pouvez en faire sortir les utilisateurs dès que l’événement se produit à la fin de l’étape. Ces utilisateurs ne recevront plus aucune communication, ce qui entraînera une approche plus ciblée de l’envoi de messages Canvas avec votre audience. 

Par exemple, imaginons que vous désirez cibler les utilisateurs qui n’ont pas encore effectué d’achats. Cliquez sur le menu déroulant et sélectionnez **Effectue un achat** en tant qu’événement d’exception. Cliquez ensuite sur **Ajouter un déclencheur**. Lors du lancement de votre Canvas, votre audience exclura donc les utilisateurs qui n’ont pas encore réalisé d’achats avec les critères de sortie suivants.

![Paramétrage de critère de sortie avec « Effectue un achat quelconque » en tant qu’événement d’exception de sorte que, si un utilisateur effectue un achat, il sortira alors de ce Canvas.][1]

Des événements d’exception supplémentaires comprennent :
* Démarrer une session
* Réaliser un événement personnalisé ou un événement de conversion
* Ajouter une adresse e-mail
* Modifier la valeur d’attribut personnalisée
* Mettre à jour le statut de l’abonnement ou le statut du groupe d’abonnement
* Interagir avec une campagne
* Saisir un emplacement
* Déclencher une géofence
* Envoyer un message SMS entrant


[1]: {% image_buster /assets/img_archive/exit_criteria_example.png %} 
