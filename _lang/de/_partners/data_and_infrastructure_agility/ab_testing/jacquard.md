---
nav_title: Jacquard
article_title: Jacquard
page_order: 1
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Jacquard Dynamic Optimisation, die Braze Currents und Connected Content nutzt, um Click-Tracking-Informationen von Ihren Abonnenten über Webhooks zu sammeln. Jacquard verknüpft diese Ereignisse dann mit Ihren Sprachvarianten zur Sprachoptimierung in Echtzeit."
page_type: partner
search_tag: Partner
---

# Dynamische Jacquard-Optimierung

> [Jacquard][1] vereint künstliche Intelligenz, Computerlinguistik und den Geist der Kundenzentrierung, um die Markensprache in großem Umfang über alle Kanäle hinweg zu verbreiten, die auf Ihre Markensprache zugeschnitten sind.

Die dynamische Optimierung, die von Jacquard X unterstützt wird, nutzt Braze Currents und Connected Content, um über Webhooks Klick-Tracking-Informationen von Ihren Abonnenten zu sammeln. Jacquard verknüpft diese Ereignisse dann mit Ihren Sprachvarianten zur Sprachoptimierung in Echtzeit. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Jacquard-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Jacquard-Konto][1]. |
| Jacquard Connect Server-Token | Eine lange Zeichenfolge, die als Passwort für Ihre Braze-Kampagne dient, um auf Ihre Jacquard-Sprache zuzugreifen.<br><br>Sie können dies bei Ihrem Jacquard-Kundenbetreuer anfordern, falls Sie es nicht bereits erhalten haben. |
| Currents | Um Daten nach Currents exportieren zu können, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Jacquard-Zugangsdaten für Amazon S3 anfordern

Sie benötigen Jacquard, um einen speziellen Amazon S3-Bucket einzurichten, der Ihre Click-Tracking-Ereignisse von Braze empfängt. Wenden Sie sich an Ihren Jacquard Customer Success Manager, um diesen Prozess zu starten. Wenn der Bucket erstellt wird, erhalten Sie eindeutige Anmeldedaten, um Ihren Strom zu erstellen. 

### Schritt 2: Aktuell erstellen

1. Wählen Sie in Braze **Currents > Create New Current > Amazon S3 Data Export**. 
2. Als Nächstes benennen Sie Ihren Strom und geben eine Kontakt-E-Mail ein.
3. Fügen Sie Ihre Jacquard AWS-Zugangsschlüssel-ID und Ihren geheimen Zugangsschlüssel in das Feld Anmeldeinformationen ein. Fügen Sie dann "phrasee-braze-currents-exports" als Namen des AWS S3-Buckets hinzu. 
4. Als letztes fügen Sie den AWS S3 Bucket-Ordner hinzu, den Sie von Ihrem Jacquard Customer Success Manager erhalten haben. Es wird wahrscheinlich der Name Ihres Unternehmens sein.
5. Aktivieren Sie unter **Allgemeine Einstellungen** das Kontrollkästchen "Ereignisse von anonymen Benutzern einbeziehen", und aktivieren Sie unter **Engagement-Ereignisse verwalten** "E-Mail-Klick".
6. Wenn Sie fertig sind, wählen Sie **Aktuelles starten**.

### Schritt 3: Antrag auf Entfernung persönlich identifizierbarer Informationen (PII).

Wenden Sie sich dann an Ihr Braze-Kundenteam, um sicherzustellen, dass keine personenbezogenen Daten an Jacquard übermittelt werden.

In der Standardeinstellung enthält Current bestimmte PII-Attribute wie E-Mail und Adresse. Jacquard kann und wird keine personenbezogenen Daten erhalten. Daher ist es wichtig, dass Sie bei Ihrem Braze-Kundenteam beantragen, dass diese Funktion für alle an Jacquard weitergeleiteten Ereignisdaten deaktiviert wird.

### Schritt 4: Jacquard X Codeschnipsel 

Wenden Sie sich an Ihr Jacquard-Kundenteam, um die erforderlichen Codeschnipsel zu erhalten.

Diese Snippets nutzen [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) und ziehen, nachdem sie in Ihren E-Mails platziert wurden, dynamisch die Sprache und ein Tracking-Pixel ein, so dass Jacquard Ihre Sprache in Echtzeit mit Jacquard X optimieren kann.


[1]: https://www.jacquard.com/
[3]: mailto:awesome@phrasee.co