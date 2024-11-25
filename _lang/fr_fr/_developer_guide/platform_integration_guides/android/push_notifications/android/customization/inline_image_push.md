---
nav_title: Notifications push d’image insérée
article_title: Notifications push d’image insérée pour Android
platform: Android
page_order: 5.9
description: "Cet article de référence explique comment implémenter une notification push d’image insérée dans votre application Android."
channel:
  - push

---

# Notifications push d’image insérée

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> Mettez en avant une image plus grande dans votre notification push Android à l’aide d’une notification push d’image insérée. Avec cette conception, les utilisateurs n’auront pas à étendre manuellement la notification push pour agrandir l’image. 

Aucune intégration supplémentaire ou modification du SDK n’est requise pour utiliser cette fonctionnalité. Les appareils ou les SDK qui ne répondent pas aux exigences minimales de version afficheront plutôt une notification push standard avec une grande image.

## Exigences d’utilisation

- Ce type de notification nécessite le SDK Braze pour Android v10.0.0 et ultérieures et des appareils Android M et ultérieurs. 
- Les appareils ou les SDK non pris en charge affichent à la place une notification push standard avec une grande image.
- Contrairement aux notifications push standard pour Android, les images des notifications push d’image insérée ont un rapport hauteur/largeur de 3:2.

{% alert note %}
Les appareils fonctionnant sous Android 12 s’afficheront différemment en raison des modifications dans les styles personnalisés de notification push.
{% endalert %}

## Configuration du tableau de bord

Lors de la création d'un message push Android, cette fonctionnalité est disponible dans le menu déroulant **Type de notification**.

![L'éditeur de campagne push montrant l'emplacement du menu déroulant "Type de notification" (au-dessus de l'aperçu push standard).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})
