---
nav_title: Juni
page_order: 7
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Juni 2020."
---
# Juni 2020

## Aufbewahrungsberichte

Retention Reports bietet jetzt Range Retention für [Kampagnen][2] und [Canvases][1]. Range Retention misst, wie viele Benutzer in bestimmten Zeitintervallen zurückkommen und ein ausgewähltes Retention-Ereignis durchführen. 

## Benutzer verfolgen API-Updates

Der [Endpunkt`users/track` ][3] hat jetzt eine Standardrate von 50.000 API-Anfragen pro Minute für Dashboard-Unternehmen, die nach dem 2. Juni 2020 gegründet wurden. Bestehende Unternehmen, die vor diesem Datum gegründet wurden, und ihre Arbeitsbereiche können weiterhin unbegrenzt API-Anfragen an den Endpunkt `users/track` stellen.

Braze führt diese Voreinstellung für unseren am meisten genutzten Endpunkt mit Kundenkontakt ein, um unsere Ziele in Bezug auf Stabilität und Zuverlässigkeit für unsere API und Infrastruktur zu erreichen. Die Begrenzung ist sehr großzügig und wird nur sehr wenige Armaturenbrettfirmen und deren regulären Betrieb betreffen. Sollten Sie eine Erhöhung dieses Limits benötigen, wenden Sie sich bitte an Ihren Customer Success Manager oder unser Support-Team, um eine Erhöhung zu beantragen.

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
