---
nav_title: Créer des notifications enrichies
article_title: "Création de notifications push riches pour Android"
page_order: 3
page_layout: tutorial
description: "Ce tutoriel explique comment implémenter des notifications Android Rich pour vos campagnes Braze."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Créer des notifications push riches pour Android

> Les notifications enrichies permettent d’obtenir plus de personnalisation dans vos notifications push en ajoutant du contenu supplémentaire en plus du texte seul. Depuis quelque temps, les notifications Android incluent des images dans les notifications push, appelées "image de notification étendue".

## Conditions préalables

Avant de créer une notification push riche pour Android, veuillez noter les détails suivants :

- Les images des notifications étendues Android doivent respecter un rapport de 2:1, mais ne sont soumises à aucune restriction de taille.
- Android permet également de définir une image séparée pour la vue de notification standard. Voici les dimensions recommandées pour les images : 
  - **Petites :** 512x256
  - **Intermédiaires :** 1024x512 
  - **Grandes :** 2048x1024
- Actuellement, les notifications enrichies Android ne permettent d'utiliser que des images statiques, y compris les formats d'image JPEG et PNG. Le format GIF et les autres formats d'image ne sont pas encore pris en charge.
- L'ajout de boutons d'action à votre notification push peut affecter la zone d'affichage de l'image. Veuillez effectuer un test à l'aide de l'aperçu du tableau de bord et des appareils en ligne/en production/instantanés afin de confirmer que les résultats correspondent à vos attentes.
- Le SDK Android Braze doit être activé pour que l'image puisse s'afficher.

{% alert note %}
Bien que Braze fournisse des instructions sur la manière de configurer le push riche, le rendu réel des notifications push riches peut varier en fonction de facteurs extérieurs tels que le rapport hauteur/largeur de l'appareil, la version d'Android, les contraintes spécifiques à l'OEM, et d'autres encore. Nous vous recommandons d'effectuer un test d'envoi sur plusieurs appareils Android pour vous assurer que vos notifications push riches s'affichent comme vous le souhaitez.
{% endalert %}

## Configurer votre notification enrichie Android

### Étape 1 : Créer une campagne de notification push

Suivez les étapes pour [créer une campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) afin de composer une notification push pour Android. Vous utiliserez le même composeur utilisé pour configurer des notifications push ne contenant pas de contenu enrichi.

### Étape 2 : Ajouter une légende

Veuillez ajouter le **texte de résumé** que vous souhaitez afficher avant l'image dans la notification.

![Une notification push riche provenant d'une application dédiée à l'alimentation pour animaux de compagnie appelée Dog, indiquant qu'il est temps de commander davantage de nourriture pour Spot, accompagnée d'un texte récapitulatif.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Étape 3 : Ajouter des médias

Veuillez ajouter votre image dans le champ **« Image de notification Android** » dans l'éditeur du message. Les images peuvent être téléchargées directement via le tableau de bord ou en spécifiant une URL pour le contenu hébergé ailleurs.

Pour plus d'informations sur les images prises en charge, consultez la rubrique [Spécifications des images.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)

![La section Image de notification Android où vous pouvez ajouter une image ou saisir une URL d'image.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Étape 4 : Continuer à créer votre campagne

Une fois que le contenu de votre notification enrichie est téléchargé dans le tableau de bord, vous pouvez continuer à [planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).
