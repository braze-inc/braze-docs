---
nav_title: Bitte melden Sie sich bei Ihrem Konto an.
article_title: Zugriff auf Ihr Konto
page_order: 0
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie Ihr Braze-Konto erhalten, wie Sie sich nach der Freischaltung anmelden und wie Sie Ihr Braze-Passwort zurücksetzen können."

---

# Bitte melden Sie sich bei Ihrem Konto an.

> In diesem Artikel erfahren Sie, wie Sie Ihr Braze-Konto erhalten, wie Sie sich anmelden, nachdem Sie Zugang erhalten haben, und wie Sie Fehlerbehebungen für Ihren Dashboard-Zugang und die Performance des Dashboards vornehmen können.

Wenn Sie der erste Braze-Benutzer in Ihrem Unternehmen sind und sich zum ersten Mal anmelden, erhalten Sie eine Willkommens-E-Mail von `@alerts.braze.com`, in der Sie aufgefordert werden, Ihre E-Mail zu bestätigen und sich am ersten Tag Ihres Vertrags anzumelden.

Nachdem Sie Ihr Konto bestätigt haben, können Sie auf der Seite [Nutzer:innen des Unternehmens]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) auf Ihrem Dashboard weitere Nutzer:innen hinzufügen. Alle Nutzer:innen erhalten eine E-Mail, in der sie aufgefordert werden, ihr Konto zu bestätigen, nachdem sie hinzugefügt worden sind.

Wenn Sie nicht der erste Nutzer:innen auf dem Braze-Konto Ihres Unternehmens sind, wenden Sie sich an den Braze-Kontoverwalter Ihres Unternehmens und bitten Sie ihn, Ihr Konto zu erstellen. Sie erhalten dann eine Willkommens-E-Mail von `@alerts.braze.com`, in der Sie aufgefordert werden, Ihre E-Mail zu bestätigen und sich anzumelden.

## Einloggen

Lassen Sie uns darüber sprechen, wie Sie sich anmelden, egal ob es das erste oder das millionste Mal ist! Wenn Sie der erste Benutzer in Ihrem Unternehmen sind, befolgen Sie die Hinweise im vorangehenden Abschnitt. Falls nicht, können Sie sich anmelden, nachdem der Braze-Administrator Ihres Unternehmens Ihr Konto erstellt hat.

Sie können sich entweder von der [Braze.com](https://www.braze.com) Home-Site anmelden, oder Sie verwenden einfach die URL Ihres Dashboards, das Ihrer speziellen [Braze-Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) entspricht. Braze bietet Ihnen verschiedene Single Sign-on (SSO)-Optionen, wie zum Beispiel:

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [SAML Just-in-Time-Bereitstellung]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
Nachdem Sie sich bei Braze mit SSO angemeldet haben, können Sie sich nicht mehr mit Ihrem Passwort beim Dashboard anmelden.
{% endalert %}

## Unterstützte Browser

Das Braze Dashboard unterstützt die folgenden Browser:
- Chrome (Version 87 oder neuer)
- Firefox (Version 85 oder neuer)
- Safari (Version 15.4 oder neuer)
- Edge (Version 87 oder neuer)

Wenn Ihr Braze-Dashboard einen unerwarteten Fehler meldet und Ihr Browser-Konsolentool den Fehler `ReferenceError: structuredClone is not defined` anzeigt, ist Ihr Browser veraltet. Wenn dieser Fehler immer wieder auftritt, deinstallieren Sie Ihren Browser und installieren Sie ihn neu.

## Zugriff auf mehrere Braze-Dashboards

Braze erlaubt es nicht, dieselbe E-Mail-Adresse für mehrere Dashboard-Nutzer:innen im selben Cluster zu registrieren (zum Beispiel, wenn Sie zwei Dashboards auf US-01 haben). Sie können dieselbe E-Mail-Adresse verwenden, um Konten auf verschiedenen Clustern zu erstellen (beispielsweise, wenn Sie ein Dashboard auf US-01 und eines auf US-05 haben). Wenn Sie auf mehrere Braze-Dashboards im selben Cluster zugreifen müssen, können Sie wie folgt vorgehen:

### Verwenden Sie E-Mail-Aliase

Wenn Sie Gmail als E-Mail-Anbieter verwenden, können Sie Aliase erstellen, indem Sie ein`+`@-Zeichen gefolgt von einem beliebigen Text an Ihre E-Mail-Adresse anhängen. Zum Beispiel:
- **Original-E-Mail:** `rocky@gmail.com`
- **Alias-E-Mail:** `rocky+1@gmail.com`

Beide E-Mail-Adressen leiten E-Mails an denselben Posteingang weiter, jedoch erkennt Braze sie beim Einloggen als separate Konten.

### Erstellen Sie separate Aliase bei anderen Anbietern.

Sollte Ihr E-Mail-Anbieter keine Aliase`+` unterstützen, können Sie dennoch separate Aliase erstellen, beispielsweise indem Sie eine Weiterleitung`rocky@braze.com`von zu einrichten`rocky.lotito@braze.com`. Dadurch ist es zulässig, dass mehrere Adressen in denselben Posteingang weitergeleitet werden, während sie von Braze als unterschiedliche E-Mails erkannt werden.

### Entwickler:innen aus mehreren Unternehmen einsetzen

Die Features für Entwickler:innen ermöglichen die gemeinsame Nutzung eines einzigen Benutzerkontos durch mehrere Unternehmen. Nutzer:innen können über das Menü ihres Nutzerprofils zwischen verschiedenen Unternehmens-Dashboards umschalten.

Wenn Sie SSO verwenden und Entwickler:innen für mehrere Unternehmen einrichten möchten, müssen Sie eine angepasste SAML-Entitäts-ID aktivieren, indem Sie eine angepasste SAML-SSO-Integration einrichten. Befolgen Sie die Schritte für [die vom Dienstanbieter (SP) initiierte Anmeldung]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), jedoch mit folgenden Änderungen:
- Ändern Sie **die Entitäts-ID** für jede `braze_dashboard_<companyID>`Dashboard-Integration in .
- Bitte wenden Sie sich an Ihren Customer-Success-Manager oder Account Manager, um die`saml_sso_custom_entity_id`Feature-Flipper-Funktion für jedes Dashboard zu aktivieren.

