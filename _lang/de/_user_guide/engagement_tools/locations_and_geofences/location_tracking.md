---
nav_title: Standortverfolgung
article_title: Standortverfolgung
page_order: 0
page_type: reference
description: "In diesem Referenzartikel wird erklärt, wie Sie das Standort-Tracking in Ihren Apps verwenden können und welche Partner das Standort-Tracking unterstützen."
tool: Location
search_rank: 2
---

# Standort-Tracking

> Die Standorterfassung erfasst anhand von GPS-Standortdaten den letzten Standort des Benutzers, als die App geöffnet wurde. Sie können diese Informationen verwenden, um Daten auf der Grundlage von Nutzer:innen zu segmentieren, die sich an einem bestimmten Standort aufgehalten haben.

## Aktivieren des Standort-Trackings

Um die Erfassung von Standorten in Ihrer App zu aktivieren, lesen Sie das Handbuch für Entwickler:innen für die von Ihnen verwendete Plattform:

- [iOS][2]
- [Android][3]
- [Internet][4]

Im Allgemeinen verwenden mobile Apps den GPS-Chip des Geräts und andere Systeme (wie z. B. Wi-Fi-Scanning), um den Standort des Benutzers zu ermitteln. Web-Apps werden WPS (Wi-Fi Positioning System) verwenden, um den Standort eines Nutzers oder einer Nutzerin zu verfolgen. Bei all diesen Plattformen müssen die Nutzer der Standortverfolgung zustimmen. Die Genauigkeit Ihrer Standortverfolgungsdaten kann davon abhängen, ob Ihre Nutzer Wi-Fi auf ihren Geräten aktiviert haben oder nicht. Android-Benutzer können auch verschiedene Standortmodi wählen - Benutzer, die sich im "Batteriesparmodus" oder "Nur Gerät" befinden, haben möglicherweise ungenaue Daten.

### SDK-Benutzerstandort nach IP-Adresse

Ab dem 26\. November 2024 wird Braze die Standorte der Nutzer:innen anhand der IP-Adresse ab dem Beginn der ersten SDK-Sitzung ermitteln. 

Zuvor verwendete Braze bei der Erstellung von SDK-Nutzern:innen und für die Dauer der ersten Sitzung den Code des Geräts. Erst nach der Verarbeitung des ersten Sitzungsbeginns würde die IP-Adresse verwendet, um das zuverlässigere Land für den oder die Nutzer:in festzulegen. Dies bedeutete, dass das Land des Nutzers oder der Nutzerin erst ab der zweiten Sitzung mit größerer Genauigkeit festgelegt wurde, nachdem der erste Sitzungsbeginn verarbeitet worden war.

Jetzt verwendet Braze die IP-Adresse, um den Länderwert in Nutzerprofilen festzulegen, die über das SDK erstellt wurden, und diese IP-basierte Ländereinstellung ist während und nach der ersten Sitzung verfügbar.

## Standort-Targeting

Mit Standort-Tracking Daten und Segmenten können Sie standortbezogene Kampagnen und Strategien einrichten. So können Sie beispielsweise eine Werbekampagne für Nutzer durchführen, die in einer bestimmten Region leben, oder Nutzer in einer Region mit strengeren Vorschriften ausschließen.

Weitere Informationen zur Erstellung eines Standortsegments finden Sie unter [Standort-Targeting][1].

## Feste Einstellung des Standardattributs für den Standort

Sie können auch den [Endpunkt`users/track` ][8] in unserer API verwenden, um das [`current_location`][9]-Standard-Attribut zu aktualisieren. Ein Beispiel ist:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Partnerschaftsunterstützung für Beacon und Geofence

Wenn Sie bestehende Beacon- oder Geofence-Unterstützung mit unseren Targeting- und Nachrichtenfunktionen kombinieren, erhalten Sie mehr Informationen über die physischen Aktionen Ihrer Nutzer, so dass Sie ihnen entsprechende Nachrichten senden können. Sie können das Standort-Tracking mit einigen unserer Partner nutzen: 

- [Radar][6]
- [Infillion][10]
- [Foursquare][7]

## Häufig gestellte Fragen

Antworten auf häufig gestellte Fragen zu den [Standorten][11] finden Sie in unseren [FAQ zu den Standorten][11].

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/message_personalization/location/infillion/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations
