---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Passkit. Diese Partnerschaft ermöglicht es Ihnen, Ihre mobile Reichweite durch die Integration von Apple Wallet und Google Pay Pässen in das Kundenerlebnis zu erweitern."
page_type: partner
search_tag: Partner

---

# PassKit

> PassKit ermöglicht es Ihnen, Ihre mobile Reichweite zu erweitern, indem Sie Apple Wallet und Google Pay Pässe in das Kundenerlebnis integrieren. Erstellen, verwalten, verteilen und analysieren Sie ganz einfach die Performance von digitalen Coupons, Kundenkarten, Mitgliedskarten, Tickets und vielem mehr, ohne dass Ihre Kunden eine weitere App benötigen.

_Diese Integration wird von Passkit gepflegt._

## Über die Integration

Die Integration von Braze und PassKit ermöglicht es Ihnen, das Engagement Ihrer Online Kampagnen zu steigern und zu messen, indem Sie angepasste Apple Wallet und Google Pay Pässe sofort zugestellt bekommen. Sie können dann die Nutzung analysieren und Anpassungen in Echtzeit vornehmen, um die Besucherzahlen im Shop zu erhöhen, indem Sie standortbezogene Nachrichten und personalisierte, dynamische Updates für die mobile Brieftasche Ihrer Kund:in triggern. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| PassKit Konto | Sie benötigen ein PassKit Konto und einen PassKit Account Manager:in. |
| `userDefinedID` | Um angepasste Events und angepasste Attribute an Ihre Nutzer:innen zwischen PassKit und Braze angemessen anzupassen, müssen Sie die externe ID von Braze als `userDefinedID` festlegen. Diese `userDefinedID` wird verwendet, wenn Sie API-Aufrufe an die PassKit Endpunkte tätigen. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Um die Erfahrungen Ihrer Kunden mit mobilen Geldbörsen weiter zu verbessern, können Sie von Ihrem PassKit-Dashboard aus Daten über den Braze [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) an Braze weitergeben. 

Beispiele für Daten, die Sie von PassKit weitergeben können, sind:
- **Pass erstellt**: wenn ein Kunde auf einen Pass-Link klickt und zum ersten Mal einen Pass angezeigt bekommt.
- **Pass-Installationen**: wenn der Kunde den Pass in seine App einfügt und speichert.
- **Pass-Updates**: wenn ein Pass aktualisiert wird.
- **Pass löschen**: wenn ein Kund:in den Pass aus seiner App löscht.

Sobald die Daten an Braze übergeben wurden, können Sie Zielgruppen aufbauen, Inhalte über Liquid personalisieren und Kampagnen oder Canvase triggern, nachdem diese Aktionen durchgeführt wurden.

## Verbinden Sie Passkit mit Braze

Um Daten von PassKit zu übergeben, stellen Sie sicher, dass Sie Ihre externe ID von Braze als `externalId` von PassKit eingestellt haben.

1. Klicken Sie in den **Einstellungen** unter **Integrationen** in Ihrem PassKit Pass-Projekt oder -Programm auf **Verbinden** unter dem Tab **Braze**.<br>![Die Braze-Integrationskachel in der PassKit-Plattform.]({% image_buster /assets/img/passkit/passkit5.png %}){: style="max-width:80%"}<br><br>
2. Geben Sie Ihren Braze API-Schlüssel und die URL des Endpunkts ein und geben Sie einen Namen für Ihren Konnektor an.<br><br>
3. Schalten Sie **Enablement** und die Ereignisse um, die Sie in Braze zum Triggern oder Personalisieren Ihrer Nachrichten verwenden möchten.<br>![Die Kachel für die Integration von PassKit Braze wurde erweitert, um den API-Schlüssel, die Endpunkt-URL, den Namen der Integration, die Enablement-Einstellungen, die Mitgliedschaftseinstellungen und die Pass-Einstellungen zu akzeptieren.]({% image_buster /assets/img/passkit/passkit4.png %}){: style="max-width:70%"}

## Pass über einen SmartPass-Link erstellen

