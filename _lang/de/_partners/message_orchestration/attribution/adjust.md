---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Adjust, einem Unternehmen für mobile Attribution und Analyse, das es Ihnen ermöglicht, Daten zur nicht-organischen Installation zu importieren, um Ihre Lifecycle-Kampagnen intelligenter zu segmentieren."
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) ist ein Unternehmen für mobile Attribution und Analysen, das die Attribution von Werbequellen mit fortschrittlichen Analysen für ein umfassendes Bild der Business Intelligence kombiniert.



## Über die Integration

Mit der Integration von Braze und Adjust können Sie Daten zur nicht-organischen Installation importieren, um Ihre Lifecycle-Kampagnen intelligenter zu segmentieren.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Konto anpassen | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Adjust Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform sind in Ihrer Anwendung möglicherweise Codeschnipsel erforderlich. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| SDK anpassen | Zusätzlich zum erforderlichen Braze SDK müssen Sie das [Adjust SDK](https://dev.adjust.com/en/sdk) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Geräte-IDs zuordnen

#### Android

Wenn Sie eine Android-App haben, müssen Sie eine eindeutige Braze-Geräte-ID an Adjust übergeben. Diese ID kann in der Methode `addSessionPartnerParameter()` des Adjust SDK festgelegt werden. Der folgende Codeschnipsel muss vor der Initialisierung des SDK auf `Adjust.onCreate.`

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

Wenn Sie eine iOS-App haben, wird Ihr IDFV von Adjust erfasst und an Braze gesendet. Diese ID wird dann auf eine eindeutige Geräte-ID in Braze abgebildet.

 Andernfalls wird die IDFV als Ersatzidentifikator für die Zuordnung von Benutzern verwendet.

{% endtab %}
{% tab Swift %}

Wenn Sie eine iOS-App haben, können Sie sich für die Erfassung von IDFV entscheiden, indem Sie das Feld `useUUIDAsDeviceId` auf `false` setzen. Wenn dies nicht der Fall ist, wird die iOS-Attribution wahrscheinlich nicht genau von Adjust auf Braze übertragen. Weitere Informationen finden Sie unter [Sammeln von IDFV]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie planen, Ereignisse nach der Installation von Adjust an Braze zu senden, müssen Sie dies tun: <br><br>1) Stellen Sie sicher, dass Sie `external_id` als Sitzungs- und Ereignisparameter innerhalb des Adjust SDK anhängen. Für die Weiterleitung von Umsatzereignissen müssen Sie auch `product_id` als Parameter für Ereignisse einrichten. Weitere Informationen zur Definition von Partnerparametern für die Ereignisweiterleitung finden Sie in der [Dokumentation von Adjust](https://github.com/adjust/sdks).<br><br>2) Generieren Sie einen neuen API-Schlüssel für die Eingabe in Adjust. Wählen Sie dazu die Schaltfläche **API-Schlüssel generieren**, die Sie auf der Seite Partner anpassen im Braze Dashboard finden.
{% endalert %}

### Schritt 2: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Integrationen** > **Technologiepartner** und wählen Sie **Anpassen**. 

Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Adjust einrichten.<br><br>![Dieses Bild zeigt das Feld "Datenimport für Installationsattribution" auf der Seite Technologie anpassen. In diesem Feld werden Ihnen der Datenimportschlüssel und der REST-Endpunkt angezeigt.][1]{: style="max-width:90%;"}

### Schritt 3: Konfigurieren Sie Braze in Adjust

1. Navigieren Sie im Dashboard von Adjust zu **App-Einstellungen** und dann zu **Partnereinrichtung** und **Partner hinzufügen**.
2. Wählen Sie **Braze (früher Appboy)** und geben Sie den Datenimportschlüssel und den Braze REST-Endpunkt an.
3. Klicken Sie auf **Speichern & Schließen**.

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attributionsdaten von Adjust empfängt, ändert sich der Verbindungsstatus auf der Adjust-Technologiepartnerseite in Braze von "Nicht verbunden" auf "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt. 

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine zugeordnete Installation erhalten. Organische Installationen, die von der Postback-Anpassung ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht berücksichtigt.

## Verfügbare Datenfelder

Wenn Sie Ihre Integration wie vorgeschlagen konfigurieren, wird Braze die Daten von Adjust den Segmentfiltern zuordnen, wie in der folgenden Tabelle beschrieben.

| Datenfeld anpassen | Hartlöt-Segmentfilter |
| --- | --- |
| `{network_name}` | Zugeschriebene Quelle |
| `{campaign_name}` | Zugeschriebene Kampagne |
| `{adgroup_name}` | Zugeschriebene Anzeigengruppe |
| `{creative_name}` | Zugeschriebene Anzeige |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Facebook und X (früher Twitter) Attributionsdaten

Attributionsdaten für Kampagnen auf Facebook und X (ehemals Twitter) sind über unsere Partner nicht verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Anpassen der Click-Tracking-URLs in Braze (optional)

Durch die Verwendung von Klick-Tracking-Links in Ihren Braze-Kampagnen können Sie leicht erkennen, welche Kampagnen zu App-Installationen und Wiedereinstieg führen. So können Sie Ihre Marketingbemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen investieren sollten, um einen maximalen ROI zu erzielen.

Um mit Adjust Click Tracking Links zu beginnen, besuchen Sie die entsprechende [Dokumentation](https://help.adjust.com/tracking/attribution/tracker-urls). Sie können die Adjust Klick-Tracking-Links direkt in Ihre Braze-Kampagnen einfügen. Adjust verwendet dann seine [probabilistischen Zuordnungsmethoden](https://www.adjust.com/blog/attribution-compatible-with-ios14/), um den Nutzer, der auf den Link geklickt hat, zuzuordnen. Wir empfehlen Ihnen, Ihre Adjust-Tracking-Links mit einer Gerätekennung zu versehen, um die Genauigkeit der Zuordnungen Ihrer Braze-Kampagnen zu verbessern. Dadurch wird der Benutzer, der auf den Link geklickt hat, deterministisch zugeordnet.

{% tabs local %}
{% tab Android %}
 Die GAID wird auch nativ über die Adjust SDK-Integration erfasst. Sie können die GAID in Ihre Adjust Klick-Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS sammeln sowohl Braze als auch Adjust die IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Gerätekennung verwendet werden. Sie können die IDFV in Ihre Adjust Klick-Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie in Ihren Click-Tracking-Links derzeit keine Gerätekennungen wie die IDFV oder GAID verwenden oder dies in Zukunft nicht vorhaben, kann Adjust diese Klicks dennoch durch seine probabilistische Modellierung zuordnen.
{% endalert %}


[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}
