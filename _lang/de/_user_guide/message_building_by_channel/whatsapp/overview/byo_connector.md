---
nav_title: BYO WhatsApp Konnektor
article_title: Bring Your Own WhatsApp Konnektor
page_order: 0
description: "Dieser referenzierte Artikel beschreibt Schritt für Schritt, wie Sie einen Bring Your Own WhatsApp Konnektor einrichten, über den Braze Zugriff auf Ihren Infobip WhatsApp Business Manager:in erhält."
page_type: reference
channel:
  - WhatsApp
---

# Bring Your Own WhatsApp Konnektor

> Der Bring Your Own (BYO) WhatsApp Konnektor bietet eine Partnerschaft zwischen Braze und Infobip, bei der Sie Braze Zugriff auf Ihren Infobip WhatsApp Business Manager (WABA) geben. Dies erlaubt es Ihnen, die Kosten für Messaging direkt mit Infobip zu verwalten und zu bezahlen, während Sie Braze für die Segmentierung, Personalisierung und Orchestrierung von Kampagnen nutzen. Braze behält alle bestehenden Funktionen bei, die der WhatsApp-Kanal bietet, z. B. ausgehende Nachrichten, eingehende Nachrichten, WhatsApp-Flows und Analytics.

## Anforderungen 

| Anforderung | Beschreibung |
| --- | --- |
| Infobip-Konto | Für die Verwendung des BYO WhatsApp Konnektors ist ein Infobip-Konto erforderlich.
| Messaging-Guthaben | Sie verbrauchen Messaging-Credits von Braze, wenn Sie WhatsApp-Nachrichten versenden. |
| WhatsApp-Anforderungen | Erfüllen Sie alle [WhatsApp-Anforderungen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#prerequisites). |
| Telefonnummer | Der Einfachheit halber empfehlen wir Ihnen, [eine Telefonnummer über Infobip zu erwerben](https://www.infobip.com/docs/numbers/getting-started). |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Einrichten 

Bevor Sie den BYO WhatsApp Konnektor einrichten, vergewissern Sie sich, dass Ihr WhatsApp Business Account nicht über Infobip versendet wurde.

### Unterstützte Fälle

- WhatsApp Business Account und Telefonnummer waren noch nie mit einem Partner verbunden
- Das WhatsApp Business-Konto ist über die native Integration direkt mit Braze verbunden.
    - Folgen Sie den Schritten in [WhatsApp Telefonnummern Migration]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/), um Ihre Telefonnummern in ein neues WhatsApp Business-Konto zu migrieren, eine Telefonnummer nach der anderen.
- Das WhatsApp Business-Konto ist mit einem anderen Lösungsanbieter als Braze und Infobip verbunden
    - Folgen Sie den Schritten in [WhatsApp Telefonnummern Migration]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/), um Ihre Telefonnummern in ein neues WhatsApp Business-Konto zu migrieren, eine Telefonnummer nach der anderen.

## Schritt 1: Abrufen von Infobip-Kontoinformationen {#step-1}

1. In Infobip identifizieren Sie das Konto, das Sie mit Ihrem WhatsApp Business-Konto verwenden möchten. 
2. Gehen Sie zu **Entwickler:** in > **API-Schlüssel** und wählen Sie **API-Schlüssel erstellen**.

![Seite "API-Schlüssel erstellen" mit einem Erstellungsdatum von "16/12/2025" und einem Ablaufdatum von "16/12/36".]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3\. Geben Sie dem Schlüssel einen aussagekräftigen Namen, z. B. "Braze - My Workspace Name - My WABA Name".
4\. Fügen Sie ein weit in der Zukunft liegendes Ablaufdatum hinzu, um Probleme mit dem Ablauf des Tokens zu vermeiden.
    \- Notieren Sie sich, einen neuen API-Schlüssel zu generieren und Ihre WABA vor dem Ablaufdatum erneut zu verbinden.
5\. Wählen Sie diese Bereiche aus:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. Nachdem Sie den Schlüssel erstellt haben, kopieren Sie den API-Schlüssel.
    - Der Schlüssel kann nach der Erstellung nur für eine begrenzte Zeit kopiert werden. Sie können diese Schritte wiederholen, um einen neuen Schlüssel zu erstellen, wenn Sie in Zukunft ein anderes WhatsApp Business-Konto verbinden möchten.

