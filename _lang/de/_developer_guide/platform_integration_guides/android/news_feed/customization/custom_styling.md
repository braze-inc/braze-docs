---
nav_title: Angepasste Stile
article_title: Angepasstes Newsfeed-Styling für Android und FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Dieser referenzierte Artikel beschreibt, wie Sie das angepasste Stile des Newsfeeds in Ihrer Android- oder FireOS-Anwendung hinzufügen."
channel:
  - news feed
  
---

# Angepasste Stile

> Dieser referenzierte Artikel beschreibt, wie Sie das angepasste Stile des Newsfeeds in Ihrer Android- oder FireOS-Anwendung hinzufügen. 

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Die UI-Elemente von Braze sind standardmäßig so gestaltet, dass sie den Standard-UI-Richtlinien von Android entsprechen und ein nahtloses Erlebnis bieten. Sie können diese Standard-Stile in der Datei `res/values/style.xml` in der Braze SDK Distribution sehen:

```xml
  <style name="Braze"/>
  <!-- Feed -->
  <style name="Braze.Feed"/>
  <style name="Braze.Feed.List">
    <item name="android:background">@android:color/transparent</item>
    <item name="android:divider">@android:color/transparent</item>
    <item name="android:dividerHeight">16.0dp</item>
    <item name="android:paddingLeft">12.5dp</item>
    <item name="android:paddingRight">5.0dp</item>
    <item name="android:scrollbarStyle">outsideInset</item>
  </style>
  ...
  </style>
```

Wenn Sie möchten, können Sie diese Stile überschreiben, um ein Erscheinungsbild zu schaffen, das besser zu Ihrer App passt. Um einen Stil zu überschreiben, kopieren Sie ihn in seiner Gesamtheit in die Datei `styles.xml` Ihres Projekts und nehmen Sie die gewünschten Änderungen vor. Der gesamte Stil muss in Ihre lokale `styles.xml`-Datei kopiert werden, damit alle Attribute korrekt gesetzt werden.

{% tabs local %}
{% tab Korrekte Überschreibung des Stils %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```
{% endtab %}
{% tab Falsche Stilüberschreibung %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
{% endtab %}
{% endtabs %}

## Feed-Stil-Elemente

Im Folgenden finden Sie eine Beschreibung der Theme-fähigen UI-Elemente von Braze und deren Namen für die Stilgestaltung:

{% gallery %}{% image_buster /assets/img_archive/Image27Theming.png %}
{% image_buster /assets/img_archive/Image28Theming.png %}
{% image_buster /assets/img_archive/Image29Theming.png %}
{% image_buster /assets/img_archive/Image30Theming.png %}{% endgallery %}

## Eine angepasste Schriftart einstellen

Braze erlaubt das Anpassen einer angepassten Schriftart mit Hilfe der [Schriftfamilienführung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization). Um sie zu verwenden, überschreiben Sie einen Stil für Karten und verwenden das Attribut `fontFamily`, um Braze anzuweisen, Ihre angepasste Schriftfamilie zu verwenden.

Wenn Sie zum Beispiel die Schriftart für alle Titel von Kurznachrichtenkarten aktualisieren möchten, überschreiben Sie den Stil `Braze.Cards.ShortNews.Title` und referenzieren Ihre angepasste Schriftfamilie. Der Wert des Attributs sollte auf eine Schriftfamilie in Ihrem Verzeichnis `res/font` verweisen.

Hier ist ein verkürztes Beispiel mit einer benutzerdefinierten Schriftfamilie, `my_custom_font_family`, auf die in der letzten Zeile verwiesen wird:

```
<style name="Braze.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
  ...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

