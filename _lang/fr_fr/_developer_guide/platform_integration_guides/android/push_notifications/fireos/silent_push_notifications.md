---
nav_title: Notifications push silencieuses
article_title: Notifications Push silencieuses pour FireOS
platform: FireOS
page_order: 3

page_type: reference
description: "Cet article de référence décrit comment envoyer des notifications push silencieuses à FireOS, ainsi que des cas d’usage potentiels lorsque des notifications push silencieuses peuvent être préférables."
channel: push

---

# Notifications push silencieuses

> Les notifications silencieuses vous permettent d’informer votre application en arrière-plan lorsque des événements importants se produisent. Vous pourriez avoir de nouveaux messages instantanés à livrer, de nouveaux numéros d’un magazine à publier, des alertes de dernières nouvelles à envoyer ou le dernier épisode de l’émission télé préférée de votre utilisateur prête à être téléchargée pour une visualisation hors-ligne. Les notifications silencieuses sont idéales pour le contenu sporadique, mais important dans l’immédiat pour lequel le délai entre les recherches en arrière-plan peut ne pas être acceptable.

Des notifications silencieuses sont disponibles via [l’API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) de Braze. Pour les utiliser, vous devez définir l’indicateur `send_to_sync` sur `true` dans l'[objet push d'Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) et vous assurer qu'aucun champ `title` ou `alert` n'est défini, car l'utilisation de cet indicateur avec `send_to_sync` entraînera des erreurs. Vous pouvez toutefois inclure les données `extras` dans l’objet.

Les notifications silencieuses sont également disponibles dans le tableau de bord. Pour envoyer une notification silencieuse, assurez-vous que les champs de titre et de corps de la notification sont vides comme illustré :

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Exemple de notification push silencieuse -- Android")

