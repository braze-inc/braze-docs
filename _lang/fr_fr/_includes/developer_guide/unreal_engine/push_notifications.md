{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Mise en place des notifications push

### Étape 1 : Configurez votre projet

{% tabs %}
{% tab Android %}
Tout d'abord, ajoutez Firebase à votre projet Android. Pour obtenir des instructions pas à pas, consultez le [guide de configuration de Firebase](https://firebase.google.com/docs/android/setup) de Google.
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/apns_token.md %}
{% endtab %}
{% endtabs %}

### Étape 2 : Activer les notifications push

{% tabs %}
{% tab Android %}
Ajoutez les lignes suivantes au fichier `engine.ini` de votre projet. Veillez à remplacer `YOUR_SEND_ID` par l'[ID de l'expéditeur dans votre projet Firebase](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials).

```ini
bEnableFirebaseCloudMessagingSupport=true
bIsFirebaseCloudMessagingRegistrationEnabled=true
FirebaseCloudMessagingSenderIdKey=YOUR_SENDER_ID
```

Dans le même répertoire que [BrazeUPLAndroid.xml](./BrazeSample/Plugins/Braze/Source/Braze/BrazeUPLAndroid.xml)créez un nouveau répertoire nommé `AndroidCopies` et ajoutez-y votre fichier `google-services.json`.
{% endtab %}

{% tab iOS %}
Dans votre projet, allez dans **Réglages** > **Réglages du projet** > **iOS** > **En ligne** puis cochez **Activer la prise en charge des notifications à distance.** Une fois que vous avez terminé, vérifiez que les fonctions "push" sont activées dans votre disposition.

{% alert important %}
Pour activer les fonctionnalités push pour iOS, votre projet doit avoir été créé à partir des sources. Pour plus d'informations, consultez [Unreal Engine : Créer à partir des sources](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configurations optionnelles

{% tabs %}
{% tab Android %}
#### Réglage des petites et grandes icônes

Pour définir les [petites et grandes icônes de notification :]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android&tab=android#configure-icons)

1. Ajoutez des icônes au dossier de dessin approprié (`drawable` par défaut) à l'intérieur du dossier `AndroidCopies/res`.
2. Ajoutez `braze.xml` au dossier `AndroidCopies/res/values` pour définir les icônes. Un fichier très basique braze.xml:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <drawable name="com_braze_push_small_notification_icon">@drawable/notification_small_icon</drawable>
        <drawable name="com_braze_push_large_notification_icon">@drawable/notification_large_icon</drawable>
    </resources>
    ```

{% alert note %}
Les fichiers du dossier `AndroidCopies` seront copiés dans la structure du projet Android généré, comme défini dans le dossier `BrazeUPLAndroid.xml`.
{% endalert %}
{% endtab %}

{% tab iOS %}
#### Notifications de lancement à distance

Depuis la version 4.25.3 d'Unreal Engine, UE4 ne prend pas en charge la réception d'une notification à distance qui provoque le lancement initial de l'application. Afin de prendre en charge la réception de cette notification, nous avons créé deux patchs git à appliquer - un pour UE4 et un pour le plugin Braze SDK.

1. Dans votre répertoire UE4 Engine `Source`, appliquez le patch git `UE4_Engine-Cache-Launch-Remote-Notification.patch`.
2. Dans votre répertoire Braze Unreal SDK, appliquez le patch git `Braze_SDK-Read-Cached-Remote-Launch-Notification.patch`.
{% endtab %}
{% endtabs %}
