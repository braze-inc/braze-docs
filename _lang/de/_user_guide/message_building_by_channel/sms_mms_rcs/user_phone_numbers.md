---
nav_title: "Nutzertelefonnummern"
article_title: SMS-Benutzer-Telefonnummern
page_order: 7
description: "Dieser Referenzartikel behandelt die Formatierung von SMS-Telefonnummern, den Import von Telefonnummern und das Hinzufügen von Benutzern zu SMS-Abonnementgruppen."
page_type: reference
alias: /user_phone_numbers/
channel: 
  - SMS
  - MMS
  - RCS
---

# Nutzertelefonnummern

> In diesem Artikel werden verschiedene Themen rund um die Telefonnummern Ihrer Nutzer oder Kunden behandelt. Wenn Sie Informationen über Ihre eigenen Nummern suchen, gehen Sie zu unserem Artikel über das [Senden von Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Empfohlenes Format

Wir empfehlen den Import von Telefonnummern im [`E.164`](https://en.wikipedia.org/wiki/e.164) Format zu importieren, um die Genauigkeit zu gewährleisten, falls Sie in mehrere Regionen mit unterschiedlichen Länder- oder Ortsvorwahlen senden - auch bei U.S...-basierten Telefonnummern.

- **U.S. Zahlen:** Alle U.S.-Nummern müssen gültige, 10-stellige Telefonnummern mit einer gültigen Vorwahl sein. Wenn bei einer 10-stelligen Telefonnummer der Code `+` und die Landesvorwahl fehlen, bildet Braze sie als U.S ab.
- **Internationale Nummern:** Alle internationalen Nummern beginnen mit einem `+`, gefolgt von der Landesvorwahl und dann der Telefonnummer. Zum Beispiel: `+442071838750`.

![Beispiel für eine gültige e164 internationale Rufnummer.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Hier ein paar Beispiele für die Unterschiede zwischen Lokalisierung und `E.164` Formatierung:

| Land | Lokal | Ländercode | `E.164` |
|---|---|---|---|
| USA | `4155552671` | (1 %) | `+14155552671` |
| Großbritannien | `2071838750` | 44 | `+442071838750` |
| Brasilien | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

## Importieren von Rufnummern

Wenn Sie Telefonnummern importieren, ist es wichtig, dass Sie das [empfohlene Format](#recommended-format) einhalten. Um Telefonnummern zu importieren, verwenden Sie eine der folgenden Methoden:

- [Hochladen einer CSV-Datei nach Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)
- [Verwendung des Endpunkts `/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
Nutzer:innen-Telefonnummern werden in Braze als String aus Ziffern angezeigt. Wenn Sie eine Zahl importieren, die keine Ziffern enthält (wie z.B. `,`, `-`, `(`, oder andere), werden die Nicht-Ziffern beim Rendern in Braze entfernt. Wenn Sie zum Beispiel `+1 (724) 123-4567` importieren, wird dies als `17241234567` angezeigt.
{% endalert %}

## Umgang mit ungültigen Telefonnummern

Wenn eine Telefonnummer als ungültig eingestuft wird, markiert Braze die Telefonnummer des Benutzers als ungültig und versucht nicht, weitere Mitteilungen an diese Telefonnummer zu senden. Eine ungültige Telefonnummer wird auf der **Registerkarte Engagement** eines Benutzerprofils markiert.

![Beispiel einer Fehlermeldung für ungültige Telefonnummern in Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

Eine Telefonnummer wird aus den folgenden Gründen als ungültig betrachtet:

- **Provider-Fehler**: Es wurde ein permanenter Fehler vom SMS- und RCS-Provider empfangen. Dies bedeutet, dass die angegebene Telefonnummer falsch formatiert ist oder dauerhaft keine SMS- oder RCS-Nachrichten empfangen kann.
- **Deaktiviert**: Die Telefonnummer wurde deaktiviert, weil ein:e Mobilfunkteilnehmer:in seinen oder ihren Dienst beendet und seine oder ihre Nummer von seinem oder ihrem Anbieter freigegeben hat (und möglicherweise wiederverwendet und einem neuen Nutzer oder einer neuen Nutzerin zugewiesen wird).

Diese ungültigen Telefonnummern können über [SMS- und RCS-Endpunkte]({{site.baseurl}}/api/endpoints/sms/) verwaltet werden. 

{% alert note %}
Wenn mehrere Benutzerprofile die gleiche Telefonnummer haben und diese Telefonnummer als ungültig markiert ist, werden alle vorhandenen Benutzerprofile mit dieser Nummer als ungültig angezeigt. Neu erstellte Benutzerprofile werden zunächst nie als ungültig markiert.
{% endalert %}

Sie können bei der [Erstellung eines Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment) auch Benutzer mit ungültigen Telefonnummern einschließen oder ausschließen.

## Hinzufügen von Nutzer:innen zu SMS und RCS Abo-Gruppen

Damit ein Nutzer:innen eine SMS oder RCS Nachricht erhalten kann, muss er eine gültige Telefonnummer haben und in einer Abo-Gruppe opt-in sein. Abo-Gruppen sind an das SMS- oder RCS-Programm gebunden, das Sie betreiben (stellen Sie sicher, dass Sie die [gesetzlichen Bestimmungen für SMS, MMS und RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) einhalten und die Zustimmung für jede Kund:in erfasst haben). Weitere Informationen finden Sie unter [Abo-Gruppen für SMS und RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

## Beschaffung und Überprüfung durch Drittanbieter

Braze verlässt sich auf Tools von Drittanbietern, um ungültige Zahlen zu ermitteln. Braze ist nicht verantwortlich für Ausfälle oder Fehlinformationen dieser Dienste. Daher sollten Sie sich nicht allein auf dieses Tool verlassen, um ungültige Nummern zu verifizieren.
