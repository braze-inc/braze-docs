---
nav_title: "Push Action-Buttons"
article_title: Push Action-Buttons
page_order: 1
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, was Push-Action-Buttons sind und worin der Unterschied zwischen iOS- und Android-Plattformen besteht."
channel:
  - Push

---

# Push-Action-Buttons

![Eine iOS-Push-Benachrichtigung mit zwei Schaltflächen für Push-Aktionen: Akzeptieren und Ablehnen.][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Mit Push-Aktionsschaltflächen können Sie Inhalte und Aktionen für Schaltflächen festlegen, wenn Sie Braze iOS- und Android-Push-Benachrichtigungen verwenden. Mit Aktionsschaltflächen können Ihre Nutzer direkt von einer Benachrichtigung aus mit Ihrer App interagieren, ohne dass sie in eine App-Erfahrung klicken müssen.

## Erstellen von Action-Buttons

Jede interaktive Schaltfläche kann zu einer Webseite oder einem Deeplink führen oder die App öffnen. Sie können Ihre Push-Aktionsschaltflächen im Abschnitt **On-Click Behavior** des Push Message Composers im Dashboard festlegen.

{% alert important %}
Wenn Sie sowohl iOS als auch Android in einer einzigen Kampagne ansprechen möchten, erstellen Sie eine Multichannel-Kampagne. Push-Action-Buttons werden beim Targeting von [Quick-Push-Kampagnen]({{site.baseurl}}/quick_push) sowohl für iOS als auch für Android nicht unterstützt.
{% endalert %}

### iOS {#ios}

Um Action-Buttons in Ihren iOS Push-Nachrichten zu verwenden, gehen Sie wie folgt vor:

1. Erstellen Sie eine [iOS-Push-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) und aktivieren Sie Aktionsschaltflächen auf der Registerkarte **Verfassen**.
2. Wählen Sie Ihre **iOS-Benachrichtigungskategorie** aus den folgenden verfügbaren Tastenkombinationen:
 - Zustimmen/Ablehnen
 - Ja/Nein
 - Bestätigen/Abbrechen
 - Mehr
 - Vorregistrierte benutzerdefinierte iOS-Kategorie

![Dropdown-Menü der iOS-Benachrichtigungskategorie.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Aufgrund der Handhabung von Schaltflächen durch iOS müssen Sie bei der Einrichtung von Push-Aktionsschaltflächen zusätzliche Integrationsschritte durchführen, die in unserer [Entwicklerdokumentation]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) beschrieben werden. Insbesondere müssen Sie entweder iOS-Kategorien konfigurieren oder aus bestimmten Standard-Schaltflächenoptionen auswählen. Bei Android-Integrationen funktionieren diese Schaltflächen automatisch.
{% endalert %}

### Android {#android}

Um Aktionsschaltflächen in Ihren Android-Push-Nachrichten zu verwenden, gehen Sie wie folgt vor:

1. Erstellen Sie eine [Android-Push-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) und aktivieren Sie Benachrichtigungsschaltflächen auf der Registerkarte **Verfassen**.
2. Wählen Sie <i class="fas fa-plus-circle"></i> **Schaltfläche hinzufügen** und geben Sie den Text Ihres Buttons und das **Verhalten beim Klicken** an. Sie können aus den folgenden verfügbaren Aktionen wählen:
  - App öffnen
  - Weiterleitung zu Web-URL
  - [Deeplink]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) zur Anwendung

![Auswählen von "App öffnen" als Klickverhalten für einen Benachrichtigungs-Button.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Sie können bis zu drei Tasten in Ihrem Push hinzufügen.

#### Android-Zeichenbegrenzungen

Im Gegensatz zu den iOS-Tasten, die gestapelt sind, werden die Android-Tasten nebeneinander in einer Reihe angezeigt. Das heißt, je mehr Buttons Sie hinzufügen (bis zu drei), desto weniger Platz haben Sie für die Kopie der Buttons. 

![Push-Action-Buttons für Android mit abgeschnittenem Text.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

In der folgenden Tabelle sehen Sie, wie viele Zeichen Sie hinzufügen können, bevor Ihre Button-Kopie abgeschnitten wird, je nachdem, wie viele Buttons Sie haben:

| Anzahl der Buttons | Maximale Zeichen pro Button |
| --- | --- |
| (1 %) | 46 Zeichen |
| (2 %) | 20 Zeichen |
| 3 | 11 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


[1]: {% image_buster /assets/img_archive/push_action_example.png %}
