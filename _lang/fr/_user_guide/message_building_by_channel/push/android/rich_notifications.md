---
nav_title: "Notifications enrichies pour Android"
article_title: Notifications enrichies pour Android
page_order: 3
page_layout: tutorial
description: "Ce didacticiel explique comment configurer des notifications enrichies Android pour vos campagnes Braze."
platform: Android
channel:
  - Notification push
tool:
  - Campaigns
  
---

# Créer des notifications enrichies pour Android

> Les notifications enrichies permettent d’obtenir plus de personnalisation dans vos notifications push en ajoutant du contenu supplémentaire en plus du texte seul. Les notifications Android autorisent les images dans les notifications push depuis un certain temps, appelées « images de notification étendue ».

## Conditions

- Prenez en compte le fait que la vue de notification étendue est uniquement disponible sur les appareils utilisant Jelly Bean (Android 4.1) ou ultérieur. Si l’appareil d’un utilisateur ne tourne pas sur ces systèmes, il ne verra pas l’image de notification.
- Les images de notification étendue Android doivent avoir un rapport 2:1, mais n’ont pas de limite de taille.
- Android permet également de définir une image séparée pour la vue de notification standard. <br>Tailles d’images recommandées : 512 x 256 pour les petites, 1024 x 512 pour les moyennes et 2048 x 1024 pour les grandes.
- Actuellement, les notifications enrichies Android permettent uniquement des images statiques utilisant les formats .jpg et .png. Les .gif et les autres formats ne sont pas encore pris en charge.
- Notez que l’ajout de boutons d’action à votre notification push peut affecter la zone de l’image pouvant être affichée. Testez avec l’aperçu du tableau de bord et directement sur des appareils pour vous assurer que vous obtenez le résultat escompté.

{% alert note %}
Même si Braze fournit des instructions sur la manière de mettre en place des push riche, leur rendu réel peut varier en fonction de facteurs externes tels que le rapport d’aspect de l’appareil, la version d’Android, des contraintes spécifiques au fabriquant, etc. 
<br><br>
Nous vous recommandons d’effectuer un test d’envoi à plusieurs appareils Android pour vous assurer que vos notifications push enrichies apparaissent comme vous le désirez.
{% endalert %}

## Configurer votre notification enrichie Android

### Étape 1 : Créer une campagne

Suivez les étapes pour [créer une campagne][3] pour composer une notification push pour Android. Vous utiliserez le même composeur utilisé pour configurer des notifications push ne contenant pas de contenu enrichi.

### Étape 2 : Ajouter une légende

Ajoutez le **texte résumé ou la légende d’image** que vous souhaitez afficher avant l’image dans la notification.

![][9]

### Étape 3 : Ajouter des médias

Ajoutez votre image dans le champ **Image de notification étendue** dans le composeur du message. Les images peuvent être téléchargées directement via le tableau de bord ou en spécifiant une URL pour le contenu hébergé ailleurs.

![][8]

### Étape 4 : Continuer à créer votre campagne

Une fois que votre contenu de notification enrichie est téléchargé sur le tableau de bord, vous pouvez simplement continuer à [planifier votre campagne][6].

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[8]: {% image_buster /assets/img_archive/android_rich_image.png %}
[9]: {% image_buster /assets/img_archive/android_rich_summarytext.png %}
