---
nav_title: Die ganze Geschichte
article_title: Die ganze Geschichte
description: "In diesem referenzierten Artikel wird die Partnerschaft zwischen Braze und Fullstory beschrieben."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Die ganze Geschichte

Die Plattform für Verhaltensdaten von Fullstory hilft Technologieführern, bessere und fundiertere Entscheidungen zu treffen. Durch das Einspeisen digitaler Verhaltensdaten in ihren Analytics Stack erschließt die patentierte Technologie von Fullstory die Leistungsfähigkeit hochwertiger Verhaltensdaten im großen Maßstab und verwandelt jeden digitalen Besuch in umsetzbare Insights. 

*Diese Integration wird von Fullstory gepflegt*

## Über diese Integration
Sie können die Insights von Fullstory in Braze nutzen, um Moment-zu-Moment-Bilder der Website oder App-Erlebnisse eines Nutzers zu erstellen, um kontextuelles Messaging zu liefern. Die Session Summary API von Fullstory ermöglicht die Erfassung detaillierter Metadaten über das Surfverhalten eines Nutzers zur Verwendung im Braze Messaging, was besonders leistungsstark ist, wenn es in einem mehrstufigen Messaging-Prozess wie einem Canvas genutzt wird. 

Der Realtime-Wert der Session Summary-Daten von Fullstory lässt sich am besten durch Connected-Content nutzen. Durch die Verwendung von Connected-Content in einem Canvas-Kontext-Schritt können Sie die Daten von Fullstory während der gesamten Canvas-Reise eines Nutzers zur Verwendung in allen nachfolgenden Canvas-Schritten speichern. Dadurch wird auch vermieden, dass diese Daten über angepasste Events oder Attribute in ein Nutzerprofil von Braze geschrieben werden müssen. 

Im folgenden Beispiel werden Canvas-Kontextdaten in einem KI Canvas-Schritt genutzt, um die optimale Nachricht zu generieren, die einen Nutzer:innen dazu ermutigt, einen abgebrochenen Warenkorb wieder abzuholen. Sie können die Daten jedoch nutzen, um die Nachricht direkt zu personalisieren, die Reise des Nutzers über die Zielgruppen-Pfade zu bestimmen oder die in den nachfolgenden Messaging-Schritten verwendeten Texte oder Assets festzulegen.

## Anwendungsfälle

![Diagramm der Anwendungsfälle für die Integration von Fullstory mit Braze]({% image_buster /assets/img/fullstory/1.png %})

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

|Anforderung     | Beschreibung |                        
|-----------------------|-----------------|
| Ein Fullstory Session API Autorisierungs-Token   | Siehe Schritt 1 unten.  | 
| Ein Braze Connected-Content Autorisierungs-Token aktiviert | Siehe den Hinweis unten zu Early Access |
| Ein Braze-Canvas-Kontext-Schritt |Siehe den Hinweis unten zu Early Access |
| Enablement Braze AI Agent Schritt | Siehe den Hinweis unten zu Early Access|
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integration von Fullstory

### Schritt 1: Fullstory für das Enablement der Session Summary APIs einrichten

#### A: Abrufen des [Auth-Tokens](https://developer.fullstory.com/server/authentication/) für den Endpunkt der Session Summary API

Um einen Fullstory API-Schlüssel zu erstellen, navigieren Sie zur Fullstory-Plattform und dann zu **Einstellungen** > **API-Schlüssel**. Wählen Sie die Berechtigungsstufe **Standard** aus, und kopieren Sie den Schlüsselwert sofort, da er nur einmal erscheint.

#### B: Erstellen einer Sitzungsübersicht Profil ID

Folgen Sie der [Anleitung von Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles) und erstellen Sie ein Profil für die Sitzungszusammenfassung über den entsprechenden Endpunkt. Hier legen Sie fest, welche Art von Daten Sie mit der Antwort Session Summary an Braze übermitteln möchten.
In der Antwort auf diese Anfrage stellt Fullstory eine Session "Profile ID" zur Verfügung. Diese Profil ID ist eine Schlüsselkomponente des Connected-Content-Anfragekörpers, der im folgenden Anwendungsfall verwendet wird.


### Schritt 2: Erstellen Sie das Connected-Content Token Auth
1. Navigieren Sie in Braze zu **Einstellungen > Workspace-Einstellungen > Connected-Content > Zugangsdaten hinzufügen > Token-Authentifizierung**. 

2. Nennen Sie die Authentifizierung "fullstory".

3. Fügen Sie den Header-Schlüssel "Autorisierung" hinzu. Geben Sie den im vorherigen Schritt angegebenen Header-Wert Fullstory ein. 

4. Geben Sie unter Zulässige Domain "api.fullstory.com" ein.

![Screenshot von Braze mit den Feldern Zugangsdaten bearbeiten]({% image_buster /assets/img/fullstory/2.png %})

## Anwendungsfälle: Nutzen Sie die Daten der Fullstory-Sitzungszusammenfassung und die Braze-Canvas-Kontext-Schritte und KI-Agenten, um dynamische Nachrichten-Journeys zu erstellen.

