---
nav_title: "Messaging Nutzer:innen"
article_title: LINE-Benutzer benachrichtigen
page_order: 2
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit Hilfe von Kampagnenvorlagen und Canvases mit Benutzern chatten können."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# LINE-Benutzer benachrichtigen

> LINE ist ein zweiseitiger Kommunikationskanal. Mit Hilfe von Kampagnenvorlagen und Canvases können Sie den Nutzern nicht nur Nachrichten schicken, sondern auch mit ihnen ins Gespräch kommen. Dieser Artikel befasst sich mit den Details der Benachrichtigung von Benutzern, z. B. wie Sie Auslösewörter für eingehende Nachrichten und nicht erkannte Antworten festlegen.

Es gibt verschiedene Methoden, um mit Nutzer:innen über LINE zu kommunizieren, z. B. die Verwendung von LINE-Trigger-Wörtern. Sie können auch Calls-to-Action (CTAs) verwenden, um die Nutzer dazu anzuregen, sich mit Ihren LINE-Nachrichten zu beschäftigen.

## Aktionsbasierte Auslöser

Sie können Kampagnen und Canvase erstellen, die starten, sich verzweigen und mittendrin Änderungen vornehmen, wenn Sie eine eingehende LINE-Nachricht (eine von einem:einer Nutzer:in gesendete Nachricht) erhalten, die ein Trigger-Wort enthält. Achten Sie darauf, dass Sie Trigger-Wörter wählen, die mit dem übereinstimmen, was Sie von den Nutzer:innen erwarten.

### Kampagne

Legen Sie Ihre Trigger-Wörter fest, wenn Sie eine aktionsbasierte Zustellungskampagne planen.

![Aktionsbasierter Auslöser von "Senden Sie diese Kampagne an Nutzer:innen, die eingehende Nachrichten an die Abo-Gruppe gesendet haben, in der sich die Nachricht befindet" und ein leeres Feld.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Legen Sie Ihre Auslösewörter innerhalb von [Aktionspfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) in Ihrem Canvas fest.

![Aktions-Pfad mit einem Trigger von "Diese Kampagne an Nutzer:innen senden, die eingehende Nachrichten an die Abo-Gruppe gesendet haben, in der sich der Nachrichtentext befindet" und einem leeren Feld.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Anforderungen

Bei der Erstellung Ihrer Kampagne oder Ihres Canvas müssen Sie jeden Buchstaben Ihres Trigger-Worts großschreiben, auch wenn Braze nicht verlangt, dass eingehende Trigger-Wörter großgeschrieben werden. Wenn Ihr Auslösewort beispielsweise "JOIN2023" lautet, wird eine eingehende Nachricht mit dem Wort "jOin2023" den Canvas oder die Kampagne trotzdem auslösen.

Wenn kein Auslösewort angegeben wird, wird die Kampagne oder das Canvas für *alle* eingehenden LINE-Nachrichten ausgeführt. Dazu gehören auch Nachrichten mit übereinstimmenden Phrasen in aktiven Kampagnen und Canvases. In diesem Fall erhält der Nutzer zwei LINE-Nachrichten.

## Unerwähnte Antworten

Sie sollten eine Auslöseroption für nicht erkannte Antworten auf interaktiven Leinwänden einbauen. Dadurch werden die Benutzer über die verfügbaren Prompts (oder Triggerwörter) informiert und ihre Erwartungen an den Kanal festgelegt.

### Einen Auslöser für nicht erkannte Antworten erstellen

Nachdem Sie Aktionsgruppen für die benutzerdefinierten Filterphrasen erstellt haben, fügen Sie eine weitere Aktionsgruppe zum Aktionspfad für **LINE-Nachricht senden** hinzu und setzen kein Häkchen bei **Wo der Nachrichtentext**. Damit werden alle nicht erkannten Benutzerantworten abgefangen, ähnlich wie bei einer "else"-Klausel.

Für diese Nachricht sollten Sie eine LINE-Nachricht senden, die den Benutzer darüber informiert, dass dieser Kanal nicht von einem Menschen überwacht wird, und ihn bei Bedarf an einen Support-Kanal weiterleitet.

