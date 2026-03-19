{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Festlegen des letzten bekannten Standorts

Um den letzten bekannten Standort einer Nutzer:in manuell festzulegen, verwenden Sie bitte die`setLastKnownLocation`Methode. Dies ist nützlich, wenn Sie Standortdaten außerhalb des Braze SDK erfassen.

```javascript
Braze.setLastKnownLocation(LATITUDE, LONGITUDE, ALTITUDE, HORIZONTAL_ACCURACY, VERTICAL_ACCURACY);
```

- Auf Android sind`latitude`  `longitude`und  erforderlich. `altitude`,`horizontalAccuracy`  und`verticalAccuracy`  sind optional.
- Unter iOS sind ,`latitude` `longitude``horizontalAccuracy`, und erforderlich.`altitude`  und`verticalAccuracy`  sind optional.

Für plattformübergreifende Kompatibilität stellen Sie bitte `horizontalAccuracy`mindestens ,`longitude` , und zur Verfügung`latitude`.

## Festlegen eines angepassten Standort-Attributs

Um ein angepasstes Attribut für den Standort in einem Nutzerprofil festzulegen, verwenden Sie bitte die`setLocationCustomAttribute`Methode.

```javascript
Braze.setLocationCustomAttribute("favorite_restaurant", 40.7128, -74.0060, optionalCallback);
```

## Anfrage der Standortinitialisierung (nur Android)

Bitte rufen Sie diese Funktion`requestLocationInitialization` auf, nachdem eine Nutzer:in Standortberechtigungen erteilt hat, um die Standort-Features von Braze auf Android zu initialisieren. Diese Methode wird unter iOS nicht unterstützt und ist für Geofence- oder Standort-Features unter iOS nicht erforderlich.

```javascript
Braze.requestLocationInitialization();
```

## Geofences

Geofences werden sowohl auf iOS als auch auf Android unterstützt. Standardmäßig kann das Braze SDK automatisch Geofences anfragen und überwachen, wenn der Standort verfügbar ist. Bei den meisten Integrationen können Sie sich auf diese automatische Konfiguration verlassen.

### Geofencing manuell anfordern

Um manuell ein Geofence-Update für eine bestimmte GPS-Koordinate anzufordern, verwenden Sie bitte`requestGeofences` . Dies ist sowohl für iOS als auch für Android verfügbar. Wenn Sie diese Methode verwenden, deaktivieren Sie bitte die automatischen Geofence-Anfragen in Ihrer nativen Konfiguration, damit das SDK Ihre manuellen Anfragen nicht überschreibt.

```javascript
Braze.requestGeofences(LATITUDE, LONGITUDE);
```
