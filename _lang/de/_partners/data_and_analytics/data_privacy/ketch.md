---
title: Ketch
nav_title: Ketch
description: "Dieser referenzierte Artikel behandelt die Integration von Braze und Ketch. Ketch bietet vereinfachte Operationen zum Schutz der Privatsphäre und vollständige, dynamische Datenkontrolle und -intelligenz."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) ermöglicht es Unternehmen, verantwortungsvoll mit ihren Daten umzugehen. Ketch bietet vereinfachte Operationen zum Schutz der Privatsphäre und vollständige, dynamische Datenkontrolle und Intelligenz. 

_Diese Integration wird von Ketch gepflegt._

## Über die Integration

Die Integration von Braze und Ketch ermöglicht es Ihnen, die Kommunikationspräferenzen Ihrer Kund:in im Ketch-Einstellungscenter zu steuern und diese Änderungen automatisch an Braze weiterzugeben. 

{% alert note %}
Sie suchen eine Anleitung zur Erstellung von Abo-Gruppen? Sehen Sie sich unsere Artikel für <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>SMS-Abo-Gruppen</a> und <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>E-Mail-Abo-Gruppen</a> an.
{% endalert %}

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| Ketsch-Konto | Zum Aktivieren dieser Integration benötigen Sie ein [Ketch-Konto](https://www.ketch.com) mit Admin-Rechten. |
| Braze API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe`, und `email.blacklist`. <br><br> Dieser kann im Braze-Dashboard erstellt werden**(Entwicklungskonsole** > **REST-API-Schlüssel** > **Neuen API-Schlüssel erstellen**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Einrichten der Braze-Verbindung

1. Navigieren Sie in Ihrer [Ketch-Instanz](https://app.ketch.com) zu **Datensysteme** und wählen Sie **Braze** aus. Klicken Sie dann auf **Neue Verbindung**.
2. Geben Sie Ihrer Braze-Verbindung einen identifizierbaren Namen, der verwendet wird, um in API-basierten Prozessen auf diese Verbindung zu referenzieren. Beachten Sie, dass auch ein Code für diese Verbindung erstellt wird. Dieser Code sollte für alle Verbindungen eindeutig sein.
3. Bestätigen Sie die Abbildung der Identität Ihrer Nutzer:innen. Standardmäßig bildet Ketch die Nutzer:innen über die E-Mail Adresse eines Nutzers ab, oder über die `external_id` in Braze.
4. Fügen Sie den Braze API-Schlüssel hinzu und geben Sie den API-Endpunkt an. Beachten Sie, dass dieser [API-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) davon abhängt, welche Braze-Instanz Ihr Unternehmen verwendet.

### Schritt 2: Abo-Einstellungen konfigurieren

1. Gehen Sie zu **Richtlinien Center > Abonnements**. Wenn Sie den Tab Abonnements unter **Richtlinien-Center** nicht sehen, vergewissern Sie sich, dass Sie Zugriff auf das Marketing Preference Center haben, und überprüfen Sie, ob Sie über die richtigen Kontoberechtigungen für den Zugriff auf diesen Teil des Produkts verfügen.
2. Klicken Sie auf **Neues Abo erstellen**, um ein neues Thema zu erstellen. Jedes Abo wird mit einem Namen und einem Code versehen.
3. Fügen Sie die Kanäle für den Versand Ihrer Abo-Themen hinzu. Jeder Kanal wird im Marketing-Präferenzzentrum für Ihre Nutzer:innen angezeigt. Sie können auch die Details hinzufügen, wie das Ketch-Einstellungscenter ein bestimmtes Opt-in oder Opt-out Signal orchestrieren soll.
4. Wählen Sie die Braze-Verbindung aus, die Sie für die Orchestrierung der Opt-in und Opt-out Signale verwenden möchten.
5. Geben Sie die Braze `subscription_group_id` für die Abo-Gruppe ein, an die Sie die Nutzer:in-Einstellungen von Ketch senden möchten.

![Braze Abo-Gruppe ID.]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
Um Opt-in und Opt-out Signale von Nutzer:innen zu sammeln und zu orchestrieren, müssen die Identitäten richtig konfiguriert sein. Ketch empfiehlt, E-Mail als Bezeichner für die Orchestrierung der Nutzer:innen-Signale für diese Integration zu konfigurieren.
{% endalert %}


### Schritt 3: Identitäten konfigurieren

Ein Nutzer:innen kann das Zentrum für Marketing-Einstellungen nur sehen, wenn Ketch die Identität des Nutzers für Marketing-Einstellungen bestätigen kann. Wenn Ketch die Identität des Nutzers nicht richtig erfassen kann, wird die Seite mit den Marketing-Einstellungen für diesen Nutzer:innen nicht angezeigt, da Ketch nicht in der Lage ist, seine Benutzereinstellungen zu verwalten.

1. Um die Identität der Marketing-Einstellungen zu konfigurieren, gehen Sie in Ketch auf die Seite **Einstellungen** und klicken Sie auf **Identitätsraum**. Sie müssen entweder einen neuen Identitätsraum erstellen oder einen bestehenden Identitätsraum bearbeiten, um diesen Identitätsraum als Marketing-Einstellungsidentität zuzuweisen. Vergewissern Sie sich, dass der für die Eigenschaft eingesetzte Ketch-Tag diesen Identitätsraum richtig erfasst.
2. Gehen Sie zu **Experience Server** > **Eigenschaften**, und bearbeiten Sie die gewünschte Eigenschaft. Stellen Sie sicher, dass Sie unter der Datenebene für diese Eigenschaft den angepassten Identitätsbereich anpassen. Konfigurieren Sie dann, wie die Identität der Marketing-Präferenz auf dieser Website erfasst werden soll.
3. Nachdem Sie den Identitätsbereich konfiguriert haben, testen Sie, ob das Einstellungscenter angezeigt wird, indem Sie das Einstellungscenter auf der Website öffnen, auf der der Ketch Tag bereitgestellt wurde.


