---
nav_title: Erstellen von Geofences
article_title: Geofences erstellen
page_order: 1
page_type: reference
toc_headers: h2
description: "In diesem Referenzartikel erfahren Sie, was Geofences sind und wie Sie Geofencing-Events erstellen und konfigurieren."
tool: 
  - Location
search_rank: 9
---

# Geofences

> Das Herzstück unseres Angebots für Realtime-Standorte ist das Konzept des Geofence. Ein Geofence ist ein virtuelles geografisches Gebiet, das als Breiten- und Längengrad in Kombination mit einem Radius dargestellt wird und einen Kreis um eine bestimmte globale Position bildet. Geofences können von der Größe eines Gebäudes bis zur Größe einer ganzen Stadt reichen.

## How it works

Geofences can be used to trigger campaigns in real-time as users enter and exit their borders, or send follow-up campaigns hours or days later. Benutzer, die Ihre Geofences betreten oder verlassen, fügen eine neue Ebene von Benutzerdaten hinzu, die Sie für die Segmentierung und das Re-Targeting verwenden können.

Geofences sind in Geofence-Sets organisiert - eine Gruppe von Geofences, die verwendet werden können, um Nutzer auf der gesamten Plattform zu segmentieren oder einzubinden. Jedes Geofence-Set kann maximal 10.000 Geofences enthalten.

You can create or upload an unlimited number of geofences.

- Android-Apps können jeweils nur bis zu 100 Geofences lokal speichern. Braze ist so konfiguriert, dass nur bis zu 20 Geofences pro App lokal gespeichert werden.
- iOS-Geräte können bis zu 20 Geofences pro App gleichzeitig überwachen. Braze wird bis zu 20 Standorte überwachen, sofern Platz vorhanden ist. 
- If the user is eligible to receive more than 20 geofences, Braze will download the maximum amount of locations based on proximity to the user at the point of session start.
- Damit Geofences korrekt funktionieren, sollten Sie sicherstellen, dass Ihre App nicht alle verfügbaren Geofence-Spots nutzt.

Refer to the following table for common geofence terms and their descriptions.

| Term | Description |
|---|---|
| Latitude and longitude | Der geographische Mittelpunkt des Geofence. |
| Radius | Der Radius des Geofence in Metern, gemessen vom geografischen Zentrum. We recommend setting a minimum radius of 100–150 meters for all geofences. |
| Cooldown | Nutzer:innen erhalten durch Geofence getriggerte Benachrichtigungen, nachdem sie einzelne Geofences betreten oder verlassen haben. After a transition occurs, there is a pre-defined time during which that user may not perform the same transition on that individual geofence again. This time is called the "cooldown" and is pre-defined by Braze, and its main purpose is to prevent unnecessary network requests. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Manually create geofences

### Step 1: Create a geofence set

To create a geofence, you'll need to create a geofence set first.

1. Go to **Audience** > **Locations** in the Braze dashboard.
2. Select **Create Geofence Set**.
3. For **Set name**, enter a name for your geofence set.
4. (Optional) Add tags to filter your set.

### Step 2: Add the geofences

Next, you can add geofences to your geofence set.

1. Select **Draw Geofence** to click and drag the circle on the map. Repeat to add more geofences to your set as needed.
2. (Optional) You can select **Edit** and replace the geofence description with a name.
3. Select **Save Geofence Set** to save.

