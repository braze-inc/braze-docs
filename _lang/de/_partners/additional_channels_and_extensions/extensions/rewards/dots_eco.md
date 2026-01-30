---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "Dieser referenzierte Artikel beschreibt die Integration von Braze und DOTS.ECO."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) können Sie Nutzer:innen mit nachvollziehbaren digitalen Zertifikaten für ihren realen Umwelteinfluss belohnen. Jedes Zertifikat kann Metadaten wie die URL des Zertifikats und die URL des Bildes enthalten, so dass Nutzer:innen ihren Wirkungsnachweis einsehen (und wieder aufrufen) können.

_Diese Integration wird von DOTS.ECO gepflegt._

## Über diese Integration

Braze und DOTS.ECO verbinden Customer-Engagement-Journeys mit realen Impact Rewards. Von einem Braze-Canvas- oder Kampagnen-Schritt aus können Sie eine Anfrage zur Erstellung eines DOTS.ECO Zertifikats mit Hilfe von Connected Content auslösen. DOTS.ECO gibt Zertifikats-Metadaten (wie `certificate_url` und `certificate_image_url`) zurück, die Sie im Benutzerprofil als angepasste Attribute speichern und über Kanäle wie In-App-Nachrichten, Content Cards und Push-Benachrichtigungen wiederverwenden können.

## Anwendungsfälle

- Triggern Sie ein Wirkungszertifikat, wenn ein Nutzer:innen ein wichtiges Ereignis (Kauf, Levelabschluss, Abo, Empfehlung) abschließt.
- Zeigen Sie ein personalisiertes Zertifikatsbild in einer In-App-Nachricht an, nachdem der Schritt Connected-Content erfolgreich war.
- Fügen Sie eine Content-Card "Ihr Zertifikat anzeigen" mit der Zertifikats-URL für den späteren Zugriff hinzu.
- Speichern Sie Zertifikats-Metadaten (wie `certificate_url`, `certificate_image_url`, `certificate_header` und `greeting`) als angepasste Attribute zur Wiederverwendung in zukünftigen Nachrichten.
- Weisen Sie Zertifikate unter Verwendung einer entfernten Nutzer:innen ID zu, so dass Nutzer:innen ihre Wirkung später beanspruchen und einsehen können.
- Führen Sie A/B-Tests mit Impact Messaging durch (unterschiedliche Texte/Bilder), während Sie denselben Update-Fluss für Nutzer:innen beibehalten. DOTS.ECO 


## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|---|---|
| DOTS.ECO Konto | DOTS.ECO Zugang zum Konto. |
| DOTS.ECO Zugangsdaten | Für die Anfrage in diesem Artikel benötigen Sie ein DOTS.ECO App Token, einen API-Schlüssel und eine ID für die Zuordnung. Um diese abzurufen, wenden Sie sich an Ihren DOTS.ECO Customer-Success-Manager:in. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Erstellen Sie diesen Schlüssel auf dem Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrieren DOTS.ECO

### Schritt 1: Erstellen Sie ein Canvas und fügen Sie einen Nutzer:innen-Update-Schritt hinzu.

Erstellen Sie im Braze-Dashboard ein neues Canvas, das triggert, wenn ein Nutzer:innen ein Schlüsselereignis (z.B. einen Kauf, ein Abo oder einen Meilenstein) abgeschlossen hat.

Fügen Sie einen Schritt Nutzer:innen Update direkt nach dem Eingang hinzu. Mit diesem Schritt wird die DOTS.ECO API über Connected-Content aufgerufen und die zurückgegebenen Zertifikatsdaten im Nutzerprofil gespeichert.

Verwenden Sie diesen Schritt, um die DOTS.ECO API über Connected-Content aufzurufen und die zurückgegebenen Zertifikatsdaten im Nutzerprofil zu speichern.

### Schritt 2: JSON vorbringen: Stellen Sie mit Connected-Content eine POST-Anfrage an DOTS.ECO 

