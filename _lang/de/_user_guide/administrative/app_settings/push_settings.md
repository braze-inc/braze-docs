---
nav_title: Push-Einstellungen
article_title: Push-Einstellungen
page_order: 16
page_type: reference
description: "Dieser Artikel bietet eine Übersicht über die Push-Einstellungen im Braze-Dashboard."
channel: push

---

# Push-Einstellungen

> Auf der Seite **Push-Einstellungen** können Sie die wichtigsten Einstellungen für Ihre Push-Benachrichtigungen konfigurieren, darunter die Push-Time-to-Live (TTL) und die Standard-FCM-Priorität für Android Kampagnen. Mit diesen Einstellungen können Sie die Zustellung und Effektivität Ihrer Push-Benachrichtigungen optimieren und so ein besseres Erlebnis für Ihre Nutzer:innen gewährleisten.

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

1. Gehen Sie zu **Einstellungen** > **Einstellungen verwalten** > **Push-Einstellungen**.
2. Legen Sie für jede Android-Plattform einen Standardwert für die Lebensdauer fest. Für eine genauere Kontrolle können Sie kleinere Schritte wie Stunden oder Sekunden einstellen.
3. Wählen Sie **Speichern**, um Ihre Änderungen zu übernehmen.

![Push TTL-Einstellungen für Firebase-, Internet-, Kindle- und Huawei-Geräte.]({% image_buster /assets/img/push_ttl.png %})

## Standard FCM Priorität für Android Kampagnen

Sie können die Standard Firebase Cloud Messaging (FCM) Priorität für alle Android Push-Kampagnen festlegen. Diese Priorität bestimmt, wie die Push-Benachrichtigung den Nutzer:innen zugestellt wird.

Zu den FCM-Prioritätsoptionen gehören:

| Priorität | Beschreibung | Anwendungsfall |
| --- | --- | --- |
| Normal | Standardpriorität für die Zustellung, die den Batterieverbrauch optimiert | Inhalte, die keine sofortige Aufmerksamkeit erfordern |
| Hoch | Nachrichten werden sofort versendet | Zeitkritische Benachrichtigungen, die eine schnelle Zustellung erfordern |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

So legen Sie die Standard FCM Priorität fest:

1. Gehen Sie zu **Einstellungen** > **Einstellungen verwalten** > **Push-Einstellungen**.
2. Wählen Sie im Bereich FCM-Priorität entweder "Normal" oder "Hoch" als Standardeinstellung aus.
3. Wählen Sie **Speichern**, um Ihre Änderungen zu übernehmen.

![Android-Einstellungen für die Zustellung.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Diese Einstellung gilt global für alle neuen Android Push Kampagnen, es sei denn, Sie wählen bei der Erstellung einer bestimmten Kampagne eine andere Priorität aus. 

{% alert note %}
Wenn FCM feststellt, dass Ihre App häufig Nachrichten mit hoher Priorität versendet, die nicht zu für den Nutzer sichtbaren Benachrichtigungen oder Engagement führen, können diese Nachrichten automatisch auf normale Priorität zurückgestuft werden.
{% endalert %}

Ausführlichere Informationen über FCM-Prioritätsstufen und Depriorisierung finden Sie unter [Erweiterte Einstellungen für Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#fcm-priority).

