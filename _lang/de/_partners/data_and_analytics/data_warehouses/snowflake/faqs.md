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
- Ihre Snowflake-Region befindet sich in AP-Southeast-2 (AWS) und Ihre Braze-Dashboard-Region ist in Australien.
- Ihre Snowflake-Region befindet sich in AP-Südost-3 (AWS) und Ihre Braze-Dashboard-Region in Indonesien.

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

### Wie oft muss ich `CREATE DATABASE` ausführen, wenn ich mehrere Workspaces habe, die Daten für dasselbe Snowflake-Konto freigeben?

Sie müssen `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` nur einmal ausführen. Wenn mehrere Datenfreigaben aus verschiedenen Braze Workspaces für dasselbe Snowflake-Konto freigegeben werden, werden sie automatisch in derselben Freigabe zusammengefasst. Nachdem Sie die erste Datenbank erstellt haben, werden Daten aus zusätzlichen Workspaces automatisch zur bestehenden Datenbank hinzugefügt, ohne dass zusätzliche Anfragen zur gemeinsamen Nutzung oder Schritte zur Erstellung der Datenbank erforderlich sind.

Wenn Sie beispielsweise eine Datenfreigabe für Snowflake Konto 123 von Workspace A aus erstellen, akzeptieren Sie die Anfrage zur Freigabe und erstellen eine Datenbank. Wenn Sie später eine Datenfreigabe für dasselbe Snowflake Konto 123 von Workspace B aus erstellen, wird keine neue Anfrage zur Freigabe gesendet - die Daten werden sofort zur bestehenden Freigabe hinzugefügt und sind in der zuvor erstellten Datenbank verfügbar.

### Wenn ich mehrere Workspaces habe, enthält dann eine einzige Datenbank die Daten aller dieser Workspaces?

Ja Wenn Sie Daten aus mehreren Braze Workspaces für dasselbe Snowflake-Konto freigeben, werden alle Daten in einer einzigen Freigabe zusammengefasst und sind in derselben Datenbank verfügbar. Sie können die Daten nach `app_group_id` filtern, um zwischen Workspaces zu unterscheiden.

Filtern Sie in Ihren Abfragen am besten immer nach `app_group_id`, um sie zukunftssicher zu machen. Dadurch wird sichergestellt, dass Ihre Dashboards und Berichte korrekt bleiben, wenn Sie in Zukunft weitere Workspaces hinzufügen. Ohne diesen Filter enthalten Ihre Metriken möglicherweise unerwartet Daten aus neu hinzugefügten Workspaces.

### Welche Vorgehensweise wird für die Verwaltung von Daten aus mehreren Workspaces in Snowflake empfohlen?

Senden Sie alle Daten von Braze in dieselbe Datenbank und filtern Sie nach `app_group_id`, um zwischen Workspaces zu unterscheiden. Dieser Ansatz vereinfacht die Datenverwaltung und gewährleistet eine konsistente Berichterstattung in Ihrem Unternehmen.

### Wie viele Snowflake Konnektoren für die gemeinsame Nutzung von Daten benötige ich für mehrere Workspaces?

Die Anzahl der Konnektoren, die Sie benötigen, hängt von Ihrer spezifischen Konfiguration und Ihren Berechtigungen ab. Kontaktieren Sie Ihr Braze-Konto Team, um mehr darüber zu erfahren, welche Berechtigungen für Ihren Anwendungsfall geeignet sind.


