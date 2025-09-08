---
nav_title: "Création de notifications riches"
article_title: "Créer des notifications push riches pour Android"
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

Avant de créer une notification push riche pour Android, notez les détails suivants :

- Les notifications riches Android ne sont pas disponibles lors de la création d'une campagne de notification push rapide.
- Les images de notification étendue Android doivent avoir un rapport 2:1, mais n’ont pas de limite de taille.
- Android permet également de définir une image séparée pour la vue de notification standard. Voici les dimensions recommandées pour les images : 
  - **Petites :** 512x256
  - **Intermédiaires :** 1024x512 
  - **Grandes :** 2048x1024
- Actuellement, les notifications enrichies Android ne permettent d'utiliser que des images statiques, y compris les formats d'image JPEG et PNG. Le format GIF et les autres formats d'image ne sont pas encore pris en charge.
- L'ajout de boutons d'action à votre notification push peut affecter la zone d'affichage de l'image. Testez avec l'aperçu du tableau de bord et les appareils en ligne/instantanés pour confirmer que les résultats sont conformes aux attentes.

{% alert note %}
Bien que Braze fournisse des instructions sur la manière de configurer le push riche, le rendu réel des notifications push riches peut varier en fonction de facteurs extérieurs tels que le rapport hauteur/largeur de l'appareil, la version d'Android, les contraintes spécifiques à l'OEM, et d'autres encore. Nous vous recommandons d'effectuer un test d'envoi sur plusieurs appareils Android pour vous assurer que vos notifications push riches s'affichent comme vous le souhaitez.
{% endalert %}

## Configurer votre notification enrichie Android

### Étape 1 : Créer une campagne de notification push

Suivez les étapes pour [créer une campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) afin de composer une notification push pour Android. Vous utiliserez le même composeur utilisé pour configurer des notifications push ne contenant pas de contenu enrichi.

### Étape 2 : Ajouter une légende

Ajoutez le **texte récapitulatif/la légende de l'image** que vous souhaitez afficher avant l'image dans la notification.

![La section de l'image de la notification étendue où vous pouvez ajouter une image ou entrer l'URL d'une image.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Étape 3 : Ajouter des médias

Ajoutez votre image dans le champ **Image de la notification élargie** dans le compositeur du message. Les images peuvent être téléchargées directement via le tableau de bord ou en spécifiant une URL pour le contenu hébergé ailleurs.

Pour plus d'informations sur les images prises en charge, consultez la rubrique [Spécifications des images.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)

![Un utilisateur reçoit une notification push pour iOS avec pour titre "Bonjour" et pour texte "Merci d'avoir adhéré à notre programme de fidélité !".]({% image_buster /assets/img_archive/android_rich_image.png %}).

### Étape 4 : Continuer à créer votre campagne

Une fois que le contenu de votre notification enrichie est téléchargé dans le tableau de bord, vous pouvez continuer à [planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

