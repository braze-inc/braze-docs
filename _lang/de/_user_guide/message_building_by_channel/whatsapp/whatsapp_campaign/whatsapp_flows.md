---
nav_title: WhatsApp-Flows
article_title: WhatsApp-Flows
page_order: 1
description: "Dieser Referenzartikel behandelt die Schritte zum Erstellen und Entwerfen einer WhatsApp Flows-Nachricht."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp-Flows

> WhatsApp Flows ist eine Erweiterung des bestehenden WhatsApp-Kanals, mit der Sie interaktive und dynamische Messaging-Erlebnisse schaffen können. Diese Seite enthält eine Schritt-für-Schritt-Anleitung zur Verwendung von WhatsApp Flows.

## Einrichtung von WhatsApp Flows

1. Bitte melden Sie sich bei Ihrem Meta-Konto an.
2. Erstellen Sie Flows von einem der beiden Hauptstandorte aus:
    - **Konto-Tools:** Bitte gehen Sie zum Tab **„Flows“,** um die Flow-ID anzuzeigen und einen neuen Flow zu erstellen.
    - **Vorlagen verwalten:** Dies ist die empfohlene Methode zum Erstellen von Flows. Hier können Sie Templates erstellen und während des Erstellungsprozesses eine Flow-Option auswählen.

