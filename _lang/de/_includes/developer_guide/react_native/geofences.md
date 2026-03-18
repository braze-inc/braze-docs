{% alert important %}
Geofences werden **sowohl** auf **iOS als auch** auf **Android** im React Native SDK unterstützt. Diese`requestLocationInitialization`Methode ist ausschließlich für Android verfügbar und für iOS nicht erforderlich. Die`requestGeofences`Methode ist auf beiden Plattformen verfügbar. Standardmäßig kann das SDK Geofences automatisch anfragen und überwachen, wenn der Standort verfügbar ist. Sie können sich auf diese automatische Konfiguration verlassen oder die Funktion manuell aufrufen`requestGeofences`.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %} Unter Android müssen Sie [stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) für die Geofence-Synchronisierung [einrichten]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Einrichten von Geofences {#setting-up-geofences}

### Schritt 1: Enablement in Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Schritt 2: Vollständige native Android-Einrichtung

Da das React Native SDK das native Braze Android SDK verwendet, führen Sie bitte die native Android-Geofence-Einrichtung für Ihr Projekt durch. Die entsprechenden Schritte für iOS werden im nativen SWIFT SDK-Leitfaden zu Geofencing ([Schritte 2.2 bis 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)) behandelt. Schritt 2.1 (Hinzufügen des BrazeLocation-Moduls) ist für React Native nicht erforderlich, da BrazeLocation bereits implizit im Braze React Native SDK enthalten ist.

1. **Update`build.gradle`:** Bitte `android-sdk-location`fügen Sie die Standortdienste von Google Play Services hinzu. Siehe [Android-Geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
2. **Bitte führen Sie ein Update des Manifests durch:** Bitte fügen Sie Standortberechtigungen und den Braze-Boot-Empfänger hinzu. Siehe [Android-Geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
3. **Bitte aktivieren Sie die Standortdatenerfassung von Braze:** Bitte führen Sie ein Update Ihrer`braze.xml`Datei durch. Siehe [Android-Geofences]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

### Schritt 3: Vollständige native iOS-Einrichtung

Da das React Native SDK das native Braze iOS SDK verwendet, führen Sie bitte die Einrichtung der nativen iOS-Geofence für Ihr Projekt durch, indem Sie die Anweisungen für das native SWIFT SDK ab Schritt 2.2 befolgen: Aktualisieren Sie Ihre`Info.plist`App mit Beschreibungen zur Nutzung der Standorte (Schritt 2.2) und aktivieren Sie Geofences in Ihrer Braze-Konfiguration, einschließlich`automaticGeofenceRequests = true`App (Schritt 3); optional können Sie die Hintergrundberichterstattung aktivieren (Schritt 3.1). Schritt 2.1 (Hinzufügen des BrazeLocation-Moduls) ist nicht erforderlich – BrazeLocation ist bereits implizit im Braze React Native SDK enthalten. Siehe [iOS-Geofences, Schritte 2.2 bis 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module).

### Schritt 4: Geofences über JavaScript als Anfrage anfordern

**Auf Android:** Nachdem die Nutzer:innen die Standortberechtigungen erteilt haben, rufen Sie die Funktion auf, um die `requestLocationInitialization()`Standort-Features von Braze zu initialisieren und Geofences von den Braze-Servern anzufordern. Diese Methode wird unter iOS nicht unterstützt und ist für iOS nicht erforderlich.

**Auf iOS:** Das Äquivalent besteht darin, die`automaticGeofenceRequests`Konfiguration in Ihrer nativen SWIFT- oder Objective C-Braze-Konfiguration zu aktivieren (siehe Schritt 3). Wenn diese Funktion aktiviert ist, fordert das SDK automatisch Geofences an und überwacht sie, sobald der Standort verfügbar ist. Eine JavaScript-Anfrage, die  entspricht,`requestLocationInitialization`ist nicht erforderlich.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Schritt 5: Geofences manuell anfragen (optional)

Sowohl auf iOS als auch auf Android können Sie manuell eine Geofence-Update-Anfrage für eine bestimmte GPS-Koordinate stellen, indem Sie `requestGeofences`. Standardmäßig ruft Braze automatisch den Standort des Geräts ab und stellt Anfragen für Geofences. Um stattdessen manuell eine Koordinate anzugeben:

1. Deaktivieren Sie automatische Geofence-Anfragen. Bitte stellen Sie auf Android in Ihrer Konfiguration`false``braze.xml` auf ein`com_braze_automatic_geofence_requests_enabled`. Bitte stellen Sie in Ihrer Braze-Konfiguration`automaticGeofenceRequests``false` unter iOS die Option auf ein.
2. Bitte rufen Sie`requestGeofences`mit den gewünschten Breiten- und Längengraden an:

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
Geofences können nur einmal pro Sitzung angefordert werden. Dies kann entweder automatisch durch das SDK oder manuell mit dieser Methode geschehen.
{% endalert %}
