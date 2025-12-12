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

> En ajoutant des événements d'exception directement aux règles d'entrée de votre Canvas, vos utilisateurs peuvent quitter votre Canvas dès que l'événement se produit à la fin de l'étape. Cela permet une approche plus ciblée de l'envoi de canvas à votre audience.

### Comment les utilisateurs quittent le site

Après l'exécution de l'événement de sortie, les utilisateurs sont sortis du canvas dès que l'étape du canvas dans laquelle ils se trouvent a été quittée. Par exemple, si un utilisateur se trouve dans une étape de temporisation pendant 30 jours et qu'il effectue l'événement de sortie le premier jour de l'étape de temporisation, l'utilisateur ne quittera pas le Canvas avant 29 jours.

Prenons un autre exemple d'utilisation de critères de sortie basés sur le temps. Un utilisateur saisit une étape de délai réglée sur 24 heures le 1er juillet à 12 heures. Dans ce délai, ils effectuent l'événement de sortie "Dernier achat effectué il y a moins d'une heure" à 3 heures du matin. Cet utilisateur sera évalué en fonction des critères de sortie le 2 juillet à 12 heures, c'est-à-dire à la fin de la durée de l'étape de retardement. Comme 21 heures se sont écoulées depuis leur achat le 1er juillet à 3 heures du matin, ils ne sortiront pas du canvas parce qu'ils n'ont pas effectué d'achat dans l'heure qui suit leur sortie de l'étape du canvas le 2 juillet. Cela a un impact sur le "Total des sorties par critère de sortie" dans votre analyse/analytique du canvas, qui n'est mis à jour qu'une fois qu'un utilisateur a complètement quitté le canvas.

## Définir des critères de sortie

À l'étape de la segmentation d'**audience** du générateur de canvas, vous pouvez définir des critères de sortie pour identifier les utilisateurs que vous souhaitez voir sortir de votre canvas. 

Les critères de sortie comprennent un événement d'exception, c'est-à-dire l'action spécifique qui peut amener les utilisateurs à quitter le Canvas.