### Überlegungen zum Single Sign-on (SSO)

Bitte beachten Sie, dass bei Verwendung von Single Sign-on (SSO) die Verwendung mehrerer unterschiedlicher E-Mail-Adressen zu Komplikationen führen kann. Bitte überprüfen Sie, ob Ihre SSO-Einstellungen korrekt konfiguriert sind, um Zugriffsprobleme zu vermeiden.

## Fehlersuche

### Ihr Passwort zurücksetzen

Um Ihr Passwort zurückzusetzen, wählen Sie den Link **Passwort vergessen?** auf der Dashboard-Anmeldeseite. Sie werden aufgefordert, Ihre E-Mail einzugeben, um einen Link zum Zurücksetzen Ihres Passworts zu erhalten.

![Anmeldung beim Dashboard mit der Aufforderung „Passwort vergessen?“.]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Löschen des Cache und der Cookies Ihres Browsers

Wenn Sie Probleme mit der Performance des Dashboards haben, z.B. wenn Ihre Performance-Liste des Dashboards oder der Segmente nicht geladen wird, versuchen Sie, Ihren Browser-Cache und Ihre Cookies zu löschen, indem Sie die Schritte für Ihren jeweiligen Browser befolgen.

{% alert important %}
Wenn Sie Cookies löschen, werden Sie abgemeldet, so dass ungespeicherte Arbeit verloren geht.
{% endalert %}

- [Bitte löschen Sie die &Cookies im Cache von Chrome.](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Cookies in Safari auf dem Mac löschen](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Cookies und Daten der Website in Firefox löschen](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Alle Cookies in Microsoft Edge löschen](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Wenn das Löschen Ihres Browser-Caches und Ihrer Cookies Ihre Probleme nicht löst, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact/).

### Zugriff auf den Drag-and-Drop-Editor

Für die meisten Unternehmensnutzer:innen sollte der Drag-and-Drop-Editor geladen werden. Wenn Sie jedoch ein VPN verwenden oder sich hinter einer Firewall befinden, müssen Sie möglicherweise eine Domain in der Liste zulassen. Wenden Sie sich an Ihren IT-Administrator, um zu überprüfen, ob `*.bz-rndr.com` in der Liste der zulässigen Anwendungen aufgeführt ist.

Beim Laden des Editors kann es aus folgenden Gründen zu Problemen kommen:

- **Vorübergehender Fehler:** Dabei handelt es sich um vorübergehende Ausfälle, die die Konnektivität, die Kommunikation oder die Übertragung von Daten beeinträchtigen können. Glücklicherweise lösen sie sich in der Regel von selbst auf, ohne dass ein nennenswerter Eingriff erforderlich ist, da sie oft durch kurzlebige Bedingungen verursacht werden und nicht auf systemische Probleme hinweisen.
- **Schwerer Fehler:** Dies kann ein Problem mit der Infrastruktur oder dem Produkt sein.  Sie können auf unserer [Braze-Systemstatusseite](https://braze.statuspage.io/) nachsehen, da uns das Problem wahrscheinlich bekannt ist und wir aktiv an einer Lösung arbeiten.

{% alert important %}
Wenn Sie immer noch Probleme haben, [öffnen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Vergewissern Sie sich zuvor, dass Ihr IT-Administrator bestätigt hat, dass `*.bz-rndr.com` auf Ihrer Seite zugelassen ist.
{% endalert %}

### Zugriff auf die Lernangebote von Braze

Sollten Sie Probleme beim Einloggen in Braze Learning haben und sich in einer Schleife befinden, die Sie immer wieder zum Dashboard weiterleitet, führen Sie bitte die folgenden Schritte aus:

1. Sollten Sie mehrere Braze-Konten besitzen, werden Sie nach zweimaliger Anmeldung mit dem falschen Konto zum Braze-Dashboard weitergeleitet. Bitte stellen Sie sicher, dass Sie sich bei dem richtigen Konto anmelden. 
2. Falls Sie einen Werbeblocker verwenden, überprüfen Sie bitte, ob dieser deaktiviert ist. Es kann vorkommen, dass Cookies blockiert werden, die für die Single Sign-on-Funktionalität erforderlich sind.
3. Bitte gehen Sie zu „Unternehmenseinstellungen“ > „Sicherheitseinstellungen“ und überprüfen Sie, ob Single Sign-on (SSO) aktiviert ist.
4. Bitte stellen Sie sicher, dass Ihr Dashboard-Nutzerprofil sowohl Ihren Vornamen als auch Ihren Nachnamen enthält. Das Fehlen eines Nachnamens kann die Anmeldung beeinträchtigen.
5. Bitte greifen Sie über Ihr Dashboard auf die Lernangebote von Braze zu, indem Sie zu **„Support“** > **„Braze Learning“** navigieren. 
6. Sollten weiterhin Probleme auftreten, empfehlen wir Ihnen, Ihr Konto neu zu erstellen. Nutzer:innen, die während der kostenlosen Demo auf Braze Learning zugegriffen haben, könnten derzeit Schwierigkeiten beim Zugriff haben.

### Probleme mit der Zwei-Faktor-Authentifizierung (2FA)

Sollte eine Nutzer:in Probleme mit der Zwei-Faktor-Authentifizierung (2FA) haben und keinen Zugriff auf das Braze-Dashboard erhalten, kann dies verschiedene Ursachen haben. In den meisten Fällen haben sie möglicherweise keinen Zugriff mehr auf die registrierte Telefonnummer oder das Gerät, auf dem die Authy-App installiert ist.

Ein Administrator sollte die 2FA für die betroffene Nutzer:in wie folgt zurücksetzen: 

1. Bitte gehen Sie zu **„Nutzer:innen verwalten**”.
2. Bitte wählen Sie **„Benutzer bearbeiten“** für den Nutzer:in, bei dem Probleme mit der 2FA auftreten.
3. Bitte wählen Sie die Option zum Zurücksetzen der 2FA.
4. Bitte bestätigen Sie die 2FA-Zurücksetzung, wenn Sie dazu aufgefordert werden.
5. Sollte das Zurücksetzen das Problem nicht umgehend beheben, löschen Sie bitte Ihre Cookies und Ihren Cache.

Aus Sicherheitsgründen kann Braze die 2FA nicht im Namen der Nutzer:innen zurücksetzen. Sollte der Administrator die 2FA nicht zurücksetzen können, erstellen Sie bitte ein Support-Ticket.

#### Überlegungen

- Wenn 2FA auf Unternehmensebene vorgeschrieben ist: Nach dem Zurücksetzen fordert Braze die Nutzer:innen auf, bei der nächsten Anmeldung die 2FA erneut einzurichten.
- Wenn 2FA auf Unternehmensebene nicht durchgesetzt wird: Der Nutzer:in wird sich im Dashboard anmelden, ohne die 2FA erneut einrichten zu müssen. Sollten sie die 2FA aktivieren wollen, können sie dies in den Kontoeinstellungen vornehmen.

{% alert note %}
Dieser Rücksetzungsprozess gilt auch für Nutzer:innen, die aufgrund zu vieler Token-Anfragen innerhalb der letzten Stunde aus ihrem Konto ausgesperrt wurden.
{% endalert %}