Wechseln Sie im Schritt **Nutzer:innen aktualisieren** zum **erweiterten JSON-Editor** und verwenden Sie Connected-Content, um eine POST-Anfrage an die DOTS.ECO certificate API zu stellen.

Verwenden Sie den Tag `capture` und eine Anfrage für Connected-Content, um den Endpunkt des Zertifikats von DOTS.ECO aufzurufen. Dann speichern Sie die Antwort auf das Nutzerprofil als angepasste Attribute.

**Connected-Content und Nutzer:innen Update Beispiel**  
{% raw %}
```  
{% capture post_body %} 
{  
  "remote_user_email": "{{${email_address} | default: 'braze+nadav@dots.eco'}}",  
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",  
  "impact_qty": 1,  
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",  
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"  
}  
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk  
  :method post  
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }  
  :body {{post_body}}  
  :content_type application/json  
  :save result  
%}

{  
  "attributes": [  
    {  
      "certificate_image_url": "{{result.certificate_image_url}}",  
      "certificate_url": "{{result.certificate_url}}",  
      "certificate_id": "{{result.certificate_id}}"  
    }  
  ]  
}  
```
{% endraw %}

Senden Sie die Anfrage an `https://impact.dots.eco/api/v1/certificate/add?format=sdk`.

![DOTS.ECO Nutzer:in Schritt Update.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}  
Diese Integration verwendet Connected-Content innerhalb eines Canvas-Schrittes zum **Nutzer:innen Update**, um die DOTS.ECO API aufzurufen. Testen Sie Anfragen zunächst mit einem API Client (z.B. Postman), um Ihr Token und die Nutzdaten zu validieren.  
{% endalert %}

### Schritt 3: Das Zertifikat in Nachrichten anzeigen

Wenn die Attribute des Zertifikats im Nutzerprofil gespeichert sind, können sie in nachgelagerten Canvas-Schritten für Nachrichten referenziert werden.

![DOTS.ECO Fluss.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![DOTS.ECO Schritt der Nachricht.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![DOTS.ECO Abschnitt Nachrichten verfassen.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

Zum Beispiel:  
- Zeigen Sie das Bild des Zertifikats in einer In-App-Nachricht mit {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}  
- Link zum gehosteten Zertifikat mit {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![DOTS.ECO Verhalten bei Klick auf eine Nachricht.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


Damit können Sie In-App-Nachrichten, Content-Cards oder Push-Benachrichtigungen mit Aufprallbestätigung personalisieren.

## Fehlersuche

Überprüfen Sie Connected-Content-Fehler im Braze-Dashboard unter **Einstellungen** > **Nachrichten-Aktivitätsprotokoll**.

- **Connected-Content gibt leer zurück**: Stellen Sie sicher, dass `:save result` eingestellt ist und dass Sie auf die erwarteten Antwortfelder verweisen.
- **Attribute werden im Schritt Nachricht nicht angezeigt**:
  - Stellen Sie sicher, dass die Namen der angepassten Attribute in Braze genau mit den Attributen übereinstimmen, die Sie im Schritt Benutzer-Update festgelegt haben.
  - Verwenden Sie im Schritt Nutzer:innen aktualisieren den Tab **Vorschau und Test**, um zu bestätigen, dass die Attribute ausgefüllt wurden. Senden Sie dann einen Test an einen Nutzer:innen und bestätigen Sie, dass die Attribute in seinem Nutzerprofil gespeichert sind.
- **`422` Fehler (nicht verarbeitbare Entität)**: Bestätigen Sie, dass Ihr App Token und die Anzahl der Auswirkungen gültig sind.
- **`401` Fehler**: Bestätigen Sie, dass das Token vorhanden und korrekt ist.
- **Keine Vorschau der Bilder im Schritt Nachricht**: Wählen Sie im Schritt Benutzer-Update die Option **Test an Nutzer**:in **senden** und geben Sie dann eine Vorschau der Nachricht mit demselben Nutzer:innen ein.