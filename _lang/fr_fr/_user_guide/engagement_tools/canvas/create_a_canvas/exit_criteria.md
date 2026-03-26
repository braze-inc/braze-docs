---
nav_title: Critères de sortie
article_title: Critères de sortie 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Cet article de référence traite des critères de sortie et de la manière dont les utilisateurs peuvent quitter votre Canvas en fonction des critères sélectionnés."
tool: Canvas
---

# Critères de sortie

> En ajoutant des événements d'exception directement aux règles d'entrée de votre Canvas, vos utilisateurs peuvent quitter votre Canvas dès que l'événement se produit à la fin de l'étape. Ceci permet une approche plus ciblée de l'envoi de messages Canvas à votre audience.

### Comment les utilisateurs sortent

Après avoir effectué l'événement de sortie, les utilisateurs quittent le Canvas dès que l'étape dans laquelle ils se trouvent est terminée. Par exemple, si un utilisateur se trouve dans une étape de temporisation de 30 jours et qu'il effectue l'événement de sortie le premier jour de cette étape, il ne quittera pas le Canvas avant 29 jours supplémentaires.

Prenons un autre exemple avec des critères de sortie basés sur le temps. Un utilisateur entre dans une étape de temporisation réglée sur 24 heures le 1er juillet à minuit. Pendant cette période, il effectue l'événement de sortie « Dernier achat effectué il y a moins d'une heure » à 3 heures du matin. Cet utilisateur sera évalué selon les critères de sortie le 2 juillet à minuit, c'est-à-dire à la fin de la durée de l'étape de temporisation. Comme 21 heures se sont écoulées depuis son achat du 1er juillet à 3 heures du matin, il ne sortira pas du Canvas car il n'a pas effectué d'achat dans l'heure précédant la fin de l'étape de temporisation le 2 juillet. Cela a un impact sur le « Total des sorties par critère de sortie » dans l'analytique de votre Canvas, qui n'est mis à jour qu'une fois qu'un utilisateur a complètement quitté le Canvas.

## Définir des critères de sortie

À l'étape **Audience cible** du générateur de Canvas, vous pouvez définir des critères de sortie pour identifier les utilisateurs que vous souhaitez voir sortir de votre Canvas. 

Les critères de sortie comprennent un événement d'exception, c'est-à-dire l'action spécifique qui peut amener les utilisateurs à quitter le Canvas.

