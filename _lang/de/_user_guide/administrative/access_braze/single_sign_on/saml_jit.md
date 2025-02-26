---
nav_title: SAML Just-in-Time-Bereitstellung
article_title: SAML Just-in-Time-Bereitstellung
page_order: 1
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie SAML Just-in-Time Provisioning konfigurieren, damit neue Dashboard-Benutzer bei ihrer ersten Anmeldung ein Braze-Konto erstellen können." 

---

# SAML Just-in-Time-Bereitstellung 

> Just-in-Time Provisioning arbeitet mit [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), damit neue Dashboard-Benutzer bei ihrer ersten Anmeldung ein Braze-Konto erstellen können. Dadurch müssen Administratoren nicht mehr manuell ein Konto für einen neuen Dashboard-Benutzer erstellen, seine Berechtigungen auswählen, ihn einem Arbeitsbereich zuweisen und darauf warten, dass er sein Konto aktiviert.

{% alert note %}
SAML Just-in-Time Provisioning befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Customer-Success-Manager von Braze, wenn Sie an einer Teilnahme am Early Access interessiert sind.
{% endalert %}

## Voraussetzungen

Dieses Feature setzt voraus, dass SAML SSO eingerichtet und integriert ist, und ist nicht mit Google SSO kompatibel.

## SAML Just-in-Time-Bereitstellung einrichten

Lassen Sie einen Braze-Administrator Folgendes tun:

1. Navigieren Sie zu **Einstellungen** > **Sicherheitseinstellungen**.
2. Schalten Sie im Abschnitt **SAML SSO** die Option **Automatische Benutzerbereitstellung** ein.
3. Wählen Sie einen Standard-Workspace aus, um einen neuen Dashboard Nutzer:innen hinzuzufügen.
4. Wählen Sie die Standardberechtigung, die dem neuen Dashboard-Benutzer zugewiesen werden soll. Wie Sie einen Berechtigungssatz erstellen, erfahren Sie unter [Festlegen von Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Wählen Sie unten auf der Seite **Änderungen speichern** 
7. Fügen Sie in den Einstellungen Ihres SSO-Anbieters alle Nutzer:innen, die auf Braze zugreifen müssen, zum Verzeichnis Ihres SSO-Anbieters hinzu.
8. Jetzt können sich Benutzer anmelden oder einloggen.