---
nav_title: Push Image Inline
article_title: Push d'image en ligne pour Android
platform: Android
page_order: 5.9
description: "Cette appication couvre la façon d'implémenter la poussée d'image en ligne dans votre application Android."
channel:
  - Pousser
---

# Push d'image en ligne Android

![Exemple de Push d'image en ligne Android]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

Montrez une image plus grande dans votre notification push Android en utilisant Inline Image push. Avec cette conception, les utilisateurs n'auront pas à étendre manuellement la poussée pour agrandir l'image.

Aucune intégration supplémentaire ou modification du SDK n'est nécessaire pour utiliser cette fonctionnalité. Les périphériques ou les SDK qui ne remplissent pas les exigences de version minimale montreront à la place une notification standard de push de grandes images.

## Exigences d'utilisation

- Ce type de notification nécessite les appareils Braze Android SDK v10.0.0+ et Android M+.
- Les périphériques non pris en charge ou les SDKs vont revenir à la notification standard de push de grandes images.
- Contrairement aux notifications push Android normales, les images poussées dans les images en ligne sont de 3:2.

{% alert tip %}
**Note**: Les appareils fonctionnant sous Android 12 se rendront différemment en raison de changements dans les styles de notification push personnalisés.
{% endalert %}

Cette fonctionnalité est disponible dans le menu **Type de Notification** lors de la création d'un message Push Android.

![Exemple de Push d'image en ligne Android]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})
