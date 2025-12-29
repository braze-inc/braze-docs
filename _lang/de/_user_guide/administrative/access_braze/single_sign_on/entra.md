---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie die Microsoft Entra Single Sign-On-Funktionen mit Braze einrichten."

---

# Microsoft Entra SSO

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) ist der Cloud-basierte Identitäts- und Zugriffsverwaltungsdienst von Microsoft, mit dem sich Ihre Mitarbeiter anmelden und auf Ressourcen zugreifen können. Mit Entra SSO können Sie den Zugriff auf Ihre Apps und App-Ressourcen auf der Grundlage Ihrer Geschäftsanforderungen kontrollieren.

## Anforderungen

Bei der Einrichtung werden Sie aufgefordert, eine URL für den Assertion Consumer Service (ACS) anzugeben.  

| Anforderung | Details |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Bei einigen Identitätsanbietern wird dies auch als Reply URL, Audience URL oder Audience URI bezeichnet. |
| Entitäts-ID | `braze_dashboard`|
| RelayState API-Schlüssel | Um die Anmeldung beim Identitätsanbieter zu aktivieren, gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login` Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Vom Service Provider (SP) initiierte Anmeldung innerhalb von Microsoft Entra SSO

### Schritt 1: Braze aus der Galerie hinzufügen

1. Gehen Sie in Ihrem Microsoft Entra Admin Center zu **Identität** > **Anwendungen** > **Unternehmensanwendungen** und wählen Sie dann **Neue Anwendung**.
2. Suchen Sie im Suchfeld nach **Braze**, wählen Sie es im Ergebnisfeld aus und wählen Sie dann **Hinzufügen**.

### Schritt 2: Microsoft Entra SSO konfigurieren

1. Gehen Sie in Ihrem Microsoft Entra Admin Center auf die Seite zur Braze-Anwendungsintegration und dort auf **Single Sign-On**.
2. Wählen Sie auf der Seite **Wählen Sie eine Methode für die einmalige Anmeldung** **SAML** als Ihre Methode.
3. Wählen Sie auf der Seite **Single Sign-On mit SAML einrichten** das Bearbeitungssymbol für die **grundlegende SAML-Konfiguration**.
4. Konfigurieren Sie die Anwendung im IdP-initiierten Modus, indem Sie eine **Antwort-URL** eingeben, die Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) mit dem folgenden Muster kombiniert: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Konfigurieren Sie optional RelayState, indem Sie Ihren von Relay State generierten API-Schlüssel in das Feld **Relay State (Optional)** eingeben.

{% alert important %}
Legen Sie das Feld **Anmelde-URL** **nicht** fest. Lassen Sie dieses Feld leer, um Probleme mit dem von Ihrem IdP initiierten SAML SSO zu vermeiden.
{% endalert %}

{: start="6"}
6\. Formatieren Sie SAML-Assertions in dem spezifischen Format, das Braze erwartet. Lesen Sie sich die folgenden Registerkarten zu Benutzerattributen und Benutzeransprüchen durch, um zu verstehen, wie diese Attribute und Werte formatiert werden müssen.

{% tabs %}
{% tab User Attributes %}
Sie können die Werte dieser Attribute im Bereich **Benutzerattribute** auf der Seite **Anwendungsintegration** verwalten.

Verwenden Sie die folgenden Attributspaarungen:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
Es ist sehr wichtig, dass das E-Mail-Feld mit dem übereinstimmt, was für Ihre Benutzer in Braze eingerichtet wurde. In den meisten Fällen ist dies dasselbe wie `user.userprincipalname`. Wenn Sie jedoch eine andere Konfiguration haben, arbeiten Sie mit Ihrem Systemadministrator zusammen, um sicherzustellen, dass diese Felder genau übereinstimmen.
{% endalert %}

{% endtab %}
{% tab User Claims %}

Auf der Seite **Single Sign-On mit SAML einrichten** wählen Sie **Bearbeiten**, um das Dialogfeld **Benutzerattribute** zu öffnen. Bearbeiten Sie dann die Benutzeransprüche entsprechend dem richtigen Format.

Verwenden Sie die folgenden Anspruchspaare:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
Es ist sehr wichtig, dass das E-Mail-Feld mit dem übereinstimmt, was für Ihre Benutzer in Braze eingerichtet wurde. In den meisten Fällen ist dies dasselbe wie `user.userprincipalname`. Wenn Sie jedoch eine andere Konfiguration haben, arbeiten Sie mit Ihrem Systemadministrator zusammen, um sicherzustellen, dass diese Felder genau übereinstimmen.
{% endalert %}

Sie können diese Benutzeransprüche und Werte im Bereich **Anspruch** verwalten verwalten.

{% endtab %}
{% endtabs %}

{: start="8"}
8\. Gehen Sie auf die Seite **Single Sign-On mit SAML einrichten**, scrollen Sie dann zum Abschnitt **SAML Signing Certificate** und laden Sie das entsprechende **Zertifikat (Base64)** entsprechend Ihren Anforderungen herunter.
9\. Gehen Sie zum Abschnitt **Braze einrichten** und kopieren Sie die entsprechenden URLs zur Verwendung in der [Braze-Konfiguration](#step-3).

### Schritt 3: Konfigurieren Sie Microsoft Entra SSO in Braze {#step-3}

Wenn Sie Braze im Microsoft Entra Admin Center eingerichtet haben, erstellt Microsoft Entra eine Ziel-URL (Anmelde-URL) und ein **x.509** Zertifikat, die Sie in Ihrem Braze-Konto eingeben müssen.

Wenn Ihr Account Manager SAML SSO für Ihr Konto aktiviert hat, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML SSO auf **EIN**.
2. Fügen Sie auf derselben Seite Folgendes hinzu:

| Anforderung | Details |
|---|---|
| `SAML Name` | Dieser Text wird auf der Schaltfläche auf dem Anmeldebildschirm angezeigt. Dies ist in der Regel der Name Ihres Identitätsanbieters, z. B. "Microsoft Entra". |
| `Target URL` | Dies ist die von Microsoft Entra bereitgestellte Anmelde-URL.|
| `Certificate` | Das `x.509` PEM-codierte Zertifikat wird von Ihrem Identitätsanbieter bereitgestellt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Wenn Sie möchten, dass sich die Benutzer Ihres Braze-Kontos nur mit SAML SSO anmelden, können Sie [die Single Sign-On-Authentifizierung]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) auf der Seite **Unternehmenseinstellungen** [einschränken]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction).
{% endalert %}
