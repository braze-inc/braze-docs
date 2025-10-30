---
nav_title: Salesforce Sales Cloud
article_title: Leads mit Salesforce Sales Cloud verwalten
page_order: 3
page_type: reference
description: "Erfahren Sie, wie Sie mit Braze-Webhooks über den Endpunkt Salesforce sobjects/Lead Leads in Salesforce Sales Cloud erstellen und aktualisieren können."
---

# Leads mit Salesforce Sales Cloud verwalten

> [Salesforce](https://www.salesforce.com/) ist eine der weltweit führenden cloudbasierten Customer Relationship Management (CRM)-Plattformen, die Unternehmen bei der Verwaltung ihres gesamten Vertriebsprozesses unterstützt, einschließlich Lead-Generierung, Opportunity Tracking und Account Management.<br><br>Auf dieser Seite wird gezeigt, wie Sie mit Braze-Webhooks über eine von der Community vorgeschlagene Integration Leads in Salesforce Sales Cloud erstellen und aktualisieren können.

{% alert important %}
Dies ist eine von der Community eingereichte Integration, die nicht direkt von Braze unterstützt wird. Nur offizielle, von Braze bereitgestellte Webhook-Templates werden von Braze unterstützt.
{% endalert %}

## Funktionsweise

Die Integration von Braze und Salesforce Sales Cloud verwendet Braze-Webhooks zum Erstellen und Aktualisieren von Leads in Salesforce Sales Cloud über den Endpunkt Salesforce [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html).

Braze bietet derzeit zwei Integrationen in Salesforce Sales Cloud für die folgenden Anwendungsfälle an:
1. [Erstellen eines Leads in Salesforce Sales Cloud](#creating-lead)
2. [Update eines Leads in Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Diese Integration dient ausschließlich dazu, Salesforce von Braze aus zu aktualisieren, und zwar als Teil Ihrer Bemühungen um die Akquisition und Pflege von Leads. Um Daten von Salesforce zurück nach Braze zu synchronisieren, sehen Sie sich das [B2B-Datenmodell]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/) an oder wenden Sie sich an einen unserer [Technologiepartner]({{site.baseurl}}/partners/home/).
{% endalert %}

## Voraussetzungen

Für diese Integration müssen Sie eine verbundene App in Salesforce Sales Cloud erstellen, indem Sie die Schritte in der Salesforce Dokumentation befolgen: [Konfigurieren Sie eine Connected App für den OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

Wenn Sie die erforderlichen OAuth-Einstellungen für die verbundene App konfigurieren, behalten Sie alle oAuth-Einstellungen mit ihren Standardwerten und -auswahlen bei, mit Ausnahme der folgenden:
1. Wählen Sie **Enablement für den Gerätefluss** aus. Sie können die **Callback URL** leer lassen, da sie standardmäßig als Platzhalter verwendet wird.
2. Fügen Sie für ausgewählte **OAuth-Bereiche** **Nutzerdaten über APIs (api) verwalten** hinzu.
3. Wählen Sie **Enablement Client Zugangsdaten Fluss**.

## Erstellen eines Leads in Salesforce Sales Cloud {#creating-lead}

Als Customer-Engagement-Plattform kann Braze neue Leads auf der Grundlage von Nutzer:in generieren, z.B. durch Ausfüllen eines Formulars auf einer Landing Page. Wenn dies geschieht, können Sie einen Braze-to-Braze-Webhook für Sales Cloud verwenden, um einen entsprechenden Lead in Salesforce zu erstellen.

### Schritt 1: Sammeln Sie Ihre `client_id` und `client_secret`

1. Gehen Sie in Salesforce zu **Plattform-Tools** > **Apps** > **App Manager**:in.
2. Suchen Sie Ihre neu erstellte Braze App und wählen Sie **Ansicht**.
3. Wählen Sie unter **Verbraucher:in Schlüssel und Geheimnis** die Option **Verbraucherdetails verwalten**.
4. Auf der daraufhin angezeigten Seite notieren Sie sich Ihren **Verbraucher:in-Schlüssel** und Ihr **Verbraucher-Geheimnis**. Der **Verbraucher:in-Schlüssel** ist Ihr `client_id`, und das **Verbraucher-Geheimnis** ist Ihr `client_secret`.

### Schritt 2: Richten Sie Ihr Webhook Template ein

Verwenden Sie Templates, um diesen Webhook schnell auf der gesamten Braze-Plattform wiederzuverwenden. 

1. Gehen Sie in Braze zu **Vorlagen**, wählen Sie **Webhook-Vorlagen** und dann **\+ Webhook-Vorlage erstellen**.
2. Geben Sie einen Namen für das Template an, z. B. "Salesforce Sales Cloud > Lead erstellen".
3. Auf dem Tab **Verfassen** geben Sie die folgenden Details ein:

#### Webhook zusammenstellen 

| Feld | Details |
| --- | --- |
| Webhook-URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| HTTP-Methode | `POST` |
| Anfragetext | JSON-Schlüssel-Wert-Paare |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Körper Eigenschaft Schlüsselwerte

Wählen Sie **\+ Neue Body-Eigenschaft hinzufügen** für jedes der Schlüssel-Wert-Paare, die Sie von Braze auf Salesforce übertragen möchten. Sie können jedes beliebige Feld abbilden, so dass die folgende Tabelle nur ein Beispiel ist.

| Schlüssel | Wert |
| --- | --- |
| Vorname | {% raw %}`{{${first_name}}}`{% endraw %} |
| Nachname | {% raw %}`{{${last_name}}}`{% endraw %} |
| E-Mail | {% raw %}`{{${email_address}}}`{% endraw %} |
| Unternehmen | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Anfrage-Header

Wählen Sie **\+ Neuen Header hinzufügen** für jeden der folgenden Anfrage-Header.

| Schlüssel | Wert |
| --- | --- |
| Autorisierung | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Typ | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4" }
4\. Wählen Sie **Template speichern**.

\![Ein ausgefülltes Webhook Template, um einen Lead zu erstellen.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}
 
## Update eines Leads in Salesforce Sales Cloud {#updating-lead}

Um einen Braze Salesforce Sales Cloud Webhook einzurichten, der Leads in Salesforce aktualisiert, benötigen Sie einen gemeinsamen Bezeichner zwischen Salesforce Sales Cloud und Braze. Im folgenden Beispiel wird die Salesforce `lead_id` als Braze `external_id` verwendet, aber Sie können dies auch durch die Verwendung eines `user_alias` erreichen. Einzelheiten hierzu finden Sie unter [B2B Daten]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models)

Dieses Beispiel zeigt speziell, wie Sie die Lead-Stufe eines Leads auf "MQL" (Marketing Qualified Lead) aktualisieren, nachdem ein Lead einen bestimmten Schwellenwert überschritten hat. Dies ist ein zentraler Bestandteil unseres [B2B-Lead-Scoring-Workflow-Anwendungsfalls]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/).

### Schritt 1: Sammeln Sie Ihre `client_id` und `client_secret`

1. Gehen Sie in Salesforce zu **Plattform-Tools** > **Apps** > **App Manager**:in.
2. Suchen Sie Ihre neu erstellte Braze App und wählen Sie **Ansicht**.
3. Wählen Sie unter **Verbraucher:in Schlüssel und Geheimnis** die Option **Verbraucherdetails verwalten**.
4. Auf der daraufhin angezeigten Seite notieren Sie sich Ihren **Verbraucher:in-Schlüssel** und Ihr **Verbraucher-Geheimnis**.
    - Der **Verbraucher:in-Schlüssel** ist Ihr `client_id`, und das **Verbraucher-Geheimnis** ist Ihr `client_secret`.

### Schritt 2: Richten Sie Ihr Webhook Template ein

1. Gehen Sie in Braze zu **Vorlagen**, wählen Sie **Webhook-Vorlagen** und dann **\+ Webhook-Vorlage erstellen**.
2. Geben Sie einen Namen für das Template an, z. B. "Salesforce Sales Cloud > Update Lead to MQL".
3. Auf dem Tab **Verfassen** geben Sie die folgenden Details ein:

#### Webhook zusammenstellen 

| Feld | Details |
| --- | --- |
|Webhook-URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| HTTP-Methode | `PATCH` |
| Anfragetext | JSON-Schlüssel-Wert-Paare |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Körper Eigenschaft Schlüsselwerte

Wählen Sie **\+ Neue Body-Eigenschaft hinzufügen** für das folgende Schlüssel-Wert-Paar. Beachten Sie, dass `Lead_Stage__c` ein Beispielname ist. Das angepasste Feld, das Sie für das Tracking von MQLs in Salesforce verwenden, kann einen anderen Namen haben, also stellen Sie sicher, dass sie übereinstimmen.

| Schlüssel | Wert |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Anfrage-Header

Wählen Sie **\+ Neuen Header hinzufügen** für jeden der folgenden Anfrage-Header.

| Schlüssel | Wert |
| --- | --- |
| Autorisierung | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Typ | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4"}
4\. Wählen Sie **Template speichern**.

\![Eine ausgefüllte Webhook-Vorlage zum Update eines Leads.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Verwendung dieser Webhooks in einem operativen Arbeitsablauf

Sie können Ihre Templates schnell zu Ihren operativen Arbeitsabläufen in Braze hinzufügen, z.B:

1. Teil einer [Kampagne für neue Nutzer:innen](#new-lead), die einen Lead in Salesforce erstellt
2. Teil eines [Lead Scoring Canvas](#lead-scoring), der Nutzer:innen, die Ihren MQL-Schwellenwert überschritten haben, auf "MQL" aktualisiert und die Salesforce Sales Cloud mit denselben Informationen aktualisiert

### Neue Kampagne {#new-lead}

Um einen Lead in Salesforce zu erstellen, wenn ein Nutzer:innen seine E-Mail Adresse angibt, können Sie eine Kampagne erstellen, die das Template "Update Lead" Webhook verwendet und triggert, wenn ein Nutzer:innen seine E-Mail Adresse hinzufügt (z.B. ein Webformular ausfüllt).

\![Schritt 2 der Erstellung einer Kampagne, die aktionsbasiert ist und die Aktion triggern soll: "Eine E-Mail Adresse hinzufügen".]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Lead Scoring Canvas für das Überschreiten der Marketing Qualified Lead (MQL)-Schwelle {#lead-scoring}

Dieser Webhook wird im Anwendungsfall [Lead Scoring]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/#lead-handoff) behandelt, aber Sie können auch nach MQLs suchen und Salesforce direkt innerhalb des Lead Scoring Canvas aktualisieren (im Gegensatz zur Erstellung einer separaten Webhook-Kampagne): 

Fügen Sie Ihrer Nutzer:innen-Aktualisierung einen weiteren Schritt hinzu, um zu prüfen, ob ein Nutzer:in die von Ihnen definierte MQL-Schwelle gelangt ist. Wenn sie sich gekreuzt haben, aktualisieren Sie den Status des Nutzers:innen auf "MQL" und aktualisieren dann Salesforce mit demselben "MQL"-Status, indem Sie dieses Webhook Template verwenden. Salesforce kümmert sich um den Rest, indem es diesen Lead anhand der von Ihnen definierten Lead-Routing-Regeln an die entsprechenden Teams weiterleitet.  

#### Hinzufügen eines Canvas-Schrittes zur Überprüfung von Nutzer:innen, die den MQL-Schwellenwert überschritten haben 

1. Fügen Sie einen **Zielgruppen-Pfad-Schritt** mit zwei Gruppen hinzu: "MQL-Schwelle" und "Alle anderen".
2. Suchen Sie in der Gruppe "MQL-Schwelle" nach Nutzern:innen, die derzeit nicht den Status "MQL" haben (z.B. `lead_stage` ist gleich "Lead"), aber einen Lead-Score haben, der über der von Ihnen definierten Schwelle liegt (z.B. `lead_score` größer als 50). Wenn ja, gehen sie zum nächsten Schritt über, wenn nicht, verlassen sie die Seite.

\![Die "MQL Threshold" Zielgruppe-Pfad-Gruppe mit Filtern für eine `lead_stage` gleich "Lead" und eine `lead_score` größer als "50".]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3\. Fügen Sie einen Schritt **zum Update des Nutzers** hinzu, der den Wert des Attributs `lead_stage` des Nutzers:innen auf "MQL" aktualisiert.

\![Der Benutzer:in-Schritt "Update auf MQL", der das Attribut `lead_stage` auf den Wert "MQL" aktualisiert.]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4\. Fügen Sie einen Webhook-Schritt hinzu, der Salesforce mit der neuen MQL-Stufe aktualisiert.

\![Der Webhook-Schritt "Update Salesforce" mit abgeschlossenen Details.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

Jetzt aktualisiert Ihr Canvas Fluss Nutzer:innen, die Ihren MQL-Schwellenwert überschritten haben!

\![Ein Canvas-Schritt zum Update von Nutzern:innen, der prüft, ob ein Nutzer:innen den MQL-Schwellenwert überschreitet, und, falls der Nutzer:innen den Schwellenwert überschreitet, Salesforce aktualisiert.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Fehlersuche

Diese Workflows verfügen nur über begrenzte Debugging-Möglichkeiten in Salesforce. Wir empfehlen daher, das Braze [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#message-activity-log) zu Rate zu ziehen, um herauszufinden, warum ein Webhook fehlgeschlagen ist und ob ein Fehler aufgetreten ist.

Ein Fehler, der durch eine ungültige URL für den Abruf des oAuth-Tokens verursacht wird, wird beispielsweise als `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL` angezeigt.

\![Ein Fehler-Antwortkörper, der besagt, dass die URL keine gültige URL ist.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})

