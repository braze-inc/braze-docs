# Banner

> Mit Bannern können Sie personalisierte Nachrichten für Ihre Nutzer:innen erstellen und gleichzeitig die Reichweite Ihrer anderen Kanäle, wie E-Mail oder Push-Benachrichtigungen, erhöhen. Sie können Banner direkt in Ihre App oder Website einbetten, wodurch Sie sich mit den Nutzer:innen durch ein natürliches Erlebnis verbinden können.

![Ein Beispiel für ein auf einem Gerät gerendertes Banner.]({% image_buster /assets/img/banners/sample_banner.png %})

## Voraussetzungen

Banner sind als Teil Ihrer Message Credits verfügbar. Wenn Sie nicht über unser flexibles Modell für Nachrichten-Credits verfügen, sind Banner als zusätzliches Feature erhältlich. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, um weitere Informationen zu erhalten.

## Warum Banner verwenden?

Mit Bannern können Marketing- und Produkt-Teams den Inhalt von Apps oder Websites dynamisch personalisieren und so die Eignung und das Verhalten der Nutzer:innen in Realtime widerspiegeln. Sie zeigen Nachrichten persistent inline an und bieten nicht-intrusive, kontextuell relevante Erlebnisse, die zu Beginn jeder Nutzer:in-Sitzung automatisch aktualisiert werden.

Nach der Integration von Bannern in eine App oder Website können Marketer die Banner mit einem einfachen Drag-and-Drop-Editor entwerfen und starten. Damit entfällt die Notwendigkeit einer ständigen Unterstützung durch die Entwickler:innen, die Komplexität wird reduziert und die Effizienz gesteigert.

| Anwendungsfall | Erklärung |
| --- | --- |
| Ankündigungen | Halten Sie Ankündigungen wie bevorstehende Veranstaltungen oder Änderungen der Richtlinien im Vordergrund Ihres App-Erlebnisses. |
| Personalisierung der Angebote | Zeigen Sie personalisierte Aktionen und Anreize auf der Grundlage des Verlaufs, des Inhalts des Warenkorbs, der Abo-Stufe und des Treuestatus eines jeden Nutzers:innen. |
| Targeting für das Engagement neuer Nutzer:innen | Führen Sie neue Nutzer:innen durch das Onboarding und die Kontoeinrichtung. |
| Verkäufe und Aktionen | Heben Sie besondere Inhalte, aktuelle Produkte und laufende Kampagnen Ihrer Marke persistent und direkt auf Ihrer Homepage hervor, ohne die Nutzer:innen zu stören. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Features

Zu den Features für Banner gehören:

- **Einfache Erstellung von Inhalten:** Erstellen Sie Ihre Banner mit einem visuellen Drag-and-Drop-Editor, der Bilder, Text, Buttons, Formulare zur Erfassung von E-Mails, angepassten Code und vieles mehr unterstützt, und zeigen Sie eine Vorschau an.
- **Flexible Einsätze:** Definieren Sie mehrere Standorte innerhalb Ihrer Anwendung oder Website, an denen Banner erscheinen können, und ermöglichen Sie so ein präzises Targeting auf bestimmte Kontexte oder Nutzer:innen.
- **Dynamische Personalisierung:** Die Banner werden bei jeder neuen Nutzer:innen-Sitzung dynamisch aktualisiert und sorgen dafür, dass die Inhalte mit den integrierten Personalisierungstools von Braze und der Liquid-Logik aktuell und personalisiert bleiben.
- **Einheimische Prioritäten:** Legen Sie die Anzeigepriorität fest, wenn mehrere Banner auf dieselbe Platzierung abzielen, um sicherzustellen, dass die richtige Nachricht die Nutzer:innen zur richtigen Zeit erreicht.
- **Angepasste HTML-Unterstützung:** Integrieren Sie angepasste HTML-Blöcke für fortgeschrittene Anpassungen oder eine nahtlose Integration mit Ihren bestehenden Internet-Styles.

## Über Banner {#about-banners}

