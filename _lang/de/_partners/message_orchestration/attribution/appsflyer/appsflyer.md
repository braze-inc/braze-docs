---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und AppsFlyer, einer Analyse- und Attributionsplattform für mobiles Marketing, die Sie bei der Analyse und Optimierung Ihrer Apps unterstützt."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyer ist eine Analyse- und Attributionsplattform für mobiles Marketing, die Sie bei der Analyse und Optimierung Ihrer Apps durch Marketing-Analysen, mobile Attribution und Deep Linking unterstützt.

Die Integration von Braze und AppsFlyer ermöglicht es Ihnen, besser zu verstehen, wie Sie Ihre Kampagnen optimieren und ganzheitlicher gestalten können, indem Sie die Attributionsdaten für mobile Installationen von AppsFlyer nutzen. 

Mit der AppsFlyer [Audiences-Integration]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/appsflyer_audiences/) können Sie auch Ihre AppsFlyer-Zielgruppen (Kohorten) direkt an Braze weitergeben. So können Sie leistungsstarke Kampagnen zur Kundenbindung erstellen, die sich genau an die richtigen Benutzer zur richtigen Zeit richten. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| AppsFlyer-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein AppsFlyer-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform sind in Ihrer Anwendung möglicherweise Codeschnipsel erforderlich. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| AppsFlyer SDK | Zusätzlich zum erforderlichen Braze SDK müssen Sie das [AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started) installieren.
| Einrichtung der E-Mail-Domäne abgeschlossen | Sie müssen den [Schritt]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) der [IP- und Domain-Einrichtung]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) bei der Einrichtung Ihrer E-Mail während des Braze Onboarding abgeschlossen haben. |
| SSL-Zertifikat | Ihr [SSL-Zertifikat]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) muss konfiguriert sein. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Geräte-ID zuordnen

{% tabs lokal %}
{% tab Android %}
Wenn Sie eine Android-App haben, müssen Sie eine eindeutige Braze-Geräte-ID an AppsFlyer übergeben. 

Stellen Sie sicher, dass die folgenden Codezeilen an der richtigen Stelle eingefügt werden - nachdem das Braze SDK gestartet wurde und vor dem Initialisierungscode für das AppsFlyer SDK. Weitere Informationen finden Sie in der AppsFlyer [Android SDK Integrationsanleitung](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk).

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
Vor Februar 2023 verwendete unsere AppsFlyer Attributionsintegration den IDFV als primären Identifikator, um iOS-Attributionsdaten abzugleichen. Für Braze-Kunden, die Objective-C verwenden, ist es nicht notwendig, die Braze `device_id` abzurufen und bei der Installation an AppsFlyer zu senden, da es keine Unterbrechung des Dienstes geben wird.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitige Kennung verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. 

Wenn Sie diese Option auf `true` setzen, müssen Sie die iOS-Geräte-ID-Zuordnung für Swift implementieren, um die Braze `device_id` bei der App-Installation an AppsFlyer zu übergeben, damit Braze die iOS-Attribute richtig zuordnen kann.

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

{% tab unity %}
Um die Geräte-ID in Unity zuzuordnen, gehen Sie wie folgt vor:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### Schritt 2: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **AppsFlyer**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im AppsFlyer Dashboard einrichten.<br><br>![Das Feld "Datenimport für Installationsattribution" ist auf der AppsFlyer Technologie-Seite verfügbar. In diesem Feld sind der Datenimportschlüssel und der REST-Endpunkt enthalten.][4]{: style="max-width:70%;"}

### Schritt 3: Konfigurieren Sie Braze im Dashboard von AppsFlyer

1. Navigieren Sie in AppsFlyer zur Seite **Integrierte Partner** in der linken Leiste. Suchen Sie dann nach **Braze** und klicken Sie auf das Logo von Braze, um ein Konfigurationsfenster zu öffnen.
2. Schalten Sie auf der Registerkarte **Integration** die Option **Partner aktivieren** ein.
3. Geben Sie den Datenimportschlüssel und den REST-Endpunkt an, den Sie im Dashboard von Braze gefunden haben. 
4. Schalten Sie den **erweiterten Datenschutz** aus und speichern Sie Ihre Konfiguration.

