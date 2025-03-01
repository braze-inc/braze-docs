---
nav_title: Schriftart anpassen
article_title: Schriftart-Anpassung für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 7
description: "Dieser Referenzartikel behandelt Optionen zur Anpassung der Schriftart, wie z.B. die Definition einer Schriftfamilie, und zeigt, wie Sie diese in Ihrer Android- oder FireOS-Anwendung referenzieren können."

---

# Anpassung der Schriftart

> Dieser Referenzartikel behandelt Optionen zur Anpassung der Schriftart, wie z.B. die Definition einer Schriftfamilie, und zeigt, wie Sie diese in Ihrer Android- oder FireOS-Anwendung referenzieren können.

Die Schriftarten im Braze SDK können über XML mit Hilfe der AndroidX Bibliotheken gemäß [Font in XML](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html) eingestellt werden. Um Ihre angepasste Schrift mit dem Braze SDK zu verwenden, müssen Sie zunächst eine Schriftfamilie erstellen.

## Eine Schriftfamilie erstellen

Im Folgenden finden Sie ein Beispiel für eine angepasste Schriftfamiliendefinition unter Verwendung des [Schriftfamilienleitfadens](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family). Für dieses Beispiel verwenden wir die [Schriftart Bungee Shade](https://fonts.google.com/specimen/Bungee+Shade).

```XML
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
             xmlns:app="http://schemas.android.com/apk/res-auto">

  <!--Note: You must declare both sets of attributes
      so that your fonts load on devices running Android 8.0 (API level 26) or lower.
      See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html -->

  <font android:fontStyle="normal"
        android:fontWeight="400"
        android:font="@font/bungeeshade"

        app:fontStyle="normal"
        app:fontWeight="400"
        app:font="@font/bungeeshade"/>
</font-family>
```

Nachdem wir die Definition der Schriftfamilie in `/res/font/bungee_font_family.xml` gespeichert haben, können wir sie in XML als `@font/bungee_font_family` referenzieren.

## Verweis auf Ihre Schriftfamilie

Jetzt, da die Schriftfamilie erstellt ist, können Sie die Standardvorgaben von Braze in Ihrem `styles.xml` überschreiben, um Referenzen auf die Schriftfamilie aufzunehmen.

Zum Beispiel würde die folgende Stilüberschreibung die Schriftfamilie `bungee` für alle In-App-Nachrichten von Braze verwenden.

```
<style name="Braze.InAppMessage">
  <item name="android:fontFamily">@font/bungee_font_family</item>
  <item name="fontFamily">@font/bungee_font_family</item>
</style>

<style name="Braze.Cards">
  <item name="android:fontFamily">@font/another_custom_font_family</item>
  <item name="fontFamily">@font/another_custom_font_family</item>
</style>
```

{% alert warning %}
Die Stilattribute `android:fontFamily` und `fontFamily` müssen gesetzt werden, um die Kompatibilität mit allen SDK-Versionen zu gewährleisten.
{% endalert %}

