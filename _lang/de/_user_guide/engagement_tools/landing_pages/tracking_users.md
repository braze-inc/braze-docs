---
nav_title: "Nutzer:innen tracken"
article_title: "Tracking von Nutzer:innen über ein Formular"
description: "Lernen Sie, wie Sie Nutzer:innen identifizieren können, die ein Formular über Ihre Landing Page abschicken, indem Sie Ihren Nachrichten einen Liquid-Tag hinzufügen."
page_order: 2
---

# Tracking von Nutzer:innen über ein Formular

> Lernen Sie, wie Sie Nutzer:innen verfolgen können, die ein Formular über Ihre Landing Page abschicken, indem Sie Ihren Nachrichten einen Liquid-Tag hinzufügen. Dieser Liquid-Tag wird von allen Messaging-Kanälen von Braze unterstützt, einschließlich E-Mail, SMS, In-App-Nachrichten und mehr. Weitere Informationen über Tracking-Daten finden Sie unter [Über Tracking-Daten für Landing Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data).

## Funktionsweise

Sie können einen {% raw %}`{% landing_page_url %}`{% endraw %} Liquid-Tag zu jeder Ihrer Nachrichten mit einem oder mehreren Kanälen in Braze hinzufügen. Wenn ein Nutzer:innen diese Landing Page besucht und das Formular absendet, verknüpft Braze diese Daten automatisch mit seinem bestehenden Profil, anstatt ein neues Profil für diesen Nutzer:innen zu erstellen. Im folgenden Beispiel wird ein Liquid-Tag auf der Landing Page verwendet, um Kunden:in mit einer Umfrage zu verbinden:

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
Sie können Landing Pages auch zur Lead-Generierung nutzen, indem Sie die URL der Seite in Ihre externen Kanäle einbetten. Nachdem Sie eine Landing Page erstellt haben, gehen Sie zu **Landing Page Details**, um die eindeutige URL für Ihre Landing Page zu erhalten.
{% endalert %}

## Landing Page Liquid-Tags verwenden

### Voraussetzungen

Bevor Sie beginnen, müssen Sie eine [Landing Page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) und eine [Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/) erstellen.

### Schritt 1: Überprüfen Sie die URL der Seite {#page-url}

Braze verwendet die URL Ihrer Landing Page, um seinen eindeutigen Liquid-Tag zu generieren. Wenn Sie die URL der aktuellen Seite ändern möchten, gehen Sie zu **Messaging** > **Landing Pages** und öffnen Sie dann Ihre Landing Page. Unter **Seiten-URL** können Sie eine neue Seiten-URL eingeben.

{% alert warning %}
Wenn Sie die URL der Seite nach dem Versenden Ihrer Nachricht ändern, wird jeder Nutzer:innen, der versucht, Ihre Landing Page mit der alten URL zu besuchen, auf die Seite `404` weitergeleitet.
{% endalert %}

![Eine Beispielseiten-URL für eine Landing Page in Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Schritt 2: Erzeugen Sie den Liquid-Tag

Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie dann eine Kampagne aus. Wählen Sie in Ihrem Nachrichten-Editor die **Personalisierung** aus.

![Der Button 'Personalisierung hinzufügen' im Drag-and-Drop-Editor.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze generiert automatisch einen Liquid-Tag mit der [URL Ihrer Landing Page](#page-url). Beziehen Sie sich auf die folgende Tabelle, um Ihren Tag zu erstellen:

\|**Art der** Personalisierung| Wählen Sie **Landing Page**.|
\|**Wählen Sie** die Landing Page, [die Sie zuvor erstellt haben](#prerequisites).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Um den Liquid-Tag zu Ihrer Nachricht hinzuzufügen, können Sie entweder **Einfügen** auswählen oder das Snippet in die Zwischenablage kopieren und es manuell hinzufügen.

![Ein automatisch generierter Liquid-Tag für die ausgewählte Landing Page.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Ihr Snippet wird in etwa so aussehen wie das folgende:

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### Schritt 3: Nachricht fertigstellen und versenden

Betten Sie das Snippet von Liquid in Ihre Nachricht ein und stellen Sie dann den Rest Ihrer Nachricht fertig. Zum Beispiel:

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

Wenn Sie bereit sind, können Sie die Nachricht senden, um das Tracking der Nutzer:innen auf Ihrer Landing Page zu starten.
