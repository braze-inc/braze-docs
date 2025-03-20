---
nav_title: SAML SSO-Einrichtung
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
| RelayState API-Schlüssel | Gehen Sie zu **Einstellungen** > **API-Schlüssel** und erstellen Sie einen API-Schlüssel mit `sso.saml.login` Berechtigungen und geben Sie dann den generierten API-Schlüssel als `RelayState` Parameter in Ihren IdP ein. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie Ihre API-Schlüssel unter **Einstellungen** unter **Entwicklerkonsole** > **API-Einstellungen**.
{% endalert %}

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

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, wählen Sie Ihr Kontosymbol und gehen Sie zu **Unternehmenseinstellungen** > **Sicherheitseinstellungen**, um den Abschnitt SAML SSO zu finden.
{% endalert %}

Geben Sie auf derselben Seite Folgendes ein:

| Anforderung | Details |
|---|---|
| `SAML Name` | Dieser Text wird auf der Schaltfläche auf dem Anmeldebildschirm angezeigt.<br>Meist der Name Ihres Identitätsanbieters, also z. B. "Okta". |
| `Target URL` | Wird nach der Einrichtung von Braze bei Ihrem IdP angegeben.<br> Einige IdP bezeichnen sie auch als SSO-URL oder SAML-2.0-Endpunkt. |
| `Certificate` | Das `x.509` Zertifikat, das von Ihrem Identitätsanbieter bereitgestellt wird.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Achten Sie darauf, dass Ihr `x.509`-Zertifikat diesem Format entspricht, wenn Sie es in das Dashboard aufnehmen:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Öffnen der Sicherheitseinstellungen und Hinzufügen von SAML SSO-Details]({% image_buster /assets/img/samlsso.gif %})

### Schritt 3: Bei Braze anmelden

Speichern Sie Ihre Sicherheitseinstellungen und melden Sie sich ab. Melden Sie sich dann wieder bei Ihrem Identitätsanbieter an.

![Dashboard-Anmeldebildschirm mit aktiviertem SSO]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

## SSO-Verhalten

Personen, die SSO nutzen, können nicht mehr wie bisher ihr Passwort verwenden. Wer sein Passwort weiter verwenden will, kann dies tun, sofern die folgenden Einschränkungen es nicht verhindern.

## Einschränkung

Sie können die Angehörigen Ihrer Organisation auf eine Anmeldung per Google SSO oder SAML SSO beschränken. Um die Einschränkungen zu aktivieren, öffnen Sie die **Sicherheitseinstellungen** und wählen Sie entweder **Anmeldung nur per Google SSO** oder **Anmeldung nur mit angepasstem SAML SSO**.

![Abschnitt zu Authentifizierungsregeln in den Sicherheitseinstellungen]({% image_buster /assets/img/sso3.png %})

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

![Menü "SAML-Trace-Einstellungen exportieren" mit der Auswahl "Keine".]({% image_buster /assets/img/export_saml_trace_preferences.png %})
