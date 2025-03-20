---
nav_title: FAQ
article_title: Standorte und Geofences – FAQ
page_order: 4
page_type: FAQ
description: "Dieser Referenzartikel behandelt einige häufig gestellte Fragen rund um die Verwendung von Standort-Tracking und Geofences."
tool: Location

---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zu Standorten und Geofences.

## Standort-Tracking

### Wann sammelt Braze Standortdaten?

Braze sammelt den Standort nur, wenn die Anwendung im Vordergrund geöffnet ist. Daher zielt unser `Most Recent Location`-Filter auf Nutzer:innen ab, die die Anwendung zuletzt geöffnet haben (auch als Sitzungsbeginn bezeichnet).

Sie sollten auch die folgenden Nuancen beachten:

- Wenn der Standort deaktiviert ist, zeigt der `Most Recent Location`-Filter den zuletzt aufgenommenen Standort an.
- Wenn ein Nutzer jemals einen Standort in seinem Profil gespeichert hat, fällt er unter den `Location Available` Filter, auch wenn er die Standortverfolgung seitdem abgelehnt hat.

### Was ist der Unterschied zwischen den Filtern „Aktuellstes Gebietsschema des Geräts“ und „Letzter Standort“?

Der Filter `Most Recent Device Locale` stammt aus den Geräteeinstellungen des Nutzers oder der Nutzerin. Bei iPhone-Benutzern erscheint dies zum Beispiel auf dem Gerät unter **Einstellungen** > **Allgemein** > **Sprache & Region**. Dieser Filter wird verwendet, um sprachliche und regionale Formatierungen zu erfassen, wie z. B. Datumsangaben und Adressen, und ist unabhängig vom `Most Recent Location`-Filter.

Die `Most Recent Location` ist der letzte bekannte GPS-Standort des Geräts. Dieser Filter wird beim Start der Sitzung aktualisiert und im Profil es Nutzers oder der Nutzerin gespeichert.

### Werden die alten Standortdaten von Braze entfernt, wenn ein Benutzer die Standortverfolgung abbestellt?

Nein! Wenn ein Nutzer jemals einen Standort in seinem Profil gespeichert hat, werden diese Daten nicht automatisch entfernt, wenn er später die Standortverfolgung abbestellt.

## Geofences

### Was ist der Unterschied zwischen Geofences und Standortverfolgung?

In Braze ist ein Geofence ein anderes Konzept als das Standort-Tracking. Geofences werden als Auslöser für bestimmte Aktionen verwendet. Ein Geofence ist eine virtuelle Grenze, die um einen geografischen Standort herum eingerichtet wird. Wenn ein:e Nutzer:in diese Grenze überschreitet oder verlässt, kann dies eine bestimmte Aktion auslösen, z. B. das Senden einer Nachricht.

Das Standort-Tracking wird verwendet, um die letzten Standortdaten eines Nutzers oder einer Nutzerin zu erfassen und zu speichern. Diese Daten können verwendet werden, um Nutzer:innen auf der Grundlage des `Most Recent Location`-Filters zu segmentieren. Sie können zum Beispiel den `Most Recent Location`-Filter verwenden, um eine bestimmte Region Ihres Publikums anzusprechen, z. B. um eine Nachricht an Nutzer:innen in New York zu senden.

### Wie genau sind die Geofences von Braze?

Die Geofences von Braze verwenden eine Kombination aller für ein Gerät verfügbaren Standortanbieter, um den Standort des Nutzers oder der Nutzerin dreidimensional zu bestimmen. Dazu gehören Wi-Fi, GPS und Mobilfunktürme.

Die typische Genauigkeit liegt im Bereich von 20–50 m, die beste Genauigkeit liegt im Bereich von 5–10 m. In ländlichen Gebieten kann sich die Genauigkeit erheblich verschlechtern, möglicherweise bis zu mehreren Kilometern. Braze empfiehlt, in ländlichen Gegenden Geofences mit größeren Radien anzulegen.

Weitere Informationen über die Genauigkeit von Geofences finden Sie in der Dokumentation [für Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) und [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### Wie wirken sich Geofences auf die Akkulaufzeit aus?

Unsere Geofencing-Lösung nutzt den nativen Geofence-Systemdienst auf iOS und Android und ist so abgestimmt, dass ein intelligenter Kompromiss zwischen Genauigkeit und Stromverbrauch gefunden wird, der eine erstklassige Akkulaufzeit und eine Verbesserung der Leistung gewährleistet, wenn sich der zugrunde liegende Dienst verbessert.

### Wann sind Geofences aktiv?

Die Geofences von Braze funktionieren zu jeder Tageszeit, auch wenn Ihre App geschlossen ist. Sie werden aktiv, sobald sie definiert und in das Braze-Dashboard hochgeladen wurden. Geofences können jedoch nicht funktionieren, wenn ein:e Nutzer:in das Standort-Tracking deaktiviert hat.

Damit Geofences funktionieren, müssen die Nutzer die Standortdienste auf ihrem Gerät aktiviert haben und Ihrer App die Erlaubnis zum Zugriff auf ihren Standort erteilt haben. Wenn ein Benutzer die Standortverfolgung deaktiviert hat, kann Ihre App nicht erkennen, wann er einen Geofence betritt oder verlässt.

### Werden Geofence-Daten in Benutzerprofilen gespeichert?

Nein, Braze speichert keine Geofence-Daten in Benutzerprofilen. Geofences werden von den Standortdiensten von Apple und Google überwacht, und Braze wird nur benachrichtigt, wenn ein Benutzer einen Geofence auslöst. Zu diesem Zeitpunkt verarbeiten wir alle damit verbundenen Trigger-Kampagnen.

### Kann ich einen Geofence innerhalb eines Geofence einrichten?

Vermeiden Sie es, Geofences ineinander einzurichten, da dies zu Problemen bei der Auslösung von Benachrichtigungen führen kann.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
