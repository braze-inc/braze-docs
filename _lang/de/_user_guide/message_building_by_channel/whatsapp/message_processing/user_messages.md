---
nav_title: "Messaging-Nutzer:innen"
article_title: "Messaging-Nutzer:innen"
description: "Dieser Referenzartikel beschreibt, wie Braze mit Nutzernachrichten umgeht."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /user_guide/message_building_by_channel/whatsapp/quick_replies/

---

# Benutzer Nachrichten

> WhatsApp ist ein zweiseitiger Kommunikationskanal. Ihre Marke kann den Nutzern nicht nur Nachrichten senden, sondern sie können sich mit Hilfe von Kampagnenvorlagen und Canvases auch an Gesprächen beteiligen. Es gibt verschiedene Möglichkeiten, dies zu tun, darunter WhatsApp-Schnellantworten und Triggerwörter. Quick Reply Calls-to-Action (CTAs) sind eine großartige Möglichkeit, das Engagement der Nutzer:innen für Ihre WhatsApp-Nachrichten zu fördern.

## Aktionsbasierte Auslöser 

Sowohl Kampagnen als auch Canvases können durch eine eingehende WhatsApp-Nachricht (ein Benutzer, der Ihnen eine WhatsApp-Nachricht schickt), z. B. ein Auslösewort, gestartet und verzweigt werden und während der Laufzeit Änderungen erfahren. 

Stellen Sie sicher, dass Ihr Trigger-Wort dem entspricht, was Sie von den Nutzer:innen erwarten.

**Wissenswertes:**
- Jeder Buchstabe Ihres Auslöseworts muss bei der Konfiguration groß geschrieben werden. Braze verlangt nicht, dass eingehende Trigger-Wörter, die von Nutzer:inne gesendet werden, groß geschrieben werden. Zum Beispiel wird die Nachricht "jOin2023" immer noch das Canvas oder die Kampagne auslösen.
- Wenn für den aktionsbasierten Trigger im Entry-Plan kein Trigger-Wort angegeben ist, wird die Kampagne oder das Canvas für ALLE eingehenden WhatsApp-Nachrichten ausgeführt. Dazu gehören auch Nachrichten mit übereinstimmenden Phrasen in aktiven Kampagnen und Canvases. In diesem Fall erhält der Nutzer zwei WhatsApp-Nachrichten.

{% tabs %}
{% tab Kampagne %}

![]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp26.png %})

{% endtab %}
{% tab Canvas %}

![]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp24.png %})
{% endtab %}
{% endtabs %}

## Unerwähnte Antworten

Wir empfehlen Ihnen, auf interaktiven Canvase eine Option für nicht erkannte Antworten vorzusehen. Dies hilft den Nutzer:innen zu verstehen, welche Prompts verfügbar sind, und legt die Erwartungen an den Kanal fest. Das Erwartungsmanagement kann besonders hilfreich sein, wenn Sie WhatsApp-Kanäle mit Live-Agent-Chat haben. 
- Fügen Sie im Aktionsschritt, nachdem Sie die Aktionsgruppen für die angepassten Filterphrasen erstellt haben, eine zusätzliche Aktionsgruppe für „WhatsApp-Nachricht senden“ hinzu, aber **aktivieren Sie nicht „Bedingung“ im Nachrichtentext**. Damit werden alle nicht erkannten Benutzerantworten abgefangen, ähnlich wie bei einer "else"-Klausel. 
- Wir empfehlen eine WhatsApp-Nachricht, die den oder die Nutzer:in darüber informiert, dass dieser Kanal nicht besetzt ist, und ihn oder sie bei Bedarf an einen Support-Kanal weiterleitet. 

## Schnelle Antworten 

![Auf dem Telefonbildschirm, auf dem ein Button mit einer Handlungsaufforderung angezeigt wird, wird der Text des angeklickten Buttons angezeigt.][11]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Schnellantworten erscheinen als klickbare Schaltflächenoptionen innerhalb der Konversation, verhalten sich aber so, als ob ein Benutzer mit Text geantwortet hätte. Braze verarbeitet diese dann als eingehende Nachrichten und kann auf der Grundlage der angeklickten Schaltfläche bestimmte Antworten zurücksenden. Verwenden Sie den Schritt „Aktion für eingehende WhatsApp-Nachrichten“, wenn Sie Antworten von Ihren Nutzer:innen erstellen und filtern.

