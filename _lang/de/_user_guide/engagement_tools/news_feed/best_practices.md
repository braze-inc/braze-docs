---
nav_title: Bewährte Praktiken
article_title: Bewährte Praktiken für News Feeds
page_order: 20
page_type: reference
description: "Dieser Artikel enthält bewährte Verfahren für die Gestaltung und Anpassung von News Feed-Karten."
channel: news feed
hidden: true

---

# Bewährte Praktiken für News Feeds

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Der Newsfeed von Braze ist ein zielgerichteter, dynamischer Stream mit reichhaltigen Inhalten. Er bietet eine leistungsstarke Möglichkeit, Nutzer:innen mit ständig aktualisierten Inhalten zu erreichen, ohne dass zusätzliche Entwicklungsarbeit erforderlich ist. Diese Inhalte können auf verschiedene Segmente ausgerichtet und auf die gleiche Weise wie andere Braze-Nachrichten geplant werden. Jede Karte besteht aus einem Titel, einer Zusammenfassung, einem Bild und optional einer URL. Der Feed bietet außerdem die Möglichkeit, Deeplinks in der App zu setzen, direkt auf App Store, Google Play usw. zu verlinken oder auf eine Webansicht zu verweisen. Dieses einzigartige Braze UI-Element muss während der [Integration][1] aktiviert werden. Diskutieren Sie das unbedingt mit Ihren Entwicklern.

Wenn Sie mehr über die verschiedenen Arten von News Feed-Karten, deren Erstellung, Anwendungsfälle sowie Karten- und Bildspezifikationen erfahren möchten, lesen Sie unsere Seite über [Erstellen von News Feed-Elementen][4].

> Braze verbessert die Ladezeiten, indem es ein globales CDN verwendet, um alle Newsfeed-Bilder zu hosten.

## Bewährte Praktiken {#news-feed-best-practices}

Bei Braze schätzen wir die Anpassungsmöglichkeiten, die News Feed bietet. Hier finden Sie einige unserer bewährten Verfahren und Tipps, damit Sie das Beste aus Braze herausholen können.

### Aufmerksamkeit erregen

Je auffälliger, relevanter und interessanter Ihr News Feed ist, desto wahrscheinlicher ist es, dass er von anderen gesehen wird.  

- Verwenden Sie den Newsfeed, um Ihre App dynamisch zu gestalten und regelmäßig um neue Inhalte zu ergänzen.
- Nutzen Sie unterschiedliche Ankündigungen, damit der Newsfeed interessant bleibt.
- Nutzen Sie Bilder und Grafiken, die auffallen.

### Persönlich kommunizieren

Unternehmen und ihre Nutzer lieben und schätzen die Personalisierung.

- Passen Sie den News Feed so an, dass er die Identität Ihrer Marke widerspiegelt und ein nahtloses App-Erlebnis bietet.
- Denken Sie daran, dass zielgerichtete Module sofort zu Aktionen innerhalb der App anregen können, und Protokoll-URLs können die Aufmerksamkeit auf verschiedene Bereiche der App lenken und zu bestimmten Verhaltensweisen wie Bewertungen, Käufen und mehr anregen.
- Segmentieren Sie die Nutzer und passen Sie bestimmte Ankündigungen so an, dass sie zu bestimmten Handlungen anregen.

### Nützlich sein

Die Inhalte, die Sie im Newsfeed anzeigen, können sehr unterschiedlich sein und mit Kampagnen zusammenwirken.  

- Geben Sie Ankündigungen heraus, die zur Interaktion anregen, Neuigkeiten hervorheben und den Verkauf fördern.
- Entwickeln Sie einen Zeitplan für Kampagnen wie Onboarding usw. und legen Sie die Abfolge und Häufigkeit Ihrer Kommunikation fest.
- Verstärken Sie Kampagnen, indem Sie Nachrichten kanalübergreifend in den Newsfeed integrieren.

## Beispiel für Integration

1-800-Flowers.com verwendet den News Feed, um seinen Nutzern relevante Informationen zu liefern. Die SDK-Integration bleibt völlig transparent: In der App selbst wird Braze nicht erwähnt und das Design des Newsfeed-Moduls passt zum Rest der App.

![shapefeed][2]{: style="max-width:50%;"}

Weitere Beispiele für News Feeds finden Sie in unseren [Fallstudien][3].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[2]: {% image_buster /assets/img_archive/18F_newsfeed.png %}
[3]: https://www.braze.com/customers
[4]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/
