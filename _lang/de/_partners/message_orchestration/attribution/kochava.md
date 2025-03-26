---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Kochava, einer mobilen Attributionsplattform, die Attributions- und Analyseergebnisse bietet, damit Sie Ihre Daten für Ihr Wachstum nutzen können."
page_type: partner
search_tag: Partner

---

# Kochava

> Kochava bietet mobile Attribution und Analysen, damit Sie Ihre Daten für Ihr Wachstum nutzen können. Mit der Kochava Audience Platform können Sie Ihre App-Kampagnen planen, ausrichten, aktivieren, messen und optimieren.

Die Integration von Braze und Kochava trägt zu einem ganzheitlichen Verständnis Ihrer Kampagnen bei, indem sie Attributionsdaten an Braze sendet, um besser zu verstehen, welche Kampagnen zu Installationen, In-App-Aktivitäten und mehr führen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Kochava Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Kochava-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform sind in Ihrer Anwendung möglicherweise Codeschnipsel erforderlich. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Kochava SDK | Zusätzlich zum erforderlichen Braze SDK müssen Sie das [Kochava SDK](https://support.kochava.com/sdk-integration/) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Benutzer-IDs zuordnen

#### Android

Das [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) SDK generiert beim Start der Sitzung eine GUID als Braze-ID. Wir empfehlen, diese Kennung in der Kochava `IdentityLink` Methode zu verwenden, da sie es Braze ermöglicht, die Daten mit dem richtigen Benutzerprofil abzugleichen. Die Braze ID kann mit der folgenden Methode abgerufen werden:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Vor Februar 2023 verwendete unsere Kochava-Attributionsintegration die IDFV als primäre Kennung, um iOS-Attributionsdaten abzugleichen. Für Braze-Kunden, die Objective-C verwenden, ist es nicht erforderlich, die Braze `device_id` abzurufen und bei der Installation an Kochava zu senden, da es zu keiner Unterbrechung des Dienstes kommt.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitige Kennung verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. Wenn Sie diese Option auf `true` setzen, müssen Sie die iOS-Geräte-ID-Zuordnung für Swift implementieren, um die Braze `device_id` bei der App-Installation an Kochava zu übergeben, damit Braze die iOS-Attribute richtig zuordnen kann.

Braze verfügt über zwei APIs, die denselben Wert erzeugen, eine mit einem Completion-Handler und eine andere, die die neue Swift-Unterstützung für Gleichzeitigkeit nutzt. Beachten Sie, dass Sie die folgenden Codeschnipsel ändern müssen, damit sie mit den Anweisungen des [iOS SDK](https://support.kochava.com/sdk-integration/ios-sdk-integration/) von Kochava übereinstimmen. Wenn Sie weitere Hilfe benötigen, wenden Sie sich an den Kochava-Support.

##### Handler für die Fertigstellung
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Schnelle Gleichzeitigkeit
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Schritt 2: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Kochava**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Kochava-Dashboard einrichten.<br><br>![Dieses Bild zeigt das Feld "Datenimport für Installationsattribution" auf der Kochava Technologieseite. In diesem Feld werden Ihnen der Datenimportschlüssel und der REST-Endpunkt angezeigt.][4]{: style="max-width:90%;"}

### Schritt 3: Einrichten eines Postbacks von Kochava

[Fügen Sie ein Postback][18] in Ihrem Kochava-Dashboard [hinzu][18]. Sie werden nach dem Datenimportschlüssel und dem REST-Endpunkt gefragt, die Sie im Dashboard von Braze gefunden haben.

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attributionsdaten von Kochava erhält, ändert sich der Verbindungsstatus auf der Kochava-Technologiepartnerseite in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine zugeordnete Installation erhalten. Organische Installationen, die vom Kochava-Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht mitgezählt.

## Facebook und X (früher Twitter) Attributionsdaten

Attributionsdaten für Kampagnen auf Facebook und X (ehemals Twitter) sind über unsere Partner nicht verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Kochava Klick-Tracking-URLs in Braze (optional)

Durch die Verwendung von Klick-Tracking-Links in Ihren Braze-Kampagnen können Sie leicht erkennen, welche Kampagnen zu App-Installationen und Wiedereinstieg führen. So können Sie Ihre Marketingbemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen investieren sollten, um einen maximalen ROI zu erzielen.

Um mit Kochava Click-Tracking-Links zu beginnen, besuchen Sie die [Dokumentation](https://support.kochava.com/reference-information/attribution-overview/). Sie können die Kochava Klick-Tracking-Links direkt in Ihre Braze-Kampagnen einfügen. Kochava verwendet dann seine [probabilistischen Zuordnungsmethoden](https://www.kochava.com/getting-prepared-for-ios-14/), um den Benutzer zuzuordnen, der auf den Link geklickt hat. Wir empfehlen Ihnen, Ihre Kochava-Tracking-Links mit einer Gerätekennung zu versehen, um die Genauigkeit der Zuordnungen Ihrer Braze-Kampagnen zu verbessern. Dadurch wird der Benutzer, der auf den Link geklickt hat, deterministisch zugeordnet.

{% tabs local %}
{% tab Android %}
Für Android ermöglicht Braze seinen Kunden, sich für die [Erfassung der Google Werbe-ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Kochava SDK-Integration erfasst. Sie können die GAID in Ihre Kochava-Klick-Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS sammeln sowohl Braze als auch Kochava die IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Gerätekennung verwendet werden. Sie können die IDFV in Ihre Kochava-Klick-Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie derzeit keine Gerätekennungen - wie die IDFV oder GAID - in Ihren Click-Tracking-Links verwenden oder dies in Zukunft nicht vorhaben, kann Kochava diese Klicks dennoch durch seine probabilistische Modellierung zuordnen.
{% endalert %}


[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
[4]: {% image_buster /assets/img/attribution/kochava.png %}
