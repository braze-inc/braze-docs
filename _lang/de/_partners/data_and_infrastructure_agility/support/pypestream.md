---
nav_title: Pypestream
article_title: Pypestream
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Pypestream, einer umfassenden KI-Plattform, mit der Sie das digitale Engagement Ihrer Marke verbessern können."
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com) ist eine umfassende KI-Plattform, die patentiertes, umfassendes Cloud Messaging anbietet, um Marken in "always-on" digitale Einheiten zu transformieren. Mit Pypestream können Marken jetzt Omnichannel-Gespräche in großem Umfang mit jedem Kunden führen und dabei ein immersives Nutzererlebnis, fortschrittliche NLU-Funktionen und Realtime-Integrationen in Backend-Systeme nutzen.

_Diese Integration wird von Pypestream gepflegt._

## Über die Integration

Die Integration von Braze und Pypestream erlaubt es Ihnen, den End-to-End Kundenlebenszyklus nahtlos zu orchestrieren, von der ersten Kontaktaufnahme über die Konversation bis hin zu Omnichannel-Follow-up(s) durch intelligentes Retargeting. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Pypestream-Konto | Ein [Pypestream-Konto](https://www.pypestream.com/contact-us/) ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen.<br><br>Sobald Sie Abonnent:innen sind, hilft Ihnen das Team von Pypestream bei der Einrichtung Ihrer speziellen Umgebung, damit Sie mit der Integration Ihrer KI-Lösung in Braze beginnen können. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die Partnerschaft zwischen Braze und Pypestream kann in Ihren Canvase genutzt werden, um gängige Anwendungsfälle zu realisieren:
* **Intelligentes Retargeting**: Retargeting von Nutzern:innen mit Braze-Canvas nach ihrem Engagement mit Ihrer Marke, indem Sie alle über Pypestream erfassten Datenpunkte nutzen.
* **Dynamisches Targeting**: Sprechen Sie bestehende und potenzielle Kunden auf der Grundlage ihrer spezifischen Kohorten und Segmente an und bedienen Sie sie mit maßgeschneiderten Konversationserlebnissen über Pypestream.
* **Kontextuelle Insights für Kund:innen**: Nachdem ein Endnutzer (bestehender oder potenzieller Kunde) sich auf Ihrer Website engagiert hat, kombinieren Sie die vom Pypestream Event Listener aufgenommenen Webseiten-Tags mit den in Braze gespeicherten Kundendaten, um eine vollständig personalisierte und kontextuelle Interaktion zu ermöglichen.

## Integration

Pypestream nutzt eine serverlose Integrationsebene, um angepasste Integrationen in verschiedene Plattformen durchzuführen. Diese Schicht dient als Schnittstelle zu Diensten oder Systemen, um die Datenanforderungen des zu erstellenden Konversationsflusses zu unterstützen. Diese Integrationen, die als Action Node-Integrationen bezeichnet werden, sind in der Regel in Python geschrieben und werden über die Pypestream-Plattform bereitgestellt. Nachdem ein Aktionsknoten instanziiert wurde, bietet er die Flexibilität, sich in jeden beliebigen Endpunkt der Braze APIs zu integrieren und erlaubt die Auswertung der Ergebnisse auf vielfältige Weise. 

{% alert note %}
In diesem [Pypestream-Artikel](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) finden Sie eine Übersicht und Konfigurationsschritte für Pypestream-Aktionsknoten. Sie müssen Kunde:in von Pypestream sein, um auf diese Dokumentation zugreifen zu können.
{% endalert %}

### Schritt 1: Endpunkt-Konfigurationen festlegen

Die primären Konfigurationswerte, wie die URL des Braze REST-Endpunkts und die Braze API-Schlüssel, sollten in der Datei `app.py` der Lösung festgelegt werden: 

```
import os

NAME = '{ CUSTOMER NAME }'
BOTS = []
CSV_BOTS = ['{ SOLUTION NAME }']
PATH = os.path.dirname(__file__)

PARAMS = {
    'sandbox': {
        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
    'prod': {

        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
}
```

### Schritt 2: Action Node Template entwickeln

Aktionsknoten nutzen die Umgebung, in der die Lösung eingesetzt wird, um mit den entsprechenden Endpunkten von Braze zu interagieren, die im vorherigen Schritt festgelegt wurden. In diesem Schritt wird ein Aktionsknoten entwickelt, um bestimmte Endpunkte von Braze zu integrieren. Verwenden Sie das folgende Template als Leitfaden für die Entwicklung der Integrationen: 

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Authorization": "{YOUR-REST-API-KEY}"
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ]
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```
### Schritt 3: Aktualisieren Sie die Entwürfe der Lösungen

Der letzte Schritt der Integration mit der Braze REST API besteht darin, die Abläufe im [Design Studio](https://platform.pypestream.com/design-studio/) von Pypestream so zu konfigurieren, dass sie den Aktionsknoten verwenden, der im vorherigen Schritt entwickelt wurde. 

{% alert note %}
In diesem [Pypestream-Artikel](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) finden Sie eine Übersicht darüber, wie Sie die Modi in Design Studio konfigurieren können. Sie müssen Kunde:in von Pypestream sein, um auf diese Dokumentation zugreifen zu können.
{% endalert %}

## Integration Anwendungsfall

Nachdem die Voraussetzungen erfüllt sind und eine Aktionsknotenstruktur erstellt wurde, steht dem Entwickler:in ein leeres Canvas zur Verfügung, von dem aus er mit den Endpunkten der Braze API arbeiten kann. Dieses Beispiel zeigt die Schritte, die für die Integration eines Aktionsknotens in den [`/user/track`Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) von Braze  erforderlich sind, insbesondere für die Erstellung eines Nutzerprofils zum Tracking eines bestimmten Nutzers:innen, der einen Pypestream-Konversationsfluss betritt.

### Schritt 1: Sammeln Sie Daten vom Nutzer:innen im Gespräch

Wenn ein Nutzer:in eine Pypestream-Sitzung eintritt, hängt die Art der erfassten Daten ganz vom jeweiligen Anwendungsfall ab. Um ein Nutzerprofil innerhalb von Braze erstellen zu können, muss die Konversation die erforderlichen Felder erfassen
die für den gewünschten Endpunkt erforderlich sind.

Wenn die Lösung beispielsweise während der Konversation für den Endpunkt Braze `/user/track` die folgenden Informationen vom Nutzer:innen gesammelt hat: 

* Vorname
* Nachname
* E-Mail-Adresse
* Geburtsdatum
* Ort des Wohnsitzes
* Betriebssystem

Diese Daten können nun an die Braze-Plattform gesendet werden, um das Engagement dieser Nutzer:innen zu verfolgen und sie möglicherweise in Zukunft zu retarchen. Sehen Sie sich die [Liste der Anwendungsfälle](#use-cases) an, um häufige Anwendungen zu sehen.

### Schritt 2: Daten in die Aktionsknotenstruktur einfügen

Indem Sie dieselbe Struktur für die Entwicklung von Aktionsknoten nutzen, können die vom Nutzer:in gesammelten Daten in den Aktionsknoten eingefügt werden, um sie über unseren `/user/track` Endpunkt an Braze zu senden.

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ],
        "partner" : 'pypestream'
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    "first_name": "{ FIRST_NAME }",
                    "last_name": "{ LAST_NAME }",
                    "email": "{ EMAIL_ADDRESS }",
                    "dob": "{ DATE_OF_BIRTH }",
                    "home_city": "{ CITY_OF_RESIDENCE }",
                    "operating_system": "{ OPERATING_SYSTEM }" #custom attributes can be added here as well
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [{
                    "external_id": "{ USER_ID }",
                    "name": "{ NAME_OF_EVENT }",
                    "time": "{ EVENT_TIME }"
                }],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```

### Schritt 3: Update der Lösungsabläufe zur Umleitung bei Erfolg/Fehlschlag des Aktionsknotens

Schließlich können Sie im Design jeder Lösung Nutzer:innen zu Knoten weiterleiten, je nachdem, ob der Aufruf der Action Node API erfolgreich war. Wenn der Aktionsknoten eine Fehlermeldung erhält, sollte der Endnutzer:in mit Vorsicht behandelt werden. 

