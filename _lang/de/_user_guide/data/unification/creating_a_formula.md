---
nav_title: Eine Formel erstellen
article_title: Eine Formel erstellen
page_order: 1.2
page_type: reference
description: "Dieser referenzierte Artikel behandelt das Erstellen und Verwalten von Formeln, mit denen Sie komplexe Beziehungen in Ihren Daten leicht verstehen können."
tool: Reports

---
# Eine Formel erstellen

> Bei der Anzeige von Analytics in Braze können Sie mehrere Datenpunkte kombinieren, um wertvolle Insights zu Ihren Nutzerdaten zu erhalten. Diese werden als Formeln bezeichnet. Verwenden Sie Formeln, um Ihre Zeitreihendaten auf der Grundlage der Gesamtzahl der monatlich aktiven Nutzer:in (MAU) und der täglich aktiven Nutzer:in (DAU) zu normalisieren. 

Formeln helfen Ihnen, komplexe Beziehungen in Ihren Daten zu verstehen. Sie können zum Beispiel vergleichen, wie viele angepasste Events von täglich aktiven Nutzer:innen, die sich für ein bestimmtes Segment qualifizieren, im Vergleich zur Allgemeinbevölkerung (oder zu einem anderen Segment) abgeschlossen wurden.

## Anwendungsfälle

Formeln, insbesondere in Kombination mit angepassten Events, können Ihnen helfen, das Nutzerverhalten innerhalb Ihrer App zu verstehen. Formeln können auch tiefere Insights in das Kaufverhalten von Segmenten geben, selbst wenn Ihr Unternehmen kostenpflichtige Medien in Verbindung mit Braze verwendet, wie z. B. Google Ads oder TV. 

Im Folgenden finden Sie einige Beispiele für die Arten von Verhaltensmustern, die mit Formeln erkannt werden können:

- **Mitfahr-Apps:** Wenn Sie ein benutzerdefiniertes Ereignis für den Fall haben, dass ein Benutzer eine Fahrt storniert, können Sie eine Funktion für stornierte Fahrten / DAU konfigurieren, um herauszufinden, ob bestimmte Benutzersegmente dazu neigen, mehr Fahrten zu stornieren als andere.
- **E-Commerce Apps:** Indem Sie eine Funktion für Käufe einer bestimmten Produkt ID / MAU konfigurieren, können Sie die Beliebtheit eines kürzlich beworbenen Produkts zwischen Segmenten vergleichen, auch wenn nicht alle Aktionen mit Braze getrackt werden konnten.
- **Medien-Apps mit Anzeigen:** Wenn das Nutzererlebnis durch Werbung zwischen Video- oder Audioclips unterbrochen wird, kann die Aufzeichnung von Mid-Ad Exits als angepasstes Event und die Berechnung des Verhältnisses von Mid-Ad Exits / DAU dabei helfen, die besten Segmente für das Targeting einer Kampagne für werbefreie Premium-Abos zu finden.

## Formeln erstellen

Auf die Formeln können Sie in den Statistik-Panels auf den Seiten [Home]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/), [Umsatzbericht]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) und [Bericht über angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) im Dashboard zugreifen. Um dieses Panel anzuzeigen, gehen Sie zum Chart **Performance im Zeitverlauf**, ändern Sie die Dropdown-Liste **Statistik für** in **KPI-Formeln** und wählen Sie dann mindestens eine KPI-Formel aus, um das Chart zu füllen.

![Statistik für KPI-Formeln im Braze-Dashboard anzeigen]({% image_buster /assets/img_archive/kpi_forms.png %})

So erstellen Sie eine neue Formel:

1. Rufen Sie das entsprechende Dashboard auf**(Home**, **Umsatzbericht** oder **Bericht über angepasste Events**).
2. Wählen Sie **KPI-Formeln verwalten**.
3. Geben Sie einen Namen für Ihre Formel ein.
4. Wählen Sie die entsprechenden Zähler und Nenner aus.
5. Wählen Sie **Speichern**.

## Verfügbare Zähler und Nenner

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Übersicht Dashboard

| Zähler | Nenner |
| --- | --- |
| DAU | MAU |
| Sitzungen | DAU |
| | Segmente Größe |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Umsatz-Dashboard

| Zähler | Nenner |
| --- | --- |
| Einkäufe (alle) | DAU |
| Einkäufe auswählen (z.B. eine Geschenkkarte oder eine Produkt ID) | MAU |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Angepasstes Event-Dashboard

| Zähler | Nenner |
| --- | --- |
| Anzahl angepasster Events | MAU |
|  | DAU |
|  | Segmentgröße (nur Segmente, für die [Analytics Tracking]({{site.baseurl}}/viewing_and_understanding_segment_data/) aktiviert ist, können verwendet werden) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

