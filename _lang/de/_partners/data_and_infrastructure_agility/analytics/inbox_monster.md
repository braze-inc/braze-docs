---
nav_title: Inbox Monster
article_title: Inbox Monster
alias: /partners/inbox_monster/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Inbox Monster, einem Online-E-Mail-Marketing-Tool, mit dem Braze-Kunden leistungsstarke Einblicke in die Zustellbarkeit und kreative Analysen erhalten, um die Leistung des Posteingangs zu verbessern."
page_type: partner
search_tag: Partner

---

# Inbox Monster

> [Inbox Monster](https://inboxmonster.com//) ist eine Plattform für Posteingangssignale, die Unternehmensmarken dabei hilft, jede Sendung zu erhalten. Es handelt sich um eine integrierte Suite von Lösungen für Zustellbarkeit, kreative Gestaltung und SMS-Überwachung, die moderne Customer Relationship Management (CRM)-Teams unterstützt und die Angst vor dem Versand beendet.

Die Integration von Braze und Inbox Monster ermöglicht es Ihnen, manuelle Seedlist-Tests zu eliminieren, die Erstellung aussagekräftiger und umsetzbarer Signale für die Platzierung im Posteingang zu automatisieren, den Prozess der Überprüfung und Genehmigung von E-Mail-Kreativmaterial zu vereinfachen und wertvolle Erkenntnisse über die Zustellbarkeit zu gewinnen. Sie können auch nahtlos E-Mail-Vorlagen für kreative Diagnosen und Gerätevorschauen importieren.

## Voraussetzungen

| Anforderung                    | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Posteingangsmonster-Plattform-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Konto auf der Inbox Monster-Plattform.                                                                                                                                                                                                                                                                                                                                                                 |
| Braze REST API Schlüssel             | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen:  <br> - `messages.send` <br>  - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> - `templates.email.list` <br><br> Und mit den folgenden Whitelist-IPs: <br> - `3.136.16.19` <br>  - `3.140.233.31`<br> - `18.220.127.138` <br><br> Dieser kann im Braze Dashboard unter **Einstellungen** > **APIs und Identifikatoren** auf der Registerkarte **API-Schlüssel** erstellt werden. |
| Braze App Kennung           | Eine Braze App-Kennung. <br><br>Diese finden Sie im Braze Dashboard unter **Einstellungen** > **APIs und Identifikatoren** auf der Registerkarte **App-Identifikatoren**.                                                                                                                                                                                                                                                                                                |
| Braze Endpunkt                 | [Ihr Braze-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) ist mit der URL Ihres Braze-Dashboards verknüpft.<br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`.                                                                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

Um Inbox Monster zu integrieren, folgen Sie den Schritten unter [Integration mit Inbox Monster](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3).

## Nutzung

Wie Sie über Inbox Monster geplante Inbox-Einstufungstests versenden können, erfahren Sie unter [Geplante Inbox-Einstufungstests](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e).