---
nav_title: "RFM Segmente"
article_title: RFM SQL Segmente
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "Dieser Artikel beschreibt, wie Sie RFM Segment-Erweiterungen erstellen, die Ihre besten Nutzer:innen durch Messung ihrer Kaufgewohnheiten identifizieren."
tool: Segments
---

# RFM SQL Segmente

> Sie können eine RFM (recency, frequency, monetary) Segment-Erweiterung erstellen, um Ihre besten Nutzer:innen durch Messung ihrer Kaufgewohnheiten zu targetieren.

Die RFM-Analyse ist eine Marketing-Technik, die Ihre besten Nutzer:innen identifiziert, indem sie Nutzer:innen auf einer Skala von 0-3 für jede Kategorie (Häufigkeit, Häufigkeit, Geldwert) bewertet, wobei 3 der beste Wert und 0 der schlechteste ist. Häufigkeit, Häufigkeit und monetäre Werte basieren alle auf Daten aus einem von Ihnen gewählten Zeitraum.

## RFM-Kategorien

| Kategorie | Definition |
| --- | --- |
| Aktualität | Wie kürzlich ein Kund:in einen Kauf getätigt hat. Eine höhere Punktzahl bedeutet, dass Sie mehr Käufe getätigt haben. |
| Häufigkeit | Wie häufig ein Kund:in einen Kauf getätigt hat. Eine höhere Punktzahl bedeutet eine höhere Häufigkeit. |
| Monetärer Wert | Gesamtbetrag, den ein Kund:in ausgegeben hat. Eine höhere Punktzahl bedeutet höhere Ausgaben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Kauf-Events müssen aktiviert sein, um RFM SQL Segmente zu verwenden, da der monetäre Wert für Ihre Nutzer:innen durch den Umsatz bestimmt wird, den sie durch Braze Kauf-Events generiert haben.
{% endalert %}

## Erstellen eines RFM Segments

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
2. Wählen Sie **Neue Erweiterung**, und wählen Sie dann **Segmente für Häufigkeit, Frequenz und Geldwert (RFM)** aus.

![Modal mit der Option, ein Katalogsegment für Ereignisse, Käufe oder RFM-Segmente zu erstellen.]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3\. Wählen Sie im Panel **Variablen** Ihren **Zeitbereich** aus, um den Zeitraum der zu analysierenden Kaufdaten festzulegen. Sie können bis zu den letzten 60 Tagen angeben. Die Zeitspanne, die Sie auswählen, ist die Zeitspanne, aus der die Daten zum Nutzer:innen-Verhalten gezogen werden und hängt von den Zielen Ihrer Kampagne ab.

| Feld Zeitbereich | Beschreibung | Anwendungsfall |
| --- | --- | --- |
| Relativ | Geben Sie die Aktivität innerhalb der letzten X Tage an | Analysieren Sie das jüngste Verhalten der Nutzer:innen mit einem rollenden Fenster. | 
| Startdatum | Legen Sie einen festen Startpunkt für Ihre Analyse fest | Analysieren Sie die Nutzer:innen-Aktivitäten ab einem bestimmten Datum, z.B. nach dem Start einer Kampagne. |
| Enddatum | Geben Sie einen festen Endpunkt für Ihre Analyse an | Analysieren Sie die Nutzer:innen-Aktivitäten bis zu einem bestimmten Datum, z.B. vor einem Update des Produkts. |
| Datumsbereich | Geben Sie sowohl ein Start- als auch ein Enddatum für einen angepassten Zeitraum an. | Analysieren Sie das Verhalten der Nutzer:innen während eines bestimmten Zeitraums, z.B. während einer Aktion. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{: start="4"}
4\. Wählen Sie die generierten [RFM-Gruppen](#rfm-groups) aus, die Sie in Ihr Segment aufnehmen möchten. Wenn Sie mehrere Gruppen auswählen, schließt Ihr Segment Nutzer:innen ein, die zu einer der ausgewählten Gruppen gehören.

![Variablen Panel mit den ausgewählten RFM-Gruppen "Champions" und "Loyale Nutzer:innen".]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5\. Führen Sie eine Vorschau aus und speichern Sie dann Ihr Segment

{% alert note %}
Sie brauchen den SQL Code in der Vorlage nicht zu bearbeiten, um ein RFM Segment zu erstellen. Sie können ausschließlich das Panel **Variablen** verwenden, um Ihr Segment anzupassen.
{% endalert %}

### RFM-Gruppen

RFM Segmente werden in einer bestimmten Reihenfolge ausgewertet. Nutzer:innen werden dem ersten Segment zugewiesen, dessen Kriterien sie von oben nach unten in der Prioritätsliste erfüllen. Ein Nutzer:innen, der sich sowohl für "Champions" als auch für "Loyale Nutzer" qualifiziert, wird beispielsweise dem Segment "Champions" zugewiesen, da es eine höhere Priorität hat.

| RFM-Gruppe          | Segmente Beschreibung                                                                 | Rang der Aktualität (R) | Häufigkeit (F) Rang | Monetärer (M) Rang |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Champions          | Das wertvollste Segment der Nutzer:innen mit Spitzenwerten in allen Kategorien.                   | 3                | 2-3                | 2-3               |
| Loyale Nutzer:innen        | Nutzer:innen, die eine hohe Häufigkeit und Frequenz aufweisen. Kann einen geringeren Geldwert haben als Champions. | 2-3              | 2-3                | 1-3               |
| Potenzielle Loyalisten| Nutzer:innen, die in letzter Zeit mit mäßiger Häufigkeit und mäßigem Geldwert gekauft haben.   | 3                | 1-3                | 1-3               |
| Vielversprechend          | Nutzer:innen, die kürzlich einen hochwertigen Erstkauf getätigt haben, aber noch keine hohe Kauffrequenz aufweisen. | 3                | 0-3                | 1-3               |
| Neue Kund:in       | Nutzer:innen, die erst vor kurzem ihren ersten Kauf getätigt haben.                             | 3                | 0-3                | 0-3               |
| Benötigt Aufmerksamkeit  | Nutzer:innen mit überdurchschnittlicher Häufigkeit, aber unterdurchschnittlicher Kaufhäufigkeit oder unterdurchschnittlichem Geldwert. | 2-3              | 0-3                | 0-3               |
| Kann sie nicht verlieren   | Nutzer:innen, die früher einen hohen Wert mit guten Frequenz- und Geldwerten hatten, aber seit langem nicht mehr gekauft haben. | 0-1              | 2-3                | 2-3               |
| Gefährdet            | Nutzer:innen, die in der Vergangenheit mäßige Häufigkeit und Geldwerte aufwiesen, aber schon lange nicht mehr gekauft haben. | 0-1              | 1-3                | 1-3               |
| Über den Schlaf     | Nutzer:innen, die in allen Metriken niedrige Punktzahlen haben.                                       | (1 %)                | 0-3                | 0-3               |
| Winterschlaf        | Nutzer:innen, die mäßig häufig, aber über einen längeren Zeitraum inaktiv sind.    | 0                | 0-2                | 0-3               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
