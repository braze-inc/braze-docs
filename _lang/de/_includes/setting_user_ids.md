Für jeden Ihrer Benutzer sollten Benutzer-IDs festgelegt werden. Diese sollten unveränderlich und zugänglich sein, wenn ein Benutzer die App öffnet. Die richtige Benennung Ihrer Benutzer-IDs von Anfang an ist einer der **wichtigsten** Schritte bei der Einrichtung von Benutzer-IDs. Wir empfehlen dringend die Verwendung des Braze-Standards für UUIDs und GUIDs (siehe unten). Wir empfehlen Ihnen außerdem dringend, diese Kennung anzugeben, da Sie damit die Möglichkeit haben:

- Verfolgen Sie Ihre Nutzer geräte- und plattformübergreifend und verbessern Sie so die Qualität Ihrer verhaltensbezogenen und demografischen Daten.
- Importieren Sie Daten über Ihre Benutzer mit unserer [Benutzerdaten-API][1].
- Richten Sie sich mit unserer [Messaging-API][2] für allgemeine und transaktionsbezogene Nachrichten an bestimmte Nutzer.

{% alert note %}
Wenn eine solche Kennung nicht verfügbar ist, weist Braze Ihren Benutzern eine eindeutige Kennung zu, aber Ihnen fehlen dann die für Benutzer-IDs aufgeführten Möglichkeiten. Sie sollten es vermeiden, Benutzer-IDs für Benutzer festzulegen, für die Sie keine eindeutige Kennung haben, die mit ihnen als Individuum verbunden ist. Die Übergabe einer Gerätekennung bietet keinen Vorteil gegenüber der automatischen anonymen Benutzerverfolgung, die Braze standardmäßig anbietet.
{% endalert %}

{% alert warning %}
Wenn Sie einen identifizierbaren Wert als Ihre Benutzer-ID angeben möchten, **empfehlen wir Ihnen dringend,** unsere [SDK-Authentifizierungsfunktion]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/) hinzuzufügen, um eine Benutzer-Identifizierung zu verhindern.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
