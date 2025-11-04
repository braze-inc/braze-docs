{% multi_lang_include developer_guide/prerequisites/react_native.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Verwendung von Expo zur Aktivierung von Rich-Push-Benachrichtigungen

Für das React Native SDK **sind Rich-Push-Benachrichtigungen für Android standardmäßig verfügbar**.

Um Rich-Push-Benachrichtigungen unter iOS mit Expo zu aktivieren, legen Sie die Eigenschaft `enableBrazeIosRichPush` im Objekt `expo.plugins`der `app.json` auf `true` fest:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Fügen Sie dann den Bundle-Bezeichner für diese App-Erweiterung zur Konfiguration der Zugangsdaten Ihres Projekts hinzu: `<your-app-bundle-id>.BrazeExpoRichPush`.
