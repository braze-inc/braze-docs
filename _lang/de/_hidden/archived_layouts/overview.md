---
nav_title: Übersicht
page_order: 0
noindex: true
---

# Beispiel-Layout: Übersicht

> Das Übersichtslayout ist gut geeignet, um eine spezielle Navigationsoption am oberen Rand einer Seite zu erstellen, die es Nutzern:innen ermöglicht, durch Klicken auf einen Button zu einem bestimmten Teil einer Seite oder zu einer ganz anderen Seite zu gelangen.

Klassische Beispiele für das SELEKTOR-Layout sind die Seite [SDK Changelogs](https://www.braze.com/docs/developer_guide/changelogs) oder die [Seite In-App-Nachricht Kreative Details](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/).

## Erforderliche Komponenten

1. YAML-Notation für Öffnungen und Schließungen. Mit anderen Worten: --- vor dem Inhalt und --- danach.
2. Anführungszeichen um bestimmte Parameterinhalte. (Header-Parameter, Textparameter, Inhalte mit Bindestrichen oder anderen Sonderzeichen).
3. Glossar Tags Notation (Dies sind Filter Tags)

## Erforderliche Parameter

|Parameter | Inhaltstyp | Details |
|---|---|---|
|`page_order`| Numerisch | Ordnen Sie die Seite innerhalb des Abschnitts. Diese Reihenfolge wird in der linken Navigation angezeigt. |
| `nav-title`| Alphanumerisch | Titel, der in der linken Navigation erscheinen wird. |
|`layout`| Alphanumerisch - Keine Leerzeichen | Wählen Sie ein Layout aus dem [Layoutbereich](https://github.com/Appboy/braze-docs/tree/develop/_layouts) der Dokumentation aus. | 
|`guide_top_header`|Alphanumerisch | Betiteln Sie Ihre Seite.|
|`guide_top_text`|Alphanumerisch | Beschreiben Sie Ihre Seite. Dies wird direkt über den Buttons und deren Titel angezeigt. Anführungszeichen um den Inhalt erforderlich. |
|`guide_featured_title`| Alphanumerisch | Betiteln Sie Ihre Karten. Dies wird direkt über den Buttons angezeigt.
|`guide_featured_list`| Mehr YAML, Alphanumerisch | Siehe [Format für Leitfaden-Listen](#guide-listing-format) unten. |

### Leitfaden-Listenformat

|Parameter | Inhaltstyp | Details |
|---|---|---|
|`name`| Alphanumerisch | Benennen Sie das Feld. |
| `link`| URL oder Pfad | Link zu dem Ort, an dem die Box aufgestellt wird. Muss die vollständige URL enthalten oder (wenn es sich um einen internen Link handelt) `/docs...`  |
|`image`| Pfad | Link zum Standort des Bildes. |

Beispiel für das Format:

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

## Beispiel

```yaml
---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}
```