Weitere Informationen zu diesen Anweisungen finden Sie in der [AppsFlyer Dokumentation][16].

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attributionsdaten von AppsFlyer erhält, ändert sich der Status der Verbindungsanzeige auf der AppsFlyer-Technologiepartnerseite in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine zugeordnete Installation erhalten. Organische Installationen, die vom AppsFlyer-Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht mitgezählt.

### Schritt 5: Daten zur Benutzerzuordnung anzeigen

#### Verfügbare Datenfelder

Wenn Sie Ihre Integration wie vorgeschlagen konfigurieren, wird Braze alle nicht-organischen Installationsdaten den Segmentfiltern zuordnen.

| AppsFlyer Datenfeld | Braze-Segmentfilter |
| -------------------- | --------------------- |
| `media_source` | Zugeschriebene Quelle |
| `campaign` | Zugeschriebene Kampagne |
| `af_adset` | Zugeschriebene Anzeigengruppe |
| `af_ad` | Zugeschriebene Anzeige |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ihre Nutzerbasis kann im Braze Dashboard mit Hilfe der Filter für die Installationsattribution nach Attributionsdaten segmentiert werden.

![Vier verfügbare Filter. Die erste lautet: "Installieren Sie Attribution Source is network_val_0". Die zweite lautet "Attributionsquelle installieren ist campaign_val_0". Die dritte ist "Installieren Sie die Attributionsquelle adgroup_val_0". Die vierte ist "Attribution installieren Quelle ist creative_val_0". Neben den aufgelisteten Filtern können Sie sehen, wie diese Attributionsquellen dem Benutzerprofil hinzugefügt werden. Im Feld "Installationsattribution" auf der Informationsseite eines Benutzers wird die Installationsquelle als network_val_0, die Kampagne als campaign_val_0, usw. aufgeführt.][2]

Darüber hinaus sind die Attributionsdaten für einen bestimmten Benutzer im Profil jedes Benutzers im Braze Dashboard verfügbar.

{% alert note %}
Attributionsdaten für Kampagnen auf Facebook und X (ehemals Twitter) sind über unsere Partner nicht verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.
{% endalert %}

## Integrieren Sie AppsFlyer mit einem E-Mail-Dienstleister für Deep Linking

AppsFlyer ist sowohl mit SendGrid als auch mit SparkPost als E-Mail Service Provider (ESP) integriert, um Deep Linking und Click Tracking zu unterstützen. Folgen Sie den nachstehenden Anweisungen, um die Integration mit dem ESP Ihrer Wahl vorzunehmen.

{% alert tip %}
Deep Links - Links, die Benutzer zu einer bestimmten Seite oder Stelle innerhalb einer App oder Website führen - werden verwendet, um ein maßgeschneidertes Benutzererlebnis zu schaffen. Obwohl diese Funktion weit verbreitet ist, kann es zu Problemen kommen, wenn Sie per E-Mail versendete Deep Links mit Klick-Tracking verwenden, einer weiteren wichtigen Funktion zur Erfassung von Benutzerdaten. Diese Probleme sind darauf zurückzuführen, dass ESPs Deep Links in eine klickaufzeichnende Domain verpacken, wodurch der ursprüngliche Link unterbrochen wird. Daher erfordert die Unterstützung von Deep Links zusätzliche Einstellungen. Durch die Integration von AppsFlyer mit SendGrid oder SparkPost können Sie diese Probleme vermeiden. Erfahren Sie mehr über dieses Thema in [Universal Links und App Links]({{site.baseurl}}/help/help_articles/email/universal_links/).
{% endalert %}

### Schritt 1: OneLink in AppsFlyer einrichten

1. Wählen Sie in AppsFlyer eine OneLink-Vorlage für Ihre E-Mail-Kampagnen. Stellen Sie sicher, dass die Vorlage universelle Links (iOS) oder App-Links (Android) unterstützt. 
2. Konfigurieren Sie Ihre App so, dass sie Deep Linking mit OneLink unterstützt. In der [AppsFlyer-Dokumentation](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup) finden Sie Einzelheiten zur Konfiguration Ihrer App für die Unterstützung von OneLink.

### Schritt 2: Konfigurieren Sie Ihre App für die Unterstützung von Universal Links und App Links

