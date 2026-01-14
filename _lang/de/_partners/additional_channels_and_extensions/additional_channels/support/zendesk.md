---
nav_title: Zendesk
article_title: Zendesk
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Zendesk, einer beliebten Suite, die es Ihnen erlaubt, Braze-Webhooks zu verwenden, mit denen Support-Daten zwischen den beiden Plattformen synchronisiert werden können."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> Die [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) bietet Unternehmen die Möglichkeit, über Omnichannel-Support per E-Mail, Webchat, Voice oder Social Messaging-Apps eine natürliche Konversation mit ihren Kund:in zu führen. Zendesk bietet ein rationalisiertes Ticketing-System, das Wert auf Tracking und Priorisierung von Interaktionen legt und es Unternehmen erlaubt, eine einheitliche historische Übersicht über ihre Kund:in zu erhalten.

Die Server-zu-Server Integration von Braze und Zendesk erlaubt Ihnen die Nutzung: 
- Braze-Webhooks zur Automatisierung der Erstellung von Support-Tickets in Zendesk aufgrund von Nachrichten-Engagement in Nutzer:in. Nachdem Sie eine Integration erfolgreich implementiert und getestet haben, kann Braze beispielsweise ein Support-Ticket von einem Nutzer erstellen, der eine In-App-Nachricht mit der Frage "Gefällt Ihnen unsere App?" negativ beantwortet hat, so dass Ihr Support-Team mit dem Kunden nachfassen kann.
- Zendesk-Webhooks zur Unterstützung bidirektionaler Anwendungsfälle wie dem Update des Nutzerprofils in Braze aufgrund einer Aktivität in Zendesk. Wenn zum Beispiel ein Ticket gelöst wurde, protokollieren Sie ein Ereignis im Nutzerprofil in Braze.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Zendesk-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Zendesk-Administratorkonto](https://`<your-zendesk-instance>`.zendesk.com/agent/admin). |
| Zendesk API-Token | Ein Zendesk [API-Token](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-) ist erforderlich, um Anfragen von Braze an den Zendesk-Ticket-Endpunkt zu senden. |
| Gemeinsamer Bezeichner (empfohlen) | Ein [gemeinsamer Bezeichner](#common-identifier) zwischen Braze und Zendesk wird empfohlen. |
| Braze API-Schlüssel | Ein Braze API-Schlüssel ist erforderlich, um Anfragen von Zendesk an einen Braze Endpunkt zu senden. Vergewissern Sie sich, dass der von Ihnen verwendete API-Schlüssel die richtigen Berechtigungen für den Braze-Endpunkt hat, den Ihr Zendesk-Webhook verwendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze to Zendesk Integration

### Schritt 1: Erstellen Sie Ihren Braze-Webhook

So erstellen Sie einen Webhook:

- **Kampagnen:** Gehen Sie im Braze-Dashboard auf die Seite **Kampagnen**. Klicken Sie auf **Kampagne erstellen** und wählen Sie **Webhook**.
- **Canvas:** Erstellen Sie aus einem neuen oder bestehenden Canvas einen Voll- oder Nachrichten-Schritt im Canvas-Builder. Klicken Sie dann auf **Messaging** und wählen Sie **Webhook** aus den Nachrichtenoptionen aus.

Füllen Sie in Ihrem Webhook die folgenden Felder aus:
- **Webhook URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Anfrage Körper**: Rohtext

Weitere Anwendungsfälle können über [Zendesk support APIs](https://developer.zendesk.com/rest_api/docs/support/introduction) gehandhabt werden, wodurch der `/api/v2/` Endpunkt am Ende der Webhook-URL entsprechend geändert würde.

#### Anfrage-Header und Methode

Zendesk benötigt einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Ersetzen Sie auf dem Tab **Einstellungen** die <email_address> durch Ihre Zendesk Admin E-Mail und <api_token> durch Ihr Zendesk API Token.

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Autorisierung**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Typ**: application/json

![]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Anfragetext

Definieren Sie die Ticketdetails wie Typ, Betreff und Status in Ihrem Webhook-Payload. Die Ticketdetails sind erweiterbar und werden auf der Grundlage der [Zendesk Ticket API](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket) angepasst. Verwenden Sie das folgende Beispiel, um Ihre Nutzdaten zu strukturieren und die gewünschten Felder einzugeben.

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

### Schritt 2: Vorschau auf Ihre Anfrage

Ihr Rohtext wird automatisch hervorgehoben, wenn es sich um einen passenden Braze Tag handelt.

Eine Vorschau Ihrer Anfrage finden Sie im Panel **Vorschau** oder auf dem Tab **Test**, wo Sie einen zufälligen oder einen bereits vorhandenen Nutzer:in auswählen oder Ihren eigenen anpassen können, um Ihren Webhook zu testen.

Prüfen Sie schließlich, ob das Ticket auf der Zendesk-Seite erstellt wurde.

## Gemeinsamer Bezeichner

Wenn Sie einen gemeinsamen Bezeichner für Braze und Zendesk haben, empfiehlt es sich, diesen als `requester_id` zu verwenden. Dies wird dazu beitragen, die beiden Gruppen von Nutzer:innen zu vereinheitlichen. Sollte dies nicht der Fall sein, empfehlen wir, eine Reihe von identifizierenden Attributen wie Name, E-Mail Adresse, Telefonnummer oder andere zu übergeben.

## Zendesk zu Braze Integration

### Schritt 1: Einen Webhook erstellen

1. Klicken Sie im [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb) in der Seitenleiste auf **Apps und Integrationen** und wählen Sie dann **Webhooks > Webhooks.**<br><br>
2. Klicken Sie auf **Webhook erstellen**.<br><br>
3. Wählen Sie **Auslöser** oder **Automatisierung** und klicken Sie auf **Weiter**.<br>![]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Geben Sie in Ihrem Webhook die folgenden Informationen an:
- Geben Sie einen Namen und eine Beschreibung für den Webhook ein.
- Geben Sie die URL des Braze-Endpunkts ein, den Ihr Webhook verwenden soll. {% raw %}Unser Beispiel wird `https://{{instance_url}}/users/track` verwenden.{% endraw %}
- Wählen Sie POST als Methode für die Anfrage des Webhooks aus und setzen Sie das Format der Anfrage auf JSON.
- Wählen Sie die Token-Authentifizierungsmethode für den Webhook aus und geben Sie Ihren [Braze-API-Schlüssel]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys) an.
  - Vergewissern Sie sich, dass der API-Schlüssel, den Sie verwenden, die [richtigen Berechtigungen]({{site.baseurl}}/api/basics/#rest-api-key-permissions) für den Braze-Endpunkt hat, den Ihr Webhook verwendet.<br><br>
5. (Empfohlen) Testen Sie den Webhook, um zu überprüfen, ob er ordnungsgemäß funktioniert.<br><br>
6. Bei Webhooks für Trigger und Automatisierung müssen Sie den Webhook mit einem Trigger oder einer Automatisierung verbinden, bevor Sie die Einrichtung abschließen. Im folgenden Schritt finden Sie ein Beispiel für die Erstellung eines Triggers für den Webhook. Nachdem der Trigger erstellt wurde, können Sie zu dieser Seite zurückkehren und **Einrichtung beenden** auswählen.

### Schritt 2: Erstellen Sie einen Trigger oder eine Automatisierung

[Folgen Sie den Anweisungen von Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb), wie Sie Ihren Webhook mit einem Trigger oder einer Automatisierung verbinden.

In unserem Beispiel unten wird ein Trigger verwendet, um den Webhook aufzurufen, wenn der Status eines Supportfalls auf "Gelöst" oder "Geschlossen" geändert wurde. 

1. Klicken Sie im **Admin Center** in der Seitenleiste auf **Objekte und Regeln** und wählen Sie dann **Geschäftsregeln > Trigger.**<br><br>
2. Wählen Sie **Auslöser hinzufügen**.<br><br>
3. Benennen Sie Ihren Auslöser und wählen Sie eine Kategorie aus.<br><br>
4. Wählen Sie **Bedingung hinzufügen**, um festzulegen, welche Bedingungen den Webhook auslösen sollen. Zum Beispiel: "Statuskategorie geändert auf geschlossen" oder "Statuskategorie geändert auf gelöst".![]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. Wählen Sie **Aktion hinzufügen**, wählen Sie **Aktiven Webhook benachrichtigen** und wählen Sie aus der Dropdown-Liste den Webhook aus, den Sie im vorherigen Schritt erstellt haben.<br><br>
6. Definieren Sie den JSON-Body so, dass er Ihrem Braze Endpunkt entspricht, und verwenden Sie variable Platzhalter von Zendesk, um die relevanten Felder dynamisch zu füllen.<br>![]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. Wählen Sie **Erstellen**.<br><br>
8. Kehren Sie zu Ihrem Webhook zurück und klicken Sie auf **Einrichtung beenden**.