### Platzierungs-IDs {#placement-id}

Bannerplatzierungen sind bestimmte Standorte in Ihrer App oder Website, [die Sie mit dem Braze SDK erstellen]({{site.baseurl}}/developer_guide/banners/creating_placements/) und die festlegen, wo Banner erscheinen können.

Zu den üblichen Standorten gehören der obere Teil Ihrer Homepage, die Produktdetailseiten und die Kassenabläufe. Nachdem die Platzierungen erstellt wurden, können die Banner [in Ihrer Kampagne zugewiesen]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/) werden.

Außerdem sind Bannerplatzierungen für jeden Workspace eindeutig und können nur für 10 Kampagnen innerhalb eines Workspace verwendet werden. Platzierungen in jedem Workspace müssen eine eindeutige ID erhalten, die Sie bei der Erstellung einer Platzierung in Braze zuweisen.

{% alert important %}
Vermeiden Sie die Änderung von Platzierungs-IDs nach dem Starten einer Kampagne.
{% endalert %}

### Banner Priorität {#priority}

Wenn mehrere Kampagnen auf dieselbe ID referenzieren, werden die Banner in der Reihenfolge ihrer Priorität angezeigt: hoch, mittel oder niedrig. Standardmäßig sind neu erstellte Banner auf mittel eingestellt, aber Sie können [die Priorität manuell festlegen]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/#set-priority), wenn Sie Ihre Banner-Kampagne erstellen oder bearbeiten. 

Wenn mehrere Banner die gleiche Priorität haben, wird das neueste Banner, für das Nutzer:innen berechtigt sind, zuerst angezeigt.

### Anfragen zur Platzierung {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Zustellung von Nachrichten

Bannernachrichten werden Ihrer App oder Website als HTML-Inhalt zugestellt, der in der Regel innerhalb eines iframe gerendert wird. Dies stellt sicher, dass Ihre Banner auf allen Geräten einheitlich dargestellt werden, und hilft Ihnen, ihre Stile und Skripte vom Rest Ihres Codes zu trennen.

iframes ermöglichen dynamische und personalisierte Updates von Inhalten, die keine Änderungen an Ihrer Codebasis erfordern. Jeder iframe ruft den HTML-Code für jede Nutzer:innen-Sitzung ab und zeigt ihn mit Hilfe der Logik für das Targeting und die Personalisierung der Kampagne an.

### Abmessungen und Größenangaben

Hier erfahren Sie, was Sie über die Abmessungen und die Größe von Bannern wissen müssen:

- Der Composer erlaubt Ihnen zwar die Vorschau von Bannern in verschiedenen Größen, aber diese Informationen werden nicht gespeichert oder an das SDK gesendet.
- Der HTML-Code nimmt die gesamte Breite des Containers ein, in dem er dargestellt wird.
- Wir empfehlen, ein Element mit festen Abmessungen zu erstellen und diese Abmessungen im Composer zu testen.

## Beschränkungen

Jeder Workspace kann bis zu 100 aktive Banner-Kampagnen unterstützen. Wenn dieses Limit erreicht ist, müssen Sie eine bestehende Kampagne [archivieren oder deaktivieren]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status), bevor Sie eine neue Kampagne erstellen können.

Außerdem unterstützen Banner Nachrichten die folgenden Features nicht:

- Canvas-Integration
- API-ausgelöste und aktionsbasierte Kampagnen
- Currents
- Connected-Content
- Aktionscodes
- Nutzer:innen-gesteuerte Entlassungen
- `catalog_items` unter Verwendung des [Tags`:rerender` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid)

{% alert tip %}
Möchten Sie bei der Festlegung der nächsten Prioritäten helfen? Kontaktieren Sie [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}

## Nächste Schritte

Da Sie nun über Banner Bescheid wissen, sind Sie bereit für die nächsten Schritte:

1. [Erstellen von Bannerplatzierungen in Ihrer App oder Website]({{site.baseurl}}/developer_guide/banners/creating_placements/)
2. [Erstellen von Bannerkampagnen in Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
