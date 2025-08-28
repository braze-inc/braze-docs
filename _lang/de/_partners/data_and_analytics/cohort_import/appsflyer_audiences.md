---
nav_title: AppsFlyer Zielgruppen
article_title: AppsFlyer Zielgruppen
alias: /partners/appsflyer_audiences/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und AppsFlyer Audiences, ein Feature der AppsFlyer Plattform, das es Ihnen erlaubt, Zielgruppen Segmente effizient zu erstellen und mit Partnernetzwerken zu verbinden."
page_type: partner
search_tag: Partner

---

# AppsFlyer Zielgruppen

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten aus AppsFlyer in Braze importieren können, indem Sie die [AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/) Integration verwenden. Weitere Informationen zur Integration von AppsFlyer und seinen anderen Funktionalitäten, wie z.B. der mobilen Attribution, finden Sie im [Hauptartikel zu AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/).

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| AppsFlyer Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein AppsFlyer-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| AppsFlyer SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Datenimporten

### Schritt 1: Konfigurieren Sie das AppsFlyer SDK

Um diese Integration zu nutzen, müssen Sie die externe ID von Braze des Nutzers:innen über die Funktion `setPartnerData()` des AppsFlyer SDK an AppsFlyer übergeben:

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

### Schritt 2: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **AppsFlyer** aus. 

Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im AppsFlyer Dashboard einrichten.<br><br>![Das Feld "Datenimport über Kohortenimport" auf der AppsFlyer Technologieseite. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### Schritt 3: Konfigurieren Sie eine Braze-Verbindung in AppsFlyer Zielgruppen

1. Gehen Sie in [AppsFlyer Zielgruppen](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections) auf den Tab **Verbindungen** und klicken Sie auf **Partnerverbindung hinzufügen**.
2. Wählen Sie Braze als Partner aus und geben Sie der Verbindung einen Namen.
3. Geben Sie den Datenimport-Schlüssel und den Braze REST-Endpunkt an.
4. Wenn Sie die Verbindung speichern, können Sie sie mit jeder neuen oder bestehenden Zielgruppe verknüpfen.

![Die Konfigurationsseite der AppsFlyer Zielgruppen Plattform für Partnerverbindungen. Im unteren Teil der Bilder sehen Sie, dass das Feld Braze externe ID markiert ist.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### Schritt 4: AppsFlyer Zielgruppen Kohorten in Braze verwenden

Sobald eine AppsFlyer Zielgruppe in Braze hochgeladen wurde, können Sie sie als Filter bei der Definition von Segmenten in Braze verwenden, indem Sie den **AppsFlyer Kohorten-Filter** auswählen.

![Nutzer:innen Filter "AppsFlyer Kohorten" ausgewählt.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Kohortenimport wird keine neuen Nutzer:innen in Braze erstellen.
{% endalert %}

## Nutzer:innen-Abgleich

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` gefunden werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