Mit den [Aktivierungs-Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) von Fullstory können Sie Braze Canvase unmittelbar nach wichtigen Nutzer:innen-Interaktionen triggern. Die Leistung dieser Integration liegt in der eindeutigen `client_session_id` (zugänglich über {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), die das System automatisch von Fullstory an Braze weitergibt. Diese ID dient als Schlüssel, der es Braze erlaubt, die vollständige Sitzungszusammenfassung zu holen, die genau zeigt, was der Nutzer:innen erlebt hat. 

Indem Sie Canvas-Kontext-Schritte und Connected-Content nutzen, können Sie diese ID verwenden, um eine API-Anfrage an Fullstory zu stellen, die Sitzungsdaten abzurufen und sie als Variable für die spätere Verwendung in der Reise zu speichern. 

![Screenshot des Braze-Canvas-Schrittes, der zeigt, wie die Kontextvariable `summary_result` erstellt und mit einem Connected-Content-Aufruf an Fullstory gefüllt wird, um eine Sitzungszusammenfassung abzurufen]({% image_buster /assets/img/fullstory/3.png %})

Verwenden Sie mit dem zuvor erstellten Autorisierungs-Token die folgende Struktur der Anfrage, um die Daten der Sitzungszusammenfassung abzurufen. 

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert Note %}
 Die Antwort wird als Liquid-Tag {% raw %}`{{context.${summary_result}.response}}`{% endraw %} gespeichert. Wir verwenden diesen Context-Tag in den nachfolgenden Canvas-Schritten.
{% endalert %}

In diesem Stadium kann der Canvas auf die Antwort auf den Aufruf von Connected-Content zugreifen, die die gesamte Nutzlast der Nachricht für die Sitzung eines Nutzers:innen enthält.

{% details Example Payload from Session Summary API %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

Sie können alle Daten, die im obigen Objekt verfügbar sind, nutzen, indem Sie den kontextuellen Liquid-Tag später in der Canvas-Reise des Nutzers verwenden. Die folgenden Schritte zeigen, wie Sie diese Daten in einem [KI Agent](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step) Canvas-Schritt verwenden können.

{% alert Note %}
Um unerwartetes Verhalten zu vermeiden, fügen Sie nach dem Context-Schritt einen Zielgruppen-Pfad ein, der Nutzer:in aus dem Kontext herausnehmen kann, wenn ihr Context-Tag leer ist, was bedeutet, dass der Aufruf von Connected-Content fehlgeschlagen ist oder anderweitig keine Informationen zurückgegeben hat.

![Screenshot von Braze Zielgruppe Schritt]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

## Erstellen Sie einen KI-Agenten, der die Payloads von Fullstory analysiert und für Ihren Anwendungsfall geeignete Kopien erstellt.

[Die Agentenanleitung von Braze]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents) beschreibt, wie Nutzer:innen von Braze KI-Agenten erstellen können. Durch das Einfügen eines KI-Agenten-Schrittes in ein von Fullstory getriggertes Canvas und den oben beschriebenen Canvas-Kontext-Schritt können Nutzer:innen ihren KI-Agenten mit den Sitzungszusammenfassungsdaten von Fullstory füttern, und zwar für eine breite Palette von Zwecken. 

In diesem Beispiel verwenden wir diese Daten, um dem KI-Agenten die Möglichkeit zu geben, geeignete Nachrichten für eine Content-Card zu erstellen, die den Nutzer:innen dazu ermutigen können, zu ihrem verlassenen Warenkorb zurückzukehren.

![Screenshot von Braze Agent Context Creator mit der Eingabeaufforderung]({% image_buster /assets/img/fullstory/4.png %})

Verwenden Sie für den in diesem Schritt erstellten Context Liquid-Tag denselben Namen wie für den Context Liquid-Tag, der in dem zuvor erstellten KI-Agent-Schritt verwendet wurde. 

Die für Ihren Anwendungsfall erforderliche Eingabeaufforderung variiert, aber unsere besten Praktiken für die Erstellung effektiver Agenten-Eingabeaufforderungen finden Sie unter [Anweisungen schreiben]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents/#writing-instructions) in *Agenten erstellen*. 


Wählen Sie in Ihrem Canvas einen KI-Agenten-Schritt und wählen Sie dann den erstellten Agenten "Sitzungskontext" aus dem Dropdown- Menü aus. Speichern Sie die Ausgabe als Variable, in diesem Fall "Nachricht", die Sie mit dem Liquid-Tag {% raw %}`{{context.${message}.message}}`{% endraw %} in die Kopie der Nachricht einfügen können.

![Screenshot des Braze Agent Context Canvas-Schrittes mit der Eingabeaufforderung]({% image_buster /assets/img/fullstory/5.png %})

Erstellen Sie einen Nachrichten-Schritt, der die von einem KI-Agenten erstellte Kopie nutzt. Verwenden Sie in diesem Schritt den Liquid-Tag. 

{% alert Note %}

Die Session Summary API von Fullstory kann sensible, identifizierbare Nutzerdaten zurückgeben. Um die Einhaltung von Vorschriften im Umgang mit PII (Personally Identifiable Information) zu gewährleisten, stellen Sie sicher, dass Ihre Fullstory-Datenerfassungsregeln PII ausschließen, bevor Sie diesen Anwendungsfall nutzen.

{% endalert %}