{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Deaktivieren des Trackings von Daten

Um die Datenerfassung zu deaktivieren, verwenden Sie bitte die`disableSDK`Methode. Nach dem Aufruf dieser Methode stellt das Braze SDK die Übermittlung von Daten an die Braze-Server ein.

```javascript
Braze.disableSDK();
```

## Wiederaufnahme des Trackings von Daten

Um die Datenerfassung nach der Deaktivierung wieder aufzunehmen, verwenden Sie bitte die`enableSDK`Methode.

```javascript
Braze.enableSDK();
```

## Daten löschen

Um alle lokal auf dem Gerät gespeicherten Braze SDK-Daten zu löschen, verwenden Sie bitte die`wipeData`Methode. Nach dem Aufruf dieser Methode wird das SDK deaktiviert und muss wieder `enableSDK`aktiviert werden.

```javascript
Braze.wipeData();
```

## Daten löschen

Um eine sofortige Übertragung aller ausstehenden Daten an die Braze-Server zu veranlassen, verwenden Sie `requestImmediateDataFlush`bitte .

```javascript
Braze.requestImmediateDataFlush();
```

## Einstellung für das Enablement der Werbe-Tracking-Funktionen

Um Braze mitzuteilen, ob das Tracking für dieses Gerät aktiviert ist, verwenden Sie bitte die`setAdTrackingEnabled`Methode. Das SDK erfasst diese Daten nicht automatisch.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

Der zweite Parameter ist die Google-Werbe-ID und wird ausschließlich auf Android-Geräten verwendet.

## Update der Zulassungsliste für Tracking-Eigenschaften (nur iOS)

Um die Liste der für das Tracking deklarierten Datentypen zu aktualisieren, verwenden Sie bitte `updateTrackingPropertyAllowList`. Dies ist auf Android nicht möglich.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

Weitere Informationen referenzieren Sie im [Datenschutzmanifest]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/).
