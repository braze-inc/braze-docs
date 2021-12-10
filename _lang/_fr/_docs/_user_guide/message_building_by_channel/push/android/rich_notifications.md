---
nav_title: "Créer des notifications riches pour Android"
article_title: Créer des notifications Rich Push
page_order: 3
page_layout: tutoriel
description: "Ce tutoriel explique comment configurer des notifications riches Android pour vos campagnes de Braze."
platform: Android
channel:
  - Pousser
tool:
  - Campagnes
---

# Créer des notifications riches pour Android

> Les notifications riches permettent une plus grande personnalisation de vos notifications push en ajoutant du contenu supplémentaire au-delà de la simple copie. Les notifications Android ont inclus des images dans les notifications push depuis un certain temps maintenant, les messages sous forme de « Image de notification étendue».

!\[Rich Not Blog\]\[7\]

## Exigences

- Notez que la vue de notification étendue n'est disponible que sur les appareils utilisant Jelly Bean (Android 4.1) ou supérieur. Si le périphérique d'un utilisateur ne fonctionne pas sur ces systèmes, il ne verra pas l'image de notification.
- Les images Android Extended Notification doivent être de 2:1, mais __n'ont pas de limite de taille__.
- Android permet également de définir une image séparée pour la vue de notification standard. <br>Taille recommandée des images : 512x256 pour Small, 1024x512 pour Medium, et 2048x1024 pour Large.
- Actuellement, les notifications riches d'Android ne permettent que les images statiques, y compris les formats de fichiers jpg et png, les gifs et autres formats d'image ne sont pas encore pris en charge.

{% alert note %}
Pendant que Braze fournit des instructions sur la façon de mettre en place une poussée riche, que le rendu réel des notifications poussées riches peut varier en fonction de facteurs extérieurs tels que le rapport d'aspect de l'appareil, la version androïde, les contraintes spécifiques à OEM, etc. <br><br> Nous vous recommandons de faire un test d'envoi sur plusieurs appareils Android pour vous assurer que vos notifications push riches apparaissent comme vous les avez prévues.
{% endalert %}

## Configuration de votre notification enrichie Android

### Étape 1 : Créer une campagne

Suivez les [étapes de la campagne][3] que vous faites normalement pour rédiger une notification push pour Android. Vous utiliserez le même compositeur que vous utilisez pour configurer les notifications push qui ne contiennent pas de contenu riche.

### Étape 2: Ajouter un sous-titrage

Ajoutez le **Résumé Texte/Image Légende** que vous souhaitez afficher au-dessus de l'image dans la notification.

!\[Ajouter un texte de résumé Android\]\[9\]

### Étape 3 : Ajouter un média

Ajoutez votre image dans le champ **Image de notification étendue** dans le compositeur du message. Les images peuvent être téléchargées directement via le tableau de bord ou en spécifiant une URL de contenu hébergée ailleurs.

!\[Ajouter une image Android\]\[8\]

### Étape 4 : Continuer à créer votre campagne

Une fois que votre contenu de notification enrichie est téléchargé sur le tableau de bord, vous pouvez simplement continuer [à planifier votre campagne][6] comme vous le faites toujours.
[7]: {% image_buster /assets/img_archive/RichNot_BlogImage.png %} [8]: {% image_buster /assets/img_archive/android_rich_image.png %} [9]: {% image_buster /assets/img_archive/android_rich_summarytext.png %}

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
