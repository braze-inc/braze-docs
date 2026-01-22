---
nav_title: Feedback nach dem Kauf
article_title: Feedback nach dem Kauf
page_order: 6
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze Canvas-Vorlage verwenden, um personalisierte Erlebnisse zu inszenieren, mit denen Sie auf Feedback reagieren und eine Beziehung zu Ihren Benutzern aufbauen können."
tool: Canvas
---

# Feedback nach dem Kauf

> Verwenden Sie die Vorlage für das Feedback nach dem Kauf, um wichtige Erkenntnisse darüber zu gewinnen, wie Ihre Kunden mit Ihrer Marke interagieren, und um sicherzustellen, dass sie weiterhin positive Erfahrungen machen. Durch den Einsatz personalisierter Kommunikation und strukturierter Nachrichten können Sie Ihre Kundenbeziehungen weiter ausbauen und pflegen.

Dieser Artikel führt Sie durch einen Anwendungsfall für die Vorlage **Post-Purchase Feedback**, die für den Konvertierungsschritt des Benutzerlebenszyklus konzipiert ist. Wenn Sie fertig sind, haben Sie ein Canvas erstellt, das Nutzer:innen dazu auffordert, Feedback zu Ihrer App zu geben.

## Voraussetzungen

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Ein [benutzerdefiniertes Attribut]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes), auf das Sie bei Feedback-Umfrageergebnissen verweisen können.
- Eine konfigurierte [Braze-Zielgruppen-Synchronisierung]({{site.baseurl}}/partners/canvas_audience_sync/) mit den Partnern und Zielgruppen, die Sie verwenden.

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, wir arbeiten für Decorumsoft, einen Entwickler von mobilen Videospielen. Wir werden die Vorlage für das Feedback nach dem Kauf verwenden, um das Feedback für unser neuestes Videospiel, Proxy War 3, zu messen: Krieg des Durstes. Anhand dieses Feedbacks werden wir unsere Entwicklungspläne für das Erweiterungspaket Liquid Mirage anpassen.

Bevor wir das Canvas erstellen, richten wir die [Braze Audience Sync to Google-Integration]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) ein, damit wir Nutzerdaten von Braze zu Google Audiences hinzufügen können, um Werbung auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu senden.

Um auf die Vorlage für das Feedback nach dem Kauf zuzugreifen, wählen Sie bei der Erstellung eines neuen Canvas die Option **Eine Canvas-Vorlage verwenden** > **Lötvorlagen**. Wählen Sie dann neben **Post-Purchase Feedback** die Option **Vorlage anwenden**. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Canvas-Details einrichten

Passen wir die Canvas-Details an, um unser Ziel zu erreichen.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Aktualisieren Sie den Namen des Canvas, um anzugeben, dass das Canvas für das Targeting neuer Nutzer:innen gedacht ist.
3\. Aktualisieren Sie die Beschreibung, um zu verdeutlichen, dass das Canvas dazu dient, Benutzer zur Abgabe von Feedback zu ermutigen.
4\. Fügen Sie das Tag **Feedback** hinzu, um auf der Canvas-Startseite danach zu filtern.

