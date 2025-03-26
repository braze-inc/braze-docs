---
title: Ketch
nav_title: Ketch
description: "Dieser Referenzartikel behandelt die Integration von Braze und Ketch. Ketch bietet vereinfachte Datenschutzvorgänge und eine vollständige, dynamische Datenkontrolle und -intelligenz."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) ermöglicht es Unternehmen, verantwortungsvoll mit ihren Daten umzugehen. Ketch bietet vereinfachte Datenschutzvorgänge und eine vollständige, dynamische Datenkontrolle und -intelligenz. 

Die Integration von Braze und Ketch ermöglicht es Ihnen, die Kommunikationspräferenzen Ihrer Kunden im Ketch-Einstellungscenter zu steuern und diese Änderungen automatisch an Braze weiterzugeben. 

{% alert note %}
Sie suchen eine Anleitung zur Erstellung von Abonnementgruppen? Sehen Sie sich unsere Artikel für <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group//'>SMS-Abonnementgruppen</a> und <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>E-Mail-Abonnementgruppen</a> an.
{% endalert %}

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| Ketsch-Konto | Zum Aktivieren dieser Integration ist ein [Ketch-Konto](https://www.ketch.com) mit Admin-Rechten erforderlich. |
| Braze API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe` und `email.blacklist`. <br><br> Dieser kann im Braze-Dashboard erstellt werden**(Developer Console** > **REST API Key** > **Create New API Key**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Einrichten der Lötverbindung

1. Navigieren Sie in Ihrer [Ketch-Instanz](https://app.ketch.com) zu **Data Systems** und wählen Sie **Braze**. Klicken Sie dann auf **Neue Verbindung**.
2. Geben Sie Ihrer Braze-Verbindung einen identifizierbaren Namen, der verwendet wird, um in API-basierten Prozessen auf diese Verbindung zu verweisen. Beachten Sie, dass für diese Verbindung auch ein Code erstellt wird. Dieser Code sollte für alle Verbindungen eindeutig sein.
3. Bestätigen Sie die Identitätszuordnung Ihrer Benutzer. Standardmäßig ordnet Ketch Benutzeridentitäten über die E-Mail-Adresse eines Benutzers oder über die `external_id` in Braze zu.
4. Fügen Sie den Braze-API-Schlüssel hinzu und geben Sie den API-Endpunkt an. Beachten Sie, dass dieser [API-Endpunkt](https://www.braze.com/docs/api/basics/#endpoints) davon abhängt, welche Braze-Instanz Ihr Unternehmen verwendet.

### Schritt 2: Konfigurieren Sie die Abonnementeinstellungen

1. Gehen Sie zu **Policy Center > Abonnements**. Wenn Sie die Registerkarte Abonnements unter **Policy Center** nicht sehen, vergewissern Sie sich, dass Sie Zugriff auf das Marketing Preference Center haben, und überprüfen Sie, ob Sie die richtigen Kontoberechtigungen für den Zugriff auf diesen Teil des Produkts haben.
2. Klicken Sie auf **Neues Abonnement erstellen**, um ein neues Thema zu erstellen. Jedes Abonnement wird einen Namen und einen Code haben.
3. Fügen Sie die Kanäle für den Versand Ihrer Abonnementthemen hinzu. Jeder Kanal wird im Marketing Preference Center für Ihre Benutzer angezeigt. Sie können auch die Details hinzufügen, wie Sie möchten, dass das Ketch-Einstellungszentrum ein bestimmtes Opt-In- oder Opt-Out-Signal orchestriert.
4. Wählen Sie die Braze-Verbindung aus, über die Sie die Opt-In- und Opt-Out-Signale orchestrieren möchten.
5. Geben Sie die Braze `subscription_group_id` für die Abonnementgruppe ein, an die Sie die Ketch-Benutzereinstellungen senden möchten.

![Braze Subscription Group ID.][1]

{% alert note %}
Um die Opt-In- und Opt-Out-Signale der Benutzer zu erfassen und zu steuern, müssen die Identitäten richtig konfiguriert sein. Ketch empfiehlt, E-Mail als Identifikator zu konfigurieren, um die Signale für die Benutzerpräferenzen für diese Integration zu orchestrieren.
{% endalert %}


### Schritt 3: Identitäten konfigurieren

Ein Benutzer kann das Zentrum für Marketing-Einstellungen nur sehen, wenn Ketch die Identität des Benutzers für Marketing-Einstellungen bestätigen kann. Wenn Ketch die Identität des Benutzers nicht richtig erfassen kann, wird die Seite mit den Marketing-Einstellungen für diesen Benutzer nicht angezeigt, da Ketch nicht in der Lage ist, seine Benutzereinstellungen zu verwalten.

1. Um die Identität der Marketing-Einstellungen zu konfigurieren, gehen Sie in Ketch auf die Seite **Einstellungen** und klicken Sie auf **Identitätsraum**. Sie müssen entweder einen neuen Identitätsraum erstellen oder einen bestehenden Identitätsraum bearbeiten, um diesen Identitätsraum als Marketingpräferenz-Identität zuzuweisen. Vergewissern Sie sich, dass das auf dem Grundstück eingesetzte Ketch-Tag diesen Identitätsraum korrekt erfasst.
2. Gehen Sie zu **Experience Server** > **Eigenschaften**, und bearbeiten Sie die gewünschte Eigenschaft. Stellen Sie unter der Datenebene für diese Eigenschaft sicher, dass Sie den benutzerdefinierten Identitätsbereich aktivieren. Konfigurieren Sie dann, wie die Identität der Marketingpräferenzen auf dieser Website erfasst werden soll.
3. Nachdem Sie den Identitätsraum konfiguriert haben, testen Sie, ob das Einstellungscenter angezeigt wird, indem Sie das Einstellungscenter auf der Website öffnen, auf der das Ketch-Tag bereitgestellt wurde.


[1]: {% image_buster /assets/img/ketch/ketch1.png %}