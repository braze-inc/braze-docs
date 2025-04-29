---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Adjust, einem Unternehmen für mobile Attribution und Analytics, das es Ihnen ermöglicht, Daten zur nicht-organischen Install-Attribution zu importieren, um innerhalb Ihrer Lebenszyklus-Kampagnen intelligenter zu segmentieren."
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) ist ein Unternehmen für mobile Attribution und Analytics, das Attribution für Werbequellen mit fortschrittlichen Analytics für ein umfassendes Bild der Business-Intelligence kombiniert.

_Diese Integration wird von Adjust gepflegt._

## Über die Integration

Mit der Integration von Braze und Adjust können Sie Daten zur nicht-organischen Install-Attribution importieren, um innerhalb Ihrer Lebenszyklus-Kampagnen intelligenter zu segmentieren.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Konto adjustieren | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Adjust Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| SDK anpassen | Neben dem erforderlichen Braze SDK müssen Sie auch das [Adjust SDK](https://dev.adjust.com/en/sdk) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Abbildung von Geräte IDs

#### Android

Wenn Sie eine Android App haben, müssen Sie Adjust eine eindeutige Braze ID für Ihr Gerät übergeben. Diese ID kann in der Methode `addSessionPartnerParameter()` des Adjust SDK festgelegt werden. Der folgende Code-Snippet muss vor der Initialisierung des SDK auf `Adjust.onCreate.`

```
Adjust.addSessionPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation as there will be no service disruption. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objective-C %}

Wenn Sie eine iOS App haben, wird Ihr IDFV von Adjust erfasst und an Braze gesendet. Diese ID wird dann einer eindeutigen ID des Geräts in Braze zugeordnet.

Braze speichert weiterhin IDFA-Werte für Nutzer:innen, die Opt-in gewählt haben, wenn Sie den IDFA mit Braze erfassen, wie in unserer [iOS-Upgraderklärung]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/) beschrieben. Andernfalls wird der IDFV als Fallback Bezeichner für die Abbildung von Nutzer:innen verwendet.

{% endtab %}
{% tab Swift %}

Wenn Sie eine iOS App haben, können Sie sich für die Erfassung von IDFV entscheiden, indem Sie das Feld `useUUIDAsDeviceId` auf `false` setzen. Wenn diese Option nicht gesetzt ist, wird die iOS Attribution wahrscheinlich nicht genau von Adjust auf Braze abgebildet. Weitere Informationen finden Sie unter [Sammeln von IDFV]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie planen, Ereignisse nach der Installation von Adjust an Braze zu senden, müssen Sie dies tun: <br><br>1) Stellen Sie sicher, dass Sie `external_id` als Sitzungs- und Ereignisparameter innerhalb des Adjust SDK anhängen. Für die Weiterleitung von Umsatzereignissen müssen Sie auch `product_id` als Parameter für Ereignisse einrichten. In der [Dokumentation von Adjust](https://github.com/adjust/sdks) finden Sie weitere Informationen zur Definition von Partner-Parametern für die Ereignisweiterleitung.<br><br>2) Generieren Sie einen neuen API-Schlüssel für die Eingabe in Adjust. Wählen Sie dazu den Button **API-Schlüssel generieren** auf der Adjust Partnerseite im Braze-Dashboard.
{% endalert %}

### Schritt 2: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Integrationen** > **Technologiepartner** und wählen Sie **Adjust**. 

Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Adjust einrichten.<br><br>![Dieses Bild zeigt das Feld "Datenimport für Install-Attribution", das Sie auf der Seite Technologie anpassen finden. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.][1]{: style="max-width:90%;"}

### Schritt 3: Braze in Adjust konfigurieren

1. Navigieren Sie im Dashboard von Adjust zu den **App-Einstellungen** und navigieren Sie zu **Partner Setup** und dann **zu Partner hinzufügen**.
2. Wählen Sie **Braze (früher Appboy)** und geben Sie den Datenimport-Schlüssel und den Braze REST Endpunkt an.
3. Klicken Sie auf **Speichern & Schließen**.

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attribution-Daten von Adjust erhält, ändert sich der Verbindungsstatus auf der Technologie-Partnerseite in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine attributierte Installation erhalten. Organische Installationen, die vom Adjust Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht mitgezählt.

## Verfügbare Datenfelder

Unter der Voraussetzung, dass Sie Ihre Integration wie vorgeschlagen konfigurieren, wird Braze die Daten von Adjust den Segmentierungsfiltern zuordnen, wie in der folgenden Tabelle beschrieben.

| Datenfeld anpassen | Braze Segmente Filter |
| --- | --- |
| `{network_name}` | Attributierte Quelle |
| `{campaign_name}` | Attribution-Kampagne |
| `{adgroup_name}` | Attributierte Anzeigengruppe |
| `{creative_name}` | Attributierte Anzeige |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Daten zur Attribution von Facebook und X (früher Twitter)

Attribution Daten für Facebook und X (ehemals Twitter) Kampagnen sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Adjustieren Sie die URLs für das Klick Tracking in Braze (optional)

Wenn Sie Tracking-Links für Klicks in Ihren Braze-Kampagnen verwenden, können Sie leicht erkennen, welche Kampagnen zu App-Installationen und erneuter Interaktion führen. So können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen für einen maximalen ROI investieren sollten.

Um mit Adjust Click Tracking Links zu beginnen, besuchen Sie die [Dokumentation](https://help.adjust.com/tracking/attribution/tracker-urls). Sie können die Adjust Klick Tracking Links direkt in Ihre Braze Kampagnen einfügen. Adjust verwendet dann seine [probabilistischen Attribution-Methoden](https://www.adjust.com/blog/attribution-compatible-with-ios14/), um den Nutzer:innen, die auf den Link geklickt haben, zu attributieren. Wir empfehlen, Ihre Adjust Tracking-Links mit einem Bezeichner für das Gerät zu versehen, um die Genauigkeit der Attributionen Ihrer Kampagnen von Braze zu verbessern. Dadurch wird der Nutzer:in, der auf den Link geklickt hat, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze den Kund:in, sich für die [Sammlung der Google Advertising ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Adjust SDK-Integration erfasst. Sie können die GAID in Ihre Adjust Click Tracking-Links einfügen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Adjust den IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Bezeichner für das Gerät verwendet werden. Sie können den Identifier for Vendors (IDFV) in Ihre Adjust Klick Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie in Ihren Click-through-Links derzeit keine Geräte-Identifikatoren wie den IDFV oder die GAID verwenden oder dies in Zukunft nicht vorhaben, kann Adjust diese Klicks dennoch durch seine probabilistische Modellierung attributieren.
{% endalert %}


[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}
