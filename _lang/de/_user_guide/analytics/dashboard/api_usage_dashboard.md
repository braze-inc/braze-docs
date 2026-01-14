---
nav_title: Dashboard zur API-Nutzung
article_title: Dashboard zur API-Nutzung
alias: "/api_usage/"
page_order: 3.5
description: "Dieser Artikel bietet eine Übersicht über das Dashboard zur API-Nutzung."
---

# Dashboard für die API-Nutzung

> Mit dem Dashboard zur API-Nutzung können Sie den bei Braze eingehenden REST API-Verkehr überwachen, um Trends bei der Nutzung unserer REST APIs zu erkennen und mögliche Probleme zu beheben.

## Über das Dashboard zur API-Nutzung

Um Ihr Dashboard zur API-Nutzung einzusehen, gehen Sie zu **Einstellungen** > **APIs und Bezeichner** und wählen Sie dann **Dashboard**.

Das Standard Dashboard ist eine Ansicht aller eingehenden REST API Anfragen für Ihren Workspace im Laufe des letzten Tages (24 Stunden). Je nach Anwendungsfall können Sie die Steuerelemente des Dashboards anpassen, um den Datenverkehr zu filtern oder zu gruppieren und auch den Zeitbereich des Dashboards zu konfigurieren.

\![API Usage Dashboard mit 130 Anfragen insgesamt, mit einer Erfolgsquote von 70 Prozent und einer Fehlerquote von 30 Prozent.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Verfügbare Metriken

Das Dashboard zur API-Nutzung enthält die folgenden Statistiken:

| Metrisch         | Beschreibung |
|----------------|-------------|
| Anfragen gesamt | Die Gesamtzahl der Anfragen, die für Ihren aktuellen Workspace an Braze gesendet wurden, unter Berücksichtigung der auf das Dashboard angewendeten Filter und Kontrollen. |
| Erfolgsrate   | Der prozentuale Anteil aller Anfragen, bei denen Braze eine `2XX` Erfolgsmeldung ausgegeben hat. |
| Fehlerrate     | Der Prozentsatz der gesamten Anfragen, bei denen Braze eine `4XX` oder `5XX` Fehlerantwort ausgab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Verwendung des Dashboards

\![Filter, die Sie auf das Dashboard anwenden können, einschließlich: API-Schlüssel, Endpunkt, Antwort-Codes, Gruppendaten und Datum.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filter

Wählen Sie **Filter** aus, um die Ansicht des REST API-Verkehrs für Ihren Workspace einzuschränken, einschließlich:

- API-Schlüssel
- Endpunkt
- Antwortcode

### Gruppendaten

Sie können Daten in verschiedenen Datenreihen gruppieren, um verschiedene Muster in Ihrer Nutzung zu untersuchen, einschließlich:

- Antwort-Codes (Standard)
- API-Endpunkt
- API-Schlüssel
- Nur Erfolge und Misserfolge

### Datum

Passen Sie den Datumsfilter an, um je nach Bedarf einen kleineren oder größeren Zeitbereich anzuzeigen. Dies beinhaltet:

- Heute (Standard)
- Angepasst
- Letzte 3 Stunden
- Letzte 6 Stunden
- Letzte 12 Stunden
- Letzte 24 Stunden
- Gestern
- Letzte 7 Tage
- Letzte 14 Tage
- Letzte 30 Tage
- Letzter Monat bis Datum

{% alert note %}
Die Optionen **Letzte 3 Stunden** und **Letzte 6 Stunden** zeigen den Verkehr nach Minuten an. Größere Zeiträume zeigen den Verkehr alle fünf Minuten, Stunden oder Tage an.
{% endalert %}

## Überlegungen

Das Dashboard zur API-Nutzung enthält alle REST API-Anfragen, die Braze erhalten hat und für die eine `2XX`, `4XX`, oder `5XX` Antwort zurückgegeben wurde. Dazu gehören die Ausgaben der Datentransformation und die Synchronisierung der Datenaufnahme in der Cloud. SDK-Traffic und Nutzer:innen-Updates sind in diesem Dashboard nicht enthalten.

Die auf dem Dashboard angezeigten Daten können bis zu einer kurzen Verzögerung bei der Anzeige des aktuellen Datenverkehrs aufweisen. In Zeiten hoher Nutzung können Sie das Dashboard bis zu 4 Mal pro Minute aktualisieren. Möglicherweise müssen Sie ein paar Minuten warten, bevor Sie das Dashboard erneut aktualisieren können.
