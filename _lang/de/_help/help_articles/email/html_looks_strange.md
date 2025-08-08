---
nav_title: HTML-Rendering in Test-E-Mails
article_title: HTML-Rendering in Test-E-Mails
page_order: 2

page_type: solution
description: "In diesem Hilfeartikel erfahren Sie, wie Sie Fehlerbehebungen bei der HTML-Darstellung in Test-E-Mails vornehmen können."
channel: email
---

# Fehlerbehebung bei der HTML-Darstellung in Test-E-Mails

Wenn Ihre [Test E-Mail]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) nicht gut aussieht, empfehlen wir Ihnen, zunächst Ihre HTML-Einstellungen zu überprüfen. Als Nächstes können Sie nach diesen Problemen suchen:
* [Konflikte bei der Verlängerung](#check-conflicts)
* [Rendering von E-Mails](#check-rendering)
* [CSS-Inlining](#switch-css-inlining)

### Konflikte bei der Verlängerung

Bestimmte Browser-Erweiterungen können Probleme mit unserem E-Mail-Editor verursachen. Ein Beispiel ist [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)), wenn es mit Google Chrome verwendet wird. Wenn Sie eine dieser Erweiterungen verwenden, sollten Sie entweder: 
- Bearbeiten Sie E-Mails von Braze in einem Browser, der nicht über Grammarly als Browsererweiterung verfügt
- Wenden Sie sich an Ihren Braze-Konto Manager:in und bitten Sie darum, Ihre E-Mail-Editoren auf HTML oder reinen Text umzustellen. 

Die reine Textansicht entfernt Ihren ```WYSIWYG``` (what you see is what you get) Editor. Daher sollten Sie sich zunächst vergewissern, dass alle Teammitglieder mit HTML vertraut sind, bevor Sie diese Anfrage stellen.

### Rendering von E-Mails

E-Mails werden je nach Browser und E-Mail Client unterschiedlich dargestellt. Notieren Sie sich also, mit welchen Browsern und E-Mail Clients Sie Probleme haben.

- Mit [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) erhalten Sie eine Vorschau Ihrer E-Mails, um zu sehen, wie Ihre E-Mails in verschiedenen Browsern und Clients aussehen.
- Nachdem Sie herausgefunden haben, welche Browser oder E-Mail-Clients Probleme verursachen, teilen Sie Ihrem Entwickler:in Team mit, dass es seinen HTML-Code anpassen und Änderungen vornehmen muss, um diese Browser oder E-Mail-Clients zu unterstützen.

### CSS-Inlining

Es kommt vor, dass die Vorschauen in Inbox Vision immer noch nicht mit dem übereinstimmen, was mit Braze gesendet wird. Dies kann auf den Unterschied beim CSS-Inlining durch Braze und andere Tools zurückzuführen sein. Wenn Sie vermuten, dass dies der Fall ist, wenden Sie sich an Ihren Braze-Konto Manager:in, um das CSS-Inlining zu deaktivieren.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 21\. Dezember 2021_

