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

> Mit Inbox Vision können Sie Ihre E-Mails aus der Perspektive verschiedener Clients für E-Mails und mobiler Geräte anzeigen. Sie können beispielsweise die Unterschiede zwischen Dark Mode und dem hellen Modus testen, um sicherzustellen, dass Ihre E-Mails wie beabsichtigt dargestellt werden.

{% alert important %}
Inbox Vision funktioniert möglicherweise nicht, wenn Ihr E-Mail-Inhalt auf Templates basiert und Daten aus dem Nutzerprofil enthält. Braze erstellt beim Versenden von E-Mails für dieses Feature ein leeres Template für einen leeren Nutzer:in.<br><br>Fügen Sie Standardwerte zu jedem Liquid in Ihrer E-Mail-Nachricht hinzu. Ohne Standardwerte kann es zu einem falschen positiven Ergebnis kommen oder der Test kann fehlschlagen.
{% endalert %}

## Überlegungen

Im Allgemeinen ist es nicht möglich, Ihre E-Mails mit Inbox Vision zu verwenden, wenn deren Inhalt auf Templates basiert, wie beispielsweise Informationen zum Nutzerprofil. Dies liegt daran, dass Braze ein leeres Template vorlegt, wenn wir E-Mails mit diesem Feature versenden.

Sie können dieses Problem beheben, indem Sie Standardwerte oder beliebige Werte zum Liquid in Ihrer E-Mail-Nachricht hinzufügen, bevor Sie Inbox Vision ausführen. Wenn Sie die Prüfung in Inbox Vision abgeschlossen haben, wird die ursprüngliche E-Mail-Nachricht angezeigt. Wenn keine Werte angegeben werden, kann es vorkommen, dass der Test die Vorschauen nicht erfolgreich rendern kann.

Ihr Unternehmen hat eine Begrenzung hinsichtlich der Anzahl der E-Mails, die Sie mit Inbox Vision in der Vorschau anzeigen können. Sie können dies im Tab **„E-Mail-Vorschau“** vom Posteingang überwachen.

Bitte geben Sie eine Betreffzeile und eine gültige Domain an, um eine Vorschau anzuzeigen. Bitte beachten Sie die Unterschiede zwischen der Darstellung auf Desktop-Computern und Mobilgeräten. Bitte überprüfen Sie anhand der Vorschau, ob die E-Mail wie beabsichtigt angezeigt wird.

Um Ihre E-Mail-Nachricht im Posteingang zu testen:

1. Gehen Sie zu Ihrem Drag-and-Drop-Editor oder HTML-E-Mail-Editor.
2. Bitte wählen Sie in Ihrem Editor **die Option „Vorschau&  Test**“.
3. Wählen Sie **Inbox Vision**.
4. Wählen Sie **Inbox Vision ausführen**. Dies kann bis zu zehn Minuten dauern.
5. Wählen Sie dann eine Kachel aus, um die Vorschau genauer zu betrachten. Diese Vorschauen sind in diese Abschnitte unterteilt: **Internet Clients**, **Anwendungsclients** und **mobile Clients**.

![Die Option, E-Mail-Clients für die Vorschau auszuwählen.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Wählen Sie **Inbox Vision ausführen**. Dieser Vorgang kann zwischen zwei und zehn Minuten in Anspruch nehmen.

{% alert note %}
Inbox Vision unterstützt keine E-Mail-Nachrichten, die [eine Abbruchlogik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) enthalten, da diese E-Mails als statischer Inhalt dargestellt werden.
{% endalert %}

### Vorschau als Nutzer:in

Wenn Sie eine Vorschau als zufällige Nutzer:in anzeigen, speichert Inbox Vision keine benutzerspezifischen Einstellungen oder Attribute (wie Name oder Präferenzen). Wenn Sie einen angepassten Benutzer auswählen, kann die Vorschau von Inbox Vision von anderen Vorschauen abweichen, da sie spezifische Nutzerdaten verwendet.

## Code-Analyse

Die Code-Analyse hebt potenzielle HTML-Probleme hervor, zeigt die Anzahl der Vorkommen an und weist auf nicht unterstützte HTML-Elemente hin.

### Anzeigen von Informationen zur Codeanalyse

Diese Informationen finden Sie auf dem Tab **„Posteingang Vision“,** indem Sie **die Listenansicht**<i class="fas fa-list"></i> auswählen. Die Listenansicht ist nur für HTML-E-Mail-Templates verfügbar. Bei Templates per Drag-and-Drop sollten Sie stattdessen die Vorschau verwenden, um Probleme zu beheben.

![Beispiel einer Code-Analyse in der Inbox Vision Vorschau.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Die Code-Analyse kann für einen bestimmten Client schneller erscheinen als die Vorschau, da Braze wartet, bis die E-Mail eintrifft, bevor der Screenshot erstellt wird.
{% endalert %}

## Spam-Tests

Spam-Tests geben eine Prognose darüber ab, ob Ihre E-Mail im Spam-Ordner oder im Posteingang landet. Braze führt Tests mit den wichtigsten Spam-Filtern (IronPort, SpamAssassin, Barracuda) und den wichtigsten ISP-Filtern (Gmail.com, Outlook.com) durch.

### Anzeigen der Spam-Test-Ergebnisse

Um Ihre Spam-Testergebnisse zu überprüfen:

1. Wählen Sie den Tab **Spam-Test** im Bereich **Inbox Vision**. In der Tabelle **Spam-Test-Ergebnis** sind der Name, der Status und der Typ des Spamfilters aufgeführt.
2. Bitte überprüfen Sie diese Ergebnisse und nehmen Sie gegebenenfalls Anpassungen an Ihrer E-Mail-Kampagne vor.
3. Wählen Sie **Test wiederholen**, um die Ergebnisse Ihres Spam-Tests erneut zu laden.

## Zugänglichkeitstests

Die Barrierefreiheitstests zeigen potenzielle Probleme hinsichtlich der Barrierefreiheit in Ihrer E-Mail auf und weisen darauf hin, welche Elemente nicht den Standards entsprechen. Braze analysiert Inhalte anhand ausgewählter Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), einer Reihe international anerkannter Standards, die vom W3C ausgewählt wurden, um Internet-Inhalte barrierefreier zu gestalten.

### Funktionsweise

Wenn Sie Inbox Vision ausführen, überprüft Braze automatisch häufige Barrierefreiheitsprobleme gemäß den [WCAG 2.2 AA-Richtlinien](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (z. B. fehlender Alt-Text, unzureichender Farbkontrast, ungeeignete Überschriftenstruktur) und kategorisiert den Schweregrad, um Ihnen bei der Priorisierung von Korrekturen zu unterstützen. 

{% alert important %}
Barrierefreiheitstests können verwendet werden, um die Bemühungen der Kund:innen zur Einhaltung von Vorschriften oder Gesetzen wie dem [Europäischen Barrierefreiheitsgesetz](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers) zu unterstützen. Die Kund:innen erkennen an, dass Braze keine Zusicherungen oder Gewährleistungen hinsichtlich der Frage macht, ob die Verwendung von Barrierefreiheitstests die Compliance-Verpflichtungen der Kund:innen erfüllt, und lehnt jede Haftung in diesem Zusammenhang ab.
{% endalert %}

### Anzeigen der Ergebnisse von Zugänglichkeitstests

Bei der Barrierefreiheitstestung werden für jede Regel Ergebnisse im Tab **„Barrierefreiheitstestung“** als „bestanden“, „nicht bestanden“ oder „muss überprüft werden“ angezeigt. Braze kategorisiert jede Regel anhand von POUR (Perceivable, Operable, Understandable, Robust), den vier Grundsätzen hinter WCAG.

#### POUR-Kategorien

Der Posteingang kategorisiert Probleme nach den vier grundlegenden [POUR-Prinzipien](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Wahrnehmbar, bedienbar, verstehbar und robust.

| Prinzip | Definition |
| --- | --- |
| Wahrnehmbar | Informationen und Komponenten der Benutzeroberfläche müssen für die Nutzer:innen auf eine für sie wahrnehmbare Weise darstellbar sein.<br><br>Nutzer:innen müssen in der Lage sein, die dargebotenen Informationen wahrzunehmen (sie dürfen nicht für alle ihre Sinne unsichtbar sein). |
| Bedienbar | Die Komponenten der Benutzeroberfläche und die Navigation müssen bedienbar sein.<br><br>Nutzer:innen müssen in der Lage sein, die Schnittstelle zu bedienen (die Schnittstelle darf keine Interaktion erfordern, die ein Nutzer:innen nicht ausführen kann). |
| Verständlich | Die Informationen und die Bedienung der Benutzeroberfläche müssen verständlich sein.<br><br>Nutzer:innen müssen in der Lage sein, sowohl die Informationen als auch die Bedienung der Benutzeroberfläche zu verstehen (der Inhalt oder die Bedienung darf nicht unverständlich sein). |
| Stabil | Die Inhalte müssen so robust sein, dass sie von einer Vielzahl von Nutzer:innen zuverlässig interpretiert werden können, einschließlich assistiver Technologien.<br><br>Nutzer:innen müssen in der Lage sein, auf die Inhalte zuzugreifen, wenn die Technologien voranbringen (wenn sich die Technologien und Benutzeragenten weiterentwickeln, sollten die Inhalte zugänglich bleiben). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Schweregrade

Inbox Vision klassifiziert Probleme hinsichtlich der Barrierefreiheit nach Schweregrad, um Ihnen bei der Priorisierung von Abhilfemaßnahmen zu unterstützen.

| Status | Definition |
| --- | --- |
| Kritisch | Probleme, die den Zugang zu Inhalten oder Funktionen für Nutzer:innen mit Behinderungen blockieren können. Diese sind am schwerwiegendsten und sollten vorrangig behoben werden. |
| Seriös | Probleme, die erhebliche Hindernisse verursachen können, aber den Zugang nicht vollständig blockieren. Diese sollten umgehend behandelt werden. |
| Moderat | Probleme, die Nutzern:innen mit Behinderungen Schwierigkeiten bereiten können, aber weniger wahrscheinlich den Zugang vollständig blockieren. |
| Geringfügig | Probleme, die eine relativ geringe Auswirkung auf die Zugänglichkeit haben und nur geringfügige Unannehmlichkeiten verursachen können. |
| Braucht Überprüfung | Ich kann nicht feststellen, ob es ein Problem gibt oder nicht. Dies kann vorkommen, wenn wir das Kontrastverhältnis nicht bestimmen können, da der Text auf einem Hintergrundbild platziert ist. Sie müssen die Überprüfung manuell durchführen, da sie nicht automatisch erfolgen kann. |
| Bestanden | Erfüllt WCAG A, AA oder die beste Praxis für Barrierefreiheit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Der Drag-and-Drop-Editor unterstützt die Einstellung eines `<title>`Dokumentelements nicht, sodass der Barrierefreiheitsscanner diese Prüfung stets nicht besteht.<br><br>Dieses Tracking erfolgt im Hinblick auf zukünftige Verbesserungen. Sollte dies Auswirkungen auf Ihre Arbeitsabläufe oder Ihre Nutzer:innen haben, [teilen Sie uns bitte Ihr Feedback mit,]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) damit wir vorrangig wirksame Korrekturen vornehmen können.
{% endalert %}

### Verständnis der automatisierten Zugänglichkeitstests

{% multi_lang_include accessibility/automated_testing.md %}

## Bewährte Praktiken

### Bitte überprüfen Sie Ihre E-Mail-Liste der Abonnent:innen.

Bitte referenzieren Sie das [E-Mail-Insights-Dashboard,]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) um die beliebtesten Gerätetypen und Anbieter zu ermitteln, die das Engagement Ihrer Abonnent:innen fördern. Sollten Sie detailliertere Informationen benötigen, wie beispielsweise den Browser, das Gerätemodell und mehr, können Sie Ihre [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Daten oder [den Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) nutzen, um diese Detailinformationen über das recente Engagement Ihrer Nutzer:innen mit E-Mails abzurufen.

Andernfalls zeigt Braze standardmäßig die 20 besten Vorschauen an, die auf allgemeinen Branchen- und Expertendaten basieren und den Großteil der Bereiche abdecken, in denen Ihre Abonnent:innen mit Ihren E-Mails interagieren. Sollten Ihre Datenanalysen auf andere, populärere Vorschauen hinweisen, können Sie bei jeder Ausführung von Inbox Vision einen Standard-Satz von Vorschauen definieren.

### Bitte wählen Sie aussagekräftige Vorschauen und betroffene Vorschauen aus.

Wenn Ihr Unternehmen hauptsächlich in den USA ansässig ist, kann es spezifische Vorschauen geben, wie beispielsweise internationale Vorschauen,GMX.de die nur von einer geringen Anzahl von Nutzer:innen genutzt werden. Wir empfehlen, Prioritäten zu setzen und sich auf Posteingänge mit einer beträchtlichen Reichweite bei den Abonnent:innen zu konzentrieren und Ihre Vorschauen für Posteingänge mit höherer Reichweite zu reservieren.

Wenn Sie Korrekturen vornehmen, die sich auf bestimmte Vorschauen auswirken, stellen Sie bitte sicher, dass Sie nur die betroffenen Vorschauen auswählen, um zu verhindern, dass nicht verwendete Vorschauen verbraucht werden.

### Führen Sie Inbox Vision auf der endgültigen E-Mail-Version aus.

Wir empfehlen, Inbox Vision auszuführen, wenn die E-Mail-Nachricht produktionsreif ist oder kurz davor steht. Dadurch können Sie die Anzahl der generierten Vorschauen reduzieren, da die E-Mail mehrere Iterationen durchläuft, bevor sie fertiggestellt und an die Nutzer:innen versendet werden kann.

Das Ausführen von Posteingang Vision bei jeder einzelnen Bearbeitung oder Änderung kann die Vorschau schnell überlasten. Wir empfehlen, zunächst alle erforderlichen Änderungen an der E-Mail vorzunehmen und anschließend Inbox Vision auszuführen, um eine Vorschau zu erhalten, wie sich Ihre Änderungen auf die Darstellung Ihrer E-Mail in verschiedenen Umgebungen auswirken können.

Braze führt Tests mit tatsächlichen E-Mail-Clients durch und stellt sicher, dass die Darstellungen korrekt sind. Sollten Sie wiederholt ein Problem mit einem Client feststellen, erstellen Sie bitte ein [Support-Ticket]({{site.baseurl}}/braze_support/).