Innerhalb von Braze können Sie einen SmartPass-Link einrichten, um eine eindeutige URL für Ihre Kund:innen zu generieren, damit sie ihren Pass entweder auf Android oder iOS installieren können. Dazu müssen Sie eine verschlüsselte SmartPass Daten-Nutzlast definieren, die von einem Braze Content-Block aufgerufen werden kann. Dieser [Content-Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) kann dann für zukünftige Pässe und Coupons wiederverwendet werden. Folgendes wird während Ihrer Integration verwendet:

- **PassKit URL**: Ihre PassKit URL ist eine eindeutige URL für Ihr PassKit Programm.<br>Jedes Programm hat eine eindeutige URL, die Sie auf dem Tab **Distribution** Ihres PassKit Programms oder Projekts finden. (zum Beispiel, https://pub1.pskt.io/c/ww0jir)<br><br>
- **PassKit Geheimnis**: Zusammen mit der URL müssen Sie den PassKit Key für dieses Programm bereithalten.<br>Diese finden Sie auf der gleichen Seite wie Ihre PassKit URL.<br><br>
- **Programm (oder Projekt) ID**: Ihre PassKit Programm ID wird benötigt, um die SmartPass URL zu erstellen. <br>Sie finden sie unter dem Tab **Einstellungen** Ihres Projekts oder Programms.

Weitere Informationen zur Erstellung verschlüsselter SmartPass-Links finden Sie in diesem [PassKit-Artikel](https://help.passkit.com/en/articles/3742778-hashed-smartpass-links).

### Schritt 1: Definieren Sie die Nutzdaten Ihres Passes {#passkit-integrations}

Zunächst müssen Sie die Nutzlast des Coupons oder Mitglieds definieren. 

Es gibt viele verschiedene Komponenten, die Sie in Ihre Nutzlast aufnehmen können, aber hier sind zwei wichtige zu nennen:

| Komponente | Erforderlich | Typ | Beschreibung |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | Erforderlich | String | Die externe ID von Braze ist entscheidend dafür, dass die Callbacks von PassKit zurück zu Braze funktionieren. So ist es zulässig, dass Nutzer:innen von Braze Gutscheine für mehrere Angebote in einer Kampagne haben. Nicht als eindeutig erzwungen. |
| `members.member.externalId` | Optional | String | Als externe ID von Braze eingestellt, können Sie Ihre externe ID zum Update des Mitgliedsausweises verwenden. Wenn Sie dieses Feld setzen, wird der Nutzer:innen innerhalb des Mitgliedschaftsprogramms als eindeutig eingestuft.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Eine vollständige Liste der verfügbaren Felder, ihrer Typen und hilfreichen Beschreibungen finden Sie in der [PassKit GitHub Dokumentation](https://github.com/PassKit/smart-pass-link-from-csv-generator).

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

Erstellen und benennen Sie einen neuen Content-Block, indem Sie im Braze-Dashboard zu **Templates** > **Content-Blöcke** navigieren.

Wählen Sie **Content-Block erstellen**, um loszulegen.

Als nächstes müssen Sie Ihren **Content-Block Liquid-Tag** definieren. Nachdem Sie diesen Content-Block gespeichert haben, können Sie beim Verfassen von Nachrichten auf diesen Liquid-Tag referenzieren. In diesem Beispiel haben wir den Liquid-Tag als {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %} zugewiesen. 

Innerhalb dieses Content-Blocks werden wir die Nutzdaten nicht direkt einbinden, sondern in einer {% raw %}`{{passData}}`{% endraw %} Variablen referenzieren. Der erste Code-Snippet, den Sie zu Ihrem Content-Block hinzufügen müssen, erfasst eine Base64-Kodierung der Variable {% raw %}`{{passData}}`{% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### Schritt 3: Erstellen Sie Ihre Signatur zur Verschlüsselung mit einem SHA1 HMAC-Hash

Als Nächstes erstellen Sie Ihre Signatur unter Verwendung eines [SHA1 HMAC](https://en.wikipedia.org/wiki/HMAC) Hashes der Projekt-URL und der Nutzdaten. 

Der zweite Code Snippet, den Sie zu Ihrem Content-Block hinzufügen müssen, erfasst die URL, die für das Hashing verwendet werden soll.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

Als nächstes müssen Sie mit diesem Hash und Ihrer `Project Secret` eine Signatur erzeugen. Dazu können Sie einen dritten Code Snippet einfügen:
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Schließlich fügen Sie die Signatur mit dem fünften Code Snippet an die vollständige URL an:
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Schritt 4: Drucken Sie Ihre URL

Stellen Sie schließlich sicher, dass Sie Ihre endgültige URL aufrufen, damit Ihre SmartPass-URL in Ihrer Nachricht gedruckt wird.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

Jetzt haben Sie einen Content-Block erstellt, der in etwa so aussieht:

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
Denken Sie daran, Ihren Content-Block zu speichern, bevor Sie die Seite verlassen.
{% endalert %}

### Schritt 5: Praxisbeispiel

Sobald dieser Content-Block erstellt wurde, kann er in Zukunft wieder verwendet werden. 

Sie werden feststellen, dass in dem Beispiel Content-Block zwei Variablen nicht definiert sind.<br> 
{% raw %}`{{passData}}`{% endraw %} - Ihre in [Schritt 1](#passkit-integrations) definierte JSON-Pass-Daten-Nutzlast <br>
{% raw %}`{{projectUrl}}`{% endraw %} - Die URL Ihres Projekts oder Programms, die Sie auf dem Tab Verteilung Ihres Passkit-Projekts finden.

Diese Entscheidung ist zweckmäßig und unterstützt die Wiederverwendbarkeit des Content-Blocks. Da diese Variablen im Content-Block nur referenziert und nicht erstellt werden, können sie sich ändern, ohne den Content-Block neu zu erstellen. 

Vielleicht möchten Sie zum Beispiel das Einführungsangebot ändern, um mehr Anfangspunkte in Ihr Kundenbindungs-Programm aufzunehmen, oder Sie möchten eine zweite Mitgliedskarte oder einen Coupon erstellen. Diese Szenarien würden unterschiedliche Passkit `projectURLs` oder unterschiedliche Pass Payloads erfordern, die Sie pro Kampagne in Braze definieren.  

#### Verfassen des Nachrichtentextes

Sie sollten diese beiden Variablen in Ihrem Nachrichtentext erfassen und dann Ihren Content-Block aufrufen.
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

**Referenzieren Sie den Content-Block, den Sie gerade erstellt haben**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

Ihr Nachrichtentext sollte in etwa so aussehen:
![Ein Bild des Nachrichten-Editors für Content-Blöcke mit den erfassten JSON- und Content-Block-Referenzen.]({% image_buster /assets/img/passkit/passkit1.png %}){: style="max-width:70%"}

Die Ausgabe-URL für das Beispiel lautet:
![Die Ausgabe-URL, die einen langen, zufällig generierten String aus Buchstaben und Zahlen enthält.]({% image_buster /assets/img/passkit/passkit2.png %}){: style="max-width:70%"}

Die Ausgabe-URL wird lang sein. Der Grund dafür ist, dass es alle Passdaten enthält und über eine erstklassige Sicherheit verfügt, um die Integrität der Daten zu gewährleisten und eine Verfälschung durch URL-Änderungen zu verhindern. Wenn Sie diese URL per SMS verbreiten, sollten Sie sie durch einen Linkverkürzungsprozess wie [bit.ly](https://dev.bitly.com/v4/#operation/createFullBitlink) laufen lassen. Dies kann durch einen Connected-Content-Aufruf an einen bit.ly Endpunkt geschehen.

## Update des Passes mit dem PassKit Webhook

Innerhalb von Braze können Sie eine Webhook-Kampagne oder einen Webhook innerhalb eines Canvas einrichten, um einen bestehenden Pass auf der Grundlage des Verhaltens Ihrer Nutzer:innen zu aktualisieren. Unter den folgenden Links finden Sie Informationen über nützliche PassKit Endpunkte. 
- [Projekte der Mitglieder](https://docs.passkit.io/protocols/member/)
- [Coupon-Projekte](https://docs.passkit.io/protocols/coupon/)
- [Flugprojekte](https://docs.passkit.io/protocols/boarding/)

### Parameter der Nutzlast

Bevor Sie beginnen, finden Sie hier die üblichen JSON-Payload-Parameter, die Sie in Ihre Webhooks zum Erstellen und Aktualisieren von PassKit aufnehmen können.

| Daten | Typ | Beschreibung |
| ---- | ---- | ----------- |
| `externalId` | String | Erlaubt das Hinzufügen einer eindeutigen ID zum Passdatensatz, um Kompatibilität mit einem bestehenden System zu gewährleisten, das eindeutige Bezeichner für Kund:in verwendet (z.B. Mitgliedsnummern). Über diesen Endpunkt können Sie Passdaten über `userDefinedId` und `campaignName` anstelle der Pass ID abrufen. Dieser Wert muss innerhalb einer Kampagne eindeutig sein, und nachdem dieser Wert festgelegt wurde, kann er nicht mehr geändert werden.<br><br>Für die Integration von Braze empfehlen wir die Verwendung der externen ID von Braze: {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (Coupon) <br><br> `programId` (Mitgliedschaft) | String | Die ID für die Kampagne oder die Programmvorlage, die Sie in PassKit erstellt haben. Gehen Sie dazu auf den Tab **Einstellungen** in Ihrem PassKit Pass-Projekt. |
| `expiryDate` | IO8601 datetime | Das Ablaufdatum des Passes. Nach Ablauf des Datums wird der Pass automatisch entwertet (siehe `isVoided`). Dieser Wert überschreibt den Wert des Templates und des Enddatums der Kampagne. |
| `status` | String | Der aktuelle Status eines Coupons, wie `REDEEMED` oder `UNREDEEMED`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 1: Erstellen Sie Ihr Braze-to-Braze-Webhook Template

Um eine PassKit-Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvase verwenden können, navigieren Sie zum Bereich **Templates und Medien** im Braze-Dashboard. Wenn Sie eine einmalige PassKit-Webhook-Kampagne erstellen oder eine bestehende Vorlage verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

Sobald Sie das PassKit Webhook Template ausgewählt haben, sollten Sie folgendes sehen:
- **Webhook URL**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

Passkit benötigt zur Autorisierung eine `HTTP Header`, die Ihren Passkit API-Schlüssel in Base 64 verschlüsselt enthält. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber auf dem Tab **Einstellungen** müssen Sie `<PASSKIT_LONG_LIVED_TOKEN>` durch Ihr PassKit Token ersetzen. Um Ihr Token abzurufen, navigieren Sie zu Ihrem PassKit-Projekt/Programm und gehen Sie zu **Einstellungen > Integrationen > Langlebiges Token**.

{% raw %}
- **HTTP-Methode**: PUT
- **Anfrage-Header**:
  - **Autorisierung**: Bearer `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Typ**: application/json
{% endraw %}

#### Anfragetext

Um den Webhook einzurichten, füllen Sie die neuen Ereignisdetails im Körper der Anfrage aus, einschließlich der für Ihren Anwendungsfall erforderlichen Nutzdatenparameter:

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### Schritt 2: Vorschau auf Ihre Anfrage

Ihr Rohtext wird automatisch hervorgehoben, wenn es sich um einen passenden Braze Tag handelt. 

Eine Vorschau Ihrer Anfrage finden Sie im Panel **Vorschau** oder auf dem Tab **Test**, wo Sie einen zufälligen Nutzer, einen bestehenden Nutzer:innen auswählen oder Ihren eigenen anpassen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

## Abrufen von Passdetails über Connected-Content

Sie können nicht nur Pässe erstellen und aktualisieren, sondern auch die Pass-Metadaten Ihrer Nutzer:innen über Braze [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) abrufen, um personalisierte Passdetails in Ihre Messaging-Kampagnen einzubinden.

**PassKit Connected-Content Aufruf**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Liquid Beispiel Antworten**

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


