---
nav_title: Zugriff auf Ihr Konto
article_title: Zugriff auf Ihr Konto
page_order: 2
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie Ihr Braze-Konto erhalten, wie Sie sich nach der Freischaltung anmelden und wie Sie Ihr Braze-Passwort zurücksetzen können."

---

# Zugriff auf Ihr Konto

> In diesem Artikel erfahren Sie, wie Sie Ihr Braze-Konto erhalten, wie Sie sich anmelden, nachdem Sie Zugang erhalten haben, und wie Sie Fehlerbehebungen für Ihren Dashboard-Zugang und die Performance des Dashboards vornehmen können.

Wenn Sie der erste Braze-Benutzer in Ihrem Unternehmen sind und sich zum ersten Mal anmelden, erhalten Sie eine Willkommens-E-Mail von `@alerts.braze.com`, in der Sie aufgefordert werden, Ihre E-Mail zu bestätigen und sich am ersten Tag Ihres Vertrags anzumelden.

Nachdem Sie Ihr Konto bestätigt haben, können Sie auf der Seite [Nutzer:innen des Unternehmens]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) auf Ihrem Dashboard weitere Nutzer:innen hinzufügen. Alle Nutzer:innen erhalten eine E-Mail, in der sie aufgefordert werden, ihr Konto zu bestätigen, nachdem sie hinzugefügt worden sind.

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

In Braze ist es nicht zulässig, dieselbe E-Mail für mehrere Nutzer:innen des Dashboards im selben Cluster zu registrieren (z.B. wenn Sie zwei Dashboards auf US-01 haben). Sie können dieselbe E-Mail verwenden, um Konten auf verschiedenen Clustern einzurichten (z.B. wenn Sie ein Dashboard auf US-01 und eines auf US-05 haben). Wenn Sie auf mehrere Braze-Dashboards im selben Cluster zugreifen müssen, können Sie wie folgt vorgehen:

### E-Mail-Aliase verwenden

Wenn Ihr E-Mail-Anbieter Gmail ist, können Sie Aliase erstellen, indem Sie ein `+` -Zeichen gefolgt von einem beliebigen Text an Ihre E-Mail-Adresse anhängen. Zum Beispiel:
- **Ursprüngliche E-Mail:** `rocky@gmail.com`
- **Alias E-Mail:** `rocky+1@gmail.com`

Beide E-Mail-Adressen leiten E-Mails an denselben Posteingang weiter, aber Braze erkennt sie als separate Konten, wenn Sie sich anmelden.

### Erstellen Sie separate Aliase bei anderen Anbietern

Wenn Ihr E-Mail-Anbieter `+` nicht unterstützt, können Sie immer noch separate Aliase erstellen, z. B. `rocky@braze.com` als Weiterleitung an `rocky.lotito@braze.com` einrichten. So ist es zulässig, dass mehrere Adressen in denselben Posteingang geleitet werden, während sie von Braze als unterschiedliche E-Mails erkannt werden.

### Verwenden Sie Entwickler:in mehreren Unternehmen

Das Feature für Entwickler:innen mehrerer Unternehmen erlaubt die gemeinsame Nutzung eines einzigen Nutzer:in-Kontos durch mehrere Unternehmen. Nutzer:innen können über das Menü ihres Nutzerprofils zwischen den verschiedenen Dashboards des Unternehmens umschalten.

