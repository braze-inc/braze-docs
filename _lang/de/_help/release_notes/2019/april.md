---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für April 2019."
---

# April 2019

## Neue Currents Veranstaltungen & Felder

Zusätzlich zu einigen Korrekturen des Abschnitts wurde ein neues [Abo-Ereignis]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) auf der Seite Messaging Engagement Events hinzugefügt. 

Sie können jetzt Daten zur Änderung des Zustands von Abo-Gruppen aus Braze in [Segmente]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) und [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mParticle/mparticle_for_currents/) sowie in [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/) als Attribution Events exportieren.

Außerdem wurde die Eigenschaft `canvas_step_id` zu den verfügbaren [Konversions-Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events) hinzugefügt.

{% alert important %}
Um von diesen Updates zu profitieren, müssen Sie die Einstellungen Ihres Currents Konnektors bearbeiten und die Ereignisse, die Sie verwenden möchten, aktivieren. Wenden Sie sich an Ihren Account Manager:in, wenn Sie Fragen haben.
{% endalert %}

## Abo-Gruppen archivieren

Sie können jetzt [Abo-Gruppen archivieren]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Archivierte Abo-Gruppen können nicht bearbeitet werden und erscheinen nicht mehr in den Segmentierungs Filtern.  Wenn Sie versuchen, eine Gruppe zu archivieren, die in einer E-Mail, einer Kampagne oder einem Canvas als Segmentfilter verwendet wird, erhalten Sie eine Fehlermeldung, die Sie daran hindert, die Gruppe zu archivieren, bis Sie alle Verwendungen der Gruppe entfernen.
