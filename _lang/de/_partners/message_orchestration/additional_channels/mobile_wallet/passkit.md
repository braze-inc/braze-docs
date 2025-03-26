---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Passkit. Diese Partnerschaft ermöglicht es Ihnen, Ihre mobile Reichweite zu vergrößern, indem Sie Apple Wallet und Google Pay-Pässe in das Erlebnis Ihrer Kunden integrieren."
page_type: partner
search_tag: Partner

---

# PassKit

> Mit PassKit können Sie Ihre mobile Reichweite erweitern, indem Sie Apple Wallet- und Google Pay-Pässe in das Erlebnis Ihrer Kunden integrieren. Erstellen, verwalten, verteilen und analysieren Sie ganz einfach die Leistung von digitalen Coupons, Kundenkarten, Mitgliedskarten, Tickets und vielem mehr, ohne dass Ihre Kunden eine weitere App benötigen.

Die Integration von Braze und PassKit ermöglicht es Ihnen, das Engagement Ihrer Online-Kampagnen zu erhöhen und zu messen, indem Sie sofort benutzerdefinierte Apple Wallet- und Google Pay-Pässe bereitstellen. Sie können dann die Nutzung analysieren und in Echtzeit Anpassungen vornehmen, um die Besucherzahlen in den Geschäften zu erhöhen, indem Sie standortbezogene Nachrichten und personalisierte, dynamische Updates für die mobile Geldbörse Ihrer Kunden auslösen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| PassKit Konto | Sie benötigen ein PassKit-Konto und einen PassKit-Kontomanager. |
| `userDefinedID` | Um benutzerdefinierte Ereignisse und benutzerdefinierte Attribute für Ihre Benutzer zwischen PassKit und Braze zu aktualisieren, müssen Sie die externe ID von Braze als `userDefinedID` festlegen. Diese `userDefinedID` wird verwendet, wenn Sie API-Aufrufe an die PassKit-Endpunkte tätigen. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze URL für Ihre Instanz][6] ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Um die Erfahrungen Ihrer Kunden mit mobilen Geldbörsen weiter zu verbessern, können Sie von Ihrem PassKit-Dashboard aus Daten über den [`/users/track` Endpunkt von Braze][7] an Braze weitergeben. 

Beispiele für Daten, die Sie von PassKit weitergeben können, sind:
- **Pass erstellt**: wenn ein Kunde auf einen Pass-Link klickt und zum ersten Mal einen Pass angezeigt bekommt.
- **Pass-Installationen**: wenn der Kunde den Pass zu seiner Brieftaschen-App hinzufügt und speichert.
- **Pass-Updates**: wenn ein Pass aktualisiert wird.
- **Pass löschen**: wenn ein Kunde den Pass aus seiner Brieftaschen-App löscht.

Sobald die Daten an Braze übergeben wurden, können Sie Zielgruppen erstellen, Inhalte über Liquid personalisieren und Kampagnen oder Canvases auslösen, nachdem diese Aktionen durchgeführt wurden.

## Passkit mit Braze verbinden

Um Daten von PassKit zu übergeben, stellen Sie sicher, dass Sie Ihre externe ID von Braze als `externalId` von PassKit eingestellt haben.

1. Klicken Sie in den **Einstellungen** unter **Integrationen** in Ihrem PassKit Pass-Projekt oder -Programm auf **Verbinden** unter der Registerkarte **Braze**.<br>![Die Braze-Integrationskachel in der PassKit-Plattform.][5]{: style="max-width:80%"}<br><br>
2. Geben Sie Ihren Braze-API-Schlüssel und die Endpunkt-URL ein und vergeben Sie einen Namen für Ihren Connector.<br><br>
3. Aktivieren Sie die Option **Integration aktivieren** und wählen Sie die Ereignisse aus, die Sie in Braze auslösen oder mit denen Sie Ihre Nachrichten personalisieren möchten.<br>![Die PassKit Braze-Integrationskachel wurde erweitert, um den API-Schlüssel, die Endpunkt-URL, den Integrationsnamen, die Aktivierungseinstellungen, die Mitgliedschaftseinstellungen und die Passeinstellungen zu akzeptieren.][4]{: style="max-width:70%"}

## Pass über einen SmartPass-Link erstellen

