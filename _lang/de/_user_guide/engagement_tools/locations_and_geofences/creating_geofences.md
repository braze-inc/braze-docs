---
nav_title: Geofences erstellen
article_title: Geofences erstellen
page_order: 1
page_type: reference
toc_headers: h2
description: "Erfahren Sie, wie Sie Standortberechtigungen einrichten, einen Standortberechtigungs-Primer erstellen und Geofences für standortbasierte Kampagnen aufbauen."
tool: 
  - Location
search_rank: 9
---

# Geofences

> Ein Geofence ist ein virtuelles geografisches Gebiet, das als Breiten- und Längengrad in Kombination mit einem Radius dargestellt wird und einen Kreis um eine bestimmte globale Position bildet. Geofences können von der Größe eines Gebäudes bis zur Größe einer ganzen Stadt reichen. Sie können Geofences verwenden, um Kampagnen in Realtime zu triggern, wenn Nutzer:innen ihre Grenzen betreten oder verlassen, oder um Folgekampagnen Stunden oder Tage später zu senden.

{% alert tip %}
Eine geführte Anleitung finden Sie im Braze-Lernkurs [Create a Geofence](https://learning.braze.com/create-a-geofence).
{% endalert %}

## So funktioniert es

Geofences sind in Geofence-Sets organisiert – einer Gruppe von Geofences, die Sie verwenden können, um Nutzer:innen auf der gesamten Plattform zu segmentieren oder einzubinden. Jedes Geofence-Set kann maximal 10.000 Geofences enthalten. Sie können eine unbegrenzte Anzahl von Geofences erstellen oder hochladen.

Nutzer:innen, die Ihre Geofences betreten oder verlassen, fügen eine neue Ebene von Nutzerdaten hinzu, die Sie für die Segmentierung und das Re-Targeting verwenden können.

Beachten Sie die folgenden Gerätelimits:

- Android-Apps können jeweils nur bis zu 100 Geofences lokal speichern. Braze ist so konfiguriert, dass nur bis zu 20 Geofences pro App lokal gespeichert werden.
- iOS-Geräte können bis zu 20 Geofences pro App gleichzeitig überwachen. Braze überwacht bis zu 20 Standorte, sofern Platz vorhanden ist.
- Wenn die:der Nutzer:in für mehr als 20 Geofences berechtigt ist, lädt Braze die maximale Anzahl von Standorten basierend auf der Nähe zur:zum Nutzer:in bei Sitzungsbeginn herunter.
- Damit Geofences korrekt funktionieren, stellen Sie sicher, dass Ihre App nicht alle verfügbaren Geofence-Spots nutzt.

Die folgende Tabelle beschreibt gängige Geofence-Begriffe:

| Begriff | Beschreibung |
|---|---|
| Breiten- und Längengrad | Der geografische Mittelpunkt des Geofence. |
| Radius | Der Radius des Geofence in Metern, gemessen vom geografischen Zentrum. Legen Sie für alle Geofences einen Mindestradius von 100 bis 150 Metern fest. |
| Cooldown | Nutzer:innen erhalten durch Geofence getriggerte Benachrichtigungen, nachdem sie einzelne Geofences betreten oder verlassen haben. Nach einem Übergang gibt es einen vordefinierten Zeitraum, in dem die:der Nutzer:in denselben Übergang an diesem einzelnen Geofence nicht erneut durchführen kann. Dieser „Cooldown" ist von Braze vordefiniert und dient hauptsächlich dazu, unnötige Netzwerkanfragen zu verhindern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Voraussetzungen

### SDK- und Plattformanforderungen

Durch Geofence getriggerte Kampagnen sind auf iOS und Android verfügbar. Um Geofences zu unterstützen, ist Folgendes erforderlich:

* Ihre Integration muss Push-Benachrichtigungen im Hintergrund unterstützen.
* Braze Geofences oder die Standorterfassung müssen aktiviert sein.
* Die:der Nutzer:in muss den Standortzugriff „Immer erlauben" gewähren.

{% alert important %}
Die Braze-Standorterfassung ist standardmäßig deaktiviert. Um zu überprüfen, ob sie unter Android aktiviert ist, vergewissern Sie sich, dass `com_braze_enable_location_collection` in Ihrer `braze.xml` auf `true` gesetzt ist.
{% endalert %}

Plattformspezifische Einrichtungsanweisungen finden Sie unter [Geofences]({{site.baseurl}}/developer_guide/geofences/) im Entwicklerhandbuch.

### Standortberechtigungen

Bevor Ihre Geofences funktionieren können, müssen Nutzer:innen Ihrer App die Berechtigung zum Zugriff auf ihren Standort erteilen. Das Verständnis der verschiedenen Berechtigungsstufen und ihrer Auswirkungen auf Geofencing ist entscheidend für den Aufbau einer effektiven standortbasierten Strategie.

## Standortberechtigungen verstehen

Sowohl iOS als auch Android bieten mehrere Stufen des Standortzugriffs. Die Berechtigungsstufe, die eine:ein Nutzer:in gewährt, beeinflusst direkt, ob Geofencing funktioniert und wie genau die Standortdaten sind.

### Berechtigungsstufen

{% tabs local %}
{% tab iOS %}

| Berechtigung | Beschreibung | Geofencing-Unterstützung |
|---|---|---|
| **Einmal erlauben** | Gewährt Standortzugriff für eine einzelne Sitzung. Die Abfrage erscheint erneut, wenn die:der Nutzer:in die App das nächste Mal öffnet. | Nein. Hintergrund-Tracking ist deaktiviert, sodass das Gerät nur Standort-Updates erhält, wenn die App geöffnet ist. |
| **Bei Nutzung der App erlauben** | Gewährt Standortzugriff, wenn die App im Vordergrund ist. Nachdem dies gewährt wurde, kann iOS eine Folgeabfrage anzeigen, die die:den Nutzer:in auffordert, auf „Immer erlauben" zu upgraden. | Ja. iOS aktiviert die Standortüberwachung im Hintergrund, einschließlich Geofence-Übergänge, für Apps mit dieser Berechtigung. |
| **Immer erlauben** | Gewährt kontinuierlichen Standortzugriff, auch im Hintergrund und wenn die App geschlossen ist. | Ja. Dies bietet die zuverlässigste Geofence-Überwachung. |
| **Nicht erlauben** | Verweigert jeglichen Standortzugriff. | Nein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Android %}

