---
nav_title: Mobile Integrationen
article_title: Geofence Mobile Integrationen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die notwendigen mobilen Integrationen, die bei der Verwendung von Geofences erforderlich sind."
tool: Location

---

# Mobile Integrationen

> Dieser Referenzartikel behandelt die notwendigen mobilen Integrationen, die bei der Verwendung von Geofences erforderlich sind.

## Plattformübergreifende Anforderungen

Geofence-ausgelöste Kampagnen sind auf iOS und Android verfügbar. Um Geofencing zu unterstützen, muss Folgendes vorhanden sein:

1. Ihre Integration muss Push-Benachrichtigungen im Hintergrund unterstützen.
2. Braze Geofences oder die Standorterfassung müssen aktiviert sein.
3. Bei Geräten mit iOS Version 11 und höher muss der Benutzer den Standortzugriff immer zulassen, damit Geofencing funktioniert.

{% alert important %}
Ab Braze SDK Version 3.6.0 ist die Sammlung von Braze-Standorten standardmäßig deaktiviert. Um zu überprüfen, ob die Funktion unter Android aktiviert ist, vergewissern Sie sich, dass `com_braze_enable_location_collection` auf `true` in Ihrem `braze.xml` eingestellt ist.
{% endalert %}

## Geofence-Konfiguration

### Breitengrad und Längengrad

Der geographische Mittelpunkt des Geofence.

### Radius

Der Radius des Geofence in Metern, gemessen vom geografischen Zentrum. Wir empfehlen, für alle GeoFences einen Mindestradius von 100-150 Metern festzulegen.

In diesen Leitfäden finden Sie weitere Anleitungen für Ihre Plattform:
- [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence)
- [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5)

### Cooldown

Nutzer:innen erhalten durch Geofence getriggerte Benachrichtigungen, nachdem sie einzelne Geofences betreten oder verlassen haben. Nachdem ein Übergang stattgefunden hat, gibt es eine vordefinierte Zeitspanne, in der der Nutzer:innen denselben Übergang auf diesem individuellen Geofence nicht noch einmal durchführen darf. Diese Zeit wird als „Cooldown“ bezeichnet und ist von Braze vordefiniert. Der Hauptzweck besteht darin, unnötige Anfragen an das Netzwerk zu verhindern.

### Technologie-Partner

Sie können Geofences auch mit einigen unserer Partner nutzen, zum Beispiel: 

- [Radar][12]
- [Foursquare][13]

## Häufig gestellte Fragen

Besuchen Sie unsere [Geofence – FAQ][5] für Antworten auf häufig gestellte Fragen zu Geofences.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
[12]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[13]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/

