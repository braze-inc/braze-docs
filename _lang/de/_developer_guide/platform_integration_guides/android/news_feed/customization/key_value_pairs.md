---
nav_title: Schlüssel-Werte-Paare
article_title: Newsfeed Schlüssel-Wert-Paare für Android und FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Schlüssel-Wert-Paare des Newsfeed in Ihrer Android- oder FireOS-Anwendung verwenden können."
channel:
  - news feed

---

# Schlüssel-Wert-Paare

> In diesem referenzierten Artikel erfahren Sie, wie Sie Schlüssel-Wert-Paare des Newsfeed in Ihrer Android- oder FireOS-Anwendung verwenden können.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

`Card` Objekte können optional Schlüssel-Wert-Paare als `extras` enthalten. Diese können verwendet werden, um Daten mit einer `Card` zur weiteren Verarbeitung durch die Anwendung nach unten zu senden.

Rufen Sie die folgende Funktion für ein `Card`-Objekt auf, um dessen Extras abzurufen:

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
