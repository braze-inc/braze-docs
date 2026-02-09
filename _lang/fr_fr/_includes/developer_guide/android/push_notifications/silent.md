{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Mise en place de notifications push silencieuses

Des notifications silencieuses sont disponibles via [l’API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) de Braze. Pour en tirer parti, vous devez définir l’indicateur `send_to_sync` sur `true` dans l'[objet Android push]({{site.baseurl}}/api/objects_filters/messaging/android_object/) et vous assurer qu'aucun champ `title` ou `alert` n'est défini, car il provoquera des erreurs s'il est utilisé avec `send_to_sync`- toutefois, vous pouvez inclure des données `extras` dans l'objet.
