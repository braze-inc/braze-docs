---
nav_title: Umstellung von News Feed
article_title: Umstellung von News Feed
page_order: 10
description: "Dieser Artikel enthält eine Anleitung zur Migration vom Newsfeed zu Braze Content-Cards."
channel:
  - content cards
  - news feed
  
---

# Umstellung von News Feed auf Content Cards

{% alert note %}
Newsfeed ist veraltet. Braze empfiehlt Kunden, die unser News Feed-Tool verwenden, auf unseren Nachrichtenkanal Content Cards umzusteigen - er ist flexibler, anpassbarer und zuverlässiger.
{% endalert %}

> Die Umstellung vom Newsfeed auf Content-Cards braucht Zeit, ist aber ganz einfach. Sie können Inhalte nicht automatisch vom Newsfeed auf Content-Cards umstellen, sondern müssen Content-Cards komplett neu integrieren. Aber mit der neuen Flexibilität der Content Cards werden Sie es sicher nicht vermissen oder sich daran stören.

Wenden Sie sich an Ihren Braze-Kundenbetreuer für weitere Einzelheiten.

## Merkmale und Funktionalität

Content-Cards bieten viele Funktionen, die vom Newsfeed nicht unterstützt werden, darunter zusätzliche Zustellungsoptionen (wie aktions- und API-basiert) und erweiterte Analysen wie Conversion-Tracking.

Bei der Planung Ihrer Umstellung vom News Feed auf Content Cards ist es wichtig, dass Sie die wichtigsten Unterschiede zwischen Content Cards und dem News Feed beachten:

- **Segmentierung:** Die Segmentierung von Content Cards kann zum Zeitpunkt des Versendens von Nachrichten oder zum Zeitpunkt der ersten Ansicht der Karte ausgewertet werden. Die Segmentierung der News Feeds wird zu dem Zeitpunkt ausgewertet, zu dem die News Feed Cards angesehen werden.
- **Personalisierung:** Die Personalisierung von Content-Cards kann beim Nachrichtenversand oder beim ersten Aufruf der Karte als Vorlage eingerichtet werden. Die Personalisierung der News-Feed-Karten wird zum Zeitpunkt der Anzeige der News-Feed-Karten als Vorlage verwendet.

In der folgenden Tabelle werden die Unterschiede zwischen den unterstützten Funktionen von News Feed und Content Cards näher erläutert:

| Merkmal | Newsfeed | Content-Cards |
|---|---|---|
| Varianten- und kanalübergreifende Kampagnen | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> |
| Geplante, aktionsbasierte und API-basierte Bereitstellung | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> |
| Per API erstellte Nachrichten | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> |
| A/B-Tests | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> |
| [Karten ablegen und anheften][4] | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> |
| [Erweiterte Analysen][3] (z. B. Conversion Tracking) | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> |
| [Erhältlich in Canvas][2] | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> |
| [Connected-Content][5] | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> |
| Personalisierung und Segmentierung | Bei Impression als Vorlage angelegt | Bei Versand oder erster Impression als Vorlage angelegt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Implementierung

- Content-Cards und Newsfeed sind verschiedene Produkte. Daher ist eine einfache Integration für Ihre App oder Website erforderlich, um Content-Cards nutzen zu können.
- Sofern dies gewünscht ist, müssen bei einem Wechsel vorhandene Newsfeed-Cards manuell auf Content-Card-Kampagnen umgestellt werden.
- Content-Cards sind nicht dafür gedacht, gleichzeitig mit dem Newsfeed verwendet zu werden, da sie diesen ersetzen.
- Content Cards unterstützt derzeit keine Kategorien. Kategorien können über [Anpassungen und Schlüssel-Wert-Paare][1] erreicht werden.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
