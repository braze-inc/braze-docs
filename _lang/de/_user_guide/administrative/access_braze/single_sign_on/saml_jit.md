---
nav_title: SAML Just-in-Time-Bereitstellung
article_title: SAML Just-in-Time-Bereitstellung
page_order: 1
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie SAML Just-in-Time Provisioning konfigurieren, damit neue Dashboard-Benutzer bei ihrer ersten Anmeldung ein Braze-Konto erstellen können." 

---

# SAML Just-in-Time-Bereitstellung 

> Just-in-Time Provisioning arbeitet mit [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), damit neue Dashboard-Benutzer bei ihrer ersten Anmeldung ein Braze-Konto erstellen können. Dadurch müssen Administratoren nicht mehr manuell ein Konto für einen neuen Dashboard-Benutzer erstellen, seine Berechtigungen auswählen, ihn einem Arbeitsbereich zuweisen und darauf warten, dass er sein Konto aktiviert.

Als Sicherheitsmaßnahme funktioniert SAML Just-in-Time Provisioning (JITP) nur für Nutzer:innen mit E-Mail Domains, die bereits in Ihrem Unternehmen existieren. JITP ist nur für Domains möglich, für die es bereits mindestens einen bestätigten, nicht-identitätswechselnden Entwickler:in im Unternehmen gibt. 

Nehmen wir zum Beispiel an, dass das Konto ```jon.smith@decorumsoft.com``` JITP verwenden kann, um sich bei Decorumsoft anzumelden. Das Konto ```jane.smith@decorumsoft.com``` hat dieselbe Domain und kann ebenfalls zulässig provisioniert werden. Wenn Sie jedoch versuchen, JITP mit ```jon.smith@decorumsoft.eu``` zu verwenden, wird die Bereitstellung nicht zulässig sein, da es kein ```decorumsoft.eu``` -Konto im Decorumsoft Braze-Dashboard gibt. 

Um eine Ausnahme für ein Unternehmen zu machen, wenden Sie sich an den [Support]({{site.baseurl}}/braze_support/).

## Voraussetzungen

SAML JITP setzt voraus, dass SAML SSO eingerichtet und integriert ist. Sie ist nicht mit Google SSO kompatibel und wird nur für vom Identitätsanbieter initiierte (IdP-initiierte) Anmelde-Workflows unterstützt.

## SAML Just-in-Time-Bereitstellung (JITP) einrichten

Lassen Sie einen Braze-Administrator Folgendes tun:

1. Navigieren Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen**.
2. Schalten Sie im Abschnitt **SAML SSO** die Option **Automatische Benutzerbereitstellung** ein.
3. Wählen Sie einen Standard-Workspace aus, um einen neuen Dashboard Nutzer:innen hinzuzufügen.
4. Wählen Sie die Standardberechtigung, die dem neuen Dashboard-Benutzer zugewiesen werden soll. Wie Sie einen Berechtigungssatz erstellen, erfahren Sie unter [Festlegen von Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Wählen Sie unten auf der Seite **Änderungen speichern** 
7. Fügen Sie in den Einstellungen Ihres SSO-Anbieters alle Nutzer:innen, die auf Braze zugreifen müssen, zum Verzeichnis Ihres SSO-Anbieters hinzu.
8. Jetzt können sich Benutzer anmelden oder einloggen.

## Häufig gestellte Fragen

### Wie kann ich SAML JITP deaktivieren?

Nachdem Sie JITP eingerichtet haben, müssen Sie [sich an den Support wenden]({{site.baseurl}}/braze_support/), um es zu deaktivieren.

## Fehlersuche

### Single Sign-Button erscheint nicht mit Microsoft Entra ID

Das Feld **Anmelde-URL** im Formular **SAML-Basiskonfiguration** von Microsoft Entra für Braze kann dazu führen, dass Nutzer:innen bei einer von einem IdP initiierten Anmeldung nur eine Passwort-Option und keinen SSO-Button sehen. Um dieses Problem zu vermeiden, lassen Sie das Feld **Anmelde-URL** leer, wenn Sie Braze in Ihrem Microsoft Entra Admin Center konfigurieren.