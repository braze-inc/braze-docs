---
nav_title: FAQs
article_title: Snowflake FAQ zur gemeinsamen Nutzung von Daten
page_order: 50
page_type: FAQ
description: "Dieser Artikel beantwortet häufig gestellte Fragen zur gemeinsamen Nutzung von Daten in Snowflake."

---

# Häufig gestellte Fragen

### Ist es möglich, PII-Daten über die Snowflake-Datenfreigabe zu verschleiern?
Nein, das wird zur Zeit nicht unterstützt.

### Benötige ich eine gemeinsame Nutzung von Daten für dieselbe Region oder für mehrere Regionen?
Verwenden Sie die gemeinsame Nutzung von Daten für dieselbe Region in den folgenden Szenarien:
- Ihr Snowflake-Konto befindet sich in US-EAST-1 (AWS) und Ihr Braze-Dashboard befindet sich in den USA.
- Ihre Snowflake-Region liegt in EU-CENTRAL-1 und Ihre Braze-Dashboard-Region liegt in der EU.

Andernfalls nutzen Sie die gemeinsame Nutzung von Daten für eine andere Region. 

### Was soll ich mit meinen Daten machen, wenn ich zu einem neuen Snowflake Konto wechsle?
Sie können die alte Datenfreigabe, die mit Ihrem alten Snowflake-Konto verbunden ist, löschen und dann eine neue Freigabe für das neue Konto erstellen. Alle historischen Daten werden in der neuen Aktie verfügbar sein. 

### Warum sehe ich keine Daten in meiner Datenfreigabe?
Sie haben bei der Erstellung Ihrer Datenfreigabe möglicherweise die falsche Snowflake Konto ID verwendet. Die Konto ID auf dem Dashboard für die gemeinsame Nutzung von Daten muss mit der Ausgabe von `CURRENT_ACCOUNT()` von Ihrem Snowflake Konto übereinstimmen.

Wenn Ihre Aktie regionsübergreifend ist, sind die Daten möglicherweise nicht sofort verfügbar. Je nach Datenvolumen kann es ein paar Stunden dauern, bis die Daten mit Ihrer Region synchronisiert sind.

### Warum erhalte ich eine Fehlermeldung zur Einhaltung des US-Gesetzes zum Schutz medizinischer Daten (HIPAA), wenn ich eine Datenfreigabe erstelle?

Das angegebene Konto entspricht entweder nicht dem US-Gesetz zum Schutz medizinischer Daten (HIPAA) oder verfügt über [Snowflake Editionen](https://docs.snowflake.com/en/user-guide/intro-editions) unterhalb von Business Critical. Ihr Snowflake-Konto muss auf die Business Critical Edition upgegradet werden, damit die gemeinsame Nutzung von Daten dem US-Gesetz zum Schutz medizinischer Daten (HIPAA) entspricht. Wenden Sie sich an den Snowflake-Support, wenn Sie weitere Unterstützung beim Upgraden Ihres Kontos benötigen.

### Warum kann ich eine Datenfreigabe nicht wiederherstellen, nachdem ich sie gelöscht habe?

Es kann sein, dass das System die Löschung Ihrer bisherigen Daten noch nicht abgeschlossen hat. Warten Sie ein paar Minuten, bis die Deprovisionierung abgeschlossen ist, und versuchen Sie dann erneut, die neue Datenfreigabe zu erstellen.


