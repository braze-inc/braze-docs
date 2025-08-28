---
nav_title: Critère de sortie 
article_title: Critère de sortie 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Cet article de référence traite des critères de sortie et de la manière dont les utilisateurs peuvent quitter votre Canvas en fonction des critères sélectionnés."
tool: Canvas
---

# Critère de sortie

> En ajoutant des événements d'exception directement aux règles d'entrée de votre Canvas, vos utilisateurs peuvent quitter votre Canvas dès que l'événement se produit à la fin de l'étape. Ceci permet une approche plus ciblée de l'envoi de messages Canvas à votre audience.

## Définir des critères de sortie

À l'étape **Audience cible** du générateur de canvas, vous pouvez définir des critères de sortie pour identifier les utilisateurs que vous souhaitez voir sortir de votre canvas. 

Les critères de sortie comprennent un événement d'exception, c'est-à-dire l'action spécifique qui peut amener les utilisateurs à quitter le Canvas.

![Les critères de sortie mis en place pour réengager les utilisateurs qui ont consulté des produits mais ne les ont pas encore ajoutés à leur panier ou n'ont pas encore passé de commande.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Sélection des événements d'exception {#exception-events}

Lorsqu'un utilisateur exécute l'événement d'exception, il quitte le canvas. Notez que les événements d'exception ne déclenchent des sorties que lorsqu'un utilisateur se trouve dans le canvas et avance dans le parcours de l'utilisateur.

Imaginons que vous ayez mis en place une toile pour promouvoir un nouveau produit. Dans ce cas, l'achat du produit serait l'événement d'exception. Ainsi, après avoir effectué son achat, l'utilisateur ne recevra pas d'autres messages concernant un produit qu'il a déjà acheté. Les événements d'exception permettent à vos messages d'être pertinents et personnalisés.

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

### Utilisation de segments et de filtres

Vous pouvez également ajouter des segmentations et des filtres dans les critères de sortie. Cela signifie que les utilisateurs qui correspondent au segment ou au filtre quitteront le canvas et ne recevront plus d'envoi de messages. 

Par exemple, si la première étape d'un canvas est une étape de délai avec un délai de cinq jours, les critères de sortie s'appliqueront à la fin de cette étape. Ainsi, si un utilisateur répond aux critères de sortie, il sortira à la fin des cinq jours.

{% alert note %}
Les attributs de tableau ne sont pas actuellement pris en charge en tant que critères de sortie pour les événements d'exception.
{% endalert %}

## Exemple

Disons que nous voulons cibler les utilisateurs qui n'ont pas encore effectué d'achats dans notre entreprise de fourniture de sacs à dos. Pour définir les critères de sortie, nous devrions :

1. Sélectionnez **Faire un achat** comme événement d'exception.
2. Sélectionnez **Ajouter un déclencheur**. 
3. Pour les **segments**, sélectionnez **Utilisé le dernier jour** afin que, lors du lancement de notre Canvas, l'audience exclue les utilisateurs qui ont effectué des achats.
4. Pour les **filtres**, sélectionnez **Comportement d'achat** > **Nombre d'achats** > **Produit acheté.**
5. Réglez le groupe interne sur `backpack-example exactly 1`. Cela signifie que les utilisateurs qui ont acheté notre produit de sac à dos quitteront le Canvas.

![Paramètres des critères de sortie avec "Effectue un achat" comme événement d'exception, de sorte que si un utilisateur effectue un achat, il quittera ce Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


