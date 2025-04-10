---
nav_title: Fortschrittsverhalten
article_title: Fortschrittsverhalten
page_order: 10
alias: /auto_advance/
page_type: reference
description: "Dieser Referenzartikel beschreibt das Aufstiegsverhalten und behandelt verschiedene Szenarien, die beim Aufstieg in einem Canvas auftreten können."
tool: Canvas

---

# Fortschrittsverhalten

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Diesen Artikel können Sie referenzieren, um zu verstehen, wie Ihre Nutzer:innen die Canvas-Komponenten im Original-Editor voranbringen. <br><br>Für Komponenten in Canvas Flow ist das **Fortschrittsverhalten** so eingestellt, dass die Zielgruppe immer sofort vorangebracht wird, oder **Zielgruppe sofort voranbringen**. Dies gilt auch für [nicht verbundene Schritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#disconnected-steps/).
{% endalert %}

> Mit der Funktion **Beförderungsverhalten** können Sie die Kriterien für die Beförderung durch Ihre [Canvas-Komponente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) festlegen. 

![Einstellungen für das Fortschrittsverhalten mit zwei Optionen, um die Zielgruppe entweder beim Senden der Nachricht voranzubringen oder die Zielgruppe sofort voranzubringen.][1]

Nutzer:innen müssen die Kriterien des Schritts erfüllen, um durch den Schritt vorangebracht zu werden. Mit den [Nachrichtenschritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) können Sie Zustellungsvalidierungen aktivieren, um zu überprüfen, ob Ihre Zielgruppe die Zustellungskriterien beim Senden der Nachricht erfüllt. Dies wird bei der Verwendung von Canvas Flow auf die Kriterien des Schritts angerechnet. Wenn also ein Benutzer die Kriterien für die Überprüfung der Lieferung nicht erfüllt, verlässt er den Canvas.

Wenn **Weiterschalten bei gesendeter Nachricht** ausgewählt ist, werden Benutzer nur dann zu den nachfolgenden Canvas-Schritten weitergeleitet, wenn eine der folgenden Bedingungen eintritt:

- Eine E-Mail-Nachricht wird gesendet
- Eine Push-Nachricht wird gesendet
- Ein Webhook wird gesendet
- Eine In-App-Nachricht wird angezeigt
- Eine Inhaltskarte wird gesendet

Wenn die Option **Publikum sofort weiterleiten** ausgewählt ist, werden Benutzer zu den nachfolgenden Canvas-Schritten weitergeleitet, wenn eine der folgenden Bedingungen eintritt:

- Eine beliebige Nachricht wird gesendet oder die In-App-Nachricht im Schritt wird live.
- Der Webhook wird nicht gesendet, weil der Webhook einen Fehler oder Fehler verursacht
- Keine Push-Benachrichtigung oder E-Mail gesendet, da Nutzer:in nicht per Push oder E-Mail erreichbar ist.
- Es wird versucht, eine Content-Card zu senden 
- Eine Karte wird abgebrochen und nicht gesendet
- Eine Nachricht wurde wegen Frequency-Capping nicht gesendet.
- Sendevorgang einer Nachricht wurde abgebrochen und die Nachricht wurde nicht gesendet.

### Geplante Schritte

Bei einer Zeitplan-Komponente müssen Nutzer:innen die Zielgruppen-Optionen für den Schritt erfüllen, um durch den Schritt vorangebracht zu werden. Wenn der Schritt ein [Ausnahme-Event]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) hat, werden Nutzer:innen, die das Ausnahme-Event ausführen, nicht durch den Schritt vorangebracht.

Wenn wir eine Multikanal-Komponente mit [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) versenden, senden wir möglicherweise Nachrichten zu unterschiedlichen Zeiten für verschiedene Kanäle oder versuchen, sie zu senden. Braze bringt Nutzer:innen automatisch zu dem Zeitpunkt voran, an dem die erste Nachricht in einer Komponente zu senden versucht wird.

### Aktionsbasierte Schritte

Bei aktionsbasierten Schritten müssen Nutzer:innen die Aktion triggern und die Zielgruppenoptionen erfüllen, um den Schritt voranbringen zu können. Wenn der Schritt ein Ausnahme-Event hat, werden Nutzer:innen, die das Ausnahme-Event ausführen, nicht durch den Schritt vorangebracht.

