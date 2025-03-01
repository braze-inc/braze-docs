---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für April 2019."
---

# April 2019

## New Currents Veranstaltungen & Felder

Zusätzlich zu einigen Korrekturen des Abschnitts wurde ein neues [Abonnement-Ereignis]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) auf der Seite Ereignisse zur Nachrichteneinbindung hinzugefügt. 

Sie können jetzt die Daten zur Änderung des Abonnementgruppenstatus von Braze nach [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) und [mParticle]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/) exportieren, sowie die Attributionsereignisse in [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents) installieren.

Außerdem wurde die Eigenschaft `canvas_step_id` zu den verfügbaren [Konvertierungsereignissen]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events) hinzugefügt.

{% alert important %}
Um die Vorteile dieser Aktualisierungen zu nutzen, müssen Sie Ihre Currents Connector-Einstellungen bearbeiten und die Ereignisse aktivieren, die Sie verwenden möchten. Wenden Sie sich an Ihren Kundenbetreuer, wenn Sie Fragen haben.
{% endalert %}

## Archivierung von Abonnementgruppen

Sie können jetzt [Abonnementgruppen archivieren]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Archivierte Abonnementgruppen können nicht bearbeitet werden und erscheinen nicht mehr in den Segmentfiltern.  Wenn Sie versuchen, eine Gruppe zu archivieren, die als Segmentfilter in einer E-Mail, einer Kampagne oder einem Canvas verwendet wird, erhalten Sie eine Fehlermeldung, die Sie daran hindert, die Gruppe zu archivieren, bis Sie alle Verwendungen der Gruppe entfernen.
