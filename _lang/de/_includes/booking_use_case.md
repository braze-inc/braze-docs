# Anwendungsfälle: Buchungserinnerung per E-Mail

> Braze ist eine umfassende Customer-Engagement-Plattform, die so konzipiert ist, dass sie in hohem Maße programmgesteuert werden kann. In diesem Anwendungsfall zeigen wir Ihnen einige Möglichkeiten, wie Sie die Funktionen von Braze in Anwendungsfälle integrieren können, die an der Schnittstelle zwischen Produkt und Marketing liegen, wie z.B. Buchungssysteme.

Dieser Anwendungsfall zeigt, wie Sie die Features von Braze nutzen können, um einen E-Mail Messaging-Dienst für Buchungserinnerungen aufzubauen. Der Dienst erlaubt es Nutzern:innen, Termine zu buchen, und sendet ihnen Nachrichten, um sie an ihre Termine zu erinnern. Obwohl in diesem Anwendungsfall E-Mail-Nachrichten verwendet werden, können Sie Nachrichten in einem beliebigen oder mehreren Kanälen auf der Grundlage eines einzigen Updates eines Nutzerprofils versenden.

Weitere Vorteile der Erstellung dieses Dienstes sind:
- Gesendete Nachrichten werden vollständig getrackt und gemeldet.
- Der Inhalt von Nachrichten kann von nicht-technischen Nutzer:innen von Braze aktualisiert werden.
- Nachrichten befolgen den Opt-in und Opt-out Status von Nutzerprofilen per Kampagnen-Konfiguration.
- Sowohl Buchungsdaten als auch Daten zur Interaktion mit Nachrichten können verwendet werden, um Nutzer:innen für zusätzliches Messaging zu segmentieren und zu targetieren. So können Sie z.B. diejenigen, die die erste Nachricht nicht geöffnet haben, mit einer zusätzlichen Erinnerung an ihren Termin retargeten.

Folgen Sie diesen Schritten, um diesen Anwendungsfall zu erreichen:
1. [Schreiben Sie anstehende Buchungsdaten in ein Nutzerprofil von Braze](#step-1)
2. [Einrichten und Starten einer Nachricht zur Buchungserinnerung](#step-2)
3. [Bearbeiten Sie aktualisierte Buchungen und Stornierungen](#step-3)

## Schritt 1: Schreiben Sie anstehende Buchungsdaten in ein Nutzerprofil von Braze {#step-1}

Verwenden Sie den Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Endpunkt, um bei jeder Buchung ein [angepasstes Attribut]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) in ein Nutzerprofil zu schreiben. Stellen Sie sicher, dass das angepasste Attribut alle Informationen enthält, die zum Senden und Personalisieren der Nachricht benötigt werden. In diesem Anwendungsfall nennen wir das angepasste Attribut "Reisen".

### Buchung hinzufügen

Wenn ein Nutzer:innen eine Buchung erstellt, verwenden Sie die folgende Struktur für das Array von Objekten, um die Daten über den Endpunkt `/users/track` an Braze zu senden.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

Das verschachtelte angepasste Attribut "Reisen" wird im Nutzerprofil wie folgt angezeigt.

![Zwei verschachtelte angepasste Attribute für eine Reise nach London und eine Reise nach Sydney.]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### Update der Buchung
Wenn ein Nutzer:innen eine Buchung aktualisiert, verwenden Sie die folgende Struktur für das Array von Objekten, um die Daten über den Endpunkt `/users/track` an Braze zu senden.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### Buchung entfernen

{% tabs %}
{% tab /benutzer/track Endpunkt %}
#### Senden Sie Daten über den Endpunkt `/users/track` 
Wenn ein Nutzer:innen eine Buchung löscht, verwenden Sie die folgende Struktur für das Array von Objekten, um die Daten über den Endpunkt `/users/track` an Braze zu senden.

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### Schreiben von verschachtelten Attributen zu Nutzerprofilen über das SDK

Wenn Sie mit Ihrer App, Website oder beidem Terminbuchungen erfassen und diese Daten direkt in ein Nutzerprofil schreiben möchten, können Sie das Braze SDK verwenden, um diese Daten zu übertragen. Hier ist ein Beispiel für die Verwendung des Internet SDK:

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

Die angegebene Buchung wird aus dem verschachtelten angepassten Attribut im Nutzerprofil entfernt und alle verbleibenden Buchungen werden angezeigt.

![Ein verschachteltes angepasstes Attribut für eine Reise nach London.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## Schritt 2: Einrichten und Starten einer Nachricht zur Buchungserinnerung {#step-2}

### Schritt 2a: Erstellen Sie eine Zielgruppe
Erstellen Sie eine Zielgruppe, die Erinnerungen erhalten soll, indem Sie eine Segmentierung nach mehreren Kriterien vornehmen. Wenn Sie zum Beispiel zwei Tage vor dem Buchungsdatum eine Erinnerung senden möchten, wählen Sie Folgendes aus:

- Ein Startdatum **in mehr als 1 Tag** und
- Ein Starttermin **in weniger als 2 Tagen** 

![Ein verschachteltes angepasstes Attribut "Reisen" mit Kriterien für ein Startdatum, das mehr als einen Tag und weniger als zwei Tage beträgt.]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### Schritt 2b: Erstellen Sie Ihre Nachricht

Erstellen Sie die Nachricht für die Erinnerungsmail, indem Sie die Schritte unter [Erstellen einer E-Mail mit angepasstem HTML-Code]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) befolgen. Verwenden Sie Liquid, um die Nachricht mit Daten aus dem angepassten Attribut des Kunden ("Reisen") anzupassen, wie in diesem Beispiel.

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}} 
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### Schritt 2c: Starten Sie Ihre Kampagne

