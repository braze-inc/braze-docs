---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "Auf dieser Seite erfahren Sie, wie Sie Inbox Vision einrichten, ein Feature, mit dem Marketer ihre E-Mails aus der Perspektive verschiedener E-Mail-Clients und mobiler Geräte betrachten können."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> Mit Inbox Vision können Sie Ihre E-Mails aus der Perspektive verschiedener E-Mail Clients und mobiler Geräte betrachten. Sie können zum Beispiel die Unterschiede zwischen Dark Mode und Light Mode testen, um zu überprüfen, ob Ihre E-Mails wie gewünscht dargestellt werden.

{% alert important %}
Inbox Vision funktioniert möglicherweise nicht, wenn Ihr E-Mail-Inhalt auf Template-Informationen wie Nutzerprofil-Daten beruht. Braze Templates einen leeren Nutzer:innen, wenn Sie E-Mails für dieses Feature versenden.<br><br>Fügen Sie Standard-Werte zu jedem Liquid in Ihrer E-Mail Nachricht hinzu. Ohne Standardwerte erhalten Sie möglicherweise ein falsches positives Ergebnis oder der Test schlägt fehl.
{% endalert %}

## Überlegungen

Im Allgemeinen wird Ihre E-Mail nicht mit Inbox Vision funktionieren, wenn Ihr E-Mail-Inhalt auf Template-Informationen beruht, wie z.B. Informationen zum Nutzerprofil. Das liegt daran, dass Braze Templates einen leeren Nutzer:innen anzeigt, wenn wir E-Mails mit diesem Feature versenden.

Sie können dieses Problem lösen, indem Sie Standardwerte oder beliebige Werte für das Liquid in Ihrer E-Mail Nachricht hinzufügen, bevor Sie Inbox Vision ausführen. Wenn Sie den Test in Inbox Vision beenden, wird die ursprüngliche Nachricht im Posteingang angezeigt. Wenn keine Werte angegeben werden, kann es sein, dass der Test die Vorschau nicht erfolgreich darstellen kann.

Ihr Unternehmen hat ein Limit für die Anzahl der E-Mails, die Sie mit Inbox Vision in der Vorschau anzeigen können. Sie können dies auf dem Tab **E-Mail-Vorschauen** von Inbox Vision überwachen.

Geben Sie eine Betreffzeile und eine gültige Domain an, um eine Vorschau zu erhalten. Achten Sie auf die Unterschiede zwischen der Darstellung auf dem Desktop und auf dem Handy. Verwenden Sie die Vorschau, um sich zu vergewissern, dass die E-Mail wie gewünscht erscheint.

So testen Sie Ihre E-Mail Nachrichten im Posteingang von Inbox Vision:

1. Gehen Sie zu Ihrem Drag-and-Drop-Editor oder HTML-E-Mail-Editor.
2. Wählen Sie in Ihrem Editor **Vorschau & Test**.
3. Wählen Sie **Inbox Vision**.
4. Wählen Sie **Inbox Vision ausführen**. Dies kann bis zu zehn Minuten dauern.
5. Wählen Sie dann eine Kachel aus, um die Vorschau genauer zu betrachten. Diese Vorschauen sind in diese Abschnitte unterteilt: **Internet Clients**, **Anwendungsclients** und **mobile Clients**.