Innerhalb von Braze können Sie einen SmartPass-Link einrichten, um eine eindeutige URL für Ihre Kunden zu generieren, mit der sie ihren Pass entweder auf Android oder iOS installieren können. Dazu müssen Sie eine verschlüsselte SmartPass-Daten-Nutzlast definieren, die von einem Braze Content Block aufgerufen werden kann. Dieser [Content Block][9] kann dann für zukünftige Pässe und Coupons wiederverwendet werden. Die folgenden Informationen werden während Ihrer Integration verwendet:

- **PassKit URL**: Ihre PassKit URL ist eine eindeutige URL für Ihr PassKit Programm.<br>Jedes Programm hat eine eindeutige URL, die Sie auf der Registerkarte **Verteilung** Ihres PassKit-Programms oder -Projekts finden können. (zum Beispiel, https://pub1.pskt.io/c/ww0jir)<br><br>
- **PassKit Geheimnis**: Zusammen mit der URL müssen Sie den PassKit Key für dieses Programm bereithalten.<br>Diese finden Sie auf der gleichen Seite wie Ihre PassKit-URL.<br><br>
- **Programm (oder Projekt) ID**: Ihre PassKit Programm-ID wird benötigt, um die SmartPass URL zu erstellen. <br>Sie finden sie auf der Registerkarte **Einstellungen** Ihres Projekts oder Programms.

Weitere Informationen zur Erstellung verschlüsselter SmartPass-Links finden Sie in diesem [PassKit-Artikel][8].

### Schritt 1: Definieren Sie Ihre Passdaten-Nutzlast {#passkit-integrations}

Zunächst müssen Sie die Nutzlast des Coupons oder Mitglieds definieren. 

Es gibt viele verschiedene Komponenten, die Sie in Ihre Nutzlast aufnehmen können, aber hier sind zwei wichtige zu nennen:

| Komponente | Erforderlich | Typ | Beschreibung |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | Erforderlich | String | Die externe ID von Braze ist entscheidend dafür, dass die Rückrufe von PassKit zurück nach Braze funktionieren. So können Braze-Benutzer Gutscheine für mehrere Angebote in einer Kampagne haben. Nicht als einzigartig erzwungen. |
| `members.member.externalId` | Optional | String | Als externe ID von Braze eingestellt, können Sie Ihre externe ID verwenden, um den Mitgliedsausweis zu aktualisieren. Wenn Sie dieses Feld setzen, wird der Benutzer innerhalb des Mitgliedschaftsprogramms als eindeutig eingestuft.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Eine vollständige Liste der verfügbaren Felder, ihre Typen und hilfreiche Beschreibungen finden Sie in der [PassKit GitHub Dokumentation][10].

#### Beispiel-Nutzlast
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### Schritt 2: Erstellen und kodieren Sie eine undefinierte Nutzlastvariable

Erstellen und benennen Sie einen neuen Inhaltsblock, indem Sie im Braze Dashboard zu **Vorlagen** > **Inhaltsblöcke** navigieren.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Inhaltsblock-Bibliothek**.
{% endalert %}

Wählen Sie **Inhaltsblock erstellen**, um zu beginnen.

Als nächstes müssen Sie Ihr **Content Block Liquid Tag** definieren. Nachdem Sie diesen Inhaltsblock gespeichert haben, können Sie beim Verfassen von Nachrichten auf dieses Liquid-Tag verweisen. In diesem Beispiel haben wir das Tag Liquid als {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %} zugewiesen. 

Innerhalb dieses Inhaltsblocks werden wir die Nutzdaten nicht direkt einbinden, sondern in einer {% raw %}`{{passData}}`{% endraw %} Variablen referenzieren. Der erste Codeschnipsel, den Sie zu Ihrem Inhaltsblock hinzufügen müssen, erfasst eine Base64-Kodierung der Variable {% raw %}`{{passData}}`{% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### Schritt 3: Erstellen Sie Ihre Verschlüsselungssignatur mit einem SHA1 HMAC-Hash

Als nächstes erstellen Sie Ihre Verschlüsselungssignatur unter Verwendung eines [SHA1 HMAC][16] Hashes der Projekt-URL und der Nutzdaten. 

Der zweite Codeschnipsel, den Sie zu Ihrem Content Block hinzufügen müssen, erfasst die URL, die für das Hashing verwendet werden soll.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

Als nächstes müssen Sie mit diesem Hash und Ihrer `Project Secret` eine Signatur erzeugen. Dazu können Sie einen dritten Codeschnipsel einfügen:
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Zum Schluss fügen Sie die Signatur mit dem fünften Codeschnipsel an die vollständige URL an:
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Schritt 4: Drucken Sie Ihre URL

Vergewissern Sie sich schließlich, dass Sie Ihre endgültige URL so aufrufen, dass Ihre SmartPass-URL in Ihrer Nachricht gedruckt wird.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

An diesem Punkt haben Sie einen Inhaltsblock erstellt, der in etwa wie folgt aussieht:

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

In diesem Beispiel wurden UTM-Parameter hinzugefügt, um die Quelle dieser Installationen bis zu Braze und dieser Kampagne zurückzuverfolgen.

{% alert tip %}
Denken Sie daran, Ihren Inhaltsblock zu speichern, bevor Sie die Seite verlassen.
{% endalert %}

### Schritt 5: Alles zusammenfügen

Sobald dieser Inhaltsblock erstellt wurde, kann er in Zukunft wieder verwendet werden. 

Sie werden feststellen, dass im Beispiel Content Block zwei Variablen undefiniert sind.<br> 
{% raw %}`{{passData}}`{% endraw %} - Ihre in [Schritt 1](#passkit-integrations) definierte JSON-Pass-Daten-Nutzlast <br>
{% raw %}`{{projectUrl}}`{% endraw %} - Die URL Ihres Projekts oder Programms, die Sie auf der Registerkarte Verteilung Ihres Passkit-Projekts finden.

Diese Entscheidung ist zweckmäßig und unterstützt die Wiederverwendbarkeit des Content Blocks. Da diese Variablen nur referenziert und nicht innerhalb des Inhaltsblocks erstellt werden, können diese Variablen geändert werden, ohne dass der Inhaltsblock neu erstellt werden muss. 

Vielleicht möchten Sie zum Beispiel das Einführungsangebot ändern, um mehr Anfangspunkte in Ihr Treueprogramm aufzunehmen, oder Sie möchten eine zweite Mitgliedskarte oder einen Coupon erstellen. Diese Szenarien würden unterschiedliche Passkit `projectURLs` oder unterschiedliche Pass Payloads erfordern, die Sie pro Kampagne in Braze definieren würden.  

#### Verfassen des Nachrichtentextes

Sie sollten diese beiden Variablen in Ihrem Nachrichtentext erfassen und dann Ihren Inhaltsblock aufrufen.
Erfassen Sie Ihre verkleinerte JSON-Nutzlast aus [Schritt 1](#passkit-integrations):

**Weisen Sie die Projekt-URL zu**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**Erfassen Sie das JSON**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**Verweisen Sie auf den Inhaltsblock, den Sie gerade erstellt haben**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

Ihr Nachrichtentext sollte in etwa so aussehen:
![Ein Bild des Content Block Message Composers mit dem erfassten JSON und der Content Block-Referenz wird angezeigt.][1]{: style="max-width:70%"}

Die Ausgabe-URL für das Beispiel lautet:
![Die Ausgabe-URL, die eine lange, zufällig generierte Zeichenfolge aus Buchstaben und Zahlen enthält.][2]{: style="max-width:70%"}

Die Ausgabe-URL wird lang sein. Der Grund dafür ist, dass sie alle Passdaten enthält und über erstklassige Sicherheitsvorkehrungen verfügt, um die Integrität der Daten zu gewährleisten und eine Verfälschung durch URL-Änderungen zu verhindern. Wenn Sie diese URL per SMS verbreiten, sollten Sie sie durch einen Linkverkürzungsprozess wie [bit.ly][3] laufen lassen. Dies kann über einen Aufruf von Connected Content an einen bit.ly Endpunkt erfolgen.

## Pass mit dem PassKit Webhook aktualisieren

In Braze können Sie eine Webhook-Kampagne oder einen Webhook innerhalb eines Canvas einrichten, um einen bestehenden Pass auf der Grundlage des Verhaltens Ihres Benutzers zu aktualisieren. Unter den folgenden Links finden Sie Informationen zu nützlichen PassKit-Endpunkten. 
- [Projekte der Mitglieder][12]
- [Coupon-Projekte][13]
- [Flugprojekte][14]

### Parameter der Nutzlast

Bevor Sie beginnen, finden Sie hier die üblichen JSON-Payload-Parameter, die Sie in Ihre Webhooks zum Erstellen und Aktualisieren von PassKit aufnehmen können.

| Daten | Typ | Beschreibung |
| ---- | ---- | ----------- |
| `externalId` | String | Ermöglicht das Hinzufügen einer eindeutigen Kennung zum Passdatensatz, um die Kompatibilität mit einem bestehenden System zu gewährleisten, das eindeutige Kundenkennungen verwendet (z. B. Mitgliedsnummern). Sie können die Passdaten über diesen Endpunkt über `userDefinedId` und `campaignName` anstelle der Pass-ID abrufen. Dieser Wert muss innerhalb einer Kampagne eindeutig sein, und nachdem dieser Wert festgelegt wurde, kann er nicht mehr geändert werden.<br><br>Für die Integration von Braze empfehlen wir die Verwendung der externen Braze-ID: {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (Coupon) <br><br> `programId` (Mitgliedschaft) | String | Die ID für die Kampagne oder Programmvorlage, die Sie in PassKit erstellt haben. Gehen Sie dazu auf die Registerkarte **Einstellungen** in Ihrem PassKit-Pass-Projekt. |
| `expiryDate` | IO8601 datetime | Das Ablaufdatum des Passes. Nach Ablauf der Gültigkeitsdauer wird der Pass automatisch entwertet (siehe `isVoided`). Dieser Wert hat Vorrang vor dem Wert der Vorlage und dem Enddatum der Kampagne. |
| `status` | String | Der aktuelle Status eines Coupons, wie `REDEEMED` oder `UNREDEEMED`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 1: Erstellen Sie Ihre Braze Webhook-Vorlage

Um eine PassKit-Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvases verwenden können, navigieren Sie zum Abschnitt **Vorlagen & Medien** im Braze Dashboard. Wenn Sie eine einmalige PassKit-Webhook-Kampagne erstellen oder eine vorhandene Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen.

Sobald Sie die PassKit Webhook-Vorlage ausgewählt haben, sollten Sie folgendes sehen:
- **Webhook URL**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

PassKit benötigt zur Autorisierung eine `HTTP Header`, die Ihren PassKit API-Schlüssel in Base 64 verschlüsselt enthält. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber auf der Registerkarte **Einstellungen** müssen Sie `<PASSKIT_LONG_LIVED_TOKEN>` durch Ihr PassKit-Token ersetzen. Um Ihr Token abzurufen, navigieren Sie zu Ihrem PassKit-Projekt/Programm und gehen Sie zu **Einstellungen > Integrationen > Langlebiges Token**.

{% raw %}
- **HTTP-Methode**: PUT
- **Kopfzeile der Anfrage**:
  - **Autorisierung**: Träger `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Inhalt-Typ**: application/json
{% endraw %}

#### Anfragetext

Um den Webhook einzurichten, geben Sie die Details des neuen Ereignisses in den Anfragekörper ein, einschließlich der für Ihren Anwendungsfall erforderlichen Payload-Parameter:

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### Schritt 2: Vorschau Ihrer Anfrage

Ihr Rohtext wird automatisch hervorgehoben, wenn es sich um ein anwendbares Braze-Tag handelt. 

Zeigen Sie Ihre Anfrage in der **Vorschau** an oder wechseln Sie zur Registerkarte **Test**, wo Sie einen zufälligen Benutzer, einen vorhandenen Benutzer oder einen eigenen Benutzer auswählen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

## Abrufen von Passdetails über Connected Content

Sie können nicht nur Pässe erstellen und aktualisieren, sondern auch die Pass-Metadaten Ihrer Benutzer über [Connected Content][15] ] von Braze abrufen, um personalisierte Passdetails in Ihre Messaging-Kampagnen einzubinden.

**Aufruf von PassKit Connected Content**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Flüssige Beispielantworten**

{% tabs local %}
{% tab Passiert EinlösungDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab passiert Status %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/passkit/passkit1.png %}
[2]: {% image_buster /assets/img/passkit/passkit2.png %}
[3]: https://dev.bitly.com/v4/#operation/createFullBitlink
[4]: {% image_buster /assets/img/passkit/passkit4.png %}
[5]: {% image_buster /assets/img/passkit/passkit5.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[7]: {{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint
[8]: https://help.passkit.com/en/articles/3742778-hashed-smartpass-links
[9]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks
[10]: https://github.com/PassKit/smart-pass-link-from-csv-generator
[12]: https://docs.passkit.io/protocols/member/
[13]: https://docs.passkit.io/protocols/coupon/
[14]: https://docs.passkit.io/protocols/boarding/
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[16]: https://en.wikipedia.org/wiki/HMAC
