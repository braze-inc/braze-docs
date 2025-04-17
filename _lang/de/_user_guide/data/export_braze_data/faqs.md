---
nav_title: FAQ
article_title: FAQ zum Exportieren
page_order: 11
page_type: FAQ
description: "Dieser Artikel behandelt einige häufig gestellte Fragen zu API- und CSV-Exporten."

---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zu API- und CSV-Exporten.

### Können Sie bestimmte Exporte in Ihrem S3-Bucket erscheinen lassen und andere nicht?

Nein. Wenn Sie S3-Anmeldedaten angegeben haben, werden alle Ihre Exporte in Ihrem S3-Bucket angezeigt. Wenn Sie keine Zugangsdaten angegeben haben, werden alle Exporte in einem S3-Bucket von Braze angezeigt.

### Muss ich S3-Anmeldedaten zu Braze hinzufügen, um Daten zu exportieren?

Nein. Wenn Sie keine S3-Anmeldedaten hinzufügen, werden Ihre Exporte in einem S3-Bucket angezeigt, das Braze gehört.

### Was passiert, wenn Sie S3-Anmeldedaten im Dashboard einrichten, aber nicht "Dies zum Standardziel für den Datenexport machen" auswählen?

Das Kontrollkästchen **Dies zum Standardziel für den Datenexport machen** hat Einfluss darauf, ob die Exporte an S3 oder Azure gehen, vorausgesetzt, Sie haben Zugangsdaten für beide hinzugefügt.

### Warum habe ich beim Exportieren von Benutzerprofilen in S3 mehrere Dateien erhalten?

Dies ist das erwartete Verhalten für Arbeitsbereiche mit vielen Benutzern. Braze teilt Ihren Export in mehrere Dateien auf, basierend auf der Anzahl der Nutzer:innen in Ihrem Workspace. In der Regel wird eine Datei pro 5.000 Nutzer:innen ausgegeben. Beachten Sie, dass Sie, wenn Sie ein kleines Segment innerhalb eines großen Workspace exportieren, möglicherweise mehrere Dateien erhalten.

### Warum sehe ich Duplikate, wenn ich Nutzer:innen über die REST API nach Segmenten exportiere?

Dies ist ein sehr seltenes Vorkommen, das durch die zugrunde liegende Architektur des Datenbankanbieters verursacht wird. Duplikate werden jede Woche bereinigt. In den meisten Wochen werden jedoch keine Duplikate bereinigt.
