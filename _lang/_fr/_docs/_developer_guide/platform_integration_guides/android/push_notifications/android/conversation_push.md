---
nav_title: Push de conversation
article_title: Conversation Push pour Android
platform: Android
page_order: 5.92
description: "Cette appication couvre comment implémenter la poussée de conversation android dans votre application Android."
channel:
  - Pousser
---

# Conversation Android push

![Exemple de poussée de conversation Android]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

L'initiative [personnes et conversations][2] est une initiative Android pluriannuelle qui vise à élever les personnes et les conversations dans la surface du système du téléphone. Cette priorité est basée sur le fait que la communication et l'interaction avec d'autres personnes reste la zone fonctionnelle la plus précieuse et la plus importante pour la majorité des utilisateurs d'Android à travers toutes les données démographiques.

Aucune intégration supplémentaire ou modification du SDK n'est nécessaire pour utiliser cette fonctionnalité. Les périphériques ou SDK qui ne répondent pas aux exigences de version minimale montreront à la place une notification push standard.

## Exigences d'utilisation

- Ce type de notification nécessite les appareils Braze Android SDK v15.0.0+ et Android 11+.
- Les périphériques non pris en charge ou les SDK seront remplacés par une notification push standard.

Cette fonctionnalité n'est disponible que sur l'API Braze REST. Voir la [Documentation de l'objet Push Android][1] pour plus d'informations.

[1]: {{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object
[2]: https://developer.android.com/guide/topics/ui/conversations
