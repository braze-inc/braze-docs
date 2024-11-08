---
nav_title: Notification push de conversation
article_title: Notification push de conversation pour Android
platform: Android
page_order: 5.92
description: "Cette application explique comment implémenter la notification push de conversation dans votre application Android."
channel:
  - push

---

# Notification push de conversation

> Cette application explique comment implémenter la notification push de conversation dans votre application Android.

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

L’[initiative des personnes et des conversations](https://developer.android.com/guide/topics/ui/conversations) est une initiative Android pluriannuelle qui vise à améliorer la prise en compte des personnes et des conversations dans les surfaces du système du téléphone. Cette priorité est basée sur le fait que la communication et l’interaction avec d’autres personnes restent la zone fonctionnelle la plus valorisée et la plus importante pour la majorité des utilisateurs d’Android dans toutes les tranches démographiques.

Aucune intégration supplémentaire ou modification du SDK n’est requise pour utiliser cette fonctionnalité. Les appareils ou les SDK qui ne répondent pas aux exigences minimales de version afficheront plutôt une notification push standard.

## Exigences d’utilisation

- Ce type de notification nécessite le SDK Braze pour Android v15.0.0 et ultérieures et des appareils Android 11 et ultérieurs. 
- Les appareils ou les SDK non pris en charge reprennent une notification push standard.

Cette fonctionnalité est uniquement disponible sur l’API REST de Braze. Voir l'[objet push d'Android]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object) pour plus d'informations.