| Berechtigung | Beschreibung | Geofencing-Unterstützung |
|---|---|---|
| **Bei Nutzung der App** | Gewährt Standortzugriff, während die App im Vordergrund ist. | Nein. Unter Android ist der Standortzugriff im Hintergrund für die Geofence-Überwachung erforderlich. |
| **Immer erlauben** | Gewährt kontinuierlichen Standortzugriff, auch im Hintergrund. Ab Android 10 erfordert dies eine separate Abfrage, nachdem die anfängliche Berechtigung „Bei Nutzung der App" gewährt wurde. | Ja. Dies ist für Geofencing unter Android erforderlich. |
| **Nicht erlauben** | Verweigert jeglichen Standortzugriff. Ab Android 13 blockiert das Betriebssystem weitere In-App-Abfragen, wenn eine:ein Nutzer:in die Standortabfrage zweimal ablehnt. | Nein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Genauer vs. ungefährer Standort

Ab iOS 14+ und Android 12+ können Nutzer:innen zwischen genauem und ungefährem Standort wählen.

| Einstellung | Genauigkeit | Auswirkung auf Geofencing |
|---|---|---|
| **Genauer Standort (ein)** | Genauigkeit im Bereich von 5 bis 50 Metern, unter Verwendung von GPS, WLAN und Mobilfunk-Triangulation. | Geofences funktionieren wie erwartet. Empfohlen für alle Geofence-basierten Anwendungsfälle. |
| **Ungefährer Standort (aus)** | Genauigkeit von etwa 3 Quadratkilometern (ca. 1 Quadratmeile). Das Gerät gibt einen allgemeinen Bereich statt exakter Koordinaten zurück. | Geofences werden nicht zuverlässig getriggert. Das Gerät kann nicht genau bestimmen, ob sich eine:ein Nutzer:in innerhalb oder außerhalb einer Geofence-Grenze befindet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Damit Geofencing zuverlässig funktioniert, müssen Nutzer:innen den genauen Standort aktivieren. Nehmen Sie diesen Hinweis in Ihre Standortberechtigungs-Primer-Nachrichten auf, damit Nutzer:innen verstehen, warum der genaue Standort wichtig ist.
{% endalert %}

