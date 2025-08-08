---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und AppsFlyer, einer Analytics-Plattform für Mobile-Marketing und Attribution, die Ihnen hilft, Ihre Apps zu analysieren und zu optimieren."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyer ist eine Analyse- und Attributionsplattform für mobiles Marketing, die Sie durch Marketinganalysen, Mobile-Attribution und Deep Linking bei der Analyse und Optimierung Ihrer Apps unterstützt.

Die Integration von Braze und AppsFlyer lässt Sie besser verstehen, wie Sie Ihre Kampagnen optimieren und ganzheitlicher gestalten können, indem Sie die mobilen Install-Attribution-Daten von AppsFlyer nutzen. 

Mit der [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/) Integration können Sie Ihre AppsFlyer Zielgruppen (Kohorten) direkt an Braze weitergeben, was es Ihnen erlaubt, leistungsstarke Customer-Engagement Kampagnen zu erstellen, die genau auf die richtigen Nutzer:innen zur richtigen Zeit ausgerichtet sind. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| AppsFlyer Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein AppsFlyer-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| AppsFlyer SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started) installieren.
| Einrichtung der E-Mail Domain abgeschlossen | Sie müssen beim Onboarding von Braze den [Schritt zur Einrichtung von IP und Domain]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) abgeschlossen haben, um Ihre E-Mail einzurichten. |
| SSL-Zertifikat | Ihr [SSL-Zertifikat]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) muss konfiguriert sein. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: ID des Geräts abbilden

{% tabs local %}
{% tab Android %}
Wenn Sie eine Android App haben, müssen Sie eine eindeutige Braze ID für Ihr Gerät an AppsFlyer übergeben. 

Stellen Sie sicher, dass die folgenden Code-Zeilen an der richtigen Stelle eingefügt werden - nachdem das Braze SDK gestartet wurde und vor dem Initialisierungscode für das AppsFlyer SDK. Weitere Informationen finden Sie im AppsFlyer [SDK-Integrationshandbuch für Android](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk).

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
Vor Februar 2023 verwendete unsere AppsFlyer Attribution Integration den IDFV als primären Bezeichner, um iOS Attribution Daten abzugleichen. Für Braze Kund:innen, die Objective-C verwenden, ist es nicht notwendig, die Braze `device_id` zu holen und bei der Installation an AppsFlyer zu senden, da es zu keiner Unterbrechung des Dienstes kommen wird.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitigen Bezeichner verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. 

