---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Jacquard Dynamic Optimisation, die Braze-Currents und Connected-Content nutzt, um über Webhooks Click-through-Informationen von Ihren Abonnenten zu sammeln. Jacquard verknüpft diese Ereignisse dann mit Ihren Sprachvarianten zur Realtime-Sprachoptimierung."
page_type: partner
search_tag: Partner
---

# Dynamische Jacquard-Optimierung

> [Jacquard](https://www.jacquard.com/) vereint künstliche Intelligenz, Computerlinguistik und den Geist der Kundenorientierung, um die Markensprache in großem Umfang über Kanäle hinweg einzusetzen, die an die Stimme Ihrer Marke angepasst sind.

Die von Jacquard X betriebene dynamische Optimierung nutzt Braze-Currents und Connected-Content, um über Webhooks Click-through-Informationen von Ihren Abonnent:innen zu sammeln. Jacquard verknüpft diese Ereignisse dann mit Ihren Sprachvarianten zur Realtime-Sprachoptimierung. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Jacquard-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Jacquard-Konto](https://www.jacquard.com/). |
| Jacquard Connect Server Token | Ein langer String von Zeichen, der als Passwort für Ihre Kampagne in Braze dient, um auf Ihre Jacquard-Sprache zuzugreifen.<br><br>Sie können dies bei Ihrem Customer-Success-Manager:in von Jacquard anfragen, falls Sie es nicht bereits erhalten haben. |
| Currents | Um Daten zu Currents exportieren zu können, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Jacquard Amazon S3-Anmeldedaten anfragen

Sie benötigen Jacquard, um einen speziellen Amazon S3-Bucket einzurichten, der Ihre Click Tracking-Ereignisse von Braze empfängt. Wenden Sie sich an Ihren Customer-Success-Manager:in, um diesen Prozess zu starten. Wenn der Bucket erstellt wird, erhalten Sie eindeutige Zugangsdaten, um Ihren Current zu erstellen. 

### Schritt 2: Currents erzeugen

1. Wählen Sie in Braze **Currents > Neue Currents erstellen > Amazon S3 Datenexport**. 
2. Benennen Sie dann Ihren Current und geben Sie eine E-Mail an.
3. Fügen Sie die ID Ihres Jacquard AWS Zugangsschlüssels und den geheimen Zugangsschlüssel in das Feld Zugangsdaten ein. Fügen Sie dann "phrasee-braze-currents-exports" als AWS S3 Bucket-Name hinzu. 
4. Fügen Sie schließlich den AWS S3-Bucket-Ordner hinzu, den Sie von Ihrem Customer-Success-Manager:in erhalten haben. Es wird wahrscheinlich der Name Ihres Unternehmens sein.
5. Aktivieren Sie unter **Allgemeine Einstellungen** das Kästchen "Ereignisse von anonymen Nutzer:innen einbeziehen" und unter **Engagement-Ereignisse verwalten** das Kästchen "E-Mail Klick".
6. Wenn Sie fertig sind, wählen Sie **Current starten**.

### Schritt 3: Anfrage zur Entfernung von persönlich identifizierbaren Informationen (PII).

Als Nächstes wenden Sie sich an das Team Ihres Braze-Kontos, um sicherzustellen, dass keine persönlich identifizierbaren Daten an Jacquard übermittelt werden.

Standardmäßig enthält der Current bestimmte PII-Attribute wie E-Mail und Adresse. Jacquard kann und wird keine PII erhalten. Daher ist es wichtig, dass Sie eine Anfrage an Ihr Braze-Konto Team stellen, um diese Funktion für alle an Jacquard weitergegebenen Daten zu deaktivieren.

### Schritt 4: Jacquard X Code Snippets 

Wenden Sie sich an Ihr Jacquard-Team, um die erforderlichen Code-Snippets zu erhalten.

Diese Snippets nutzen [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) und ziehen, nachdem sie in Ihren E-Mails platziert wurden, dynamisch Sprache und ein Tracking-Pixel ein, so dass Jacquard Ihre Sprache in Realtime mit Jacquard X optimieren kann.


