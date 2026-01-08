# Banner: Häufig gestellte Fragen

> Hier finden Sie Antworten auf häufig gestellte Fragen zu Bannern in Braze. Weitere allgemeine Informationen finden Sie unter [Über Banner]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Wann erscheinen die Banner Updates für Nutzer:innen?

Die Banner werden mit den neuesten Daten aktualisiert, sobald Sie die Aktualisierungsmethode aufrufen. Sie müssen Ihre Banner-Kampagne nicht erneut versenden oder aktualisieren.

## Wie viele Vermittlungen kann ich in einer Sitzung anfragen?

In einer einzigen Anfrage zur Aktualisierung können Sie maximal 10 Platzierungen anfragen. Für jede Anfrage, die Sie stellen, gibt Braze das Banner mit der höchsten Priorität zurück, für das ein Nutzer:innen in Frage kommt. Weitere Anfragen führen zu einer Fehlermeldung.

Weitere Informationen finden Sie unter [Platzierungsanfragen]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Wie viele Banner Kampagnen können gleichzeitig aktiv sein?

Jeder Workspace kann bis zu 200 aktive Banner-Kampagnen unterstützen. Wenn dieses Limit erreicht ist, müssen Sie eine bestehende Kampagne [archivieren oder deaktivieren]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status), bevor Sie eine neue Kampagne erstellen können.

## Welcher Banner wird bei Kampagnen, die sich eine Platzierung teilen, zuerst angezeigt?

Wenn sich ein Nutzer:innen für mehrere Kampagnen qualifiziert, die sich dieselbe Platzierung teilen, wird das Banner mit der höchsten Priorität angezeigt. Weitere Informationen finden Sie unter [Bannerpriorität]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "Entwickler" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Kann ich Banner in meinem bestehenden Content-Card-Feed verwenden?

Banner unterscheiden sich von Content-Cards, d.h. Sie können Banner und Content-Cards nicht im selben Feed verwenden. Um bestehende Content-Card-Feeds durch Banner zu ersetzen, müssen Sie [Platzierungen in Ihrer App oder Website erstellen]({{site.baseurl}}/developer_guide/banners/placements/).

## Können Nutzer:innen einen Banner manuell ablehnen?

Nein. Nutzer:innen können Banner nicht manuell entlassen. Sie können jedoch die Sichtbarkeit von Bannern kontrollieren, indem Sie die Berechtigung von Nutzern:in Segmenten verwalten. Wenn ein Nutzer:innen die Targeting-Kriterien für eine Banner-Kampagne nicht mehr erfüllt, wird sie ihm bei seiner nächsten Sitzung nicht mehr angezeigt.

Wenn Sie beispielsweise ein Werbebanner anzeigen, bis ein Nutzer einen Kauf tätigt, kann die Protokollierung eines Ereignisses wie `purchase_completed` diesen Nutzer aus dem Targeting-Segment entfernen und das Banner in nachfolgenden Sitzungen effektiv ausblenden.

## Kann ich die Analytics für Banners Kampagnen über die Braze API exportieren?

Ja Über den [Endpunkt `/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) können Sie Daten darüber abrufen, wie viele Banner Kampagnen angesehen, angeklickt oder konvertiert wurden.

## Wann werden Nutzer:innen segmentiert?

Nutzer:innen werden zu Beginn der Sitzung segmentiert. Wenn die zielgerichteten Segmente einer Kampagne von angepassten Attributen, angepassten Events oder anderen Targeting-Attributen abhängen, müssen diese beim Nutzer:innen zu Beginn der Sitzung vorhanden sein.

## Wie kann ich Banner zusammenstellen, um die geringste Latenzzeit zu gewährleisten?

Je einfacher das Messaging in Ihrem Banner ist, desto schneller wird es dargestellt. Testen Sie Ihre Banner Kampagne am besten anhand der erwarteten Latenzzeit für Ihren Anwendungsfall. Testen Sie zum Beispiel unbedingt Liquid Attribute wie `catalog_items`.

## Werden alle Liquid-Tags unterstützt?

Nein. Die meisten Liquid-Tags werden jedoch für Banner Nachrichten unterstützt, mit Ausnahme von `catalog_items`, die mit dem [Tag `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid) neu gerendert werden.

## Kann ich Klick-Ereignisse erfassen?

Klick-Ereignisse werden nur erfasst, wenn eine On-Click-Aktion auf einem `logClick`-Element festgelegt ist und über die [JS-Bridge]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge) aufgerufen wird.
