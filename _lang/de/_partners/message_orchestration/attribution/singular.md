---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Singular, einer einheitlichen Marketing-Analyseplattform, die es Ihnen ermöglicht, Daten zur bezahlten Installation zu importieren."
page_type: partner
search_tag: Partner

---

# Singular

> Singular ist eine einheitliche Plattform für Marketing-Analysen, die Attribution, Kostenaggregation, Marketing-Analysen, kreative Berichte und Workflow-Automatisierung bietet.

Die Integration von Braze und Singular ermöglicht Ihnen den Import von Attributionsdaten für bezahlte Installationen, um Ihre Lifecycle-Kampagnen intelligent zu segmentieren.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Singuläres Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Singular-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform sind in Ihrer Anwendung möglicherweise Codeschnipsel erforderlich. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Singular SDK | Zusätzlich zum erforderlichen Braze SDK müssen Sie auch das [Singular SDK](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Benutzer-IDs zuordnen

#### Android

Wenn Sie eine Android-App haben, müssen Sie den folgenden Codeschnipsel einfügen, der eine eindeutige Braze-Benutzer-ID an Singular übergibt.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
Vor Februar 2023 verwendete unsere Singular-Attributionsintegration die IDFV als primäre Kennung, um iOS-Attributionsdaten abzugleichen. Für Braze-Kunden, die Objective-C verwenden, ist es nicht erforderlich, die Braze `device_id` abzurufen und bei der Installation an Singular zu senden, da es zu keiner Unterbrechung des Dienstes kommt.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitige Kennung verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. 

Wenn Sie diese Option auf `true` setzen, müssen Sie die iOS-Geräte-ID-Zuordnung für Swift implementieren, um die Braze `device_id` bei der App-Installation an Singular zu übergeben, damit Braze die iOS-Attribute richtig zuordnen kann.

{% tabs local %}
{% tab Objective-C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### Schritt 2: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Singular**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. 

Sie müssen Ihrem Singular-Kundenbetreuer den Datenimportschlüssel und den REST-Endpunkt mitteilen, damit die Integration abgeschlossen werden kann.<br><br>![Dieses Bild zeigt das Feld "Datenimport für Installationsattribution" auf der Seite Singular-Technologie. In diesem Feld werden Ihnen der Datenimportschlüssel und der REST-Endpunkt angezeigt.][4]{: style="max-width:90%;"}

### Schritt 3: Bestätigen Sie die Integration

Sobald Braze die Attributionsdaten von Singular erhält, ändert sich der Verbindungsstatus auf der Seite der Singular-Technologiepartner in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine zugeordnete Installation erhalten. Organische Installationen, die von der Singular-Postback-Funktion ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht berücksichtigt.

## Facebook und X (früher Twitter) Attributionsdaten

Attributionsdaten für Kampagnen auf Facebook und X (ehemals Twitter) sind über unsere Partner nicht verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Einzelne Click-Tracking-URLs in Braze (optional)

Durch die Verwendung von Klick-Tracking-Links in Ihren Braze-Kampagnen können Sie leicht erkennen, welche Kampagnen zu App-Installationen und Wiedereinstieg führen. So können Sie Ihre Marketingbemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen investieren sollten, um einen maximalen ROI zu erzielen.

Um mit Singular Click Tracking Links zu beginnen, besuchen Sie die [Dokumentation](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). Sie können die Singular Klick-Tracking-Links direkt in Ihre Braze-Kampagnen einfügen. Singular verwendet dann seine [probabilistischen Zuordnungsmethoden](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true), um den Nutzer, der auf den Link geklickt hat, zuzuordnen. Wir empfehlen Ihnen, Ihre Singular-Tracking-Links mit einer Gerätekennung zu versehen, um die Genauigkeit der Zuordnungen Ihrer Braze-Kampagnen zu verbessern. Dadurch wird der Benutzer, der auf den Link geklickt hat, deterministisch zugeordnet.

{% tabs local %}
{% tab Android %}
Für Android ermöglicht Braze seinen Kunden, sich für die [Erfassung der Google Werbe-ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Singular SDK-Integration erfasst. Sie können die GAID in Ihre Singular-Klickverfolgungslinks aufnehmen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Singular die IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Gerätekennung verwendet werden. Sie können die IDFV in Ihre Singular-Klickverfolgungslinks integrieren, indem Sie die folgende Liquid-Logik verwenden:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Diese Empfehlung ist rein optional**<br>
Wenn Sie derzeit keine Geräteidentifikatoren - wie IDFV oder GAID - in Ihren Click-Tracking-Links verwenden oder dies in Zukunft nicht vorhaben, kann Singular diese Klicks dennoch durch seine probabilistische Modellierung zuordnen.
{% endalert %}

[4]: {% image_buster /assets/img/attribution/singular.png %}
