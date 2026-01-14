---
nav_title: Race-Conditions
article_title: Rennbedingungen
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Dieser Artikel beschreibt bewährte Praktiken, um zu vermeiden, dass Race-Conditions Ihre Messaging-Kampagnen beeinträchtigen."
toc_headers: h2
---

# Race-Conditions

> Eine Race-Condition tritt auf, wenn ein Ergebnis von der Abfolge oder dem Zeitpunkt mehrerer Ereignisse abhängt. Wenn zum Beispiel die gewünschte Reihenfolge der Ereignisse "Ereignis A" und dann "Ereignis B" ist, aber manchmal kommt "Ereignis A" zuerst, und manchmal kommt "Ereignis B" zuerst - das nennt man eine Race-Condition. Dies kann zu unerwarteten Ergebnissen oder Fehlern führen, da diese Ereignisse um den Zugriff auf gemeinsame Ressourcen oder Daten konkurrieren.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

In Braze können Race-Conditions auftreten, wenn mehrere Aktionen gleichzeitig auf der Grundlage von Nutzer:innen-Daten oder Ereignissen ausgelöst werden. Wenn ein Nutzer:innen beispielsweise mehrere Kampagnen triggert (z.B. die Anmeldung für einen Newsletter oder einen Kauf), erhalten sie die Nachrichten möglicherweise nicht in der richtigen Reihenfolge.

## Arten von Race-Conditions

Die häufigsten Race-Conditions können auftreten, wenn Sie Folgendes tun:

- Targeting von neuen Nutzer:innen
- Mehrere API-Endpunkte verwenden
- Passende aktionsbasierte Trigger und Zielgruppen-Filter. 

Ziehen Sie die folgenden Szenarien in Betracht und wenden Sie bewährte Verfahren an, um diese Race-Conditions zu vermeiden.

## Szenario 1: Targeting von neuen Nutzer:innen

In Braze tritt eine der häufigsten Race-Conditions bei Nachrichten auf, die sich an neu erstellte Nutzer:innen richten. Die erwartete Reihenfolge der Ereignisse ist:

1. Ein Benutzer wird erstellt;
2. Derselbe Nutzer:in wird sofort für eine Nachricht angesprochen, führt ein angepasstes Event durch oder protokolliert ein angepasstes Attribut.

In manchen Fällen wird jedoch das zweite Ereignis zuerst ausgelöst. Dies bedeutet, dass eine Nachricht an einen Nutzer:innen gesendet werden soll, der noch nicht existiert. Infolgedessen erhält der Nutzer:in sie nie. Dies gilt auch für Ereignisse oder Attribute, bei denen versucht wird, das Ereignis oder Attribut in einem Nutzerprofil zu protokollieren, das noch nicht erstellt wurde.

### Bewährte Praktiken

#### Verzögerungen einführen

Nachdem ein neuer Nutzer:innen erstellt wurde, können Sie eine Verzögerung hinzufügen, bevor Sie Targeting Kampagnen oder Canvase versenden. Diese Zeitverzögerung erlaubt es, das Nutzerprofil zu erstellen und alle relevanten Attribute zu aktualisieren, die die Berechtigung zum Empfang der Nachricht bestimmen können.

Nachdem sich ein Nutzer:innen für Ihre App registriert hat, können Sie zum Beispiel nach 24 Stunden ein Aktionsangebot versenden. Wenn Sie einen Nutzer:innen anlegen oder ein angepasstes Attribut protokollieren, können Sie auch eine einminütige Verzögerung einfügen, bevor Sie mit Ihrem Prozess fortfahren, um diese Race-Condition zu vermeiden.

Sie können diese Verzögerung auch im [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration) für das spezifische angepasste Event hinzufügen, das einen neuen Nutzer:innen zum Betreten eines Canvas triggert. 

## Szenario 2: Mehrere API-Endpunkte verwenden

{% alert important %}
Wir verwenden asynchrone Verarbeitung, um Geschwindigkeit und Flexibilität zu maximieren. Das bedeutet, wenn API-Aufrufe separat an uns gesendet werden, können wir nicht garantieren, dass sie in der Reihenfolge verarbeitet werden, in der sie gesendet wurden.
{% endalert %}