Les critères de sortie mis en place pour réengager les utilisateurs qui ont consulté des produits mais ne les ont pas encore ajoutés à leur panier ou n'ont pas encore passé de commande.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Sélection des événements d'exception {#exception-events}

Lorsqu'un utilisateur exécute l'événement d'exception, il quitte le canvas. Notez que les événements d'exception ne déclenchent des sorties que lorsqu'un utilisateur se trouve dans le canvas et avance dans le parcours de l'utilisateur.

Imaginons que vous ayez mis en place une toile pour promouvoir un nouveau produit. Dans ce cas, l'achat du produit serait l'événement d'exception. Ainsi, après avoir effectué son achat, l'utilisateur ne recevra pas d'autres messages concernant un produit qu'il a déjà acheté. Les événements d'exception permettent à vos messages d'être pertinents et personnalisés.

D'autres événements d'exception sont prévus :

- Effectuer un achat
- Démarrer une session
- Exécution d'un événement personnalisé
- Exécution d'un événement de conversion
- Ajout d'une adresse e-mail
- Modification de la valeur d'un attribut personnalisé
- Mise à jour de l'état d'un abonnement
- Mise à jour du statut du groupe d'abonnement
- Interagir avec une campagne
- Saisir un emplacement/localisation
- Déclencher un géorepérage
- Envoi d'un message SMS entrant
- Envoi d'un message WhatsApp entrant
- Envoi d'un message entrant LINE
- Exécution d'un événement de mise à jour du panier
- Exécution d'un événement de fin de paiement
- Exécution d'un événement de démarrage de la caisse

#### Étapes planifiées

Si une étape du canvas est planifiée, l'utilisateur quittera immédiatement le canvas après l'événement d'exception. Supposons qu'un utilisateur entre dans un canvas dont la première étape comporte un délai d'une semaine et un événement d'exception. Si l'utilisateur effectue l'événement d'exception le jour 5, il sortira immédiatement après avoir effectué l'événement d'exception (le jour 5). 
 
#### Étapes déclenchées

Si une étape du canvas est déclenchée par un événement, le dernier envoi planifié mis en file d'attente à partir de ce déclencheur sera annulé, mais l'utilisateur restera à l'intérieur du canvas pendant la durée de la fenêtre. Cela signifie que l'événement déclencheur peut toujours être envoyé à l'utilisateur s'il effectue à nouveau l'événement déclencheur dans la fenêtre. Une fois la fenêtre passée, l'utilisateur quittera le Canvas.

### Utilisation de segments et de filtres

Vous pouvez également ajouter des segmentations et des filtres dans les critères de sortie. Cela signifie que les utilisateurs qui correspondent au segment et au filtre quitteront le Canvas et ne recevront plus d'envoi de messages. 

Par exemple, si la première étape d'un canvas est une étape de délai avec un délai de cinq jours, les critères de sortie s'appliqueront à la fin de cette étape. Ainsi, si un utilisateur final remplit les critères de sortie, il sortira au bout des cinq jours.

{% alert note %}
Les attributs de tableau ne sont pas actuellement pris en charge en tant que critères de sortie pour les événements d'exception.
{% endalert %}

### Avoir le même événement de sortie et de conversion

Lorsque l'événement de sortie et l'événement de conversion sont identiques, les deux événements de conversion et de sortie seront pris en compte. Par exemple, si un Canvas comporte une étape de temporisation et qu'un utilisateur effectue le critère de sortie pendant cette étape de temporisation, l'événement de sortie s'incrémentera dès que l'utilisateur quittera l'étape de temporisation. La conversion sera également incrémentée dès que l'événement sera journal des événements utilisateurs.

Les conversions sont suivies même après la fin du canvas, mais les sorties ne sont pas suivies une fois que l'utilisateur quitte le canvas. La fenêtre de conversion s'étend à trois jours au-delà de la durée maximale de la toile. Cela signifie que les conversions continueront d'être suivies après que les sorties cessent d'être suivies. 

La durée minimale d'une fenêtre de conversion est de cinq minutes. Fixez les fenêtres de conversion à cinq minutes pour vos événements de conversion afin de vous rapprocher le plus possible de la parité avec les événements de sortie. Nous vous recommandons également de définir la fenêtre de conversion de manière à ce qu'elle corresponde au moins au chemin le plus long dans le Canvas.

Prenons l'exemple suivant sur la manière dont les analyses/analytiques sont calculées :

1. Dix utilisateurs passent par le Canvas.
2. Trois utilisateurs effectuent l'événement de conversion en l'espace de cinq minutes (le nombre d'événements de sortie est de trois, et le nombre d'événements de conversion est de trois).
3. Cinq autres utilisateurs quittent le Canvas au bout de cinq minutes, mais effectuent l'événement de conversion au bout de deux jours (le nombre d'événements de sortie reste le même, mais l'événement de conversion passe à huit).
4. Les deux derniers utilisateurs quittent le Canvas après cinq minutes mais n'effectuent pas l'événement de conversion, ou l'effectuent après trois jours et cinq minutes (ils ne sont pas comptabilisés dans les indicateurs d'événements de sortie ou d'événements de conversion).

## Exemple

Disons que nous voulons cibler les utilisateurs qui n'ont pas encore effectué d'achats dans notre entreprise de fourniture de sacs à dos. Pour définir les critères de sortie, nous devrions.. :

1. Sélectionnez **Faire un achat** comme événement d'exception.
2. Sélectionnez **Ajouter un déclencheur**. 
3. Pour les **segments**, sélectionnez **Utilisé le dernier jour** afin que, lors du lancement de notre Canvas, l'audience exclue les utilisateurs qui ont effectué des achats.
4. Pour les **filtres**, sélectionnez **Comportement d'achat** > **Nombre d'achats** > **Produit acheté.**
5. Réglez le groupe interne sur `backpack-example exactly 1`. Cela signifie que les utilisateurs qui ont acheté notre produit de sac à dos quitteront le Canvas.

Les paramètres des critères de sortie avec "Effectue un achat" comme événement d'exception, de sorte que si un utilisateur effectue un achat, il quittera ce Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