## Einen Standortberechtigungs-Primer einrichten

Ein Standortberechtigungs-Primer ist eine In-App-Nachricht, die den Wert der Standortfreigabe erklärt, bevor die:der Nutzer:in die native Betriebssystem-Berechtigungsabfrage sieht. Da die native Standortabfrage nur einmal (auf iOS) oder eine begrenzte Anzahl von Malen (auf Android) angezeigt werden kann, erhöht das vorherige Priming der Nutzer:innen die Opt-in-Raten.

### 1. Schritt: Mit Ihrem Entwicklungsteam zusammenarbeiten

Da Braze In-App-Nachrichten keine integrierte Button-Aktion zum Aufrufen der nativen Standortberechtigungsabfrage enthalten, muss Ihr Entwicklungsteam die Standortberechtigungen auf der Geräteseite handhaben. Bevor Sie die In-App-Nachricht in Braze erstellen, stimmen Sie sich mit Ihrem Entwicklungsteam ab, um Deeplinks einzurichten, die Ihre In-App-Nachricht aufrufen kann. Die spezifische Implementierung hängt von der Architektur Ihrer App ab, aber gängige Ansätze umfassen:

- Einen Deeplink, der die native Standortberechtigungsabfrage innerhalb Ihrer App triggert.
- Einen Deeplink, der die Standorteinstellungsseite der App in den Betriebssystemeinstellungen des Geräts öffnet, was nützlich ist, um Nutzer:innen erneut aufzufordern, die zuvor ihre Berechtigungen verweigert oder eingeschränkt haben.

Weitere Informationen zu Deeplinks finden Sie unter [Deeplinking zu In-App-Inhalten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/). Plattformspezifische Anleitungen zur Standort- und Geofence-Integration finden Sie unter [Geofences]({{site.baseurl}}/developer_guide/geofences/) im Entwicklerhandbuch.

### 2. Schritt: Die Standort-Primer-In-App-Nachricht erstellen

Erstellen Sie eine In-App-Nachricht-Kampagne, die den Wert des Standortzugriffs erklärt. Alle In-App-Nachrichtentypen unterstützen dieses Opt-in, einschließlich Drag-and-Drop.

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign** > **In-App Message**.
2. Wählen Sie einen Nachrichtentyp und ein Layout. Ein **Modal**- oder **Full**-Layout gibt Ihnen mehr Platz, um die Vorteile zu erläutern.
3. Verfassen Sie eine Nachricht, die klar erklärt, warum der Standortzugriff für die:den Nutzer:in von Vorteil ist. Zum Beispiel:
    - „Aktivieren Sie den Standort, um über Angebote in Ihrer Nähe benachrichtigt zu werden."
    - „Schalten Sie den Standort ein, damit wir Ihnen mitteilen können, wenn Ihre Bestellung in Ihrem nächsten Shop zur Abholung bereit ist."
4. Fügen Sie einen primären Call-to-Action-Button hinzu (z. B. **Standort aktivieren**) und setzen Sie das Klickverhalten auf **Deep Link into App**, wobei Sie den Deeplink verwenden, den Ihr Entwicklungsteam erstellt hat, um die native Standortabfrage zu triggern.
5. Fügen Sie einen sekundären Button hinzu (z. B. **Nicht jetzt**), der die Nachricht schließt.

### 3. Schritt: Die richtige Zielgruppe ansprechen

Für beste Ergebnisse zeigen Sie den Standort-Primer, wenn Nutzer:innen engagiert sind und wahrscheinlich einen Mehrwert in der Standortfreigabe sehen.

