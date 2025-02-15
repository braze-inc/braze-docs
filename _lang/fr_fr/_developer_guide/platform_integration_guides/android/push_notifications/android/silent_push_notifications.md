---
nav_title: Notifications push silencieuses
article_title: Notifications Push silencieuses pour Android
platform: Android
page_order: 3
description: "Cet article explique comment mettre en œuvre des notifications push silencieuses dans votre application Android."
channel:
  - push

---

# Notifications push silencieuses pour Android

> Les notifications silencieuses vous permettent d’informer votre application en arrière-plan lorsque des événements importants se produisent. Vous pourriez avoir de nouveaux messages instantanés à livrer, de nouveaux numéros d’un magazine à publier, des alertes de dernières nouvelles à envoyer ou le dernier épisode de l’émission télé préférée de votre utilisateur prête à être téléchargée pour une visualisation hors-ligne. Les notifications silencieuses sont idéales pour le contenu sporadique, mais important dans l’immédiat pour lequel le délai entre les recherches en arrière-plan peut ne pas être acceptable.

## Mise en place de notifications push silencieuses

Des notifications silencieuses sont disponibles via [l’API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) de Braze. Pour en tirer parti, vous devez définir l’indicateur `send_to_sync` sur `true` dans l'[objet Android push]({{site.baseurl}}/api/objects_filters/messaging/android_object/) et vous assurer qu'aucun champ `title` ou `alert` n'est défini, car il provoquera des erreurs s'il est utilisé avec `send_to_sync`- toutefois, vous pouvez inclure des données `extras` dans l'objet.

{% alert tip %}
Lorsque vous [composez votre message de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message//?tab=android#step-4-compose-your-push-message), vous pouvez envoyer une notification push Android silencieuse en envoyant un message ne comportant qu'un seul espace. Gardez à l'esprit qu'il ne s'agit **pas** de la méthode recommandée pour envoyer des notifications push, mais qu'elle peut être utile dans certains cas.
{% endalert %}