Wenn Sie SSO haben und Entwickler:in für mehrere Unternehmen einrichten möchten, müssen Sie eine SAML Custom Entity ID aktivieren, indem Sie eine angepasste SAML SSO Integration einrichten. Befolgen Sie die Schritte unter [Anmeldung durch den Service Provider (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), übernehmen Sie jedoch diese Änderungen:
- Ändern Sie für jede Dashboard Integration die **Entity ID** in `braze_dashboard_<companyID>`.
- Wenden Sie sich an Ihren Customer-Success-Manager oder Account Manager:in, um das `saml_sso_custom_entity_id` Feature flipper für jedes Dashboard anzupassen.

### Überlegungen für Single Sign-on (SSO)

Wenn Sie Single Sign-on (SSO) verwenden, sollten Sie sich darüber im Klaren sein, dass die Verwendung mehrerer verschiedener E-Mail-Adressen zu Komplikationen führen kann. Vergewissern Sie sich, dass Ihre SSO-Einstellungen korrekt konfiguriert sind, um Zugriffsprobleme zu vermeiden.

## Fehlersuche

### Ihr Passwort zurücksetzen

Um Ihr Passwort zurückzusetzen, wählen Sie den Link **Passwort vergessen?** auf der Dashboard-Anmeldeseite. Sie werden aufgefordert, Ihre E-Mail einzugeben, um einen Link zum Zurücksetzen Ihres Passworts zu erhalten.

![Dashboard Anmeldung mit der Aufforderung "Haben Sie Ihr Passwort vergessen?".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Löschen des Cache und der Cookies Ihres Browsers

Wenn Sie Probleme mit der Performance des Dashboards haben, z.B. wenn Ihre Performance-Liste des Dashboards oder der Segmente nicht geladen wird, versuchen Sie, Ihren Browser-Cache und Ihre Cookies zu löschen, indem Sie die Schritte für Ihren jeweiligen Browser befolgen.

{% alert important %}
Wenn Sie Cookies löschen, werden Sie abgemeldet, so dass ungespeicherte Arbeit verloren geht.
{% endalert %}

- [Cache löschen & Cookies in Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Cookies in Safari auf dem Mac löschen](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Cookies und Daten der Website in Firefox löschen](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Alle Cookies in Microsoft Edge löschen](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Wenn das Löschen Ihres Browser-Caches und Ihrer Cookies Ihre Probleme nicht löst, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact/).

### Zugriff auf den Drag-and-Drop-Editor

Bei den meisten Nutzer:innen von Braze sollte der Drag-and-Drop-Editor geladen werden. Wenn Sie jedoch ein VPN verwenden oder sich hinter einer Firewall befinden, müssen Sie möglicherweise eine Domain in der Liste zulassen. Wenden Sie sich an Ihren IT-Administrator, um zu überprüfen, ob `*.bz-rndr.com` in der Liste der zulässigen Anwendungen aufgeführt ist.

Beim Laden des Editors kann es aus folgenden Gründen zu Problemen kommen:

- **Vorübergehender Fehler:** Dabei handelt es sich um vorübergehende Ausfälle, die die Konnektivität, die Kommunikation oder die Übertragung von Daten beeinträchtigen können. Glücklicherweise lösen sie sich in der Regel von selbst auf, ohne dass ein nennenswerter Eingriff erforderlich ist, da sie oft durch kurzlebige Bedingungen verursacht werden und nicht auf systemische Probleme hinweisen.
- **Schwerer Fehler:** Dies kann ein Problem mit der Infrastruktur oder dem Produkt sein.  Sie können auf unserer [Braze-Systemstatusseite](https://braze.statuspage.io/) nachsehen, da uns das Problem wahrscheinlich bekannt ist und wir aktiv an einer Lösung arbeiten.

{% alert important %}
Wenn Sie immer noch Probleme haben, [öffnen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Vergewissern Sie sich zuvor, dass Ihr IT-Administrator bestätigt hat, dass `*.bz-rndr.com` auf Ihrer Seite zugelassen ist.
{% endalert %}

### Zugriff auf Braze Lernangebote

Wenn Sie Probleme bei der Anmeldung bei Braze Lernangebote haben und in einer Schleife stecken bleiben, die Sie zum Dashboard weiterleitet, führen Sie die folgenden Schritte aus:

1. Wenn Sie mehrere Braze-Konten haben, werden Sie beim zweimaligen Einloggen mit dem falschen Konto auf das Braze-Dashboard weitergeleitet. Vergewissern Sie sich, dass Sie sich bei dem richtigen Konto anmelden. 
2. Wenn Sie einen Werbeblocker verwenden, vergewissern Sie sich, dass er ausgeschaltet ist. Es kann Cookies blockieren, die für die Single Sign-on-Funktionalität erforderlich sind.
3. Gehen Sie zu Unternehmenseinstellungen > Sicherheitseinstellungen und überprüfen Sie, ob Single Sign-on (SSO) aktiviert ist.
4. Stellen Sie sicher, dass Ihr Nutzerprofil auf dem Dashboard sowohl einen Vor- als auch einen Nachnamen enthält. Das Fehlen eines Nachnamens kann zu Störungen bei der Anmeldung führen.
5. Greifen Sie über Ihr Dashboard auf Braze Lernangebote zu, indem Sie zu **Support** > Braze Lernangebote gehen. 
6. Wenn Sie weiterhin Probleme haben, sollten Sie Ihr Konto neu erstellen. Nutzer:innen, die während der kostenlosen Testphase auf Braze Lernangebote zugegriffen haben, haben jetzt möglicherweise Schwierigkeiten beim Zugriff.

### Probleme mit der Zwei-Faktor-Authentifizierung (2FA)

Wenn ein Nutzer:innen Probleme mit der Zwei-Faktor-Authentifizierung (2FA) hat und nicht auf das Braze-Dashboard zugreifen kann, kann dies mehrere Gründe haben. In den meisten Fällen haben sie keinen Zugriff mehr auf die registrierte Telefonnummer oder das Gerät, auf dem die Authy App installiert ist.

Ein Administrator sollte die 2FA für die betroffenen Nutzer:innen wie folgt zurücksetzen: 

1. Gehen Sie zu **Nutzer:innen verwalten**.
2. Wählen Sie **Benutzer bearbeiten** für den Nutzer:in, bei dem 2FA-Probleme auftreten.
3. Wählen Sie die Option zum Zurücksetzen von 2FA.
4. Bestätigen Sie das Zurücksetzen der 2FA, wenn Sie dazu aufgefordert werden.
5. Wenn das Zurücksetzen das Problem nicht sofort behebt, löschen Sie Ihre Cookies und Ihren Cache.

Aus Sicherheitsgründen kann Braze 2FA nicht im Namen von Nutzer:innen zurücksetzen. Wenn der Administrator also nicht in der Lage ist, 2FA zurückzusetzen, sollte ein Support-Ticket erstellt werden.

#### Überlegungen

- Wenn 2FA auf Unternehmensebene durchgesetzt wird: Nach dem Zurücksetzen wird der Nutzer:in aufgefordert, seine 2FA bei der nächsten Anmeldung erneut einzurichten.
- Wenn 2FA auf Unternehmensebene nicht durchgesetzt wird: Der Nutzer:in meldet sich beim Dashboard an, ohne dass er erneut 2FA einrichten muss. Wenn sie 2FA aktivieren möchten, können sie dies in den Kontoeinstellungen tun.

{% alert note %}
Dieser Rücksetzungsprozess gilt auch für Nutzer:innen, die aufgrund einer Anfrage nach zu vielen Token innerhalb der letzten Stunde aus ihrem Konto ausgesperrt wurden.
{% endalert %}