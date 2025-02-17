---
nav_title: Rennbedingungen
article_title: Rennbedingungen
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Dieser Artikel beschreibt bewährte Praktiken, um zu vermeiden, dass Race-Conditions Ihre Messaging-Kampagnen beeinträchtigen."

---

# Race-Conditions

> Eine Race Condition ist ein Konzept, bei dem ein Ergebnis von der Abfolge oder dem Timing anderer Ereignisse abhängig ist. 

Wenn zum Beispiel die gewünschte Reihenfolge der Ereignisse "Ereignis A" und dann "Ereignis B" ist, aber manchmal kommt "Ereignis A" zuerst und manchmal kommt "Ereignis B" zuerst - das nennt man eine Race Condition.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

## Targeting von neuen Nutzer:innen

In Braze tritt eine der häufigsten Race-Conditions bei Nachrichten auf, die sich an neu erstellte Nutzer:innen richten. Hier ist die erwartete Reihenfolge der Ereignisse:

1. Ein Benutzer wird erstellt;
2. Derselbe Nutzer:in wird sofort für eine Nachricht angesprochen, führt ein angepasstes Event durch oder protokolliert ein angepasstes Attribut.

In manchen Fällen wird jedoch das zweite Ereignis zuerst ausgelöst. Dies bedeutet, dass versucht wird, eine Nachricht an eine:n Nutzer:in zu senden, der noch nicht erstellt wurde. Infolgedessen erhält die:der Nutzer:in die Nachricht nie. Dasselbe gilt für Events oder Attribute, bei denen versucht wird, das Event oder Attribut in einem Nutzerprofil zu protokollieren, das noch nicht existiert.

## Mehrere API-Endpunkte verwenden

Es gibt ein paar Szenarien, in denen mehrere API Endpunkte ebenfalls zu dieser Race-Condition führen können, z. B. wenn:

- Verwendung separater API-Endpunkte zum Erstellen von Benutzern und Auslösen von Canvases oder Kampagnen
- Mehrere separate Aufrufe des Endpunkts `/users/track`, um angepasste Attribute, Events oder Käufe zu aktualisieren

Wenn Nutzer:innen Informationen über den Endpunkt `/users/track` an Braze senden, kann es gelegentlich ein paar Sekunden dauern, bis sie verarbeitet werden. Wenn also gleichzeitig Anfragen an `/users/track` und die [Messaging-Endpunkte][4] gestellt werden, gibt es derzeit keine Garantie, dass die Benutzerinformationen aktualisiert werden, bevor eine Nachricht gesendet wird.

Wenn diese Anfragen in der gleichen API-Anfrage gestellt werden, gibt es in beiden Fällen keine Probleme.

{% alert note %}
Wenn Nutzerattribute und Events in derselben Anfrage gesendet werden (entweder von `/users/track` oder vom SDK), dann verarbeitet Braze die Attribute vor den Events oder vor dem Versuch, eine Nachricht zu senden.
{% endalert %}

Beachten Sie, dass, wenn Sie eine API-Anfrage für geplante Nachrichten senden, diese Anfragen getrennt sein müssen und ein:e Nutzer:in erstellt werden muss, bevor Sie die geplante API-Anfrage senden.

### Vermeiden der Race-Condition

Eine Möglichkeit, diese Race-Condition zu vermeiden, besteht darin, eine Verzögerung - etwa eine Minute - zwischen der Erstellung und dem Targeting einer Nutzerin oder eines Nutzers durch Ihr Canvas oder Ihre Kampagne oder dem Versuch, ein Attribut oder Event für dieses Nutzerprofil zu protokollieren, einzufügen.

In ähnlicher Weise können Sie das [`Attributes`][1] Objekt verwenden, um einen Benutzer hinzuzufügen, zu erstellen oder zu aktualisieren, und ihn dann entweder über den [`/canvas/trigger/send` Endpunkt][2] oder den [`/campaign/trigger/send` Endpunkt][3] ansprechen. Diese API-Anfrage verarbeitet das Objekt `attributes` vor dem Targeting der Nutzer:innen.

Attribute, die in diesem Objekt enthalten sind, werden verarbeitet, bevor Braze beginnt, die Kampagne zu versenden. Wenn das Kennzeichen `send_to_existing_only` auf false gesetzt ist und ein `external_user_id` in der Braze-Datenbank nicht existiert, erstellen wir ein Benutzerprofil für das `external_user_id` und verarbeiten die zugehörigen Attribute im Benutzerprofil, bevor Braze mit dem Versand der Kampagne beginnt. Beachten Sie auch, dass, wenn das `send_to_existing_only`-Flag auf false gesetzt ist, das Attribute-Objekt enthalten sein muss, um die:den Nutzer:in zu erstellen. Das Flag `send_to_existing_only` kann nicht mit Benutzer-Aliasen verwendet werden.

## Abgleich von aktionsbasierten Triggern und Zielgruppenfiltern

Eine weitere häufige Race Condition kann auftreten, wenn Sie eine aktionsbasierte Kampagne oder ein Canvas mit demselben Auslöser wie der Zielgruppenfilter konfigurieren (z. B. ein geändertes Attribut oder die Durchführung eines benutzerdefinierten Ereignisses). Der Benutzer befindet sich möglicherweise nicht in der Zielgruppe, wenn er das Trigger-Ereignis ausführt. Das bedeutet, dass er die Kampagne nicht erhält oder den Canvas nicht betritt. In diesem Fall empfiehlt Braze Ihnen, Ihren Trigger nicht so zu konfigurieren, dass er mit Ihrem Zielgruppenfilter übereinstimmt. 

### Vermeiden der Race-Condition

Eine Möglichkeit, diese Race-Condition zu vermeiden, besteht darin, eine Verzögerung von mehr als einer Minute hinzuzufügen, damit die Nutzer:innen genügend Zeit haben, den Canvas zu betreten.

[1]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[3]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
