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

> WhatsApp Flows ist eine Erweiterung des bestehenden WhatsApp-Kanals, die es Ihnen erlaubt, interaktive und dynamische Messaging-Erlebnisse zu erstellen. Auf dieser Seite finden Sie eine schrittweise Anleitung zur Verwendung von WhatsApp Flows.

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

![Nachrichten-Editor für WhatsApp unter Verwendung einer WhatsApp Flow-Vorlage.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Erstellen Sie in einem Braze-Canvas einen WhatsApp-Schritt, der eine Antwortnachricht und eine Flussnachricht verwendet.

![Ein Nachrichtenschritt für einen WhatsApp Antwortnachrichtentyp und ein Flow Nachrichtenlayout.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Wählen Sie den entsprechenden Flow aus und fahren Sie dann mit der Erstellung Ihrer Nachricht fort. 

![Ein Nachrichten-Editor für Messaging-Nachrichten mit einem erweiterten Dropdown-Menü zum Auswählen eines Messagings.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Flow-Vorschau

Bevor Sie ein Canvas mit einem Flow starten, können Sie **Flow-Vorschau** auswählen, um eine Vorschau des Flows direkt in Braze zu sehen und zu bestätigen, dass er sich wie erwartet verhält. Sie können auch mit dem Flow in der Vorschau interagieren, um zu erfahren, wie ein Nutzer:innen durch den Flow navigieren würde, und dann Anpassungen in Realtime vornehmen. Wenn ein Flow mehrere Seiten enthält, können Sie mit jeder Seite interagieren.

![Vorschau-Fenster, das ein Formular anzeigt, mit dem ein Nutzer:in die Registrierung einsteigen kann.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Speichern der vollständigen Flow-Antwort {#full-flow}

Wenn Sie eine WhatsApp Flow Nachricht in ein Braze-Canvas oder eine Kampagne einbinden, möchten Sie vielleicht bestimmte Informationen, die Nutzer:innen über den Flow übermitteln, erfassen und nutzen. Braze benötigt zusätzliche Informationen über die Struktur der Nutzer:innen-Antwort, insbesondere die erwartete Form der JSON-Antwort, um das erforderliche Schema für die angepassten Attribute (NCA) zu erstellen.

### Schritt 1: Erzeugen Sie das angepasste Attribut Flow

{% tabs local %}
{% tab Recommended method %}

Der einfachste Weg, Braze die Informationen über die Antwortstruktur zu geben, besteht darin, die Flow-Antwort als angepasstes Attribut zu speichern und einen Testversand durchzuführen.

#### Einen Flow verwenden, der noch nicht in Braze verwendet wurde

Wenn Sie einen Flow verwenden, der zuvor noch nicht in Braze verwendet wurde, sehen Sie bei der Anzeige des Abschnitts **Angepasste Attribute des Flows** in der Funktion **Nachrichten verfassen** möglicherweise keine Informationen. Das bedeutet, dass das Schema noch nicht erstellt wurde.

![Meta Flow-Abschnitt mit einer Option zur Anzeige des angepassten Attributs Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Um dies zu beheben, gehen Sie wie folgt vor:

1. Vervollständigen Sie den Schritt zur Einrichtung Ihrer WhatsApp Nachrichten.
2. Bestätigen Sie, dass Sie **Flussantworten als angepasstes Attribut speichern** markiert haben.

![Meta Flow-Abschnitt mit einem Kontrollkästchen zum Speichern von Flow-Antworten als angepasstes Attribut.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Senden Sie sich selbst eine Nachricht zum Test und schließen Sie den Flow als Nutzer:in ab.

Jetzt hat Braze die Form der Flow-Antwort JSON und kann das angepasste Attribut generieren.

{% endtab %}
{% tab Alternative methods %}

Verwenden Sie den erweiterten JSON-Editor, um Attribute aus der Flow-Antwort in angepassten Attributen zu speichern, oder verwenden Sie ein mehrstufiges Canvas, um die Antwort in einem angepassten Attribut zu speichern. 

{% subtabs %}
{% subtab Advanced JSON editor %}

Geben Sie im vorab gebrachten JSON-Editor {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %} ein, wobei “flow_1” das angepasste Attribut ist, in dem Sie den Fluss speichern möchten.

![Nutzer:innen Update-Schritt mit einem fortschrittlichen JSON-Editor.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Vergewissern Sie sich, dass Sie bereits ein angepasstes Attribut mit dem Objektdatentyp (in diesem Beispiel ("flow_1" ) innerhalb Ihrer Workspace-Dateneinstellungen erstellt haben.
2. Verwenden Sie im UI-Editor das Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}```, um das angepasste Attribut zu füllen und die gesamte Flow-Antwort des Nutzers:innen darin zu speichern. Sie müssen den Schlüsselwert als ```{{whats_app.${inbound_flow_response}}}```{% endraw %} eingeben, bevor Sie das angepasste Attribut auswählen, das Sie erstellt haben.

![Nutzer:in Update-Schritt, der den UI-Editor verwendet.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Nachdem Braze eine Flow-Antwort erhalten hat, speichern wir das verschachtelte angepasste Attribut mit der vorgeschriebenen Benennung im Nutzerprofil. Dieses angepasste Attribut kann bei der Erstellung von Canvase verwendet werden. 

![Ein Fenster, das den Inhalt eines angepassten Attributs von "flow_1" anzeigt.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Schritt 2: Anzeigen der gespeicherten Flow-Antwort

Wenn der Flow abgeschlossen ist, erstellt Braze automatisch ein angepasstes Attribut für den Flow mit einem Namen, der auf der Flow ID basiert. Sie können dann zum Nutzerprofil gehen, um die gespeicherte Flow-Antwort als verschachteltes Objekt im Bereich **Angepasste Attribute** anzuzeigen.

Nachdem das Schema generiert wurde, zeigt der Abschnitt **Flussangepasste Attribute** die erwartete Struktur an, einschließlich der erwarteten Datentypen für jede Antwort (zum Beispiel "String" oder "String-Array").

![Fenster mit Details zu angepassten Attributen mit Schema-Dropdown.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Überlegungen

- **Vorhandene Attribute:** Wenn ein angepasstes Attribut für einen bestimmten Flow bereits erstellt wurde, wird der Flow mit den verfügbaren Attribut-Informationen geladen. In diesen Fällen brauchen Sie keine Testnachricht zu senden, um das Schema zu erstellen, da Braze die erwarteten Nachrichten bereits erkennt.
- **Flussänderungen:** Wenn Sie Änderungen am Flow vornehmen, nachdem das Schema generiert wurde, müssen Sie eine zusätzliche Testnachricht senden, damit Braze versteht, dass sich die Form der Flow-Antwort geändert hat und die Attributstruktur entsprechend anpassen kann. Diese Aktion ist auf einmal alle 24 Stunden beschränkt. 
- **Konsistenz:** Das erzeugte angepasste Attribut für den Flow ist konsistent und wird für diesen spezifischen Flow das gleiche Attribut sein, unabhängig davon, in welchem Canvas es verwendet wird.
- **Manuelle Option:** Sie müssen das Kontrollkästchen **Flussantworten als angepasstes Attribut speichern** nicht auswählen. Sie können das angepasste Attribut manuell generieren, indem Sie [bestimmte Felder aus den Flow-Antworten in einem bestimmten angepassten Attribut speichern](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), wodurch doppelte Schritte der Nutzer:innen vermieden werden.

## Speichern von bestimmten Feldern aus Flow-Antworten in einem bestimmten angepassten Attribut 

### Schritt 1: Erstellen Sie einen Aktions-Pfad

Erstellen Sie einen [Action-Pfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) Canvas-Schritt oder eine aktionsbasierte Kampagne. Wählen Sie einen Auslöser für **eingehende Nachrichten in WhatsApp** und die Bedingung **"Antwort auf Flow"** und wählen Sie dann den entsprechenden Flow oder **einen beliebigen Flow** aus.

![Ein Trigger für Nutzer:innen, die eine eingehende WhatsApp Nachricht gesendet und auf einen Flow geantwortet haben.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Schritt 2: Felder aus Flow-Antworten extrahieren

Sie können verschachtelte angepasste Attribute oder den `json_parse` Liquid-Tag verwenden, um bestimmte Felder aus Flow-Antworten zu extrahieren.

{% tabs %}
{% tab Nested custom attributes %}

Um bestimmte Teile der Nutzer:innen-Flow-Antwort zu speichern, führen Sie alle Schritte unter [Speichern der vollständigen Flow-Antwort](#full-flow) aus, **einschließlich des Starts des Canvas**. Das Canvas muss gestartet werden, um das angepasste Attribut, das Sie referenzieren werden, zu erstellen. Nachdem Sie den Canvas gestartet und einen Flow abgeschlossen haben, führen Sie die folgenden Schritte aus:

1. Erstellen Sie einen nachfolgenden Schritt Nutzer:in Update, der den UI-Editor verwendet.
2. Wählen Sie **Personalisierung hinzufügen**, dann wählen Sie **Verschachteltes angepasstes Attribut** und das entsprechende Attribut der obersten Ebene, in dem der Fluss gespeichert ist.  

![Benutzer:in Update-Schritt mit einer Personalisierung der angepassten Attribute verschachtelt.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Wählen Sie das Attribut, das Sie speichern möchten, und fügen Sie das Liquid in das Feld **Schlüsselwert** ein.

![Fenster für "flow_1" mit Attributen zum Auswählen.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Wählen Sie das Attribut, in dem Sie es speichern möchten.
5\. Senden Sie eine Testnachricht, um den Fluss zu testen.

{% endtab %}
{% tab Parse function %}

Verwenden Sie den `json_parse` Liquid-Tag, um bestimmte Antworten aus dem Fluss zu extrahieren. Sie können zum Beispiel das Flow-Token und ausgewählte Optionen herausziehen, um eine Nachricht anzupassen.

Wählen Sie im UI-Editor das Folgende aus: 

- **Attribut Name:** YOUR_CUSTOM_ATTRIBUTE (in diesem Beispiel: “First_name”)
- **Aktion:** Aktualisieren
- **Schlüsselwert:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![WhatsApp Nachrichten-Editor mit einer Komponente "Personalisierung hinzufügen" zum Einfügen einer Personalisierung von WhatsApp Eigenschaften mit dem angepassten Attribut `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

Wenn Sie bereit sind, senden Sie eine Testnachricht, um den Flow zu testen. Dann starten Sie den Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Eine neue WhatsApp-Nachricht "löscht" die Fähigkeit des Canvas, die Liquid Flow-Antwort zu verwenden (und wiederzuverwenden). Stellen Sie also sicher, dass die nachfolgenden Nachrichten nach allen Nutzer:innen-Update-Schritten, Webhooks oder anderen Schritten, die die Liquid Flow-Antwort verwenden, erfolgen.
{% endalert %}

## Hinzufügen eines Tags zur Personalisierung des Flusses

Um die Flow-Antwort über Liquid mit [unterstützten Tags für die Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) zu verwenden, führen Sie die folgenden Schritte aus:

1. Wenn Sie Ihre WhatsApp Nachricht verfassen, wählen Sie das Plus-Symbol aus, um das Fenster **Personalisierung hinzufügen zu** öffnen.
2. Wählen Sie **WhatsApp Eigenschaften** für die Art der Personalisierung und **inbound_flow_response** für das angepasste Attribut. Damit können Sie Informationen in Nutzerprofilen speichern, in Nachrichten einfügen oder an andere Dienste, z.B. Webhooks, weiterleiten.

![WhatsApp Nachrichten-Editor mit einer Komponente "Personalisierung hinzufügen" zum Einfügen einer Personalisierung von WhatsApp Eigenschaften mit dem angepassten Attribut inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Wenn Sie Fragen haben oder weitere Hilfe benötigen, wenden Sie sich bitte an den [Support]({{site.baseurl}}/braze_support/).