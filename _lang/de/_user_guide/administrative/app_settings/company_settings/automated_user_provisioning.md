---
nav_title: Automatisierte Benutzerbereitstellung
article_title: Automatisierte Benutzerbereitstellung
page_order: 10
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, welche Informationen Sie für die automatische Bereitstellung von Nutzer:innen bereitstellen müssen und wie und wo Sie Ihr generiertes System for Cross-Domain Identity Management (SCIM) Token verwenden."
alias: /scim/automated_user_provisioning/

---

# Automatisierte Bereitstellung von Nutzer:innen

> Erfahren Sie, was Sie für die automatisierte Bereitstellung von Nutzer:innen bereitstellen müssen und wie und wo Sie Ihr generiertes System for Cross-Domain Identity Management (SCIM) Token und den SCIM API Endpunkt verwenden. Sie können diesen Endpunkt dann mit Ihrer API aufrufen, um automatisch neue Nutzer:innen für das Dashboard bereitzustellen.

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **SCIM Provisioning**.

## Wie Sie Ihr SCIM-Token erhalten

Um Ihren SCIM Token zu erhalten, müssen Sie die folgenden Informationen angeben:

1. Wählen Sie einen Standardarbeitsbereich aus, zu dem neue Dashboard-Entwickler hinzugefügt werden sollen. Wenn Sie beim [SCIM-API-Aufruf Nutzer:innen erstellen]({{site.baseurl}}/post_create_user_account/) keinen Workspace angeben, werden sie hier hinzugefügt.
2. Bieten Sie eine Herkunft für Dienste an. Anhand des Service-Ursprungs kann Braze erkennen, woher die Anfrage kommt.
3. Geben Sie optional eine kommagetrennte Liste oder einen Bereich von IP-Adressen an, die für SCIM-Anfragen zulässig sind. Der `X-Origin-Request` -Header in jeder Anfrage wird verwendet, um die IP-Adresse der Anfrage mit der Zulassen-Liste zu vergleichen.<br><br>

{% alert note %}
Dieser SCIM-Endpunkt lässt sich nicht direkt mit Identitätsanbietern integrieren.
{% endalert %}

![][1]

Nachdem Sie die erforderlichen Felder ausgefüllt haben, können Sie ein SCIM-Token generieren und Ihren SCIM API Endpunkt sehen. **Dieser Token wird nur einmal vorgelegt.** Braze erwartet, dass alle SCIM-Anfragen das SCIM API-Inhaber-Token enthalten, das über einen HTTP `Authorization` -Header angehängt wird.

[1]: {% image_buster /assets/img/scim.png %}
