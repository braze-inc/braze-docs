---
nav_title: "Nutzertelefonnummern"
article_title: WhatsApp Benutzer-Telefonnummern
page_order: 1.5
description: "Dieser Referenzartikel behandelt die Formatierung von WhatsApp-Telefonnummern, den Import von Telefonnummern sowie das Hinzufügen von Benutzern zu WhatsApp-Abonnementgruppen."
page_type: reference
channel: 
  - WhatsApp
  
---

# Nutzertelefonnummern

> In diesem Artikel werden verschiedene Themen rund um die Telefonnummern Ihrer Nutzer oder Kunden behandelt.

Telefonnummern werden im Benutzerprofil in lokalen Formaten angezeigt, aber nicht in dem Format, das Sie zum Importieren der Nummer verwenden (`(724) 123 4567`).

## Importieren von Telefonnummern

Sie können Telefonnummern importieren, indem Sie eine [CSV-Datei hochladen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) oder [über API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) eine:n Nutzer:in anlegen.

### Formatieren

Es ist wichtig, dass Sie Nicht-U.S.-Nummern im [`E.164`](https://en.wikipedia.org/wiki/e.164)-Format importieren,einschließlich des „+“-Zeichens und der Landesvorwahl. Alle Telefonnummern, die nicht in diesem Format angegeben werden, werden als US-Nummern interpretiert.  

Wenn eine Telefonnummer in das Format E.164 gezwungen wird, aber die Validierung nicht besteht, kann Braze keine WhatsApp-Nachrichten an diese Nummer senden. Alle Nutzer:innen mit Telefonnummern, die nicht formatierbar sind, werden automatisch aus einem Canvas-Schritt, der WhatsApp einschließt, ausgeschlossen.

Alle U.S.-Nummern müssen gültige, 10-stellige Telefonnummern mit einer gültigen Vorwahl sein. Sie können ohne die `+` und die Landesvorwahl eingegeben werden, da Braze alle gültigen, 10-stelligen Telefonnummern als U.S annimmt und zuordnet.

Alle internationalen Nummern beginnen mit einem `+`, gefolgt von der Landesvorwahl und der Telefonnummer. (e.g `+442071838750`)

\![]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Um jedoch die Genauigkeit zu gewährleisten, wenn Sie in mehrere Regionen mit unterschiedlichen Länder- oder Ortsvorwahlen senden, wird empfohlen, das Format `E.164` zu verwenden, auch für Telefonnummern mit U.S.

In der folgenden Tabelle sehen Sie die Unterschiede zwischen der Formatierung lokaler Nummern und der universellen Formatierung `E.164`:

| Land | Lokal | Ländercode | `E.164` |
|---|---|---|---|
| USA | `4155552671` | (1 %) | `+14155552671` |
| Großbritannien | `02071838750` | 44 | `+442071838750` |
| Brasilien | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Hinzufügen von Benutzern zu einer WhatsApp-Abonnementgruppe

Damit ein Kunde eine WhatsApp-Nachricht erhalten kann, muss er über eine gültige Telefonnummer verfügen und einer Abonnementgruppe angehören. Weitere Informationen finden Sie unter [WhatsApp-Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).


### Mehrere Benutzer mit der gleichen Rufnummer

Wenn mehrere Benutzer innerhalb eines Segments einer einzelnen Kampagne oder eines Canvas-Schrittes dieselbe Telefonnummer haben, wird Braze den Versand deduplizieren und nur eine Nachricht an diese eine Telefonnummer senden. 


