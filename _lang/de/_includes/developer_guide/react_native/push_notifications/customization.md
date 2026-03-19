{% multi_lang_include developer_guide/prerequisites/react_native.md %} Bitte [richten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native) Sie auch [Push-Benachrichtigungen ein]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Anpassung in React Native vorantreiben

Das Braze React Native SDK stellt keine Anpassungsmöglichkeiten für Push-Benachrichtigungen (Aktions-Buttons, Kategorien, benutzerdefinierte Benachrichtigungsfabriken) über seine JavaScript-API zur Verfügung. Diese Features erfordern eine native Konfiguration in Ihren iOS- und Android-Projekten.

Die folgende Tabelle zeigt, welche Features eine native Konfiguration erfordern:

| Feature | iOS | Android |
| --- | --- | --- |
| Aktions-Buttons | In nativem SWIFT/OBJECTIVE-C konfigurieren | In nativem Java/Kotlin konfigurieren |
| Push-Kategorien | In nativem SWIFT/OBJECTIVE-C konfigurieren | In nativem Java/Kotlin konfigurieren |
| Angepasste Benachrichtigungsfabrik | -- | In nativem Java/Kotlin konfigurieren |
| Anpassung von Badges | In nativem SWIFT/OBJECTIVE-C konfigurieren | -- |
| Benutzerdefinierte Klänge | In nativem SWIFT/OBJECTIVE-C konfigurieren | In nativem Java/Kotlin konfigurieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### iOS-Anpassung

Um Push-Action-Buttons, Kategorien, Badges oder benutzerdefinierte Sounds unter iOS hinzuzufügen, implementieren Sie bitte die native Konfiguration in Ihrer Anwendung`AppDelegate`(SWIFT oder Objective C). Eine Schritt-für-Schritt-Anleitung finden Sie unter [„Push-Benachrichtigungen anpassen – SWIFT]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift)“.

### Android-Anpassung

Um Push-Action-Buttons, Kategorien oder eine benutzerdefinierte Benachrichtigungsfabrik auf Android hinzuzufügen, implementieren Sie bitte die native Konfiguration in Ihrem Android-Projekt. Eine Schritt-für-Schritt-Anleitung finden Sie unter [Push-Benachrichtigungen anpassen – Android]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android).
