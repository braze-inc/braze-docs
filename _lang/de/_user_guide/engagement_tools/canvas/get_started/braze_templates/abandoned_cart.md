---
nav_title: Warenkorb-Abbruch
article_title: Warenkorb-Abbruch
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze Canvas-Vorlage verwenden können, um Benutzer in Echtzeit anzusprechen und sie zu ermutigen, ihre Einkäufe abzuschließen."
tool: Canvas
---

# Warenkorb-Abbruch

> Interagieren Sie mit Nutzer:innen in Realtime, um sie zum Kaufabschluss zu bewegen. Verwenden Sie diese Vorlage, um eine User Journey zu erstellen, die sich auf das Versenden von rechtzeitigen, personalisierten Nachrichten konzentriert, die die Benutzer an ihre abgebrochenen Warenkörbe erinnern, indem sie die Produktvorteile hervorheben und Anreize bieten, wie z.B. Rabattcodes.

In diesem Artikel erläutern wir Ihnen einen Anwendungsfall für die Vorlage **Abandoned Intent**, die für die Überlegungsphase des Benutzerlebenszyklus gedacht ist. Nach diesem Artikel haben Sie eine User Journey erstellt, die Nutzer, die nach dem Hinzufügen von Artikeln zu ihrem Warenkorb noch keine Käufe getätigt haben, zum Kauf animiert.

## Voraussetzungen

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Ein separates Canvas für die Nutzer:innen nach dem Kauf, da ein Kauf in diesem Canvas zum Verlassen des Canvas führt.
- Eine konfigurierte [Braze-Zielgruppen-Synchronisierung]({{site.baseurl}}/partners/canvas_audience_sync/) mit den Partnern und Zielgruppen, die Sie verwenden.

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, wir arbeiten bei Kitchenerie, einer Einzelhandelsmarke, die sich auf Küchenutensilien spezialisiert hat, und unser Ziel ist es, Nutzer, die das neueste Produkt "Riesiger Pappteller" in ihren Einkaufswagen gelegt, aber nicht gekauft haben, wieder anzusprechen.

Bevor wir das Canvas erstellen, richten wir die [Braze Audience Sync to Facebook-Integration]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) ein, so dass wir Benutzerdaten von Braze zu Facebook Audiences hinzufügen können, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu senden.

Um auf die Vorlage für verlassene Absichten zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas die Option **Canvas-Vorlage verwenden** > **Braze-Vorlagen**. Wählen Sie dann neben **Abandoned Intent** die Option **Vorlage anwenden**. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Details einrichten

Passen wir die Canvas-Details an, um unser Ziel zu erreichen.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Aktualisieren Sie den Namen des Canvas, um anzugeben, dass das Canvas für das Targeting von Nutzer:innen mit abgebrochenen Warenkörben bestimmt ist.
3\. Aktualisieren Sie die Beschreibung, um zu verdeutlichen, dass das Canvas dazu dient, Nutzer zum Kauf der neuesten saisonalen Küchenartikel zu animieren.
4\. Fügen Sie den Tag **Warenkorb-Abbruch** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Schritt 2: Konversions-Events zuweisen

Als nächstes weisen wir unser Konvertierungsereignis zu. Da wir uns auf unser Produkt „Riesiger Pappteller“ konzentrieren, werden wir für das **primäre Konversions-Event A** Folgendes tun:

1. Wählen Sie für den **Ereignistyp Umwandlung** die Option **Kauf tätigen**.
2. Wählen Sie **Einen bestimmten Kauf tätigen**. So können wir einen bestimmten Produktnamen auswählen.
3. Wählen Sie **Enorm großer Pappteller**.

