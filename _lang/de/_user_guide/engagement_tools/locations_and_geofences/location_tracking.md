---
nav_title: Standort-Tracking
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

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Internet]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

Im Allgemeinen verwenden mobile Apps den GPS-Chip des Geräts und andere Systeme (wie z. B. Wi-Fi-Scanning), um den Standort des Benutzers zu ermitteln. Web-Apps werden WPS (Wi-Fi Positioning System) verwenden, um den Standort eines Nutzers oder einer Nutzerin zu verfolgen. Bei all diesen Plattformen müssen die Nutzer der Standortverfolgung zustimmen. Die Genauigkeit Ihrer Standortverfolgungsdaten kann davon abhängen, ob Ihre Nutzer Wi-Fi auf ihren Geräten aktiviert haben oder nicht. Android-Benutzer können auch verschiedene Standortmodi wählen - Benutzer, die sich im "Batteriesparmodus" oder "Nur Gerät" befinden, haben möglicherweise ungenaue Daten.

### SDK-Benutzerstandort nach IP-Adresse

Ab dem 26\. November 2024 wird Braze die Standorte der Nutzer:innen anhand der IP-Adresse ab dem Beginn der ersten SDK-Sitzung ermitteln. 

Zuvor verwendete Braze bei der Erstellung von SDK-Nutzern:innen und für die Dauer der ersten Sitzung den Code des Geräts. Erst nach der Verarbeitung des ersten Sitzungsbeginns würde die IP-Adresse verwendet, um das zuverlässigere Land für den oder die Nutzer:in festzulegen. Dies bedeutete, dass das Land des Nutzers oder der Nutzerin erst ab der zweiten Sitzung mit größerer Genauigkeit festgelegt wurde, nachdem der erste Sitzungsbeginn verarbeitet worden war.

Jetzt verwendet Braze die IP-Adresse, um den Länderwert in Nutzerprofilen festzulegen, die über das SDK erstellt wurden, und diese IP-basierte Ländereinstellung ist während und nach der ersten Sitzung verfügbar.

## Standort-Targeting

Mit Standort-Tracking Daten und Segmenten können Sie standortbezogene Kampagnen und Strategien einrichten. So können Sie beispielsweise eine Werbekampagne für Nutzer durchführen, die in einer bestimmten Region leben, oder Nutzer in einer Region mit strengeren Vorschriften ausschließen.

Weitere Informationen zur Erstellung eines Standortsegments finden Sie unter [Standort-Targeting]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/).

## Feste Einstellung des Standardattributs für den Standort

Sie können auch den [Endpunkt`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) in unserer API verwenden, um das [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)-Standard-Attribut zu aktualisieren. Ein Beispiel ist:

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

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Häufig gestellte Fragen

### Wann sammelt Braze Standortdaten?

Braze sammelt den Standort nur, wenn die Anwendung im Vordergrund geöffnet ist. Daher zielt unser `Most Recent Location`-Filter auf Nutzer:innen ab, die die Anwendung zuletzt geöffnet haben (auch als Sitzungsbeginn bezeichnet).

Sie sollten auch die folgenden Nuancen beachten:

- Wenn der Standort deaktiviert ist, zeigt der `Most Recent Location`-Filter den zuletzt aufgenommenen Standort an.
- Wenn ein Nutzer jemals einen Standort in seinem Profil gespeichert hat, fällt er unter den `Location Available` Filter, auch wenn er die Standortverfolgung seitdem abgelehnt hat.

### Was ist der Unterschied zwischen den Filtern „Aktuellstes Gebietsschema des Geräts“ und „Letzter Standort“?

Der Filter `Most Recent Device Locale` stammt aus den Geräteeinstellungen des Nutzers oder der Nutzerin. Für Nutzer:innen eines iPhones erscheint dies beispielsweise in ihrem Gerät unter **Einstellungen** > **Allgemein** > **Sprache & Region**. Dieser Filter wird verwendet, um sprachliche und regionale Formatierungen zu erfassen, wie z. B. Datumsangaben und Adressen, und ist unabhängig vom `Most Recent Location`-Filter.

Die `Most Recent Location` ist der letzte bekannte GPS-Standort des Geräts. Dieser Filter wird beim Start der Sitzung aktualisiert und im Profil es Nutzers oder der Nutzerin gespeichert.

### Werden die alten Standortdaten von Braze entfernt, wenn ein Benutzer die Standortverfolgung abbestellt?

Nein. Wenn ein Nutzer:innen jemals einen Standort in seinem Profil gespeichert hat, werden diese Daten nicht automatisch entfernt, wenn er/sie sich später gegen das Standort-Tracking entscheidet.

