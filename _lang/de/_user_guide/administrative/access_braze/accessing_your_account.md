---
nav_title: Zugriff auf Ihr Konto
article_title: Zugriff auf Ihr Konto
page_order: 0
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie Ihr Braze-Konto erhalten, wie Sie sich nach der Freischaltung anmelden und wie Sie Ihr Braze-Passwort zurücksetzen können."

---

# Zugriff auf Ihr Konto

> In diesem Artikel erfahren Sie, wie Sie Ihr Braze-Konto erhalten, wie Sie sich anmelden, nachdem Sie Zugang erhalten haben, und wie Sie bei Problemen mit dem Dashboard-Zugang und der Dashboard-Performance vorgehen können.

Wenn Sie die erste Braze-Nutzer:in in Ihrem Unternehmen sind und sich zum ersten Mal anmelden, erhalten Sie eine Willkommens-E-Mail von `@alerts.braze.com`, in der Sie aufgefordert werden, Ihre E-Mail-Adresse zu bestätigen und sich am ersten Tag Ihres Vertrags anzumelden.

Nachdem Sie Ihr Konto bestätigt haben, können Sie auf der Seite [Nutzer:innen des Unternehmens]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) in Ihrem Dashboard weitere Nutzer:innen hinzufügen. Alle Nutzer:innen erhalten eine E-Mail, in der sie aufgefordert werden, ihr Konto zu bestätigen, nachdem sie hinzugefügt worden sind.

Wenn Sie nicht die erste Nutzer:in auf dem Braze-Konto Ihres Unternehmens sind, wenden Sie sich an die Braze-Kontoverwaltung Ihres Unternehmens und bitten Sie darum, Ihr Konto zu erstellen. Sie erhalten dann eine Willkommens-E-Mail von `@alerts.braze.com`, in der Sie aufgefordert werden, Ihre E-Mail-Adresse zu bestätigen und sich anzumelden.

## Anmelden

Lassen Sie uns darüber sprechen, wie Sie sich anmelden – egal ob es das erste oder das millionste Mal ist! Wenn Sie die erste Nutzer:in in Ihrem Unternehmen sind, befolgen Sie die Hinweise im vorangehenden Abschnitt. Falls nicht, können Sie sich anmelden, nachdem die Braze-Administration Ihres Unternehmens Ihr Konto erstellt hat.

Sie können sich entweder über die [Braze.com](https://www.braze.com)-Startseite anmelden oder einfach die Dashboard-URL verwenden, die Ihrer spezifischen [Braze-Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) entspricht. Braze bietet Ihnen verschiedene Single Sign-on (SSO)-Optionen, wie zum Beispiel:

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [SAML Just-in-Time-Bereitstellung]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
Nachdem Sie sich bei Braze mit SSO angemeldet haben, können Sie sich nicht mehr mit Ihrem Passwort beim Dashboard anmelden.
{% endalert %}

## Unterstützte Browser

Das Braze-Dashboard unterstützt die folgenden Browser:
- Chrome (Version 87 oder neuer)
- Firefox (Version 85 oder neuer)
- Safari (Version 15.4 oder neuer)
- Edge (Version 87 oder neuer)

Wenn Ihr Braze-Dashboard einen unerwarteten Fehler meldet und Ihr Browser-Konsolentool den Fehler `ReferenceError: structuredClone is not defined` anzeigt, ist Ihr Browser veraltet. Wenn dieser Fehler immer wieder auftritt, deinstallieren Sie Ihren Browser und installieren Sie ihn neu.

## Zugriff auf mehrere Braze-Dashboards

Braze erlaubt es nicht, dieselbe E-Mail-Adresse für mehrere Dashboard-Nutzer:innen im selben Cluster zu registrieren (zum Beispiel, wenn Sie zwei Dashboards auf US-01 haben). Sie können dieselbe E-Mail-Adresse verwenden, um Konten auf verschiedenen Clustern zu erstellen (beispielsweise, wenn Sie ein Dashboard auf US-01 und eines auf US-05 haben). Wenn Sie auf mehrere Braze-Dashboards im selben Cluster zugreifen müssen, können Sie wie folgt vorgehen:

### E-Mail-Aliase verwenden

Wenn Sie Gmail als E-Mail-Anbieter verwenden, können Sie Aliase erstellen, indem Sie ein `+`-Zeichen gefolgt von einem beliebigen Text an Ihre E-Mail-Adresse anhängen. Zum Beispiel:
- **Original-E-Mail:** `rocky@gmail.com`
- **Alias-E-Mail:** `rocky+1@gmail.com`

Beide E-Mail-Adressen leiten E-Mails an denselben Posteingang weiter, jedoch erkennt Braze sie bei der Anmeldung als separate Konten.

### Separate Aliase bei anderen Anbietern erstellen

Sollte Ihr E-Mail-Anbieter keine `+`-Aliase unterstützen, können Sie dennoch separate Aliase erstellen, beispielsweise indem Sie eine Weiterleitung von `rocky@braze.com` zu `rocky.lotito@braze.com` einrichten. Dadurch können mehrere Adressen in denselben Posteingang weitergeleitet werden, während sie von Braze als unterschiedliche E-Mail-Adressen erkannt werden.

### Entwickler:innen für mehrere Unternehmen einsetzen

Das Feature für Entwickler:innen aus mehreren Unternehmen ermöglicht die gemeinsame Nutzung eines einzigen Nutzerkontos durch mehrere Unternehmen. Nutzer:innen können über das Menü ihres Nutzerprofils zwischen verschiedenen Unternehmens-Dashboards umschalten.

Wenn Sie SSO verwenden und Entwickler:innen für mehrere Unternehmen einrichten möchten, müssen Sie eine angepasste SAML-Entitäts-ID aktivieren, indem Sie eine angepasste SAML-SSO-Integration einrichten. Befolgen Sie die Schritte für [die vom Dienstanbieter (SP) initiierte Anmeldung]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), jedoch mit folgenden Änderungen:
- Ändern Sie die **Entitäts-ID** für jede Dashboard-Integration in `braze_dashboard_<companyID>`.
- Wenden Sie sich an Ihren Customer-Success-Manager oder Account Manager, um den `saml_sso_custom_entity_id`-Feature-Flipper für jedes Dashboard zu aktivieren.

