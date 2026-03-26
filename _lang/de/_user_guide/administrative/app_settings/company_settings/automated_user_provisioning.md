---
nav_title: "Automatisierte Bereitstellung von Nutzer:innen"
article_title: Automatisierte Benutzerbereitstellung
page_order: 10
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, welche Informationen Sie für die automatische Bereitstellung von Nutzer:innen bereitstellen müssen und wie und wo Sie Ihr generiertes System for Cross-Domain Identity Management (SCIM) Token verwenden."
alias: /scim/automated_user_provisioning/

---

# Automatisierte Bereitstellung von Nutzer:innen

> Verwenden Sie SCIM Provisioning, um Nutzer:innen von Braze automatisch über APIs zu erstellen und zu verwalten. In diesem Artikel erfahren Sie, welche Informationen Sie angeben müssen, wie Sie Ihr SCIM-Token generieren und wo Sie Ihren SCIM-API-Endpunkt finden.

{% multi_lang_include early_access_beta_alert.md feature='SCIM provisioning' %}

## Zugriff auf die SCIM-Bereitstellungseinstellungen

1. Bitte navigieren Sie im Braze-Dashboard zu **„Einstellungen“** > **„Admin-Einstellungen“** > **„SCIM-Bereitstellung**“ und wählen Sie anschließend **„SCIM-Integration auswählen**“.
2. Wählen Sie im Konfigurationsschritt **von Braze** eine Bereitstellungsmethode aus und geben Sie die Zugriffseinstellungen an.

![Eine Seite zur Einrichtung der SCIM-Integration mit Abschnitten, in denen man eine Bereitstellungsmethode auswählt und Zugriffseinstellungen angibt.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Befolgen Sie im Schritt zur** IdP-Konfiguration** die Anweisungen innerhalb der Plattform für die Methode, die Sie ausgewählt haben.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Bitte verwenden Sie die Option **„Okta – Braze-App“,** wenn Sie die Braze-App für SAML SSO in Okta eingerichtet haben. Wenn Sie eine benutzerdefinierte App für SSO einrichten möchten, befolgen Sie bitte die Anweisungen auf dem Tab [„Okta – Integration benutzerdefinierter Apps]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning)“.

## Schritt 1: SCIM-Bereitstellung einrichten

### Schritt 1.1: SCIM aktivieren

