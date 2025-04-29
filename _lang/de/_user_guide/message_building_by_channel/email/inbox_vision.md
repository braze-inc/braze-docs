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
Im Allgemeinen wird Ihre E-Mail nicht mit Inbox Vision funktionieren, wenn Ihr E-Mail-Inhalt auf Template-Informationen beruht, wie z. B. Informationen zum Nutzerprofil. Das liegt daran, dass Braze Templates in einem leeren Nutzer:in erscheinen, wenn wir E-Mails mit diesem Feature versenden.
{% endalert %}

## Testen Sie Ihre E-Mails in Inbox Vision

Ihre E-Mail muss eine Betreffzeile und eine gültige Domain für den Versand enthalten, damit Sie diese Vorschauen sehen können. Achten Sie darauf, dass Ihre E-Mail auf dem Desktop anders dargestellt werden kann als auf mobilen Geräten. Während Sie diese Vorschauen betrachten, können Sie Ihren Inhalt überprüfen und sicherstellen, dass Ihre E-Mail wie vorgesehen angezeigt wird.

Um Ihre E-Mail Nachrichten in Inbox Vision zu testen, gehen Sie wie folgt vor:

1. Gehen Sie zu Ihrem Drag-and-Drop-Editor oder HTML-E-Mail-Editor.
2. Wählen Sie in Ihrem Editor **Vorschau und Test**.
3. Wählen Sie **Inbox Vision**. 
4. Wählen Sie **Inbox Vision ausführen**. Dieser Vorgang kann zwischen zwei und zehn Minuten in Anspruch nehmen.
5. Wählen Sie dann eine Kachel aus, um die Vorschau genauer zu betrachten. Diese Vorschauen sind in diese Abschnitte unterteilt: **Internet Clients**, **Anwendungsclients** und **mobile Clients**.

![Übersicht über die Inbox Vision für den HTML-Editor.][1]

{: start="6"}
6\. Nehmen Sie ggf. Änderungen an einer Template vor.
7\. Wählen Sie **Test wiederholen**, um die aktualisierten Vorschauen zu sehen.

### Vorschau als Nutzer:in

Wenn Sie eine Vorschau der E-Mail als zufälliger Nutzer:innen erstellen, werden alle spezifischen Einstellungen oder Attribute, die mit einer Nutzerin oder einem Nutzer verbunden sind, wie z. B. Name oder Vorlieben, nicht für die aktuelle oder zukünftige Vorschau gespeichert. Wenn Sie eine:n angepasste:n Nutzer:in auswählen, kann sich die in Inbox Vision angezeigte Vorschau von der Nachrichtenvorschau an anderer Stelle unterscheiden, da diese Option spezifische Nutzerdaten zur Erstellung der Vorschau verwendet.

## Code-Analyse

Die Code-Analyse ist eine Möglichkeit für Braze, Probleme mit Ihrem HTML-Code hervorzuheben. Sie zeigt die Anzahl der Vorkommen der einzelnen Probleme an und gibt Aufschluss darüber, welche HTML-Elemente nicht unterstützt werden. 

### Anzeigen von Informationen zur Codeanalyse

Diese Informationen finden Sie auf der Registerkarte **Posteingangsansicht**, indem Sie <i class="fas fa-list"></i> **Listenansicht** wählen. Diese Listenansicht ist nur für HTML-E-Mail-Vorlagen verfügbar. Wenn Sie per Drag-and-Drop erstellte Templates für E-Mails verwenden, überprüfen Sie stattdessen die Vorschauen, um eventuelle Probleme zu beheben.

![Beispiel einer Code-Analyse in der Inbox Vision Vorschau.][2]

{% alert note %}
Manchmal wird die Codeanalyse schneller angezeigt als die Vorschau für einen bestimmten E-Mail-Client. Das liegt daran, dass Braze wartet, bis die E-Mail im Posteingang angekommen ist, bevor es den Screenshot macht.
{% endalert %}

## Spam-Tests

Mit Spam-Tests wird versucht vorherzusagen, ob Ihre E-Mail in Spam-Ordnern oder im Posteingang Ihrer Kunden landen wird. Die Spam-Tests laufen mit den wichtigsten Spam-Filtern wie IronPort, SpamAssassin und Barracuda sowie mit den Filtern der wichtigsten Internet Service Provider (ISP) wie Gmail.com und Outlook.com.

### Anzeigen der Spam-Test-Ergebnisse

Um die Ergebnisse Ihres Spam-Tests zu überprüfen, gehen Sie wie folgt vor:

1. Wählen Sie den Tab **Spam-Test** im Bereich **Inbox Vision**. In der Tabelle **Spam-Test-Ergebnis** sind der Name, der Status und der Typ des Spamfilters aufgeführt.

![Spam-Test-Ergebnis-Tabelle mit drei Spalten: Name, Status und Typ. Es gibt eine Liste von Spam-Filtern und ISP-Filtern, die den Spam-Test bestanden haben, was bedeutet, dass die E-Mail-Kampagne nicht im Spam-Ordner landet.][4]

{: start="2"}
2\. Überprüfen Sie diese Ergebnisse und nehmen Sie gegebenenfalls Anpassungen an Ihrer E-Mail-Kampagne vor.
3\. Wählen Sie **Test wiederholen**, um die Ergebnisse Ihres Spam-Tests erneut zu laden.

## Test Genauigkeit

Alle unsere Tests werden mit echten E-Mail-Clients durchgeführt. Braze arbeitet hart, um sicherzustellen, dass alle Renderings so genau wie möglich sind. Wenn Sie immer wieder ein Problem mit einem E-Mail-Client haben, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}
