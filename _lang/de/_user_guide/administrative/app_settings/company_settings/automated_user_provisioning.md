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

## Schritt 1: Zugriff auf die SCIM-Privatisierungseinstellungen

Gehen Sie im Braze-Dashboard zu **Einstellungen** > **Admin-Einstellungen** > **SCIM Provisioning**.

## Schritt 2: Konfigurieren Sie Ihre SCIM-Einstellungen

Um die SCIM-Bereitstellung zu aktivieren, geben Sie die folgenden Informationen an:

- **Standard Workspace:** Wählen Sie den Workspace aus, in dem neue Nutzer:innen standardmäßig hinzugefügt werden sollen. Wenn Sie in Ihrer [SCIM API-Anfrage]({{site.baseurl}}/post_create_user_account/) keinen Workspace angeben, weist Braze die Nutzer:innen diesem Workspace zu.
- **Herkunft der Dienste:** Geben Sie die Domain ein, aus der Ihre SCIM-Anfragen stammen. Braze verwendet dies im `X-Request-Origin` -Header, um zu überprüfen, woher die Anfragen kommen.
- **IP Allowlisting (optional):** Sie können SCIM-Anfragen auf bestimmte IP-Adressen beschränken.
Geben Sie eine durch Komma getrennte Liste oder einen Bereich von IP-Adressen ein, die zulässig sein sollen. Der `X-Request-Origin` -Header in jeder Anfrage wird verwendet, um die IP-Adresse der Anfrage mit der Zulassen-Liste zu vergleichen.

{% alert note %}
Dieser SCIM-Endpunkt lässt sich nicht direkt mit Identitätsanbietern integrieren.
{% endalert %}

![SCIM-Provisioning-Einstellungsformular mit drei Feldern: Standard Workspace, Herkunft des Dienstes und optionale IP-Zulassungsliste. Der Button "SCIM-Token generieren" ist deaktiviert.]({% image_buster /assets/img/scim_unfilled.png %})

## Schritt 3: Holen Sie sich Ihr SCIM-Token und Ihren Endpunkt

Nachdem Sie die erforderlichen Felder ausgefüllt haben, klicken Sie auf **SCIM-Token generieren**, um ein SCIM-Token zu generieren und Ihren SCIM API Endpunkt anzuzeigen. Stellen Sie sicher, dass Sie das SCIM Token kopieren, bevor Sie weg navigieren. **Dieser Token wird nur einmal vorgelegt.** 

![SCIM API Endpunkt und SCIM Token Felder werden mit maskierten Werten und Kopierbuttons angezeigt. Unterhalb des Token-Feldes befindet sich ein Button "Token zurücksetzen".]({% image_buster /assets/img/scim.png %})

Braze erwartet, dass alle SCIM-Anfragen das SCIM API-Inhaber-Token enthalten, das über einen HTTP `Authorization` -Header angehängt wird.

