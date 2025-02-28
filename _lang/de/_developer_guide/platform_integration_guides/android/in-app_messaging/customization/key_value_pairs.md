---
nav_title: Schlüssel-Werte-Paare
article_title: In-App-Nachrichten-Schlüssel-Wertepaare für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 6.9
description: "Dieser Referenzartikel behandelt Schlüssel-Wert-Paare für In-App-Nachrichten für Ihre Android- oder FireOS-Anwendung."
channel:
  - in-app messages

---

# Schlüssel-Wert-Paare

> Dieser Referenzartikel behandelt Schlüssel-Wert-Paare für In-App-Nachrichten für Ihre Android- oder FireOS-Anwendung.

Objekte des Typs "In-App-Nachricht" können Schlüssel-Wert-Paare als `extras` enthalten. Sie werden beim Erstellen einer In-App-Nachrichten-Kampagne auf dem Dashboard unter **Einstellungen** festgelegt. Sie können verwendet werden, um Daten mit einer In-App-Nachricht zur weiteren Bearbeitung durch die Anwendung zu senden.

Rufen Sie Folgendes auf, wenn Sie ein Objekt des Typ In-App-Nachricht erhalten und dessen Extras abrufen möchten:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie in dieser [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).