### Überlegungen zum Single Sign-on (SSO)

Bitte beachten Sie, dass bei Verwendung von Single Sign-on (SSO) die Nutzung mehrerer unterschiedlicher E-Mail-Adressen zu Komplikationen führen kann. Überprüfen Sie, ob Ihre SSO-Einstellungen korrekt konfiguriert sind, um Zugriffsprobleme zu vermeiden.

## Fehlerbehebung

### Passwort zurücksetzen

Um Ihr Passwort zurückzusetzen, wählen Sie den Link **Passwort vergessen?** auf der Dashboard-Anmeldeseite. Sie werden aufgefordert, Ihre E-Mail-Adresse einzugeben, um einen Link zum Zurücksetzen Ihres Passworts zu erhalten.

![Anmeldung beim Dashboard mit der Aufforderung „Passwort vergessen?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Browser-Cache und Cookies löschen

Wenn Sie Probleme mit der Performance des Dashboards haben, z. B. wenn Ihre Dashboard- oder Segment-Performance-Liste nicht geladen wird, versuchen Sie, Ihren Browser-Cache und Ihre Cookies zu löschen, indem Sie die Schritte für Ihren jeweiligen Browser befolgen.

{% alert important %}
Wenn Sie Cookies löschen, werden Sie abgemeldet, sodass ungespeicherte Arbeit verloren geht.
{% endalert %}

- [Cache und Cookies in Chrome löschen](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Cookies in Safari auf dem Mac löschen](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Cookies und Website-Daten in Firefox löschen](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Alle Cookies in Microsoft Edge löschen](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Wenn das Löschen Ihres Browser-Caches und Ihrer Cookies das Problem nicht löst, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact/).

### „Bitte Seite aktualisieren" oder „Unerwarteter Fehler" beim Navigieren im Dashboard

Dieser Fehler kann auftreten, wenn eine Unternehmensnutzer:in keinem Workspace zugeordnet ist. Zur Fehlerbehebung:

1. Gehen Sie zur Seite [Nutzer:innen des Unternehmens]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/).
2. Überprüfen Sie, ob die Nutzer:in einem Workspace hinzugefügt wurde.
3. Falls sie keinem Workspace zugeordnet ist, fügen Sie sie hinzu und weisen Sie die entsprechenden Berechtigungen zu.
4. Bitten Sie die Nutzer:in, ihr Dashboard zu aktualisieren.
5. Wenn das Problem weiterhin besteht, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact/).

### Zugriff auf den Drag-and-Drop-Editor

Für die meisten Unternehmensnutzer:innen sollte der Drag-and-Drop-Editor geladen werden. Wenn Sie jedoch ein VPN verwenden oder sich hinter einer Firewall befinden, müssen Sie möglicherweise eine Domain auf die Zulassungsliste setzen. Wenden Sie sich an Ihre IT-Administration, um zu überprüfen, ob `*.bz-rndr.com` auf der Zulassungsliste steht.

Beim Laden des Editors kann es aus folgenden Gründen zu Problemen kommen:

- **Vorübergehender Fehler:** Dabei handelt es sich um temporäre Ausfälle, die die Konnektivität, die Kommunikation oder die Datenübertragung beeinträchtigen können. Glücklicherweise lösen sie sich in der Regel von selbst, ohne dass ein nennenswerter Eingriff erforderlich ist, da sie oft durch kurzlebige Bedingungen verursacht werden und nicht auf systemische Probleme hinweisen.
- **Schwerer Fehler:** Dies kann ein Problem mit der zugrunde liegenden Infrastruktur oder dem Produkt sein. Sie können auf unserer [Braze-Systemstatusseite](https://braze.statuspage.io/) nachsehen, da uns das Problem wahrscheinlich bekannt ist und wir aktiv an einer Lösung arbeiten.

{% alert important %}
Wenn Sie immer noch Probleme haben, [öffnen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Vergewissern Sie sich zuvor, dass Ihre IT-Administration bestätigt hat, dass `*.bz-rndr.com` auf Ihrer Seite zugelassen ist.
{% endalert %}

### Zugriff auf Braze Learning

Sollten Sie Probleme beim Einloggen in Braze Learning haben und sich in einer Schleife befinden, die Sie immer wieder zum Dashboard weiterleitet, führen Sie bitte die folgenden Schritte aus:

1. Sollten Sie mehrere Braze-Konten besitzen, werden Sie nach zweimaliger Anmeldung mit dem falschen Konto zum Braze-Dashboard weitergeleitet. Stellen Sie sicher, dass Sie sich beim richtigen Konto anmelden.
2. Falls Sie einen Werbeblocker verwenden, überprüfen Sie, ob dieser deaktiviert ist. Er kann Cookies blockieren, die für die Single Sign-on-Funktionalität erforderlich sind.
3. Gehen Sie zu Unternehmenseinstellungen > Sicherheitseinstellungen und überprüfen Sie, ob Single Sign-on (SSO) aktiviert ist.
4. Stellen Sie sicher, dass Ihr Dashboard-Nutzerprofil sowohl einen Vornamen als auch einen Nachnamen enthält. Das Fehlen eines Nachnamens kann den Anmeldevorgang beeinträchtigen.
5. Greifen Sie über Ihr Dashboard auf Braze Learning zu, indem Sie zu **Support** > **Braze Learning** navigieren.
6. Sollten weiterhin Probleme auftreten, empfehlen wir Ihnen, Ihr Konto neu zu erstellen. Nutzer:innen, die während der kostenlosen Demo auf Braze Learning zugegriffen haben, könnten derzeit Schwierigkeiten beim Zugriff haben.

### Probleme mit der Zwei-Faktor-Authentifizierung (2FA)

Sollte eine Nutzer:in Probleme mit der Zwei-Faktor-Authentifizierung (2FA) haben und keinen Zugriff auf das Braze-Dashboard erhalten, kann dies verschiedene Ursachen haben. In den meisten Fällen hat die betroffene Person möglicherweise keinen Zugriff mehr auf die registrierte Telefonnummer oder das Gerät, auf dem die Authy-App installiert ist.

Eine Administration sollte die 2FA für die betroffene Nutzer:in wie folgt zurücksetzen:

1. Gehen Sie zu **Nutzer:innen verwalten**.
2. Wählen Sie **Nutzer:in bearbeiten** für die Person, bei der Probleme mit der 2FA auftreten.
3. Wählen Sie die Option zum Zurücksetzen der 2FA.
4. Bestätigen Sie die 2FA-Zurücksetzung, wenn Sie dazu aufgefordert werden.
5. Sollte das Zurücksetzen das Problem nicht umgehend beheben, löschen Sie Ihre Cookies und Ihren Cache.

Aus Sicherheitsgründen kann Braze die 2FA nicht im Namen der Nutzer:innen zurücksetzen. Sollte die Administration die 2FA nicht zurücksetzen können, erstellen Sie bitte ein Support-Ticket.

#### Überlegungen

- Wenn 2FA auf Unternehmensebene vorgeschrieben ist: Nach dem Zurücksetzen fordert Braze die Nutzer:in auf, bei der nächsten Anmeldung die 2FA erneut einzurichten.
- Wenn 2FA auf Unternehmensebene nicht vorgeschrieben ist: Die Nutzer:in meldet sich im Dashboard an, ohne die 2FA erneut einrichten zu müssen. Wenn sie die 2FA aktivieren möchte, kann sie dies in den Kontoeinstellungen tun.

{% alert note %}
Dieser Zurücksetzungsprozess gilt auch für Nutzer:innen, die aufgrund zu vieler Token-Anfragen innerhalb der letzten Stunde aus ihrem Konto ausgesperrt wurden.
{% endalert %}