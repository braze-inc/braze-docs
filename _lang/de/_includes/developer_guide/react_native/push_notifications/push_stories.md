{% multi_lang_include developer_guide/prerequisites/react_native.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Enablement von Push-Storys

Für das React Native SDK **sind Push-Storys für Android standardmäßig verfügbar**.

Um Push-Storys unter iOS mit Expo zu aktivieren, stellen Sie sicher, dass Sie eine App-Gruppe für Ihre Anwendung definiert haben. Weitere Informationen finden Sie unter [Hinzufügen einer App-Gruppe]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Konfigurieren Sie als Nächstes die Eigenschaft `enableBrazeIosPushStories` auf `true` und weisen Sie Ihre App-Gruppen-ID `iosPushStoryAppGroup` in Ihrem `expo.plugins` -Objekt auf `app.json` zu:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Fügen Sie dann den Bundle-Bezeichner für diese App-Erweiterung zur Konfiguration der Zugangsdaten Ihres Projekts hinzu: `<your-app-bundle-id>.BrazeExpoPushStories`. Weitere Einzelheiten zu diesem Vorgang finden Sie unter [Verwendung von App-Erweiterungen mit Expo Application Services]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).

{% alert warning %}
Wenn Sie Push-Storys mit Expo Application Services verwenden, stellen Sie sicher, dass Sie das Flag `EXPO_NO_CAPABILITY_SYNC=1` verwenden, wenn Sie `eas build` ausführen. Es gibt ein bekanntes Problem in der Befehlszeile, das die App-Gruppen-Funktion aus dem Provisioning-Profil der Erweiterung entfernt.
{% endalert %}
