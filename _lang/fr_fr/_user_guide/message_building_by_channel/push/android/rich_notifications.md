---
nav_title: "Créer des notifications enrichies"
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

> Les notifications riches permettent de personnaliser davantage vos notifications push en ajoutant du contenu supplémentaire au-delà de la simple copie. Depuis quelque temps, les notifications Android incluent des images dans les notifications push, appelées "image de notification étendue".

## Conditions préalables

Avant de créer une notification push riche pour Android, notez les détails suivants :

- Les notifications riches Android ne sont pas disponibles lors de la création d'une campagne push rapide.
- Les images des notifications étendues Android doivent avoir un rapport de 2:1, mais n'ont pas de limite de taille.
- Android permet également de définir une image distincte pour l'affichage standard des notifications. Il s'agit des dimensions recommandées pour les images : 
  - **Petit :** 512x256
  - **Moyen :** 1024x512 
  - **Grandes :** 2048x1024
- Actuellement, les notifications enrichies d'Android n'autorisent que les images statiques, y compris les formats d'image JPEG et PNG. Les formats GIF et autres formats d'image ne sont pas encore pris en charge.
- L'ajout de boutons d'action à votre notification push peut affecter la zone d'affichage de l'image. Testez avec l'aperçu du tableau de bord et les appareils en ligne/instantanés pour confirmer que les résultats sont conformes aux attentes.
- Le SDK Android de Braze doit être activé pour que l'image soit rendue.

{% alert note %}
Bien que Braze fournisse des instructions sur la manière de configurer le push riche, le rendu réel des notifications push riches peut varier en fonction de facteurs extérieurs tels que le rapport hauteur/largeur de l'appareil, la version d'Android, les contraintes spécifiques à l'OEM, et d'autres encore. Nous vous recommandons d'effectuer un test d'envoi sur plusieurs appareils Android pour vous assurer que vos notifications push riches s'affichent comme vous le souhaitez.
{% endalert %}

## Configuration de votre notification enrichie Android

### Étape 1 : Créer une campagne de push

Suivez les étapes pour [créer une campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) afin de composer une notification push pour Android. Vous utiliserez le même compositeur pour configurer les notifications push qui ne contiennent pas de contenu riche.

### Étape 2 : Ajouter des sous-titres

Ajoutez le **texte de synthèse/la légende de l'image** que vous souhaitez afficher avant l'image dans la notification.

La section de l'image de notification étendue où vous pouvez ajouter une image ou entrer une URL d'image.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Étape 3 : Ajouter un média

Ajoutez votre image dans le champ **Image de la notification élargie** dans le compositeur du message. Les images peuvent être téléchargées directement via le tableau de bord ou en spécifiant une URL de contenu hébergée ailleurs.

Pour plus d'informations sur les images prises en charge, consultez la rubrique [Spécifications des images.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)

\![Un utilisateur reçoit une notification push pour iOS avec pour titre "Bonjour" et pour texte "Merci d'avoir adhéré à notre programme de fidélité !".]({% image_buster /assets/img_archive/android_rich_image.png %})

### Étape 4 : Poursuivre la création de votre campagne

Une fois que le contenu de votre notification enrichie est téléchargé dans le tableau de bord, vous pouvez continuer à [planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