- **Sprechen Sie Nutzer:innen an, die noch keinen Standortzugriff gewährt haben.** Arbeiten Sie mit Ihrem Entwicklungsteam zusammen, um den besten Weg zu finden, Nutzer:innen basierend auf ihrem Standortberechtigungsstatus zu tracken und zu segmentieren.
- **Zeigen Sie den Primer nach einer hochwertigen Aktion,** wie dem Abschluss eines Kaufs, dem Speichern eines Shops als Favorit oder dem Durchsuchen von Events in der Nähe. Nutzer:innen sind eher bereit, sich anzumelden, wenn sie den Vorteil verstehen.
- **Vermeiden Sie es, den Primer beim ersten Start zu zeigen.** Warten Sie, bis Nutzer:innen genug Mehrwert aus der App erfahren haben, um ein personalisierteres Erlebnis zu wünschen.

### 4. Schritt: Die empfohlene Berechtigungsstufe fördern

Ihre Primer-Nachricht sollte Nutzer:innen ermutigen, die Berechtigungsstufe zu gewähren, die Geofencing ermöglicht:

- **Auf iOS** ermutigen Sie Nutzer:innen, mindestens **Bei Nutzung der App erlauben** auszuwählen. iOS kann die:den Nutzer:in später von sich aus auffordern, auf **Immer erlauben** zu upgraden. Sie können auch mit einer separaten Kampagne nachfassen, um zu erklären, warum „Immer erlauben" das beste Erlebnis bietet.
- **Auf Android** ermutigen Sie Nutzer:innen, **Immer erlauben** zu gewähren. Ab Android 10 muss die:der Nutzer:in zuerst „Bei Nutzung der App" gewähren und dann „Immer erlauben" in einer separaten Folgeabfrage. Führen Sie sie durch beide Schritte.

Erinnern Sie Nutzer:innen in beiden Fällen daran, den **genauen Standort** für das beste Erlebnis aktiviert zu lassen.

## Nutzer:innen zu den Betriebssystemeinstellungen weiterleiten

Wenn eine:ein Nutzer:in den Standortzugriff zuvor verweigert oder eine eingeschränkte Berechtigung gewählt hat, können Sie die native Abfrage auf den meisten Betriebssystemversionen nicht erneut aus der App heraus triggern. Leiten Sie sie stattdessen dazu an, ihre Berechtigungen in den Geräteeinstellungen zu aktualisieren.

