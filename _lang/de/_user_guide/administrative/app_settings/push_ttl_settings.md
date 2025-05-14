---
nav_title: Push TTL-Einstellungen
article_title: Push TTL-Einstellungen
page_order: 16
page_type: reference
description: "Dieser Referenzartikel behandelt die Einstellungsseite \"Push-Time-to-Live\" im Braze-Dashboard."
channel: push

---

# Push TTL Einstellungen

> Erfahren Sie mehr über die Einstellungsseite Push-Time-to-Live im Braze-Dashboard.

## Was ist Push TTL?

Die Push-Time-to-Live (TTL) steuert, wie lange Braze versucht, eine Push-Benachrichtigung an Geräte zuzustellen, die zum Zeitpunkt der Versendung der Kampagne offline sind. Wenn ein Gerät die Verbindung nach Ablauf der TTL wieder aufnimmt, wird die Nachricht nicht zugestellt. Mit dieser Einstellung wird eine Push-Benachrichtigung nicht entfernt, wenn sie bereits auf dem Gerät des Nutzers:innen eingegangen ist. Sie steuert nur, wie lange der Push-Anbieter versucht, eine Benachrichtigung zuzustellen.

## Einstellung der Standard Push TTL Werte

Standardmäßig setzt Braze die Push TTL für jeden Push Messaging Dienst auf das Maximum. 

| Push Messaging Dienst | Maximum TTL |
| --- | --- |
| Internet (über FCM- oder Web-Push-Dienste) | 28 Tage |
| Firebase Cloud Messaging (FCM) | 28 Tage |
| Kindle (ADM) | 31 Tage |
| Huawei (HMS) | 15 Tage |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Diese Einstellungen gelten global für alle Push-Kampagnen, es sei denn, für eine bestimmte Nachricht wurde eine andere TTL festgelegt. Um die TTL einer Nachricht anzupassen, siehe [Erweiterte Kampagnen-Einstellungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl).

Um einen anderen Standard einzustellen Push TTL:

1. Gehen Sie zu **Einstellungen** > **Einstellungen verwalten** > **Push TTL Einstellungen**.
2. Legen Sie für jede Android-Plattform einen Standardwert für die Lebensdauer fest. Für eine genauere Kontrolle können Sie kleinere Schritte wie Stunden oder Sekunden einstellen.
3. Wählen Sie **Speichern**, um Ihre Änderungen zu übernehmen.

![Schieben Sie Zeit auf die Registerkarte Live-Einstellungen unter Einstellungen verwalten][1]


[1]: {% image_buster /assets/img/push_ttl.png %}
