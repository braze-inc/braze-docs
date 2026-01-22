---
nav_title: WhatsApp-Flows
article_title: WhatsApp-Flows
page_order: 1
description: "Dieser referenzierte Artikel beschreibt die Schritte, die zum Aufbau und zur Erstellung einer WhatsApp Flows Nachricht gehören."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp-Flows

> WhatsApp Flows ist eine Erweiterung des bestehenden WhatsApp-Kanals, die es Ihnen erlaubt, interaktive und dynamische Messaging-Erlebnisse zu erstellen. Auf dieser Seite finden Sie eine Schritt-für-Schritt-Anleitung für die Teilnahme am Early Access-Programm und die Nutzung von WhatsApp Flows.

## Einrichten von WhatsApp Flows

1. Melden Sie sich bei Ihrem Meta-Konto an.
2. Erstellen Sie Flows von einem der beiden Hauptstandorte aus:
    - **Konto-Tools:** Gehen Sie auf den Tab **Flows**, um die Flow ID zu sehen und einen neuen Flow zu erstellen.
    - **Verwalten Sie Templates:** Dies ist die empfohlene Methode zur Erstellung von Flows. Hier können Sie Templates erstellen und bei der Erstellung des Templates eine Flow-Option auswählen.

![WhatsApp Manager:in mit einer Seite zur Erstellung eines Flows Templates.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Wählen Sie eine vorhandene Bewegung aus oder erstellen Sie eine. Wenn Sie einen Flow erstellen, wählen Sie aus zwei Optionen:
  - **Angepasstes Formular:** Für besondere Anforderungen
  - **Vorgefertigte Elemente:** Für eine schnellere Einrichtung

## Konfigurieren von WhatsApp Flow Nachrichten und Antworten

{% tabs local %}
{% tab Template message %}

1. Erstellen Sie in einem Braze-Canvas einen WhatsApp-Schritt, der die Template-Nachricht verwendet, die den jeweiligen Flow enthält.
2. Fahren Sie mit der Erstellung Ihres Templates fort. Fügen Sie Ihrer Nachricht bei Bedarf Medien, variable Inhalte oder beides hinzu. Ihre Flow-Auswahl wurde bei der Erstellung des Templates ausgewählt, so dass zusätzliche Informationen für das Flow-Erlebnis nicht erforderlich sind.

![WhatsApp Nachrichten-Editor mit einer WhatsApp Flow-Vorlage.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Erstellen Sie in einem Braze-Canvas einen WhatsApp-Schritt, der eine Antwortnachricht und eine Flussnachricht verwendet.

![Ein Nachrichtenschritt für einen WhatsApp-Antwortnachrichtentyp und ein Flow-Nachrichtenlayout.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Wählen Sie den entsprechenden Flow aus und fahren Sie dann mit der Erstellung Ihrer Nachricht fort. 

![Ein Nachrichten-Editor für Messaging-Nachrichten mit einem erweiterten Dropdown-Menü zum Auswählen eines Messagings.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Flow-Vorschau

Bevor Sie ein Canvas mit einem Flow starten, können Sie **Flow-Vorschau** auswählen, um eine Vorschau des Flows direkt in Braze zu sehen und zu bestätigen, dass er sich wie erwartet verhält. Sie können auch mit dem Flow in der Vorschau interagieren, um zu erfahren, wie ein Nutzer:innen durch den Flow navigieren würde, und dann Anpassungen in Realtime vornehmen. Wenn ein Flow mehrere Seiten enthält, können Sie mit jeder Seite interagieren.

![Vorschau-Fenster, das ein Formular anzeigt, mit dem ein Nutzer:in die Registrierung einsteigen kann.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Speichern der vollständigen Flow-Antwort {#full-flow}

### Schritt 1: Erstellen Sie einen Aktions-Pfad

Erstellen Sie einen [Action-Pfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) Canvas-Schritt oder eine aktionsbasierte Kampagne. Wählen Sie einen Auslöser für **eingehende Nachrichten in WhatsApp** und die Bedingung **"Antwort auf Flow"** und wählen Sie dann den entsprechenden Flow oder **einen beliebigen Flow** aus.

![Ein Trigger für Nutzer:in, die eine eingehende WhatsApp Nachricht gesendet und auf einen Flow geantwortet haben.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Schritt 2: Verfassen Sie Ihre WhatsApp-Nachricht

Wenn Sie Ihre WhatsApp Nachricht verfassen, wählen Sie das Plus-Symbol, um das Fenster **Personalisierung hinzufügen** zu öffnen, und wählen Sie dann **WhatsApp Eigenschaften** für die Art der Personalisierung und **inbound_flow_response** für das angepasste Attribut. Damit werden Informationen in Nutzerprofilen gespeichert oder an andere Dienste, wie z.B. Webhooks, weitergeleitet.

![WhatsApp Nachrichten-Editor mit einer Komponente "Personalisierung hinzufügen" zum Einfügen einer Personalisierung der WhatsApp Eigenschaften mit dem angepassten Attribut `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:60%;"}

### Schritt 3: Speichern Sie die vollständige Flow-Antwort

Sie können den erweiterten JSON-Editor verwenden, um Attribute aus der Flow-Antwort in angepassten Attributen zu speichern, oder ein mehrstufiges Canvas verwenden, um die Antwort in einem angepassten Attribut zu speichern. 

{% tabs %}
{% tab Advanced JSON editor %}

Geben Sie im vorab gebrachten JSON-Editor {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %} ein, wobei “flow_1” das angepasste Attribut ist, in dem Sie den Fluss speichern möchten.

Nutzer:in Update-Schritt mit einem fortschrittlichen JSON-Editor.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endtab %}
{% tab UI editor %}

1. Vergewissern Sie sich, dass Sie bereits ein angepasstes Attribut mit dem Objektdatentyp (in diesem Beispiel ("flow_1" ) innerhalb Ihrer Workspace-Dateneinstellungen erstellt haben.
2. Verwenden Sie im UI-Editor das Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}```, um das angepasste Attribut zu füllen und die gesamte Flow-Antwort des Nutzers:innen darin zu speichern. Sie müssen den Schlüsselwert als ```{{whats_app.${inbound_flow_response}}}```{% endraw %} eingeben, bevor Sie das angepasste Attribut auswählen, das Sie erstellt haben.

![Nutzer:in Update-Schritt, der den UI-Editor verwendet.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Nachdem Braze eine Flow-Antwort erhalten hat, speichern wir das verschachtelte angepasste Attribut mit der vorgeschriebenen Benennung im Nutzerprofil. Dieses angepasste Attribut kann bei der Erstellung von Canvase verwendet werden. 

![Ein Fenster, das den Inhalt eines angepassten Attributs von "flow_1" anzeigt.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endtab %}
{% endtabs %}

Wenn Sie bereit sind, senden Sie eine Testnachricht, um den Flow zu testen. Dann starten Sie den Canvas!

## Speichern von bestimmten Feldern aus Flow-Antworten in einem bestimmten angepassten Attribut 

Sie können verschachtelte angepasste Attribute oder den `json_parse` Liquid-Tag verwenden, um bestimmte Felder aus Flow-Antworten zu extrahieren.

{% tabs %}
{% tab Nested custom attributes %}

Um bestimmte Teile der Nutzer:innen-Flow-Antwort zu speichern, führen Sie alle Schritte unter [Speichern der vollständigen Flow-Antwort](#full-flow) aus, **einschließlich des Starts des Canvas**. Das Canvas muss gestartet werden, um das angepasste Attribut, das Sie referenzieren werden, zu erstellen. Nachdem Sie den Canvas gestartet und einen Flow abgeschlossen haben, führen Sie die folgenden Schritte aus:

1. Erstellen Sie einen nachfolgenden Schritt Nutzer:in Update, der den UI-Editor verwendet.
2. Wählen Sie **Personalisierung hinzufügen**, dann wählen Sie **Verschachteltes angepasstes Attribut** und das entsprechende Attribut der obersten Ebene, in dem der Fluss gespeichert ist.  

![Benutzer:in Update-Schritt mit verschachtelten angepassten Attributen Personalisierung.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Wählen Sie das Attribut, das Sie speichern möchten, und fügen Sie das Liquid in das Feld **Schlüsselwert** ein.

![Fenster für "flow_1" mit Attributen zum Auswählen.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Wählen Sie das Attribut, in dem Sie es speichern möchten.
5\. Senden Sie eine Testnachricht, um den Fluss zu testen.

{% endtab %}
{% tab Parse function %}

Verwenden Sie den `json_parse` Liquid-Tag, um bestimmte Antworten aus dem Fluss zu extrahieren. Sie können zum Beispiel das Flow-Token und ausgewählte Optionen herausziehen, um eine Nachricht anzupassen.

### Schritt 1: Erstellen Sie einen Aktions-Pfad

Erstellen Sie einen [Aktions-Pfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) mit **Senden einer eingehenden WhatsApp Nachricht** triggern, um die Flow-Informationen zu verarbeiten.

{% alert note %}
Sie können den Flow angeben, wenn zusätzliche Features während des Early Access veröffentlicht werden.
{% endalert %}

### Schritt 2: Verfassen Sie Ihre WhatsApp-Nachricht

Wenn Sie Ihre WhatsApp Nachricht verfassen, wählen Sie das Plus-Symbol, um das Fenster **Personalisierung hinzufügen** zu öffnen, und wählen Sie dann **WhatsApp Eigenschaften** für die Art der Personalisierung und **inbound_flow_response** für das angepasste Attribut. Damit werden Informationen in Nutzerprofilen gespeichert oder an andere Dienste, wie z.B. Webhooks, weitergeleitet.

### Schritt 3: Bestimmte Felder aus der Flow-Antwort speichern

Wählen Sie im UI-Editor das Folgende aus: 

- **Attribut Name:** YOUR_CUSTOM_ATTRIBUTE (in diesem Beispiel: “First_name”)
- **Aktion:** Aktualisieren
- **Schlüsselwert:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![WhatsApp Nachrichten-Editor mit einer Komponente "Personalisierung hinzufügen" zum Einfügen einer Personalisierung der WhatsApp Eigenschaften mit dem angepassten Attribut `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

{% alert note %}
Eine neue WhatsApp-Nachricht "löscht" die Fähigkeit des Canvas, die Liquid Flow-Antwort zu verwenden (und wiederzuverwenden). Stellen Sie also sicher, dass die nachfolgenden Nachrichten nach allen Nutzer:innen-Update-Schritten, Webhooks oder anderen Schritten, die die Liquid Flow-Antwort verwenden, erfolgen.
{% endalert %}

Wenn Sie bereit sind, senden Sie eine Testnachricht, um den Flow zu testen. Dann starten Sie den Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Es werden zusätzliche Flow-Funktionen eingeführt, einschließlich vorgebrachter Filter für Aktionsschritte und Nachrichten, die Flow-Elemente einbeziehen.
{% endalert %}

Wenn Sie Fragen haben oder weitere Hilfe benötigen, wenden Sie sich bitte an den [Support]({{site.baseurl}}/braze_support/).