Starten Sie die Kampagne für die Nachricht zur Erinnerung per E-Mail. Jetzt wird jedes Mal, wenn Braze das angepasste Attribut "Reisen" empfängt, eine Nachricht entsprechend den Daten im Objekt der jeweiligen Buchung geplant.

## Schritt 3: Bearbeiten Sie aktualisierte Updates und Stornierungen von Buchungen {#step-3}

Jetzt, wo Sie Erinnerungsnachrichten versenden, können Sie auch Nachrichten zur Bestätigung einrichten, die gesendet werden, wenn Buchungen aktualisiert oder storniert werden.

### Schritt 3a: Senden Sie aktualisierte Daten

{% tabs %}
{% tab /benutzer:innen/track %}

#### Senden Sie Daten über den Endpunkt `/users/track` 
Verwenden Sie den Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Endpunkt, um ein angepasstes Event zu senden, wenn ein Nutzer:innen eine Buchung aktualisiert oder storniert. In diesem Fall geben Sie die erforderlichen Daten in Event-Eigenschaften ein, die die Änderung bestätigen. 

Nehmen wir an, dass in diesem Anwendungsfall ein Nutzer:innen das Datum seiner Reise nach Sydney aktualisiert hat. Das Ereignis würde wie folgt aussehen:

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### Schreiben von verschachtelten Attributen zu Nutzerprofilen über das SDK

Senden Sie angepasste Events über das SDK an das Nutzerprofil. Wenn Sie zum Beispiel das Web SDK verwenden, könnten Sie senden:

{% raw %}
```json
braze.logCustomEvent("trip_updated", { 
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Schritt 3b: Erstellen Sie eine Nachricht zur Bestätigung des Updates

Erstellen Sie eine [aktionsbasierte Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/), um dem Nutzer:innen eine Bestätigung für seine aktualisierte Buchung zu schicken. [Mit Liquid können Sie ein Template für Event-Eigenschaften erstellen]({{site.baseurl}}/user_guide/data/custom_data/custom_events/), das den Namen, die alte Zeit und die neue Zeit der Buchung (oder nur den Namen, wenn es sich um eine Stornierung handelt) in der Nachricht selbst wiedergibt.

Sie könnten zum Beispiel die folgende Nachricht verfassen:

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### Schritt 3c: Ändern Sie das Nutzerprofil entsprechend dem Update

Um schließlich die Buchungserinnerungen aus Schritt 1 und 2 auf der Grundlage der neuesten Daten zu versenden, aktualisieren Sie die verschachtelten angepassten Attribute, um die Änderung oder Stornierung der Buchung zu berücksichtigen.

#### Update der Buchung

Wenn der Nutzer:innen in diesem Anwendungsfall seine Reise nach Sydney aktualisiert, würden Sie den Endpunkt `/users/track` verwenden, um das Datum mit einem Aufruf wie diesem zu ändern:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### Stornierte Buchung

Wenn der Nutzer:innen in diesem Anwendungsfall seine Syndey-Reise storniert, würden Sie den folgenden Aufruf an den Endpunkt `/users/track` senden:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

Nach dem Versenden dieser Anrufe und dem Update des Nutzerprofils werden die Nachrichten zur Buchungserinnerung die neuesten Daten über die Buchungsdaten des Nutzers:innen wiedergeben.

