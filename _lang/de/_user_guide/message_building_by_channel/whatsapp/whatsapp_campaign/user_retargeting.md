---
nav_title: "Retargeting von Nutzer:innen"
article_title: "Retargeting von Nutzer:innen"
page_order: 4
description: "In diesem Referenzartikel erfahren Sie, wie Sie Ihre Nachrichten nach den WhatsApp-Interaktionen der Nutzer:innen neu ausrichten können."
page_type: reference
channel:
  - WhatsApp
---

# Retargeting von Nutzer:innen 

> Neben der Änderung des Abonnementstatus des Benutzers zeichnet Braze auch Interaktionen mit dem Benutzerprofil auf, um Nachrichten zu filtern und auszulösen.<br><br>Mit diesen Filtern und Auslösern können Sie Benutzer filtern, die WhatsApp-Nachrichten erhalten haben oder WhatsApp-Nachrichten aus einer bestimmten WhatsApp-Kampagne oder einem Canvas-Schritt erhalten haben.

## Retargeting-Optionen

{% alert note %}
Beim Aufbau von Zielgruppen mit dem Retargeting von Nutzer:innen möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, z. B. das Recht „Nicht verkaufen oder weitergeben“ gemäß dem CCPA. Vermarkter sollten die entsprechenden Filter für die Eignung von Nutzern in ihre Canvas- und/oder Kampagneneingabekriterien implementieren.
{% endalert %}

### Benutzer nach WhatsApp filtern

Benutzer können danach gefiltert werden, wann sie zuletzt eine WhatsApp erhalten haben oder ob sie eine WhatsApp von einer bestimmten WhatsApp-Kampagne erhalten haben. Filter können im Schritt Zielbenutzer des Kampagnenerstellers festgelegt werden.

**Nach zuletzt erhaltener WhatsApp filtern**<br>
![Filter für den letzten Empfang einer WhatsApp Nachricht am 22\. April 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**Filter nach empfangenen Nachrichten aus der WhatsApp-Kampagne**<br>
Filtert Benutzer, die eine Nachricht von einer bestimmten WhatsApp-Kampagne erhalten haben. Mit diesem Filter haben Sie auch die Möglichkeit, diejenigen herauszufiltern, die keine Nachrichten aus einer WhatsApp-Kampagne erhalten haben.<br>
![Filter für den Empfang einer WhatsApp Kampagne.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Nach Engagement filtern
Rufen Sie Nutzer:innen erneut auf, die eine WhatsApp-Kampagne oder einen Canvas-Schritt gelesen oder nicht gelesen haben. 

**Retargeting von Nutzer:innen, die eine bestimmte WhatsApp-Kampagne geöffnet/gelesen haben**
1. Erstellen Sie ein Segment mit dem Filter **Geklickte/geöffnete Kampagne**.
2. Wählen Sie **WhatsApp-Nachricht lesen**.
3. Wählen Sie die gewünschte Kampagne.<br>

![Filter für das Lesen einer WhatsApp Nachricht.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**Retargeting von Nutzer:innen, die einen bestimmten Canvas-Schritt geöffnet/gelesen haben**
1. Erstellen Sie ein Segment mit dem Filter **Geklickter/geöffneter Schritt**.
2. Wählen Sie **WhatsApp-Nachricht lesen**.
3. Wählen Sie den gewünschten Canvas und die Canvas-Schritte.<br>

![Filter zum Lesen eines WhatsApp-Schrittes.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**Nach Kampagne oder Canvas-Attribution filtern**<br>
Filtern Sie nach Nutzern, die eine bestimmte WhatsApp-Kampagne oder Canvas-Komponente oder -Tag geöffnet/gelesen haben.

![Filter zum Öffnen einer bestimmten WhatsApp Nachricht.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

