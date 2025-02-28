---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2017."
---

# September 2017

## Neue Funktionalität für Engagementberichte

Sie können jetzt [Engagement-Berichte][72] verwenden, um Metriken für eine Kampagne über bestimmte Zeiträume hinweg zu aggregieren. Sie können zum Beispiel die Gesamtzahl der Öffnungen eines Quartals oder die Gesamtzahl der Klicks über die gesamte Laufzeit einer Kampagne oder eines Canvas exportieren. Alles, was Sie tun müssen, ist:
- Wählen Sie einen Zeitrahmen aus, aus dem Sie Daten exportieren möchten,
- Planen Sie einen Engagement-Bericht, der regelmäßig an einen oder mehrere Empfänger gesendet wird, und
- Fügen Sie Kampagnen und Canvases anhand ihrer Tags zu Ihrem Bericht hinzu.

## Aktualisierungen der Benutzerprofilseite

Die [Benutzerprofilseite][73] wurde aktualisiert.

## Web-Push-Benachrichtigungen, die eine Benutzeraktion erfordern, um sie abzubrechen

Sie können jetzt für Chrome Web Pushes ein Verhalten zum Schließen von Nachrichten einrichten, bei dem der Empfänger mit der Nachricht interagieren muss, damit sie geschlossen wird. Diese Funktion erfordert Web SDK Version 1.6.13 oder höher.

## E-Mail Kopfzeilen

Wenn Sie in Braze eine E-Mail-Nachricht erstellen, können Sie jetzt ganz einfach eine Kopfzeile in den Abschnitt **Sendeinformationen** einfügen.

## Neuer API-Endpunkt für den Export roher Ereignisse

Wir haben einen neuen [API-Endpunkt][71] hinzugefügt, /raw_data/status, mit dem Sie abfragen können, ob ein bestimmter Tag in den Raw Event Export geladen wurde. Sie können damit prüfen, ob die Rohdaten eines bestimmten Tages verfügbar sind, um die Fehlersuche und Automatisierung zu erleichtern.



[71]: {{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges
[72]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[73]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
