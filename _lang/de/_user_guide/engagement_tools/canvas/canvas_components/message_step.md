---
nav_title: Nachricht 
article_title: Nachricht 
alias: "/message_step/"
page_order: 5
page_type: reference
description: "In diesem Referenzartikel wird erläutert, wie Sie mit dem Schritt „Nachricht“ eine eigenständige Nachricht erstellen."
tool: Canvas

---

# Nachricht 

> Mit den Messaging-Schritten können Sie an jeder beliebigen Stelle in Ihrem Canvas eine eigenständige Nachricht hinzufügen.

![Ein Nachrichten-Schritt mit dem Namen "Mittags-Promo" über den Push-Kanal.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Erstellen einer Nachricht

Um eine Nachricht-Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> plus Button am Ende eines Schrittes und wählen Sie **Nachricht**. 

### Schritt 1: Wählen Sie Ihren Messaging-Kanal aus

Sie können aus den folgenden Messaging-Kanälen auswählen: 
- Content-Cards
- E-Mail
- LINE
- Push-Benachrichtigungen
- SMS/MMS/RCS
- In-App-Nachrichten 
- Webhook
- WhatsApp

![Eine Liste der verfügbaren Messaging-Kanäle, die Sie für den Schritt Nachricht auswählen können.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Schritt 2: Zustellungseinstellungen bearbeiten

Als nächstes können Sie die Einstellungen für die Intelligente Zustellung, die Überschreitung der Ruhezeiten und die Zustellungsvalidierung bearbeiten.

#### Intelligentes Timing

Sie können die [intelligente Zeitmessung]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) mit einer Ausweichoption aktivieren, wenn das Profil eines Benutzers nicht über genügend Daten verfügt, um eine optimale Zeit zu berechnen. Wir empfehlen die Aktivierung von Intelligent Timing und [Ratenbegrenzung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) als zusätzliche Kontrolle für eventuelle Verzögerungen zwischen der Eingabe des Schritts Nachricht und dem tatsächlichen Versand der Nachricht.

Wählen Sie **Intelligentes Timing verwenden** auf der Registerkarte **Zustellungseinstellungen**. Hier können Sie entweder die beliebteste Zeit oder eine bestimmte Ausweichzeit auswählen. Wenn Ruhezeiten aktiviert sind, können Sie diese Einstellung im Schritt „Nachricht“ auch außer Kraft setzen.

#### Zustellungsvalidierungen

Zustellungsvalidierungen bieten eine zusätzliche Prüfung, um zu bestätigen, dass Ihre Zielgruppe die Zustellungskriterien beim Senden von Nachrichten erfüllt. Diese Einstellung wird empfohlen, wenn Stille Stunden, Intelligentes Timing oder Ratenbegrenzung aktiviert sind. Sie können ein Segment oder zusätzliche Filter hinzufügen, die zum Zeitpunkt des Versands der Nachricht überprüft werden. Wenn ein:e Nutzer:in die festgelegten Zustellungsvalidierungen für einen Messaging-Schritt nicht erfüllt, verlässt er den Canvas bei diesem Schritt.

![Der Tab Zustellungseinstellungen für die Einstellungen der Komponente Nachrichten. Ruhezeiten sind aktiviert, und das Kontrollkästchen „Intelligentes Timing verwenden“ ist ausgewählt, um die Nachricht zu einem optimalen Zeitpunkt zuzustellen. Zustellungsvalidierungen sind aktiviert, um die Zielgruppen beim Senden von Nachrichten zu validieren.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

## Wie Nutzer:innen den Fortschritt voranbringen

Alle Nutzer:innen, die den Schritt „Nachricht“ eingeben, werden zum nächsten Schritt vorgebracht, wenn eine der folgenden Bedingungen erfüllt ist:

- Beliebige Nachricht wird gesendet
- Eine Nachricht wird in der Frequenz begrenzt und nicht gesendet
- Eine Nachricht wird abgebrochen
- Ein Benutzer ist über den Kanal nicht erreichbar, also wird die Nachricht nicht gesendet

{% raw %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende SMS-Nachricht ausgelöst wird, können Sie im ersten Schritt (Nachrichtenschritt) oder in einem Nachrichtenschritt, der unter einem Aktionspfadschritt verschachtelt ist, auf SMS-Eigenschaften verweisen. Im Schritt „Nachricht“ können Sie zum Beispiel `{{sms.${inbound_message_body}}}` oder `{{sms.${inbound_media_urls}}}` verwenden.
{% endraw %}

## Referenzieren von Canvas-Eingängen Eigenschaften

Die Eingangs-Eigenschaften eines Canvas werden im **Zeitplan-Schritt** der Erstellung eines Canvas konfiguriert und geben den Auslöser an, der einen Nutzer:innen in ein Canvas bringt. Diese Eigenschaften können auch auf die Eigenschaften von Eingabe-Nutzdaten in API-ausgelösten Canvases zugreifen. Beachten Sie, dass das Objekt `canvas_entry_properties` maximal 50 KB groß sein darf. 

Eingangs-Eigenschaften können in Liquid in jedem Schritt von Messaging verwendet werden. Verwenden Sie das folgende Liquid, wenn Sie auf diese Eingangs-Eigenschaften verweisen: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise verwendet werden zu können.

{% alert note %}
Speziell für In-App-Nachricht-Kanäle gilt: `canvas_entry_properties` kann nur in Canvas referenziert werden.
{% endalert %}

Verwenden Sie das folgende Liquid, wenn Sie auf diese Eingangs-Eigenschaften verweisen: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Beachten Sie, dass es sich bei den Events um angepasste Events oder Kauf-Events handeln muss, um auf diese Weise verwendet werden zu können.

{% raw %}
Nehmen wir zum Beispiel die folgende Anfrage: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Sie können einer Nachricht mit dem Liquid `{{canvas_entry_properties.${product_name}}}` das Wort „Schuhe“ hinzufügen.
{% endraw %}

Sie können auch [persistente Entry-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) in jedem Nachrichten-Schritt nutzen, um Ihre Nutzer:innen durch personalisierte Schritte in Ihrem Canvas-Workflow zu führen.

### Event-Eigenschaften

Event-Eigenschaften referenzieren auf die Eigenschaften, die Sie für angepasste Events und Kauf-Events festlegen. Diese Event-Eigenschaften können sowohl in Kampagnen mit aktionsbasierter Zustellung als auch in Canvase verwendet werden. 

In Canvas können angepasste Event- und Kauf-Event-Eigenschaften in Liquid in jedem Nachrichten-Schritt verwendet werden, der auf einen [Aktions-Pfad-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) folgt. Wenn Sie zum Beispiel auf `event_properties` verweisen, verwenden Sie dieses Liquid Snippet: {% raw %}``{{event_properties.${property_name}}}``{% endraw %} 

{% alert important %}
`event_properties` kann nicht unabhängig von Aktions-Pfade-Schritten verwendet werden.
{% endalert %}

Im ersten Nachrichten-Schritt, der einem Aktionspfad folgt, können Sie `event_properties` verwenden, das sich auf das Event bezieht, das in diesem Aktionspfad referenziert wird. Zwischen dem Schritt „Aktionspfade“ und dem Schritt „Nachricht“ können weitere Schritte liegen (die keine anderen Aktionspfade oder Nachrichten sind). Beachten Sie, dass Sie nur dann auf `event_properties` zugreifen können, wenn Ihr Schritt „Nachricht“ auf einen Nicht-Alle-anderen-Pfad in einem Aktionspfad-Schritt zurückverfolgt werden kann.

{% alert important %}
Sie können `event_properties` nicht für den Lead-Nachrichtenschritt verwenden. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen Aktionspfad-Schritt mit dem entsprechenden Event vor dem Schritt „Nachricht“ hinzufügen, der `event_properties` enthält.
{% endalert %}

{% details Expand for original Canvas editor %}

Sie können Canvase nicht mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt ist nur zum Referenzieren verfügbar.

- `event_properties` kann nicht in geplanten Vollschritten verwendet werden. Sie können jedoch `event_properties` im ersten vollständigen Schritt aktionsbasierter Canvase verwenden, auch wenn ein vollständiger Schritt geplant ist.
- `canvas_entry_properties` kann nur im ersten vollständigen Schritt eines Canvas referenziert werden.
- Speziell für In-App-Nachricht-Kanäle kann `canvas_entry_properties` im ursprünglichen Canvas-Editor referenziert werden, wenn Sie die persistenten Eingangs-Eigenschaften im Rahmen des früheren Early Access aktiviert haben.

{% enddetails %}

## Analytics

In der folgenden Tabelle finden Sie die Definitionen der Metriken der Nachrichtenkomponente: 

| Metrisch | Beschreibung |
| --- | --- |
| _Entrys_ | Die Anzahl, wie oft der Schritt aufgerufen wurde. Wenn Ihr Canvas eine Wiederholungsberechtigung hat und ein:e Nutzer:in einen Nachrichten-Schritt zweimal eingibt, werden zwei Entrys aufgezeichnet. |
| _Fortgefahren mit nächstem Schritt_ | Die Anzahl der Entrys, die zum nächsten Schritt im Canvas weitergeleitet wurden. |
| _Sendungen_ | Die Gesamtzahl der Nachrichten, die der Schritt gesendet hat. Wenn Ihr Canvas wieder freigegeben wird und ein:e Nutzer:in einen Messaging-Schritt zweimal eingibt, werden zwei Entrys aufgezeichnet. |
| _Eindeutige Empfänger:innen_ | Die Anzahl der Benutzer, die Nachrichten aus diesem Schritt erhalten haben. |
| _Primäres Konversions-Event_ | Die Anzahl, wie oft ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Kampagne aufgetreten ist. Sie definieren dieses Event, wenn Sie die Kampagne erstellen. |
| _Umsatz_ | Der Gesamtumsatz in Dollar von Kampagnenempfängern innerhalb des festgelegten primären Umrechnungsfensters. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


