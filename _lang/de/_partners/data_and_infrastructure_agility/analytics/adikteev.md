---
nav_title: Adiktejew
article_title: Adikteev Abwanderungsprognose
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Adikteev, einer Engine zur Benutzerbindung, die Abwanderungsvorhersagen mit Full-Service-App-Retargeting kombiniert"
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Adikteev Abwanderungsprognose

> [Adikteev](https://www.adikteev.com/churn-prediction) ist eine Engine zur Nutzerbindung, die Abwanderungsprognosen mit einem Full-Service-App-Retargeting kombiniert.

Die Integration von Braze und Adikteev ermöglicht es Ihnen, die Benutzerbindung zu erhöhen, indem Sie die Technologie von Adikteev zur Vorhersage der Abwanderung innerhalb von Braze CRM-Kampagnen nutzen, um Benutzersegmente mit hohem Risiko prioritär anzusprechen.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Adikteev-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Adikteev-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit der Berechtigung `users.track`. <br><br> Diese können Sie im Braze Dashboard unter **Einstellungen** > **APIs und Identifikatoren** erstellen. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

{% tabs %}
{% tab Filterung des Publikums %}
Verfeinerung Ihrer Zielgruppensegmente basierend auf dem Abwanderungsrisiko.<br> Die Namen und Werte der von Adikteev gesendeten benutzerdefinierten Attribute sind konfigurierbar.

![Ein Screenshot zeigt ein Beispiel für die Verwendung eines von Adikteev gesendeten benutzerdefinierten Attributs als Zielgruppensegmentfilter.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Zielgerichtete Nachrichten %}
Individuelle Anpassung Ihrer Braze Messaging-Kampagnen auf der Grundlage des Abwanderungsrisikos der Empfänger.

![Ein Screenshot zeigt ein Beispiel für die Verwendung eines von Adikteev gesendeten benutzerdefinierten Attributs als Filter für die Kampagnenausrichtung.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: Teilen Sie den Event-Stream Ihrer App

Um die Abwanderungsvorhersage für Ihre App-Zielgruppe zu starten, müssen Sie bei Adikteev die Ereignis-Postbacks Ihrer mobilen Messplattform aktivieren. Folgen Sie den Anweisungen auf der [Adikteev Support-Website](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation), um dies einzurichten.

### Schritt 2: Erstellen Sie Ihren Braze REST API Schlüssel

Navigieren Sie in Braze zu **Einstellungen** > **APIs und Identifikatoren**. Wählen Sie **Neuen API-Schlüssel erstellen**, geben Sie den API-Schlüsselnamen Ihrer Wahl ein und stellen Sie sicher, dass die folgende Berechtigung hinzugefügt wird:

- `users.track`

### Schritt 3: Informationen für das Adikteev-Team bereitstellen

Um die Integration abzuschließen, müssen Sie Ihrem Adikteev-Kundenbetreuer Ihren REST-API-Schlüssel und die URL des REST-Endpunkts mitteilen. Adikteev wird die Verbindung herstellen und Sie nach Abschluss der Einrichtung kontaktieren, um die Integration zu bestätigen.

## Batching und Ratenbeschränkungen

Der Endpunkt `user.track` wird verwendet, um Details über Ihre Benutzer zu aktualisieren. In der [API-Dokumentation]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) finden Sie alle Einzelheiten zu den Ratenbeschränkungen des Endpunkts, zur Stapelverarbeitung von Anfragen und zu Anfragedetails.

{% alert tip %}
Denken Sie daran, dass API-Aufrufe nur zur Aktualisierung von Daten erfolgen sollten, die sich geändert haben, um die Anzahl der API-Aufrufe insgesamt zu reduzieren. Mit anderen Worten: Aktualisieren Sie nur Benutzer, bei denen sich das Abwanderungssegment geändert hat.
{% endalert %}

## Benutzer- und Gerätekennungen

Benutzerprofile in Braze können mit jeder Art von Benutzer- oder Gerätekennungen verknüpft werden. Die Liste der verfügbaren Optionen hängt davon ab, wie Sie die Datenerfassung mit Braze integriert haben. Für Adikteev müssen Sie einen gemeinsamen Bezeichner zwischen Ihrem MMP und Ihren Benutzerprofilen in Braze finden, damit die Churn-Segment-Informationen korrekt gesendet werden können.

## Aufbewahrung und Löschung von Daten

Wenn keine Aktualisierung vorgenommen wird, werden das Attribut und sein Wert auf unbestimmte Zeit in den Braze-Benutzerprofilen gespeichert.

Um ein Profilattribut zu entfernen, setzen Sie es auf `null`.

## Payloads anfordern

Die von Adikteev an Braze gesendete Nutzlast ist anpassbar und kann nach den Bedürfnissen des Kunden konfiguriert werden. Dazu gehört die Konfiguration der verwendeten Bezeichner, des Namens des benutzerdefinierten Attributs und ob Adikteev neue Benutzer in Braze erstellen oder nur bestehende Benutzer aktualisieren kann.


## Unterstützung und Fehlerbehebung

Wenden Sie sich an Ihren Adikteev-Kundenbetreuer, wenn Sie Fragen zur Integration haben oder Unterstützung bei Ihren Anwendungsfällen benötigen.