1. Bitte navigieren Sie in Okta zu **„Anwendungen“** > **„Anwendungen“** und wählen Sie anschließend **„App-Integration auswählen**“. Bitte wählen Sie **SAML 2.0** als Anmeldemethode aus.
2. Bitte füllen Sie die folgenden Angaben aus (die sich im [Konfigurationsschritt](#accessing-scim-provisioning-settings) „Braze [**IdP“**](#accessing-scim-provisioning-settings) befinden), um eine angepasste App zu erstellen:
- App-Logo
- URL für Single Sign-on
- Zielgruppen-URL (SP-Entity-ID)
3. Wählen Sie **Finish**.
4. Bitte wählen Sie das Tab **„Allgemein**“. 
5. Bitte wählen Sie im Abschnitt **„App-Einstellungen**“ **die Option „Bearbeiten**“.
6. Wählen Sie im Feld **„Bereitstellung“** **die Option „SCIM“** aus. 

### Schritt 1.2: Anwendungssichtbarkeit deaktivieren

1. Wählen Sie im Feld **„Anzeigbarkeit der** **Anwendung**“ das Kontrollkästchen **„Anwendungssymbol für Nutzer:innen nicht anzeigen“** aus. Dadurch wird verhindert, dass Nutzer:innen über die App auf SSO zugreifen, die ausschließlich für SCIM vorgesehen ist. 
2. Wählen Sie **Speichern**.

### Schritt 1.3: Richten Sie die SCIM-Integration ein.

1. Bitte wählen Sie den Tab **„Bereitstellung**“.
2. Bitte wählen Sie unter **„Einstellungen“** > **„Integration“** > **„SCIM-Verbindung“** die Option **„Bearbeiten“** und geben Sie die Feldwerte ein, die in der Tabelle auf der Seite **„SCIM-Bereitstellung einrichten“** angezeigt werden.

### Schritt 1.4: API-Zugangsdaten testen

Bitte wählen Sie **„Test-API-Zugangsdaten“** aus. Bei erfolgreicher Integration wird eine Bestätigungsnachricht angezeigt, und Sie können speichern.

### Schritt 1.5: Bitte aktivieren Sie die Bereitstellung für die App.

1. Wählen Sie unter **„Bereitstellung“** > **„Einstellungen“** > **„Zur App**“ > **„Bereitstellung zur App**“ die Option **„Bearbeiten**“.
2. Aktivieren Sie Folgendes:
    - Create Users (Nutzer:innen erstellen)
    - Update Users Attributes (Nutzer-Attribute aktualisieren)
    - Deactivate Users (Nutzer:innen deaktivieren)
3. Überprüfen und konfigurieren Sie den Abschnitt **„Attributzuordnung“** mit den Abbildungen, die in der Tabelle auf der Seite **„SCIM-Bereitstellung einrichten“** angezeigt werden.

## Schritt 2: Nutzer:innen der App zuweisen

1. Bitte wählen Sie das Tab **„Zuweisung**“.
2. Bitte wählen Sie **„Zuweisen“** und anschließend eine Option aus.
3. Weisen Sie die App den Personen zu, die Zugriff auf Braze haben sollen.
4. Bitte wählen Sie **„Fertig“,** wenn Sie die Aufgabe abgeschlossen haben.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Bitte verwenden Sie die Option **„Okta – Benutzerdefinierte App-Integration“,** wenn Sie eine benutzerdefinierte App für SSO einrichten. Wenn Sie die Braze-App für SAML SSO in Okta einrichten möchten, befolgen Sie bitte die Anweisungen auf dem Tab [„Okta – Braze-App]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning)“.

## Schritt 1: SCIM-Bereitstellung einrichten

### Schritt 1.1: SCIM aktivieren

1. Bitte gehen Sie in Okta zu Ihrer Braze-App.
2. Bitte wählen Sie das Tab **„Allgemein**“.
3. Bitte wählen Sie im Abschnitt **„App-Einstellungen**“ **die Option „Bearbeiten**“.
4. Wählen Sie im Feld **„Bereitstellung“** **die Option „SCIM“** aus.
5. Wählen Sie **Speichern**.

### Schritt 1.2: SCIM-Integration einrichten

1. Bitte wählen Sie den Tab **„Bereitstellung**“.
2. Bitte gehen Sie zu **„Einstellungen“** > **„Integration“** > **„SCIM-Verbindung“**, wählen Sie **„Bearbeiten“** und wählen Sie die Feldwerte aus, die in der Tabelle auf der Seite **„SCIM-Bereitstellung einrichten“** angezeigt werden.
3. Bitte überprüfen Sie die API-Zugangsdaten, indem Sie **„API-Zugangsdaten testen“** auswählen.
4. Wählen Sie **Speichern**.

### Schritt 1.3: Bitte aktivieren Sie die Bereitstellung für die App.

1. Wählen Sie unter **„Bereitstellung“** > **„Einstellungen“** > **„Zur App**“ > **„Bereitstellung zur App**“ die Option **„Bearbeiten**“.
2. Aktivieren Sie Folgendes:
    - Create Users (Nutzer:innen erstellen)
    - Update Users Attributes (Nutzer-Attribute aktualisieren)
    - Deactivate Users (Nutzer:innen deaktivieren)
3. Überprüfen und konfigurieren Sie den Abschnitt **„Attributzuordnung“** mit den Abbildungen, die in der Tabelle auf der Seite **„SCIM-Bereitstellung einrichten“** angezeigt werden.

## Schritt 2: Nutzer:innen der App zuweisen

1. Bitte wählen Sie das Tab **„Zuweisung**“.
2. Bitte wählen Sie **„Zuweisen“** und anschließend eine Option aus.
3. Weisen Sie die App den Personen zu, die Zugriff auf Braze haben sollen.
4. Wählen Sie **Erledigt**.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include early_access_beta_alert.md feature='The Entra ID integration' %}

## Schritt 1: SCIM-Bereitstellungs-App einrichten

### Schritt 1.1: Melden Sie sich im Microsoft Entra Admin Center an.

Bitte melden Sie sich bei Ihrem Microsoft Entra Admin Center an.

### Schritt 1.2: Erstellen und konfigurieren Sie Ihre SCIM-App