{% alert tip %}
Wir empfehlen, Geofences mit einem Radius von mindestens 200 Metern zu erstellen, um eine optimale Funktionalität zu gewährleisten. For more information on configurable options, refer to [Mobile integrations](#mobile-integrations).
{% endalert %}

![Ein Geofence-Set mit zwei Geofences "EastCoastGreaterNY" und "WesternRegion" mit zwei Kreisen auf der Karte.]({% image_buster /assets/img/geofence_example.png %})

## Bulk upload geofences {#creating-geofence-sets-via-bulk-upload}

Geofences können in großen Mengen als GeoJSON-Objekt vom Typ `FeatureCollection` hochgeladen werden. Each geofence is a `Point` geometry type in the feature collection. Die Eigenschaften für jedes Feature erfordern einen `radius` Schlüssel und einen optionalen `name` Schlüssel für jeden Geofence. 

To upload your GeoJSON, select **More** > **Upload GeoJSON**.

When creating your geofences, consider the following details:

- The `coordinates` value in the GeoJSON is formatted as `[Longitude, Latitude]`.
- Der maximale Geofence-Radius, der hochgeladen werden kann, beträgt 10.000 Meter (etwa 10 Kilometer oder 6,2 Meilen).

### Beispiel

The following example represents the correct GeoJSON for specifying two geofences: one for Braze headquarters in NYC, and one for the Statue of Liberty south of Manhattan.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Geofence-Ereignisse verwenden

After geofences have been configured, you can use them to enhance and enrich how you communicate with your users.

### Triggering campaigns and Canvases

Um Geofence-Daten als Teil von Kampagnen- und Canvas-Triggern zu verwenden, wählen Sie für die Zustellung die Option **Aktionsbasierte Zustellung**. Als Nächstes fügen Sie eine Aktion triggern von `Trigger a Geofence` hinzu. Wählen Sie schließlich den Geofence-Satz und die Geofence-Übergangs-Event-Typen für Ihre Nachricht. Sie können Nutzer:innen auch mit Geofence-Events durch ein Canvas voranbringen.

![Eine aktionsbasierte Kampagne mit einem Geofence, der ausgelöst wird, wenn ein Nutzer:innen einen deutschen Flughafen betritt.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalizing messages

Um Geofence-Daten für die Personalisierung einer Nachricht zu verwenden, können Sie die folgende Liquid-Syntax für die Personalisierung verwenden:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Aktualisieren von Geofence-Sets

Für aktive Nutzer:innen fragt das Braze SDK Geofences nur einmal pro Tag bei Sitzungsbeginn an. Das heißt, wenn nach dem Start der Sitzung Änderungen an den Geofence-Sets vorgenommen werden, müssen Sie 24 Stunden ab dem Zeitpunkt warten, an dem die Sets zum ersten Mal heruntergeladen werden, um das aktualisierte Set zu erhalten.

{% alert note %}
Wenn die Geofences nicht lokal auf das Gerät geladen werden, kann die:der Nutzer:in den Geofence nicht triggern, selbst wenn er das Gebiet betritt.
{% endalert %}

## Mobile integrations {#mobile-integrations}

### Cross-platform requirements

Geofence-ausgelöste Kampagnen sind auf iOS und Android verfügbar. Um Geofencing zu unterstützen, muss Folgendes vorhanden sein:

1. Ihre Integration muss Push-Benachrichtigungen im Hintergrund unterstützen.
2. Braze Geofences oder die Standorterfassung müssen aktiviert sein.
3. Bei Geräten mit iOS Version 11 und höher muss der Benutzer den Standortzugriff immer zulassen, damit Geofencing funktioniert.

{% alert important %}
Ab Braze SDK Version 3.6.0 ist die Sammlung von Braze-Standorten standardmäßig deaktiviert. Um zu überprüfen, ob die Funktion unter Android aktiviert ist, vergewissern Sie sich, dass `com_braze_enable_location_collection` auf `true` in Ihrem `braze.xml` eingestellt ist.
{% endalert %}

Refer to [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence) or [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5) documentation for more guidance based on your platform.

{% alert tip %}
You can also leverage geofences with our Technology Partners, such as [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) and [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)
{% endalert %}

## Häufig gestellte Fragen

### What's the difference between geofences and location tracking?

In Braze ist ein Geofence ein anderes Konzept als das Standort-Tracking. Geofences werden als Auslöser für bestimmte Aktionen verwendet. Ein Geofence ist eine virtuelle Grenze, die um einen geografischen Standort herum eingerichtet wird. Wenn ein:e Nutzer:in diese Grenze überschreitet oder verlässt, kann dies eine bestimmte Aktion auslösen, z. B. das Senden einer Nachricht.

Das Standort-Tracking wird verwendet, um die letzten Standortdaten eines Nutzers oder einer Nutzerin zu erfassen und zu speichern. Diese Daten können verwendet werden, um Nutzer:innen auf der Grundlage des `Most Recent Location`-Filters zu segmentieren. Sie können zum Beispiel den `Most Recent Location`-Filter verwenden, um eine bestimmte Region Ihres Publikums anzusprechen, z. B. um eine Nachricht an Nutzer:innen in New York zu senden.

### Wie genau sind die Geofences von Braze?

Die Geofences von Braze verwenden eine Kombination aller für ein Gerät verfügbaren Standortanbieter, um den Standort des Nutzers oder der Nutzerin dreidimensional zu bestimmen. Dazu gehören Wi-Fi, GPS und Mobilfunktürme.

Die typische Genauigkeit liegt im Bereich von 20-50 m, und die beste Genauigkeit liegt im Bereich von 5-10 m. In ländlichen Gebieten kann sich die Genauigkeit erheblich verschlechtern, möglicherweise bis zu mehreren Kilometern. Braze empfiehlt, in ländlichen Gegenden Geofences mit größeren Radien anzulegen.

Weitere Informationen über die Genauigkeit von Geofences finden Sie in der Dokumentation [für Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) und [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### How do geofences affect battery life?

Our geofencing solution uses the native geofence system service on iOS and Android and is tuned to intelligently trade off accuracy and power, saving battery life and improving performance as the underlying service improves.

### When are geofences active?

Die Geofences von Braze funktionieren zu jeder Tageszeit, auch wenn Ihre App geschlossen ist. Sie werden aktiv, sobald sie definiert und in das Braze-Dashboard hochgeladen wurden. Geofences können jedoch nicht funktionieren, wenn ein:e Nutzer:in das Standort-Tracking deaktiviert hat.

Damit Geofences funktionieren, müssen die Nutzer die Standortdienste auf ihrem Gerät aktiviert haben und Ihrer App die Erlaubnis zum Zugriff auf ihren Standort erteilt haben. Wenn ein Benutzer die Standortverfolgung deaktiviert hat, kann Ihre App nicht erkennen, wann er einen Geofence betritt oder verlässt.

### Werden Geofence-Daten in Benutzerprofilen gespeichert?

Nein, Braze speichert keine Geofence-Daten in Benutzerprofilen. Geofences werden von den Standortdiensten von Apple und Google überwacht, und Braze wird nur benachrichtigt, wenn ein Benutzer einen Geofence auslöst. Zu diesem Zeitpunkt verarbeiten wir alle damit verbundenen Trigger-Kampagnen.

### Kann ich einen Geofence innerhalb eines Geofence einrichten?

Vermeiden Sie es, Geoofences einzurichten, die sich gegenseitig überschneiden, da dies zu Problemen beim Triggern von Benachrichtigungen führen kann.

