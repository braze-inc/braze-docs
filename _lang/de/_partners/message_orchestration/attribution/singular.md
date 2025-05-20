---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Singular, einer einheitlichen Analytics-Plattform für Marketing, die es Ihnen erlaubt, Daten zur bezahlten Install-Attribution zu importieren."
page_type: partner
search_tag: Partner

---

# Singular

> Singular ist eine einheitliche Analytics-Plattform für Marketing, die Attribution, Kostenaggregation, Marketing-Analysen, kreative Berichte und Workflow-Automatisierung zustellt.

_Diese Integration wird von Singular gepflegt._

## Über die Integration

Die Integration von Braze und Singular erlaubt es Ihnen, Daten zur bezahlten Install-Attribution zu importieren, um innerhalb Ihrer Lebenszyklus-Kampagnen intelligent zu segmentieren.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Singulares Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Singular Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Singular SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [Singular SDK](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Abbildung der Nutzer:innen IDs

#### Android

Wenn Sie eine Android App haben, müssen Sie den folgenden Code Snippet einfügen, der eine eindeutige Braze Nutzer:in ID an Singular weitergibt.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
Vor Februar 2023 verwendete unsere Singular Attribution Integration den IDFV als primären Bezeichner, um iOS Attribution Daten abzugleichen. Für Braze-Kund:innen, die Objective-C verwenden, ist es nicht notwendig, die Braze `device_id` zu holen und bei der Installation an Singular zu senden, da es zu keiner Unterbrechung des Dienstes kommt.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitigen Bezeichner verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. 

Wenn Sie diese Option auf `true` setzen, müssen Sie die Abbildung der iOS Geräte ID für Swift implementieren, um die Braze `device_id` bei der Installation der App an Singular zu übergeben, damit Braze die iOS Attribute richtig zuordnen kann.

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

### Schritt 2: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Singular** aus. 

Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. 

Sie müssen den Datenimport-Schlüssel und den REST-Endpunkt an Ihren Singular Account Manager:in weitergeben, um die Integration abzuschließen.<br><br>![Dieses Bild zeigt das Feld "Datenimport für Install-Attribution", das Sie auf der Seite Singular Technologie finden. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.][4]{: style="max-width:90%;"}

### Schritt 3: Bestätigen Sie die Integration

Sobald Braze Attribution-Daten von Singular erhält, ändert sich der Verbindungsstatus auf der Technologie-Partnerseite von Singular in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine attributierte Installation erhalten. Organische Installationen, die vom Singular Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht mitgezählt.

## Daten zur Attribution von Facebook und X (früher Twitter)

Attribution Daten für Facebook und X (ehemals Twitter) Kampagnen sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Singuläre Click Tracking URLs in Braze (optional)

Wenn Sie Tracking-Links für Klicks in Ihren Braze-Kampagnen verwenden, können Sie leicht erkennen, welche Kampagnen zu App-Installationen und erneuter Interaktion führen. So können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen für einen maximalen ROI investieren sollten.

Um mit Singular Click Tracking Links zu beginnen, besuchen Sie deren [Dokumentation](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). Sie können die Singular Click Tracking Links direkt in Ihre Kampagnen in Braze einfügen. Singular verwendet dann seine [probabilistischen Attributionsmethoden](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true), um den Nutzer:innen zuzuordnen, die auf den Link geklickt haben. Wir empfehlen, Ihre Singular Tracking-Links mit einem Bezeichner für das Gerät zu versehen, um die Genauigkeit der Attributionen Ihrer Kampagnen von Braze zu verbessern. Dadurch wird der Nutzer:in, der auf den Link geklickt hat, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze den Kund:in, sich für die [Sammlung der Google Advertising ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Singular SDK-Integration erfasst. Sie können die GAID in Ihre Singular Click Tracking Links einfügen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Singular den IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Bezeichner für das Gerät verwendet werden. Sie können den Identifier for Vendors (IDFV) in Ihre Singular Click Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie derzeit keine Geräte-Identifikatoren - wie IDFV oder GAID - in Ihren Click-through-Links verwenden oder dies in Zukunft nicht vorhaben, ist Singular dennoch in der Lage, diese Klicks durch seine probabilistische Modellierung zu attributieren.
{% endalert %}


[4]: {% image_buster /assets/img/attribution/singular.png %}
