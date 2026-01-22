---
nav_title: Analytics
article_title: "Analytics für Artikel-Empfehlungen"
description: "Erfahren Sie mehr über Analytics für Artikel-Empfehlungen und wie Sie diese in Braze anzeigen können."
page_order: 1.3
---

# Analytics für Artikel-Empfehlungen

> Erfahren Sie mehr über Analytics für Artikel-Empfehlungen und wie Sie diese in Braze anzeigen können.

## Analytik anzeigen

Sie können die Analysen für Ihre Empfehlungen einsehen, um zu sehen, welche Artikel Benutzern empfohlen wurden und wie genau das Empfehlungsmodell war.

1. Gehen Sie zu **Analytics** > **Artikel-Empfehlung**.
2. Wählen Sie Ihre Empfehlung aus der Liste aus.

## Verfügbare Metriken

### Zielgruppe

Dies sind Metriken, die sich auf Ihre Zielgruppe beziehen. Dazu gehören Präzision, Reichweite und Art der Empfehlung.

Die Metriken für die Zielgruppe der Empfehlungen zeigen die Genauigkeit (25,3%), die Abdeckung (54,3%) und die Aufteilung der Empfehlungstypen in personalisierte und beliebteste Artikel.]({% image_buster /assets/img/item_recs_analytics_1.png %})

Weitere Informationen finden Sie in der folgenden Tabelle:

| Metrisch              | Beschreibung |
| ------------------- | ---------- |
| **Präzision**           | Der Prozentsatz der Zeit, in der das Modell den nächsten Artikel, den ein Benutzer gekauft hat, richtig erraten hat. Die Genauigkeit hängt stark von Ihrer spezifischen Kataloggröße und -mischung ab und sollte als Richtwert dienen, um zu verstehen, wie oft das Modell korrekt ist.<br><br>Bei Tests haben wir festgestellt, dass Modelle mit einer Genauigkeit von 6–20% am besten abschneiden. Diese Metrik wird aktualisiert, wenn das Modell das nächste Mal neu trainiert wird.  |
| **Abdeckung**            | Wie viel Prozent der verfügbaren Artikel im Katalog werden mindestens einem Benutzer empfohlen. Sie können davon ausgehen, dass Sie eine höhere Artikelabdeckung mit personalisierten Artikelempfehlungen als mit den beliebtesten Artikeln erreichen. |
| **Empfehlungstyp** | Der Prozentsatz der Nutzer:innen, die personalisierte oder neueste Empfehlungen erhalten, im Vergleich zum Fallback der beliebtesten Artikel. Der Fallback wird an Benutzer gesendet, die nicht über genügend Daten verfügen, um eine personalisierte oder aktuelle Empfehlung zu erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Artikel

Diese Tabelle enthält Metriken zu Ihren personalisierten, neuesten und beliebtesten Artikeln aus Ihrem Katalog.

\![Nebeneinander angeordnete Tabellen mit den den Nutzer:innen zugewiesenen Artikeln, getrennt nach personalisierten Empfehlungen und beliebtesten Empfehlungen.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Weitere Informationen finden Sie in der folgenden Tabelle:

| Metrisch              | Beschreibung |
| ------------------- | ---------- |
| **Personalisierte Artikel**<br><br>**Letzte Artikel** | Diese Spalte listet jeden Artikel im Katalog in absteigender Reihenfolge der am häufigsten empfohlenen Artikel auf. In dieser Spalte sehen Sie auch, wie viele Benutzer den einzelnen Artikeln durch das Modell zugeordnet wurden.<br><br>Je nach [Art der Empfehlung]({{site.baseurl}}/user_guide/brazeai/recommendations/) werden entweder **personalisierte** Artikel oder **die neuesten** Artikel aufgelistet. |
| **Beliebteste Artikel** | Diese Spalte listet jeden Artikel im Katalog in absteigender Reihenfolge seiner Beliebtheit auf. Beliebtheit bezieht sich hier auf die Objekte im Katalog, mit denen Benutzer im gesamten Arbeitsbereich am häufigsten interagieren. Beliebteste wird als Ausweichlösung verwendet, wenn für einen einzelnen Benutzer keine personalisierte oder neueste Version berechnet werden kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Übersicht

Dies ist eine Übersicht über die von Ihnen gewählte Empfehlungskonfiguration, die auch angibt, wann die Empfehlung zuletzt aktualisiert wurde.

\![Übersichtstabelle für Empfehlungen, die den Typ, den Katalog, den Ereignistyp, den Namen des angepassten Events, den Namen der Eigenschaften und das Datum des letzten Updates anzeigt.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }
