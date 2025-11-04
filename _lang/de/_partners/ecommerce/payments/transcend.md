---
nav_title: Transcend
article_title: Transcend
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Transcend, einer Infrastruktur für den Datenschutz, die den Nutzer:innen von Braze hilft, die Erfüllung von Anfragen zu automatisieren."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend ist ein Unternehmen für die Infrastruktur des Datenschutzes, das es Unternehmen einfach macht, ihren Nutzer:innen die Kontrolle über ihre Daten zu geben, indem es automatisch Anfragen von Betroffenen innerhalb von Unternehmen über alle ihre Datensysteme und Anbieter hinweg erfüllt. 

_Diese Integration wird von Transcend gepflegt._

## Über die Integration

Die Partnerschaft von Braze und Transcend hilft Nutzern:innen bei der Automatisierung von Anfragen zum Datenschutz durch Orchestrierung von Daten über Dutzende von Datensystemen hinweg und unterstützt Teams bei der Einhaltung von Vorschriften wie DSGVO und CCPA. Transcend stellt Endnutzern ein Control Panel oder Privacy Center zur Verfügung, das unter `privacy.\<company\>.com` gehostet wird. Dort können Nutzer:innen ihre Datenschutzeinstellungen verwalten, ihre Daten exportieren oder sie löschen. 

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| Transcend Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Transcend-Konto](https://app.transcend.io/) mit Admin-Rechten. |
| Braze API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.delete, users.alias.new, users.export.ids, email.unsubscribe,`und `email.blacklist`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Transcend erlaubt Ihnen, in Übereinstimmung mit den Datenschutzbestimmungen programmatisch auf die Braze-Plattform zuzugreifen, sie zu löschen und Nutzer:innen von der Kommunikation auszuschließen.

### Schritt 1: Einrichten der Braze Integration
Um loszulegen, melden Sie sich bei [Transcend](https://app.transcend.io/login) an.
1. Navigieren Sie zu **Data Map > Add Data Silo > Braze** und wählen Sie den Button **Connect**.<br><br>
2. Wenn Ihr Konto eingerichtet ist, melden Sie sich unter einer der entsprechenden URLs an: `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Verwenden Sie die folgende [Tabelle]({{site.baseurl}}/api/basics/#endpoints), um herauszufinden, welche Subdomain Sie auf der Grundlage Ihrer Dashboard-URL einschließen sollten.<br><br>
3. Wenn Sie verbunden sind, navigieren Sie zum Tab Transcend **Privacy Center**. Hier müssen Sie die Daten in Braze auf Ihre Datenpraktiken abbilden. Erstellen Sie dazu eine neue Kategorie und eine neue Datensammlung mit der entsprechenden Namenskonvention (z.B. "Mailinglisten oder Nutzer:innen-Profil"). Wenn Sie fertig sind, klicken Sie auf **Veröffentlichen**.<br><br>
4. Navigieren Sie zurück zu Ihrer Data Map und klicken Sie auf das Silo mit den isolierten Daten von Braze. Erweitern Sie **Datenpunkte verwalten** und wählen Sie die Sammlungsbezeichnung (Kategorie), die Sie im vorherigen Schritt erstellt haben, aus der Dropdown-Liste aus. Sie können auch wählen, welche Datenaktionen (z.B. Zugriff oder Löschen) für welche Datenpunkte aktiviert sind. <br><br>
5. Erweitern Sie als nächstes, während Sie sich noch im Silo der Braze-Daten befinden, **Bezeichner verwalten**. Markieren Sie die entsprechenden Kästchen für die Bezeichner, die Sie aktivieren möchten. Wenn Sie z.B. möchten, dass Transcend Nutzer:innen nach ihrer E-Mail Adresse sucht, aktivieren Sie das Kästchen zum Enablement des Bezeichners für die E-Mail Adresse.

{% alert note %}
Wenn Bezeichner nicht korrekt aktiviert sind, kann Transcend Anfragen für bestimmte Nutzer:innen möglicherweise nicht bearbeiten.
{% endalert %}

### Schritt 2: Test Anfragen
Transcend empfiehlt, Anfragen über Ihre Data Map zu testen, bevor Sie mit der Verarbeitung von Anfragen von Endnutzern beginnen.
1. Gehen Sie in Transcend zum **Datenschutz-Center** und klicken Sie auf **Ihr Datenschutz-Center anzeigen**.<br><br>
2. Klicken Sie in Ihrem **Datenschutz-Center** auf **Kontrolle übernehmen** und dann auf **Meine Daten herunterladen**. Geben Sie Ihre E-Mail ein oder melden Sie sich an, um sich vor dem Absenden der Anfrage zu authentifizieren.<br><br>
3. Prüfen Sie Ihre E-Mail auf eine Nachricht von Transcend. Sie werden aufgefordert, auf einen Verifizierungslink zu klicken, um die Anfrage zu überprüfen.<br><br>
4. Als nächstes gehen Sie zurück zum **Admin** Dashboard, navigieren zum Tab **Eingehende Anfragen** und wählen Ihre Anfrage aus. Kontaktieren Sie Transcend unter [support@transcend.io](mailto:support@transcend.io), wenn Sie die Anfrage hier nicht sehen.<br><br>
5. Nachdem Sie auf Ihre Anfrage geklickt haben, navigieren Sie zum Tab **Daten Silos** und wählen **Braze** aus. Prüfen und bestätigen Sie die zurückgegebenen Daten.<br><br>
6. Navigieren Sie schließlich zum Tab **Bericht** und klicken Sie auf **Genehmigen und Senden**. Sie sollten den Bericht an die E-Mail Adresse erhalten, die Sie bei der Anfrage angegeben haben.

## Entfernen Sie die Integration von Braze
So entfernen Sie das Silo der Braze Daten aus Ihrer Transcend Data Map:
1. Navigieren Sie zu Ihrer **Data Map**, und klicken Sie auf **Braze**. <br><br>
2. Erweitern Sie am unteren Rand des Bildschirms **Braze entfernen** und klicken Sie auf **Silo entfernen**. Sie werden aufgefordert, zu bestätigen, dass Sie das Silo entfernen möchten. Klicken Sie auf **Ok**. <br><br>
3. Vergewissern Sie sich, dass das Silo entfernt wurde, indem Sie zurück zu Ihrer Data Map navigieren.


