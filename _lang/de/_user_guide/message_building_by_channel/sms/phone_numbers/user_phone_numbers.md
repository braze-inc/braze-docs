---
nav_title: "Benutzer-Telefonnummern"
article_title: SMS-Benutzer-Telefonnummern
page_order: 1
description: "Dieser Referenzartikel behandelt die Formatierung von SMS-Telefonnummern, den Import von Telefonnummern und das Hinzufügen von Benutzern zu SMS-Abonnementgruppen."
page_type: reference
channel: 
  - SMS
  
---

# Nutzertelefonnummern

> In diesem Artikel werden verschiedene Themen rund um die Telefonnummern Ihrer Nutzer oder Kunden behandelt. Wenn Sie Informationen über Ihre eigenen Nummern suchen, gehen Sie zu unserem Artikel über das [Senden von Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).

Telefonnummern werden im Nutzerprofil als String aus Ziffern angezeigt. Wenn Sie eine Zahl importieren, die keine Ziffern enthält (wie z. B. `,`, `-`, `(` oder andere), werden die nicht vorhandenen Ziffern entfernt. Wenn Sie zum Beispiel `+1 (724) 123-4567` importieren, wird dies als `17241234567` angezeigt.

## Importieren von Rufnummern

Sie können Telefonnummern importieren, indem Sie eine [CSV-Datei]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) hochladen oder über die [API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) einen Benutzer anlegen.

### Formatieren

Als Best Practice gilt, dass Telefonnummern am besten im [`E.164`](https://en.wikipedia.org/wiki/e.164)-Format importiert werden. Braze wird jedoch versuchen, jede U.S. Zahl nach bestem Wissen und Gewissen zu interpretieren oder umzurechnen.

Alle U.S.-Nummern müssen gültige, 10-stellige Telefonnummern mit einer gültigen Vorwahl sein. Sie können ohne die `+` und die Landesvorwahl eingegeben werden, da Braze alle gültigen, 10-stelligen Telefonnummern als U.S annimmt und zuordnet.

Alle internationalen Nummern beginnen mit einem `+`, gefolgt von der Landesvorwahl und der Telefonnummer. (e.g `+442071838750`)

![][Bild]{: style="max-width:50%;border: 0;"}

Um jedoch die Genauigkeit zu gewährleisten, wenn Sie in mehrere Regionen mit unterschiedlichen Länder- oder Ortsvorwahlen senden, wird empfohlen, das Format `E.164` zu verwenden, auch für Telefonnummern mit U.S.

In der folgenden Tabelle sehen Sie die Unterschiede zwischen der Formatierung lokaler Nummern und der universellen Formatierung `E.164`:

| Land | Lokal | Ländercode | `E.164` |
|---|---|---|---|
| USA | `4155552671` | (1 %) | `+14155552671` |
| Großbritannien | `2071838750` | 44 | `+442071838750` |
| Brasilien | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Hinzufügen von Benutzern zu SMS-Abonnementgruppen

Damit ein Kunde eine SMS-Nachricht erhalten kann, muss er eine gültige Telefonnummer haben und einer Abonnementgruppe angehören. Die Abonnementgruppen sind an das von Ihnen betriebene SMS-Programm gebunden (stellen Sie sicher, dass Sie die [gesetzlichen Bestimmungen für SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) einhalten und die Zustimmung jedes Kunden erfasst haben). Weitere Informationen finden Sie unter [SMS-Abonnementgruppen][1]. 

### Umgang mit ungültigen Telefonnummern

Wenn eine Telefonnummer als ungültig eingestuft wird, markiert Braze die Telefonnummer des Benutzers als ungültig und versucht nicht, weitere Mitteilungen an diese Telefonnummer zu senden. Eine ungültige Telefonnummer wird auf der **Registerkarte Engagement** eines Benutzerprofils markiert.

![][Bild2]{: style="max-width:50%;border: 0;"}

Eine Telefonnummer wird aus den folgenden Gründen als ungültig betrachtet:
- **Provider-Fehler**: Es wurde ein permanenter Fehler vom SMS-Provider empfangen. Dies bedeutet, dass die angegebene Telefonnummer falsch formatiert ist oder dauerhaft keine SMS-Nachrichten empfangen kann.
- **Deaktiviert**: Die Telefonnummer wurde deaktiviert, weil ein:e Mobilfunkteilnehmer:in seinen oder ihren Dienst beendet und seine oder ihre Nummer von seinem oder ihrem Anbieter freigegeben hat (und möglicherweise wiederverwendet und einem neuen Nutzer oder einer neuen Nutzerin zugewiesen wird).

Diese ungültigen Telefonnummern können über [SMS-Endpunkte]({{site.baseurl}}/api/endpoints/sms/) verwaltet werden. 

{% alert note %}
Wenn mehrere Benutzerprofile die gleiche Telefonnummer haben und diese Telefonnummer als ungültig markiert ist, werden alle vorhandenen Benutzerprofile mit dieser Nummer als ungültig angezeigt. Neu erstellte Benutzerprofile werden zunächst nie als ungültig markiert.
{% endalert %}

Sie können bei der [Erstellung eines Segments][2] auch Benutzer mit ungültigen Telefonnummern einschließen oder ausschließen. 

### Beschaffung und Überprüfung durch Drittanbieter

Braze verlässt sich auf Tools von Drittanbietern, um ungültige Zahlen zu ermitteln. Braze ist nicht verantwortlich für Ausfälle oder Fehlinformationen dieser Dienste. Daher sollten Sie sich nicht allein auf dieses Tool verlassen, um ungültige Nummern zu verifizieren.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[Bild]: {% image_buster /assets/img/sms/e164.png %}
[picture2]: {% image_buster /assets/img/sms/invalid_banner.png %}
