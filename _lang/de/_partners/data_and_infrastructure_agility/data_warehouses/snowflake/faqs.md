---
nav_title: FAQs
article_title: FAQs zur Snowflake-Datenfreigabe
page_order: 50
page_type: FAQ
description: "Dieser Artikel beantwortet häufig gestellte Fragen zur gemeinsamen Nutzung von Snowflake-Daten."

---

# Häufig gestellte Fragen

### Ist es möglich, PII-Daten über Snowflake Data Sharing zu verschleiern?
Nein, das wird zur Zeit nicht unterstützt.

### Benötige ich eine Datenfreigabe für dieselbe Region oder für eine andere Region?
Verwenden Sie die gemeinsame Nutzung von Daten für dieselbe Region in den folgenden Szenarien:
- Ihr Snowflake-Konto befindet sich in US-EAST-1 (AWS) und Ihre Braze Dashboard-Region befindet sich in den USA.
- Ihre Snowflake-Region liegt in EU-CENTRAL-1 und Ihre Braze Dashboard-Region liegt in der EU.

Andernfalls nutzen Sie die gemeinsame Nutzung von Daten für eine andere Region. 

### Was soll ich mit meiner Datenfreigabe machen, wenn ich zu einem neuen Snowflake-Konto wechsle?
Sie können die alte Datenfreigabe, die mit Ihrem alten Snowflake-Konto verbunden ist, löschen und dann eine neue Freigabe für das neue Konto erstellen. Alle historischen Daten werden in der neuen Aktie verfügbar sein. 

### Warum sehe ich keine Daten in meiner Datenfreigabe?
Sie haben bei der Erstellung Ihrer Datenfreigabe möglicherweise die falsche Snowflake-Konto-ID verwendet. Die Konto-ID auf dem Dashboard für die gemeinsame Nutzung von Daten muss mit der Ausgabe von `CURRENT_ACCOUNT()` von Ihrem Snowflake-Konto übereinstimmen.

Wenn Ihre Aktie regionsübergreifend ist, sind die Daten möglicherweise nicht sofort verfügbar. Je nach Datenvolumen kann es ein paar Stunden dauern, bis die Daten mit Ihrer Region synchronisiert sind.


