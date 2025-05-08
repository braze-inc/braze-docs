---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Kochava, einer mobilen Attributions-Plattform, die Ihnen Insights zu Attribution und Analytics bietet, damit Sie Ihre Daten für Ihr Wachstum nutzen können."
page_type: partner
search_tag: Partner

---

# Kochava

> Kochava bietet mobile Attribution und Analytics, damit Sie Ihre Daten für Ihr Wachstum nutzen können. Die Kochava Audience Platform ermöglicht Ihnen die Planung, das Targeting, die Aktivierung, die Messung und die Optimierung Ihrer Kampagnen für Apps.

_Diese Integration wird von Kochava gepflegt._

## Über die Integration

Die Integration von Braze und Kochava trägt zu einem ganzheitlicheren Verständnis Ihrer Kampagnen bei, indem sie Attributionsdaten an Braze sendet, um besser zu verstehen, welche Kampagnen zu Installationen, In-App-Aktivitäten und mehr führen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Kochava Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein Kochava-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Kochava SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [Kochava SDK](https://support.kochava.com/sdk-integration/) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Abbildung der Nutzer:innen IDs

#### Android

Das [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) SDK generiert eine GUID als Braze ID beim Start der Sitzung. Wir empfehlen, diesen Bezeichner in die Kochava-Methode `IdentityLink` einzugeben, da Braze damit die Daten mit dem richtigen Nutzerprofil abgleichen kann. Die Braze ID kann mit der folgenden Methode abgerufen werden:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Vor Februar 2023 verwendete unsere Kochava Attribution Integration den IDFV als primären Bezeichner, um iOS Attribution Daten abzugleichen. Für Braze-Kund:innen, die Objective-C verwenden, ist es nicht notwendig, die Braze `device_id` zu holen und bei der Installation an Kochava zu senden, da es keine Unterbrechung des Dienstes gibt.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitigen Bezeichner verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. Wenn Sie diese Option auf `true` setzen, müssen Sie die Abbildung der iOS Geräte ID für Swift implementieren, um die Braze `device_id` bei der Installation der App an Kochava zu übergeben, damit Braze die iOS Attribute richtig zuordnen kann.

Braze verfügt über zwei APIs, die denselben Wert erzeugen, eine mit einem Completion Handler und eine andere, die die neue Swift-Gleichzeitigkeitsunterstützung nutzt. Beachten Sie, dass Sie die folgenden Code-Snippets ändern müssen, damit sie den Anweisungen des [iOS SDK](https://support.kochava.com/sdk-integration/ios-sdk-integration/) von Kochava entsprechen. Wenn Sie weitere Hilfe benötigen, wenden Sie sich an den Kochava-Support.

##### Completion Handler
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Swift-Gleichzeitigkeit
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Schritt 2: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Kochava** aus. 

Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Kochava einrichten.<br><br>![Dieses Bild zeigt das Feld "Datenimport für Install-Attribution", das Sie auf der Kochava Technologieseite finden. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.][4]{: style="max-width:90%;"}

### Schritt 3: Einrichten eines Postbacks von Kochava

Fügen Sie ein [Postback][18] in Ihrem Kochava Dashboard hinzu. Sie werden zur Eingabe des Datenimport-Schlüssels und des REST-Endpunkts aufgefordert, die Sie im Braze-Dashboard gefunden haben.

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attribution-Daten von Kochava erhält, ändert sich der Verbindungsstatus auf der Kochava Technologie-Partnerseite in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine attributierte Installation erhalten. Organische Installationen, die vom Kochava-Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht mitgezählt.

## Daten zur Attribution von Facebook und X (früher Twitter)

Attribution Daten für Facebook und X (ehemals Twitter) Kampagnen sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Kochava Click Tracking URLs in Braze (optional)

Wenn Sie Tracking-Links für Klicks in Ihren Braze-Kampagnen verwenden, können Sie leicht erkennen, welche Kampagnen zu App-Installationen und erneuter Interaktion führen. So können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen für einen maximalen ROI investieren sollten.

Um mit Kochava Click Tracking Links zu beginnen, besuchen Sie die [Dokumentation](https://support.kochava.com/reference-information/attribution-overview/). Sie können die Kochava Click Tracking Links direkt in Ihre Kampagnen bei Braze einfügen. Kochava verwendet dann seine [probabilistischen Attributionsmethoden](https://www.kochava.com/getting-prepared-for-ios-14/), um den Nutzer:innen zuzuordnen, die auf den Link geklickt haben. Wir empfehlen, Ihre Kochava Tracking-Links mit einem Bezeichner für das Gerät zu versehen, um die Genauigkeit der Attributionen Ihrer Kampagnen von Braze zu verbessern. Dadurch wird der Nutzer:in, der auf den Link geklickt hat, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze den Kund:in, sich für die [Sammlung der Google Advertising ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Kochava SDK-Integration erfasst. Sie können die GAID in Ihre Kochava Click Tracking Links integrieren, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Kochava den IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Bezeichner für das Gerät verwendet werden. Sie können den Identifier for Vendors (IDFV) in Ihre Kochava Click Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie derzeit keine Geräte-Identifikatoren - wie IDFV oder GAID - in Ihren Click-through-Links verwenden oder dies in Zukunft nicht vorhaben, ist Kochava dennoch in der Lage, diese Klicks durch seine probabilistische Modellierung zu attributieren.
{% endalert %}


[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
[4]: {% image_buster /assets/img/attribution/kochava.png %}
