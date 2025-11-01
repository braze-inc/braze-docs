---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie Braze für die Verwendung von Okta für Single Sign-on konfigurieren." 

---

# Okta 

> Okta verbindet jede Person mit jeder Anwendung auf jedem Gerät. Es handelt sich um einen Identitätsverwaltungsdienst für Unternehmen, der für die Cloud entwickelt wurde, aber mit vielen lokalen Anwendungen kompatibel ist. Mit Okta kann Ihr IT-Team den Zugriff eines jeden Mitarbeiters auf jede Anwendung oder jedes Gerät verwalten.

## Anforderungen

| Anforderung | Details |
| ----------- | ------- |
| Okta ist für Ihr Konto aktiviert | Wenden Sie sich an Ihren Braze-Kundenbetreuer, um diese Funktion für Ihr Konto aktivieren zu lassen. |
| Okta Admin-Rechte | Vergewissern Sie sich, dass Sie über Admin-Rechte verfügen, bevor Sie Okta einrichten. |
| Braze Admin-Rechte | Vergewissern Sie sich, dass Sie über Admin-Rechte verfügen, bevor Sie Okta einrichten. |
| RelayState API-Schlüssel | Um die IdP-Anmeldung zu aktivieren, gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login` Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Schritt 1: Braze konfigurieren

### Schritt 1a: Navigieren Sie zu den Sicherheitseinstellungen in Braze

Nachdem Ihr Account Manager SAML SSO für Ihr Konto aktiviert hat, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML SSO auf **EIN**.

\![Okta SAML SSO auf der Seite Sicherheitseinstellungen aktiviert.]({% image_buster/assets/img/Okta/okta1.png %})

### Schritt 1b: SAML SSO-Einstellungen bearbeiten

Über Ihr Okta Admin-Dashboard erhalten Sie eine Ziel-URL (Anmelde-URL) und ein `x.509` -Zertifikat, die Sie auf der Seite **Sicherheitseinstellungen** Ihres Braze-Kontos eingeben müssen.

\![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Anforderung | Details |
|---|---|
| `SAML Name` | Dieser Text wird als Button-Text auf dem Anmeldebildschirm angezeigt. Dies ist in der Regel der Name Ihres Identitätsanbieters, zum Beispiel "Okta". |
| `Target URL` | Dies ist die Anmelde-URL, die vom Okta-Admin-Dashboard bereitgestellt wird. Gehen Sie dazu auf **Anwendungen** > Ihre Anwendung > Registerkarte **Allgemein** > **App Embed Link** > **Embed Link**. |
| `Certificate` | Das `x.509` PEM-codierte Zertifikat wird von Ihrem Identitätsanbieter bereitgestellt. Sie müssen sie kopieren und in dieses Feld einfügen. Rufen Sie es in Okta ab, indem Sie zu **SAML-Signaturzertifikate** gehen und **Aktionen** > **Zertifikat herunterladen** wählen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wählen Sie unten auf der Seite **Änderungen speichern**, wenn Sie fertig sind.

## Schritt 2: Okta konfigurieren

Wählen Sie in Okta die Registerkarte **Anmelden** für die Braze SAML-App und klicken Sie dann auf **Bearbeiten**. 

Als nächstes geben Sie den RelayState-API-Schlüssel mit der Berechtigung `sso.saml.login` in das Feld **Standard-Relay-Status** ein. 

\![Okta Standard RelayState auf dem Tab Anmelden.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Stellen Sie sicher, dass Sie diese neuen Einstellungen speichern.

{% alert tip %}
Wenn Sie möchten, dass sich die Benutzer Ihres Braze-Kontos nur mit SAML SSO anmelden, können Sie [die Single Sign-On-Authentifizierung]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) auf der Seite **Unternehmenseinstellungen** [einschränken]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction).
{% endalert %}

## Schritt 3: Anmelden

Sie sollten jetzt in der Lage sein, sich mit Okta bei Braze anzumelden!

Anmeldung im Braze-Dashboard mit Okta SSO Enablement.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}

