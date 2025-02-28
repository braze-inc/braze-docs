---
nav_title: Große Segmente exportieren
article_title: Große Segmente exportieren
page_order: 4

page_type: solution
description: "Dieser Hilfe-Artikel führt Sie durch verschiedene Methoden zum Exportieren großer Benutzersegmente."
tool: Segments
---

# Große Segmente exportieren

Es gibt mehrere Methoden, ein großes Benutzersegment zu exportieren. Bei Segmenten, die mehr als 500.000 Benutzer enthalten, können Sie dieses größere Segment in kleinere Segmente aufteilen, um diese Benutzer zu erfassen, und jedes der kleineren Segmente aus dem Braze-Dashboard exportieren. 

Sie können auch [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) verwenden, um Ihre Nutzerbasis in mehrere Segmente aufzuteilen und diese dann nach dem Export zu kombinieren. Wenn Sie zum Beispiel Ihr Segment in zwei verschiedene Segmente aufteilen müssen, können Sie dies mit den folgenden Filtern tun:
- Segment:  Die zufällige Eimernummer ist kleiner als 5000 (umfasst 0-4999)
- Segment 2: Die zufällige Eimerzahl ist größer als 4999 (einschließlich 5000-9999)

Sie können auch die folgenden Endpunkte nutzen, um Benutzerdaten für ein bestimmtes Segment zu exportieren. Beachten Sie, dass für diese Endpunkte Datenlimits gelten.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 24\. Oktober 2022_
