---
nav_title: FAQ
article_title: Häufig gestellte Fragen zur Verwaltung benutzerdefinierter Daten
page_order: 1
page_type: FAQ
description: "Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zur Verwaltung benutzerdefinierter Daten in Braze."
---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zur Verwaltung benutzerdefinierter Daten.

### Warum wird mein benutzerdefiniertes Attribut in der Produktion als anderer Datentyp erkannt als in der Entwicklung?

Braze erkennt automatisch den Datentyp eines benutzerdefinierten Attributs anhand des ersten Werts, den es empfängt. Wenn Ihre Entwicklungsumgebung zunächst einen numerischen`100` Wert sendet, wird das Attribut als Zahl gespeichert. Wenn der erste Wert Ihrer Produktionsumgebung als String (z. B. in `"100"`Anführungszeichen eingeschlossen) vorliegt, wird das Attribut als String gespeichert.

Um dies zu verhindern, stellen Sie bitte sicher, dass Ihre Integration in allen Umgebungen konsistente Datentypen sendet. Sollte bereits ein falscher Typ eingestellt sein, können Sie den korrekten Datentyp unter **„Dateneinstellungen** > **Benutzerdefinierte Attribute“** über das [Dropdown-Menü „Datentyp“]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#forcing-data-type-comparisons) festlegen.

### Wenn ich eine Änderung des Datentyps für ein angepasstes Attribut erzwinge, werden dann die vorhandenen Daten konvertiert?

Nein. Das Erzwingen einer Änderung des Datentyps wirkt sich nur auf neue Daten aus, die in Braze eingehen. Alle Daten, die vor der Typänderung erfasst wurden, werden weiterhin als alter Typ gespeichert und können möglicherweise nicht mit den Filtern des neuen Typs segmentiert werden. Auf den Nutzerprofilen der betroffenen Nutzer:innen wird eine Warnung angezeigt. Bei neuen eingehenden Daten kann Braze Werte, die nicht mit dem erzwungenen Typ übereinstimmen, in den erzwungenen Typ umwandeln (z. B. eine Zeichenfolge`"100"`in eine Zahl`100`). Werte, die nicht umgewandelt werden können, werden ignoriert und führen nicht zu einem Update des Attributs.

Wenn Sie möchten, dass alle vorhandenen Nutzerdaten mit dem neuen Typ übereinstimmen, müssen Sie die Attributwerte für diese Nutzer:innen über das SDK, die API oder einen CSV-Import erneut senden. Es gibt keine automatische Konversion für vorhandene Daten.

### Wie kann ich Probleme mit Datentypen bei der Verwendung von Cloud Datenaufnahme (CDI) vermeiden?

Wenn Sie CDI zur Synchronisierung von Daten aus externen Quellen (wie Databricks oder Snowflake) verwenden, stellen Sie bitte sicher, dass Ihre Quellspalten die korrekten Datentypen verwenden, bevor Sie die Synchronisierung durchführen. Häufige Probleme sind:

- **Als String gespeicherte Zeitstempel**: Bitte stellen Sie sicher, dass Ihre Datumsspalten in Ihrer Quelldatenbank einen Zeitstempel oder Datums-/Uhrzeit-Typ verwenden und keinen Varchar- oder String-Typ.
- **Als String gespeicherte Zahlen**: Konvertieren Sie numerische Spalten in Ihrer Quellabfrage vor der Synchronisierung in Ganzzahl- oder Gleitkommazahl-Typen.
- **Inkonsistente Typen bei Synchronisierungen**: Sollte sich der Spaltentyp zwischen den Synchronisierungen ändern, kann es vorkommen, dass Braze die neuen Daten ablehnt. Bitte überprüfen Sie, ob Ihr Quellschema konsistent bleibt.
