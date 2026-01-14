---
nav_title: RudderStack
article_title: RudderStack
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und RudderStack, einer Öffnung für Kundendaten-Infrastrukturen, die eine nahtlose Integration von Braze für Ihre Android-, iOS- und Internet-Anwendungen bietet. Mit Rudderstack können Sie die Daten Ihrer In-App-Kundendaten direkt an Braze senden, um sie kontextuell zu analysieren."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) ist eine quelloffene Infrastruktur für Kundendaten zum Sammeln und Weiterleiten von Kundendaten an Ihr bevorzugtes Data Warehouse und Dutzende anderer Analytics-Anbieter, wie z.B. Braze. Es ist unternehmenstauglich und bietet ein robustes Transformations-Framework, mit dem Sie Ihre Ereignisdaten im Handumdrehen verarbeiten können.

Die Integration von Braze und Rudderstack bietet eine native SDK-Integration für Ihre Android-, iOS- und Internet-Anwendungen sowie eine Server-zu-Server-Integration von Ihren Backend-Diensten.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Rudderstack Konto | Sie benötigen ein [Rudderstack-Konto](https://app.rudderstack.com/), um die Vorteile dieser Partnerschaft zu nutzen. |
| Konfigurierte Quelle | Eine [Quelle](https://www.rudderstack.com/docs/dashboard-guides/sources/) ist im Wesentlichen die Herkunft aller Daten, die an Rudderstack gesendet werden, wie Websites, mobile Apps oder Backend-Server. Bevor Sie Braze als Ziel in Rudderstack einrichten, müssen Sie die Quelle konfigurieren. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `users.identify`, `users.delete`, und `users.alias.new`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze App Schlüssel | Um Ihren App-Schlüssel im Braze-Dashboard zu erhalten, gehen Sie zu **Einstellungen** > **App-Einstellungen** > **Identifizierung** und suchen Sie den Namen Ihrer App. Speichern Sie den zugehörigen Bezeichner String.
| Datenzentrum | Ihr Datenzentrum stimmt mit Ihrer Braze-Dashboard-[Instanz]({{site.baseurl}}/api/basics/#endpoints) überein.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Eine Quelle hinzufügen

Um mit dem Senden von Daten an Braze zu beginnen, müssen Sie zunächst sicherstellen, dass eine Quelle in Ihrer Rudderstack App eingerichtet ist. Besuchen Sie [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started), um zu erfahren, wie Sie Ihre Datenquelle einrichten.

### Schritt 2: Ziel konfigurieren

Da Ihre Datenquelle nun eingerichtet ist, wählen Sie im Rudderstack Dashboard unter **Ziele** **ZIELE HINZUFÜGEN** aus. Wählen Sie aus der Liste der verfügbaren Ziele **Braze** aus und klicken Sie auf **Weiter**.

Geben Sie im Ziel Braze den App-Schlüssel, den REST API-Schlüssel von Braze, den Daten-Cluster und die native SDK-Option (nur im Gerätemodus) an. Die Option Natives SDK verwendet das native SDK von Braze zum Senden von Ereignissen, wenn Sie diese Option umschalten. 

![]({% image_buster /assets/img/RudderStack/braze_settings.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

### Schritt 3: Wählen Sie die Art der Integration

Sie können die web- und nativen Client-seitigen Bibliotheken von Rudderstack auf eine der folgenden Arten in Braze integrieren:

- [Side-by-Side / Gerät-Modus](#device-mode)**:** Rudderstack sendet die Ereignisdaten direkt von Ihrem Client (Browser oder mobile Anwendung) an Braze.
- [Server-zu-Server / Cloud-Modus](#cloud-mode)**:** Das Braze SDK sendet die Ereignisdaten direkt an Rudderstack, die dann transformiert und an Braze weitergeleitet werden.
- [Hybrid-Modus](#hybrid-mode)**:** Verwenden Sie den Hybrid-Modus, um mit iOS und Android automatisch und von Nutzer:innen generierte Ereignisse über eine einzige Verbindung an Braze zu senden.

{% alert note %}
Erfahren Sie mehr über die [Verbindungsmodi](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) von Rudderstack und die Vorteile der einzelnen Modi.
{% endalert %}

#### Side-by-side-Integration (Geräte-Modus) {#device-mode}

In diesem Modus können Sie Ihre Ereignisse mit dem Braze SDK, das Sie auf Ihrer Website oder in Ihrer mobilen App eingerichtet haben, an Braze senden.

Richten Sie die Abbildungen zum Rudderstack SDK für Ihre Plattform im Braze GitHub Repository ein, wie unter [Unterstützte Methoden](#supported-methods) beschrieben:

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Schnell](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Internet](https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Um die Integration des Gerätemodus abzuschließen, lesen Sie die ausführliche Rudderstack-Anleitung zum [Hinzufügen von Braze zu Ihrem Projekt](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Server-zu-Server-Integration (Cloud-Modus) {#cloud-mode}

In diesem Modus sendet das SDK die Ereignisdaten direkt an den Rudderstack Server. Rudderstack transformiert dann diese Daten und leitet sie an das gewünschte Ziel weiter. Diese Transformation wird im Backend von Rudderstack mithilfe des Transformer-Moduls von Rudderstack durchgeführt.

Um die Integration zu aktivieren, müssen Sie die Rudderstack-Methoden auf Braze abbilden, wie unter [Unterstützte Methoden](#supported-methods) beschrieben.

{% alert note %}
Die Server-seitigen SDKs von Rudderstack (Java, Python, Node.js, Go, Ruby) unterstützen nur den Cloud-Modus. Das liegt daran, dass ihre Server-seitigen SDKs im Rudderstack Backend arbeiten und kein Braze-spezifisches SDK laden können.
{% endalert %}

{% alert important %}
Die Server-zu-Server Integration unterstützt keine Braze UI Features, wie Push-Benachrichtigungen oder In-App Messaging. Diese Features werden jedoch von der Integration des Gerätemodus unterstützt.
{% endalert %}

#### Hybrid-Modus {#hybrid-mode}

Verwenden Sie den Hybrid-Modus, um alle Ereignisse von Ihren iOS- und Android-Quellen an Braze zu senden. 

Wenn Sie den Hybridmodus wählen, um Ereignisse an Braze zu senden, wird Rudderstack:
1. Initialisiert das Braze SDK.
2. Sendet alle vom Nutzer:innen erzeugten Ereignisse (Bezeichner, Tracking, Seite, Bildschirm und Gruppe) nur über den Cloud-Modus an Braze und verhindert, dass sie über den Gerätemodus gesendet werden.
3. Sendet die automatisch generierten Ereignisse (In-App-Nachrichten, Push-Benachrichtigungen, die das Braze SDK erfordern) über den Gerätemodus.

Um [Ereignisse über den Hybridmodus zu senden](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), verwenden Sie die Option Hybridmodus, während Sie Ihre Quelle mit dem Braze-Ziel verbinden. Fügen Sie dann die Integration von Braze zu Ihrem Projekt hinzu.

## Schritt 4: Konfigurieren Sie zusätzliche Einstellungen

Nach Abschluss der Ersteinrichtung konfigurieren Sie die folgenden Einstellungen, um Ihre Daten in Braze korrekt zu empfangen:

- **Enablement von Abo-Gruppen im Gruppenruf**: Aktivieren Sie diese Einstellung, um den Abo-Gruppenstatus in Ihren Gruppenereignissen zu senden. Weitere Informationen finden Sie unter [Gruppe](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Angepasste Attribute verwenden Operation**: Aktivieren Sie diese Einstellung, wenn Sie die [verschachtelten angepassten Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) in Braze nutzen möchten, um Segmente zu erstellen und Ihre Nachrichten mithilfe eines angepassten Attributs zu personalisieren. Weitere Informationen finden Sie unter [Senden von Nutzer:innen als verschachtelte angepasste Attribute](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Tracking von Ereignissen für anonyme Nutzer:innen**: Aktivieren Sie diese Einstellung, um anonyme Nutzer:in-Aktivitäten zu tracken und diese Informationen an Braze zu senden.

### Einstellungen des Gerätemodus

Die folgenden Einstellungen gelten nur, wenn Sie Ereignisse über den [Gerätemodus](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode) an Braze senden:

- **Client-seitige Filterung von Ereignissen**: Mit dieser Einstellung können Sie festlegen, welche Ereignisse für Braze gesperrt oder zugelassen werden sollen. Weitere Informationen zu dieser Einstellung finden Sie unter [Client-seitiges Filtern von Ereignissen](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Eigenschaften deduplizieren**: Aktivieren Sie diese Einstellung, um die Nutzer:innen in der [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify) Aufruf.
- **Braze-Protokolle anzeigen**: Diese Einstellung gilt nur, wenn Sie das [JavaScript SDK](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) als Quelle verwenden. Enablement, um die Braze-Protokolle für Ihre Nutzer:innen anzuzeigen.
- **OneTrust Cookie Kategorien**: Mit dieser Einstellung können Sie die [OneTrust-Cookie-Zustimmungsgruppen](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) mit Braze verknüpfen.

## Unterstützte Methoden

Braze unterstützt die Rudderstack-Methoden identify, track, screen, page, group und alias.

{% tabs %}
{% tab Identifizieren %}

Die Rudderstack-[Methode `identify`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) verbindet Nutzer:innen mit ihren Aktionen. Rudderstack erfasst eine eindeutige Nutzer:innen ID und optionale Merkmale wie Name, E-Mail, IP-Adresse, etc.

**Delta-Verwaltung für Bezeichner-Anrufe**<br>
Wenn Sie Ereignisse über den Gerätemodus an Braze senden, können Sie Kosten sparen, indem Sie Ihre `identify` Anrufe deduplizieren. Aktivieren Sie dazu die Dashboard-Einstellung Traits deduplizieren. Rudderstack sendet dann nur die geänderten oder modifizierten Attribute (Traits) an Braze.

**Nutzer:in löschen**<br>
Sie können einen Nutzer:innen in Braze mit der [Verordnung Unterdrückung mit Löschen](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) der Rudderstack [Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/) löschen.

{% endtab %}
{% tab Tracking %}

Die [Methode`track` ](https://rudderstack.com/docs/destinations/marketing/braze/#track) von Rudderstack erfasst alle Nutzer:innen und die mit diesen Aktivitäten verbundenen Eigenschaften.

**Bestellung abgeschlossen**<br>
Wenn Sie die [RudderStack eCommerce API](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) verwenden, um die Tracking-Methode für ein Ereignis mit dem Namen `Order Completed` aufzurufen, sendet RudderStack die in diesem Ereignis aufgeführten Produkte an Braze als [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

{% endtab %}
{% tab Bildschirm %}

Mit der [Methode`screen` ](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) von Rudderstack können Sie die mobilen Bildschirmansichten Ihrer Nutzer:innen mit allen zusätzlichen Informationen über den betrachteten Bildschirm aufzeichnen.

{% endtab %}
{% tab Seite %}

Mit der [Methode`page` ](https://rudderstack.com/docs/destinations/marketing/braze/#page) von Rudderstack können Sie die Seitenaufrufe Ihrer Website aufzeichnen. Außerdem werden alle anderen relevanten Informationen über diese Seite erfasst.

{% endtab %}
{% tab Gruppe %}

Mit der [Methode`group` ](https://rudderstack.com/docs/destinations/marketing/braze/#group) von Rudderstack können Sie einen Nutzer:innen mit einer Gruppe verknüpfen.

**Status der Abonnementgruppe**<br>
Um den Abo-Gruppenstatus zu aktualisieren, aktivieren Sie im Rudderstack Dashboard die Einstellung "Abo-Gruppen in Gruppenanruf aktivieren" und senden Sie den Abo-Gruppenstatus im Gruppenanruf.

{% endtab %}
{% tab Alias %}

Die [Methode`alias` ](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) von Rudderstack erlaubt es Ihnen, verschiedene Identitäten eines bekannten Nutzer:innen zusammenzuführen. Beachten Sie, dass Rudderstack den Alias-Aufruf für Braze nur im Cloud-Modus unterstützt.

{% endtab %}
{% endtabs %}

## Senden Sie Nutzer:innen als verschachtelte angepasste Attribute

Sie können die Eigenschaften der Nutzer:innen als verschachtelte angepasste Attribute an Braze senden und diese hinzufügen, aktualisieren und entfernen. Aktivieren Sie dazu die Einstellung "Angepasste Attribute Operation Dashboard verwenden" in Rudderstack, während Sie das Braze-Ziel konfigurieren. Dieses Feature ist nur im Cloud-Modus verfügbar.

Sie können die Nutzer:in als verschachtelte angepasste Attribute in Ihren `identify` Events in folgendem Format senden:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Mike"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

Um die Benutzermerkmale als angepasste Attribute über die Aufrufe `track`, `page` oder `screen` zu senden, übergeben Sie `traits` als kontextuelles Feld im Event:
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Mike"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
Für die Vorgänge Update und Entfernen ist `identifier` ein erforderlicher Schlüssel. Wenn in dem verschachtelten Array keine Operationen zum Hinzufügen, Aktualisieren oder Entfernen vorhanden sind, verwendet Rudderstack standardmäßig die Operation create, um die Eigenschaften zu erstellen. Weitere Informationen zum Senden von verschachtelten angepassten Attributen finden Sie unter [Array von Objekten]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).
{% endalert %}

