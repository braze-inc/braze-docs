---
nav_title: Zweig für Attribution
article_title: Zweig für Attribution
alias: /partners/branch_for_attribution/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Branch, einer mobilen Linking-Plattform, die Ihnen hilft, Kunden zu gewinnen, zu binden und über alle Geräte, Kanäle und Plattformen zu messen."
page_type: partner
search_tag: Partner

---

# Zweig für Attribution {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/), eine Plattform für die Verknüpfung von Mobilgeräten, hilft Ihnen bei der Akquise, dem Engagement und der Messung über alle Geräte, Kanäle und Plattformen hinweg, indem sie einen ganzheitlichen Überblick über alle Berührungspunkte mit dem Benutzer bietet.

Die Integration von Braze und Branch hilft Ihnen dabei, genau zu verstehen, wann und wo Nutzer akquiriert wurden und wie Sie ihre Journey durch robuste Attribution und [Deep Linking]({{site.baseurl}}/partners/channel_extensions/deep_linking/branch_for_deeplinking/) personalisieren können.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Filialkonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Branch-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform sind in Ihrer Anwendung möglicherweise Codeschnipsel erforderlich. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Filiale SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Geräte-IDs zuordnen

#### Android 

Wenn Sie eine Android-App haben, müssen Sie eine eindeutige Braze-Geräte-ID an Branch übergeben. Diese ID kann in der Methode `setRequestMetadataKey()` des Branch SDK festgelegt werden. Der folgende Codeschnipsel muss vor dem Aufruf von `initSession` eingefügt werden. Sie müssen auch das Braze SDK initialisieren, bevor Sie die Anfragemetadaten im Branch SDK festlegen.

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
Vor Februar 2023 nutzte unsere Branch-Attribution-Integration die IDFV als primäre Kennung, um iOS-Attributionsdaten abzugleichen. Für Braze-Kunden, die Objective-C verwenden, ist es nicht erforderlich, die Braze `device_id` abzurufen und bei der Installation an Branch zu senden, da es zu keiner Unterbrechung des Dienstes kommt.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitige Kennung verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. 

Wenn Sie diese Option auf `true` setzen, müssen Sie die iOS-Geräte-ID-Zuordnung für Swift implementieren, um die Braze `device_id` bei der App-Installation an Branch zu übergeben, damit Braze die iOS-Attribute richtig zuordnen kann.

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Schnell %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init 
}
```

{% endtab %}
{% endtabs %}

### Schritt 2: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Branch**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Branch einrichten.<br><br>![Diese Abbildung zeigt das Feld "Datenimport für Installationsattribution" auf der Seite Zweigstellen-Technologie. In diesem Feld werden Ihnen der Datenimportschlüssel und der REST-Endpunkt angezeigt.][4]{: style="max-width:90%;"}

### Schritt 3: Einrichten von Datenfeeds

1. Klicken Sie in der Zweigstelle unter dem Abschnitt **Exporte** auf **Daten-Feeds**.
2. Klicken Sie auf der Seite **Data Feeds Manager** auf die Registerkarte **Datenintegrationen** oben auf der Seite. 
3. Wählen Sie Braze aus der Liste der verfügbaren Datenpartner aus. 
4. Geben Sie auf der Braze-Export-Seite den Datenimportschlüssel und den REST-Endpunkt ein, den Sie im Braze-Dashboard gefunden haben, und klicken Sie auf **Aktivieren**.

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attributionsdaten von Branch erhält, ändert sich der Verbindungsstatus auf der Branch-Technologiepartnerseite in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine zugeordnete Installation erhalten. Organische Installationen, die vom Branch-Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht berücksichtigt.

## Facebook und X (früher Twitter) Attributionsdaten

Attributionsdaten für Kampagnen auf Facebook und X (ehemals Twitter) sind über unsere Partner nicht verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Verzweigungsklick-URLs in Braze (optional)

Durch die Verwendung von Klick-Tracking-Links in Ihren Braze-Kampagnen können Sie leicht erkennen, welche Kampagnen zu App-Installationen und Wiedereinstieg führen. So können Sie Ihre Marketingbemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen investieren sollten, um einen maximalen ROI zu erzielen.

Um mit Branch Click-Tracking-Links zu beginnen, besuchen Sie die entsprechende [Dokumentation](https://help.branch.io/using-branch/docs/ad-links). Sie können die Branch-Click-Tracking-Links direkt in Ihre Braze-Kampagnen einfügen. Branch verwendet dann ihre [probabilistischen Zuordnungsmethoden](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings), um den Benutzer, der auf den Link geklickt hat, zuzuordnen. Wir empfehlen Ihnen, Ihre Branch-Tracking-Links mit einer Gerätekennung zu versehen, um die Genauigkeit der Zuordnungen Ihrer Braze-Kampagnen zu verbessern. Dadurch wird der Benutzer, der auf den Link geklickt hat, deterministisch zugeordnet.

{% tabs local %}
{% tab Android %}
Für Android ermöglicht Braze seinen Kunden, sich für die [Erfassung der Google Werbe-ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Branch SDK-Integration erfasst. Sie können die GAID in Ihre Zweigstellen-Klickverfolgungslinks aufnehmen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS sammeln sowohl Braze als auch Branch die IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Gerätekennung verwendet werden. Sie können die IDFV in Ihre Zweigstellen-Klickverfolgungslinks aufnehmen, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie derzeit keine Geräteidentifikatoren - wie IDFV oder GAID - in Ihren Click-Tracking-Links verwenden oder dies in Zukunft nicht vorhaben, kann Branch diese Klicks dennoch durch die probabilistische Modellierung zuordnen.
{% endalert %}

[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Zweigstelle Webhooks"
[4]: {% image_buster /assets/img/attribution/branch.png %}
