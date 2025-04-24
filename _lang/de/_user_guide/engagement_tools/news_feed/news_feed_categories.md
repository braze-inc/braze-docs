---
nav_title: News Feed Kategorien
page_order: 9

page_type: reference
description: "Dieser Referenzartikel beschreibt Newsfeed-Kategorien, die es ermöglichen, mehrere Instanzen des Newsfeeds in Ihre Anwendung zu integrieren."
tool: Dashboard
channel: news feed
hidden: true

---

# News Feed Kategorien

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Newsfeed-Kategorien ermöglichen es, mehrere Instanzen des Newsfeeds in Ihre Anwendung zu integrieren. Es ist möglich, Feeds in verschiedene Fenster zu integrieren, die nur Newsfeed-Karten einer bestimmten Kategorie anzeigen.

![Das News Feed-Panel mit einer Bildkartenvorschau mit Untertiteln für einen News Feed-Artikel mit dem Titel "Sweet Teeth - Buy candy in bulk!" mit der Nachricht "Satisfy your sweet tooth and stop by our store! Erwähnen Sie diese Anzeige und Sie erhalten 50% Rabatt auf Ihre erste Tüte Süßigkeiten." Es gibt vier Kontrollkästchen für News Feed-Kategorien: Nachrichten, Ankündigungen, Werbung und Soziales. Keine der Kategorien ist ausgewählt.][1]

Die Kennzeichnung eines News Feeds als aus einer bestimmten Kategorie stammend ist für den Endbenutzer nicht sichtbar. Standardmäßig zeigt der Braze News Feed Karten aller Kategorien an, es sei denn, ein Feed wurde im App-Code speziell für die Anzeige bestimmter Kategorien konfiguriert. Weitere Informationen zur Konfiguration des App-Codes finden Sie unter [Definieren einer News Feed Kategorie][2].

[1]: {% image_buster /assets/img_archive/Newsfeed_category.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/defining_a_news_feed_category/