![Primäres Konversions-Event - A mit dem Konversionstyp "Macht Kauf" mit dem Produktnamen "Riesiger Pappteller". Es gibt eine Frist von 3 Tagen für die Konversion.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Schritt 3: Entry-Zeitplan festlegen

Der Zeitplan für den Eintrag dieser Vorlage ist zwar auf **API-gesteuert** eingestellt, aber unser Anwendungsfall profitiert mehr von einem aktionsbasierten Eintrag für diesen Canvas, da wir uns auf Benutzer konzentrieren möchten, die ihren Einkaufswagen verlassen haben (was eine Aktion ist).

1. Wählen Sie **Aktionsbasiert** als Entry-Zeitplantyp aus.
2. Wählen Sie **Abgebrochener Warenkorb** als Auslöser.
3. Wählen Sie für das Entry-Fenster das Datum der Startzeit aus.
4. Wählen Sie die Option aus, die es Nutzern:innen erlaubt, ihre Ortszeit einzugeben. Dies kann die Relevanz unserer Nachrichten aufrechterhalten und zu einem höheren Engagement führen, wenn die Nachrichten zum optimalen Zeitpunkt gesendet werden.

![Ein aktionsbasiertes Canvas, das auf Nutzer:innen abzielt, die ihren Warenkorb abgebrochen haben, mit dem Eingangsfenster 15\. Oktober 2024 15:20 Uhr in der Ortszeit der Nutzer:innen.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Schritt 4: Festlegen, wer das Canvas aufruft

Als nächstes definieren wir unsere Zielgruppe als Nutzer, die in den letzten 90 Tagen ausschließlich online bei uns eingekauft haben. So können wir unser Publikum auf die Nutzer eingrenzen, von denen wir wissen, dass sie sich für unsere Produkte interessieren. 

!["Online Shoppers Segment - 90 Tage" als Segment der Nutzer:innen für das Targeting in diesem Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Wir belassen die Eingangskontrollen so, wie sie sind, so dass Nutzer:innen diesen Canvas nicht erneut betreten dürfen und die Anzahl der Personen, die diesen Canvas betreten können, nicht begrenzt ist.

Als Ausstiegskriterium werden Nutzer:innen den Canvas verlassen, wenn sie den "Riesigen Pappteller" gekauft haben. Auf diese Weise erhalten sie keine weiteren Nachrichten zu einem Artikel, den sie bereits gekauft haben.

![Exit-Kriterium, das festlegt, dass Nutzer:innen, die einen bestimmten Kauf für den riesigen Pappteller tätigen, den Canvas verlassen.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Wir behalten die Standardeinstellungen für das Abonnement bei, d.h. wir senden nur an Benutzer, die sich für den Erhalt von Nachrichten oder Benachrichtigungen angemeldet oder entschieden haben, und lassen die anderen Einstellungen unverändert.

### Schritt 6: Canvas anpassen

Jetzt bauen wir unser Canvas auf, indem wir die in der Vorlage enthaltenen Schritte anpassen:

1. Wählen Sie den Schritt „Aktionspfade“ und dann den Namen der Aktionsgruppe **Kauf erfolgt** aus.
2. Wählen Sie für **Kauf tätigen** die Option **Einen bestimmten Kauf tätigen** und wählen Sie als Produkt **Enormes Pappteller**. Ähnlich wie bei den Ausstiegskriterien werden Nutzer:innen, die dieses Produkt kaufen, den Canvas verlassen.

!["Made purchase" Aktionsgruppe, die das Canvas verlässt, wenn der Nutzer:in den riesigen Pappteller kauft.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3\. Für den Schritt Nachricht wählen Sie **Nachricht bearbeiten**, um die E-Mail anzupassen, die an unsere Benutzer gesendet wird, um sie über die Artikel in ihrem abgebrochenen Warenkorb zu informieren.
4\. Lassen Sie den Schritt „Delay“ unverändert.
5\. In den Schritten für die Nachrichten, die sich an den Schritt für den Zielgruppenpfad anschließen, passen wir die E-Mail- und SMS-Nachrichten an, die unsere Nutzer erhalten werden. Hier möchten wir unsere Nutzer mit personalisierten Nachrichten zum Kauf von Produkten anregen.

![Eine Vorschau auf die SMS Nachricht, die Nutzer:innen erhalten werden: "Hallo, Sie haben den riesigen Pappteller in Ihrem Einkaufswagen vergessen! Schließen Sie Ihren Kauf jetzt ab und verbessern Sie Ihre Hosting-Fähigkeiten. Verwenden Sie den Code MYPLATE beim Checkout, um 20 % Rabatt auf Ihre Bestellung zu erhalten!“]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6\. Im nächsten Schritt Aktions-Pfade wählen Sie die Aktionsgruppe **Gekauft aus**. Wählen Sie dann **Gezielt einkaufen** und wählen Sie **Enormous Paper Plate** als Produkt aus. Dieser Schritt spiegelt den ersten Schritt von Action Paths wider, indem er Benutzer, die unser Produkt gekauft haben, ausschließt, damit sie keine weiteren Nachrichten erhalten.
7\. Stellen Sie sicher, dass unser Schritt „Zielgruppen-Synchronisierung“ für die Synchronisierung mit Facebook eingerichtet ist. Dies wird auch beim Retargeting von Anzeigen helfen.

{% alert tip %}
Sie können die [Canvas-Eingabeeigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) verwenden, um die Nachrichten in Ihrem Canvas je nach dem Produkt, auf das Sie sich beziehen, anzupassen.
{% endalert %}

### Schritt 7: Testen und starten Sie den Canvas

Nachdem Sie unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Canvas starten**, um das Canvas zu starten. Jetzt können wir Nutzer:innen mit einer personalisierten User Journey gezielt ansprechen, um sie zu ermutigen, das Produkt zu kaufen, das sie in ihren Warenkorb gelegt haben!

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}

