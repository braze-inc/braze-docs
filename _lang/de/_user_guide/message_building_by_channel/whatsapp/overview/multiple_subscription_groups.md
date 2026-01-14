---
nav_title: Mehrere Geschäftskonten
article_title: Mehrere WhatsApp Geschäftskonten und Telefonnummern
page_order: 2
description: "Dieser Referenzartikel beschreibt die Schritte zum Hinzufügen von WhatsApp Business-Konten und Telefonnummern."
page_type: reference
channel:
  - WhatsApp
---

# Mehrere WhatsApp Business-Konten und Telefonnummern

> Sie können mehrere WhatsApp Business-Konten und Abonnementgruppen (und Telefonnummern) zu jedem Arbeitsbereich hinzufügen. <br><br>Jede Abonnementgruppe ist mit einer einzigen Telefonnummer verbunden. Sie können also nicht dieselbe Telefonnummer mit mehreren Abonnementgruppen verbinden oder mehrere Telefonnummern mit einer Abonnementgruppe verbinden.

## Mehrere WhatsApp Business-Konten 

Mehrere WhatsApp Business-Konten sind nützlich, wenn Sie WhatsApp-Nachrichten an Benutzer in einem Braze-Arbeitsbereich senden möchten, der mehrere Marken umfasst. Das liegt daran, dass jedes Geschäftskonto innerhalb von WhatsApp separat funktioniert und seine eigene Telefonnummer, Nachrichtenvorlage und Qualitätsbewertung hat.

Geschäftskonten, die innerhalb desselben Meta Business Manager verschachtelt sind, teilen sich auch die Verwaltung der Nutzerzugriffsrechte und Kataloge (noch nicht von Braze unterstützt).

![Diagramm des Braze- und WhatsApp-Ökosystems, das zeigt, wie Workspaces und WhatsApp Business-Konten miteinander verbunden sind: Sie können eine Abo-Gruppe mit einer Telefonnummer, mehrere WhatsApp Business-Konten mit einem Workspace und einen Workspace mit mehreren Meta Business-Portfolios verbinden.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Hinzufügen eines WhatsApp Business-Kontos

Sie können bis zu 10 WhatsApp Business-Konten pro Arbeitsbereich hinzufügen. Die Geschäftskonten können in verschiedenen Meta Business Managern verschachtelt sein. Um ein Konto hinzuzufügen:

1. Gehen Sie zu **Technologie Partner** > **WhatsApp** und wählen Sie **WhatsApp Business-Konto hinzufügen**. 

![WhatsApp Messaging Integration mit Optionen zum Hinzufügen eines Geschäftskontos oder zum Hinzufügen einer Abo-Gruppe und einer Nummer.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Gehen Sie den Anmeldevorgang durch. Eine detaillierte Schritt-für-Schritt-Anleitung finden Sie unter [WhatsApp Embedded Signup]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

{% alert important %}
Ihre Telefonnummer muss alle Anforderungen an eine WhatsApp-Telefonnummer erfüllen, einschließlich der, dass sie nicht für andere WhatsApp-Konten registriert ist.
{% endalert %}

## Mehrere Abonnementgruppen und Telefonnummern

Nachrichtenvorlagen werden von allen Telefonnummern im selben WhatsApp Business-Konto gemeinsam genutzt. Einzelheiten zu WhatsApp-Abonnementgruppen finden Sie unter [Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).

Jede WhatsApp-Telefonnummer wird den Benutzern als separater WhatsApp-Chat angezeigt. Jede Telefonnummer innerhalb eines WhatsApp Business-Kontos funktioniert unabhängig voneinander, so dass sie die gleichen oder unterschiedliche Werte für die folgenden Punkte haben können: 
- Name anzeigen 
- Status 
- Bewertung der Qualität 
- Messaging-Limit 

### Hinzufügen einer Abonnementgruppe und einer Rufnummer

Sie können bis zu 20 Abonnementgruppen (und sendende Telefonnummern) pro WhatsApp Business-Konto hinzufügen. So fügen Sie eine Abonnementgruppe und eine Rufnummer hinzu:

1. Gehen Sie zu **Technologie Partner** > **WhatsApp** und wählen Sie **Abo-Gruppe und Nummer hinzufügen**.

![WhatsApp Messaging Integration mit Optionen zum Hinzufügen eines Geschäftskontos oder zum Hinzufügen einer Abo-Gruppe und einer Nummer.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Gehen Sie den Anmeldevorgang durch. <br><br> Im Schritt **Wählen Sie Ihr WhatsApp Business-Konto** wählen Sie Ihr bestehendes WhatsApp Business-Konto aus und fügen eine neue Telefonnummer hinzu. Diese Nummer muss alle Anforderungen an eine WhatsApp-Telefonnummer erfüllen, einschließlich der, dass sie nicht für andere WhatsApp-Konten registriert ist.

### Entfernen einer Abonnementgruppe und Rufnummer 

1. Gehen Sie zu **Zielgruppe** > **Abonnements** und archivieren Sie die Abonnementgruppe.
2. Gehen Sie zu Ihrem Meta Business Manager und löschen Sie die Rufnummer.
