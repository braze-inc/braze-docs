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

## Zugriff auf SCIM-Einstellungen für die Bereitstellung

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **Admin-Einstellungen** > **SCIM Provisioning** und fügen Sie einen Identitätsanbieter hinzu.
2. Im Schritt **Braze Provisioning** wählen Sie eine Provisioning-Methode aus und geben die Zugriffseinstellungen an.

![Eine Seite zum Einrichten der SCIM-Integration mit Abschnitten zum Auswählen einer Bereitstellungsmethode und zum Bereitstellen von Zugriffseinstellungen.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Im Schritt **IdP-Konfiguration** folgen Sie den Schritten innerhalb der Plattform für die von Ihnen ausgewählte Bereitstellungsmethode.

{% tabs %}
{% tab Okta - Braze app %}

{% alert important %}
Die Okta-Integration befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Schritt 1: SCIM-Bereitstellung einrichten

### Schritt 1.1: SCIM aktivieren

1. Gehen Sie zu Ihrer Braze App in Okta.
2. Wählen Sie den Tab **Allgemein**.
3. Wählen Sie im Bereich **App-Einstellungen** die Option **Bearbeiten**.
4. Wählen Sie im Feld **Provisionierung** **SCIM** aus und wählen Sie dann **Speichern**.

### Schritt 1.2: SCIM-Integration einrichten

1. Wählen Sie den Tab **Provisioning**.
2. Wählen Sie unter **Einstellungen** > **Integration** > **SCIM-Verbindung** die Option **Bearbeiten** aus und geben Sie die Feldwerte ein, die in der Tabelle auf der Seite **SCIM-Provisioning einrichten** angezeigt werden.

### Schritt 1.3: API-Zugangsdaten testen

Wählen Sie **API-Zugangsdaten testen**. Wenn die Integration erfolgreich war, erscheint eine Nachricht zur Bestätigung und Sie können speichern.

### Schritt 1.4: Bereitstellung für die App aktivieren

1. Wählen Sie unter **Provisionierung** > **Einstellungen** > **Zu App** > **Provisionierung zu App** die Option **Bearbeiten**.
2. Aktivieren Sie Folgendes:
    - Create Users (Nutzer:innen erstellen)
    - Update Users Attributes (Nutzer-Attribute aktualisieren)
    - Deactivate Users (Nutzer:innen deaktivieren)
3. Überprüfen und konfigurieren Sie den Abschnitt **Attribute Mapping** mit den Abbildungen, die in der Tabelle auf der Seite **Setup SCIM Provisioning** angezeigt werden.

## Schritt 2: Weisen Sie Nutzer:innen der App zu

1. Wählen Sie den Tab **Zuweisung** aus.
2. Wählen Sie **Zuweisen** und wählen Sie eine Option aus.
3. Weisen Sie die App den Personen zu, die Zugriff auf Braze haben sollen.
4. Wählen Sie **Erledigt**, wenn Sie die Aufgabe abgeschlossen haben.

{% endtab %}
{% tab Okta - Custom app integration %}

{% alert important %}
Die Okta-Integration befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Schritt 1: SCIM-Bereitstellung einrichten

### Schritt 1.1: SCIM aktivieren

1. Gehen Sie in Okta zu Ihrer Braze App.
2. Wählen Sie den Tab **Allgemein**.
3. Wählen Sie im Bereich **App-Einstellungen** die Option **Bearbeiten**.
4. Wählen Sie im Feld **Provisionierung** **SCIM** aus.
5. Wählen Sie **Speichern**.

### Schritt 1.2: SCIM-Integration einrichten

1. Wählen Sie den Tab **Provisioning**.
2. Wählen Sie unter **Einstellungen** > **Integration** > **SCIM-Verbindung** die Option **Bearbeiten** aus, und geben Sie die Feldwerte ein, die in der Tabelle auf der Seite **SCIM-Provisioning einrichten** angezeigt werden.
3. Testen Sie die API-Zugangsdaten, indem Sie **API-Zugangsdaten testen** auswählen.
4. Wählen Sie **Speichern**.

### Schritt 1.3: Bereitstellung für die App aktivieren

1. Wählen Sie unter **Provisionierung** > **Einstellungen** > **Zu App** > **Provisionierung zu App** die Option **Bearbeiten**.
2. Aktivieren Sie Folgendes:
    - Create Users (Nutzer:innen erstellen)
    - Update Users Attributes (Nutzer-Attribute aktualisieren)
    - Deactivate Users (Nutzer:innen deaktivieren)
3. Überprüfen und konfigurieren Sie den Abschnitt **Attribute Mapping** mit den Abbildungen, die in der Tabelle auf der Seite **Setup SCIM Provisioning** angezeigt werden.

## Schritt 2: Weisen Sie Nutzer:innen der App zu

1. Wählen Sie den Tab **Zuweisung** aus.
2. Wählen Sie **Zuweisen** und wählen Sie eine Option aus.
3. Weisen Sie die App den Personen zu, die Zugriff auf Braze haben sollen.
4. Wählen Sie **Erledigt**.

{% endtab %}
{% tab Entra ID %}

{% alert important %}
Die Integration von Entra ID befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Schritt 1: SCIM-Bereitstellungs-App einrichten

### Schritt 1.1. Melden Sie sich im Microsoft Entra Admin Center an
Melden Sie sich bei Ihrem Microsoft Entra Admin Center an.

### Schritt 1.2: Erstellen und Einrichten Ihrer SCIM App

1. Gehen Sie im Navigationsmenü zu **Entra ID** > **Enterprise Apps**.
2. Wählen Sie **Neue Anwendung**.
3. Wählen Sie **Eigene Anwendung erstellen**.
4. Geben Sie in dem Panel einen Namen für Ihre App ein.
5. Wählen Sie im Abschnitt **Was möchten Sie mit Ihrer Anwendung tun?** **Anwendung integrieren, die Sie nicht in der Galerie finden (Nicht-Galerie**).
6. Wählen Sie **Erstellen**.

### Schritt 1.3: SCIM-Integration einrichten

1. Gehen Sie in Ihrer SCIM-Anwendung in den Bereich **Verwalten** > **Provisionierung**.
2. Wählen Sie **Ihre Anwendung verbinden** oder **Neue Konfiguration** aus und geben Sie die Feldwerte ein, die in der Tabelle auf der Seite **SCIM-Provisioning einrichten** angezeigt werden.

### Schritt 1.4: Bereitstellung für die App aktivieren

1. Gehen Sie zum Abschnitt **Verwalten** > **Abbildung von Attributen (Vorschau)** in Ihrer SCIM-Anwendung.
2. Wählen Sie **Bereitstellung Microsoft Entra ID Nutzer**: **innen**.
3. Überprüfen und konfigurieren Sie den Abschnitt **Abbildung der Attribute** so, dass sie mit den Attributen übereinstimmen, die in der Tabelle auf der Seite **Setup SCIM Provisioning** angezeigt werden.
4. Schließen Sie die Seite **Attribut-Abbildung**.

## Schritt 2: Weisen Sie Nutzer:innen der App zu

1. Gehen Sie zu **Verwalten** > **Nutzer:innen und Gruppen**.
2. Wählen Sie **Nutzer:in/Gruppe hinzufügen**.
3. Wählen Sie **Keine ausgewählt**, um Nutzer:innen der App zuzuweisen.
4. Wählen Sie den Button **Auswählen**, um die Zuweisung zu bestätigen.

{% endtab %}
{% tab Custom %}

## Schritt 1: Konfigurieren Sie Ihre SCIM-Einstellungen

- **Standard Workspace:** Wählen Sie den Workspace aus, in dem neue Nutzer:innen standardmäßig hinzugefügt werden sollen. Wenn Sie in Ihrer [SCIM API-Anfrage]({{site.baseurl}}/post_create_user_account/) keinen Workspace angeben, weist Braze die Nutzer:innen diesem Workspace zu.
- **Herkunft der Dienste:** Geben Sie die Domain ein, aus der Ihre SCIM-Anfragen stammen. Braze verwendet dies im `X-Request-Origin` -Header, um zu überprüfen, woher die Anfragen kommen.
- **IP Allowlisting (optional):** Sie können SCIM-Anfragen auf bestimmte IP-Adressen beschränken. Geben Sie eine durch Komma getrennte Liste oder einen Bereich von IP-Adressen ein, die zulässig sein sollen. Der `X-Request-Origin` -Header in jeder Anfrage wird verwendet, um die IP-Adresse der Anfrage mit der Zulassen-Liste zu vergleichen.

![Formular SCIM Provisioning-Einstellungen mit drei Feldern: Standard Workspace, Herkunft des Dienstes und optionale IP-Zulassungsliste. Der Button "SCIM-Token generieren" ist deaktiviert.]({% image_buster /assets/img/scim_unfilled.png %})

## Schritt 2: Generieren Sie ein SCIM Token

Nachdem Sie die erforderlichen Felder ausgefüllt haben, klicken Sie auf **SCIM-Token generieren**, um ein SCIM-Token zu generieren und Ihren SCIM API Endpunkt anzuzeigen. Stellen Sie sicher, dass Sie das SCIM Token kopieren, bevor Sie weg navigieren. **Dieses Token erscheint nur einmal.** 

![SCIM API Endpunkt und SCIM Token Felder werden mit maskierten Werten und Kopierbuttons angezeigt. Unterhalb des Token-Feldes befindet sich ein Button "Token zurücksetzen".]({% image_buster /assets/img/scim.png %})

Braze erwartet, dass alle SCIM-Anfragen das SCIM API-Inhaber-Token enthalten, das über einen HTTP `Authorization` -Header angehängt wird.

{% endtab %}
{% endtabs %}