![Les critères de sortie mis en place pour réengager les utilisateurs qui ont parcouru des produits mais ne les ont pas encore ajoutés à leur panier ou passé une commande.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Sélection des événements d'exception {#exception-events}

Lorsqu'un utilisateur effectue l'événement d'exception, il quitte le Canvas. Notez que les événements d'exception ne déclenchent des sorties que lorsqu'un utilisateur se trouve dans le Canvas et progresse dans son parcours.

Imaginons que vous ayez un Canvas configuré pour promouvoir un nouveau produit. Dans ce cas, l'achat du produit serait l'événement d'exception. Ainsi, après avoir effectué son achat, l'utilisateur ne recevra plus de messages concernant un produit qu'il a déjà acheté. Les événements d'exception permettent de garder vos messages pertinents et personnalisés.

Voici d'autres événements d'exception disponibles :

- Effectuer un achat
- Démarrer une session
- Réaliser un événement personnalisé
- Effectuer un événement de conversion
- Ajouter une adresse e-mail
- Modifier la valeur d'un attribut personnalisé
- Mettre à jour un statut d'abonnement
- Mettre à jour le statut d'un groupe d'abonnement
- Interagir avec une campagne
- Entrer dans un emplacement
- Déclencher un géorepérage
- Envoyer un message SMS entrant
- Envoyer un message WhatsApp entrant
- Envoyer un message LINE entrant
- Effectuer un événement de mise à jour du panier
- Effectuer un événement de finalisation de commande
- Effectuer un événement de début de paiement

#### Étapes planifiées

Si une étape du Canvas est planifiée, l'utilisateur quittera immédiatement le Canvas après l'événement d'exception. Supposons qu'un utilisateur entre dans un Canvas dont la première étape comporte un délai d'une semaine et un événement d'exception. Si l'utilisateur effectue l'événement d'exception le jour 5, il sortira immédiatement après avoir effectué l'événement d'exception (le jour 5). 
 
#### Étapes déclenchées

Si une étape du Canvas est déclenchée par un événement, le dernier envoi planifié mis en file d'attente à partir de ce déclencheur sera annulé, mais l'utilisateur restera dans le Canvas pendant la durée de la fenêtre. Cela signifie que l'utilisateur peut toujours recevoir l'étape s'il effectue à nouveau l'événement déclencheur dans la fenêtre. Une fois la fenêtre écoulée, l'utilisateur quittera le Canvas.

### Utilisation de segments et de filtres

Vous pouvez également ajouter des segments et des filtres dans les critères de sortie. Cela signifie que les utilisateurs qui correspondent au segment et au filtre quitteront le Canvas et ne recevront plus aucun message. 

Par exemple, si la première étape d'un Canvas est une étape de temporisation avec un délai de cinq jours, les critères de sortie s'appliqueront à la fin de cette étape. Ainsi, si un utilisateur répond aux critères de sortie, il sortira à la fin des cinq jours.

{% alert note %}
Les attributs de type tableau ne sont pas actuellement pris en charge en tant que critères de sortie pour les événements d'exception.
{% endalert %}

### Avoir le même événement de sortie et de conversion

Lorsque l'événement de sortie et l'événement de conversion sont identiques, les deux sont pris en compte. Par exemple, si un Canvas comporte une étape de temporisation et qu'un utilisateur remplit le critère de sortie pendant cette étape, l'événement de sortie sera incrémenté dès que l'utilisateur quittera l'étape de temporisation. La conversion sera également incrémentée dès que l'événement sera enregistré sur le profil utilisateur.

Les conversions sont suivies même après la fin du Canvas, mais les sorties ne sont plus suivies une fois que l'utilisateur quitte le Canvas. La fenêtre de conversion s'étend à trois jours au-delà de la durée maximale du Canvas. Cela signifie que les conversions continueront d'être suivies après que le suivi des sorties aura cessé. 

La durée minimale d'une fenêtre de conversion est de cinq minutes. Réglez les fenêtres de conversion à cinq minutes pour vos événements de conversion afin de vous rapprocher le plus possible de la parité avec les événements de sortie. Nous vous recommandons également de définir la fenêtre de conversion de manière à ce qu'elle corresponde au moins au chemin le plus long du Canvas.

Prenons l'exemple suivant pour illustrer le calcul des analyses :

1. Dix utilisateurs passent par le Canvas.
2. Trois utilisateurs effectuent l'événement de conversion en l'espace de cinq minutes (le nombre d'événements de sortie est de trois, et le nombre d'événements de conversion est de trois).
3. Cinq autres utilisateurs quittent le Canvas au bout de cinq minutes, mais effectuent l'événement de conversion au bout de deux jours (le nombre d'événements de sortie reste le même, mais le nombre d'événements de conversion passe à huit).
4. Les deux derniers utilisateurs quittent le Canvas après cinq minutes mais n'effectuent pas l'événement de conversion, ou l'effectuent après trois jours et cinq minutes (ils ne sont comptabilisés ni dans les indicateurs d'événements de sortie, ni dans ceux d'événements de conversion).

## Exemple

Imaginons que nous voulions cibler les utilisateurs qui n'ont pas encore effectué d'achats dans notre entreprise de fourniture de sacs à dos. Pour définir les critères de sortie, nous devrions :

1. Sélectionner **Effectuer un achat** comme événement d'exception.
2. Sélectionner **Ajouter un déclencheur**. 
3. Pour les **Segments**, sélectionner **Utilisé le dernier jour** afin que, lors du lancement de notre Canvas, l'audience exclue les utilisateurs qui ont effectué des achats.
4. Pour les **Filtres**, sélectionner **Comportement d'achat** > **Nombre d'achats** > **Produit acheté**.
5. Régler le groupe de filtres sur `backpack-example exactly 1`. Cela signifie que les utilisateurs qui ont acheté notre produit de sac à dos quitteront le Canvas.

![Paramètres des critères de sortie avec « Effectue un achat » comme événement d'exception, de sorte que si un utilisateur effectue un achat, il quittera ce Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}

{% alert tip %}
Pour définir des critères de sortie qui comparent les propriétés d'événement aux propriétés d'entrée du Canvas (par exemple, sortir uniquement lorsqu'un utilisateur achète l'article spécifique qu'il a abandonné), consultez [Faire correspondre les critères de sortie aux événements d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/matching_entry_and_exit_criteria/).
{% endalert %}