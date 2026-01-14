---
nav_title: "Push-Action-Buttons"
article_title: Push Action-Buttons
page_order: 1
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, was Push-Action-Buttons sind und worin der Unterschied zwischen iOS- und Android-Plattformen besteht."
channel:
  - Push

---

# Push-Action-Buttons

![Eine iOS Push-Benachrichtigung mit zwei Push-Action-Buttons: Akzeptieren und Ablehnen.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Mit Push-Aktionsschaltflächen können Sie Inhalte und Aktionen für Schaltflächen festlegen, wenn Sie Braze iOS- und Android-Push-Benachrichtigungen verwenden. Mit Aktionsschaltflächen können Ihre Nutzer direkt von einer Benachrichtigung aus mit Ihrer App interagieren, ohne dass sie in eine App-Erfahrung klicken müssen.

## Erstellen von Action-Buttons

Jede interaktive Schaltfläche kann zu einer Webseite oder einem Deeplink führen oder die App öffnen. 

- Für standardmäßige Push-Kampagnen können Sie Ihre Push-Action-Buttons im Abschnitt **On-Click-Verhalten** des Nachrichten-Editors im Dashboard festlegen.
- Für [schnelle Push-Kampagnen]({{site.baseurl}}/quick_push) können Aktions-Buttons für jede Plattform separat auf dem Tab **Einstellungen** konfiguriert werden.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Um Action-Buttons in Ihren iOS Push-Nachrichten zu verwenden, gehen Sie wie folgt vor:

1. Aktivieren Sie Aktions-Buttons auf dem Tab **Verfassen** für eine Standardkampagne oder auf dem Tab **Einstellungen** für einen schnellen Push.
2. Wählen Sie Ihre **iOS-Benachrichtigungskategorie** aus den folgenden verfügbaren Tastenkombinationen:
 - Zustimmen/Ablehnen
 - Ja/Nein
 - Bestätigen/Abbrechen
 - Mehr
 - Vorregistrierte benutzerdefinierte iOS-Kategorie

![iOS Benachrichtigungskategorie Dropdown-Menü.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Aufgrund der Handhabung von Schaltflächen durch iOS müssen Sie bei der Einrichtung von Push-Aktionsschaltflächen zusätzliche Integrationsschritte durchführen, die in unserer [Entwicklerdokumentation]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) beschrieben werden. Insbesondere müssen Sie entweder iOS-Kategorien konfigurieren oder aus bestimmten Standard-Schaltflächenoptionen auswählen. Bei Android-Integrationen funktionieren diese Schaltflächen automatisch.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

Um Aktionsschaltflächen in Ihren Android-Push-Nachrichten zu verwenden, gehen Sie wie folgt vor:

1. Aktivieren Sie Aktions-Buttons auf dem Tab **Verfassen** für eine Standardkampagne oder auf dem Tab **Einstellungen** für einen schnellen Push.
2. Wählen Sie <i class="fas fa-plus-circle"></i> **Schaltfläche hinzufügen** und geben Sie den Text Ihres Buttons und das **Verhalten beim Klicken** an. Sie können aus den folgenden verfügbaren Aktionen wählen:
  - App öffnen
  - Weiterleitung zu Web-URL
  - [Deeplink]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) zur Anwendung

![Auswählen von "App öffnen" als Klickverhalten für einen Benachrichtigungs-Button.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Sie können bis zu drei Tasten in Ihrem Push hinzufügen.

#### Android-Zeichenbegrenzungen

Im Gegensatz zu den iOS-Tasten, die gestapelt sind, werden die Android-Tasten nebeneinander in einer Reihe angezeigt. Das heißt, je mehr Buttons Sie hinzufügen (bis zu drei), desto weniger Platz haben Sie für die Kopie der Buttons. 

![Android Push-Action-Buttons mit verkürztem Text.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

In der folgenden Tabelle sehen Sie, wie viele Zeichen Sie hinzufügen können, bevor Ihre Button-Kopie abgeschnitten wird, je nachdem, wie viele Buttons Sie haben:

| Anzahl der Buttons | Maximale Zeichen pro Button |
| --- | --- |
| (1 %) | 46 Zeichen |
| (2 %) | 20 Zeichen |
| 3 | 11 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

