---
nav_title: Storyly
article_title: Storyly
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Storyly, einem leichtgewichtigen SDK, das es App-Besitzern erlaubt, ihre Segmente gezielt zu segmentieren und Braze mit mehr First-Party-Daten zu füttern."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) ist ein leichtgewichtiges SDK, das Geschichten in Ihre App oder Website bringt. Mit einem intuitiven Designstudio, aufschlussreichen Analytics und nahtloser Konnektivität ist Storyly ein leistungsstarkes Tool zur Bereicherung des Erlebnisses der Zielgruppe. 

_Diese Integration wird von Storyly gepflegt._

## Über die Integration

Die Integration von Braze und Storyly erlaubt es Ihnen, Ihre Segmente in Braze als Zielgruppe in der Storyly-Plattform zu verwenden. Mit dieser Integration können Sie:
- Targeting Ihrer Segmente mit spezifischen Storys
- Verwenden Sie Nutzer:innen-Attribute, um die Inhalte Ihrer Story zu personalisieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Storyly Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein Storyly-Konto. |
| Storyly SDK | Sie müssen das [Storyly SDK](https://integration.storyly.io/) installieren. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit der Integration von Braze und Storyly können App-Besitzer allen Segmenten in Braze Stories zeigen und die Stories mit Attributen der Nutzer:innen personalisieren.

Einige häufige Anwendungsfälle sind:

__Targeting von Segmenten in Braze in Storyly__<br>Nach Abschluss der Integration können Sie eine Storyly Zielgruppe erstellen, die auf Ihren Segmenten in Braze basiert. Dabei kann es sich um ein demografisches oder verhaltensbezogenes Segment handeln. Stellen Sie beispielsweise Nutzer:innen zusammen, die an einem bestimmten Standort leben, die eine bestimmte Aktion in Ihrer App ausführen oder die sich für bestimmte Produkte mit bestimmten Stories interessieren, um die Konversion zu steigern.<br>
__Personalisierte Stories mit Nutzer:innen-Attributen__<br>Braze Nutzer:innen-Attribute können auch in Storyly verwendet werden, um dynamische Stories zu erstellen. Dies könnte den Namen eines Nutzers, Produkte in einem Warenkorb oder sogar favorisierte Produkte beinhalten, um den Nutzer:innen eindeutige personalisierte Geschichten zu liefern. Die Personalisierung trägt dazu bei, die Konversionsrate von Storys und die Engagement-Rate insgesamt zu erhöhen.

## Datenexport Integration

Die Integration von Braze Storyly wird im folgenden Video erklärt:

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Stellen Sie sicher, dass Ihre Storyly Integration angepasste Parameter enthält. Diese Parameter werden mit den Eigenschaften von Braze `external id` Nutzer:innen abgeglichen. Die angepasste Implementierung der Parameter wird hier für [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) und [Internet](https://integration.storyly.io/web/personalization-customaudience.html) erläutert.

Weitere Informationen finden Sie auch in der Dokumentation [von Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly).

### Schritt 1: Stellen Sie die Integration auf dem Dashboard von Storyly ein

Erstellen Sie eine Integration im **Storyly Dashboard > Einstellungen > Integrationen > Mit Braze verbinden**. Hier benötigen Sie Ihren Braze REST API-Schlüssel und den Braze REST-Endpunkt. 

### Schritt 2: Holen Sie sich Ihre Segmente 

Als nächstes können Sie Segmente von Braze verwenden, um eine Zielgruppe für Storyly zu erstellen. Diese können Sie über das **Storyly Dashboard > Einstellungen > Zielgruppen > Neue Zielgruppe > Zielgruppen mit Braze erstellen** erstellen.

Hier gibt es zwei Optionen für die Synchronisierung. Wählen Sie **Einmalige Synchronisierung** für bestimmte Kampagnen-Storys oder **Tägliche Synchronisierung** für langfristige Storys.


