---
nav_title: Fehlersuche
article_title: Fehlerbehebung Braze Access
page_order: 8
page_type: reference
description: "Dieser Artikel führt Sie durch die Fehlerbehebung von Problemen, die beim Zugriff auf Braze auftreten können."

---

# Fehlerbehebung Braze Zugang

> Dieser Artikel hilft Ihnen bei der Fehlerbehebung von Problemen, die beim Zugriff auf Braze auftreten können.

## Aus dem Konto ausgesperrt

Sie haben sich also aus Ihrem Braze-Konto ausgesperrt - keine Sorge! Wir können Ihnen helfen, wieder einzusteigen.	

Welche Art von Sperre bei Ihnen vorliegt, erkennen Sie an der Fehlermeldung, die Sie erhalten:	

- [Ich sehe eine Fehlermeldung bezüglich meines Passworts.](#password-error)	
- [Ich sehe keinen Fehler, aber Braze lässt mich trotzdem nicht rein.](#instance-error)	
- [Ich sehe einen Fehler bezüglich der Kontosperrung.](#account-suspension)	

### Passwort-Fehler

Die Sicherheit Ihres Kontos ist uns sehr wichtig. Deshalb benötigen Sie ein Passwort, um sich bei Ihrem Braze-Konto anzumelden.	
- Überprüfen Sie, ob Sie sich bei der richtigen [Braze-Dashboard-Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) anmelden. Erkundigen Sie sich bei Ihrem Account Administrator oder Braze-Konto Manager:in, um sicherzugehen.	
- Möglicherweise ist Ihr Passwort abgelaufen, so dass Sie [es zurücksetzen]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password) müssen.	
- Wenn Sie einen [Single Sign-on]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) Dienst verwenden, überprüfen Sie mit Ihrem Kontoverwalter, ob die Einrichtung ordnungsgemäß abgeschlossen wurde.	
- Wenn Ihr Unternehmen auf mehreren Instanzen von Braze vertreten ist, verwenden Sie möglicherweise die falsche E-Mail für die Anmeldung.  	

Im Zweifelsfall können Sie [Ihr Passwort]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password) jederzeit [zurücksetzen]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	

### Fehler in der Instanz

Wenn Sie denselben Rechner verwenden, auf dem Sie sich normalerweise anmelden, sollte Braze automatisch die richtige Instanz erkennen. Sollte dies jedoch nicht der Fall sein oder sollten Sie sich zum ersten Mal anmelden, empfehlen wir Ihnen, Folgendes zu beachten:	

- Überprüfen Sie, ob Sie sich bei der richtigen [Braze-Dashboard-Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) anmelden. Erkundigen Sie sich bei Ihrem Account Administrator oder Braze-Konto Manager:in, um sicherzugehen.
- Wenn Ihr Unternehmen auf mehreren Instanzen von Braze vertreten ist, verwenden Sie möglicherweise die falsche E-Mail für die Anmeldung.	

### Kontoaussetzung	

Das passiert nicht sehr oft, aber wir nehmen die Sperrung und Löschung von Konten sehr ernst. Wenn dieser Fehler auftritt, empfehlen wir Ihnen, sich an den Braze-Administrator Ihres Unternehmens, den Braze-Konto Manager:in oder den [Support][support] zu wenden.

## Braze-Dashboard wird nicht geladen oder funktioniert nicht wie erwartet

Testen Sie zunächst, ob das Dashboard in einem anderen Browser geladen werden kann. Wenn das Problem in einem anderen Browser nicht persistent ist, versuchen Sie Folgendes:

- **Starten Sie das Dashboard neu:** Melden Sie sich ab, beenden Sie Ihren Browser und versuchen Sie dann, sich bei Ihrem Dashboard anzumelden.
- **Aktualisieren Sie Ihren lokalen Browser:** [Löschen Sie Ihre Cookies und Ihren Browser-Cache]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies) und versuchen Sie dann erneut, sich in Ihrem Dashboard anzumelden.
- **Verwenden Sie kompatible Plugins oder Tools von Drittanbietern:** Werbeblocker oder Sicherheitssoftware können verhindern, dass das Braze-Dashboard geladen wird. Testen Sie dies, indem Sie einen Werbeblocker deaktivieren und sich dann bei Ihrem Braze-Dashboard anmelden.
        \- Sie können auch die Protokolle Ihrer Browser-Konsole überprüfen. Fehler im Zusammenhang mit `ERR_BLOCKED_BY_CLIENT` können darauf hinweisen, dass der Inhalt durch einen Werbeblocker blockiert wird.
