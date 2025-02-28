---
nav_title: Zendesk
article_title: Zendesk
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Zendesk, einer beliebten Support-Suite, die es Ihnen ermöglicht, Braze-Webhooks zu nutzen, die Support-Daten zwischen den beiden Plattformen synchronisieren können."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> Die [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) bietet Unternehmen die Möglichkeit, über den Omnichannel-Support per E-Mail, Webchat, Sprache oder Social Messaging-Apps eine natürliche Konversation mit ihren Kunden zu führen. Zendesk bietet ein rationalisiertes Ticketingsystem, das die Verfolgung und Priorisierung von Interaktionen schätzt und es Unternehmen ermöglicht, eine einheitliche historische Übersicht über ihre Kunden zu erhalten.

Die Server-zu-Server-Integration von Braze und Zendesk ermöglicht es Ihnen, diese zu nutzen: 
- Braze-Webhooks, um die Erstellung von Support-Tickets in Zendesk zu automatisieren, die auf die Einbindung von Nachrichten in die User Journeys in Braze zurückzuführen sind. Nach erfolgreicher Implementierung und Prüfung einer Integration kann Braze beispielsweise ein Support-Ticket von einem Benutzer erstellen, der auf eine In-App-Nachricht "Gefällt Ihnen unsere App?" negativ antwortet.
- Zendesk-Webhooks, um bidirektionale Anwendungsfälle zu unterstützen, z. B. die Aktualisierung des Benutzerprofils in Braze aufgrund einer Aktivität in Zendesk. Wenn zum Beispiel ein Ticket gelöst wurde, protokollieren Sie ein Ereignis im Benutzerprofil in Braze.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Zendesk-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Zendesk-Administratorkonto](https://`<your-zendesk-instance>`.zendesk.com/agent/admin). |
| Zendesk API-Token | Ein [Zendesk-API-Token][2] ist erforderlich, um Anfragen von Braze an den Zendesk-Ticket-Endpunkt zu senden. |
| Gemeinsamer Bezeichner (empfohlen) | Eine [gemeinsame Kennung](#common-identifier) zwischen Braze und Zendesk wird empfohlen. |
| Braze API-Schlüssel | Ein Braze-API-Schlüssel ist erforderlich, um Anfragen von Zendesk an einen Braze-Endpunkt zu senden. Stellen Sie sicher, dass der von Ihnen verwendete API-Schlüssel die richtigen Berechtigungen für den Braze-Endpunkt hat, den Ihr Zendesk-Webhook verwendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Braze in Zendesk

### Schritt 1: Erstellen Sie Ihren Braze Webhook

Um einen Webhook zu erstellen:

- **Kampagnen:** Gehen Sie auf die Seite **Kampagnen** im Braze-Dashboard. Klicken Sie auf **Kampagne erstellen** und wählen Sie **Webhook**.
- **Segeltuch:** Erstellen Sie aus einem neuen oder bestehenden Canvas einen Voll- oder Nachrichtenschritt im Canvas-Builder. Klicken Sie dann auf **Nachrichten** und wählen Sie **Webhook** aus den Nachrichtenoptionen.

Füllen Sie in Ihrem Webhook die folgenden Felder aus:
- **Webhook URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Anfrage Körper**: Rohtext

Weitere Anwendungsfälle können über [Zendesk Support-APIs][4] behandelt werden, wodurch der `/api/v2/` Endpunkt am Ende der Webhook-URL entsprechend geändert würde.

#### Kopfzeile und Methode der Anfrage

Zendesk benötigt einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Ersetzen Sie auf der Registerkarte **Einstellungen** <email_address> durch Ihre Zendesk-Administrator-E-Mail und <api_token> durch Ihr Zendesk-API-Token.

- **HTTP-Methode**: POST
- **Kopfzeilen anfordern**:
  - **Autorisierung**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Inhalt-Typ**: application/json

![][3]{: style="max-width:70%;"}

#### Anfragetext

Definieren Sie die Ticketdetails wie Typ, Betreff und Status in Ihrer Webhook-Nutzlast. Ticketdetails sind auf der Grundlage der [Zendesk Ticket API][6]] erweiterbar und anpassbar. Verwenden Sie das folgende Beispiel, um Ihre Nutzdaten zu strukturieren und die gewünschten Felder einzugeben.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### Schritt 2: Vorschau Ihrer Anfrage

Ihr Rohtext wird automatisch hervorgehoben, wenn es sich um ein anwendbares Braze-Tag handelt.

Zeigen Sie Ihre Anfrage in der **Vorschau** an oder gehen Sie auf die Registerkarte **Test**, wo Sie einen zufälligen Benutzer oder einen bestehenden Benutzer auswählen oder Ihren eigenen Benutzer zum Testen Ihres Webhooks anpassen können.

Prüfen Sie abschließend, ob das Ticket auf der Zendesk-Seite erstellt wurde.

## Gemeinsamer Bezeichner

Wenn Sie einen gemeinsamen Bezeichner für Braze und Zendesk haben, empfiehlt es sich, diesen als `requester_id` zu verwenden. Dies wird dazu beitragen, die beiden Gruppen von Benutzern zu vereinheitlichen. Wenn dies nicht der Fall ist, empfehlen wir, eine Reihe von identifizierenden Attributen wie Name, E-Mail-Adresse, Telefonnummer oder andere zu übergeben.

## Integration von Zendesk in Braze

### Schritt 1: Einen Webhook erstellen

1. Klicken Sie im [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb) in der Seitenleiste auf **Apps und Integrationen** und wählen Sie dann **Webhooks > Webhooks**.<br><br>
2. Klicken Sie auf **Webhook erstellen**.<br><br>
3. Wählen Sie **Auslöser** oder **Automatisierung** und klicken Sie auf **Weiter**.<br>![][9]{: style="max-width:70%;"}<br><br>
4. Geben Sie die folgenden Informationen in Ihrem Webhook an:
- Geben Sie einen Namen und eine Beschreibung für den Webhook ein.
- Geben Sie die URL des Braze-Endpunkts ein, den Ihr Webhook verwenden soll. {% raw %}Unser Beispiel wird `https://{{instance_url}}/users/track` verwenden.{% endraw %}
- Wählen Sie POST als Anfragemethode für den Webhook und stellen Sie das Anfrageformat auf JSON ein.
- Wählen Sie die Bearer-Token-Authentifizierungsmethode für den Webhook und geben Sie Ihren [Braze-API-Schlüssel](https://www.braze.com/docs/api/basics/#creating-and-managing-rest-api-keys) an.
  - Vergewissern Sie sich, dass der von Ihnen verwendete API-Schlüssel die [richtigen Berechtigungen](https://www.braze.com/docs/api/basics/#rest-api-key-permissions) für den Braze-Endpunkt hat, den Ihr Webhook verwendet.<br><br>
5. (Empfohlen) Testen Sie den Webhook, um zu überprüfen, ob er ordnungsgemäß funktioniert.<br><br>
6. Bei Trigger- und Automatisierungs-Webhooks müssen Sie den Webhook mit einem Trigger oder einer Automatisierung verbinden, bevor Sie die Einrichtung abschließen. Im folgenden Schritt sehen Sie ein Beispiel für die Erstellung eines Triggers für den Webhook. Nachdem der Auslöser erstellt wurde, können Sie zu dieser Seite zurückkehren und **Einrichtung beenden** wählen.

### Schritt 2: Erstellen Sie einen Auslöser oder eine Automatisierung

[Folgen Sie den Anweisungen von Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb), wie Sie Ihren Webhook mit einem Auslöser oder einer Automatisierung verbinden.

In unserem Beispiel unten wird ein Trigger verwendet, der den Webhook aufruft, wenn der Status eines Supportfalls auf "Gelöst" oder "Geschlossen" geändert wurde. 

1. Klicken Sie im **Admin Center** in der Seitenleiste auf **Objekte und Regeln** und wählen Sie dann **Geschäftsregeln > Auslöser**.<br><br>
2. Wählen Sie **Auslöser hinzufügen**.<br><br>
3. Benennen Sie Ihren Auslöser und wählen Sie eine Kategorie.<br><br>
4. Wählen Sie **Bedingung hinzufügen**, um festzulegen, welche Bedingungen den Webhook auslösen sollen. Zum Beispiel: "Statuskategorie geändert auf geschlossen" oder "Statuskategorie geändert auf gelöst".![][8]{: style="max-width:70%;"}<br><br>
5. Wählen Sie **Aktion hinzufügen**, wählen Sie **Aktiven Webhook benachrichtigen** und wählen Sie aus der Dropdown-Liste den im vorherigen Schritt erstellten Webhook.<br><br>
6. Definieren Sie den JSON-Körper so, dass er Ihrem Braze-Endpunkt entspricht, und verwenden Sie variable Zendesk-Platzhalter, um die relevanten Felder dynamisch zu füllen.<br>![][10]{: style="max-width:70%;"}<br><br>
7. Wählen Sie **Erstellen**.<br><br>
8. Kehren Sie zu Ihrem Webhook zurück und klicken Sie auf **Einrichtung beenden**.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[2]: https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %}
[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[5]: {% image_buster /assets/img_archive/zendesk_step2.png %}
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket
[7]: {% image_buster /assets/img_archive/zdfinal.gif %}

[8]: {% image_buster /assets/img_archive/zendesk1.png %}
[9]: {% image_buster /assets/img_archive/zendesk2.png %}
[10]: {% image_buster /assets/img_archive/zendesk3.png %}
