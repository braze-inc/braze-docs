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

> Mit Nachrichtenschritten können Sie eine eigenständige Nachricht an der gewünschten Stelle in Ihrem Canvas Flow hinzufügen.

![][1]{: style="float:right;max-width:25%;margin-left:15px;"}

## Eine Nachricht erstellen

Um eine Nachricht-Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente aus der Seitenleiste oder klicken Sie auf die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> am unteren Rand eines Schritts und wählen Sie **Nachricht**. 

### Nachrichten einrichten

Alle Nutzer:innen, die den Schritt „Nachricht“ eingeben, werden zum nächsten Schritt vorgebracht, wenn eine der folgenden Bedingungen erfüllt ist:
- Beliebige Nachricht wird gesendet
- Eine Nachricht wird in der Frequenz begrenzt und nicht gesendet
- Eine Nachricht wird abgebrochen
- Ein Benutzer ist über den Kanal nicht erreichbar, also wird die Nachricht nicht gesendet

![Richten Sie die Messaging-Einstellungen für den Schritt „Nachricht“ ein, der die Option enthält, Ihren Messaging-Kanal auszuwählen und die Zustellung anzupassen.][2]{: style="max-width:75%;"}

{% raw %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende SMS-Nachricht ausgelöst wird, können Sie im ersten Schritt (Nachrichtenschritt) oder in einem Nachrichtenschritt, der unter einem Aktionspfadschritt verschachtelt ist, auf SMS-Eigenschaften verweisen. Im Schritt „Nachricht“ können Sie zum Beispiel `{{sms.${inbound_message_body}}}` oder `{{sms.${inbound_media_urls}}}` verwenden.
{% endraw %}

### Zustellungseinstellungen bearbeiten

Die Komponente Nachrichten enthält außerdem Einstellungen für die intelligente Zustellung, die Überschreitung der Ruhezeiten und die Zustellungsprüfung. Sie können die [intelligente Zeitmessung]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) mit einer Ausweichoption aktivieren, wenn das Profil eines Benutzers nicht über genügend Daten verfügt, um eine optimale Zeit zu berechnen. Wir empfehlen die Aktivierung von Intelligent Timing und [Ratenbegrenzung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) als zusätzliche Kontrolle für eventuelle Verzögerungen zwischen der Eingabe des Schritts Nachricht und dem tatsächlichen Versand der Nachricht.

Wählen Sie **Intelligentes Timing verwenden** auf der Registerkarte **Zustellungseinstellungen**. Hier können Sie entweder die beliebteste Zeit oder eine bestimmte Ausweichzeit auswählen. Wenn Ruhezeiten aktiviert sind, können Sie diese Einstellung im Schritt „Nachricht“ auch außer Kraft setzen.

Zustellungsvalidierungen bieten eine zusätzliche Prüfung, um zu bestätigen, dass Ihre Zielgruppe die Zustellungskriterien beim Senden von Nachrichten erfüllt. Diese Einstellung wird empfohlen, wenn Stille Stunden, Intelligentes Timing oder Ratenbegrenzung aktiviert sind. Sie können ein Segment oder zusätzliche Filter hinzufügen, die zum Zeitpunkt des Versands der Nachricht überprüft werden. Wenn ein:e Nutzer:in die festgelegten Zustellungsvalidierungen für einen Messaging-Schritt nicht erfüllt, verlässt er den Canvas bei diesem Schritt.

![Der Tab „Zustellungseinstellungen“ für die Einstellungen der Komponente „Nachrichten“. Ruhezeiten sind aktiviert, und das Kontrollkästchen „Intelligentes Timing verwenden“ ist ausgewählt, um die Nachricht zu einem optimalen Zeitpunkt zuzustellen. Zustellungsvalidierungen sind aktiviert, um die Zielgruppen beim Senden von Nachrichten zu validieren.][4]{: style="max-width:80%;"}

### Eigenschaften der Leinwandeinträge

Die Canvas-Eingabeeigenschaften werden im Schritt Eingabezeitplan bei der Erstellung eines Canvas konfiguriert und geben den Auslöser an, der einen Benutzer in ein Canvas eintreten lässt. Diese Eigenschaften können auch auf die Eigenschaften von Eingabe-Nutzdaten in API-ausgelösten Canvases zugreifen. Beachten Sie, dass für das Objekt `canvas_entry_properties` eine maximale Größe von 50 KB gilt. 

{% alert note %}
Speziell für In-App-Nachricht-Kanäle kann `canvas_entry_properties` nur dann in Canvas Flow und im ursprünglichen Canvas-Editor referenziert werden, wenn Sie persistente Entry-Eigenschaften im ursprünglichen Editor als Teil des früheren Early Access aktiviert haben.
{% endalert %}

#### Canvas Flow

