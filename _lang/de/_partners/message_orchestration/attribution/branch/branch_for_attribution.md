---
nav_title: Branch für Attribution
article_title: Branch für Attribution
alias: /partners/branch_for_attribution/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Branch, einer mobilen Linking-Plattform, die Sie bei der Akquise, dem Engagement und der Messung über alle Geräte, Kanäle und Plattformen hinweg unterstützt."
page_type: partner
search_tag: Partner

---

# Branch für Attribution {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/), eine mobile Verknüpfungsplattform, unterstützt Sie bei der Akquise, dem Engagement und der Messung über alle Geräte, Kanäle und Plattformen hinweg, indem sie einen ganzheitlichen Überblick über alle Nutzer:innen-Touchpoints bietet.

_Diese Integration wird von Branch gepflegt._

## Über die Integration

Die Integration von Braze und Branch hilft Ihnen dabei, genau zu verstehen, wann und wo Nutzer:innen akquiriert wurden und wie Sie ihre Journeys durch robuste Attribution und [Deeplinks]({{site.baseurl}}/partners/message_orchestration/attribution/branch/branch_for_deeplinking/) personalisieren können.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Branch-Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein Branch-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Branch SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Abbildung von Geräte IDs

#### Android 

Wenn Sie eine Android App haben, müssen Sie eine eindeutige Braze ID für Ihr Gerät an Branch übergeben. Diese ID kann in der Methode `setRequestMetadataKey()` des Branch SDK festgelegt werden. Der folgende Code-Snippet muss vor dem Aufruf von `initSession` eingefügt werden. Sie müssen auch das Braze SDK initialisieren, bevor Sie die Metadaten der Anfrage im Branch SDK festlegen.

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId); 
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
Vor Februar 2023 verwendete unsere Branch Attribution Integration den IDFV als primären Bezeichner, um iOS Attribution Daten abzugleichen. Für Braze-Kund:innen, die Objective-C verwenden, ist es nicht erforderlich, die Braze `device_id` abzurufen und bei der Installation an Branch zu senden, da es zu keiner Unterbrechung des Dienstes kommen wird.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitigen Bezeichner verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. 

Bei der Einstellung `true` müssen Sie die Abbildung der iOS-Geräte-ID für Swift implementieren, um die Braze `device_id` bei der Installation der App an Branch weiterzugeben, damit Braze die iOS Attribute richtig zuordnen kann.

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init 
}
```

{% endtab %}
{% endtabs %}

### Schritt 2: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Branch** aus. 

Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Branch einrichten.<br><br>![Dieses Bild zeigt das Feld "Datenimport für Install-Attribution" auf der Seite Branch-Technologie. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.][4]{: style="max-width:90%;"}

### Schritt 3: Daten-Feeds einrichten

1. Wählen Sie in Branch unter dem Abschnitt **Exporte** die Option **Daten-Feeds**.
2. Wählen Sie auf der Seite **Manager:in Daten-Feeds** den Tab **Datenintegration** am oberen Rand der Seite. 
3. Wählen Sie Braze aus der Liste der verfügbaren Daten-Partner aus. 
4. Geben Sie auf der Braze-Exportseite den Datenimport-Schlüssel und den REST-Endpunkt an, den Sie im Braze-Dashboard gefunden haben, und wählen Sie **Enablement**.

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attribution-Daten von Branch erhält, ändert sich der Verbindungsstatus auf der Technologie-Partnerseite von Branch von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine attributierte Installation erhalten. Organische Installationen, die vom Branch-Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht mitgezählt.

## Daten zur Attribution von Facebook und X (früher Twitter)

Attribution Daten für Facebook und X (ehemals Twitter) Kampagnen sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Branch Click Tracking URLs in Braze (optional)

Wenn Sie Tracking-Links für Klicks in Ihren Braze-Kampagnen verwenden, können Sie leicht erkennen, welche Kampagnen zu App-Installationen und erneuter Interaktion führen. So können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen für einen maximalen ROI investieren sollten.

Um mit Branch Click Tracking Links zu beginnen, besuchen Sie die [Dokumentation](https://help.branch.io/using-branch/docs/ad-links). Sie können die Links zum Branch Klick Tracking direkt in Ihre Braze Kampagnen einfügen. Branch verwendet dann seine [probabilistischen Attribution-Methoden](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings), um den Nutzer:innen, die auf den Link geklickt haben, zu attributieren. Wir empfehlen, Ihre Branch Tracking-Links mit einem Bezeichner für das Gerät zu versehen, um die Genauigkeit der Attributionen Ihrer Kampagnen von Braze zu verbessern. Dadurch wird der Nutzer:in, der auf den Link geklickt hat, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze den Kund:in, sich für die [Sammlung der Google Advertising ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Branch SDK-Integration erfasst. Sie können die GAID in Ihre Branch-Klick-Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Branch den IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Bezeichner für das Gerät verwendet werden. Sie können den Identifier for Vendors (IDFV) in Ihre Branch-Klick-Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Diese Empfehlung ist rein optional**<br>
Wenn Sie derzeit keine Bezeichner für Geräte - wie IDFV oder GAID - in Ihren Click-through-Links verwenden oder dies in Zukunft nicht vorhaben, kann Branch diese Klicks dennoch durch seine probabilistische Modellierung attributieren.
{% endalert %}


[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Branch Webhooks"
[4]: {% image_buster /assets/img/attribution/branch.png %}
