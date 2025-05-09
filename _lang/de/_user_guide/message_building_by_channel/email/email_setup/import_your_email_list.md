---
nav_title: Importieren Ihrer E-Mail-Liste
article_title: Importieren Ihrer E-Mail-Liste in Braze
page_order: 4
page_type: reference
description: "In diesem Referenzartikel erfahren Sie bewährte Praktiken zum Importieren Ihrer E-Mail-Liste in Braze."
channel: email

---

# Importieren Ihrer E-Mail-Liste in Braze {#importing-email-lists}

> Ein wichtiger Schritt, um ein erfolgreicher E-Mail Sender zu werden, ist die Sicherstellung einer hochwertigen E-Mail-Liste. Die richtige Verwaltung von E-Mail-Listen kann Ihre Zustellbarkeit verbessern und Ihnen präzisere und saubere Kampagnenergebnisse liefern.

## Überlegungen vor dem Importieren

{% multi_lang_include email-via-sms-warning.md %}

### Validieren Sie Ihre E-Mail-Listen

Bevor Sie Ihre E-Mail-Liste in Braze importieren, vergewissern Sie sich, dass Ihre Liste nur echte E-Mail-Adressen enthält. Eine hohe Absprungrate kann Ihrer E-Mail-Absender-Reputation schaden. 

E-Mail-Listenbereinigungsdienste können dies für Sie tun, indem sie feststellen, ob die E-Mail-Adresse der korrekten Syntax folgt und die physischen Eigenschaften einer E-Mail-Adresse aufweist, die E-Mail-Domäne überprüfen und eine Verbindung zum E-Mail-Server herstellen, um zu authentifizieren, ob die E-Mail-Adresse dort existiert.

### Identifizieren Sie Ihre engagierten Nutzer:innen

Um Ihre am stärksten engagierten Nutzer:innen zu identifizieren, entfernen Sie zunächst die Nutzer:innen, die sich am meisten zurückgezogen haben. Es empfiehlt sich, keine E-Mails an Benutzer zu senden, die seit mehr als sechs Monaten nicht mehr auf eine E-Mail reagiert haben, da dies dem Ruf Ihres E-Mail-Versenders schaden kann. Achten Sie beim Import Ihrer E-Mail-Liste darauf, dass Sie nur Nutzer:innen aufnehmen, die in den letzten sechs Monaten eine E-Mail von Ihnen geöffnet haben.

Langfristig sollten Sie auch die Einführung einer [Sunsetting-Richtlinie][60] in Betracht ziehen.

### Vermeiden Sie Unterdrückungslisten

Wenn Sie von einem bestehenden E-Mail-Anbieter wechseln, stellen Sie sicher, dass Sie keine Nutzer:innen aus einer Unterdrückungsliste importieren. Die Unterdrückungslisten bieten Features für E-Mail-Adressen, die sich entweder abgemeldet haben, Ihre Mails als Spam markiert haben oder zu Rückläufern (Hard Bounce) führen.

## Methoden zum Importieren

Sobald Sie Ihre E-Mail-Liste vorbereitet haben, gibt es mehrere Möglichkeiten, Nutzer:innen in Braze zu importieren, z. B. über die Braze REST API oder CSV-Dateien. Lesen Sie mehr in unserem Artikel über den [Benutzerimport]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

[60]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/
