---
nav_title: "Ereignis-Objekt"
article_title: API-Ereignis-Objekt
page_order: 6
page_type: reference
description: "In diesem Referenzartikel erfahren Sie mehr über das Event-Objekt, was es ist und warum es ein entscheidender Bestandteil von Event-basierten Kampagnenstrategien ist."

---

# Ereignis-Objekt

> In diesem Artikel werden die verschiedenen Komponenten eines Ereignisobjekts erläutert, wie Sie dieses Objekt verwenden können und welche Beispiele Sie verwenden können.

## Was ist das Ereignisobjekt?

Ein Ereignisobjekt ist ein Objekt, das über die API übergeben wird, wenn ein bestimmtes Ereignis eintritt. Ereignisobjekte sind in einem Ereignis-Array untergebracht. Jedes Ereignisobjekt im Ereignis-Array steht für ein einzelnes Auftreten eines benutzerdefinierten Ereignisses durch einen bestimmten Benutzer zum angegebenen Zeitpunkt. Das Ereignisobjekt hat viele verschiedene Felder, die Sie durch die Einstellung und Verwendung von Ereigniseigenschaften in Nachrichten, Datenerfassung und Personalisierung anpassen können.

Wie Sie benutzerdefinierte Ereignisse für eine bestimmte Plattform einrichten können, erfahren Sie in der Anleitung zur Plattformintegration im [Entwicklerhandbuch][1]. Sie finden diese Informationen auf der Seite **Benutzerdefinierte Ereignisse verfolgen** auf der Registerkarte **Analytics** der verschiedenen Plattformen. Wir haben mehrere für Sie verlinkt.

Artikel Benutzerdefinierte Ereignisse nachverfolgen:

- [Android][2]
- [iOS][3]
- [Web][4]

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
- [App Kennung]({{site.baseurl}}/api/identifier_types/)
- [ISO 8601 Zeitcode][22]

#### Nur bestehende Profile aktualisieren

Wenn Sie nur bestehende Benutzerprofile in Braze aktualisieren möchten, sollten Sie den Schlüssel `_update_existing_only` mit dem Wert `true` im Text Ihrer Anfrage übergeben. Wenn dieser Wert weggelassen wird, erstellt Braze ein neues Benutzerprofil, wenn das `external_id` nicht bereits existiert.

{% alert note %}
Wenn Sie ein reines Alias-Benutzerprofil über den Endpunkt `/users/track` erstellen, muss `_update_existing_only` auf `false` gesetzt werden. Wenn dieser Wert weggelassen wird, wird das Profil, das nur einen Alias enthält, nicht erstellt.
{% endalert %}

## Ereignis-Eigenschaften Objekt
Benutzerdefinierte Ereignisse und Käufe können Ereigniseigenschaften haben. Die "Eigenschaften"-Werte sollten ein Objekt sein, bei dem die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen müssen nicht leere Zeichenketten sein, die maximal 255 Zeichen lang sind und keine führenden Dollarzeichen ($) enthalten.

Eigenschaftswerte können alle der folgenden Datentypen sein:

| Daten Typ | Beschreibung |
| --- | --- |
| Zahlen | Entweder als [Ganzzahl](https://en.wikipedia.org/wiki/Integer) oder als [Fließkommazahl](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Boolesche Wörter | `true` oder `false` |
| Datumsangaben | Formatiert als Zeichenketten im [ISO-8601-](https://en.wikipedia.org/wiki/ISO_8601) oder `yyyy-MM-dd'T'HH:mm:ss:SSSZ` -Format. Innerhalb von Arrays nicht unterstützt. |
| Streicher | 255 Zeichen oder weniger. |
| Arrays | Arrays können keine Datumsangaben enthalten. |
| Objekte | Objekte werden als Strings eingelesen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Objekte mit Ereigniseigenschaften, die Array- oder Objektwerte enthalten, können eine Nutzlast für Ereigniseigenschaften von bis zu 100 KB haben.

### Persistenz von Ereigniseigenschaften
Ereigniseigenschaften dienen zum Filtern von Nachrichten, die von ihren übergeordneten Ereignissen ausgelöst werden, und zur flüssigen Personalisierung dieser Nachrichten. Standardmäßig werden sie nicht im Braze-Benutzerprofil gespeichert. Zur Verwendung von Ereigniseigenschaftswerten bei der Segmentierung lesen Sie bitte den Abschnitt [Benutzerdefinierte Ereignisse][5], in dem die verschiedenen Ansätze zur langfristigen Speicherung von Ereigniseigenschaftswerten beschrieben werden.

#### Ereignisbeispiel Anfrage

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
- [ISO 8601 Zeitcode Wiki][19]

## Ereignis-Objekte

Anhand des angegebenen Beispiels können wir sehen, dass jemand vor kurzem einen Trailer gesehen und dann einen Film ausgeliehen hat. Wir können zwar nicht in eine Kampagne gehen und die Benutzer anhand dieser Eigenschaften segmentieren, aber wir können diese Eigenschaften strategisch nutzen, indem wir sie in Form einer Quittung verwenden, um eine benutzerdefinierte Nachricht über einen Kanal mit Liquid zu senden. Zum Beispiel: "Hallo **Beth**, danke, dass Sie **The Sad Egg** von **Dan Alexander** ausgeliehen haben, hier sind einige Filmempfehlungen, die auf Ihrer Ausleihe basieren..."


[1]: {{site.baseurl}}/developer_guide/home/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Zeitcode Wiki"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Zeitcode"
[23]: {{site.baseurl}}/api/basics/#external-user-id-explanation
