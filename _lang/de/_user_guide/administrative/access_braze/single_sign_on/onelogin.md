---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie Braze für die Verwendung von Single Sign-on mit OneLogin konfigurieren."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) ist eine Cloud-Identitätsplattform für die umfassende Verwaltung von Benutzeridentitäten. OneLogin lässt sich per von SAML 2.0 in Cloud- und On-Premise-Anwendungen integrieren – für Single Sign-On (SSO), Benutzerbereitstellung, mehrstufige Authentifizierung und vieles mehr.

## Anforderungen

Bei der Einrichtung werden Sie aufgefordert, eine Anmelde-URL und eine ACS-URL (Assertion Consumer Service) anzugeben.  

| Anforderung | Details |
|---|---|
| Braze-Domain | Sie benötigen Ihre Braze-Domäne, um Braze in OneLogin einzurichten. Wenn Ihre Instanz `US-01` ist, müssen Sie Ihre Dashboard-URL in das Dashboard von OneLogin eingeben. <br><br> Wenn Ihre Dashboard-URL z. B. `https://dashboard-01.braze.com` lautet, geben Sie `dashboard-01.braze.com` ein.  |
| RelayState API-Schlüssel | Um die IdP-Anmeldung zu aktivieren, gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login` Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## IdP-initiierte Anmeldung bei OneLogin

### Schritt 1: Konfigurieren Sie die Braze App

1. Melden Sie sich bei [OneLogin](https://app.onelogin.com/login) an. Klicken Sie auf **Administration**.\![OneLogin Administrationsseite.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Gehen Sie zu **Apps** > **Apps hinzufügen** in der oberen Navigationsleiste. Suchen Sie nach "Braze" und wählen Sie die Braze App aus\![Suchergebnisse für Braze in OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Speichern Sie die Braze App in Ihrem Unternehmen.[.]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Gehen Sie nach dem Speichern zu **Konfiguration** und fügen Sie Ihre **Braze Domain** und Ihren **RelayState** API-Schlüssel hinzu.\![Tab OneLogin Konfiguration für die Braze App.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze erwartet die SAML-Assertions in einem [bestimmten Format]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider). Unter **Parameter** sollten die von Braze unterstützten Attribute vorausgefüllt sein. Überprüfen Sie, ob sie korrekt sind\![Braze SAML-Parameter in OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Kopieren Sie das **Zertifikat** und den **SAML 2.0 Endpunkt (HTTP)**, die für die Einrichtung des Braze-Dashboards benötigt werden, aus dem **SSO** Tab.\![Zertifikate, die Sie aus dem Braze App SSO Tab in OneLogin kopieren müssen.]({% image_buster /assets/img/onelogin_6.jpg %})

### Schritt 2: Konfigurieren Sie OneLogin in Braze

Sobald Sie Braze in Ihrem OneLogin eingerichtet haben, erhalten Sie eine Ziel-URL (`SAML 2.0 Endpoint (HTTP)`) und ein `x.509` Zertifikat, das Sie in Ihr Braze-Konto eingeben.

Nachdem Ihr Kontomanager SAML SSO für Ihr Konto aktiviert hat, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML SSO auf **EIN**

Geben Sie auf dieser Seite Folgendes ein:

| Anforderung | Details |
|---|---|
| `SAML Name` | Dieser Text wird auf der Schaltfläche auf dem Anmeldebildschirm angezeigt. Dies ist normalerweise der Name Ihres Identitätsanbieters, z.B. "OneLogin". |
| `Target URL` | Dies ist die von OneLogin bereitgestellte `SAML 2.0 Endpoint (HTTP)` URL.|
| `Certificate` | Das `x.509`-PEM-kodierte Zertifikat wird von OneLogin bereitgestellt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![SAML SSO Einstellungen mit dem ausgewählten Umschalter.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Wenn Sie möchten, dass sich die Benutzer Ihres Braze-Kontos nur mit SAML SSO anmelden, können Sie [die Single Sign-On-Authentifizierung]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) auf der Seite **Unternehmenseinstellungen** [einschränken]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction).
{% endalert %}

