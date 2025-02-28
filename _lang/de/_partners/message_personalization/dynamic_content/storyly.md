---
nav_title: Storyly
article_title: Storyly
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Storyly, einem leichtgewichtigen SDK, das es App-Besitzern ermöglicht, ihre Segmente gezielt einzusetzen und Braze mit mehr First-Party-Daten zu versorgen."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) ist ein leichtgewichtiges SDK, das Geschichten auf Ihre App oder Website bringt. Mit einem intuitiven Design-Studio, aufschlussreichen Analysen und nahtloser Konnektivität ist Storyly ein leistungsstarkes Tool zur Bereicherung des Zuschauererlebnisses. 

Die Integration von Braze und Storyly ermöglicht es Ihnen, Ihre Segmente in Braze als Zielgruppe in der Storyly-Plattform zu verwenden. Mit dieser Integration können Sie:
- Richten Sie Ihre Segmente mit spezifischen Geschichten aus
- Verwenden Sie Benutzerattribute, um die Inhalte Ihrer Geschichten zu personalisieren

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Storyly Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein Storyly-Konto. |
| Storyly SDK | Sie müssen das [Storyly SDK](https://integration.storyly.io/) installieren. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit der Integration von Braze und Storyly können App-Besitzer allen Segmenten in Braze Geschichten zeigen und die Geschichten mit Benutzerattributen personalisieren.

Einige häufige Anwendungsfälle sind:

__Ziel-Lötstellen-Segmente in Storyly__<br>Nachdem die Integration abgeschlossen ist, können Sie eine Storyly-Zielgruppe erstellen, die auf Ihren Braze-Segmenten basiert. Dies könnte ein demografisches oder verhaltensbezogenes Segment sein. Richten Sie sich beispielsweise an Nutzer, die an einem bestimmten Ort leben, an Nutzer, die eine bestimmte Aktion in Ihrer App ausführen, oder an Nutzer, die sich für bestimmte Produkte mit bestimmten Geschichten interessieren, um die Konversion zu erhöhen.<br>
__Personalisierte Geschichten mit Benutzerattributen__<br>Braze-Benutzerattribute können auch in Storyly verwendet werden, um dynamische Geschichten zu erstellen. Dies könnte den Namen eines Benutzers, Produkte in einem Warenkorb oder sogar favorisierte Produkte beinhalten, um den Benutzern einzigartige personalisierte Geschichten zu bieten. Die Personalisierung trägt dazu bei, die Konversionsrate bei Geschichten und die allgemeine Engagement-Rate bei Geschichten zu erhöhen.

## Integration des Datenexports

Die Integration von Braze Storyly wird im folgenden Video erklärt:

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Stellen Sie sicher, dass Ihre Storyly-Integration benutzerdefinierte Parameter enthält. Diese Parameter werden mit der Benutzereigenschaft Braze `external id` abgeglichen. Die Implementierung benutzerdefinierter Parameter wird hier für [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) und [Web](https://integration.storyly.io/web/personalization-customaudience.html) erläutert.

Weitere Informationen finden Sie auch in der [Storyly-Dokumentation](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly).

### Schritt 1: Legen Sie die Integration im Storyly-Dashboard fest

Eine Integration wird im **Storyly Dashboard > Einstellungen > Integrationen > Mit Braze verbinden** erstellt. Hier benötigen Sie Ihren Braze REST API-Schlüssel und den Braze REST-Endpunkt. 

### Schritt 2: Holen Sie sich Ihre Segmente 

Als nächstes können Sie Braze-Segmente verwenden, um eine Storyly-Zielgruppe zu erstellen. Diese können Sie im **Storyly Dashboard > Einstellungen > Audiences > Neue Audience > Audience mit Braze erstellen** erstellen.

Hier gibt es zwei Optionen für die Synchronisierung. Wählen Sie **Einmalige Synchronisierung** für bestimmte Kampagnenberichte oder **Tägliche Synchronisierung** für langfristige Berichte.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints