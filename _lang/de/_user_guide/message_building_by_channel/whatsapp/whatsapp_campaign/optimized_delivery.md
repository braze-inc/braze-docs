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

> Erhöhen Sie die Zustellbarkeit und das Engagement, indem Sie mit einer dynamischen, engagementbasierten Zustellung mehr der richtigen Nutzer:innen auf WhatsApp erreichen.

WhatsApp Nachrichten mit optimierter Zustellung werden über die [Marketing Messages API for WhatsApp](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) (MM API for WhatsApp) von Meta versendet, die eine dynamische, auf Engagement basierende Zustellung bietet. Das bedeutet, dass Ihre Nachrichten mit hohem Engagement (z.B. solche, die eher gelesen und angeklickt werden) mehr Nutzer:innen erreichen, die sich wahrscheinlich auch mit ihnen beschäftigen werden. WhatsApp geht davon aus, dass Ihre Nachrichten ein hohes Engagement aufweisen, wenn sie erwartet, relevant und zeitnah sind und daher eher gelesen und angeklickt werden. 

Marken können mit der MM API für WhatsApp die gleiche oder eine höhere Zustellbarkeit erwarten als mit der Cloud API. In Indien wurden laut Meta bei Marketing-Nachrichten mit hohem Engagement bis zu 9% mehr Nachrichten zugestellt als bei Cloud APIs. Beachten Sie, dass die MM API für WhatsApp immer noch keine 100%ige Zustellbarkeit garantiert.

### Regionale Verfügbarkeit

Die Verfügbarkeit und die Möglichkeiten der optimierten Zustellung hängen von der Region der geschäftlichen Rufnummer und dem Nutzer:innen ab. Weitere Informationen finden Sie unter [Geografische Verfügbarkeit von Features](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features). 

## Optimierte Zustellung einrichten

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** > **WhatsApp**.
2. Im Abschnitt **Optimieren Sie Ihren Versand mit optimierter Zustellung**, wählen Sie **Upgrade-Einstellung**, um den [eingebetteten Registrierungs-Workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) zu triggern.

![Der Bereich Integration von WhatsApp Nachrichten mit einer Option zur Optimierung des Versands mit optimierter Zustellung.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. Nachdem die optimierte Zustellung aktiviert wurde, wird der Status der optimierten Zustellung in Ihren Kontodetails im **WhatsApp Business Account Management** angezeigt.

![WhatsApp Business Account Management mit einer aufgelisteten Abo-Gruppe, die den Nummernstatus Aktiv hat.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

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

### Retargeting von Nutzer:innen auf anderen Braze Kanälen 

Da die MM API für WhatsApp keine 100%ige Zustellbarkeit bietet, ist es wichtig zu wissen, wie Sie Nutzer:innen, die Ihre Nachricht auf anderen Kanälen nicht erhalten haben, retargeten können. 

Für das Retargeting von Nutzern:innen empfehlen wir die Erstellung eines Segments von Nutzern:innen, die eine bestimmte Nachricht nicht erhalten haben. Filtern Sie dazu nach dem Fehlercode `131049`, der anzeigt, dass eine Nachricht mit einem Marketing Template nicht gesendet wurde, weil WhatsApp das Limit für Marketing-Templates pro Nutzer:innen nicht einhält. Sie können dies mit Braze-Currents oder SQL Segment-Erweiterungen tun:

- **Braze Currents:** Exportieren Sie Nachrichten-Fehlerereignisse mit Braze Currents. Mit diesen Daten können Sie dann ein angepasstes Attribut im Nutzerprofil (z.B. `whatsapp_failed_last_msg: true`) aktualisieren, das Sie als Filter für Ihre Retargeting-Kampagne verwenden können.
- **SQL Segment-Erweiterungen:** Wenn Sie Zugriff auf dieses Feature haben, können Sie SQL verwenden, um die Protokolle der Nachrichtenfehler abzufragen und ein Segment dieser Nutzer:innen zu erstellen und dieses Segment dann auf einem anderen Kanal zu targetieren.
