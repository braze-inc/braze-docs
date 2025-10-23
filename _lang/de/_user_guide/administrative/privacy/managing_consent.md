---
nav_title: Verwaltung der Zustimmung
article_title: Zustimmung verwalten
page_order: 10
page_type: reference
description: "In diesem Referenzartikel finden Sie Tipps für die Verwaltung von Einwilligungen mit Braze."
---

# Verwaltung der Zustimmung

> In diesem Referenzartikel finden Sie Tipps, wie Sie die Zustimmung Ihrer Nutzer:innen mit Braze verwalten können.

Braze kann keine spezifischen Ratschläge zur Auslegung von Gesetzen und Vorschriften oder zur Handhabung des Zustimmungsmanagements geben, da dies von der Auslegung des Gesetzes durch Ihr Rechtsteam abhängt. Wir bieten jedoch eine Reihe von Tools zur Unterstützung des Abo- und Einwilligungsmanagements.

Ihre Herangehensweise sollte von der Strenge abhängen, die Ihr juristisches Team aufgrund seiner Auslegung des Gesetzes verlangt. Hier sind einige Optionen, die Sie in Betracht ziehen können, aufgelistet von den strengsten bis zu den am wenigsten strengen:

- **Teams:** Verwenden Sie [Braze-Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) für echte Governance. Dazu müssen Sie allen Benutzerprofilen ein benutzerdefiniertes Attribut hinzufügen, um den Status der Zustimmung, das Datum der Zustimmung oder beides anzugeben. Sie müssen dann alle Kampagnen und Canvases in das vorgesehene Team migrieren und die Benutzerberechtigungen auf dem Dashboard entsprechend anpassen.
- **Attribut des Nutzerprofils:** Fügen Sie ein Zustimmungsattribut zu allen Benutzerprofilen hinzu. Dieses Attribut zeigt an, ob ein Benutzer seine Zustimmung gegeben hat oder nicht. In Zukunft können Sie dann ein Segment von Nutzern, die zugestimmt haben (z.B. `consent = true`), in alle Ihre Kampagnen und Canvases aufnehmen.
- **Kanalspezifische Abonnementgruppen:** Bearbeiten Sie Abo-Gruppen für bestimmte Kanäle (Push-Benachrichtigungen, E-Mail usw.), um die Zustimmung zu verwalten. Markieren Sie Nutzer:innen zunächst als abgemeldet von diesen Kanälen und erst dann als Abonnent:in, wenn sie zugestimmt haben.

{% alert important %}
Wenden Sie sich an Ihr juristisches Team, um den geeigneten Ansatz für die Einhaltung der Anforderungen an das Einwilligungsmanagement in Ihrem Unternehmen zu ermitteln.
{% endalert %}

