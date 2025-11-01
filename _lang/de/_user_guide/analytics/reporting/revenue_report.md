---
nav_title: Bericht über die Einnahmen
article_title: Umsatzbericht
page_type: reference
description: "Auf dieser Seite wird beschrieben, wie Sie die Seite Umsatzbericht verwenden, um Daten zu den Umsätzen über bestimmte Zeiträume, zu den Umsätzen eines bestimmten Produkts und zu den Gesamteinnahmen Ihrer App anzuzeigen."
tool: Reports
---

# Umsatzbericht

> Auf der Seite Umsatzbericht können Sie Daten zum Umsatz über bestimmte Zeiträume, zum Umsatz eines bestimmten Produkts und zum Gesamtumsatz Ihrer App einsehen.

Um einen Bericht über Ihre Einnahmen auf dem Dashboard anzuzeigen, gehen Sie zu **Analytics** > **Umsatzbericht**. 

## Umsatzberichte anpassen

Sie können Ihren Umsatzbericht anpassen, indem Sie einen Datumsbereich, Apps und Parameter auswählen.

\![Die Seite "Umsatzbericht" zeigt das Diagramm "Performance im Zeitverlauf" mit dem Parameter "Umsatz".]({% image_buster /assets/img/revenue_report.png %})

### Filtern nach Datum und Apps

Wählen Sie den Datumsbereich für Ihren Umsatzbericht und, wenn Sie möchten, eine bestimmte App oder eine Auswahl von Apps.

### Filterung nach Parametern

Das Diagramm **Performance im Zeitverlauf** zeigt die Daten für verschiedene Parameter an, die Sie in der Dropdown-Liste **Statistik für** auswählen können. In der Dropdown-Liste **Aufschlüsselung** können Sie die Daten bestimmter Parameter optional aufschlüsseln.

Sie können die folgenden Daten im **Diagramm Performance im Zeitverlauf** anzeigen:
- KPI-Formeln
- Käufe
    - (Optional) Käufe nach Produkt
- Umsatz
    - (Optional) Umsatzerlös nach Segmenten
    - (fakultativ) Umsatzerlöse nach Produkten
- Umsatz pro Stunde
    - (Fakultativ) Umsatz pro Stunde nach Segmenten
- Umsatz pro Nutzer:in

## Die Umsatzberechnung

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Lifetime-Umsatz</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Lifetime-Value je Benutzer</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Durchschnittlicher Tagesumsatz</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">Tägliche Einkäufe</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Täglicher Umsatz pro Nutzer:in</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Die Produktaufschlüsselung

In der Tabelle **Aufschlüsselung der Produkte** finden Sie eine Liste der Produkte, die während des von Ihnen ausgewählten Zeitraums gekauft wurden, wie viele Produkte gekauft wurden und wie viel Umsatz jedes Produkt generiert hat.

\![Die Tabelle "Aufschlüsselung der Produkte" mit den Spalten "Produktname", "Gekauft" und "Umsatz".]({% image_buster /assets/img/revenue_report_product_breakdown.png %})


