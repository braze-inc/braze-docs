---
nav_title: HTML-Rendering in Test-E-Mails
article_title: HTML-Rendering in Test-E-Mails
page_order: 2

page_type: solution
description: "Dieser Hilfeartikel zeigt Ihnen, wie Sie Probleme mit der HTML-Darstellung in Test-E-Mails beheben können."
channel: email
---

# Fehlerbehebung bei der HTML-Darstellung in Test-E-Mails

Wenn Ihre [Test-E-Mail][37] falsch aussieht, empfehlen wir Ihnen, zunächst Ihre HTML-Einstellungen zu überprüfen. Als Nächstes können Sie nach diesen Problemen suchen:
* [Konflikte bei der Verlängerung](#check-conflicts)
* [E-Mail-Rendering](#check-rendering)
* [CSS-Inlining](#switch-css-inlining)

### Konflikte bei der Verlängerung

Bestimmte Browser-Erweiterungen können Probleme mit unserem E-Mail-Editor verursachen. Ein Beispiel ist [Grammarly][38]), wenn es mit Google Chrome verwendet wird. Wenn Sie eine dieser Erweiterungen verwenden, sollten Sie entweder: 
- Bearbeiten Sie Braze-E-Mails in einem Browser, in dem Grammarly nicht als Browsererweiterung installiert ist.
- Wenden Sie sich an Ihren Braze-Kundenbetreuer und bitten Sie darum, Ihre E-Mail-Editoren auf HTML oder reinen Text umzustellen. 

Die reine Textansicht entfernt Ihren ```WYSIWYG``` (what you see is what you get) Editor. Daher sollten Sie sich zunächst vergewissern, dass alle Teammitglieder mit HTML vertraut sind, bevor Sie diese Anfrage stellen.

### E-Mail-Rendering

E-Mails werden je nach Browser und E-Mail-Client unterschiedlich dargestellt. Notieren Sie sich also, mit welchen Browsern und E-Mail-Clients Sie Probleme haben.

- Zeigen Sie mit [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) eine Vorschau Ihrer E-Mails an, um zu sehen, wie Ihre E-Mails in verschiedenen Browsern und E-Mail-Clients aussehen.
- Nachdem Sie herausgefunden haben, welche Browser oder E-Mail-Clients Probleme verursachen, teilen Sie Ihrem Entwicklerteam mit, dass sie ihren HTML-Code ändern müssen, um diese Browser oder E-Mail-Clients zu unterstützen.

### CSS-Inlining

Es kann vorkommen, dass die Vorschauen in Inbox Vision nicht mit dem übereinstimmen, was mit Braze gesendet wird. Dies kann auf den Unterschied beim CSS-Inlining von Braze und anderen Tools zurückzuführen sein. Wenn Sie vermuten, dass dies der Fall ist, wenden Sie sich an Ihren Braze-Kundenbetreuer und bitten Sie darum, das CSS-Inlining zu deaktivieren.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 21\. Dezember 2021_

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