Es gibt ein paar Szenarien, in denen mehrere API Endpunkte ebenfalls zu dieser Race-Condition führen können, z. B. wenn:

- Verwendung separater API-Endpunkte zum Erstellen von Benutzern und Auslösen von Canvases oder Kampagnen
- Mehrere separate Aufrufe des Endpunkts `/users/track`, um angepasste Attribute, Events oder Käufe zu aktualisieren

Wenn Nutzer:innen Informationen über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track) an Braze senden, kann es gelegentlich ein paar Sekunden dauern, bis sie verarbeitet werden. Das bedeutet, dass es bei gleichzeitigen Anfragen an die Endpunkte `/users/track` und Messaging wie `/campaign/trigger/send` keine Garantie dafür gibt, dass die Nutzer:innen aktualisiert werden, bevor eine Nachricht gesendet wird.

{% alert note %}
Wenn Nutzerattribute und Events in derselben Anfrage gesendet werden (entweder von `/users/track` oder vom SDK), dann verarbeitet Braze die Attribute vor den Events oder vor dem Versuch, eine Nachricht zu senden.
{% endalert %}

### Bewährte Praktiken

#### Wenn Sie mehrere Endpunkte verwenden, senden Sie Ihre Anfragen nacheinander

Wenn Sie mehrere Endpunkte verwenden, können Sie versuchen, Ihre Anfragen so zu staffeln, dass jede Anfrage abgeschlossen ist, bevor die nächste beginnt. Dies kann die Wahrscheinlichkeit einer Race-Condition verringern. Wenn Sie z.B. Nutzerattribute aktualisieren und eine Nachricht senden müssen, warten Sie zunächst, bis das Nutzerprofil vollständig aktualisiert ist, bevor Sie eine Nachricht über einen Endpunkt senden.

Wenn Sie eine API-Anfrage für geplante Nachrichten senden, müssen diese Anfragen getrennt sein und ein Nutzer:innen muss erstellt werden, bevor Sie die geplante API-Anfrage senden.

#### Schlüsseldaten mit dem Trigger einbeziehen

