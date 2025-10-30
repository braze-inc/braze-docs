---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Max verstärkt Android-Push-Benachrichtigungen, indem es fehlgeschlagene Push-Benachrichtigungen verfolgt und die Push-Benachrichtigung erneut sendet, wenn es wahrscheinlicher ist, dass der Benutzer sie erhält."

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Erfahren Sie mehr über Push Max und wie Sie diese Funktion nutzen können, um die Zustellbarkeit von Android-Push-Benachrichtigungen an [chinesische OEM-Geräte]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/) potenziell zu verbessern.

## Was ist Push Max?

Push Max verstärkt Android-Push-Benachrichtigungen, indem es fehlgeschlagene Push-Benachrichtigungen verfolgt und die Push-Benachrichtigung erneut sendet, wenn es wahrscheinlicher ist, dass der Benutzer sie erhält.

Einige Android-Geräte chinesischer Originalhersteller (OEMs) wie Xiaomi, OPPO und Vivo verwenden ein robustes Akku-Optimierungssystem, um die Akkulaufzeit zu verlängern. Dieses Verhalten kann die unbeabsichtigte Folge haben, dass die Verarbeitung von Apps im Hintergrund abgeschaltet wird, wodurch die Zustellbarkeit von Push-Benachrichtigungen auf diesen Geräten verringert wird, wenn sich die App nicht im Vordergrund befindet. Dieser Umstand tritt am häufigsten in den asiatisch-pazifischen Märkten (APAC) auf.

## Verfügbarkeit

- Nur für Android-Push-Benachrichtigungen verfügbar
- Nicht unterstützt für aktionsbasierte oder API-ausgelöste Nachrichten
- Nicht unterstützt, wenn die Option, [nur an das zuletzt verwendete Gerät des Benutzers zu senden]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options), ausgewählt ist

## Voraussetzungen

Push-Benachrichtigungen, die mit Push Max gesendet werden, werden nur Geräten zugestellt, die mindestens über die folgende [SDK-Version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) verfügen:

{% sdk_min_versions android:29.0.1 %}

## Push Max verwenden

{% tabs %}
{% tab Campaigns %}

So verwenden Sie Push Max in Ihrer Kampagne:

1. Erstellen Sie eine Push-Kampagne.
2. Wählen Sie **Android Push** als Ihre Plattform.
3. Gehen Sie zum Schritt **Lieferung planen**.
4. Wählen Sie **Senden mit Push Max**.

\![Android Push Zustellbarkeit im Schritt Zustellung planen mit der Option "Mit Push Max senden".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

So verwenden Sie Push Max in Ihrem Canvas:

1. Fügen Sie einen Nachrichtenschritt zu Ihrem Canvas hinzu.
2. Wählen Sie **Android Push** als Ihre Plattform.
3. Gehen Sie auf die Registerkarte **Zustellungseinstellungen**.
4. Wählen Sie **Senden mit Push Max**.

\![Tab Zustellungseinstellungen eines Android Push Message Schrittes mit der Option "Senden mit Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Die folgenden beiden Features, Intelligentes Timing und Time-to-Live, können zusammen mit Push Max verwendet werden, um die Zustellbarkeit Ihrer Android Push-Benachrichtigungen zu erhöhen.

### Intelligentes Timing

Push Max funktioniert am besten, wenn [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) eingeschaltet ist. Intelligent Timing kann die Push-Benachrichtigung zu einem Zeitpunkt berechnen und versenden, zu dem der Benutzer die App am wahrscheinlichsten nutzt und die Push-Benachrichtigung am wahrscheinlichsten zugestellt wird.

### Lebenszeit (TTL)

Time-to-Live (TTL) kann fehlgeschlagene Push-Benachrichtigungen an Firebase Cloud Messaging (FCM) tracken und die Benachrichtigung erneut versuchen, wenn die:der Nutzer:in sie wahrscheinlich erhalten wird.

Standardmäßig ist Time to Live auf 28 Tage eingestellt, das ist das Maximum. Sie können die Standard TTL für alle neuen Android Push-Nachrichten unter **Einstellungen** > **Workspace-Einstellungen** > **Push-Einstellungen** verringern, oder Sie können die Anzahl der Tage pro Nachricht auf dem Tab **Einstellungen** konfigurieren, wenn Sie eine Android Push-Benachrichtigung verfassen.

\![Time to Live-Feld auf 28 Tage eingestellt.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Was Sie wissen sollten

### Aktionscodes

Wir empfehlen Ihnen, keine [Braze-Promotionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) in Nachrichten zu verwenden, in denen Push Max aktiviert ist.

Das liegt daran, dass Aktionscodes einzigartig sind. Wenn eine Push-Benachrichtigung, die einen Aktionscode enthält, nicht zugestellt werden kann, wird beim erneuten Senden dieser Benachrichtigung dank Push Max ein neuer Aktionscode gesendet. Dies kann dazu führen, dass Sie Promotion-Codes schneller als erwartet verbrauchen.

### Eigenschaften von Canvas-Ereignissen und Einträgen

Push Max funktioniert möglicherweise nicht wie erwartet, wenn Sie Liquid-Referenzen auf [Canvas-Entry-Eigenschaften oder Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) in Ihre Nachricht aufnehmen. Das liegt daran, dass die Entry- und Event-Eigenschaften nicht verfügbar sind, wenn Push Max versucht, die Nachricht erneut zu senden.
