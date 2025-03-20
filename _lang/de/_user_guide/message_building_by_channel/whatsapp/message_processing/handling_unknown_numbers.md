---
nav_title: Umgang mit unbekannten Telefonnummern
article_title: Umgang mit unbekannten Telefonnummern
description: "In diesem Referenzartikel erfahren Sie, wie Braze mit unbekannten Telefonnummern für WhatsApp-Benutzer umgehen wird."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Umgang mit unbekannten Telefonnummern

> Möglicherweise stellen Sie fest, dass Sie, nachdem Sie WhatsApp mit Braze zum Laufen gebracht haben, Nachrichten von unbekannten Benutzern erhalten. Die folgenden Schritte beschreiben, wie ein:e nicht identifizierte:r Nutzer:in und eine Nummer verarbeitet werden.

## Opt-in/out und benutzerdefinierter Schlüsselwort-Workflow für unbekannte Nummern

Braze wird zunächst versuchen, einen Benutzer mit einer passenden Nummer zu finden. Wenn keine gefunden wird, adressiert Braze automatisch eine unbekannte Nummer auf eine von zwei Arten:

1. **Wenn ein Auslösewort mit einer [Opt-in-Leinwand]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) eingerichtet ist:**
- Braze erstellt ein anonymes Profil
- Wir weisen dem Profil einen Benutzer-Alias mit den folgenden Angaben zu:
  - Eine `alias_name` mit dem Wert der vom Benutzer angegebenen Telefonnummer
  - Eine `alias_label` mit dem Wert `phone`
- Unser System legt das Telefon-Attribut fest
- Der oder die Nutzer:in wird auf der Grundlage der Logik, die im Canvas eingerichtet ist, in die entsprechende Abonnementgruppe aufgenommen.<br><br>
2. **Wenn kein Opt-In-Canvas eingerichtet ist:**
- Braze erstellt ein anonymes Profil
- Wir weisen dem Profil einen Benutzer-Alias mit den folgenden Angaben zu:
  - Eine `alias_name` mit dem Wert der vom Benutzer angegebenen Telefonnummer
  - Eine `alias_label` mit dem Wert `phone`
- Unser System legt das Telefon-Attribut fest
- Der Abonnementstatus des Benutzers wird für alle WhatsApp-Abonnementgruppen standardmäßig auf `unsubscribed` gesetzt.<br><br>