Verwenden Sie einen Deeplink in einer benutzerdefinierten [In-App-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), um die:den Nutzer:in zur Standorteinstellungsseite der App im Betriebssystem zu navigieren. Ihr Entwicklungsteam kann einen Deeplink dafür als Teil der Standortberechtigungshandhabung Ihrer App einrichten (siehe [1. Schritt](#step-1-work-with-your-development-team)).

Beachten Sie beim Erstellen dieser In-App-Nachricht Folgendes:

- **Wann anzeigen:** Sprechen Sie Nutzer:innen an, die die Berechtigung „Bei Nutzung der App" haben, wenn Sie „Immer erlauben" benötigen, oder Nutzer:innen, die den Standortzugriff zuvor verweigert haben.
- **Nachrichtenbeispiel:** „Um standortbasierte Features optimal zu nutzen, aktualisieren Sie Ihre Standorteinstellungen auf ‚Immer erlauben'. Tippen Sie unten, um zu den Einstellungen zu gelangen."

{% alert tip %}
Sie können diese In-App-Nachricht an jedem Punkt der User Journey triggern – nach einem Kauf, beim Durchsuchen von Inhalten in der Nähe oder als Teil eines Canvas-Flows. Seien Sie selektiv beim erneuten Auffordern: Beschränken Sie diese Kampagnen auf treue oder stark engagierte Nutzer:innen, um Opt-in-Müdigkeit zu vermeiden.
{% endalert %}

## Beispielstrategien für Standort-Priming

### „Bei Nutzung der App"-Primer

Eine Einzelhandels-App zeigt eine modale In-App-Nachricht an, nachdem eine:ein Nutzer:in einen Shop als Favorit gespeichert hat:

- **Überschrift:** „Erhalten Sie Benachrichtigungen über Angebote im Shop"
- **Text:** „Schalten Sie den Standort ein, damit wir Ihnen exklusive Angebote senden können, wenn Sie in der Nähe Ihrer Lieblingsshops sind. Ihr Standort wird nur bei Nutzung der App abgerufen."
- **CTA:** **Standort aktivieren** verlinkt per Deeplink zur nativen Standortberechtigungsabfrage
- **Schließen:** **Vielleicht später** schließt die Nachricht

Dieser Ansatz ist effektiv, weil die:der Nutzer:in bereits Interesse an einem bestimmten Shop gezeigt hat, was einen natürlichen Kontext für die Standortberechtigungsanfrage schafft.

### „Immer erlauben"-Nachfassung

Nachdem eine:ein Nutzer:in die Berechtigung „Bei Nutzung der App" gewährt hat, zeigen Sie eine Folge-In-App-Nachricht während der nächsten Sitzung:

- **Überschrift:** „Verpassen Sie nie ein Angebot in der Nähe"
- **Text:** „Aktualisieren Sie Ihre Standorteinstellungen auf ‚Immer', damit wir Sie über Angebote benachrichtigen können, auch wenn Sie die App nicht nutzen. Wir senden nur relevante Hinweise, wenn Sie in der Nähe teilnehmender Standorte sind."
- **CTA:** **Einstellungen aktualisieren** verlinkt per Deeplink zur Standorteinstellungsseite der App im Betriebssystem
- **Schließen:** **Aktuelle Einstellungen beibehalten** schließt die Nachricht

Diese Nachfassung gibt der:dem Nutzer:in Kontext, warum das Upgrade auf „Immer erlauben" zusätzlichen Mehrwert über die anfängliche Berechtigungsstufe hinaus bietet.

## Geofences manuell erstellen

### 1. Schritt: Ein Geofence-Set erstellen

Um einen Geofence zu erstellen, erstellen Sie zunächst ein Geofence-Set.

1. Gehen Sie im Braze-Dashboard zu **Audience** > **Locations**.
2. Wählen Sie **Create Geofence Set**.
3. Geben Sie unter **Set name** einen Namen für Ihr Geofence-Set ein.
4. (Optional) Fügen Sie Tags hinzu, um Ihr Set zu filtern.

### 2. Schritt: Die Geofences hinzufügen

Fügen Sie als Nächstes Geofences zu Ihrem Geofence-Set hinzu.

1. Wählen Sie **Draw Geofence**, um den Kreis auf der Karte zu klicken und zu ziehen. Wiederholen Sie den Vorgang, um bei Bedarf weitere Geofences zu Ihrem Set hinzuzufügen.
2. (Optional) Wählen Sie **Edit** und ersetzen Sie die Geofence-Beschreibung durch einen Namen.
3. Wählen Sie **Save Geofence Set** zum Speichern.

{% alert tip %}
Erstellen Sie Geofences mit einem Radius von mindestens 200 Metern für optimale Funktionalität. Weitere Informationen finden Sie unter [Best Practices für Geofences](#geofence-best-practices).
{% endalert %}

![Ein Geofence-Set mit zwei Geofences „EastCoastGreaterNY" und „WesternRegion" mit zwei Kreisen auf der Karte.]({% image_buster /assets/img/geofence_example.png %})

## Geofences per Massenupload hochladen {#creating-geofence-sets-via-bulk-upload}

Sie können Geofences in großen Mengen als GeoJSON-Objekt vom Typ `FeatureCollection` hochladen. Jeder Geofence ist ein `Point`-Geometrietyp in der Feature-Sammlung. Die Eigenschaften für jedes Feature erfordern einen `radius`-Schlüssel und einen optionalen `name`-Schlüssel für jeden Geofence.

Um Ihre JSON-Datei hochzuladen, wählen Sie **More** > **Upload JSON**.

Beachten Sie beim Erstellen Ihrer Geofences die folgenden Details:

- Der `coordinates`-Wert im GeoJSON ist als `[Longitude, Latitude]` formatiert.
- Der maximale Geofence-Radius, der hochgeladen werden kann, beträgt 10.000 Meter (etwa 10 Kilometer oder 6,2 Meilen).

### Beispiel

Das folgende Beispiel zeigt das korrekte GeoJSON-Format zur Festlegung von zwei Geofences: einen für den Hauptsitz von Braze in NYC und einen für die Freiheitsstatue südlich von Manhattan.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.9853689, 40.7434683]
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

## Geofence-Events verwenden

Nachdem Sie Ihre Geofences konfiguriert haben, können Sie sie nutzen, um Ihre Kommunikation mit Nutzer:innen zu verbessern und zu bereichern.

### Kampagnen und Canvase triggern

Um Geofence-Daten als Teil von Kampagnen- und Canvas-Triggern zu verwenden, wählen Sie **aktionsbasierte Zustellung** als Zustellungsmethode. Fügen Sie dann die Aktion triggern `Trigger a Geofence` hinzu. Wählen Sie schließlich das Geofence-Set und die Geofence-Übergangs-Event-Typen für Ihre Nachricht. Sie können Nutzer:innen auch mit Geofence-Events durch ein Canvas voranbringen.

![Eine aktionsbasierte Kampagne mit einem Geofence, der getriggert wird, wenn eine:ein Nutzer:in deutsche Flughäfen betritt.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Nachrichten personalisieren

Um Geofence-Daten für die Personalisierung einer Nachricht zu verwenden, können Sie die folgende Liquid-Personalisierungssyntax verwenden:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Geofence-Sets aktualisieren

Das Braze SDK fragt Geofences nur einmal pro Tag bei Sitzungsbeginn ab. Wenn Sie nach dem Sitzungsbeginn Änderungen an den Geofence-Sets vornehmen, müssen Sie 24 Stunden ab dem Zeitpunkt warten, an dem die Sets zum ersten Mal heruntergeladen wurden, um das aktualisierte Set zu erhalten.

Wenn die:der Nutzer:in Hintergrund-Push aktiviert hat, sendet Braze alle 24 Stunden einen stillen Push, wenn Geofence-Sets aktualisiert werden, um die neuesten Standorte auf das Gerät herunterzuladen.

{% alert note %}
Wenn die Geofences nicht lokal auf das Gerät geladen werden, kann die:der Nutzer:in den Geofence nicht triggern, selbst wenn sie:er das Gebiet betritt.
{% endalert %}

## Best Practices für Geofences

### Geofence-Konfiguration

- Verwenden Sie einen Radius von 200 Metern oder mehr für zuverlässiges Triggern.
- Vermeiden Sie es, Geofences einzurichten, die sich überlappen oder ineinander verschachtelt sind, da dies zu Problemen beim Triggern führen kann.
- Ein Geofence kann ein Eintritts-Event nur einmal alle sechs Stunden triggern. Dieser Cooldown-Zeitraum wird lokal durchgesetzt. Wenn eine:ein Nutzer:in die App deinstalliert oder App-Daten löscht, werden alle Cooldowns zurückgesetzt.
- Maximal 20 Geofences können insgesamt auf einem Gerät gespeichert werden. Wenn die:der Nutzer:in für mehr als 20 berechtigt ist, lädt Braze die nächstgelegenen Standorte basierend auf der Nähe bei Sitzungsbeginn oder stiller Push-Aktualisierung herunter.
- Braze sendet nur Geofences innerhalb eines Radius von 2.000 Kilometern um die:den Nutzer:in an das Gerät.

### Geräteanforderungen

- Push-Berechtigungen und Standortberechtigungen müssen beide für die App aktiviert sein.
- Ein gültiger Vordergrund-Push-Token ist erforderlich.

{% alert note %}
Die grundlegende SDK-Integration aktiviert nur Standort-Tracking. Geofencing erfordert zusätzliche Einrichtungsschritte sowohl für iOS als auch für Android. Details finden Sie unter [Geofences]({{site.baseurl}}/developer_guide/geofences/) im Entwicklerhandbuch.
{% endalert %}

Sie können Geofences auch mit Braze-Technologiepartnern verwenden, wie [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) und [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/).

## Häufig gestellte Fragen

### Was ist der Unterschied zwischen Geofences und Standort-Tracking?

In Braze ist ein Geofence ein anderes Konzept als Standort-Tracking. Geofences werden als Auslöser für bestimmte Aktionen verwendet – wenn eine:ein Nutzer:in eine virtuelle Grenze betritt oder verlässt, die um einen geografischen Standort eingerichtet wurde, kann dies eine bestimmte Aktion auslösen, z. B. das Senden einer Nachricht.

Standort-Tracking erfasst und speichert die letzten Standortdaten einer:eines Nutzer:in. Diese Daten können verwendet werden, um Nutzer:innen basierend auf dem Filter `Most Recent Location` zu segmentieren. Sie können zum Beispiel den Filter `Most Recent Location` verwenden, um Nutzer:innen in New York anzusprechen.

Weitere Informationen finden Sie unter [Standort-Tracking]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### Wie genau sind Braze Geofences?

Braze Geofences verwenden eine Kombination aller für ein Gerät verfügbaren Standortanbieter, um den Standort der:des Nutzer:in zu triangulieren, einschließlich WLAN, GPS und Mobilfunktürme.

Die typische Genauigkeit liegt im Bereich von 20 bis 50 Metern, und die beste Genauigkeit liegt im Bereich von 5 bis 10 Metern. In ländlichen Gebieten kann sich die Genauigkeit erheblich verschlechtern, möglicherweise bis zu mehreren Kilometern. Erstellen Sie in ländlichen Gegenden Geofences mit größeren Radien.

Die Genauigkeit hängt auch davon ab, ob die:der Nutzer:in den genauen Standort aktiviert hat. Bei nur ungefährem Standort sinkt die Genauigkeit auf etwa 3 Quadratkilometer, was Geofences unzuverlässig macht. Weitere Informationen finden Sie unter [Genauer vs. ungefährer Standort](#precise-versus-approximate-location).

### Wie wirken sich Geofences auf die Akkulaufzeit aus?

Braze Geofencing verwendet den nativen Geofence-Systemdienst auf iOS und Android. Er ist so abgestimmt, dass er intelligent zwischen Genauigkeit und Energieverbrauch abwägt, Akkulaufzeit spart und die Performance verbessert, wenn sich der zugrunde liegende Dienst verbessert.

### Wann sind Geofences aktiv?

Braze Geofences funktionieren zu jeder Tageszeit, auch wenn Ihre App geschlossen ist. Sie werden aktiv, sobald sie definiert und in das Braze-Dashboard hochgeladen wurden. Geofences können jedoch nicht funktionieren, wenn eine:ein Nutzer:in das Standort-Tracking deaktiviert hat.

Damit Geofences funktionieren, müssen Nutzer:innen die Standortdienste auf ihrem Gerät aktiviert haben und Ihrer App die erforderliche Standortberechtigungsstufe gewährt haben. Weitere Informationen finden Sie unter [Standortberechtigungen verstehen](#understanding-location-permissions).

### Werden Geofence-Daten in Nutzerprofilen gespeichert?

Nein, Braze speichert keine Geofence-Daten in Nutzerprofilen. Geofences werden von den Standortdiensten von Apple und Google überwacht, und Braze wird nur benachrichtigt, wenn eine:ein Nutzer:in einen Geofence triggert. Zu diesem Zeitpunkt verarbeitet Braze alle zugehörigen Trigger-Kampagnen.

### Kann ich einen Geofence innerhalb eines Geofence einrichten?

Als Best Practice sollten Sie es vermeiden, Geofences einzurichten, die sich überlappen, da dies zu Problemen beim Triggern von Benachrichtigungen führen kann.

### Was passiert, wenn eine:ein Nutzer:in den Standortzugriff verweigert?

Ihr Entwicklungsteam kann einen Deeplink einrichten, der die Standorteinstellungsseite der App in den Betriebssystemeinstellungen öffnet, wo Nutzer:innen ihre Berechtigungen aktualisieren können. Sie können diesen Deeplink in einer benutzerdefinierten In-App-Nachricht an jedem Punkt der User Journey verwenden. Seien Sie selektiv, wann Sie diese Nachricht anzeigen – sprechen Sie Nutzer:innen an, die engagiert sind oder eine hochwertige Aktion durchgeführt haben, um die Chance auf ein Opt-in zu erhöhen. Weitere Informationen finden Sie unter [Nutzer:innen zu den Betriebssystemeinstellungen weiterleiten](#redirecting-users-to-os-settings).