- **Prüfen Sie die Qualität Ihrer Verbindung:** Die Qualität Ihrer Verbindung ist möglicherweise schlecht. Versuchen Sie, sich auf einem anderen Gerät bei Ihrem Braze-Dashboard anzumelden.
- **Vergewissern Sie sich, dass Sie auf den richtigen Cluster zugreifen:** Vergewissern Sie sich, dass Sie sich bei dem Cluster anmelden, der Ihrem Unternehmen zugewiesen ist. Sie können zum Beispiel US-03 zugewiesen sein, sich aber bei US-01 anmelden.
- **Aktualisieren Sie Ihren Browser:** Aktualisieren Sie Ihren Browser auf den neuesten [unterstützten Browser]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers) und versuchen Sie dann, sich bei Ihrem Dashboard anzumelden.

Wenn das Problem bei allen Browsern auftritt, versuchen Sie Folgendes:

- **Überprüfen Sie Ihre Netzwerkverbindung:** Versuchen Sie, Ihr VPN auszuschalten, falls möglich, oder deaktivieren Sie Ihre Netzwerkverbindung und aktivieren Sie sie wieder.
- **Starten Sie Ihr Gerät neu:** Versuchen Sie, sich nach dem Neustart Ihres Geräts bei Ihrem Braze-Dashboard anzumelden.

Wenn Sie die oben genannten Probleme gelöst haben und Ihr Dashboard immer noch nicht lädt oder nicht wie erwartet funktioniert, wenden Sie sich an den [Support]({{site.baseurl}}/braze_support/).

## Der Nutzer:in gehört zu keinem Workspace

Überprüfen Sie dies, indem Sie unter **Einstellungen** > **Benutzer im Unternehmen** die Berechtigungen des Nutzers:innen auf Workspace-Ebene überprüfen. Fügen Sie die erforderlichen Workspaces zu **Workspaces** hinzu.

## Fehlerbehebung als neuer Nutzer:in

Wenn Sie ein neuer Nutzer:innen von Braze sind und Probleme bei der Anmeldung oder beim ersten Zugriff auf Ihr Konto haben, befolgen Sie diese Schritte, um die häufigsten Probleme zu lösen:

### Ich habe die Willkommens-E-Mail nie erhalten

- Prüfen Sie Ihren Spam-Ordner: Vergewissern Sie sich, dass die E-Mail zur Kontoaktivierung nicht in Ihren Spam- oder Junk-Ordner gefiltert wurde.
- Überprüfen Sie Ihre E-Mail Adresse: Bitten Sie Ihren Administrator, die mit Ihrem neuen Braze-Konto verknüpfte E-Mail Adresse zu überprüfen, um sicherzustellen, dass sie korrekt ist.
- IT-Richtlinien: Vergewissern Sie sich bei Ihrem IT Team, dass es keine Richtlinien gibt, die den Empfang der Aktivierungs-E-Mail verhindern könnten.

### Ich habe die E-Mail erhalten, aber ich kann die Zwei-Faktor-Authentifizierung (2FA) nicht einrichten.

- 2FA zurücksetzen: Wenn Sie Probleme bei der Einrichtung von 2FA haben, kann Ihr Administrator 2FA für Ihr Nutzer:in-Konto in den Einstellungen zurücksetzen.
- Nutzer:in neu hinzufügen: Wenn die Probleme persistent sind, kann der Administrator Ihr Nutzer:in-Konto aus dem Dashboard löschen und Sie erneut hinzufügen. Dies erlaubt die Erstellung eines Nutzers:in mit denselben Details.

Wenn die Probleme nach diesen Schritten weiterhin bestehen, wenden Sie sich bitte an den [Support]({{site.baseurl}}/braze_support/) für weitere Unterstützung.