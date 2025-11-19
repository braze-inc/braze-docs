---
nav_title: "Messaging Nutzer:innen"
article_title: "Messaging-Nutzer:innen"
description: "Dieser Referenzartikel beschreibt, wie Braze mit Nutzernachrichten umgeht."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# Benutzer Nachrichten

> WhatsApp ist ein zweiseitiger Kommunikationskanal. Ihre Marke kann den Nutzern nicht nur Nachrichten senden, sondern sie können sich mit Hilfe von Kampagnenvorlagen und Canvases auch an Gesprächen beteiligen. Es gibt verschiedene Möglichkeiten, dies zu tun, einschließlich WhatsApp-Schnellantworten, Listennachrichten und triggernde Wörter. Schnellantworten und Calls-to-Action (CTAs) für Listennachrichten sind eine großartige Möglichkeit, das Engagement der Nutzer:innen für Ihr WhatsApp Messaging zu fördern.

## Aktionsbasierte Auslöser 

Sowohl Kampagnen als auch Canvase können durch eine eingehende WhatsApp-Nachricht (ein Nutzer:innen, der Ihnen eine Nachricht auf WhatsApp schickt), z.B. ein Trigger-Wort, gestartet, verzweigt und in der Mitte der Reise geändert werden. 

Stellen Sie sicher, dass Ihr Trigger-Wort dem entspricht, was Sie von den Nutzer:innen erwarten.

**Wissenswertes:**
- Jeder Buchstabe Ihres Auslöseworts muss bei der Konfiguration groß geschrieben werden. Braze verlangt nicht, dass eingehende Trigger-Wörter, die von Nutzer:inne gesendet werden, groß geschrieben werden. Zum Beispiel wird die Nachricht "jOin2023" immer noch das Canvas oder die Kampagne auslösen.
- Wenn für den aktionsbasierten Trigger im Entry-Plan kein Trigger-Wort angegeben ist, wird die Kampagne oder das Canvas für ALLE eingehenden WhatsApp-Nachrichten ausgeführt. Dazu gehören auch Nachrichten mit übereinstimmenden Phrasen in aktiven Kampagnen und Canvases. In diesem Fall erhält der Nutzer zwei WhatsApp-Nachrichten.

{% tabs %}
{% tab Campaign %}