![Eine WhatsApp-Nachricht mit Text und drei Schaltflächen mit Handlungsaufforderungen.][13]{: style="max-width:50%;"}

### Quick Reply-Umgebung in Canvas konfigurieren

#### Schritt 1: CTAs erstellen

Erstellen Sie zunächst Ihre Schnellantwort-CTAs im [WhatsApp Nachrichtenvorlagen-Manager](https://business.facebook.com/wa/manage/message-templates/) innerhalb einer Nachrichtenvorlage. 

![Die Nutzeroberfläche des WhatsApp-Nachrichten-Template-Managers zeigt, wie Sie einen CTA-Button erstellen, indem Sie den Button-Typ (angepasst) und den Button-Text angeben.][12]{: style="max-width:80%;"}

Sobald Ihre Vorlage eingereicht und von WhatsApp genehmigt wurde, können Sie sie verwenden, um ein Canvas in Braze zu erstellen. 

{% alert tip %}
Sie können das Canvas erstellen, bevor Sie die Genehmigung für Ihre Nachrichten-Template erhalten.
{% endalert %}

#### Schritt 2: Canvas erstellen

Als nächstes erstellen Sie ein Canvas mit einem Nachrichtenschritt, der Ihre erstellte Template enthält. 

![][14]

Erstellen Sie einen Aktionsschritt, der auf den Nachrichtenschritt folgt. Erstellen Sie in diesem Aktionsschritt eine Gruppe pro Schnellantwortoption.

![Ein Canvas, bei dem die Bewertungsaktion „eine eingehende WhatsApp-Nachricht senden“ lautet.][15]

Geben Sie für jede Gruppe von Quick-Reply-Optionen den genauen Text des Buttons an, den Sie anpassen möchten. Beachten Sie, dass die Schlüsselwörter in Großbuchstaben geschrieben werden müssen. 

![Ein Canvas-Schritt, bei dem die Aktion „Eingehende WhatsApp-Nachricht senden“ so eingestellt ist, dass sie gesendet wird, wenn ein bestimmter Nachrichtentext empfangen wird.][16]

Wenn Sie eine Standardantwort für Benutzer wünschen, die auf die Nachricht mit Text statt mit Schnellantworten antworten, erstellen Sie eine zusätzliche Gruppe ohne passenden Nachrichtentext.

Fahren Sie ab diesem Punkt mit dem Erstellen des Canvas fort, wie Sie es sonst auch tun würden.

### Antworten

Sie werden wahrscheinlich für jede Antwort eine Antwortnachricht benötigen. Wir empfehlen, eine Sammeloption für Antworten außerhalb der Grenzen schneller Antworten vorzusehen (z. B. für Kund:innen, die mit einer allgemeinen Nachricht statt einer vorgegebenen Prompt antworten). Zum Beispiel: "Es tut uns leid, wir haben Ihre Antwort nicht erkannt. Für Supportanfragen wenden Sie sich bitte an <support channel>."

![Ein Canvas zeigt die Antworten für jeden CTA-Button an.][18]

Beachten Sie, dass Sie alle nachfolgenden Aktionen verwenden können, die Braze Canvas anbietet, wie z.B. Nachrichten als Antwort, Aktualisierungen des Benutzerprofils oder Braze-to-Braze Webhooks. 

[1]: {% image_buster /assets/img/whatsapp/whatsapp24.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp25.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp26.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp27.png %} 

[11]: {% image_buster /assets/img/whatsapp/whatsapp11.png %}
[12]: {% image_buster /assets/img/whatsapp/whatsapp12.png %}
[13]: {% image_buster /assets/img/whatsapp/whatsapp13.png %}
[14]: {% image_buster /assets/img/whatsapp/whatsapp14.png %}
[15]: {% image_buster /assets/img/whatsapp/whatsapp15.png %}
[16]: {% image_buster /assets/img/whatsapp/whatsapp16.png %}
[17]: {% image_buster /assets/img/whatsapp/whatsapp17.png %}
[18]: {% image_buster /assets/img/whatsapp/whatsapp18.png %}
