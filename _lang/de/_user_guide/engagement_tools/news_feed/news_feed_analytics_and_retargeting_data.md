---
nav_title: Nachrichten-Feed-Analytik
article_title: News Feed-Analyse und Retargeting-Daten
page_order: 10
page_type: reference
description: "Dieser Referenzartikel behandelt die Analyse von News Feeds und verschiedene damit verbundene Filter."
tool: 
- Reports
channel: news feed
hidden: true

---

# Nachrichten-Feed-Analysen

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Ähnlich wie bei geplanten Kampagnen verfügt das Newsfeed-Tool über ein Analytics-Dashboard zur Überwachung von Impressionen, Klicks und Klickraten. Wenn Sie in Ihrem Dashboard auf eine bestimmte News Feed-Nachricht klicken, können Sie eine Vielzahl von visuellen Analysen durchsehen. 

Oben auf der Seite können Sie Ihren Datumsbereich auswählen und eine schnelle Visualisierung Ihrer wichtigsten Metriken sehen. Außerdem können Sie Einzelheiten zu dieser News Feed-Nachricht sehen, z. B. wann sie gesendet wurde und an wen sie gesendet wurde.

![Details und Analysen für News Feed.][19]

Wenn Sie auf der Seite nach unten scrollen, sehen Sie eine größere Aufschlüsselung Ihrer Klicks und Impressionen von Tag zu Tag. Die Gesamtzahl der Klicks/Impressionen lässt sich anhand von Liniendiagrammen leicht mit den einzelnen Klicks und Impressionen vergleichen, während die Klickrate in einem interaktiven Balkendiagramm dargestellt wird.

![Grafik zur Aufschlüsselung der Performance.][20]

## Retargeting-Daten

Sie können die Daten von Braze darüber, welche Nutzer mit Ihrem News Feed interagieren, über Segmentfilter nutzen, mit denen Sie bestimmte Verhaltensweisen erneut ansprechen können.

### Filter für Impressionen einspeisen

Braze verfolgt automatisch, wann Nutzer:innen den Feed ansehen und wie oft sie ihn angesehen haben. Es sind zwei Filter verfügbar:

- Zuletzt aufgerufener Newsfeed
- Anzahl der Newsfeed-Aufrufe

**Last Viewed News Feed** ist eine effektive Möglichkeit, andere Kanäle zu nutzen, um Nutzer wieder in den Feed zu locken. Dies kann ganz einfach mit Push- und In-App-Benachrichtigungen geschehen. Braze hat mit effektiver Zielgruppenansprache eine Steigerung der News Feed Impressionen um über 100% erreicht. Mit zunehmendem Bekanntheitsgrad des Feeds werden diese Vorteile aufrechterhalten.

Mit der **Anzahl der Newsfeed-Ansichten** können Sie Nutzer:innen ansprechen, die den Feed noch nie oder nur selten angesehen haben, um mehr Impressionen für Ihre Karten zu erhalten.

Erwägen Sie, diese Filter zusammen oder mit anderen Filtern zu verwenden, um einen noch gezielteren Aufruf zum Handeln zu erstellen.

### Angeklickter Kartenfilter

Sie können Segmente erstellen, die darauf basieren, wie Nutzer mit bestimmten Karten im Feed interagiert haben. Der Filter befindet sich im Abschnitt „Retargeting“ der Filterliste und heißt „Angeklickte Karte“.

### Hat den Kartenfilter angeklickt

- Eignet sich gut für die erneute Ansprache von Nutzern, die auf eine Karte geklickt haben, aber Ihrer Aufforderung zum Handeln nicht nachgekommen sind.
- Es ist auch nützlich, Nutzer:innen mit verwandtem Content erneut anzusprechen, die für sie von Interesse sein könnten.
- Sie können diesen Filter auch verwenden, um Nutzer:innen, die nicht auf eine Karte geklickt haben, als Zielgruppe zusammenzustellen. Dieser Filter kann auf bestimmte Karten angewendet werden, so dass sie aus dem Feed eines Nutzers verschwinden, nachdem er sie angeklickt hat.
  - Um dies einzurichten, gehen Sie nach dem Erstellen einer Karte zurück und bearbeiten Sie das Zielsegment, um **Has nicht angeklickt** einzuschließen.
  - Nachdem ein Benutzer auf die Karte geklickt hat, wird die Karte automatisch aus dem Feed entfernt, wenn die nächste Sitzung des Benutzers beginnt.
  - Vermeiden Sie es, dieses Targeting übermäßig zu nutzen, da Nutzer:innen möglicherweise mit leeren Feeds enden. Am besten ist es, eine Kombination aus statischem und automatisch entfernten Content zu verwenden.
- Sie eignet sich auch gut, um Nutzer, die nicht auf eine Karte klicken, erneut anzusprechen, damit sie eine weitere Aufforderung zum Handeln erhalten.

![Beispiel für einen Segment Filter, der Nutzer:innen anzeigt, die nicht auf die Karte "Prost! Die Dos und Don'ts eines Trinkspruchs“.][14]


[19]: {% image_buster /assets/img_archive/braze_newsfeedanalytics.png %}
[20]: {% image_buster /assets/img_archive/braze_newsfeedanalytics2.png %}
[14]: {% image_buster /assets/img_archive/braze_newsfeedsegment.png %}
