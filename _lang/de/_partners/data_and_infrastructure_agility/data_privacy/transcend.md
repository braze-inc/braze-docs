---
nav_title: Transcend
article_title: Transcend
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Transcend, einer Datenschutz-Infrastrukturplattform, die Braze-Benutzern hilft, die Erfüllung von Anfragen von Betroffenen zu automatisieren."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend ist ein Unternehmen für Datenschutzinfrastrukturen, das es Unternehmen einfach macht, ihren Nutzern die Kontrolle über ihre Daten zu geben, indem es automatisch Anfragen von Betroffenen innerhalb von Unternehmen über alle ihre Datensysteme und Anbieter hinweg erfüllt. 

Die Partnerschaft zwischen Braze und Transcend hilft Anwendern, Datenschutzanfragen zu automatisieren, indem sie Daten über Dutzende von Datensystemen hinweg orchestrieren und so Teams bei der Einhaltung von Vorschriften wie GDPR und CCPA unterstützen. Transcend stellt den Endbenutzern ein Kontrollpanel oder Datenschutzzentrum zur Verfügung, das auf `privacy.\<company\>.com` gehostet wird. Dort können die Benutzer ihre Datenschutzeinstellungen verwalten, ihre Daten exportieren oder löschen. 

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| Konto transzendieren | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Transcend-Konto](https://app.transcend.io/) mit Admin-Rechten. |
| Braze API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.delete, users.alias.new, users.export.ids, email.unsubscribe,`und `email.blacklist`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Transcend ermöglicht Ihnen den programmgesteuerten Zugriff, die Löschung und die Abmeldung von Benutzern von der Kommunikation in der Braze-Plattform in Übereinstimmung mit den Datenschutzbestimmungen.

### Schritt 1: Einrichten der Braze-Integration
Um loszulegen, melden Sie sich bei [Transcend](https://app.transcend.io/login) an.
1. Navigieren Sie zu **Data Map > Datensilo hinzufügen > Braze** und wählen Sie die Schaltfläche **Verbinden**.<br><br>
2. Wenn Ihr Konto eingerichtet ist, melden Sie sich unter einer der entsprechenden URLs an: `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Verwenden Sie die folgende [Tabelle]({{site.baseurl}}/api/basics/#endpoints), um herauszufinden, welche Subdomain Sie auf der Grundlage Ihrer Dashboard-URL einschließen sollten.<br><br>
3. Wenn Sie verbunden sind, navigieren Sie zur Registerkarte Transcend **Privacy Center**. Hier müssen Sie die Daten in Braze mit Ihren Datenpraktiken abgleichen. Erstellen Sie dazu eine neue Kategorie und eine neue Datensammlung mit der entsprechenden Namenskonvention (z.B. "Mailinglisten oder Benutzerprofil"). Wenn Sie fertig sind, klicken Sie auf **Veröffentlichen**.<br><br>
4. Navigieren Sie zurück zu Ihrer Data Map und klicken Sie auf das Datensilo von Braze. Erweitern Sie **Datenpunkte verwalten** und wählen Sie aus der Dropdown-Liste die Sammlungsbezeichnung (Kategorie), die Sie im vorherigen Schritt erstellt haben. Sie können auch wählen, welche Datenaktionen (z.B. Zugriff oder Löschen) für welche Datenpunkte aktiviert sind. <br><br>
5. Erweitern Sie als Nächstes, während Sie sich noch im Braze-Datensilo befinden, **Identifikatoren verwalten**. Markieren Sie die entsprechenden Kästchen für die Identifikatoren, die Sie aktivieren möchten. Wenn Sie z.B. möchten, dass Transcend Benutzer nach ihrer E-Mail-Adresse sucht, aktivieren Sie das Kästchen zur Kennzeichnung der E-Mail-Adresse.

{% alert note %}
Wenn Kennungen nicht korrekt aktiviert sind, kann Transcend Anfragen für bestimmte Benutzer nicht bearbeiten.
{% endalert %}

### Schritt 2: Test Anfragen
Transcend empfiehlt, Anfragen über Ihre Data Map zu testen, bevor Sie mit der Verarbeitung von Anfragen von Endbenutzern beginnen.
1. Gehen Sie in Transcend zum **Datenschutz-Center** und klicken Sie auf **Ihr Datenschutz-Center anzeigen**.<br><br>
2. Klicken Sie in Ihrem **Datenschutz-Center** auf **Kontrolle übernehmen** und dann auf **Meine Daten herunterladen**. Geben Sie Ihre E-Mail-Adresse ein oder melden Sie sich an, um sich zu authentifizieren, bevor Sie die Anfrage abschicken.<br><br>
3. Prüfen Sie Ihre E-Mail auf eine Nachricht von Transcend. Sie werden aufgefordert, auf einen Verifizierungslink zu klicken, um die Anfrage zu überprüfen.<br><br>
4. Als nächstes gehen Sie zurück zum **Admin-Dashboard**, navigieren zur Registerkarte **Eingehende Anfragen** und wählen Ihre Anfrage aus. Kontaktieren Sie Transcend unter [support@transcend.io](mailto:support@transcend.io), wenn Sie die Anfrage hier nicht sehen.<br><br>
5. Nachdem Sie auf Ihre Anfrage geklickt haben, navigieren Sie zur Registerkarte **Datensilos** und wählen Sie **Braze**. Prüfen und bestätigen Sie die zurückgegebenen Daten.<br><br>
6. Navigieren Sie schließlich zur Registerkarte **Bericht** und klicken Sie auf **Genehmigen und Senden**. Sie sollten den Bericht an die E-Mail-Adresse erhalten, die Sie bei der Anfrage angegeben haben.

## Entfernen Sie die Integration der Lötstellen
So entfernen Sie das Braze Datensilo aus Ihrer Transcend Data Map:
1. Navigieren Sie zu Ihrer **Data Map**, und klicken Sie auf **Braze**. <br><br>
2. Erweitern Sie am unteren Rand des Bildschirms **Lötstellen entfernen** und klicken Sie auf **Silo entfernen**. Sie werden aufgefordert, zu bestätigen, dass Sie das Silo entfernen möchten. Klicken Sie auf **Ok**. <br><br>
3. Vergewissern Sie sich, dass das Silo entfernt wurde, indem Sie zurück zu Ihrer Data Map navigieren.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints