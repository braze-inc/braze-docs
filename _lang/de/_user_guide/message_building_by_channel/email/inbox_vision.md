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

> Mit Inbox Vision können Sie Ihre E-Mails aus der Perspektive verschiedener E-Mail-Clients und mobiler Geräte betrachten. Mit Inbox Vision können Sie z. B. die Unterschiede zwischen dem dunklen und dem hellen Modus testen, um sicherzugehen, dass Sie Ihre E-Mails genau richtig formatiert haben.

{% alert important %}
Im Allgemeinen wird Ihre E-Mail nicht mit Inbox Vision funktionieren, wenn Ihr E-Mail-Inhalt auf Template-Informationen beruht, wie z. B. Informationen zum Nutzerprofil. Das liegt daran, dass Braze Templates in einem leeren Nutzer:in erscheinen, wenn wir E-Mails mit diesem Feature versenden.<br><br>Vergewissern Sie sich, dass Sie Standard-Werte für alle Liquids in Ihrer E-Mail Nachricht hinzugefügt haben. Wenn keine Standardwerte angegeben werden, kann es sein, dass Sie ein falsches positives Ergebnis erhalten oder dass der Test nicht ausgeführt werden kann.
{% endalert %}

## Testen Sie Ihre E-Mails in Inbox Vision

Ihre E-Mail muss eine Betreffzeile und eine gültige Domain für den Versand enthalten, damit Sie diese Vorschauen sehen können. Achten Sie darauf, dass Ihre E-Mail auf dem Desktop anders dargestellt werden kann als auf mobilen Geräten. Während Sie diese Vorschauen betrachten, können Sie Ihren Inhalt überprüfen und sicherstellen, dass Ihre E-Mail wie vorgesehen angezeigt wird.

Um Ihre E-Mail Nachrichten in Inbox Vision zu testen, gehen Sie wie folgt vor:

1. Gehen Sie zu Ihrem Drag-and-Drop-Editor oder HTML-E-Mail-Editor.
2. Wählen Sie in Ihrem Editor **Vorschau & Test**.
3. Wählen Sie **Inbox Vision**.
4. Wählen Sie **Inbox Vision ausführen**. Dieser Vorgang kann zwischen zwei und zehn Minuten in Anspruch nehmen.
5. Wählen Sie dann eine Kachel aus, um die Vorschau genauer zu betrachten. Diese Vorschauen sind in diese Abschnitte unterteilt: **Internet Clients**, **Anwendungsclients** und **mobile Clients**.

![Übersicht von Inbox Vision für den HTML-Editor.]({% image_buster /assets/img_archive/inboxvision1.png %})

{: start="6"}
6\. Nehmen Sie ggf. Änderungen an einer Template vor.
7\. Wählen Sie **Test wiederholen**, um die aktualisierten Vorschauen zu sehen.

{% alert note %}
Inbox Vision wird nicht unterstützt, wenn Ihre E-Mail Nachricht eine [Abbruchlogik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) enthält, da diese E-Mails als statischer Inhalt wiedergegeben werden.
{% endalert %}

### Vorschau als Nutzer:in

Wenn Sie eine Vorschau der E-Mail als zufälliger Nutzer:innen erstellen, werden alle spezifischen Einstellungen oder Attribute, die mit einer Nutzerin oder einem Nutzer verbunden sind, wie z. B. Name oder Vorlieben, nicht für die aktuelle oder zukünftige Vorschau gespeichert. Wenn Sie einen angepassten Nutzer auswählen, kann sich die in Inbox Vision angezeigte Vorschau von der Nachrichtenvorschau an anderer Stelle unterscheiden, da diese Option spezifische Nutzerdaten zur Erstellung der Vorschau verwendet.

## Code-Analyse

Die Code-Analyse ist eine Möglichkeit für Braze, Probleme mit Ihrem HTML-Code hervorzuheben. Sie zeigt die Anzahl der Vorkommen der einzelnen Probleme an und gibt Aufschluss darüber, welche HTML-Elemente nicht unterstützt werden.

### Anzeigen von Informationen zur Codeanalyse

Diese Informationen finden Sie auf der Registerkarte **Posteingangsansicht**, indem Sie <i class="fas fa-list"></i> **Listenansicht** wählen. Diese Listenansicht ist nur für HTML-E-Mail-Vorlagen verfügbar. Wenn Sie per Drag-and-Drop erstellte Templates für E-Mails verwenden, überprüfen Sie stattdessen die Vorschauen, um eventuelle Probleme zu beheben.

![Beispiel einer Code-Analyse in der Vorschau von Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Manchmal wird die Codeanalyse schneller angezeigt als die Vorschau für einen bestimmten E-Mail-Client. Das liegt daran, dass Braze wartet, bis die E-Mail im Posteingang angekommen ist, bevor es den Screenshot macht.
{% endalert %}

## Spam-Tests

Mit Spam-Tests wird versucht vorherzusagen, ob Ihre E-Mail in Spam-Ordnern oder im Posteingang Ihrer Kunden landen wird. Die Spam-Tests laufen mit den wichtigsten Spam-Filtern wie IronPort, SpamAssassin und Barracuda sowie mit den Filtern der wichtigsten Internet Service Provider (ISP) wie Gmail.com und Outlook.com.

### Anzeigen der Spam-Test-Ergebnisse

Um die Ergebnisse Ihres Spam-Tests zu überprüfen, gehen Sie wie folgt vor:

1. Wählen Sie den Tab **Spam-Test** im Bereich **Inbox Vision**. In der Tabelle **Spam-Test-Ergebnis** sind der Name, der Status und der Typ des Spamfilters aufgeführt.

![Spam-Test-Ergebnis-Tabelle mit drei Spalten: Name, Status und Typ. Es gibt eine Liste von Spam-Filtern und ISP-Filtern, die den Spam-Test bestanden haben, was bedeutet, dass die E-Mail-Kampagne nicht im Spam-Ordner landet.]({% image_buster /assets/img_archive/email_spam_testing.png %})

{: start="2"}
2\. Überprüfen Sie diese Ergebnisse und nehmen Sie gegebenenfalls Anpassungen an Ihrer E-Mail-Kampagne vor.
3\. Wählen Sie **Test wiederholen**, um die Ergebnisse Ihres Spam-Tests erneut zu laden.

## Zugänglichkeitstests

Die Zugänglichkeitstests in Inbox Vision heben Probleme mit der Zugänglichkeit Ihrer E-Mails hervor und geben Insights darüber, welche Elemente nicht den Zugänglichkeitsstandards entsprechen. Es analysiert Ihre E-Mail-Inhalte anhand einiger Internet Content Accessibility Guidelines[(WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). WCAG ist eine Reihe von international anerkannten technischen Standards, die vom World Wide Web Consortium (W3C) entwickelt wurden, um Webinhalte für Menschen mit Behinderungen zugänglicher zu machen. 

### Funktionsweise

Wenn Sie einen Inbox Vision-Test durchführen, prüft das Tool automatisch auf gängige Probleme bei der Barrierefreiheit von E-Mails gemäß [WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa), wie z. B. fehlender Alt-Text, unzureichender Farbkontrast und falsche Überschriftenstruktur, und kategorisiert dann den Schweregrad jedes Problems, um Ihnen bei der Priorisierung von Korrekturen zu helfen. 

{% alert important %}
Der Kunde erkennt jedoch an, dass Braze keine Zusicherungen oder Garantien in Bezug darauf abgibt, ob die Verwendung der Zugänglichkeitstests die Verpflichtungen des Kunden erfüllt oder nicht, und lehnt jegliche Haftung in diesem Zusammenhang ab.
{% endalert %}

### Anzeigen der Ergebnisse von Zugänglichkeitstests

Die Zugänglichkeitstests erzeugen Ergebnisse für jede Regel als bestanden, nicht bestanden oder überarbeitungsbedürftig auf dem Tab **Zugänglichkeitstests**. Jede Regel wird anhand von POUR (Perceivable, Operable, Understandable, Robust) kategorisiert, den vier Hauptprinzipien der WCAG.

#### POUR-Kategorien

Die Themen werden unter den vier grundlegenden [POUR-Prinzipien](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) kategorisiert: Wahrnehmbar, bedienbar, verstehbar und robust. Jedes Prinzip behandelt einen anderen Aspekt des barrierefreien Designs.

| Prinzip | Definition |
| --- | --- |
| Wahrnehmbar | Informationen und Komponenten der Benutzeroberfläche müssen für die Nutzer:innen auf eine für sie wahrnehmbare Weise darstellbar sein.<br><br>Nutzer:innen müssen in der Lage sein, die dargebotenen Informationen wahrzunehmen (sie dürfen nicht für alle ihre Sinne unsichtbar sein). |
| Bedienbar | Die Komponenten der Benutzeroberfläche und die Navigation müssen bedienbar sein.<br><br>Nutzer:innen müssen in der Lage sein, die Schnittstelle zu bedienen (die Schnittstelle darf keine Interaktion erfordern, die ein Nutzer:innen nicht ausführen kann). |
| Verständlich | Die Informationen und die Bedienung der Benutzeroberfläche müssen verständlich sein.<br><br>Nutzer:innen müssen in der Lage sein, sowohl die Informationen als auch die Bedienung der Benutzeroberfläche zu verstehen (der Inhalt oder die Bedienung darf nicht unverständlich sein). |
| Stabil | Die Inhalte müssen so robust sein, dass sie von einer Vielzahl von Nutzer:innen zuverlässig interpretiert werden können, einschließlich assistiver Technologien.<br><br>Nutzer:innen müssen in der Lage sein, auf die Inhalte zuzugreifen, wenn die Technologien voranbringen (wenn sich die Technologien und Benutzeragenten weiterentwickeln, sollten die Inhalte zugänglich bleiben). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Schweregrade

Inbox Vision klassifiziert Zugänglichkeitsprobleme nach ihrem Schweregrad und hilft Ihnen so bei der Priorisierung von Abhilfemaßnahmen.

| Status | Definition |
| --- | --- |
| Kritisch | Probleme, die den Zugang zu Inhalten oder Funktionen für Nutzer:innen mit Behinderungen blockieren können. Diese sind am schwerwiegendsten und sollten vorrangig behoben werden. |
| Seriös | Probleme, die erhebliche Hindernisse verursachen können, aber den Zugang nicht vollständig blockieren. Diese sollten umgehend behandelt werden. |
| Moderat | Probleme, die Nutzern:innen mit Behinderungen Schwierigkeiten bereiten können, aber weniger wahrscheinlich den Zugang vollständig blockieren. |
| Geringfügig | Probleme, die eine relativ geringe Auswirkung auf die Zugänglichkeit haben und nur geringfügige Unannehmlichkeiten verursachen können. |
| Braucht Überprüfung | Ich kann nicht feststellen, ob es ein Problem gibt oder nicht. Dies kann vorkommen, wenn wir das Kontrastverhältnis nicht bestimmen können, da der Text auf einem Hintergrundbild platziert ist. Dies muss manuell überprüft werden, da es nicht automatisch ermittelt werden kann. |
| Bestanden | Erfüllt WCAG A, AA oder die beste Praxis für Barrierefreiheit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Der E-Mail Drag-and-Drop-Editor unterstützt derzeit nicht die Einstellung eines Dokuments `<title>` Element. Daher wird der Barrierefreiheits-Scanner diese Prüfung immer nicht bestehen.<br><br>
Wir tracken diese Einschränkung für zukünftige Verbesserungen. Wenn dies Ihre Arbeitsabläufe oder Ihre Nutzer:innen betrifft, [teilen Sie uns Ihr Feedback mit]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback), damit wir die wirksamsten Korrekturen priorisieren können.
{% endalert %}

### Verständnis der automatisierten Zugänglichkeitstests

{% multi_lang_include accessibility/automated_testing.md %}

## Test Genauigkeit

Alle unsere Tests werden mit echten E-Mail-Clients durchgeführt. Braze arbeitet hart, um sicherzustellen, dass alle Renderings so genau wie möglich sind. Wenn Sie immer wieder ein Problem mit einem E-Mail-Client haben, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).
