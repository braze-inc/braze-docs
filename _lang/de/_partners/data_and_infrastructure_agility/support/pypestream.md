---
nav_title: Pypestream
article_title: Pypestream
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Pypestream, einer umfassenden KI-Plattform, mit der Sie die digitale Interaktion mit Ihrer Marke verbessern können."
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com) ist eine umfassende KI-Plattform für Konversation, die patentiertes, umfassendes Cloud Messaging bietet, um Marken in "always-on" digitale Einheiten zu verwandeln. Mit Pypestream können Marken jetzt Omnichannel-Gespräche in großem Umfang mit jedem Kunden führen und dabei ein immersives Benutzererlebnis, fortschrittliche NLU-Funktionen und Echtzeit-Integrationen in Backend-Systeme nutzen.

Die Integration von Braze und Pypestream ermöglicht es Ihnen, den gesamten Kundenlebenszyklus nahtlos zu orchestrieren, von der ersten Kontaktaufnahme über ein Gesprächserlebnis bis hin zu Omnichannel-Follow-up(s) über intelligentes Retargeting. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Pypestream-Konto | Ein [Pypestream-Konto](https://www.pypestream.com/contact-us/) ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen.<br><br>Sobald Sie sich angemeldet haben, hilft Ihnen das Pypestream-Team bei der Einrichtung Ihrer speziellen Umgebung, damit Sie Ihre KI-Lösung für die Integration mit Braze aufbauen können. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die Partnerschaft zwischen Braze und Pypestream kann in Ihren Canvases genutzt werden, um gängige Anwendungsfälle zu realisieren:
* **Intelligentes Retargeting**: Sprechen Sie Nutzer mit Braze Canvas erneut an, nachdem sie sich mit Ihrer Marke unterhalten haben, indem Sie alle über Pypestream gesammelten Datenpunkte nutzen.
* **Dynamisches Targeting**: Sprechen Sie bestehende und potenzielle Kunden auf der Grundlage ihrer spezifischen Kohorten und Segmente an und bieten Sie ihnen über Pypestream maßgeschneiderte Gesprächserlebnisse.
* **Kontextbezogene Kundeneinblicke**: Nachdem ein Endbenutzer (bestehender oder potenzieller Kunde) Ihre Website besucht hat, kombinieren Sie die vom Pypestream Event Listener erfassten Webseiten-Tags mit den in Braze gespeicherten Kundendaten, um eine vollständig personalisierte und kontextbezogene Konversation zu ermöglichen.

## Integration

Pypestream nutzt eine serverlose Integrationsschicht, um kundenspezifische Integrationen in verschiedene Plattformen vorzunehmen. Diese Schicht wird als Schnittstelle zu Diensten oder Systemen verwendet, um die Datenanforderungen des zu erstellenden Konversationsflusses zu unterstützen. Diese Integrationen, die als Action Node-Integrationen bezeichnet werden, sind in der Regel in Python geschrieben und werden über die Pypestream-Plattform bereitgestellt. Nachdem ein Aktionsknoten instanziiert wurde, bietet er die Flexibilität, sich in einen beliebigen Braze-API-Endpunkt zu integrieren, und ermöglicht die Auswertung der Ergebnisse auf viele Arten. 

{% alert note %}
In diesem [Pypestream-Artikel](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) finden Sie eine Übersicht und Konfigurationsschritte für Pypestream-Aktionsknoten. Sie müssen Pypestream-Kunde sein, um Zugang zu dieser Dokumentation zu erhalten.
{% endalert %}

### Schritt 1: Endpunkt-Konfigurationen festlegen

Die primären Konfigurationswerte, wie z.B. die Braze REST-Endpunkt-URL und die Braze API-Schlüssel, sollten in der Datei `app.py` der Lösung festgelegt werden: 

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

### Schritt 2: Aktionsknoten-Vorlage entwickeln

Aktionsknoten nutzen die Umgebung, in der die Lösung eingesetzt wird, um mit den entsprechenden Braze-Endpunkten, die im vorherigen Schritt festgelegt wurden, zu interagieren. In diesem Schritt wird ein Aktionsknoten entwickelt, um bestimmte Braze-Endpunkte zu integrieren. Verwenden Sie die folgende Vorlage als Leitfaden für die Entwicklung der Integrationen: 

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
### Schritt 3: Aktualisieren Sie die Lösungskonzepte

Der letzte Schritt der Integration mit der Braze REST API besteht darin, die Abläufe im [Design Studio](https://platform.pypestream.com/design-studio/) von Pypestream so zu konfigurieren, dass sie den im vorherigen Schritt entwickelten Aktionsknoten verwenden. 

{% alert note %}
In diesem [Pypestream-Artikel](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) finden Sie einen Überblick darüber, wie Sie die Modi in Design Studio konfigurieren. Sie müssen Pypestream-Kunde sein, um Zugang zu dieser Dokumentation zu erhalten.
{% endalert %}

## Anwendungsfall Integration

Nachdem die Voraussetzungen erfüllt sind und eine Aktionsknotenstruktur erstellt wurde, hat der Entwickler eine leere Leinwand, auf der er bei der Interaktion mit den Braze-API-Endpunkten arbeiten kann. Dieses Beispiel zeigt die Schritte, die erforderlich sind, um einen Aktionsknoten in den Braze [`/user/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) zu integrieren [, insbesondere]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) um ein Benutzerprofil zu erstellen, um einen bestimmten Benutzer zu verfolgen, der einen Pypestream-Konversationsfluss betritt.

### Schritt 1: Sammeln Sie im Gespräch mit dem Benutzer Daten

Wenn ein Benutzer eine Pypestream-Sitzung aufruft, hängen die Einzelheiten der erfassten Daten vollständig vom jeweiligen Anwendungsfall ab. Um ein Benutzerprofil in Braze erstellen zu können, muss die Konversation die notwendigen Felder erfassen
die für den gewünschten Endpunkt erforderlich sind.

Wenn die Lösung beispielsweise die folgenden Informationen vom Benutzer während der Konversation für den Endpunkt Braze `/user/track` erfasst hat: 

* Vorname
* Nachname
* E-Mail-Adresse
* Geburtsdatum
* Stadt des Wohnsitzes
* Betriebssystem

Diese Daten können nun an die Braze-Plattform gesendet werden, um das Engagement dieses Benutzers zu verfolgen und ihn möglicherweise in Zukunft erneut anzusprechen. Sehen Sie sich die [Liste der Anwendungsfälle](#use-cases) an, um häufige Anwendungen zu sehen.

### Schritt 2: Daten in die Struktur der Aktionsknoten einfügen

Unter Verwendung derselben Struktur für die Entwicklung von Aktionsknoten können die vom Benutzer gesammelten Daten in den Aktionsknoten eingefügt werden, um über unseren `/user/track` Endpunkt an Braze gesendet zu werden.

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

### Schritt 3: Aktualisieren Sie die Lösungsströme, um sie bei Erfolg/Fehlschlag des Aktionsknotens umzuleiten.

Schließlich können Sie im Design jeder Lösung Benutzer zu Knoten weiterleiten, je nachdem, ob der Aufruf der Action Node API erfolgreich war. Wenn der Aktionsknoten eine Fehlermeldung erhält, sollte der Endbenutzer mit Vorsicht behandelt werden. 