![Die Option zum Auswählen von E-Mail Clients für die Vorschau.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Wählen Sie **Inbox Vision ausführen**. Dieser Vorgang kann zwischen zwei und zehn Minuten in Anspruch nehmen.

{% alert note %}
Posteingang Vision unterstützt keine Nachrichten, die eine [Abbruchlogik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) enthalten, da diese Nachrichten als statische Inhalte dargestellt werden.
{% endalert %}

### Vorschau als Nutzer:in

Wenn Sie als zufälliger Nutzer:innen eine Vorschau anzeigen, speichert Inbox Vision keine benutzerspezifischen Einstellungen oder Attribute (wie z.B. den Namen oder die Einstellungen). Wenn Sie einen angepassten Nutzer auswählen, kann sich die Vorschau von Inbox Vision von anderen Vorschauen unterscheiden, da sie spezifische Nutzerdaten verwendet.

## Code-Analyse

Die Code-Analyse hebt mögliche HTML-Probleme hervor, zeigt die Anzahl der Vorkommen an und weist auf nicht unterstützte HTML-Elemente hin.

### Anzeigen von Informationen zur Codeanalyse

Sie finden diese Informationen auf dem Tab **Posteingang Vision**, indem Sie <i class="fas fa-list"></i> **Listenansicht** auswählen. Die Listenansicht ist nur für HTML-E-Mail-Templates verfügbar. Verwenden Sie bei Drag-and-Drop Templates stattdessen die Vorschau, um Probleme zu beheben.

![Beispiel einer Code-Analyse in der Inbox Vision Vorschau.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Die Code-Analyse kann schneller erscheinen als die Vorschau für einen bestimmten Client, da Braze wartet, bis die E-Mail eintrifft, bevor es den Screenshot macht.
{% endalert %}

## Spam-Tests

Spam-Tests prognostizieren, ob Ihre E-Mails in Spam-Ordnern oder Posteingängen landen. Braze führt Tests mit den wichtigsten Spam-Filtern (IronPort, SpamAssassin, Barracuda) und den wichtigsten ISP-Filtern (Gmail.com, Outlook.com) durch.

### Anzeigen der Spam-Test-Ergebnisse

So überprüfen Sie die Ergebnisse Ihres Spam-Tests:

1. Wählen Sie den Tab **Spam-Test** im Bereich **Inbox Vision**. In der Tabelle **Spam-Test-Ergebnis** sind der Name, der Status und der Typ des Spamfilters aufgeführt.
2. Überprüfen Sie diese Ergebnisse und nehmen Sie gegebenenfalls Anpassungen an Ihrer E-Mail Kampagne vor.
3. Wählen Sie **Test wiederholen**, um die Ergebnisse Ihres Spam-Tests erneut zu laden.

## Zugänglichkeitstests

Barrierefreiheitstests heben mögliche Probleme bei der Barrierefreiheit Ihrer E-Mails hervor und zeigen, welche Elemente nicht den Standards entsprechen. Braze analysiert Inhalte anhand ausgewählter Web Content Accessibility Guidelines[(WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), einer Reihe international anerkannter Standards, die vom W3C entwickelt wurden, um Internet-Inhalte besser zugänglich zu machen.

### Funktionsweise

Wenn Sie Inbox Vision ausführen, prüft Braze automatisch auf häufige Zugänglichkeitsprobleme im Rahmen des [WCAG 2.2 AA-Regelsatzes](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (z. B. fehlender Alt-Text, unzureichender Farbkontrast, falsche Überschriftenstruktur) und kategorisiert den Schweregrad, um Ihnen bei der Priorisierung von Korrekturen zu helfen. 

{% alert important %}
Der Kunde erkennt jedoch an, dass Braze keine Zusicherungen oder Garantien in Bezug darauf abgibt, ob die Verwendung der Zugänglichkeitstests die Verpflichtungen des Kunden zur Einhaltung von Vorschriften oder Gesetzen erfüllt oder nicht, und lehnt jegliche Haftung in diesem Zusammenhang ab.
{% endalert %}

### Anzeigen der Ergebnisse von Zugänglichkeitstests

Die Zugänglichkeitstests generieren Ergebnisse für jede Regel als bestanden, nicht bestanden oder überarbeitungsbedürftig auf dem Tab **Zugänglichkeitstests**. Braze kategorisiert jede Regel anhand von POUR (Perceivable, Operable, Understandable, Robust), den vier Prinzipien der WCAG.

#### POUR-Kategorien

Posteingang Vision kategorisiert die Themen nach den vier grundlegenden [POUR-Prinzipien](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Wahrnehmbar, bedienbar, verstehbar und robust.

| Prinzip | Definition |
| --- | --- |
| Wahrnehmbar | Informationen und Komponenten der Benutzeroberfläche müssen für die Nutzer:innen auf eine für sie wahrnehmbare Weise darstellbar sein.<br><br>Nutzer:innen müssen in der Lage sein, die dargebotenen Informationen wahrzunehmen (sie dürfen nicht für alle ihre Sinne unsichtbar sein). |
| Bedienbar | Die Komponenten der Benutzeroberfläche und die Navigation müssen bedienbar sein.<br><br>Nutzer:innen müssen in der Lage sein, die Schnittstelle zu bedienen (die Schnittstelle darf keine Interaktion erfordern, die ein Nutzer:innen nicht ausführen kann). |
| Verständlich | Die Informationen und die Bedienung der Benutzeroberfläche müssen verständlich sein.<br><br>Nutzer:innen müssen in der Lage sein, sowohl die Informationen als auch die Bedienung der Benutzeroberfläche zu verstehen (der Inhalt oder die Bedienung darf nicht unverständlich sein). |
| Stabil | Die Inhalte müssen so robust sein, dass sie von einer Vielzahl von Nutzer:innen zuverlässig interpretiert werden können, einschließlich assistiver Technologien.<br><br>Nutzer:innen müssen in der Lage sein, auf die Inhalte zuzugreifen, wenn die Technologien voranbringen (wenn sich die Technologien und Benutzeragenten weiterentwickeln, sollten die Inhalte zugänglich bleiben). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Schweregrade

Inbox Vision klassifiziert Zugänglichkeitsprobleme nach Schweregrad und hilft Ihnen so bei der Priorisierung von Abhilfemaßnahmen.

| Status | Definition |
| --- | --- |
| Kritisch | Probleme, die den Zugang zu Inhalten oder Funktionen für Nutzer:innen mit Behinderungen blockieren können. Diese sind am schwerwiegendsten und sollten vorrangig behoben werden. |
| Seriös | Probleme, die erhebliche Hindernisse verursachen können, aber den Zugang nicht vollständig blockieren. Diese sollten umgehend behandelt werden. |
| Moderat | Probleme, die Nutzern:innen mit Behinderungen Schwierigkeiten bereiten können, aber weniger wahrscheinlich den Zugang vollständig blockieren. |
| Geringfügig | Probleme, die eine relativ geringe Auswirkung auf die Zugänglichkeit haben und nur geringfügige Unannehmlichkeiten verursachen können. |
| Braucht Überprüfung | Ich kann nicht feststellen, ob es ein Problem gibt oder nicht. Dies kann vorkommen, wenn wir das Kontrastverhältnis nicht bestimmen können, da der Text auf einem Hintergrundbild platziert ist. Sie müssen es manuell überprüfen, da es nicht automatisch ermittelt werden kann. |
| Bestanden | Erfüllt WCAG A, AA oder die beste Praxis für Barrierefreiheit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Der Drag-and-Drop-Editor unterstützt das Setzen eines `<title>` Elements nicht, so dass der Barrierefreiheits-Scanner diese Prüfung immer nicht besteht.<br><br>Diese Einschränkung wird für zukünftige Verbesserungen getrackt. Wenn dies Ihre Arbeitsabläufe oder Ihre Nutzer:innen betrifft, [teilen Sie uns Ihr Feedback mit]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback), damit wir wirksame Korrekturen priorisieren können.
{% endalert %}

### Verständnis der automatisierten Zugänglichkeitstests

{% multi_lang_include accessibility/automated_testing.md %}

## Bewährte Praktiken

### Überprüfen Sie Ihre E-Mail Abonnent:innen-Liste

Referenzieren Sie das [E-Mail Insights Dashboard]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard), um die beliebtesten Gerätetypen und Anbieter zu ermitteln, bei denen sich Ihre Abonnent:innen engagieren. Wenn Sie mehr Details benötigen, wie z.B. den Browser, das Gerätemodell und mehr, können Sie Ihre [Currents-Daten]({{site.baseurl}}/user_guide/data/distribution/braze_currents) oder den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) nutzen, um diese Details über das jüngste E-Mail Engagement Ihrer Nutzer:innen abzurufen.

Andernfalls wählt Braze standardmäßig die 20 besten Vorschauen aus, die auf allgemeinen Branchen- und Expertendaten basieren und den Großteil des Engagements Ihrer Abonnent:innen mit Ihren E-Mails abdecken. Wenn Ihre Datenpunkte auf andere, beliebtere Vorschauen hindeuten, können Sie bei jedem Start von Inbox Vision einen Standard-Vorschau-Satz definieren.

### Wählen Sie aussagekräftige Vorschauen und beeinträchtigte Vorschauen aus

Wenn Ihr Unternehmen hauptsächlich in den USA ansässig ist, gibt es möglicherweise bestimmte Vorschauen, z. B. internationale Vorschauen wie GMX.de, die nur von einer nominellen Anzahl von Nutzer:innen verwendet werden. Wir empfehlen Ihnen, die Posteingänge mit einem hohen Abonnent:in-Anteil zu priorisieren und zu optimieren und Ihre Vorschau für Posteingänge mit einem hohen Abonnent:in-Anteil zu reservieren.

Wenn Sie Korrekturen vornehmen, die sich auf bestimmte Vorschauen auswirken, sollten Sie nur die betroffenen Vorschauen auswählen, um zu verhindern, dass ungenutzte Vorschauen verbraucht werden.

### Führen Sie Inbox Vision für die endgültige Version der E-Mail aus

Wir empfehlen, Inbox Vision auszuführen, wenn die E-Mail Nachricht produktionsreif ist oder kurz davor steht. Auf diese Weise können Sie die Anzahl der generierten Vorschauen reduzieren, da die E-Mail mehrere Iterationen durchläuft, bevor sie fertiggestellt und zum Versand an die Nutzer:innen bereit ist.

Wenn Sie Inbox Vision jedes Mal ausführen, wenn Sie eine einzelne Bearbeitung oder Änderung vornehmen, können Sie die Vorschau schnell verbrauchen. Wir empfehlen Ihnen, zunächst alle notwendigen Änderungen an der E-Mail vorzunehmen und dann Inbox Vision auszuführen, um eine Vorschau darauf zu erhalten, wie sich Ihre Änderungen auf die Darstellung Ihrer E-Mails in verschiedenen Umgebungen auswirken.

Braze führt Tests mit aktuellen E-Mail Clients durch und stellt sicher, dass die Darstellung korrekt ist. Wenn Sie ständig ein Problem mit einem Client sehen, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).