1. Bitte navigieren Sie im Menü zu **„Entra ID**“ > **„Unternehmens-Apps**“.
2. Bitte wählen Sie **„Neue Anwendung**“.
3. Bitte wählen Sie **„Eigene Anwendung erstellen**“.
4. Bitte geben Sie im Panel einen Namen für Ihre App ein.
5. Auswählen Sie im Abschnitt **„Was möchten Sie mit Ihrer Anwendung tun?**“ die **Option „Integration der Anwendung**, **die Sie nicht in der Galerie finden (Nicht in der Galerie)**“ aus.
6. Wählen Sie **Erstellen**.

### Schritt 1.3: SCIM-Integration einrichten

1. Bitte gehen Sie zum Abschnitt **„Verwalten** > **Bereitstellung“** Ihrer SCIM-Anwendung.
2. Wählen Sie **„Anwendung verbinden“** oder **„Neue Konfiguration“** und wählen Sie die Feldwerte aus, die in der Tabelle auf der Seite **„SCIM-Bereitstellung einrichten**“ angezeigt werden.

### Schritt 1.4: Bitte aktivieren Sie die Bereitstellung für die App.

1. Bitte gehen Sie in Ihrer SCIM-Anwendung zum Abschnitt **„Verwalten** > **Attribut-Abbildung (Vorschau)**“.
2. Bitte wählen Sie **„Microsoft Entra ID-Nutzer:innen bereitstellen**“ aus.
3. Überprüfen und konfigurieren Sie den Abschnitt **„Attribut-Abbildung“,** um die Attribute anzupassen, die in der Tabelle auf der Seite **„SCIM-Bereitstellung einrichten“** angezeigt werden.
4. Schließen Sie die Seite **„Attribut-Abbildung**“.

## Schritt 2: Nutzer:innen der App zuweisen

1. Bitte gehen Sie zu **„Verwalten** > **Nutzer:innen und Gruppen**“.
2. Bitte wählen Sie **„Nutzer:in/Gruppe hinzufügen**”.
3. Wählen Sie **„Keine Auswahl“** aus, um der App Nutzer:innen zuzuweisen.
4. Bitte wählen Sie den Button **„Auswählen“,** um die Zuweisung zu bestätigen.

{% endtab %}
{% tab Custom %}

## Schritt 1: Konfigurieren Sie Ihre SCIM-Einstellungen

- **Standard Workspace:** Bitte wählen Sie den Workspace aus, in dem neue Nutzer:innen standardmäßig hinzugefügt werden sollen. Wenn Sie in Ihrer [SCIM API-Anfrage]({{site.baseurl}}/post_create_user_account/) keinen Workspace angeben, weist Braze die Nutzer:innen diesem Workspace zu.
- **Herkunft der Dienste:** Geben Sie die Domain ein, aus der Ihre SCIM-Anfragen stammen. Braze verwendet dies im `X-Request-Origin` -Header, um zu überprüfen, woher die Anfragen kommen.
- **IP Allowlisting (optional):** Sie können SCIM-Anfragen auf bestimmte IP-Adressen beschränken. Geben Sie eine durch Komma getrennte Liste oder einen Bereich von IP-Adressen ein, die zulässig sein sollen. Der`X-Request-Origin`Header in jeder Anfrage wird verwendet, um die IP-Adresse der Anfrage mit der Zulassungsliste abzugleichen.

![Formular SCIM Provisioning-Einstellungen mit drei Feldern: Standard-Workspace, Herkunft des Dienstes und optionale IP-Zulassungsliste. Der Button „SCIM-Token generieren“ ist deaktiviert.]({% image_buster /assets/img/scim_unfilled.png %})

## Schritt 2: Erstellen Sie einen SCIM-Token.

Nachdem Sie die erforderlichen Felder ausgefüllt haben, klicken Sie auf **SCIM-Token generieren**, um ein SCIM-Token zu generieren und Ihren SCIM API Endpunkt anzuzeigen. Stellen Sie sicher, dass Sie das SCIM Token kopieren, bevor Sie weg navigieren. **Dieser Token erscheint nur einmal.** 

![SCIM API Endpunkt und SCIM Token Felder werden mit maskierten Werten und Kopierbuttons angezeigt. Unterhalb des Token-Feldes befindet sich der Button „Token zurücksetzen“.]({% image_buster /assets/img/scim.png %})

Braze erwartet, dass alle SCIM-Anfragen das SCIM API-Inhaber-Token enthalten, das über einen HTTP `Authorization` -Header angehängt wird.

{% endtab %}
{% endtabs %}