![Der neue Name und die Beschreibung für das Canvas. In der neuen Beschreibung heißt es: Ein Canvas mit Feedback nach dem Kauf, um das Interesse an der kommenden Erweiterung für PWD3, Liquid Mirage, zu ermitteln.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### Schritt 2: Konversions-Events zuweisen

Als nächstes weisen wir unsere Konvertierungsereignisse zu. Aktualisieren Sie das **primäre Konvertierungsereignis - A** auf **Einen bestimmten Kauf tätigen** und wählen Sie **Proxy War**.

!["Konversions-Events zuweisen" für den Konversions-Event-Typ des Kaufs des Produkts Proxy War game.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

Wir behalten die Frist für die Konversion des Templates von drei Tagen bei, da wir unsere jüngsten Nutzer:innen ansprechen wollen.

### Schritt 3: Entry-Zeitplan festlegen

1. Behalten Sie den Entry-Zeitplan als **aktionsbasiert** bei.
2. Setzen Sie die **Startzeit** für das Eingabefenster auf das Datum, an dem das Spiel gestartet wird.

### Schritt 4: Festlegen, wer das Canvas aufruft

Unsere Targeting-Zielgruppe für das Feedback sind Nutzer:innen, die Proxy War 3 kürzlich gekauft haben.

1. Wählen Sie unser Targeting-Segment "Gekaufter Proxy War 3" aus, das aus Nutzer:innen besteht, die das Spiel gekauft haben.
2. Wählen Sie einen Filter, um Benutzer einzuschließen, die "Proxy War 3" mehr als "0" Mal gekauft haben.

![Ein Segment namens "Gekaufter Proxy War 3", das Nutzer:innen segmentiert, die das Spiel gekauft haben.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3\. Aktualisieren Sie die Eingangskontrollen, damit Nutzer:innen nach Ablauf der maximalen Dauer des Canvas nicht mehr in das Canvas eintreten können.

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Wir behalten die Standardeinstellungen für das Abonnement bei, d.h. wir senden nur an Benutzer, die sich angemeldet oder für den Erhalt von Nachrichten oder Benachrichtigungen entschieden haben. 

Da wir mit dem Versenden achtsam sein wollen, wählen wir die Option **Ruhige Zeiten aktivieren**, um zu vermeiden, dass wir zwischen 23 und 10 Uhr in der Zeitzone unserer Nutzer um Feedback bitten, und senden erst zur nächsten verfügbaren Zeit.

!["Sendeeinstellungen" Schritt Targeting von Nutzern:in, die Abonnent:in sind oder sich angemeldet haben. Die Ruhezeiten sind eingeschaltet.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

Für unser Beispiel überspringen wir die anderen Einstellungen (Frequenzkappung und Seed-Gruppen).

### Schritt 6: Canvas anpassen

Als nächstes bauen wir unser Canvas auf, indem wir die Messaging-Kanäle und die Inhalte, die an die Nutzer:innen gesendet werden, anpassen. Da wir nur über die Kanäle E-Mail, In-App-Nachricht und Webhook um Feedback bitten, gehen wir die Vorlage durch und entfernen die SMS-Varianten aus den Nachrichtenschritten.

Wir beginnen unsere Anpassung, indem wir die einzelnen Messaging-Komponenten durchgehen, um den Inhalt zu aktualisieren. Unser angepasstes Attribut zum Referenzieren ist `Experience Feedback`.

1. Wählen Sie im Canvas-Builder den ersten Nachrichtenschritt in der User Journey aus.
2. Wählen Sie die Variante **E-Mail**.
3. Füllen Sie die **Sendeinfo** mit einem Betreff aus, der Nutzer:innen zum Feedback ermutigt. 
4. Wählen Sie **Nachricht bearbeiten**, um die E-Mail-Nachricht der Vorlage durch die Nachricht unserer Feedback-Umfrage zu ersetzen. Dazu gehört auch das Ersetzen der Links für jede Call-to-Action, um zu erfassen, welche Option ausgewählt wurde, die im Schritt Aktions-Pfad unserer Nutzer:innen referenziert wird.

{% alert tip %}
Sie können die [Canvas-Eingabeeigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) verwenden, um die Nachrichten in Ihrem Canvas je nach dem Produkt, auf das Sie sich beziehen, anzupassen.
{% endalert %}

#### Feedback-Umfrage einrichten

Als Nächstes müssen wir die Details für die Variante **In-App-Nachricht** ausfüllen. Hier müssen wir unser benutzerdefiniertes Attribut `Experience Feedback` angeben, das die Stimmung unseres Nutzerfeedbacks angibt. (Wir werden auch im nächsten Schritt des Aktionsplans darauf verweisen.)

1. Im gleichen ersten Schritt wählen Sie die Variante **In-App-Nachrichten**. Wir behalten die Kontrolle über die Nachrichten wie bisher bei. 
2. In der Kopfzeile und im Hauptteil werden wir eine Sprache verwenden, die die Nutzer dazu ermutigt, ehrlich über ihre Erfahrungen mit Proxy War 3 zu berichten.
3. Da wir möchten, dass ihre Umfragebeantwortungen mit ihren Profilen protokolliert werden, belassen wir die Umfrage als **Single-Choice-Auswahl** und **protokollieren die Attribute bei der Übermittlung**.
4. Wählen Sie für jede der drei Umfragen das Attribut **Experience Feedback** als unser angepasstes Attribut aus. 
5. Wir behalten die Attributwerte im Benutzerprofil unverändert bei, da diese Werte mit unserem benutzerdefinierten Attribut übereinstimmen.

![Eine Umfrage, die den Nutzer:innen die Frage stellt, ob sie mit dem Kauf von Proxy War 3 zufrieden waren: "Ich habe es geliebt", "Es war OK" und "Nichts für mich".]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Aktionspfad weiterentwickeln

Mit unserem benutzerdefinierten Attribut `Experience Feedback` und den Attributwerten aus dem vorherigen Abschnitt aktualisieren wir den Aktionspfad der Vorlage, damit er mit unserem Attribut und den Werten übereinstimmt.

![Die Gruppe "Gutes Feedback" für den Schritt Aktions-Pfad, die Nutzer:innen umfasst, die bei unserer Umfrage mit "Gefällt mir" geantwortet haben.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Retargeting von Anzeigen einrichten

Wir stellen sicher, dass unser Google Audience Sync im Schritt **Anzeigen-Retargeting** eingerichtet ist. Dazu gehört die Auswahl unseres Anzeigenkontos, einer bestehenden Zielgruppe und der Option, Nutzer zur Zielgruppe hinzuzufügen.

### Webhook-Unterstützungsfälle einrichten

Als Nächstes richten wir den Webhook ein, um potenzielle Supportfälle auszulösen. Dies kann in Kombination mit der Analyse des Feedbacks unserer Nutzer:innen besonders aufschlussreich sein.

Für den Schritt Nachricht mit dem Namen **Erstellung von Supportfällen** aktualisieren wir die Vorlage, um einen Webhook für Benutzer zu erstellen, die mit ihrem Kauf unzufrieden sind und eine Rückerstattung wünschen.

![Ein Webhook, der Support-Fälle für Kund:in erstellt, die eine negative Stimmung haben und eine Rückerstattung für ihren Kauf von Proxy War 3 wünschen.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### Schritt 6: Testen und starten Sie den Canvas

Nachdem Sie unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Canvas starten**, um das Canvas zu starten. Jetzt können wir Benutzer mit einer personalisierten Benutzerführung gezielt ansprechen, um sie zu ermutigen, auf der Grundlage ihres jüngsten Kaufs von Proxy War 3 an unserer Feedback-Umfrage teilzunehmen!

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}
