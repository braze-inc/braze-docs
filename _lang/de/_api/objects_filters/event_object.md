---
nav_title: "Ereignis-Objekt"
article_title: API-Ereignis-Objekt
page_order: 6
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, was das Event-Objekt ist und warum es ein wichtiger Bestandteil eventbasierter Kampagnen-Strategien ist."

---

# Ereignis-Objekt

> In diesem Artikel werden die verschiedenen Komponenten eines Ereignisobjekts erläutert, wie Sie dieses Objekt verwenden können und welche Beispiele Sie verwenden können.

## Was ist ein Ereignisobjekt?

Ein Ereignisobjekt ist ein Objekt, das über die API übergeben wird, wenn ein bestimmtes Ereignis eintritt. Ereignisobjekte sind in einem Ereignis-Array untergebracht. Jedes Event-Objekt im Events-Array repräsentiert ein einzelnes Vorkommen eines angepassten Events durch einen bestimmten Nutzer:in zum angegebenen Zeitwert. Das Event-Objekt verfügt über viele verschiedene Felder, die Sie anpassen können, indem Sie Event-Eigenschaften in Nachrichten, Datenerfassung und Personalisierung festlegen und verwenden.

Wie Sie angepasste Events für eine bestimmte Plattform einrichten, erfahren Sie in der Anleitung zur Plattformintegration im [Entwicklerhandbuch]({{site.baseurl}}/developer_guide/home/). Verweisen Sie auf den entsprechenden Artikel für Ihre Plattform:

- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### Objektkörper

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

- [Externe Benutzer-ID]({{site.baseurl}}/api/basics/#user-ids)
- [Bezeichner der App]({{site.baseurl}}/api/identifier_types/)
- [ISO 8601 Zeitcode](https://en.wikipedia.org/wiki/ISO_8601)

#### Nur bestehende Profile aktualisieren

Um nur bestehende Nutzerprofile in Braze zu aktualisieren, sollten Sie den Schlüssel `_update_existing_only` mit dem Wert `true` im Hauptteil Ihrer Anfrage übergeben. Wenn dieser Wert weggelassen wird, erstellt Braze ein neues Nutzerprofil, wenn das `external_id` nicht bereits existiert.

{% alert note %}
Wenn Sie über den Endpunkt `/users/track` ein Nutzerprofil erstellen, das nur aus Aliasen besteht, muss `_update_existing_only` auf `false` gesetzt werden. Wenn dieser Wert weggelassen wird, wird das Profil, das nur einen Alias enthält, nicht erstellt.
{% endalert %}

## Event-Eigenschaften Objekt

Angepasste Events und Käufe können Event-Eigenschaften haben. Die "Eigenschaften"-Werte sollten ein Objekt sein, bei dem die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen müssen nicht-leere Strings mit maximal 255 Zeichen sein, ohne führende Dollarzeichen ($).

Bei den Eigenschaften kann es sich um jeden der folgenden Datentypen handeln:

| Datentyp | Beschreibung |
| --- | --- |
| Zahlen | Entweder als [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) oder [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Boolesche Werte | `true` oder `false` |
| Datumsangaben | Müssen als Strings im Format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) oder in einem der folgenden Formate formatiert sein: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Innerhalb von Arrays nicht unterstützt. <br><br>Beachten Sie, dass "T" ein Zeitbezeichner und kein Platzhalter ist und nicht geändert oder entfernt werden sollte. <br><br>Zeitattribute ohne Zeitzone sind standardmäßig auf Mitternacht UTC eingestellt (und werden auf dem Dashboard als das Äquivalent zu Mitternacht UTC in der Zeitzone des Unternehmens formatiert). <br><br> Ereignisse mit Zeitstempeln in der Zukunft werden standardmäßig auf die aktuelle Zeit gesetzt.  |
| Strings | 255 Zeichen oder weniger. |
| Arrays | Arrays können keine Datumsangaben enthalten. |
| Objekte | Die Objekte werden als Strings eingelesen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Objekte mit Event-Eigenschaften, die Array- oder Objektwerte enthalten, können eine Nutzlast für Event-Eigenschaften von bis zu 100 KB haben.

### Reservierte Tasten

Die folgenden Schlüssel sind reserviert und können nicht als benutzerdefinierte Ereigniseigenschaften verwendet werden:

- `time`
- `event_name`

{% alert important %}
Die Verwendung von reservierten Schlüsseln als Namen für angepasste Event-Eigenschaften führt zu API-Fehlern beim Senden von Anfragen an den Endpunkt `/users/track`.
{% endalert %}

### Persistenz der Eigenschaften von Ereignissen

Event-Eigenschaften dienen zum Filtern und zur Liquid Personalisierung von Nachrichten, die durch ihre übergeordneten Ereignisse getriggert werden. Standardmäßig werden sie nicht auf dem Braze Nutzerprofil persistent gehalten. Um die Werte von Event-Eigenschaften bei der Segmentierung zu verwenden, lesen Sie bitte den Abschnitt [Angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/), in dem die verschiedenen Ansätze zur langfristigen Speicherung von Werten für Event-Eigenschaften beschrieben werden.

#### Ereignis Beispiel Anfrage

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [ISO 8601 Zeitcode Wiki](http://en.wikipedia.org/wiki/ISO_8601)

## Ereignis-Objekte

Anhand des angegebenen Beispiels können wir sehen, dass jemand vor kurzem einen Trailer gesehen und dann einen Film ausgeliehen hat. Wir können zwar nicht in eine Kampagne gehen und die Nutzer auf der Grundlage dieser Eigenschaften segmentieren, aber wir können diese Eigenschaften strategisch nutzen, indem wir sie in Form einer Quittung verwenden, um eine angepasste Nachricht über einen Kanal mit Liquid zu versenden. Zum Beispiel: "Hallo **Beth**, danke, dass Sie **The Sad Egg** von **Dan Alexander** ausgeliehen haben, hier sind einige Filmempfehlungen, die auf Ihrer Ausleihe basieren..."


