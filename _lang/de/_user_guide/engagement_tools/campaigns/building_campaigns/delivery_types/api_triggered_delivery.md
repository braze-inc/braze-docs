---
nav_title: API-getriggerte Zustellung
article_title: API-getriggerte Zustellung
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie eine API-getriggerte Kampagne planen und einrichten."
tool: Campaigns
platform: API

---

# API-getriggerte Zustellung

> API-getriggerte Kampagnen oder Server-getriggerte Kampagnen sind ideal für fortgeschrittene transaktionale Anwendungsfälle. Mit den API-getriggerten Kampagnen von Braze können Marketingexperten Kampagnentexte, multivariate Tests und Regeln für die Wiederzulassung im Braze-Dashboard verwalten und gleichzeitig die Zustellung dieser Inhalte über ihre eigenen Server und Systeme triggern. Die API-Anfrage zum Triggern der Nachricht kann auch zusätzliche Daten enthalten, die in Echtzeit in die Nachricht eingefügt werden.

## Einrichten einer API-gesteuerten Kampagne

Die Einrichtung einer API-gesteuerten Kampagne erfordert nur wenige Schritte. Erstellen Sie zunächst eine neue Multichannel- oder Singlechannel-Kampagne (mit multivariaten Tests).

{% alert note %}
Eine API-ausgelöste Kampagne unterscheidet sich von einer [API-Kampagne]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Als Nächstes konfigurieren Sie Ihr Exemplar und die Benachrichtigungen auf dieselbe Weise, wie Sie es normalerweise für geplante Benachrichtigungen tun würden, und wählen Sie **API-gesteuerte Zustellung**. Weitere Informationen zum Auslösen dieser Kampagnen von Ihrem Server aus finden Sie in diesem Artikel [über das Senden von API-gesteuerten Kampagnen]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

![][37]

## Verwendung der in einer API-Anfrage enthaltenen Inhaltsvorlage

Zusätzlich zum Triggern der Nachricht können Sie auch Inhalte mit der API-Anfrage in die Nachricht innerhalb des `trigger_properties` Objekts einfügen, die als Template dienen sollen. Auf diesen Inhalt kann im Hauptteil der Nachricht verwiesen werden. Zum Beispiel können Sie Folgendes hinzufügen:
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``. Weitere Informationen finden Sie im folgenden Beispiel für eine Benachrichtigung in den sozialen Medien:

![Die oben erwähnte Trigger-Eigenschaft, die in der Nachricht enthalten ist, füllt automatisch den Namen des Nutzers oder der Nutzerin aus, gefolgt von dem Text: „Ihr Foto hat mir gefallen! Klicken Sie hier, um zu sehen, was sie gemacht haben.“.][38]{: style="max-width:70%;"}

## Erneute Qualifizierung mit API-getriggerten Kampagnen

Die Anzahl, wie oft ein:e Nutzer:in eine über die API getriggerte Kampagne erhält, kann mit den Einstellungen für die erneute Qualifizierung begrenzt werden. Das bedeutet, dass der Benutzer die Kampagne nur einmal oder einmal in einem bestimmten Fenster erhält, unabhängig davon, wie oft der API-Auslöser ausgelöst wird.

Nehmen wir an, Sie verwenden eine API-getriggerte Kampagne, um dem Nutzer oder der Nutzerin eine Kampagne zu einem Artikel zu senden, den er oder sie kürzlich angesehen hat. In diesem Fall können Sie die Kampagne darauf beschränken, maximal eine Nachricht pro Tag zu senden, unabhängig davon, wie viele Artikel sie angesehen haben, während Sie den API-Trigger für jeden Artikel auslösen. Wenn Ihre API-ausgelöste Kampagne hingegen transaktionsabhängig ist, möchten Sie sicherstellen, dass der Benutzer die Kampagne jedes Mal erhält, wenn er die Transaktion durchführt, indem Sie die Verzögerung auf null Minuten einstellen.

![][43]


[37]: {% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %}
[38]: {% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}
[39]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
[42]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery
[43]: {% image_buster /assets/img_archive/api_triggered_reeligible.png %}