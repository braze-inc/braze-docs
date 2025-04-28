---
nav_title: Geofences erstellen
article_title: Geofences erstellen
page_order: 1
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, was Geofences sind und wie Sie Geofencing-Events erstellen und konfigurieren."
tool: 
  - Location
search_rank: 9
---

# Geofences

> Das Herzstück unseres Angebots für Realtime-Standorte ist das Konzept des Geofence. Ein Geofence ist ein virtuelles geografisches Gebiet, das als Breiten- und Längengrad in Kombination mit einem Radius dargestellt wird und einen Kreis um eine bestimmte globale Position bildet. Geofences können von der Größe eines Gebäudes bis zur Größe einer ganzen Stadt reichen.

Sie können auf dem Braze-Dashboard Geofences definieren und diese verwenden, um Kampagnen in Echtzeit auszulösen, wenn Benutzer ihre Grenzen betreten oder verlassen, oder um Stunden oder Tage später Folgekampagnen zu versenden. Benutzer, die Ihre Geofences betreten oder verlassen, fügen eine neue Ebene von Benutzerdaten hinzu, die Sie für die Segmentierung und das Re-Targeting verwenden können.

## Übersicht

Verwalten Sie Geofences unter **Publikum** > **Standorte**.

Geofences sind in Geofence-Sets organisiert - eine Gruppe von Geofences, die verwendet werden können, um Nutzer auf der gesamten Plattform zu segmentieren oder einzubinden. Jedes Geofence-Set kann maximal 10.000 Geofences enthalten.

Sie können eine unbegrenzte Anzahl von Geofences auf dem Dashboard erstellen oder hochladen, so dass Ihr Marketingteam Geofence-Sets und Kampagnen einrichten kann, ohne die Anzahl der Geofences berechnen zu müssen. Braze wird die Geofences, die es für jede:n einzelne:n Nutzer:in trackt, dynamisch neu synchronisieren, um sicherzustellen, dass die für sie:ihn relevantesten Geofences immer verfügbar sind.

- Android-Apps können jeweils nur bis zu 100 Geofences lokal speichern. Braze ist so konfiguriert, dass nur bis zu 20 Geofences pro App lokal gespeichert werden.
- iOS-Geräte können bis zu 20 Geofences pro App gleichzeitig überwachen. Braze wird bis zu 20 Standorte überwachen, sofern Platz vorhanden ist. 
- Wenn die:der Nutzer:in berechtigt ist, mehr als 20 Geofences zu erhalten, lädt Braze die maximale Anzahl an Standorten herunter, die auf der Nähe der Nutzerin oder des Nutzers zum Zeitpunkt des Sitzungsstars/der stillen Push-Aktualisierung basieren
- Damit Geofences korrekt funktionieren, sollten Sie sicherstellen, dass Ihre App nicht alle verfügbaren Geofence-Spots nutzt.

## Erstellen von Geofence-Sets

### Sets manuell erstellen

Klicken Sie auf der Seite **Standorte** auf **\+ Geofence-Set erstellen**.

![Geofence-Set der deutschen Flughäfen mit einem Benutzer, der einen Radius von zweitausend Metern auf der Karte für den Flughafen Hamburg zeichnet.][1]

Sobald Sie ein Geofence-Set erstellt haben, können Sie Geofences manuell hinzufügen, indem Sie sie auf der Karte einzeichnen. Wir empfehlen, Geofences mit einem Radius von mindestens 200 Metern zu erstellen, um eine optimale Funktionalität zu gewährleisten. Weitere Informationen zu den konfigurierbaren Optionen finden Sie unter [Geofence-Konfiguration]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/mobile_integrations/).

### Erstellen von Sets per Bulk-Upload {#creating-geofence-sets-via-bulk-upload}

Geofences können in großen Mengen als GeoJSON-Objekt vom Typ `FeatureCollection` hochgeladen werden. Jeder einzelne Geofence ist ein `Point` Geometrietyp in der Feature-Sammlung. Die Eigenschaften für jedes Feature erfordern einen `"radius"` Schlüssel und einen optionalen `"name"` Schlüssel für jeden Geofence. Um Ihre GeoJSON hochzuladen, klicken Sie auf **\+ Geofence Set erstellen** und anschließend auf **GeoJSON hochladen**.

Das folgende Beispiel zeigt die korrekte GeoJSON für die Angabe von zwei Geofences: eine für den Hauptsitz von Braze in NYC und eine für die Freiheitsstatue südlich von Manhattan. Wir empfehlen, Geofences mit einem Radius von mindestens 100 Metern hochzuladen, um eine optimale Funktionalität zu gewährleisten.

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

Wenn Sie Ihre Geofences erstellen, sollten Sie die folgenden Punkte beachten:

- Der Wert `coordinates` in GeoJSON ist formatiert als [Längengrad, Breitengrad].
- Der maximale Geofence-Radius, der hochgeladen werden kann, beträgt 10.0000 Meter (etwa 100 Kilometer oder 62 Meilen).

## Aktualisieren von Geofence-Sets

Für aktive Nutzer:innen fragt das Braze SDK Geofences nur einmal pro Tag bei Sitzungsbeginn an. Das heißt, wenn nach dem Start der Sitzung Änderungen an den Geofence-Sets vorgenommen werden, müssen Sie 24 Stunden ab dem Zeitpunkt warten, an dem die Sets zum ersten Mal heruntergeladen werden, um das aktualisierte Set zu erhalten.

Für inaktive Nutzer:innen sendet Braze bei aktiviertem Hintergrund-Push einmal alle 24 Stunden einen stillen Push, um die neuesten Standorte auf das Gerät zu übertragen.

{% alert note %}
Wenn die Geofences nicht lokal auf das Gerät geladen werden, kann die:der Nutzer:in den Geofence nicht triggern, selbst wenn er das Gebiet betritt.
{% endalert %}

### Update für einzelne Nutzer:innen

Die Aktualisierung von Geofences für einzelne Benutzer kann beim Testen hilfreich sein. Um Geofence-Sets zu aktualisieren, navigieren Sie zum unteren Ende der Seite **Standorte** und klicken Sie auf **Geofences neu synchronisieren**. Sie werden dann aufgefordert, `external_id` oder `email` der Nutzer:innen einzugeben, die Sie aktualisieren möchten

## Geofence-Ereignisse verwenden

Sobald Sie Geofences konfiguriert haben, können Sie diese nutzen, um die Kommunikation mit Ihren Nutzern zu verbessern und zu bereichern.

### Triggern

Um Geofence-Daten als Teil von Kampagnen- und Canvas-Triggern zu verwenden, wählen Sie für die Zustellung die Option **Aktionsbasierte Zustellung**. Als Nächstes fügen Sie eine Aktion triggern von `Trigger a Geofence` hinzu. Wählen Sie schließlich den Geofence-Satz und die Geofence-Übergangs-Event-Typen für Ihre Nachricht. Sie können Nutzer:innen auch mit Geofence-Events durch ein Canvas voranbringen.

![][2]

### Personalisierung

Um Geofence-Daten für die Personalisierung einer Nachricht zu verwenden, können Sie die folgende Liquid-Syntax für die Personalisierung verwenden:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Häufig gestellte Fragen

Besuchen Sie [Geofence FAQ][3] für Antworten auf häufig gestellte Fragen zu Geofencing.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
