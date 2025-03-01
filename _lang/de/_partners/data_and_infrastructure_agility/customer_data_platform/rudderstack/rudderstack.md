---
nav_title: RuderStack
article_title: RuderStack
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und RudderStack, einer Open-Source-Kundendateninfrastruktur, die eine nahtlose Braze-Integration für Ihre Android-, iOS- und Webanwendungen bietet. Mit RudderStack können Sie Ihre In-App-Kundenereignisdaten zur kontextbezogenen Analyse direkt an Braze senden."
page_type: partner
search_tag: Partner

---

# RuderStack

> [RudderStack][1] ist eine Open-Source-Kundendateninfrastruktur zum Sammeln und Weiterleiten von Kundenereignisdaten an Ihr bevorzugtes Data Warehouse und Dutzende von anderen Analyseanbietern, wie z.B. Braze. Es ist unternehmenstauglich und bietet ein robustes Transformations-Framework, mit dem Sie Ihre Ereignisdaten im Handumdrehen verarbeiten können.

Die Integration von Braze und RudderStack bietet eine native SDK-Integration für Ihre Android-, iOS- und Webanwendungen und eine Server-zu-Server-Integration von Ihren Backend-Diensten.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| RuderStack-Konto | Ein [RudderStack-Konto](https://app.rudderstack.com/) ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Konfigurierte Quelle | Eine [Quelle][3] ist im Wesentlichen der Ursprung aller Daten, die an RudderStack gesendet werden, wie z.B. Websites, mobile Apps oder Backend-Server. Sie müssen die Quelle konfigurieren, bevor Sie Braze als Ziel in RudderStack einrichten. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `users.identify`, `users.delete` und `users.alias.new`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze App Schlüssel | Um Ihren App-Schlüssel im Braze-Dashboard zu erhalten, gehen Sie zu **Einstellungen** > **App-Einstellungen** > **Identifizierung** und suchen Sie den Namen Ihrer App. Speichern Sie die zugehörige Identifizierungszeichenfolge.
| Rechenzentrum | Ihr Rechenzentrum ist auf Ihr Braze Dashboard abgestimmt [Instanz][15].  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Eine Quelle hinzufügen

Um mit dem Senden von Daten an Braze zu beginnen, müssen Sie zunächst sicherstellen, dass eine Quelle in Ihrer RudderStack-App eingerichtet ist. Besuchen Sie [RudderStack][22] um zu erfahren, wie Sie Ihre Datenquelle einrichten.

### Schritt 2: Ziel konfigurieren

Nachdem Sie nun Ihre Datenquelle eingerichtet haben, wählen Sie im RudderStack-Dashboard unter **Ziele** die Option **ZIEL HINZUFÜGEN**. Wählen Sie aus der Liste der verfügbaren Ziele **Braze** aus und klicken Sie auf **Weiter**.

Geben Sie im Braze-Ziel den App-Schlüssel, den Braze REST API-Schlüssel, den Daten-Cluster und die native SDK-Option (nur Gerätemodus) an. Die Option Natives SDK verwendet das native SDK von Braze zum Senden von Ereignissen, wenn diese Option aktiviert ist. 

![][0]{: style="max-width:70%;margin-bottom:15px;border:none;"}

### Schritt 3: Wählen Sie die Art der Integration

Sie können die web- und nativen client-seitigen Bibliotheken von RudderStack mit Braze auf eine der folgenden Arten integrieren:

- [Side-by-Side / Geräte-Modus](#device-mode)**:** RudderStack sendet die Ereignisdaten direkt von Ihrem Client (Browser oder mobile Anwendung) an Braze.
- [Server-zu-Server / Cloud-Modus](#cloud-mode)**:** Das Braze SDK sendet die Ereignisdaten direkt an RudderStack, die dann umgewandelt und an Braze weitergeleitet werden.
- [Hybrid-Modus](#hybrid-mode)**:** Verwenden Sie den Hybrid-Modus, um über eine einzige Verbindung automatisch generierte und benutzergenerierte Ereignisse für iOS und Android an Braze zu senden.

{% alert note %}
Erfahren Sie mehr über die [Verbindungsmodi](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) von RudderStack und die Vorteile der einzelnen Modi.
{% endalert %}

#### Side-by-Side-Integration (Geräte-Modus) {#device-mode}

In diesem Modus können Sie Ihre Ereignisse über das Braze SDK, das auf Ihrer Website oder Ihrer mobilen App eingerichtet ist, an Braze senden.

Richten Sie die Mappings zum RudderStack SDK für Ihre Plattform im GitHub-Repository von Braze ein, wie unter [Unterstützte Methoden](#supported-methods) beschrieben:

- [Android][android]
- [iOS][ios]
- [Swift][swift]
- [Web][web]
- [React Native][react]
- [Flattert][Flattert]

Um die Integration des Gerätemodus abzuschließen, lesen Sie bitte die ausführliche RudderStack-Anleitung zum [Hinzufügen von Braze zu Ihrem Projekt](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Server-zu-Server-Integration (Cloud-Modus) {#cloud-mode}

In diesem Modus sendet das SDK die Ereignisdaten direkt an den RudderStack-Server. RudderStack wandelt diese Daten dann um und leitet sie an das gewünschte Ziel weiter. Diese Umwandlung erfolgt im RudderStack-Backend unter Verwendung des RudderStack-Transformer-Moduls.

Um die Integration zu ermöglichen, müssen Sie die Methoden von RudderStack auf Braze abbilden, wie unter [Unterstützte Methoden](#supported-methods) beschrieben.

{% alert note %}
Die serverseitigen SDKs von RudderStack (Java, Python, Node.js, Go, Ruby) unterstützen nur den Cloud-Modus. Das liegt daran, dass ihre serverseitigen SDKs im RudderStack-Backend arbeiten und kein Braze-spezifisches SDK laden können.
{% endalert %}

{% alert important %}
Die Server-zu-Server-Integration unterstützt keine Braze UI-Funktionen, wie z. B. Push-Benachrichtigungen oder In-App-Nachrichten. Diese Funktionen werden jedoch durch die Integration des Gerätemodus unterstützt.
{% endalert %}

#### Hybrid-Modus {#hybrid-mode}

Verwenden Sie den Hybrid-Modus, um alle Ereignisse von Ihren iOS- und Android-Quellen an Braze zu senden. 

Wenn Sie den Hybrid-Modus wählen, um Ereignisse an Braze zu senden, wird RudderStack:
1. Initialisiert das Braze SDK.
2. Sendet alle vom Benutzer erzeugten Ereignisse (Identifizieren, Verfolgen, Seite, Bildschirm und Gruppe) nur über den Cloud-Modus an Braze und verhindert, dass sie über den Gerätemodus gesendet werden.
3. Sendet die automatisch generierten Ereignisse (In-App-Nachrichten, Push-Benachrichtigungen, die das Braze SDK erfordern) über den Gerätemodus.

Um [Ereignisse über den Hybridmodus zu senden](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), verwenden Sie die Option Hybridmodus, während Sie Ihre Quelle mit dem Braze-Ziel verbinden. Dann fügen Sie die Braze-Integration zu Ihrem Projekt hinzu.

## Schritt 4: Konfigurieren Sie zusätzliche Einstellungen

Nachdem Sie die Ersteinrichtung abgeschlossen haben, konfigurieren Sie die folgenden Einstellungen, um Ihre Daten korrekt in Braze zu empfangen:

- **Aktivieren Sie Abonnementgruppen im Gruppenanruf**: Aktivieren Sie diese Einstellung, um den Status der Abonnementgruppe in Ihren Gruppenereignissen zu senden. Weitere Informationen finden Sie unter [Gruppe](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Operation Benutzerdefinierte Attribute verwenden**: Aktivieren Sie diese Einstellung, wenn Sie die [verschachtelten benutzerdefinierten Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/) in Braze verwenden möchten, um Segmente zu erstellen und Ihre Nachrichten mithilfe eines benutzerdefinierten Attributobjekts zu personalisieren. Weitere Informationen finden Sie unter [Senden von Benutzermerkmalen als verschachtelte benutzerdefinierte Attribute](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Verfolgen Sie Ereignisse für anonyme Benutzer**: Aktivieren Sie diese Einstellung, um anonyme Benutzeraktivitäten zu verfolgen und diese Informationen an Braze zu senden.

### Einstellungen des Gerätemodus

Die folgenden Einstellungen gelten nur, wenn Sie Ereignisse über den [Gerätemodus](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode) an Braze senden:

- **Client-seitige Ereignisfilterung**: Mit dieser Einstellung können Sie festlegen, welche Ereignisse für Braze gesperrt oder zugelassen werden sollen. Weitere Informationen zu dieser Einstellung finden Sie unter [Client-seitige Ereignisfilterung](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Eigenschaften deduplizieren**: Aktivieren Sie diese Einstellung, um die Benutzereigenschaften im Anruf zu deduplizieren. [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify) Aufruf.
- **Braze-Protokolle anzeigen**: Diese Einstellung ist nur anwendbar, wenn Sie das [JavaScript SDK](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) als Quelle verwenden. Aktivieren Sie diese Option, um die Braze-Protokolle für Ihre Benutzer anzuzeigen.
- **OneTrust Cookie-Kategorien**: Mit dieser Einstellung können Sie die [OneTrust-Cookie-Zustimmungsgruppen](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) mit Braze verknüpfen.

## Unterstützte Methoden

Braze unterstützt die RuderStack-Methoden identify, track, screen, page, group und alias.

{% tabs %}
{% tab Identifizieren Sie %}

Die [Methode](https://rudderstack.com/docs/destinations/marketing/braze/#identify) RudderStack [`identify` verknüpft Benutzer mit ihren Aktionen.](https://rudderstack.com/docs/destinations/marketing/braze/#identify)  RudderStack erfasst eine eindeutige Benutzer-ID und optionale Merkmale, die mit diesem Benutzer verbunden sind, wie Name, E-Mail, IP-Adresse usw.

**Delta-Management für Identifizierungsanrufe**<br>
Wenn Sie Ereignisse über den Gerätemodus an Braze senden, können Sie Kosten sparen, indem Sie Ihre `identify` Anrufe deduplizieren. Aktivieren Sie dazu die Dashboard-Einstellung Traits deduplizieren. RudderStack sendet dann nur die geänderten oder modifizierten Attribute (Traits) an Braze.

**Löschen eines Benutzers**<br>
Sie können einen Benutzer in Braze mit der [Verordnung Unterdrückung mit Löschen](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) der RuderStack [Data Regulation API](https://www.rudderstack.com/docs/api/data-regulation-api/) löschen.

{% endtab %}
{% tab Spur %}

Die [Methode`track` ](https://rudderstack.com/docs/destinations/marketing/braze/#track) von RudderStack erfasst alle Benutzeraktivitäten und die mit diesen Aktivitäten verbundenen Eigenschaften.

**Bestellung abgeschlossen**<br>
Wenn Sie die [RudderStack Ecommerce API][20] verwenden, um die Track-Methode für ein Ereignis mit dem Namen `Order Completed` aufzurufen, sendet RudderStack die in diesem Ereignis aufgeführten Produkte an Braze als [`purchases`][21].

{% endtab %}
{% tab Bildschirm %}

Mit der [Methode`screen` ](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) von RudderStack können Sie die mobilen Bildschirmansichten Ihrer Benutzer mit allen zusätzlichen Informationen über den betrachteten Bildschirm aufzeichnen.

{% endtab %}
{% tab Seite %}

Mit der [Methode`page` ](https://rudderstack.com/docs/destinations/marketing/braze/#page) von RudderStack können Sie die Seitenaufrufe Ihrer Website aufzeichnen. Außerdem werden alle anderen relevanten Informationen über diese Seite erfasst.

{% endtab %}
{% tab Gruppe %}

Die [Methode`group` ](https://rudderstack.com/docs/destinations/marketing/braze/#group) von RudderStack ermöglicht es Ihnen, einen Benutzer mit einer Gruppe zu verknüpfen.

**Status der Abonnementgruppe**<br>
Um den Status der Abonnementgruppen zu aktualisieren, aktivieren Sie die Einstellung "Abonnementgruppen im Gruppenaufruf aktivieren" im RudderStack-Dashboard und senden den Status der Abonnementgruppen im Gruppenaufruf.

{% endtab %}
{% tab Alias %}

Mit der [Methode`alias` ](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) von RudderStack können Sie verschiedene Identitäten eines bekannten Benutzers zusammenführen. Beachten Sie, dass RudderStack den Alias-Aufruf für Braze nur im Cloud-Modus unterstützt.

{% endtab %}
{% endtabs %}

## Senden von Benutzermerkmalen als verschachtelte benutzerdefinierte Attribute

Sie können die Benutzereigenschaften als verschachtelte benutzerdefinierte Attribute an Braze senden und mit ihnen Operationen zum Hinzufügen, Aktualisieren und Entfernen durchführen. Aktivieren Sie dazu in RudderStack bei der Konfiguration des Braze-Ziels die Einstellung "Benutzerdefinierte Attribute für das Dashboard verwenden". Diese Funktion ist nur im Cloud-Modus verfügbar.

Sie können die Benutzermerkmale als verschachtelte benutzerdefinierte Attribute in Ihren `identify` Ereignissen im folgenden Format senden:
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

Um die Benutzereigenschaften als benutzerdefinierte Benutzerattribute über die Aufrufe `track`, `page` oder `screen` zu senden, übergeben Sie `traits` als kontextabhängiges Feld im Ereignis:
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
Für die Vorgänge Aktualisieren und Entfernen ist `identifier` ein erforderlicher Schlüssel. Wenn die Operationen Hinzufügen, Aktualisieren oder Entfernen in dem verschachtelten Array nicht vorhanden sind, verwendet RudderStack standardmäßig die Operation Erstellen, um die Eigenschaften zu erstellen. Weitere Informationen zum Senden von verschachtelten benutzerdefinierten Attributen finden Sie unter [Array von Objekten]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/).
{% endalert %}

[0]: {% image_buster /assets/img/RudderStack/braze_settings.png %}
[1]: https://rudderstack.com/
[3]: https://www.rudderstack.com/docs/dashboard-guides/sources/
[15]: {{site.baseurl}}/api/basics/#endpoints
[20]: https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/
[21]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[22]: https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started
[android]: https://github.com/rudderlabs/rudder-integration-braze-android
[ios]: https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master
[swift]: https://github.com/rudderlabs/rudder-integration-braze-swift
[web]: https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze
[react]: https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native
[flattern]: https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter