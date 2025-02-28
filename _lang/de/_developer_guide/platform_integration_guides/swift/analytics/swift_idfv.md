---
nav_title: IDFV einsammeln
article_title: IDFV einsammeln
platform: Swift
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie das optionale IDFV-Feld für das Swift SDK erfassen."
page_order: 4

---

# IDFV einsammeln 

## Hintergrund

In früheren Versionen des Braze iOS SDK wurde das Feld IDFV (Identifier for Vendors) automatisch als Geräte-ID des Nutzers erfasst. Ab Swift SDK v5.7.0 wurde das IDFV-Feld optional deaktiviert. Stattdessen setzte Braze eine zufällige UUID als Geräte ID. Ab Swift SDK v7.0.0 wird das IDFV-Feld standardmäßig nicht mehr erfasst. Stattdessen wird eine UUID als Geräte-ID gesetzt.

Das Feature `useUUIDAsDeviceId` konfiguriert das [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) so, dass die Geräte-ID als UUID gesetzt wird. Traditionell würde das iOS SDK den von Apple generierten IDFV-Wert als Geräte-ID zuweisen. Wenn diese Funktion in Ihrer iOS-App standardmäßig aktiviert ist, wird allen neuen Benutzern, die über das SDK erstellt werden, eine Geräte-ID zugewiesen, die einer UUID entspricht.

Wenn Sie den IDFV-Wert weiterhin separat erfassen möchten, können Sie das über das Swift SDK tun. Eine Beschreibung dazu finden Sie [hier](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

## Überlegungen

### SDK Version

Wenn `useUUIDAsDeviceId` in Swift SDK v7.0.0+ aktiviert ist (Standardeinstellung), wird allen neu angelegten Nutzern eine zufällige Geräte ID zugewiesen. Für alle bereits bestehenden Nutzer wird der Wert der Geräte-ID, was möglicherweise der IDFV war, beibehalten.

Wenn dieses Feature deaktiviert ist, wird den Geräten bei der Erstellung weiterhin der IDFV zugewiesen.

### Downstream 

**Technologie-Partner**: Wenn dieses Feature aktiviert ist, haben alle Technologiepartner, die den IDFV-Wert von der Braze Geräte-ID ableiten, keinen Zugriff mehr auf diese Daten. Wenn der vom Gerät abgeleitete IDFV-Wert für Ihre Partnerintegration benötigt wird, empfehlen wir Ihnen, dieses Feature auf true zu setzen.

**Currents**: `useUUIDAsDeviceId` auf true gesetzt bedeutet, dass die in Currents gesendete Geräte-ID nicht mehr dem IDFV-Wert entspricht.

## Häufig gestellte Fragen

#### Wird sich diese Änderung auf meine bestehenden Benutzer in Braze auswirken?
Nein. Wenn diese Funktion aktiviert ist, überschreibt sie keine Benutzerdaten in Braze. Neue UUID-Geräte-IDs werden nur von neu erstellten Geräten – oder nach dem Aufruf von `wipedata()` – generiert.

#### Kann ich diese Funktion ausschalten, nachdem ich sie eingeschaltet habe?
Ja, diese Funktion kann nach Ihrem Ermessen ein- und ausgeschaltet werden. Zuvor gespeicherte Geräte-IDs werden niemals überschrieben.

#### Kann ich den IDFV-Wert auch anderweitig über Braze erfassen?
Ja, Sie können den IDFV weiterhin optional über das Swift SDK erfassen (die Erfassung ist standardmäßig deaktiviert). 