![Aktionsbasierte Optionen für die Zeitplanung von Kampagnen.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![Aktionsbasierte Zeitplan-Optionen für Canvas.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## Unerwähnte Antworten

Wir empfehlen Ihnen, auf interaktiven Canvase eine Option für nicht erkannte Antworten vorzusehen. Dies hilft den Nutzer:innen zu verstehen, welche Prompts verfügbar sind, und legt die Erwartungen an den Kanal fest. Das Erwartungsmanagement kann besonders hilfreich sein, wenn Sie WhatsApp-Kanäle mit Live-Agent-Chat haben. 
- Fügen Sie im Aktionsschritt, nachdem Sie die Aktionsgruppen für die angepassten Filterphrasen erstellt haben, eine zusätzliche Aktionsgruppe für „WhatsApp-Nachricht senden“ hinzu, aber **aktivieren Sie nicht „Bedingung“ im Nachrichtentext**. Damit werden alle nicht erkannten Benutzerantworten abgefangen, ähnlich wie bei einer "else"-Klausel. 
- Wir empfehlen eine WhatsApp-Nachricht, die den oder die Nutzer:in darüber informiert, dass dieser Kanal nicht besetzt ist, und ihn oder sie bei Bedarf an einen Support-Kanal weiterleitet. 

## Schnelle Antworten 

![Telefonbildschirm, der einen Aktions-Button anzeigt, antwortet mit dem Text des angeklickten Buttons.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Schnellantworten erscheinen als klickbare Schaltflächenoptionen innerhalb der Konversation, verhalten sich aber so, als ob ein Benutzer mit Text geantwortet hätte. Braze verarbeitet diese dann als eingehende Nachrichten und kann auf der Grundlage der angeklickten Schaltfläche bestimmte Antworten zurücksenden. Verwenden Sie den Schritt „Aktion für eingehende WhatsApp-Nachrichten“, wenn Sie Antworten von Ihren Nutzer:innen erstellen und filtern.

![Eine WhatsApp Nachricht mit Text und drei Aktions-Buttons.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Konfigurieren Sie die Schnellantwortfunktion in Canvas

#### Schritt 1: CTAs erstellen

Erstellen Sie zunächst Ihre Schnellantwort-CTAs im [WhatsApp Nachrichtenvorlagen-Manager](https://business.facebook.com/wa/manage/message-templates/) innerhalb einer Nachrichtenvorlage. 

![Das UI des Managers für WhatsApp Nachrichten-Templates zeigt, wie Sie einen CTA-Button erstellen, indem Sie den Button-Typ (angepasst) und den Button-Text angeben.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

Sobald Ihre Vorlage eingereicht und von WhatsApp genehmigt wurde, können Sie sie verwenden, um ein Canvas in Braze zu erstellen. 

{% alert tip %}
Sie können das Canvas erstellen, bevor Sie die Genehmigung für Ihre Nachrichten-Template erhalten.
{% endalert %}

#### Schritt 2: Canvas erstellen

Als nächstes erstellen Sie ein Canvas mit einem Nachrichtenschritt, der Ihre erstellte Template enthält. 

![WhatsApp Schritt Nachrichten-Editor mit einer ausgefüllten Vorlage für schnelle Antworten.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

Erstellen Sie einen Aktionsschritt, der auf den Nachrichtenschritt folgt. Erstellen Sie in diesem Aktionsschritt eine Gruppe pro Schnellantwortoption.

![Ein Canvas, bei dem die Auswertungsaktion "eine eingehende Nachricht über Whatsapp senden" lautet.]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

Geben Sie für jede Gruppe von Quick-Reply-Optionen den genauen Text des Buttons an, den Sie anpassen möchten. Beachten Sie, dass die Schlüsselwörter in Großbuchstaben geschrieben werden müssen. 

![Ein Canvas-Schritt, bei dem die Aktion "eine eingehende Whatsapp-Nachricht senden" so eingestellt ist, dass sie gesendet wird, wenn eine bestimmte Nachricht empfangen wird.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

Wenn Sie eine Standardantwort für Benutzer wünschen, die auf die Nachricht mit Text statt mit Schnellantworten antworten, erstellen Sie eine zusätzliche Gruppe ohne passenden Nachrichtentext.

Fahren Sie ab diesem Punkt mit dem Erstellen des Canvas fort, wie Sie es sonst auch tun würden.

### Antworten

Sie werden wahrscheinlich für jede Antwort eine Antwortnachricht benötigen. Wir empfehlen, eine Sammeloption für Antworten außerhalb der Grenzen schneller Antworten vorzusehen (z. B. für Kund:innen, die mit einer allgemeinen Nachricht statt einer vorgegebenen Prompt antworten). Zum Beispiel: "Es tut uns leid, wir haben Ihre Antwort nicht erkannt. Für Supportanfragen wenden Sie sich bitte an <support channel>."

![Ein Canvas, das die Antworten für jeden Aktions-Button anzeigt.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Beachten Sie, dass Sie alle nachfolgenden Aktionen verwenden können, die Braze Canvas anbietet, wie z.B. Nachrichten als Antwort, Aktualisierungen des Benutzerprofils oder Braze-to-Braze Webhooks. 

## Nachrichten auflisten

Nachrichten in der Liste erscheinen als Nachricht mit einer Liste von anklickbaren Optionen. Jede Liste kann mehrere Abschnitte haben, und jede Liste kann bis zu 10 Zeilen haben.

![Beispiel einer WhatsApp-Listennachricht mit Zeilen für verschiedene Modestile.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Konfigurieren Sie das Messaging-Erlebnis für die Liste in Canvas

#### Schritt 1: Erstellen oder bearbeiten Sie eine bestehende aktionsbasierte Canvase

Sie können nur Nachrichten aus der WhatsApp-Liste zu Canvase hinzufügen, die aktionsbasiert sind, da sie als Reaktion auf eine Nutzer:innen-Nachricht erfolgen müssen.

#### Schritt 2: Schritt zum Erstellen einer WhatsApp Nachricht

Fügen Sie einen Schritt WhatsApp [Messaging]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) hinzu und wählen Sie dann das Layout für die Antwortnachricht von **List Message aus**.

![Eine auswählbare Sammlung der verschiedenen Arten von WhatsApp Messaging-Nachrichten, die Sie erstellen können, einschließlich "List Message".]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

Fügen Sie einen Namen für den **Button Liste** hinzu, den die Nutzer:innen auswählen, um Ihre Liste anzuzeigen. Verwenden Sie dann die Felder in **Listeninhalt**, um Ihre Liste zu erstellen:

- **Abschnitt:** Fügen Sie bis zu 10 Abschnitte hinzu, um Ihre Artikel in der Liste zu gruppieren und zu organisieren. Ein Bekleidungshändler könnte zum Beispiel Abschnitte verwenden, um nach saisonalen Stilen (wie Frühling, Sommer, Herbst und Winter) oder Artikeln (wie Oberteile, Unterteile und Schuhe) zu organisieren.
- **Reihe:** Fügen Sie bis zu 10 Zeilen oder Artikel in allen Abschnitten hinzu.
- **Zeilenbeschreibung (optional):** Fügen Sie allen Zeilen (Artikeln der Liste) eine optionale Beschreibung hinzu.

![Der Abschnitt "Inhalt auflisten" wurde mit zwei Abschnitten und mehreren Zeilen und Zeilenbeschreibungen ausgefüllt.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

Ändern Sie die Reihenfolge der Abschnitte und Zeilen, indem Sie das Symbol neben den Namen auswählen und ziehen.

![Ziehen Sie einen Listenabschnitt an einen neuen Standort.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

Fügen Sie im Canvas-Schritt nach dem Nachrichten-Schritt einen [Aktions-Pfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) hinzu, der eine Gruppe für jede Listenantwort enthält. In jeder Gruppe:

1. Fügen Sie einen Trigger für **Gesendete eingehende WhatsApp Abo-Gruppe** hinzu und wählen Sie die entsprechende Abo-Gruppe aus.
2. Aktivieren Sie das Kontrollkästchen **Wo der Nachrichtentext ist**.
3. Geben Sie den Inhalt für eine Zeile (oder einen Artikel der Liste) an.

![Composer für einen Aktions-Pfad mit Gruppen für verschiedene Kleidungsstile.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Bauen Sie Ihr Canvas weiter aus.

### Aktions-Pfade für lange Beschreibungen erstellen

Wenn Sie Zeilenbeschreibungen haben, müssen Sie **Matches Regex** verwenden, um eine Zeile anzugeben. Wenn Sie zum Beispiel eine Zeile mit der Beschreibung "Unser neuer Stil, der über Ihr Lieblingspaar Stiefeletten passt" angeben möchten, könnten Sie [Regex]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) mit "Stiefeletten" verwenden.

![Ein WhatsApp Trigger, der den Filter für "Matches regex" verwendet, um Nachrichten mit "Ankle Boots" als Antwort zu erfassen.]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## Überlegungen zu Nachrichten als Antwort

Nachrichten, die responsiv sind, müssen innerhalb von 24 Stunden nach Erhalt der Nachricht eines Nutzers:innen gesendet werden. Um den Aufbau erfolgreicher Messaging-Erlebnisse zu unterstützen, prüft Braze die Nachrichtenlogik, um zu bestätigen, dass es eine eingehende Nachricht eines Nutzers:in gibt, die die Antwortnachricht freigibt. 

Die folgenden Ereignisse heben die Blockierung von Nachrichten auf: 

- Eingehende Nachricht 
  - [Aktions-Pfad]({{site.baseurl}}/action_paths/) oder [aktionsbasierter Eingang]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) mit dem Trigger **Eine eingehende WhatsApp Nachricht senden**.

![Ein aktionsbasierter Eingangsschritt mit dem Trigger "Eine eingehende WhatsApp Nachricht senden".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [API-gesteuerter Eingang]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)
- Eingehende Nachricht zum Produkt 
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated#types-of-ecommerce-recommended-events) Veranstaltung

![Ein Aktions-Pfad mit dem Trigger eines durchgeführten angepassten Events `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

