---
nav_title: Nutzer-Retargeting
article_title: "Retargeting von Nutzer:innen über eine Landing Page"
description: "Lernangebote für das Retargeting von Nutzer:innen, die ein Formular über eine Landing Page abgeschickt haben."
page_order: 3
---

# Retargeting von Nutzer:innen über eine Landing Page

> Lernen Sie, wie Sie Nutzer:innen, die ein Formular über eine Landing Page abgeschickt haben, retargeten können, indem Sie ein spezielles Segment erstellen oder eine Nachricht triggern, wenn das Formular abgeschickt wird.

## Voraussetzungen

Bevor Sie beginnen, müssen Sie eine [Landing Page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) erstellen.

## Nutzer-Retargeting

Braze verfolgt automatisch, wenn ein Nutzer:innen ein Landing Page-Formular abschickt. Sie können die Gesamtzahl der Eingaben für ein Formular unter [Landing Page Analytics]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics) einsehen. Für benutzerspezifisches Retargeting müssen Sie jedoch Nutzer:innen über Ihr Landing Page-Formular mit einer der folgenden Methoden retargeten:

- **Verwendung eines Segments:** Sie können ein neues Segment erstellen, um automatisch Nutzer:innen zu identifizieren, die ein Landing Page-Formular abgeschickt haben oder nicht.
- **Verwendung eines Triggers für Nachrichten:** Sie können einen Trigger für Nachrichten einrichten, um Nutzern:innen automatisch Nachrichten zu senden oder sie in ein Canvas aufzunehmen, nachdem sie das Formular abgeschickt haben.

{% tabs local %}
{% tab Using a segment %}
Wenn Sie [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), wählen Sie unter der Gruppe "Retargeting" die Option **Übermitteltes Formular auf der Landing Page**.

\![Segmentierung mit ausgewählter Filtergruppe "Eingereichtes Formular auf der Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

Von hier aus können Sie Nutzer:innen danach segmentieren, ob sie ein Landing Page-Formular für Ihre Landing Page abgeschickt haben oder nicht.
{% endtab %}

{% tab Using a message trigger %}
Wenn Sie die Zustellung für Ihre [Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) oder Ihr [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/) auswählen, wählen Sie die **aktionsbasierte Zustellung** und dann das **Formular für die übermittelte Landing Page**.

Alle Nutzer:innen, die ein Formular über dieses Landing Page-Formular einreichen, erhalten entweder eine Nachricht über den gewählten Messaging-Kanal oder werden in den gewählten Canvas eingetragen.

\![Landing Page Aktion triggern im Messaging.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
Die aktionsbasierte Zustellung für Landing Pages ist für In-App-Nachrichten nicht verfügbar. Um Nutzer:innen, die ein Formular auf einer Landing Page mit einer In-App-Nachricht eingereicht haben, als Zielgruppe zusammenzustellen, wählen Sie den Filter **Eingereichtes Formular auf Landing Page** in den **Targeting-Optionen** Ihrer Kampagne aus.
{% endalert %}

{% endtab %}
{% endtabs %}