Anstatt mehrere Endpunkte zu verwenden, können Sie die [Nutzer:innen-Attribute]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) und [triggernden Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object) in einem einzigen API-Aufruf unter Verwendung des [Endpunkts`campaign/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) zusammenfassen. 

Wenn diese Objekte in den Trigger aufgenommen werden, werden die Attribute zuerst verarbeitet, bevor die Nachricht getriggert wird, wodurch mögliche Race-Conditions vermieden werden. Beachten Sie, dass triggernde Eigenschaften das Nutzerprofil nicht aktualisieren, sondern nur im Zusammenhang mit der Nachricht verwendet werden.

#### Verwenden Sie die POST: Tracking von Nutzer:innen (Sync) Endpunkt

Verwenden Sie den [Endpunkt`/users/track/sync/` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous), um angepasste Events und Käufe aufzuzeichnen und die Attribute des Nutzerprofils synchron zu aktualisieren. Wenn Sie diesen Endpunkt verwenden, um Nutzerprofile gleichzeitig und in einem einzigen Aufruf zu aktualisieren, können Sie mögliche Race-Conditions verhindern.

{% alert important %}
Dieser Endpunkt befindet sich derzeit in der Beta-Phase. Wenden Sie sich an Ihren Braze-Konto Manager:in, wenn Sie an einer Teilnahme an der Beta interessiert sind.
{% endalert %}

## Szenario 3: Abgleich von aktionsbasierten Triggern und Zielgruppenfiltern

Eine weitere häufige Race Condition kann auftreten, wenn Sie eine aktionsbasierte Kampagne oder ein Canvas mit demselben Auslöser wie der Zielgruppenfilter konfigurieren (z. B. ein geändertes Attribut oder die Durchführung eines benutzerdefinierten Ereignisses). Es kann sein, dass der Nutzer:innen zum Zeitpunkt des Auslösens des Ereignisses nicht in der Zielgruppe ist. Das bedeutet, dass er die Kampagne nicht erhält und auch nicht in den Canvas gelangt.

### Bewährte Praktiken

#### Prüfen Sie Ihre Zielgruppe nach einer Verzögerung

Um die Verwendung von Zielgruppen-Filtern zu vermeiden, die die Trigger-Kriterien enthalten, empfehlen wir, Ihre Zielgruppe vor der Zustellung zu überprüfen. So können Sie beispielsweise [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#edit-delivery-settings) in Canvas-Schritten für Nachrichten als zusätzliche Prüfung verwenden, um zu bestätigen, dass Ihre Zielgruppe die Zustellungskriterien beim Senden der Nachricht erfüllt. Sie können auch Ausstiegskriterien für Canvas nutzen, um Nutzer:innen zu einem beliebigen Zeitpunkt während der User Journey aussteigen zu lassen, wenn sie Ihre Kriterien erfüllen.

Für Kampagnen können Sie Exit-Ereignisse verwenden, um zu ermöglichen, dass Kampagnen mit einem triggernden Ereignis Nachrichten an Nutzer:innen abbrechen, die das Exit-Ereignis während der Verzögerung ausführen.

#### Verwenden Sie eindeutige Filter mit dem auslösenden Ereignis

Wenn Sie Ihre Filter konfigurieren, möchten Sie vielleicht einen redundanten Filter "für den Fall der Fälle" hinzufügen. Diese Redundanz kann jedoch zu weiteren Problemen führen. Vermeiden Sie stattdessen nach Möglichkeit die Verwendung von Filtern, die den Trigger enthalten. Dies ist der sicherste Weg, um eine Race-Condition zu vermeiden.

Wenn der Trigger Ihrer Kampagne beispielsweise "Hat einen Kauf getätigt" lautet und Ihr Zielgruppen-Filter "Hat irgendeinen Kauf getätigt", kann diese Redundanz eine Race-Condition verursachen. 

#### Vermeiden Sie Zielgruppen-Filter, die davon ausgehen, dass das auslösende Ereignis aktualisiert wurde.

Diese bewährte Methode ähnelt der Vermeidung von redundanten Filtern mit dem Trigger-Ereignis. Normalerweise schlägt ein Filter, der davon ausgeht, dass das triggernde Ereignis im Nutzerprofil aktualisiert wurde, fehl.

#### Liquid verwenden Abbrüche (nur Attribute)

Verwenden Sie in Kampagnen und Canvas-Schritten Liquid-Abbrüche, um die Verwendung von Zielgruppen-Filtern zu vermeiden, die die triggernden Attribute im Zeitplan der Eingabe enthalten. Nehmen wir an, Sie haben ein Array-Attribut "Lieblingsfarben" und möchten alle Nutzer:innen ansprechen, die das Attribut-Array mit einem beliebigen Wert aktualisieren und nach Abschluss des Updates auch die Farbe "blau" im Array haben. Wenn Sie die Zielgruppen-Filter in diesem Beispiel verwenden, tritt eine Race-Condition auf und Sie verpassen Nutzer:innen, die zum ersten Mal "blau" in das Array eingeben.

In diesem Fall können Sie eine Trigger-Verzögerung in einer Kampagne implementieren oder einen Delay-Schritt in Canvas verwenden, um das Update des Nutzerprofils für eine gewisse Zeit zuzulassen, und dann die folgende Liquid-Abbruchlogik verwenden:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Bestätigen Sie, wie die Nutzerdaten verwaltet werden

Wenn eine Race-Condition bei der Auswertung des Canvas-Eingangs auftritt, können Nutzer:innen einen Canvas betreten, den sie eigentlich nicht betreten sollten. Das Profil des Nutzers könnte beispielsweise so eingestellt werden, dass es in die Zielgruppe aufgenommen wird, und anschließend aktualisiert werden, nachdem der Canvas die Nutzer:innen in die Warteschlange gestellt hat, damit sie nicht mehr für die Zielgruppe in Frage kommen. 

Wir empfehlen Ihnen, sich zu vergewissern, wie Nutzerdaten verwaltet und aktualisiert werden, insbesondere wann und wie bestimmte Attribute aktualisiert werden, z.B. über SDK, API, Batch-API und andere Methoden. Dies kann dabei helfen, zu erkennen und zu klären, warum ein Nutzer:innen eine Kampagne oder ein Canvas betreten hat und wann das Profil des Nutzers aktualisiert wurde.
