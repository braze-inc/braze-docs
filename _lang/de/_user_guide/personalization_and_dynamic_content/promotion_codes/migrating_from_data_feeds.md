---
nav_title: Migration von Daten-Feeds zu Aktionscodes
article_title: Migration von Daten-Feeds zu Promotion-Codes
page_order: 0
description: "Dieser referenzierte Artikel enthält eine Anleitung zur Migration von Daten-Feeds zu Aktionscodes."
---

# Migration von Daten-Feeds zu Aktionscodes

{% alert note %}
Die Daten-Feed-Funktion ist veraltet. Braze empfiehlt Kund:innen, die Daten-Feeds verwenden, den Übergang zu Aktionscode-Listen.
{% endalert %}

> Diese Seite führt Sie durch die Migration von Daten-Feeds zu Aktionscodes. Dies ist ein unkomplizierter Prozess, bei dem Sie manuell Aktionscode-Listen mit den Informationen aus Ihren Daten-Feeds erstellen und Ihre Nachrichten-Referenzen entsprechend aktualisieren.

## Merkmale und Funktionalität

Es gibt ein paar Unterschiede zwischen Aktionscode-Listen und Data Feeds.

| Merkmal          | Aktionscodes | Daten-Feeds   |
|------------------|-----------------|--------------|
| Beschreibungen     | Ja             | Kein:e           |
| Ablaufdaten | Ja             | Kein:e           |
| Erstellungsmethode  | Hochladen einer CSV | Text einfügen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Migrationsmethode

Um einen Daten-Feed durch eine Liste mit Aktionscodes zu ersetzen, gehen Sie wie folgt vor: 

1. Gehen Sie zu **Dateneinstellungen** und wählen Sie **Aktionscode-Liste erstellen**.
2. [Richten Sie Ihre Liste mit Aktionscodes ein]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. Navigieren Sie zu Ihren Nachrichten, die zuvor auf den Daten-Feed referenziert haben, und aktualisieren Sie sie, um die Liste der Aktionscodes zu verwenden.