Universelle Links (iOS) oder App-Links (Android) erlauben es dem Betriebssystem des Geräts, eine bestimmte App zu öffnen, wenn Sie darauf klicken.

Führen Sie die folgenden Schritte aus, um Universal Links und App Links zu unterstützen.

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
Richten Sie das Dateihosting der Apple App Site Association (AASA) ein, um universelle Links in Ihren Emails zu ermöglichen.

1. Beschaffen Sie sich eine AASA-Datei auf eine der folgenden Arten:
    * Wenn Sie OneLink mit universellen Links eingerichtet haben, haben Sie möglicherweise bereits eine AASA-Datei, die mit OneLink verknüpft ist. Um die AASA-Datei zu erhalten, gehen Sie wie folgt vor:
        * Kopieren Sie die OneLink-Subdomain Ihrer OneLink-Vorlage. Stellen Sie sicher, dass die Vorlage universelle Links unterstützt.
        * Fügen Sie ihn anstelle des Platzhalters in die folgende URL ein: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Um die AASA-Datei herunterzuladen, fügen Sie die OneLink-URL in die Adressleiste Ihres Browsers ein und drücken die **Eingabetaste**. Die Datei wird dann auf Ihren Computer heruntergeladen, und Sie können den Inhalt mit einem beliebigen Texteditor öffnen und anzeigen.
    * [In der Anleitung von Apple zu universellen Links](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) wird erklärt, wie Sie die AASA-Datei erstellen können.
2. Hosten Sie die AASA-Datei auf Ihrem Domain-Server für die Klickaufzeichnung. Die Datei sollte in dem Pfad: `click.example.com/.well-known/apple-app-site-association` abgelegt werden. 