Wenn Sie diese Option auf `true` setzen, müssen Sie die Abbildung der iOS Geräte ID für Swift implementieren, um die Braze `device_id` bei der Installation der App an AppsFlyer weiterzugeben, damit Braze die iOS Attribute richtig zuordnen kann.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Unity %}
Um die ID des Geräts in Unity abzubilden, gehen Sie wie folgt vor:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### Schritt 2: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **AppsFlyer** aus. 

Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im AppsFlyer Dashboard einrichten.<br><br>![Das Feld "Datenimport für Install-Attribution" ist auf der AppsFlyer Technologie-Seite verfügbar. In diesem Feld sind der Datenimport-Schlüssel und der REST-Endpunkt enthalten.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Schritt 3: Braze im Dashboard von AppsFlyer konfigurieren

1. Navigieren Sie in AppsFlyer auf die Seite **Integrierte Partner** in der linken Leiste. Suchen Sie dann nach **Braze** und wählen Sie das Braze-Logo aus, um ein Konfigurationsfenster zu öffnen.
2. Schalten Sie auf dem Tab **Integration** die Option **Partner aktivieren** ein.
3. Geben Sie den Datenimport-Schlüssel und den REST-Endpunkt an, den Sie im Braze-Dashboard gefunden haben. 
4. Schalten Sie den **erweiterten Datenschutz** aus und speichern Sie Ihre Konfiguration.

Weitere Informationen zu diesen Anweisungen finden Sie in der [AppsFlyer Dokumentation](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attribution-Daten von AppsFlyer erhält, ändert sich der Verbindungsstatus auf der AppsFlyer Technologie-Partnerseite in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine attributierte Installation erhalten. Organische Installationen, die vom AppsFlyer-Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht mitgezählt.

### Schritt 5: Daten zur Nutzer:innen-Attribution anzeigen

#### Verfügbare Datenfelder

Vorausgesetzt, Sie konfigurieren Ihre Integration wie vorgeschlagen, wird Braze alle nicht-organischen Installationsdaten auf Segmentierungsfilter abbilden.

| AppsFlyer Datenfeld | Braze Segmente Filter |
| -------------------- | --------------------- |
| `media_source` | Attributierte Quelle |
| `campaign` | Attribution-Kampagne |
| `af_adset` | Attributierte Anzeigengruppe |
| `af_ad` | Attributierte Anzeige |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ihre Nutzer:innen können im Braze-Dashboard mit Hilfe der Install-Attribution-Filter nach Attributionsdaten segmentiert werden.

![Vier verfügbare Filter. Die erste lautet "Install-Attribution Quelle ist network_val_0". Die zweite lautet "Install-Attribution Quelle ist campaign_val_0". Die dritte lautet "Install-Attribution Quelle ist adgroup_val_0". Die vierte lautet "Install-Attribution Quelle ist creative_val_0". Neben den aufgelisteten Filtern können Sie sehen, wie diese Attributionsquellen dem Nutzerprofil hinzugefügt werden. Im Feld "Install-Attribution" auf der Informationsseite eines Nutzers:in wird die Installationsquelle als network_val_0, die Kampagne als campaign_val_0 usw. aufgeführt.]({% image_buster /assets/img/braze_attribution.png %})

Außerdem sind die Attributionsdaten für einen bestimmten Nutzer auf dem Profil jedes Nutzers im Braze-Dashboard verfügbar.

{% alert note %}
Attribution Daten für Facebook und X (ehemals Twitter) Kampagnen sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.
{% endalert %}

## Integrieren Sie AppsFlyer mit einem E-Mail-Anbieter für Deeplinks

AppsFlyer ist sowohl mit SendGrid als auch mit SparkPost als E-Mail Service-Anbieter (ESP) integriert, um Deeplinks und Click Tracking zu unterstützen. Folgen Sie den nachstehenden Anweisungen, um die Integration mit dem ESP Ihrer Wahl vorzunehmen.

{% alert tip %}
Deeplinks - Links, die Nutzer:innen zu einer bestimmten Seite oder Stelle innerhalb einer App oder Website führen - werden verwendet, um ein maßgeschneidertes Nutzer-Erlebnis zu schaffen. Obwohl es weit verbreitet ist, kann es bei der Verwendung von per E-Mail gesetzten Deeplinks mit Click Tracking, einem weiteren wichtigen Feature für die Erfassung von Nutzerdaten, zu Problemen kommen. Diese Probleme sind darauf zurückzuführen, dass ESPs Deeplinks in eine Domain zur Aufzeichnung von Klicks setzen, wodurch der ursprüngliche Link unterbrochen wird. Die Unterstützung von Deeplinks erfordert daher eine zusätzliche Einrichtung. Durch die Integration von AppsFlyer mit SendGrid oder SparkPost können Sie diese Probleme vermeiden. Erfahren Sie mehr über dieses Thema in [Universal Links und App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).
{% endalert %}

### Schritt 1: OneLink in AppsFlyer einrichten

1. Wählen Sie in AppsFlyer ein OneLink Template für Ihre E-Mail Kampagnen aus. Stellen Sie sicher, dass das Template universelle Links (iOS) oder App Links (Android) unterstützt. 
2. Konfigurieren Sie Ihre App so, dass sie Deeplinks mit OneLink unterstützt. In der [AppsFlyer Dokumentation](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup) finden Sie Einzelheiten zur Konfiguration Ihrer App für die Unterstützung von OneLink.

### Schritt 2: Konfigurieren Sie Ihre App für die Unterstützung von Universal Links und App Links

Universelle Links (iOS) oder App-Links (Android) sind durch das Betriebssystem des Geräts zulässig, um eine bestimmte App zu öffnen, wenn Sie darauf klicken.

Führen Sie die folgenden Schritte aus, um Universal Links und App Links zu unterstützen.

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
Richten Sie das Dateihosting der Apple App Site Association (AASA) ein, um universelle Links in Ihren E-Mails zu aktivieren.

1. Beschaffen Sie sich eine AASA-Datei auf eine der folgenden Arten:
    * Wenn Sie OneLink mit universellen Links eingerichtet haben, haben Sie möglicherweise bereits eine AASA-Datei, die mit OneLink verknüpft ist. Um die AASA-Datei zu erhalten, gehen Sie wie folgt vor:
        * Kopieren Sie die OneLink-Subdomain Ihrer OneLink-Vorlage. Stellen Sie sicher, dass das Template universelle Links unterstützt.
        * Fügen Sie ihn anstelle des Platzhalters in die folgende URL ein: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Um die AASA-Datei herunterzuladen, fügen Sie die OneLink-URL in die Adressleiste Ihres Browsers ein und drücken die **Eingabetaste**. Die Datei wird dann auf Ihren Computer heruntergeladen, und Sie können sie mit einem beliebigen Texteditor öffnen und ihren Inhalt anzeigen.
    * [In der Anleitung von Apple zu universellen Links](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) wird erklärt, wie Sie die AASA-Datei erstellen können.
2. Hosten Sie die AASA-Datei auf Ihrem Domain Server für die Aufzeichnung von Klicks. Die Datei sollte in dem Pfad: `click.example.com/.well-known/apple-app-site-association` abgelegt werden. 

In der [Dokumentation von SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links) erfahren Sie, wie Sie die AASA-Datei für SendGrid konfigurieren und die CDN Dienste einrichten, um die AASA-Datei zu hosten.

{% alert important %}
Sobald die AASA-Datei gehostet wird, muss für jede Änderung Ihrer OneLink-Konfiguration (Modifikation oder Austausch) eine neue AASA-Datei erstellt werden.
{% endalert %}
{% endsubtab %}
{% subtab Android %}
Richten Sie das Dateihosting für Digital Asset Links ein, um App-Links in Ihren E-Mails zu aktivieren.

1. Beziehen Sie eine Digital Asset Links-Datei auf eine der folgenden Arten:
    * Wenn Sie OneLink mit App Links eingerichtet haben, verfügen Sie möglicherweise bereits über eine mit OneLink verknüpfte Digital Asset Links-Datei. Um die Datei zu erhalten, gehen Sie wie folgt vor:
        * Kopieren Sie die OneLink-Subdomain Ihrer OneLink-Vorlage. Stellen Sie sicher, dass das Template App-Links unterstützt.
        * Fügen Sie `/.well-known/assetlinks.json` an das Ende der OneLink URL an.
        * Um die Datei Digital Asset Links herunterzuladen, fügen Sie die OneLink URL in die Adressleiste Ihres Browsers ein und drücken Sie die **Eingabetaste**. Zum Beispiel: `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. Die Datei wird dann auf Ihren Computer heruntergeladen, und Sie können sie mit einem beliebigen Texteditor öffnen und ihren Inhalt anzeigen.
    * [In der Android-Anleitung zu App Links](https://developer.android.com/studio/write/app-link-indexing) wird erklärt, wie Sie die Datei Digital Asset Links erstellen.
2. Hosten Sie die Datei mit den digitalen Asset-Links auf Ihrem Domain Server für die Aufzeichnung von Klicks. Die Datei sollte in dem Pfad: `click.example.com/.well-known/apple-app-site-association` abgelegt werden.

In der [Dokumentation von SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links) erfahren Sie, wie Sie die Datei Digital Asset Links für SendGrid konfigurieren und CDN Dienste einrichten, um die Datei Digital Asset Links zu hosten.

{% alert important %}
Sobald die Datei mit den digitalen Asset-Links gehostet wird, muss für jede Änderung Ihrer OneLink-Konfiguration (Modifikation oder Austausch) eine neue Datei erstellt werden.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Schritt 2a: AASA-Dateihosting einrichten
Richten Sie das Dateihosting der Apple App Site Association (AASA) ein, um universelle Links in Ihren E-Mails zu aktivieren.

1. Beschaffen Sie sich eine AASA-Datei auf eine der folgenden Arten:
    * Wenn Sie OneLink mit universellen Links eingerichtet haben, haben Sie möglicherweise bereits eine AASA-Datei, die mit OneLink verknüpft ist. Um die AASA-Datei zu erhalten, gehen Sie wie folgt vor:
        * Kopieren Sie die OneLink-Subdomain Ihrer OneLink-Vorlage. Stellen Sie sicher, dass das Template universelle Links unterstützt.
        * Fügen Sie ihn anstelle des Platzhalters in die folgende URL ein: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Um die AASA-Datei herunterzuladen, fügen Sie die OneLink-URL in die Adressleiste Ihres Browsers ein und drücken die **Eingabetaste**. Die Datei wird dann auf Ihren Computer heruntergeladen, und Sie können sie mit einem beliebigen Texteditor öffnen und ihren Inhalt anzeigen.
    * [In der Anleitung von Apple zu universellen Links](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) wird erklärt, wie Sie die AASA-Datei erstellen können.
2. Hosten Sie die AASA-Datei auf Ihrem Domain Server für die Aufzeichnung von Klicks. Die Datei sollte in dem Pfad: `click.example.com/.well-known/apple-app-site-association` abgelegt werden. 

In der [Dokumentation zu SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) erfahren Sie, wie Sie die AASA-Datei für SparkPost konfigurieren und angepasste Link-Unterpfade festlegen können.

{% alert important %}
Sobald die AASA-Datei gehostet wird, muss für jede Änderung Ihrer OneLink-Konfiguration (Modifikation oder Austausch) eine neue AASA-Datei erstellt werden.
{% endalert %}

#### Schritt 2b: Leiten Sie Ihre Click-Tracking Domain auf Ihren AASA Filehost um
Bei der [Konfiguration Ihrer E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) haben Sie einen CNAME-Eintrag in Ihrem DNS Server erstellt. Führen Sie die folgenden Schritte aus, nachdem Sie Ihre Click-Tracking Domain in Braze überprüft haben. 

1. Löschen Sie den CNAME-Eintrag, der Ihre Subdomain auf die SparkPost Domain umleitet.
2. Erstellen Sie einen CNAME-Eintrag, der Ihre Click Tracking Domain auf das CDN umleitet, das Ihre App AASA-Datei hostet, anstatt des Eintrags, den Sie oben gelöscht haben.
{% endsubtab %}
{% subtab Android %}
#### Schritt 2a: Einrichten von Digital Asset Links zum Hosten von Dateien
Richten Sie das Dateihosting für Digital Asset Links ein, um App-Links in Ihren E-Mails zu aktivieren.

1. Beziehen Sie eine Digital Asset Links-Datei auf eine der folgenden Arten:
    * Wenn Sie OneLink mit App Links eingerichtet haben, verfügen Sie möglicherweise bereits über eine mit OneLink verknüpfte Digital Asset Links-Datei. Um die Datei zu erhalten, gehen Sie wie folgt vor:
        * Kopieren Sie die OneLink-Subdomain Ihrer OneLink-Vorlage. Stellen Sie sicher, dass das Template App-Links unterstützt.
        * Fügen Sie `/.well-known/assetlinks.json` an das Ende der OneLink URL an.
        * Um die Datei Digital Asset Links herunterzuladen, fügen Sie die OneLink URL in die Adressleiste Ihres Browsers ein und drücken Sie die **Eingabetaste**. Zum Beispiel: `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. Die Datei wird dann auf Ihren Computer heruntergeladen, und Sie können sie mit einem beliebigen Texteditor öffnen und ihren Inhalt anzeigen.
    * [In der Android-Anleitung zu App Links](https://developer.android.com/studio/write/app-link-indexing) wird erklärt, wie Sie die Datei Digital Asset Links erstellen.
2. Hosten Sie die Datei mit den digitalen Asset-Links auf Ihrem Domain Server für die Aufzeichnung von Klicks. Die Datei sollte in dem Pfad: `click.example.com/.well-known/apple-app-site-association` abgelegt werden.

In der [Dokumentation zu SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) erfahren Sie, wie Sie die Datei Digital Asset Links für SparkPost konfigurieren und angepasste Link-Unterpfade festlegen.

{% alert important %}
Sobald die Datei mit den digitalen Asset-Links gehostet wird, muss für jede Änderung Ihrer OneLink-Konfiguration (Modifikation oder Austausch) eine neue Datei erstellt werden.
{% endalert %}

#### Schritt 2b: Leiten Sie Ihre Domain für das Klick-Tracking auf den Dateihoster für Ihre digitalen Assets um.
Bei der [Konfiguration Ihrer E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) haben Sie einen CNAME-Eintrag in Ihrem DNS Server erstellt. Führen Sie die folgenden Schritte aus, nachdem Sie Ihre Click-Tracking Domain in Braze überprüft haben. 

1. Löschen Sie den CNAME-Eintrag, der Ihre Subdomain auf die SparkPost Domain umleitet.
2. Erstellen Sie einen CNAME-Eintrag, der Ihre Click Tracking Domain auf das CDN umleitet, in dem Ihre App Digital Asset Links-Datei gehostet wird, und nicht auf den Eintrag, den Sie oben gelöscht haben.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Schritt 3: Konfigurieren Sie Ihr AppsFlyer SDK zur Unterstützung von Deeplinks

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
#### Schritt 3a: Konfigurieren Sie Ihr SDK so, dass es die AASA-Datei unterstützt
Nachdem Sie die AASA-Datei in Ihrer Domain für die Aufzeichnung von Klicks gehostet haben, konfigurieren Sie Ihr AppsFlyer SDK für die Unterstützung der AASA-Datei.

1. Wählen Sie in Xcode Ihr Projekt aus.
2. Wählen Sie **Fähigkeiten** aus.
3. Aktivieren Sie **Assoziierte Domains.**
4. Klicken Sie auf **+**, und geben Sie Ihre Klick Domain ein. Zum Beispiel: `applinks:click.example.com`.
Wenn ein Klick auf den universellen Link erfolgt, wird Ihre App geöffnet und das SDK gestartet. Um die App in die Lage zu versetzen, den OneLink hinter der Klick Domain zu extrahieren und den Deeplink aufzulösen, gehen Sie wie folgt vor:

#### Schritt 3b: Daten für Deeplinks setzen
1. Stellen Sie der SDK API die Domain für die Klick-Aufzeichnung zur Verfügung [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Diese API muss vor der Initialisierung des SDKs aufgerufen werden. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. Verwenden Sie die [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API, um die Deeplink-Parameter abzurufen und die Deeplink-Daten zu verarbeiten.

{% endsubtab %}
{% subtab Android %}
#### Schritt 3a: Konfigurieren Sie Ihr SDK für die Unterstützung der Datei Digital Asset Links

Nachdem Sie im vorherigen Schritt die Digital Asset Links-Datei in Ihrer Domain für die Klick-Aufzeichnung gehostet haben, konfigurieren Sie Ihr SDK so, dass es die Datei unterstützt.

Fügen Sie in Ihrem Android-Manifest den Klick-Domain-Host und ein beliebiges Präfix in den Tag der Aktivität ein, in die Sie Deeplinks setzen möchten.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### Schritt 3b: Daten für Deeplinks setzen
Wenn Sie auf einen App-Link klicken, wird Ihre App geöffnet und das SDK wird gestartet.  Um die App in die Lage zu versetzen, den OneLink hinter der Klick-Domain zu extrahieren und den Deeplink aufzulösen, listen Sie die Klick-Domains in der SDK-Methode auf [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Diese Eigenschaft muss vor der Initialisierung des SDK eingestellt werden. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Schritt 3a: Konfigurieren Sie Ihr SDK so, dass es die AASA-Datei unterstützt
Nachdem Sie die AASA-Datei in Ihrer Domain für die Aufzeichnung von Klicks gehostet haben, konfigurieren Sie Ihr SDK für die Unterstützung der AASA-Datei.

1. Wählen Sie in Xcode Ihr Projekt aus.
2. Wählen Sie **Fähigkeiten** aus.
3. Aktivieren Sie **Assoziierte Domains.**
4. Klicken Sie auf **+**, und geben Sie Ihre Klick Domain ein. Zum Beispiel: `applinks:click.example.com`.

#### Schritt 3b: Daten für Deeplinks setzen
Wenn ein Klick auf den universellen Link erfolgt, wird Ihre App geöffnet und das SDK gestartet. Um das SDK zu aktivieren, um den OneLink hinter der Klick Domain zu extrahieren, gehen Sie wie folgt vor:
1. Liste der Klick Domains in der SDK Eigenschaft  [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Stellen Sie sicher, dass Sie diese Eigenschaft vor der Initialisierung des SDK einstellen.
2. Vergewissern Sie sich, dass Liste <em>spgo.io</em> eine der aufgeführten Domains ist. SparkPost besitzt diese Domain und sie ist Teil des Umleitungsflusses. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. Verwenden Sie die [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API, um die Deeplink-Parameter abzurufen und die Deeplink-Daten zu verarbeiten.
{% endsubtab %}
{% subtab Android %}
#### Schritt 3a: Konfigurieren Sie Ihr SDK für die Unterstützung der Datei Digital Asset Links

Nachdem Sie im vorherigen Schritt die Digital Asset Links-Datei in Ihrer Domain für die Klick-Aufzeichnung gehostet haben, konfigurieren Sie Ihr SDK so, dass es die Datei unterstützt.

Fügen Sie in Ihrem Android-Manifest den Klick-Domain-Host und ein beliebiges Präfix in den Tag der Aktivität ein, in die Sie Deeplinks setzen möchten.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### Schritt 3b: Umgang mit den App Link Daten
Wenn Sie auf einen App-Link klicken, wird Ihre App geöffnet und das SDK wird gestartet. Um die App in die Lage zu versetzen, den OneLink hinter der Klick Domain zu extrahieren und den Deeplink aufzulösen, gehen Sie wie folgt vor:

1. Auflisten der Klick Domains in der SDK Methode [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Diese Eigenschaft muss vor der Initialisierung des SDK eingestellt werden.
2. Vergewissern Sie sich, dass Liste *spgo.io* eine der aufgeführten Domains ist. SparkPost besitzt diese Domain und sie ist Teil des Umleitungsflusses. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Sobald Sie die Integration abgeschlossen haben, können Sie die Qualitätssicherung und Fehlerbehebung durchführen, indem Sie einen Deeplink mit OneLink setzen. Einzelheiten zur Verwendung von OneLink finden Sie in der [AppsFlyer Dokumentation](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a).

### AppsFlyer Klick Tracking URLs in Braze (optional)

Sie können die [OneLink Attribution-Links](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) von AppsFlyer in Kampagnen von Braze für Push, E-Mail und mehr verwenden. Dies erlaubt es Ihnen, Daten zur Install-Attribution oder zum erneuten Engagement aus ihren Braze Kampagnen an AppsFlyer zurückzusenden. Auf diese Weise können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen treffen.

Sie können Ihre OneLink Tracking-URL einfach in AppsFlyer erstellen und sie direkt in Ihre Kampagnen in Braze einfügen. AppsFlyer verwendet dann seine [probabilistischen Attributionsmethoden](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling), um den Nutzer:innen, die auf den Link geklickt haben, zu attributieren. Wir empfehlen, Ihre AppsFlyer Tracking-Links mit einem Bezeichner für das Gerät zu versehen, um die Genauigkeit der Attributionen Ihrer Kampagnen von Braze zu verbessern. Dadurch wird der Nutzer:in, der auf den Link geklickt hat, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze den Kund:in, sich für die [Sammlung der Google Advertising ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die AppsFlyer SDK-Integration erfasst. Sie können die GAID in Ihre AppsFlyer Click Tracking Links einfügen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch AppsFlyer den IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Bezeichner für das Gerät verwendet werden. Sie können den Identifier for Vendors (IDFV) in Ihre AppsFlyer Click Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}



