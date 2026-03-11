---
nav_title: SAML Just-in-Time-Bereitstellung
article_title: SAML Just-in-Time-Bereitstellung
page_order: 1
page_type: tutorial
description: "Dieser Artikel führt Sie durch die Konfiguration der SAML-Just-in-Time-Bereitstellung, damit neue Unternehmensnutzer:innen bei ihrer ersten Anmeldung ein Braze-Konto erstellen können." 

---

# SAML Just-in-Time-Bereitstellung 

> Just-in-Time-Bereitstellung funktioniert mit [SAML SSO,]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) sodass neue Nutzer:innen bei ihrer ersten Anmeldung ein Braze-Konto erstellen können. Dadurch entfällt für Administratoren die Notwendigkeit, manuell ein Konto für einen neuen Unternehmensnutzer:in zu erstellen, dessen Berechtigungen auszuwählen, ihn einem Workspace zuzuweisen und darauf zu warten, dass er sein Konto aktiviert.

Aus Sicherheitsgründen funktioniert SAML Just-in-Time Provisioning (JITP) nur für Nutzer:innen mit E-Mail-Domains, die bereits in Ihrem Unternehmen vorhanden sind. JITP ist nur für Domains möglich, in denen bereits mindestens ein bestätigter Entwickler:in im Unternehmen tätig ist, der keinen Identitätswechsel betreibt. 

Nehmen wir beispielsweise an, dass das Konto JITP verwenden```jon.smith@decorumsoft.com``` kann, um sich bei Decorumsoft anzumelden. Das Konto```jane.smith@decorumsoft.com```verfügt über dieselbe Domain und kann ebenfalls für die Bereitstellung zugelassen werden. Wenn Sie jedoch versuchen, JITP mit zu verwenden```jon.smith@decorumsoft.eu```, ist die Bereitstellung nicht zulässig, da es kein ```decorumsoft.eu```Braze-Konto im Decorumsoft Braze-Dashboard gibt. 

Um eine Ausnahme für ein Unternehmen zu beantragen, wenden Sie sich bitte an [den Support]({{site.baseurl}}/braze_support/).

## Voraussetzungen

SAML JITP erfordert, dass SAML SSO eingerichtet und integriert ist. Es ist nicht mit Google SSO kompatibel und wird nur für von Identitätsanbietern initiierte (IdP-initiierte) Anmeldungen unterstützt.

## Einrichtung von SAML Just-in-Time-Provisioning (JITP)

Lassen Sie einen Braze-Administrator Folgendes tun:

1. Bitte navigieren Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen**.
2. Schalten Sie im Abschnitt **SAML SSO** die Option **Automatische Benutzerbereitstellung** ein.
3. Bitte wählen Sie einen Standard-Workspace aus, um einen neuen Unternehmensnutzer hinzuzufügen.
4. Bitte wählen Sie die Standardberechtigungen aus, die Sie dem neuen Nutzer:in zuweisen möchten. Wie Sie einen Berechtigungssatz erstellen, erfahren Sie unter [Festlegen von Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Wählen Sie unten auf der Seite **Änderungen speichern** 
7. Fügen Sie in den Einstellungen Ihres SSO-Anbieters alle Nutzer:innen, die auf Braze zugreifen müssen, zum Verzeichnis Ihres SSO-Anbieters hinzu.
8. Weisen Sie die Nutzer:innen an, sich bei ihrer ersten Anmeldung über Ihr IdP-Portal bei Braze anzumelden. Anschließend wird für zukünftige Anmeldungen der Button für das SAML-Single Sign-on angezeigt.

## Häufig gestellte Fragen

### Wie deaktiviere ich SAML JITP?

Nach der Einrichtung von JITP müssen Sie [sich an den Support wenden]({{site.baseurl}}/braze_support/), um es deaktivieren zu lassen.

## Fehlersuche

### Der Button für die einmalige Anmeldung wird mit Microsoft Entra ID nicht angezeigt.

Das Feld **„Anmelde-URL“** im Formular **„Grundlegende SAML-Konfiguration“** von Microsoft Entra für Braze kann dazu führen, dass Nutzer:innen bei der IdP-initiierten Anmeldung nur eine Option für das Passwort und keinen SSO-Button sehen. Um dieses Problem zu vermeiden, lassen Sie das Feld **„Anmelde-URL“** leer, wenn Sie Braze in Ihrem Microsoft Entra Admin Center konfigurieren.