![WhatsApp Manager mit einer Seite zum Erstellen eines Flows-Templates.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Bitte wählen Sie einen bestehenden Flow aus oder erstellen Sie einen neuen. Wenn Sie einen Flow erstellen möchten, haben Sie zwei Optionen zur Auswahl:
  - **Angepasstes Formular:** Für spezifische Anforderungen
  - **Vorgefertigte Elemente:** Für eine schnellere Einrichtung

## Konfiguration von WhatsApp Flow-Nachrichten und Antworten

{% tabs local %}
{% tab Template message %}

1. Erstellen Sie in einem Braze-Canvas einen WhatsApp-Nachrichtenschritt, der das Template mit dem entsprechenden Flow verwendet.
2. Bitte setzen Sie die Erstellung Ihres Templates fort. Fügen Sie Ihrer Nachricht bei Bedarf Medien, variable Inhalte oder beides hinzu. Ihre Flow-Auswahl wurde bei der Erstellung des Templates ausgewählt, daher sind keine zusätzlichen Informationen für die Flow-Erfahrung erforderlich.

![WhatsApp-Nachrichten-Editor unter Verwendung eines WhatsApp Flow-Templates.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Erstellen Sie in Braze-Canvas einen WhatsApp-Nachrichtenschritt, der eine Antwortnachricht und eine Flow-Nachricht verwendet.

![Ein Nachrichtenschritt für einen WhatsApp-Antwortnachrichtentyp und ein Flow-Nachrichtenlayout.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Bitte wählen Sie den entsprechenden Ablauf aus und fahren Sie dann mit der Erstellung Ihrer Nachricht fort. 

![Ein Flow-Nachrichten-Editor mit einem erweiterten Dropdown-Menü, um einen Flow auszuwählen.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Flow-Vorschau

Bevor Sie ein Canvas mit einem Flow starten, können Sie **„Flow in der Vorschau anzeigen“** auswählen, um den Flow direkt in Braze **in der Vorschau** anzuzeigen und zu überprüfen, ob er wie erwartet funktioniert. Sie können auch mit dem Flow in der Vorschau interagieren, um zu erfahren, wie ein Nutzer:in durch den Flow navigieren würde, und dann Anpassungen in Realtime vornehmen. Wenn ein Flow mehrere Seiten enthält, können Sie mit jeder Seite interagieren.

![Vorschau-Fenster, in dem ein Formular angezeigt wird, mit dem ein Nutzer:in die Registrierung abschließen kann.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Speichern der vollständigen Flow-Antwort {#full-flow}

Wenn Sie eine WhatsApp Flow-Nachricht in ein Braze-Canvas oder eine Kampagne integrieren, möchten Sie möglicherweise bestimmte Informationen erfassen und nutzen, die Nutzer:innen über den Flow übermitteln. Braze benötigt zusätzliche Informationen zur Struktur der Benutzerantwort, insbesondere zur erwarteten Form der JSON-Antwort, um das erforderliche Schema für verschachtelte angepasste Attribute (NCA) zu generieren.

### Schritt 1: Erstellen Sie das benutzerdefinierte Attribut „Flow“.

{% tabs local %}
{% tab Recommended method %}

Die einfachste Methode, Braze die Informationen über die Antwortstruktur zu übermitteln, besteht darin, die Flow-Antwort als angepasstes Attribut zu speichern und einen Testversand durchzuführen.

#### Verwendung eines Flows, der in Braze noch nicht verwendet wurde

Wenn Sie einen Flow verwenden, der zuvor noch nicht in Braze verwendet wurde, werden möglicherweise keine Informationen angezeigt, wenn Sie den Abschnitt **„Flow-benutzerdefinierte Attribute“** unter **„Nachrichten** **verfassen**“ aufrufen. Dies bedeutet, dass das Schema noch nicht generiert wurde.

![Meta-Flow-Abschnitt mit der Option, das benutzerdefinierte Flow-Attribut anzuzeigen.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Um dieses Problem zu beheben, gehen Sie bitte wie folgt vor:

1. Bitte schließen Sie die Einrichtung Ihrer WhatsApp-Nachricht ab.
2. Bitte bestätigen Sie, dass Sie **„Flow-Antworten als benutzerdefiniertes Attribut speichern**“ aktiviert haben.

![Meta-Flow-Abschnitt mit einem Kontrollkästchen zum Speichern von Flow-Antworten als angepasstes Attribut.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Senden Sie sich selbst eine Testnachricht und schließen Sie den Ablauf als Nutzer:in ab.

Nun verfügt Braze über die Form des Flow-Antwort-JSON und kann das angepasste Attribut generieren.

{% endtab %}
{% tab Alternative methods %}

Verwenden Sie den erweiterten JSON-Editor, um Attribute aus der Flow-Antwort in angepassten Attributen zu speichern, oder verwenden Sie ein mehrstufiges Canvas, um die Antwort in verschachtelten angepassten Attributen zu speichern. 

{% subtabs %}
{% subtab Advanced JSON editor %}

Geben Sie im erweiterten JSON-Editor ein{% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, wobei das “flow_1”angepasste Attribut ist, unter dem der Ablauf gespeichert werden soll.

![Update-Schritt für Nutzer:innen mit einem erweiterten JSON-Editor.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Bitte bestätigen Sie, dass Sie bereits ein angepasstes Attribut mit dem Objekttyp (("flow_1"in diesem Beispiel) in Ihren Workspace-Daten-Einstellungen erstellt haben.
2. Verwenden Sie im UI-Editor Liquid, {% raw %}```{{whats_app.${inbound_flow_response}}}```um das angepasste Attribut zu füllen und die gesamte Flow-Antwort der Nutzer:innen darin zu speichern. Bitte geben Sie den Schlüsselwert ein,```{{whats_app.${inbound_flow_response}}}```{% endraw %}bevor Sie das von Ihnen erstellte angepasste Attribut auswählen.

![Benutzer-Update-Schritt, der den UI-Editor verwendet.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Sobald Braze eine Flow-Antwort erhält, speichern wir das verschachtelte angepasste Attribut mit der vorgeschriebenen Benennung im Nutzerprofil. Dieses benutzerdefinierte Attribut kann beim Erstellen von Canvases abgerufen werden. 

![Ein Fenster, das den Inhalt eines"flow_1"benutzerdefinierten Attributs anzeigt.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Schritt 2: Die gespeicherte Flow-Antwort anzeigen

Nach Abschluss des Flows erstellt Braze automatisch ein benutzerdefiniertes Flow-Attribut mit einem Namen, der auf der Flow-ID basiert. Anschließend können Sie im Nutzerprofil die gespeicherte Flow-Antwort als verschachteltes Objekt im Abschnitt **„Angepasste Attribute“** anzeigen.

Nach der Generierung des Schemas wird im Abschnitt „Flow **Custom Attribute“** (**Benutzerdefinierte Flow-Attribute**) die erwartete Struktur angezeigt, einschließlich der voraussichtlichen Datentypen für jede Antwort (z. B. „String“ oder „String Array“).

![Fenster mit Details zu angepassten Attributen mit Schema-Dropdown-Menü.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Überlegungen

- **Bestehende Attribute:** Wenn für einen bestimmten Flow bereits ein angepasstes Attribut generiert wurde, wird der Flow mit den verfügbaren Attributinformationen geladen. In diesen Fällen ist es nicht erforderlich, eine Testnachricht zu senden, um das Schema zu generieren, da Braze die erwarteten Antwortnachrichten bereits erkennt.
- **Strömungsänderungen:** Sollten Sie nach der Generierung des Schemas Änderungen am Flow vornehmen, ist es erforderlich, eine zusätzliche Testnachricht zu senden, damit Braze die veränderte Struktur der Flow-Antwort erkennen und die Attribute entsprechend anpassen kann. Diese Aktion ist auf einmal alle 24 Stunden beschränkt. 
- **Konsistenz:** Das generierte benutzerdefinierte Attribut „Flow“ ist konsistent und bleibt für diesen spezifischen Flow unverändert, unabhängig davon, in welchem Canvas es verwendet wird.
- **Manuelle Option:** Es ist nicht erforderlich, das Kontrollkästchen **„Flow-Antworten als benutzerdefiniertes Attribut speichern**“ auszuwählen. Sie können das angepasste Attribut manuell generieren, indem [Sie bestimmte Felder aus Flow-Antworten in einem bestimmten angepassten Attribut speichern](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), wodurch doppelte Schritte für die Nutzer:innen vermieden werden.

## Spezifische Felder aus Flow-Antworten in einem bestimmten angepassten Attribut speichern 

### Schritt 1: Erstellen Sie einen Aktions-Pfad

Erstellen Sie einen Canvas-Schritt [für den Aktions-Pfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) oder eine aktionsbasierte Kampagne. Wählen Sie den Auslöser **„WhatsApp-eingehende Nachricht senden“** und die **Flow**-Bedingung **„Beantwortet“** aus und wählen Sie anschließend den entsprechenden Flow oder **„Beliebiger Flow“** aus.

![Ein Auslöser für Nutzer:innen, die eine eingehende WhatsApp-Nachricht gesendet und auf einen beliebigen Flow geantwortet haben.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Schritt 2: Extrahieren Sie Felder aus Flow-Antworten

Sie können verschachtelte angepasste Attribute oder das`json_parse`Liquid-Tag verwenden, um bestimmte Felder aus Flow-Antworten zu extrahieren.

{% tabs %}
{% tab Nested custom attributes %}

Um bestimmte Teile der Flow-Antwort der Nutzer:innen zu speichern, führen Sie bitte alle Schritte unter [„Speichern der vollständigen Flow-Antwort“](#full-flow) aus, **einschließlich des Startens von Canvas**. Die Canvas-Anwendung muss gestartet sein, um das verschachtelte angepasste Attribut zu erstellen, das Sie referenzieren werden. Nachdem Sie Canvas gestartet und einen Ablauf abgeschlossen haben, führen Sie bitte die folgenden Schritte aus:

1. Erstellen Sie einen nachfolgenden Schritt zum Update der Nutzer:innen, der den UI-Editor verwendet.
2. Bitte wählen Sie **„Personalisierung hinzufügen”** aus, anschließend **„Verschachtelte angepasste Attribute**” und das entsprechende Attribut der obersten Ebene, in dem der Flow gespeichert ist.  

![Benutzer-Update-Schritt mit einer Personalisierung durch verschachtelte angepasste Attribute.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Bitte wählen Sie das Schlüsselattribut aus, das Sie speichern möchten, und fügen Sie Liquid in das Feld **„Schlüsselwert“** ein.

![Fenster mit"flow_1" Attributen, um diese auszuwählen.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Bitte wählen Sie das Attribut aus, in dem Sie es speichern möchten.
5\. Bitte senden Sie eine Testnachricht, um den Ablauf zu überprüfen.

{% endtab %}
{% tab Parse function %}

Verwenden Sie das`json_parse`Liquid-Tag, um bestimmte Antworten aus dem Ablauf zu extrahieren. Beispielsweise können Sie das Flow-Token und ausgewählte Optionen verwenden, um eine Follow-up-Nachricht anzupassen.

Bitte wählen Sie im UI-Editor Folgendes aus: 

- **Attributname:**YOUR_CUSTOM_ATTRIBUTE(in diesem Beispiel: “First_name”)
- **Aktion:** Aktualisieren
- **Schlüsselwert:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![WhatsApp-Nachrichten-Editor mit einer Komponente „Personalisierung hinzufügen”, um eine WhatsApp-Eigenschaftspersonalisierung mit dem angepassten Attribut`inbound_flow_response`.]({%image_buster/assets/img/whatsapp/flows/parsed_json.png einzufügen.

Wenn Sie bereit sind, senden Sie bitte eine Testnachricht, um den Ablauf zu überprüfen. Starten Sie anschließend Canvas.

{% endtab %}
{% endtabs %}

{% alert note %}
Eine neue WhatsApp-Nachricht „löscht“ die Fähigkeit von Canvas, die Liquid Flow-Antwort zu verwenden (und wiederzuverwenden). Stellen Sie daher sicher, dass Folgemeldungen nach allen Updates, Webhooks oder anderen Schritten erfolgen, die die Liquid Flow-Antwort verwenden.
{% endalert %}

## Hinzufügen eines Flow-Tag-Tags für die Personalisierung

Um die Flow-Antwort über Liquid mit [unterstützten Tags für Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) zu verwenden, führen Sie bitte die folgenden Schritte aus:

1. Wählen Sie beim Verfassen Ihrer WhatsApp-Nachricht das Plus-Symbol, um das Fenster **„Personalisierung hinzufügen”** zu öffnen.
2. Wählen Sie **„WhatsApp-Eigenschaften“** als Personalisierungstyp und**inbound_flow_response**  als benutzerdefiniertes Attribut. Dies kann verwendet werden, um Informationen in Nutzerprofilen zu speichern, sie in Nachrichten einzufügen oder an andere Dienste, wie beispielsweise Webhooks, weiterzuleiten.

![WhatsApp-Nachrichten-Editor mit einer Komponente „Personalisierung hinzufügen”, um eine WhatsApp-Eigenschaftspersonalisierung mit dem angepassten Attributinbound_flow_response.]({%image_buster/assets/img/whatsapp/flows/inbound_flow_response.png einzufügen.{: style="max-width:80%;"}

Bei Fragen oder für weitere Unterstützung wenden Sie sich bitte an [den Support]({{site.baseurl}}/braze_support/).