In der [SendGrid-Dokumentation](https://docs.sendgrid.com/ui/sending-email/universal-links) erfahren Sie, wie Sie die AASA-Datei für SendGrid konfigurieren und CDN-Dienste zum Hosten der AASA-Datei einrichten.

{% alert important %}
Sobald die AASA-Datei gehostet wird, muss für jede Änderung Ihrer OneLink-Konfiguration (Modifikation oder Austausch) eine neue AASA-Datei erstellt werden.
{% endalert %}
{% endsubtab %}
{% subtab Android %}
Richten Sie das Dateihosting für Digital Asset Links ein, um App-Links in Ihren E-Mails zu aktivieren.

1. Beziehen Sie eine Digital Asset Links-Datei auf eine der folgenden Arten:
    * Wenn Sie OneLink mit App Links eingerichtet haben, verfügen Sie möglicherweise bereits über eine mit OneLink verknüpfte Digital Asset Links-Datei. Um die Datei zu erhalten, gehen Sie wie folgt vor:
        * Kopieren Sie die OneLink-Subdomain Ihrer OneLink-Vorlage. Stellen Sie sicher, dass die Vorlage App-Links unterstützt.
        * Fügen Sie `/.well-known/assetlinks.json` an das Ende der OneLink URL an.
        * Um die Datei Digital Asset Links herunterzuladen, fügen Sie die OneLink URL in die Adressleiste Ihres Browsers ein und drücken Sie die **Eingabetaste**. Zum Beispiel: `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. Die Datei wird dann auf Ihren Computer heruntergeladen, und Sie können den Inhalt mit einem beliebigen Texteditor öffnen und anzeigen.
    * [Die Android-Anleitung zu App-Links](https://developer.android.com/studio/write/app-link-indexing) erklärt, wie Sie die Datei Digital Asset Links erstellen.
2. Hosten Sie die Datei mit den digitalen Asset-Links auf dem Server Ihrer Click-Recording-Domain. Die Datei sollte in dem Pfad: `click.example.com/.well-known/apple-app-site-association` abgelegt werden.

In der [SendGrid-Dokumentation](https://docs.sendgrid.com/ui/sending-email/universal-links) erfahren Sie, wie Sie die Digital Asset Links-Datei für SendGrid konfigurieren und CDN-Dienste zum Hosten der Digital Asset Links-Datei einrichten.

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
Richten Sie das Dateihosting der Apple App Site Association (AASA) ein, um universelle Links in Ihren Emails zu ermöglichen.

1. Beschaffen Sie sich eine AASA-Datei auf eine der folgenden Arten:
    * Wenn Sie OneLink mit universellen Links eingerichtet haben, haben Sie möglicherweise bereits eine AASA-Datei, die mit OneLink verknüpft ist. Um die AASA-Datei zu erhalten, gehen Sie wie folgt vor:
        * Kopieren Sie die OneLink-Subdomain Ihrer OneLink-Vorlage. Stellen Sie sicher, dass die Vorlage universelle Links unterstützt.
        * Fügen Sie ihn anstelle des Platzhalters in die folgende URL ein: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Um die AASA-Datei herunterzuladen, fügen Sie die OneLink-URL in die Adressleiste Ihres Browsers ein und drücken die **Eingabetaste**. Die Datei wird dann auf Ihren Computer heruntergeladen, und Sie können den Inhalt mit einem beliebigen Texteditor öffnen und anzeigen.
    * [In der Anleitung von Apple zu universellen Links](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) wird erklärt, wie Sie die AASA-Datei erstellen können.
2. Hosten Sie die AASA-Datei auf Ihrem Domain-Server für die Klickaufzeichnung. Die Datei sollte in dem Pfad: `click.example.com/.well-known/apple-app-site-association` abgelegt werden. 

In der [SparkPost-Dokumentation](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) erfahren Sie, wie Sie die AASA-Datei für SparkPost konfigurieren und benutzerdefinierte Link-Unterpfade festlegen.

{% alert important %}
Sobald die AASA-Datei gehostet wird, muss für jede Änderung Ihrer OneLink-Konfiguration (Modifikation oder Austausch) eine neue AASA-Datei erstellt werden.
{% endalert %}

#### Schritt 2b: Leiten Sie Ihre Click-Tracking-Domain auf Ihren AASA-Dateihost um
Während Ihrer [E-Mail-Konfiguration]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) haben Sie einen CNAME-Eintrag in Ihrem DNS-Server erstellt. Führen Sie die folgenden Schritte aus, nachdem Sie Ihre Click-Tracking-Domain in Braze überprüft haben. 

1. Löschen Sie den CNAME-Eintrag, der Ihre Subdomain auf die SparkPost-Domain umleitet.
2. Erstellen Sie einen CNAME-Eintrag, der Ihre Click-Tracking-Domain auf das CDN umleitet, das Ihre App-AASA-Datei hostet, anstelle des Eintrags, den Sie oben gelöscht haben.
{% endsubtab %}
{% subtab Android %}
#### Schritt 2a: Einrichten von Digital Asset Links zum Hosten von Dateien
Richten Sie das Dateihosting für Digital Asset Links ein, um App-Links in Ihren E-Mails zu aktivieren.

1. Beziehen Sie eine Digital Asset Links-Datei auf eine der folgenden Arten:
    * Wenn Sie OneLink mit App Links eingerichtet haben, verfügen Sie möglicherweise bereits über eine mit OneLink verknüpfte Digital Asset Links-Datei. Um die Datei zu erhalten, gehen Sie wie folgt vor:
        * Kopieren Sie die OneLink-Subdomain Ihrer OneLink-Vorlage. Stellen Sie sicher, dass die Vorlage App-Links unterstützt.
        * Fügen Sie `/.well-known/assetlinks.json` an das Ende der OneLink URL an.
        * Um die Datei Digital Asset Links herunterzuladen, fügen Sie die OneLink URL in die Adressleiste Ihres Browsers ein und drücken Sie die **Eingabetaste**. Zum Beispiel: `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. Die Datei wird dann auf Ihren Computer heruntergeladen, und Sie können den Inhalt mit einem beliebigen Texteditor öffnen und anzeigen.
    * [Die Android-Anleitung zu App-Links](https://developer.android.com/studio/write/app-link-indexing) erklärt, wie Sie die Datei Digital Asset Links erstellen.
2. Hosten Sie die Datei mit den digitalen Asset-Links auf dem Server Ihrer Click-Recording-Domain. Die Datei sollte in dem Pfad: `click.example.com/.well-known/apple-app-site-association` abgelegt werden.

In der [SparkPost-Dokumentation](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) erfahren Sie, wie Sie die Datei Digital Asset Links für SparkPost konfigurieren und benutzerdefinierte Link-Unterpfade festlegen.

{% alert important %}
Sobald die Datei mit den digitalen Asset-Links gehostet wird, muss für jede Änderung Ihrer OneLink-Konfiguration (Modifikation oder Austausch) eine neue Datei erstellt werden.
{% endalert %}

#### Schritt 2b: Leiten Sie Ihre Click-Tracking-Domain zu Ihrem Dateihoster für digitale Asset-Links um
Während Ihrer [E-Mail-Konfiguration]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) haben Sie einen CNAME-Eintrag in Ihrem DNS-Server erstellt. Führen Sie die folgenden Schritte aus, nachdem Sie Ihre Click-Tracking-Domain in Braze überprüft haben. 

1. Löschen Sie den CNAME-Eintrag, der Ihre Subdomain auf die SparkPost-Domain umleitet.
2. Erstellen Sie einen CNAME-Eintrag, der Ihre Click-Tracking-Domain auf das CDN umleitet, in dem Ihre App Digital Asset Links-Datei gehostet wird, und nicht auf den Eintrag, den Sie oben gelöscht haben.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Schritt 3: Konfigurieren Sie Ihr AppsFlyer SDK für die Unterstützung von Deep Linking

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
#### Schritt 3a: Konfigurieren Sie Ihr SDK so, dass es die AASA-Datei unterstützt
Nachdem Sie die AASA-Datei in Ihrer Click-Recording-Domain gehostet haben, konfigurieren Sie Ihr AppsFlyer SDK für die Unterstützung der AASA-Datei.

1. Wählen Sie in Xcode Ihr Projekt aus.
2. Wählen Sie **Fähigkeiten.**
3. Aktivieren Sie **Assoziierte Domains.**
4. Klicken Sie auf **+**, und geben Sie Ihre Klick-Domain ein. Zum Beispiel: `applinks:click.example.com`.
Wenn ein Klick auf den universellen Link erfolgt, wird Ihre App geöffnet und das SDK wird gestartet. Um die App in die Lage zu versetzen, den OneLink hinter der Klick-Domäne zu extrahieren und den Deep Link aufzulösen, gehen Sie wie folgt vor:

#### Schritt 3b: Bearbeiten Sie die Deep-Link-Daten
1. Stellen Sie der SDK-API die Klickaufzeichnungsdomäne zur Verfügung [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Diese API muss vor der Initialisierung des SDKs aufgerufen werden. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. Verwenden Sie die [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API, um die Deep-Link-Parameter abzurufen und die Deep-Link-Daten zu verarbeiten.

{% endsubtab %}
{% subtab Android %}
#### Schritt 3a: Konfigurieren Sie Ihr SDK für die Unterstützung der Datei Digital Asset Links

Nachdem Sie im vorigen Schritt die Datei mit den digitalen Asset-Links in Ihrer Click-Recording-Domäne gehostet haben, konfigurieren Sie Ihr SDK so, dass es die Datei unterstützt.

Fügen Sie in Ihrem Android-Manifest den Click-Domain-Host und ein beliebiges Präfix in das Activity-Tag der Aktivität ein, in die Sie einen Deep Link einfügen möchten.

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

#### Schritt 3b: Bearbeiten Sie die Deep-Link-Daten
Wenn ein Klick auf einen App-Link erfolgt, wird Ihre App geöffnet und das SDK wird gestartet.  Damit die App den OneLink hinter der Klick-Domäne extrahieren und den Deep Link auflösen kann, listen Sie die Klick-Domänen in der SDK-Methode auf [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Diese Eigenschaft muss vor der SDK-Initialisierung eingestellt werden. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Schritt 3a: Konfigurieren Sie Ihr SDK so, dass es die AASA-Datei unterstützt
Nachdem Sie die AASA-Datei in Ihrer Click-Recording-Domain gehostet haben, konfigurieren Sie Ihr SDK für die Unterstützung der AASA-Datei.

1. Wählen Sie in Xcode Ihr Projekt aus.
2. Wählen Sie **Fähigkeiten.**
3. Aktivieren Sie **Assoziierte Domains.**
4. Klicken Sie auf **+**, und geben Sie Ihre Klick-Domain ein. Zum Beispiel: `applinks:click.example.com`.

#### Schritt 3b: Bearbeiten Sie die Deep-Link-Daten
Wenn ein Klick auf den universellen Link erfolgt, wird Ihre App geöffnet und das SDK wird gestartet. Um das SDK in die Lage zu versetzen, den OneLink hinter der Klick-Domäne zu extrahieren, gehen Sie wie folgt vor:
1. Listen Sie die Klick-Domänen in der SDK-Eigenschaft  [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Stellen Sie sicher, dass Sie diese Eigenschaft vor der SDK-Initialisierung einstellen.
2. Vergewissern Sie sich, dass Liste <em>spgo.io</em> eine der aufgelisteten Domänen ist. SparkPost ist Eigentümer dieser Domain und sie ist Teil des Weiterleitungsflusses. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. Verwenden Sie die [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API, um die Deep-Link-Parameter abzurufen und die Deep-Link-Daten zu verarbeiten.
{% endsubtab %}
{% subtab Android %}
#### Schritt 3a: Konfigurieren Sie Ihr SDK für die Unterstützung der Datei Digital Asset Links

Nachdem Sie im vorigen Schritt die Datei mit den digitalen Asset-Links in Ihrer Click-Recording-Domäne gehostet haben, konfigurieren Sie Ihr SDK so, dass es die Datei unterstützt.

Fügen Sie in Ihrem Android-Manifest den Click-Domain-Host und ein beliebiges Präfix in das Activity-Tag der Aktivität ein, in die Sie einen Deep Link einfügen möchten.

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

#### Schritt 3b: Verarbeiten Sie die App Link Daten
Wenn ein Klick auf einen App-Link erfolgt, wird Ihre App geöffnet und das SDK wird gestartet. Um die App in die Lage zu versetzen, den OneLink hinter der Klick-Domäne zu extrahieren und den Deep Link aufzulösen, gehen Sie wie folgt vor:

1. Listen Sie die Klick-Domänen in der SDK-Methode auf [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Diese Eigenschaft muss vor der SDK-Initialisierung eingestellt werden.
2. Vergewissern Sie sich, dass Liste *spgo.io* eine der aufgelisteten Domänen ist. SparkPost ist Eigentümer dieser Domain und sie ist Teil des Weiterleitungsflusses. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Sobald Sie die Integrationsschritte abgeschlossen haben, können Sie die Qualitätssicherung und Fehlerbehebung durchführen, indem Sie einen Deep Link mit OneLink senden. Einzelheiten zur Verwendung von OneLink finden Sie in der [AppsFlyer-Dokumentation](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a).

### AppsFlyer Klick-Tracking-URLs in Braze (optional)

Sie können die [OneLink-Attributionslinks](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) von AppsFlyer in Braze-Kampagnen für Push, E-Mail und mehr verwenden. So können Sie die Installations- oder Re-Engagement-Attributionsdaten aus ihren Braze-Kampagnen an AppsFlyer zurücksenden. So können Sie Ihre Marketingbemühungen effektiver messen und datengestützte Entscheidungen treffen.

Sie können Ihre OneLink-Tracking-URL einfach in AppsFlyer erstellen und sie direkt in Ihre Braze-Kampagnen einfügen. AppsFlyer verwendet dann seine [probabilistischen Zuordnungsmethoden](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling), um den Benutzer zuzuordnen, der auf den Link geklickt hat. Wir empfehlen Ihnen, Ihre AppsFlyer-Tracking-Links mit einer Gerätekennung zu versehen, um die Genauigkeit der Zuordnungen Ihrer Braze-Kampagnen zu verbessern. Dadurch wird der Benutzer, der auf den Link geklickt hat, deterministisch zugeordnet.

{% tabs local %}
{% tab Android %}
Für Android ermöglicht Braze seinen Kunden, sich für die [Erfassung der Google Werbe-ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die AppsFlyer SDK-Integration erfasst. Sie können die GAID in Ihre AppsFlyer Klick-Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS sammeln sowohl Braze als auch AppsFlyer die IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Gerätekennung verwendet werden. Sie können die IDFV in Ihre AppsFlyer Klick-Tracking-Links einbinden, indem Sie die folgende Liquid-Logik verwenden:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}



[1]: {% image_buster /assets/img/braze_integration.png %}
[2]: {% image_buster /assets/img/braze_attribution.png %}
[3]: https://support.appsflyer.com/hc/en-us/articles/360001294118
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[31]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration
[4]: {% image_buster /assets/img/attribution/appsflyer.png %}