!["Braze Beispiel API-Schlüssel" mit 6 hinzugefügten Geltungsbereichen.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7\. Kopieren Sie die Basis-URL der Konto-API.

!["API-Schlüssel" Seite mit einer hervorgehobenen API-Basis-URL.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## Schritt 2: Starten Sie die eingebettete Anmeldung

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** > **WhatsApp**
2. Wählen Sie den Tab **BYO Connector - Infobip** aus.

![Die WhatsApp Technologie Partnerseite.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3\. Geben Sie den API-Schlüssel und die Basis-URL aus [Schritt 1](#step-1) ein.
4\. Wählen Sie **Verbinden**.
5\. Fahren Sie mit dem [Arbeitsablauf der eingebetteten Anmeldung]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/#whatsapp-embedded-signup-workflow) unter Berücksichtigung dieser Überlegungen fort:
- Sie können nicht dasselbe Geschäftsportfolio auswählen, das von einem anderen Business Solution Provider verwendet wird.
- Sie können keine Telefonnummer auswählen, die bereits von einem anderen Anbieter von Business-Lösungen verwendet wird.
- Sie müssen eine neue WABA erstellen, nicht eine bestehende auswählen.

{% alert note %}
Um den Verifizierungscode zu erhalten, gehen Sie zu Ihrem Infobip Dashboard > **Analysieren** > **Protokolle**, und ziehen Sie den Code aus der eingehenden SMS Nachricht.  
{% endalert %}

![Nachrichtenprotokolle, die eine eingehende SMS-Nachricht mit dem Verifizierungscode zeigen.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Nach Abschluss der Einrichtung wird Ihre Rufnummer als Abo-Gruppe unter Ihrer WhatsApp Business Group aufgeführt. Die WhatsApp Business Group enthält den Namen des Infobip-Kontos und die API-Basis-URL, mit der es verbunden ist. Konten, die über die native Integration verbunden sind, haben keinen Infobip-Kontonamen.

{% alert note %}
Verbinden Sie jedes WhatsApp Business-Konto mit einem einzigen Infobip-Konto. Jedes Mal, wenn Sie eine zusätzliche Telefonnummer oder Abo-Gruppe verbinden, müssen Sie, wenn das WhatsApp Business-Konto bereits mit einem Infobip-Konto verbunden ist, die API Zugangsdaten für das bestehende Konto erneut eingeben.
{% endalert %}

## Schritt 3: Versenden von Nachrichten

Befolgen Sie den Sendeprozess der nativen Integration, einschließlich:
- [Nutzer:innen in die Abo-Gruppe einschreiben]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)
- [WhatsApp-Nachrichten erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)

## Fehlerbehebung bei der Einrichtung

### Die ID des WhatsApp Business-Kontos konnte nicht abgerufen werden

Stellen Sie sicher, dass Ihr WhatsApp Business-Konto nicht mit einem anderen Braze Workspace verbunden ist.

### Ich konnte die ID meines WhatsApp Business Accounts nicht mit Infobip teilen.

1. Stellen Sie sicher, dass Ihr WhatsApp Business-Konto nicht mit Braze oder einem anderen Partner verbunden ist.
2. Bestätigen Sie, dass keine Telefonnummern in Ihrem WhatsApp Business Account mit einem anderen Infobip-Konto verbunden sind. Bei importierten Nummern können Sie die Nummer in Infobip finden und **Nummer stornieren** auswählen.

![Der Button "Nummer stornieren" für eine Infobip-Nummer.]({% image_buster /assets/img/whatsapp/byo_connector/cancel_number.png %})

## Überlegungen 


Während alle bestehenden Funktionen von Braze unterstützt werden, werden diese Anwendungsfälle derzeit nicht unterstützt.

| Anwendungsfall | Grund |
| --- | --- |
| Verarbeitung eingehender Nachrichten in Braze und Infobip | Dies verhindert, dass Logikstränge, die von einem der beiden Systeme getriggert werden, doppelte und möglicherweise widersprüchliche Nachrichten-Threads erzeugen. |
| Versenden von Nachrichten von Braze und Infobip | Bei WhatsApp Business-Konten, die mit Braze verbunden sind, werden alle Sendungen von Braze aus versendet. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