Für Canvas Flow-Nachrichten können die Eingabeeigenschaften in Liquid in jedem Nachrichtenschritt verwendet werden. Verwenden Sie das folgende Liquid, wenn Sie auf diese Entry-Eigenschaften verweisen: {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise verwendet werden zu können.

Verwenden Sie das folgende Liquid, wenn Sie auf diese Entry-Eigenschaften verweisen: {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Beachten Sie, dass es sich bei den Events um angepasste Events oder Kauf-Events handeln muss, um auf diese Weise verwendet werden zu können.

{% raw %}
Nehmen wir zum Beispiel die folgende Anfrage: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Sie können einer Nachricht mit dem Liquid `{{canvas_entry_properties.${product_name}}}` das Wort „Schuhe“ hinzufügen.
{% endraw %}

Sie können auch [persistente Entry-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) in jedem Nachrichten-Schritt nutzen, um Ihre Nutzer:innen durch personalisierte Schritte in Ihrem Canvas-Workflow zu führen.

#### Ursprünglicher Workflow

Bei den mit dem Original-Editor erstellten Canvases kann `canvas_entry_properties` nur im ersten vollständigen Schritt eines Canvas referenziert werden.

### Event-Eigenschaften

Event-Eigenschaften referenzieren auf die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können sowohl in Kampagnen mit aktionsbasierter Zustellung als auch in Canvase verwendet werden. 

#### Canvas Flow

In Canvas Flow können angepasste Event- und Kauf-Event-Eigenschaften in Liquid in jedem Nachrichten-Schritt verwendet werden, der auf einen [Aktionspfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)-Schritt folgt. Verwenden Sie für Canvas Flow dieses Liquid `` {% raw %} {{event_properties.${property_name}}} {% endraw %}``, wenn Sie auf diese `event_properties` verweisen. Diese Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise in der Komponente „Nachricht“ verwendet werden zu können.

{% alert important %}
`event_properties` kann nicht unabhängig von Aktionspfaden für Canvas Flow verwendet werden.
{% endalert %}

Im ersten Nachrichten-Schritt, der einem Aktionspfad folgt, können Sie `event_properties` verwenden, das sich auf das Event bezieht, das in diesem Aktionspfad referenziert wird. Zwischen dem Schritt „Aktionspfade“ und dem Schritt „Nachricht“ können weitere Schritte liegen (die keine anderen Aktionspfade oder Nachrichten sind). Beachten Sie, dass Sie nur dann auf `event_properties` zugreifen können, wenn Ihr Schritt „Nachricht“ auf einen Nicht-Alle-anderen-Pfad in einem Aktionspfad-Schritt zurückverfolgt werden kann.

#### Ursprünglicher Workflow

`event_properties` kann im ersten vollständigen Schritt in einem aktionsbasierten Canvas unter Verwendung des ursprünglichen Workflows verwendet werden, auch wenn der vollständige Schritt geplant ist. 

{% alert important %}
Für Canvas Flow und den Original-Editor können Sie `event_properties` im Hauptschritt „Nachricht“ nicht verwendet. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen Aktionspfad-Schritt mit dem entsprechenden Event vor dem Schritt „Nachricht“ hinzufügen, der `event_properties` enthält.
{% endalert %}

Weitere Informationen und Beispiele finden Sie unter [Canvas-Eingabeeigenschaften und Ereigniseigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).


## Analytics

In der folgenden Tabelle finden Sie die Definitionen der Metriken der Nachrichtenkomponente: 

| Metrisch | Beschreibung |
| --- | --- |
| Entrys | Die Anzahl, wie oft der Schritt aufgerufen wurde. Wenn Ihr Canvas eine Wiederholungsberechtigung hat und ein:e Nutzer:in einen Nachrichten-Schritt zweimal eingibt, werden zwei Entrys aufgezeichnet. |
| Fortgefahren mit nächstem Schritt | Die Anzahl der Entrys, die zum nächsten Schritt im Canvas weitergeleitet wurden. |
| Sendungen | Die Gesamtzahl der Nachrichten, die der Schritt gesendet hat. Wenn Ihr Canvas wieder freigegeben wird und ein:e Nutzer:in einen Messaging-Schritt zweimal eingibt, werden zwei Entrys aufgezeichnet. |
| Eindeutige Empfänger:innen | Die Anzahl der Benutzer, die Nachrichten aus diesem Schritt erhalten haben. |
| Primäres Konversions-Event | Die Anzahl, wie oft ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Kampagne aufgetreten ist. Sie definieren dieses Event, wenn Sie die Kampagne erstellen. |
| Umsatz | Der Gesamtumsatz in Dollar von Kampagnenempfängern innerhalb des festgelegten primären Umrechnungsfensters. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]{: style="max-width:20%;"}


[1]: {% image_buster /assets/img/canvas_components/message_step1.png %}
[2]: {% image_buster /assets/img/canvas_components/message_step2.png %}
[3]: {% image_buster /assets/img/canvas_components/message_step3.png %}
[4]: {% image_buster /assets/img/canvas_components/message_step4.png %}
