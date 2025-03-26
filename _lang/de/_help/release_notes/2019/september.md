---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2019."
---

# September 2019

## Braze-App in OneLogin

Kunden können innerhalb von [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) einfach nach Braze suchen und Braze für die SP- oder IdP-initiierte Anmeldung auswählen. Das bedeutet, dass Kunden keine benutzerdefinierte Anwendung in OneLogin hinzufügen müssen. Dies sollte dazu führen, dass bestimmte Einstellungen wie Attribute, die seit der Einführung von SAML SSO auftauchen, vorausgefüllt werden.

## Rokt Kalender Partnerschaft

[Rokt Calendar]({{site.baseurl}}/partners/additional_channels/calendar/rokt_calendar/) bietet Braze-Kunden die Möglichkeit, ihre personalisierten Marketinginitiativen aufeinander abzustimmen und personalisierte Inhalte auf den Kalender des Endbenutzers auszuweiten. Dadurch wird das Erlebnis für den Endbenutzer noch nahtloser und die Bindung an die Dienste unserer Kunden wird noch stärker. Kunden werden in der Lage sein...

- Senden Sie eine Kalendereinladung über die Braze-Plattform, um das Datum zu speichern und unsere Kommunikation zu erweitern.
- Aktualisieren Sie eine bestehende Einladung, wenn sich der Inhalt der Veranstaltung geändert hat.

## Passkit Partnerschaft

Mit [Passkit]({{site.baseurl}}/partners/additional_channels/mobile_wallet/passkit/) können Braze-Kunden ihr Kundenengagement auf mobile Geldbörsen ausweiten. Sie werden in der Lage sein, personalisierte Wallet-Kampagnen zu erstellen und dabei die leistungsstarke Segmentierung von Braze zu nutzen und neben Kanälen wie Push-, In-App-Nachrichten und mehr zu orchestrieren.

## Rückgabe der Versand-ID über Messaging-Endpunkte

Die `dispatch_id` einer Nachricht wird in den folgenden Antworten des Messaging-Endpunkts enthalten sein:
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

Auf diese Weise können Kunden, die Transaktionsnachrichten verwenden, den Anruf über Currents zurückverfolgen.

## Canvas Änderungsprotokolle

Haben Sie sich schon einmal Gedanken darüber gemacht, wer in Ihrem Konto an einem Canvas arbeitet? Wundern Sie sich nicht mehr! Sie können jetzt auf Canvas-Changelogs zugreifen.

![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog1.png %})
![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog2.png %})
