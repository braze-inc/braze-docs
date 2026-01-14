---
nav_title: Lead Scoring
article_title: Erstellen eines Lead Scoring-Workflows
page_order: 1
page_type: reference
description: "Lernen Sie, wie Sie mit Braze einfaches Lead Scoring, ein externes Lead Scoring und die Übergabe von Leads durchführen können."
---

# Erstellen eines Arbeitsablaufs zur Lead-Bewertung

> Dieser Anwendungsfall zeigt, wie Sie mit Braze die Lead-Bewertungen der Benutzer in Echtzeit aktualisieren und Leads automatisch an Ihre Vertriebsteams weitergeben können.

Die Erstellung eines Lead Scoring-Workflows in Braze besteht aus zwei wichtigen Schritten:

1. Erstellen Sie ein Lead Scoring-Canvas in Braze oder integrieren Sie ein externes Lead Scoring-Tool:
- [Einfaches Lead Scoring](#simple-lead-scoring)
- [Externes Lead Scoring](#external-lead-scoring)

2. Erstellen Sie eine Webhook-Kampagne, um qualifizierte Leads an Ihr Vertriebsteam zu senden:
- [Lead-Übergabe: Marketing Qualified Lead (MQL) an den Vertrieb](#lead-handoff)

## Einfaches Lead Scoring

### Schritt 1: Eine Leinwand erstellen

1. Gehen Sie zu **Messaging** > **Canvas** und wählen Sie **Canvas erstellen**, und geben Sie dann Ihre Canvas-Grundlagen ein.

2. Geben Sie Ihrem Canvas einen aussagekräftigen Namen, z. B. „Lead Scoring-Canvas“, und versehen Sie es zur besseren Auffindbarkeit mit Tags wie „Lead-Management“.<br><br>![Schritt 1 der Erstellung eines Canvas mit dem Namen "Lead Scoring Canvas" und dem Tag "Lead Management".]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Schritt 2: Entry-Kriterien festlegen

1. Fahren Sie mit dem Schritt **Eingabezeitplan** fort und wählen Sie einen **aktionsbasierten** Eingabezeitplan aus. Dadurch werden Nutzer:innen in den Canvas aufgenommen, wenn sie bestimmte Aktionen ausführen.

2. Fügen Sie unter **Aktionsbasierte Optionen** diese beiden Aktionen hinzu:
    - **Ändern Sie den Wert des angepassten Attributs** mit dem Namen Ihres Lead Scoring-Attributs (z .B. `lead score`). Wenn Sie noch kein Lead Scoring-Attribut erstellt haben, folgen Sie den Schritten unter [Benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/). Dadurch werden Nutzer:innen in den Canvas aufgenommen, sobald sich ihr Lead Score ändert.
    - **E-Mail-Adresse hinzufügen**

![Schritt 2 der Erstellung eines Canvas mit dem Zeitplan "Aktionsbasiert" und aktionsbasierten Optionen zur Änderung eines angepassten Attributs "Lead Score" und Hinzufügen einer E-Mail Adresse.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Schritt 3: Zielgruppe identifizieren

#### Schritt 3a: Segmente auswählen

Alle Benutzer kommen für die Lead-Bewertung in Frage. Sie können also unternehmensspezifische Regeln für die Bewertung hinzufügen, indem Sie auswählen, welche [Benutzersegmente]({{site.baseurl}}/user_guide/engagement_tools/segments/) Sie ansprechen möchten und zusätzliche [Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) anwenden. Sie können zum Beispiel Mitarbeiter, Nutzer:innen, die bereits Kunden sind, und ähnliches ausschließen. 

![Schritt 3 der Erstellung eines Canvas mit Optionen zur Auswahl von Segmenten und Filtern zur Eingrenzung der Zielgruppe für den Eingang.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Schritt 3b: Canvas Wiederzulassung festlegen

Ein Benutzer wird diesen Canvas im Laufe seines Lebenszyklus mit Ihnen viele Male durchlaufen. Stellen Sie also sicher, dass er so schnell wieder einsteigen kann, wie er beim letzten Mal ausgestiegen ist. Dies kann durch die Einstellungen für die erneute Qualifizierung erreicht werden. 

Gehen Sie in **Entry Controls** wie folgt vor:
- Wählen Sie **Benutzer dürfen diesen Canvas erneut betreten**.
- Wählen Sie **Bestimmtes Fenster**.
- Legen Sie die erneute Qualifizierung auf „0“ **Sekunden** fest.

!["Eingangskontrollen" mit Auswahlmöglichkeiten für "Nutzern:innen erlauben, diesen Canvas erneut zu betreten" in einem "spezifizierten Fenster" von 0 Sekunden.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Schritt 3c: Sendeeinstellungen aktualisieren

Angesichts der operativen Natur dieses Canvas und der Tatsache, dass keine Nachrichten an diese Benutzer gesendet werden, müssen Sie sich nicht an den Abonnementstatus halten.

Wählen Sie unter **Abonnementeinstellungen** für **An diese Benutzer senden:** **alle Benutzer, einschließlich nicht abonnierter Benutzer**. 

![Schritt 4 der Erstellung eines Canvas zur Einstellung der Optionen für den Versand von Nachrichten.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Schritt 4: Canvas erstellen

#### Schritt 4a: Einen Aktionspfad hinzufügen

Klicken Sie unter Ihrer Variante auf das Plus-Symbol und wählen Sie dann **Aktionspfade**.

![Canvas mit "Aktions-Pfade", die im Menü angezeigt werden, das durch das Plus-Symbol geöffnet wird.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Schritt 4b: Aktionsgruppen erstellen

Jede Aktionsgruppe repräsentiert alle Aktionen, die zu derselben Punkte-Erhöhung oder -Verringerung führen. Sie können bis zu acht Aktionsgruppen einrichten. In diesem Szenario werden wir vier Gruppen einrichten.

Fügen Sie die folgenden Gruppen zu Ihrem Aktionspfad hinzu:

- **Gruppe 1:** Alle Ereignisse, die für eine 1-Punkte-Erhöhung zählen.
- **Gruppe 2:** Alle Ereignisse, die für ein 5-Punkte-Inkrement zählen.
- **Gruppe 3:** Alle Ereignisse, die für einer 1-Punkte-Verringerung zählen.
- **Alle anderen:** Aktions-Pfade ermöglichen es Ihnen, das Fenster zu definieren, in dem gewartet wird, ob ein Nutzer:innen eine Aktion ausführt, bevor er in eine Gruppe "Alle anderen" eingeordnet wird. Für das Lead Scoring ist dies eine Opportunity, um die Punktzahl für „Inaktivität“ zu verringern.

![Aktions-Pfad mit Aktionsgruppen für das Hinzufügen von einem Punkt, fünf Punkten und zehn Punkten; das Abziehen von einem Punkt und zehn Punkten; und "Alle anderen".]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Schritt 4c: Jede Gruppe so konfigurieren, dass sie die relevanten Event enthält

Wählen Sie in jeder Aktionsgruppe die Option **Auslöser auswählen** und wählen Sie das Ereignis, das die Anzahl der Punkte für die jeweilige Aktionsgruppe hinzufügen wird. Fügen Sie weitere Trigger hinzu, um alle Events zu berücksichtigen, die den Lead Score um eins erhöhen. Ein Nutzer:in könnte beispielsweise seinen Punktestand um eins erhöhen, wenn er eine Sitzung in einer beliebigen App beginnt oder ein angepasstes Event durchführt (z.B. die Registrierung oder Teilnahme an einem Webinar). 

![Aktionsgruppe zum Hinzufügen eines Punktes mit den Triggern "Sitzung in einer beliebigen App starten" und "Angepasstes Event durchführen".]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Schritt 4d: Schritte zur Nutzeraktualisierung hinzufügen

Fügen Sie jedem Canvas-Pfad, der unterhalb Ihres Aktionspfades erstellt wurde, einen Schritt zur Nutzeraktualisierung hinzu. 

![Canvas, das den Aktions-Pfad mit verzweigten Nutzer:innen-Update-Pfaden für jede Aktionsgruppe anzeigt.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start=”2”}
Führen Sie auf der Registerkarte **Verfassen der** einzelnen Schritte der Benutzeraktualisierung die folgenden Schritte für die jeweiligen Felder aus:

| Feld | Aktion |
| --- | --- |
| **Attributname** | Wählen Sie das Attribut aus, das Sie in Schritt 2 ausgewählt haben (`lead score`).|
| **Aktion** | Ändern Sie die Aktion in **Erhöhen um**, wenn der Pfad die Punktzahl erhöht oder **Verringern um**, wenn der Pfad die Punktzahl verringert. |
| **Erhöhen um** oder **Verringern um** | Geben Sie die Anzahl der Punkte ein, die von der Hauptbewertung erhöht oder verringert werden sollen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 5: Starten Sie Ihr Canvas

Das war's! Ihr Lead Scoring Canvas ist bereit für den Start.

## Externe Lead-Bewertung

Ob Sie einen unserer [Technologiepartner]({{site.baseurl}}/partners/home/), Ihr eigenes internes Lead Scoring-Modell, maschinelles Lernen oder ein anderes Lead Scoring-Tool verwenden, wir haben mehrere Optionen für Sie.

### Externe Partner

Unter [Technologiepartner]({{site.baseurl}}/partners/home) erfahren Sie mehr über unsere B2B-Partner, die Lead-Scoring-Funktionen anbieten. Sie sehen Ihr Tool dort nicht? Sie können die Integration durch den Aufruf unseres [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users)-API-Endpunkts durchführen. 

### Interne Datenmodelle für die Lead-Bewertung

Sie können Braze auf verschiedene Weise mit Ihren internen Datenmodellen, einschließlich Lead Scoring-Modellen, integrieren. Im Folgenden finden Sie einige Beispiele dafür, wie unsere Kunden Braze integriert haben.

#### Integriertes Data Warehouse in der Cloud

{% tabs %}
{% tab Braze as a data source %}

Als Ihr Marketing-Tool enthält Braze äußerst relevante Daten, die das interne Lead Score-Modell Ihres Teams ergänzen können. 

So können beispielsweise Daten über das Engagement eines Leads (z. B. Öffnen und Anklicken von E-Mails, Engagement auf der Landing Page usw.) den Grad seines Engagements bestimmen. Mit den Lösungen von Braze für den Daten-Streaming-Export können Sie diese Daten an Ihr Data Warehouse in der Cloud zurückgeben und sie als Input für Ihre Lead-Scoring-Modelle zur Verfügung stellen:

- [Braze-Currents]({{site.baseurl}}/user_guide/data/braze_currents/)
- [Sicherer Datenaustausch mit Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze as a destination %}

Nachdem Ihre internen Teams Ihr Lead-Scoring-Modell erstellt und ausgeführt haben, können Sie diese Daten wieder in Braze einspeisen, so dass Sie die Leads besser segmentieren und für relevante Botschaften ansprechen können. Sie können dies mit [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) tun. 

Mit Cloud Data Ingestion erstellen Ihre internen Teams eine neue Tabelle oder Ansicht mit Ihren Benutzerkennungen, den neuesten Lead-Bewertungen und den Zeitstempeln, wann die Bewertungen aktualisiert wurden. Braze übernimmt die Tabelle oder die Ansicht und fügt die Lead Scores zu den Benutzerprofilen hinzu.

{% endtab %}
{% endtabs %}

## Lead-Übergabe: Marketing Qualified Lead (MQL) an den Vertrieb{#lead-handoff}

Wir empfehlen Ihnen, allen Nutzer:innen in Braze einen entsprechenden Kontakt zuzuordnen, um die Übergabe zu erleichtern. Diese Leads würden in die Warteschlange Ihres Vertriebsteams gelangen, wenn ihr Lead-Status in ein MQL-Stadium übergeht. Zu diesem Zeitpunkt würde Salesforce einen Lead-Routing- oder Zuweisungsworkflow starten. 

Um den Lead-Datensatz in Salesforce mit dem Lead-Status von Braze zu aktualisieren, empfehlen wir die Verwendung eines getriggerten Webhook-Templates.

### Schritt 1: Erstellen Sie eine Webhook-Kampagne

### Schritt 2: Konfigurieren Sie Ihren Webhook

#### Schritt 2a: Webhook zusammenstellen

1. Geben Sie Ihrer Webhook-Kampagne einen Namen, z. B. „Salesforce > Lead auf MQL aktualisieren“.

2. Geben Sie Ihre Webhook-URL im Format von {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} ein. Die Braze-Benutzer-ID von {% raw %}`{{$user_id}}}`{% endraw %} sollte mit Ihrer Salesforce-Kontakt-ID übereinstimmen. Wenn nicht, verwenden Sie einen Alias anstelle von {% raw %}`{{$user_id}}}`{% endraw %}.

3. Aktualisieren Sie die **HTTP-Methode** auf **PATCH**.

4. Konfigurieren Sie Ihren Payload so, dass der Lead-Datensatz in Salesforce nur dann aktualisiert wird, wenn der Lead-Score dieses Leads Ihren vordefinierten Schwellenwert überschreitet. Sehen Sie sich den Anfragetext unten an, wenn Sie einen Lead Score von mehr als 100 haben.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5\. Fügen Sie die folgenden Kopfzeilen ein:

| Header | Content |
| --- | --- |
| Autorisierung | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Um ein Token abzurufen, [konfigurieren Sie eine verbundene App](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) für den OAuth 2.0 Client-Zugangsdaten-Flow und verwenden Sie dann Connected-Content, um den Bearer aus Salesforce abzurufen: <br><br>{% raw %}<code>{% connected_content https://[Instanz].my.salesforce.com/services/oauth2/token <br>:methode post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Träger {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content_Type | application/json |
{: .reset-td-br-1 reset-td-br-2}

![Webhook, der aus einer Salesforce Webhook-URL, der HTTP-Methode PATCH, einem Rohtext-Anfragetext und Anfrage-Headern besteht.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Schritt 2b: Zeitplan für das Senden von Webhooks

Die Kampagne sollte immer dann triggern, wenn sich der Lead Score des Nutzers:innen ändert. Diese Kampagne wird für jeden Benutzer ausgelöst, dessen Punktestand sich ändert, aber sie betrifft nur Benutzer, die derzeit kein MQL sind und den von Ihnen im vorherigen Schritt festgelegten Schwellenwert überschritten haben.

Im Schritt **Lieferung planen** wählen Sie Folgendes aus:
- Ein **handlungsorientierter** Lieferungstyp
- Eine Auslöseraktion von **Benutzerdefinierten Attributwert ändern** mit dem Namen Ihres Lead Scoring-Attributs und einer Aktion mit einem **beliebigen neuen Wert**

#### Schritt 2c: Zielgruppe identifizieren

Fügen Sie im Schritt **Zielgruppen** einen Filter ein, der Nutzer:innen ausschließt, deren Lead-Status bereits auf MQL oder darüber hinaus ist, z. B. „`lead_status` `is none of` `MQL`“.

![Webhook Targeting Optionen mit dem Filter von “lead_status” ist keine von "MQL".]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Schritt 3: Kampagne starten

Wählen Sie **Starten** und beobachten Sie, wie sich Ihr Lead-Status in Salesforce ändert, wenn Ihre Kunden den Schwellenwert für MQL-Leads überschreiten.

