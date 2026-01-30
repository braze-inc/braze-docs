{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Mise en place de notifications push silencieuses

Des notifications silencieuses sont disponibles via [l’API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) de Braze. Pour les utiliser, vous devez définir l’indicateur `send_to_sync` sur `true` dans l'[objet push d'Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) et vous assurer qu'aucun champ `title` ou `alert` n'est défini, car l'utilisation de cet indicateur avec `send_to_sync` entraînera des erreurs. Vous pouvez toutefois inclure les données `extras` dans l’objet.

Les notifications silencieuses sont également disponibles dans le tableau de bord. Pour envoyer une notification silencieuse, assurez-vous que les champs de titre et de corps de la notification sont vides comme illustré :

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Silent Push Notification Example -- Android")