{% alert important %}
Nutzer:innen, die einen Schritt voranbringen, ohne Nachrichten zu erhalten, werden nicht als eindeutige Empfänger:innen für diesen Schritt gezählt. Nutzer:innen müssen eine oder mehrere Nachrichten von einem Schritt erhalten, um als eindeutige Empfänger:in gezählt zu werden.
{% endalert %}

## Anwendungsfall

Das Voranbringen von Fortschritten funktioniert gut, wenn die nachfolgenden Nachrichten auf die vorherigen Nachrichten Bezug nehmen. Sie möchten zum Beispiel keinen Push über eine E-Mail senden, die nie an Nutzer:innen gesendet wurde.

Es kann vorkommen, dass Sie möchten, dass Nutzer:innen auch dann durch einen Canvas vorangebracht werden, wenn sie eine bestimmte Nachricht nicht erhalten haben. Sie könnten z. B. einen "Willkommen"-Push an Tag 3 und eine "Willkommen"-E-Mail an Tag 6 haben. Einige Ihrer Nutzer sind möglicherweise nicht über Push-Benachrichtigungen erreichbar, da sich nicht jeder für den Empfang von Push-Nachrichten entscheidet. Vielleicht möchten Sie die E-Mail von Tag 6 an alle Nutzer:innen senden, auch wenn sie den Push von Tag 3 nicht erhalten haben.

In diesem Szenario können Sie die Optionen für das Fortschrittsverhalten verwenden, um sicherzustellen, dass Nutzer:innen den Canvas auch dann weiter durchlaufen, wenn sie den Push für Tag 3 nicht erhalten haben.

Wenn Sie möchten, dass alle Benutzer die E-Mail von Tag 6 erhalten, auch wenn sie den Push von Tag 3 nicht bekommen haben, können Sie das **Weiterleitungs-Verhalten** für den Push von Tag 3 auf **Sofortige Weiterleitung** einstellen.

Wenn Sie für den Push von Tag 3 die Option **Sofort vorrücken** wählen, werden die Benutzer vorrücken, wenn Braze versucht, den Push zu senden. Benutzer, die mit den Zielgruppenoptionen übereinstimmen und nicht über Push erreichbar sind, erhalten die Push-Mitteilung nicht, werden aber trotzdem weitergereicht.

{% details Vorheriger Canvas Fortschrittsverhalten %}

Vor der Veröffentlichung von Fortschrittsverhalten hat Braze Nutzer:innen über eine Canvas-Komponente vorangebracht, nachdem sie eine Nachricht von dieser Komponente erhalten hatten. Wenn zum Beispiel eine Canvas-Komponente eine E-Mail und einen Push enthält, würden die Benutzer erst dann zu den nächsten Schritten des Canvas übergehen, wenn Braze dem Benutzer entweder den Push oder die E-Mail geschickt hat.

Wenn der Benutzer die Push-Mitteilung oder die E-Mail nicht erhalten hat, kann er nicht zu den nächsten Schritten im Canvas übergehen.

Für Braze-Kund:innen, die nicht an der ersten Runde der Canvas-Beta für In-App-Nachrichten teilgenommen haben, wird die Fortschrittsverhalten-Option "Nachricht gesendet" auf alle Canvas-Schritte angewendet, die vor dem 30\. Juli 2019 erstellt wurden. Vor der Veröffentlichung von Fortschrittsverhalten wurde der Fortschritt der Nutzer:innen durch das Versenden von Nachrichten aus Canvas-Schritten erzielt.

Für Braze-Kund:innen, die an der ersten Runde der Canvas-Beta für In-App-Nachrichten teilgenommen haben, wird die Fortschrittsverhalten-Option "Nachricht gesendet" für alle Canvas-Schritte ohne In-App-Nachrichten, die vor dem 30\. Juli 2019 erstellt wurden, und "Zielgruppe voranbringen nach Verzögerung" für alle Canvas-Schritte mit In-App-Nachrichten, die vor dem 30\. Juli 2019 erstellt wurden, angewendet. Vor der Veröffentlichung von Fortschrittsverhalten wurde der Fortschritt der Nutzer:innen durch In-App-Nachrichten von Canvas ausgelöst.

{% enddetails %}

[1]: {% image_buster /assets/img/push-advancement-behavior.png %} Fortschrittsverhalten"
