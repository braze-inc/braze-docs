---
nav_title: WhatsApp Nachrichten mit optimierter Zustellung
article_title: WhatsApp Nachrichten mit optimierter Zustellung
page_order: 1
description: "Dieser Artikel referenziert die Schritte, die zum Aufbau und zur Erstellung einer WhatsApp Nachricht mit optimierter Zustellung gehören."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# WhatsApp Nachrichten mit optimierter Zustellung

> Nutzen Sie die fortschrittlichen KI-Systeme von Meta, um Ihre Marketing Nachrichten an mehr Nutzer:innen zuzustellen, die am ehesten bereit sind, sich mit ihnen zu beschäftigen, und so die Zustellbarkeit und das Engagement für Ihre Nachrichten deutlich zu erhöhen.

WhatsApp Nachrichten mit optimierter Zustellung werden über die neue [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) von Meta versendet, die im Vergleich zur herkömmlichen Cloud API eine bessere Performance bietet. Mit dieser neuen Sendepipeline können Sie Nutzer:innen besser erreichen, die Ihre Nachrichten wertschätzen und empfangen möchten.

Zu den Vorteilen einer optimierten Zustellung gehören:

- **Dynamische Grenzen für Messaging:** Die neue API bietet dynamischere Grenzen für das Messaging pro Benutzer, so dass Marketing-Nachrichten mit hohem Engagement (die eher gelesen oder angeklickt werden) mehr Nutzer:innen erreichen können.
- **Optimierte Zustellbarkeit:** Sie können mit niedrigeren Zustellungs-Raten, aber höheren Engagement-Raten für die zugestellten Nachrichten rechnen, da die fortschrittliche KI von Meta für Nutzer:innen optimiert wird, von denen sie erwartet, dass sie die Nachricht wertschätzen und sich mit ihr beschäftigen. 
- **Bewährte Ergebnisse:** In Indien wurden bei Nachrichten, die als eher lesbar oder klickbar identifiziert wurden, bis zu 9 % mehr Nachrichten zugestellt als beim Versand über die Cloud API.
- **Gezielte Zustellung:** Metas fortschrittliche KI identifiziert Nachrichten mit hohem Engagement und bringt sie mehr Nutzern zugestellt, was es Ihnen erlaubt, die richtige Nachricht an mehr Nutzer:innen zu übermitteln.

### Regionale Verfügbarkeit

Die Verfügbarkeit und die Möglichkeiten der optimierten Zustellung hängen von der Region der geschäftlichen Rufnummer und dem Nutzer:innen ab. Weitere Informationen finden Sie unter [Geografische Verfügbarkeit von Features](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features). 

## Optimierte Zustellung einrichten

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** > **WhatsApp**.
2. Im Abschnitt **Optimieren Sie Ihren Versand mit optimierter Zustellung**, wählen Sie **Upgrade-Einstellung**, um den [eingebetteten Registrierungs-Workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) zu triggern.

![Der Bereich Integration von WhatsApp Nachrichten mit einer Option zur Optimierung des Versands mit optimierter Zustellung.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. Nachdem die optimierte Zustellung aktiviert wurde, wird der Status der optimierten Zustellung in Ihren Kontodetails im **WhatsApp Business Account Management** angezeigt.

![WhatsApp Business Account Management Abschnitt mit einer aufgelisteten Abo-Gruppe, die den Status Aktiv hat.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Alternativ können Sie die optimierte Zustellung auch direkt in Ihrem WhatsApp Manager aktivieren und dann mit dem Senden in Braze beginnen.

### Fehlerbehebung bei der Einrichtung

- **Allgemeiner Fehler:** Wenn während des Upgrades etwas schief geht, wird dieser Fehlerbanner angezeigt und Sie werden aufgefordert, [den Support zu kontaktieren]({{site.baseurl}}/braze_support/).
- **Unzulässiger Fehler:** Wenn Sie durch Meta eingeschränkt sind, wird dieser Fehlerbanner angezeigt: "Mindestens ein WhatsApp Business-Konto wird von Meta eingeschränkt. Um upgraden zu können, müssen die Konten in gutem Zustand sein." Das kann nicht abgetan werden, bevor das Problem nicht gelöst ist.

## Optimierte Zustellung in Kampagnen und Canvase verwenden

Die optimierte Zustellung sollte für **Marketing Nachrichten** verwendet werden. Braze entfernt automatisch die Option der optimierten Zustellung für **Utility-, Authentifizierungs-, Dienst- und Antwortnachrichten**, die weiterhin über die Cloud API gesendet werden sollten, was die Standardeinstellung ist. 

### Auswählen der Zustellungsart

1. Gehen Sie im Braze WhatsApp-Editor für eine Kampagne oder einen Canvas-Schritt auf den Tab **Einstellungen**.
2. Im Abschnitt **Zustellungsmethode** ist das Kontrollkästchen für **Optimierte Zustellung (empfohlen)** standardmäßig aktiviert, wenn Ihr WhatsApp Business Account (WABA) aktiviert ist. Wenn Sie die optimierte Zustellung für diese spezielle Nachricht nicht verwenden möchten, deaktivieren Sie das Kontrollkästchen.
- Wenn Sie die optimierte Zustellung auswählen, diese aber nicht verfügbar ist, wird die Nachricht automatisch auf die Methode der Cloud API zurückgreifen.

![Nachrichten-Editor mit einem Tab für die Vorschau, der ein Kontrollkästchen zum Auswählen der optimierten Zustellung enthält.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})