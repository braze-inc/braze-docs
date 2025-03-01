---
nav_title: AppsFlyer Zielgruppen
article_title: AppsFlyer Zielgruppen
alias: /partners/appsflyer_audiences/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und AppsFlyer Audiences, einer Funktion der AppsFlyer-Plattform, mit der Sie effizient Zielgruppensegmente erstellen und mit Partnernetzwerken verbinden können."
page_type: partner
search_tag: Partner

---

# AppsFlyer Zielgruppen

> Dieser Artikel beschreibt, wie Sie mit Hilfe der [AppsFlyer Audiences-Integration][2] Benutzerkohorten aus AppsFlyer in Braze importieren. Weitere Informationen zur Integration von AppsFlyer und seinen anderen Funktionen, wie z.B. der mobilen Attribution, finden Sie im [Hauptartikel zu AppsFlyer][3].

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| AppsFlyer-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein AppsFlyer-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform sind in Ihrer Anwendung möglicherweise Codeschnipsel erforderlich. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| AppsFlyer SDK | Zusätzlich zum erforderlichen Braze SDK müssen Sie das [AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Datenimporten

### Schritt 1: Konfigurieren Sie das AppsFlyer SDK

Um diese Integration zu nutzen, müssen Sie die externe Braze-ID des Benutzers über die Funktion `setPartnerData()` des AppsFlyer SDK an AppsFlyer übergeben:

#### Android 
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### Schritt 2: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **AppsFlyer**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im AppsFlyer Dashboard einrichten.<br><br>![Das Feld "Datenimport mit Cohort Import" auf der AppsFlyer Technologieseite. In diesem Feld werden Ihnen der Datenimportschlüssel und der REST-Endpunkt angezeigt.][5]{: style="max-width:90%;"}

### Schritt 3: Konfigurieren Sie eine Braze-Verbindung in AppsFlyer Audiences

1. Gehen Sie in [AppsFlyer Audiences][4] auf die Registerkarte **Verbindungen** und klicken Sie auf **Partnerverbindung hinzufügen**.
2. Wählen Sie Braze als Partner und geben Sie der Verbindung einen Namen.
3. Geben Sie den Datenimportschlüssel und den Braze REST-Endpunkt an.
4. Speichern Sie die Verbindung, und sie steht für die Verknüpfung mit einem neuen oder bestehenden Publikum zur Verfügung.

![Die Konfigurationsseite der AppsFlyer Publikumsplattform für Partnerverbindungen. Im unteren Teil der Bilder sehen Sie, dass das Feld Externe ID anlöten markiert ist.][6]{: style="max-width:80%;"}

### Schritt 4: AppsFlyer Audiences-Kohorten in Braze verwenden

Sobald eine AppsFlyer-Zielgruppe in Braze hochgeladen wurde, können Sie sie bei der Definition von Segmenten in Braze als Filter verwenden, indem Sie den **AppsFlyer-Kohortenfilter** auswählen.

![Benutzerattribute-Filter "AppsFlyer-Kohorten" ausgewählt.][7]

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: {{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}
[6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}
[7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}