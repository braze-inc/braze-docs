---
nav_title: SAML SSO Einrichtung
article_title: SAML SSO-Einrichtung
page_order: 0
page_type: tutorial
description: "Dieser Artikel zeigt Ihnen, wie Sie SAML Single Sign-On für Ihr Braze-Konto aktivieren."

---

# Anmeldung per Dienstanbieter (SP)

> In diesem Artikel erfahren Sie, wie Sie SAML Single Sign-on in Ihrem Braze-Konto aktivieren und die SAML-Ablaufverfolgung abrufen.

## Anforderungen

Bei der Einrichtung werden Sie aufgefordert, eine Anmelde-URL und eine ACS-URL (Assertion Consumer Service) anzugeben.  

| Anforderung | Details |
|---|---|
| Assertion Consumer Service (ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Für Domains in der Europäischen Union lautet die ASC-URL `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Bei einigen Identitätsanbietern wird dies auch als Reply-URL, Sign-On URL, Audience-URL oder Audience-URI bezeichnet. |
| Entitäts-ID | `braze_dashboard` |
| RelayState API-Schlüssel | Gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login` Berechtigungen und geben Sie dann den generierten API-Schlüssel als `RelayState` Parameter in Ihren IdP ein. Detaillierte Schritte finden Sie unter [Einrichten Ihres RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SAML SSO einrichten

### Schritt 1: Identitätsanbieter konfigurieren

Richten Sie Braze bei Ihrem Identitätsanbieter (IdP) mit den folgenden Angaben als Dienstanbieter (SP) ein. Richten Sie außerdem eine SAML-Attribut-Zuordnung ein.

{% alert important %}
Wenn Sie Okta als Identitätsanbieter verwenden möchten, nutzen Sie bitte die vorkonfigurierte Integration von der [Okta-Website](https://www.okta.com/integrations/braze/).
{% endalert %}

| SAML-Attribut | Erforderlich? | Akzeptierte SAML-Attribute |
|---|---|---|
|`email` | Erforderlich | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Optional | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Optional | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze benötigt nur `email` in der SAML-Assertion.
{% endalert %}

### Schritt 2: Braze konfigurieren

Wenn Sie die Einrichtung von Braze in Ihrem Identitätsanbieter abgeschlossen haben, erhalten Sie von Ihrem Identitätsanbieter eine Ziel-URL und ein `x.509` Zertifikat, die Sie in Ihr Braze-Konto eingeben können.

Nachdem Ihr Account Manager SAML SSO für Ihr Konto aktiviert hat, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie den Abschnitt SAML SSO auf **EIN**.

Geben Sie auf derselben Seite Folgendes ein:

| Anforderung | Details |
|---|---|
| SAML-Name | Dieser Text wird als Button-Text auf dem Anmeldebildschirm angezeigt.<br>Meist der Name Ihres Identitätsanbieters, also z. B. "Okta". |
| Ziel-URL | Wird nach der Einrichtung von Braze bei Ihrem IdP angegeben.<br> Einige IdP bezeichnen sie auch als SSO-URL oder SAML-2.0-Endpunkt. |
| Zertifikat | Das `x.509` Zertifikat, das von Ihrem Identitätsanbieter bereitgestellt wird.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Achten Sie darauf, dass Ihr `x.509`-Zertifikat diesem Format entspricht, wenn Sie es in das Dashboard aufnehmen:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![SAML SSO Einstellungen mit dem ausgewählten Umschalter.]({% image_buster /assets/img/samlsso.png %})

### Schritt 3: Bei Braze anmelden

Speichern Sie Ihre Sicherheitseinstellungen und melden Sie sich ab. Melden Sie sich dann wieder bei Ihrem Identitätsanbieter an.

![Dashboard Anmeldebildschirm mit SSO Enablement]({% image_buster /assets/img/sso1.png %}){: style="max-width:60%;"}

## Einrichten Ihres RelayState

1. Gehen Sie in Braze zu **Einstellungen** > **APIs und Bezeichner**.
2. Wählen Sie auf dem Tab **API-Schlüssel** den Button **API-Schlüssel erstellen** aus.
3. Geben Sie in das Feld **Name des API-Schlüssels** einen Namen für Ihren Schlüssel ein.
4. Erweitern Sie das Dropdown-Menü **SSO** unter **Berechtigungen** und markieren Sie **sso.saml.login**.<br><br>![Der Abschnitt "Berechtigungen" mit sso.saml.login markiert.]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. Wählen Sie **API-Schlüssel erstellen**.
6. Kopieren Sie auf dem Tab **API-Schlüssel** den Bezeichner neben dem API-Schlüssel, den Sie erstellt haben.
7. Fügen Sie den RelayState API-Schlüssel in den RelayState Ihres IdP ein (je nach IdP kann er auch als "Relay State" oder "Default Relay State" erscheinen).

## SSO-Verhalten

Personen, die SSO nutzen, können nicht mehr wie bisher ihr Passwort verwenden. Wer sein Passwort weiter verwenden will, kann dies tun, sofern die folgenden Einschränkungen es nicht verhindern.

## Einschränkung

Sie können die Angehörigen Ihrer Organisation auf eine Anmeldung per Google SSO oder SAML SSO beschränken. Um die Einschränkungen zu aktivieren, öffnen Sie die **Sicherheitseinstellungen** und wählen Sie entweder **Anmeldung nur per Google SSO** oder **Anmeldung nur mit angepasstem SAML SSO**.

![Beispiel für die Einrichtung des Bereichs "Authentifizierungsregeln" mit einer Mindestlänge des Passworts von 8 Zeichen und einer 3-fachen Wiederverwendbarkeit des Passworts. Die Passwörter laufen nach 180 Tagen ab, und die Nutzer:innen werden nach 1.440 Minuten Inaktivität abgemeldet.]({% image_buster /assets/img/sso3.png %})

Wenn Sie die Einschränkungen aktivieren, können sich die Braze-Benutzer Ihres Unternehmens nicht mehr mit einem Passwort anmelden, selbst wenn sie sich zuvor mit einem Passwort angemeldet haben.

## SAML-Ablaufverfolgung abrufen

Wenn Sie Probleme bei der Anmeldung im Zusammenhang mit SSO haben, kann Ihnen die SAML-Ablaufverfolgung bei der Fehlerbehebung helfen, da Sie so herausfinden, was in den SAML-Anfragen enthalten ist.

### Voraussetzungen

Um eine SAML-Ablaufverfolgung abzurufen, benötigen Sie einen SAML-Tracer. Hier sind zwei mögliche Optionen je nach Ihrem Browser:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Schritt 1: Öffnen Sie den SAML-Tracer

Wählen Sie den SAML-Tracer in der Navigationsleiste Ihres Browsers aus. Vergewissern Sie sich, dass **Pause** nicht ausgewählt ist, da der SAML-Tracer ansonsten nicht erfassen kann, was in den SAML-Anfragen gesendet wird. Wenn der SAML-Tracer geöffnet ist, sehen Sie, wie die Ablaufverfolgung ausgefüllt wird.

![SAML-Tracer für Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Schritt 2: SSO-Anmeldung bei Braze

Öffnen Sie das Braze-Dashboard und versuchen Sie, sich per SSO anzumelden. Wenn ein Fehler auftritt, öffnen Sie den SAML-Tracer und versuchen Sie es erneut. Ein SAML-Trace wurde erfolgreich erfasst, wenn es eine Zeile mit einer URL wie `https://dashboard-XX.braze.com/auth/saml/callback` und einem orangefarbenen SAML-Tag gibt.

### Schritt 3: Exportieren und an Braze senden

Wählen Sie **Exportieren**. Für **Cookie-Filter-Profil auswählen** wählen Sie **Keine**. Wählen Sie dann **Exportieren**. Nun wird eine JSON-Datei generiert, die Sie zur weiteren Fehlerbehebung an den Braze-Support senden können.

!["SAML-Trace-Einstellungen exportieren" mit der ausgewählten Option "Keine".]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Fehlersuche

### Ist die E-Mail Adresse des Nutzers:innen korrekt eingerichtet?

Wenn Sie die Fehlermeldung `ERROR_CODE_SSO_INVALID_EMAIL` erhalten, ist die E-Mail Adresse des Nutzers:innen ungültig. Vergewissern Sie sich in der SAML-Ablaufverfolgung, dass das Feld `saml2:Attribute Name="email"` mit der E-Mail Adresse übereinstimmt, die der Nutzer:in für die Anmeldung verwendet. Wenn Sie Microsoft Entra ID (früher Azure Active Directory) verwenden, lautet die Abbildung der Attribute `email = user.userprincipalname`.

Bei der E-Mail Adresse wird zwischen Groß- und Kleinschreibung unterschieden. Sie muss genau mit der Adresse übereinstimmen, die in Braze eingerichtet wurde, einschließlich der in Ihrem Identitätsanbieter (wie Okta, OneLogin, Microsoft Entra ID und andere) konfigurierten Adresse.

Andere Fehler, die darauf hinweisen, dass Sie Probleme mit der E-Mail Adresse des Nutzers:innen haben, sind
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: Die E-Mail Adresse des Nutzers:innen ist nicht im Dashboard enthalten.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: Die E-Mail Adresse des Nutzers:innen ist leer oder anderweitig falsch konfiguriert.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` oder `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: Die E-Mail Adresse des Nutzers:innen stimmt nicht mit derjenigen überein, die für die Einrichtung von SSO verwendet wurde.

### Verfügen Sie über ein gültiges SAML-Zertifikat (x.509 Zertifikat)?

Sie können Ihr SAML-Zertifikat mit [diesem SAML-Validierungstool](https://www.samltool.com/validate_response.php) validieren. Beachten Sie, dass ein abgelaufenes SAML-Zertifikat auch ein ungültiges SAML-Zertifikat ist.

### Haben Sie ein korrektes SAML-Zertifikat (x.509 Zertifikat) hochgeladen?

Vergewissern Sie sich, dass das Zertifikat im Abschnitt `ds:X509Certificate` des SAML-Trace mit dem Zertifikat übereinstimmt, das Sie in Braze hochgeladen haben. Die Kopfzeile `-----BEGIN CERTIFICATE-----` und die Fußzeile `-----END CERTIFICATE-----` sind dabei nicht berücksichtigt.

### Haben Sie Ihr SAML-Zertifikat (x.509 Zertifikat) falsch eingegeben oder falsch formatiert?

Vergewissern Sie sich, dass das Zertifikat, das Sie im Braze-Dashboard eingereicht haben, keine Leerzeichen oder zusätzlichen Zeichen enthält.

Wenn Sie Ihr Zertifikat in Braze eingeben, muss es mit Privacy Enhanced Mail (PEM) kodiert und korrekt formatiert sein (einschließlich der `-----BEGIN CERTIFICATE-----` Kopfzeile und `-----END CERTIFICATE-----` Fußzeile). 

Hier ist ein Beispielzertifikat, das korrekt formatiert ist:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### Ist das Token des Nutzers:innen gültig?

Lassen Sie die betroffenen Nutzer:innen [den Cache und die Cookies ihres Browsers löschen](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) und versuchen Sie dann erneut, sich mit SAML SSO anzumelden.

### Haben Sie Ihren RelayState eingestellt?

Wenn Sie die Fehlermeldung `ERROR_CODE_SSO_INVALID_RELAY_STATE` erhalten, könnte Ihr RelayState falsch konfiguriert oder nicht vorhanden sein. Wenn Sie das noch nicht getan haben, müssen Sie Ihren RelayState in Ihrem IdP-Verwaltungssystem einstellen. Weitere Schritte finden Sie unter [Einrichten Ihres RelayState](#setting-up-your-relaystate). 

### Steckt der Nutzer:innen in einer Anmeldeschleife zwischen Okta und Braze fest?

Wenn sich ein Nutzer nicht anmelden kann, weil er zwischen dem Okta SSO und dem Braze-Dashboard hin und her wechselt, müssen Sie zu Okta gehen und das Ziel der SSO-URL auf Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) setzen (zum Beispiel `https://dashboard-07.braze.com`). 

Wenn Sie einen anderen IdP verwenden, überprüfen Sie, ob Ihr Unternehmen das richtige SAML- oder x.509 -Zertifikat auf Braze hochgeladen hat.

### Verwenden Sie eine manuelle Integration?

Wenn Ihr Unternehmen die App Braze nicht aus dem App Shop Ihres IdP heruntergeladen hat, müssen Sie die vorgefertigte Integration herunterladen. Wenn Okta zum Beispiel Ihr IdP ist, laden Sie die App von Braze von der [Integrationsseite](https://www.okta.com/integrations/braze/) herunter.
