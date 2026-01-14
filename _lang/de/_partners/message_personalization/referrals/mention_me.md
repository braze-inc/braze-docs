---
nav_title: Mention Me
article_title: Integration von Mention Me mit Braze
description: Anleitung zur Einrichtung der Mention Me Integration
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> Gemeinsam können [Mention Me](https://www.mention-me.com/) und Braze Ihr Tor zur Gewinnung von Premium-Kund:innen und zur Förderung einer unerschütterlichen Markentreue sein. Durch die nahtlose Integration von First-Party-Daten für Empfehlungen in Braze können Sie hoch personalisierte Omnichannel-Erlebnisse liefern, die auf Ihre Markenfans zugestellt sind.

_Diese Integration wird von Mention Me gepflegt._

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Mention Me-Konto   | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Mention Me-Konto](https://mention-me.com/login).                                                                     |
| Ein Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `templates.email.create`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Ein Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

* Senden Sie Kontaktdaten und Opt-ins von Mention Me verwiesenen Kunden in Realtime an Braze
* Verwenden Sie Daten von Empfehlungen, um E-Mail-Erinnerungen für Gutscheine zu erstellen
* Verbessern Sie die Performance anderer Marketing-Kanäle, indem Sie Daten aus Empfehlungen nutzen, um hochwertige Kunden zu segmentieren und zu targetieren.

## Welche Daten werden von Mention Me an Braze gesendet?

Wenn Sie diese Integration einrichten, erstellt Mention Me automatisch Ihre Kunden-Events und -Attribute - Sie müssen dies also nicht im Voraus tun.

Die E-Mail-Adressen Ihrer Kund:innen in Braze werden verwendet, um relevante Events und angepasste Attribute zu verknüpfen. Mention Me sendet Events und Attribute des Kontaktprofils für jeden Interessenten oder Kunden, der dieses Event über Mention Me triggert, unabhängig von seinem Opt-in-Status.

Weitere Einzelheiten finden Sie unter [Attribute und Ereignisse des Kontaktprofils](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze).

## Integration von Mention Me

{% alert tip %}
Eine vollständige Schritt-für-Schritt-Anleitung finden Sie in [der Dokumentation zur Einrichtung von Braze von Mention Me](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me).
{% endalert %}

So integrieren Sie Mention Me mit Braze:

1. Gehen Sie in Mention Me auf die [Integrationsseite von Braze](https://mention-me.com/merchant/~/integrations/braze) und wählen Sie dann **Verbinden**.
2. Wählen Sie **Neue Autorisierung erstellen**, fügen Sie dann [den von Ihnen zuvor erstellten API-Schlüssel](#prerequisites) hinzu und wählen Sie Ihre Braze-Instanz aus.
3. Wählen Sie ein oder mehrere Länder, mit denen Sie synchronisieren möchten.
4. Wenn Sie fertig sind, wählen Sie **Verbinden**.
