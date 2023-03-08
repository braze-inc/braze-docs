---
nav_title: Pypestream
article_title: Pypestream
page_order: 5
description: "Cet article présente le partenariat entre Braze et Pypestream, une plateforme d’IA conversationnelle complète qui vous permet d’améliorer l’engagement numérique avec votre marque."
alias: /partners/pypestream/
page_type: partner
search_tag: Partenaire

---

# Pypestream

> [Pypestream](https://www.pypestream.com) est une plateforme complète d’IA conversationnelle comprenant une messagerie cloud brevetée et tout-en-un qui transforme les marques en entités numériques toujours présentes en ligne. Avec Pypestream, les marques peuvent désormais mener des conversations omnicanales à grande échelle avec chacun de leurs clients, tout en tirant parti d’une expérience utilisateur immersive, de capacités avancées de compréhension du langage naturel et d’intégrations en temps réel aux systèmes back-end.

L’intégration de Braze et de Pypestream vous permet de gérer de manière harmonieuse le cycle de vie de bout en bout du client, depuis la première interaction jusqu’aux expériences conversationnelles, en passant par les suivis omnicanaux via des reciblages intelligents. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Pypestream | Un compte [Pypestream](https://www.pypestream.com/contact-us/) est requis pour profiter de ce partenariat.<br><br>Une fois inscrit, l’équipe Pypestream vous aidera à configurer votre environnement dédié pour commencer à concevoir votre solution d’IA conversationnelle et l’intégrer à Braze. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance]({site.baseurl}}/api/basics/?redirected=true). |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Le partenariat entre Braze et Pypestream peut être utilisé dans vos Canvas pour des exemples d’utilisation courants comme :
* **Reciblage intelligent** : Reciblez des utilisateurs avec Braze Canvas après leur engagement conversationnel avec votre marque en tirant parti de tous les points de données enrichis collectés via Pypestream.
* **Ciblage dynamique** : Contactez les clients existants et potentiels en fonction de leurs cohortes et segments pour leur offrir des expériences conversationnelles personnalisées via Pypestream.
* **Informations contextuelles sur les clients** : Lorsqu’un utilisateur final (client existant ou potentiel) interagit avec votre site Web, combinez les balises Web acquises sur Pypestream Event Listener avec les données client stockées dans Braze pour fournir des interactions conversationnelles personnalisées et contextuelles.

## Intégration

Pypestream exploite une couche d’intégration sans serveur qui permet d’effectuer des intégrations personnalisées sur diverses plateformes. Cette couche est utilisée pour interagir avec des services ou systèmes afin de soutenir les exigences en matière de données du flux conversationnel en cours d’élaboration. Ces intégrations, appelées Action Node Integrations, sont généralement écrites en langage Python et déployées à l’aide de la plateforme Pypestream. Une fois qu’un nœud d’action est instancié, il peut intégrer n’importe quel endpoint d’API Braze et permet d’évaluer les résultats de plusieurs manières. 

{% alert note %}
Consultez cet [article de Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) pour obtenir un aperçu des nœuds d’action Pypestream et les étapes de configuration. Vous devez être un client Pypestream pour accéder à cette documentation.
{% endalert %}

### Étape 1 : Définir les configurations d’endpoint

Les valeurs de configuration principales, telles que **URL d’endpoint REST Braze** et les **clés API Braze**, doivent être définies dans le fichier `app.py` de la solution : 

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

### Étape 2 : Développer un modèle de nœud d’action

Les nœuds d’action tirent parti de l’environnement dans lequel la solution est déployée pour interagir avec le ou les endpoints Braze respectifs qui ont été configurés à l’étape précédente. Cette étape développe un nœud d’action pour intégrer des endpoints spécifiques de Braze. Utilisez le modèle suivant pour vous aider à développer des intégrations : 

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
### Étape 3 : Mettre à jour les conceptions de solution

L’étape finale de l’intégration avec l’API REST de Braze consiste à configurer des flux dans le [Design Studio](https://platform.pypestream.com/design-studio/) de Pypestream pour utiliser le nœud d’action développé à l’étape précédente. 

{% alert note %}
Consultez cet [article de Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) pour obtenir un aperçu de la configuration des modes dans Design Studio. Vous devez être un client Pypestream pour accéder à cette documentation.
{% endalert %}

## Exemple d’intégration

Une fois les conditions préalables remplies et une structure de nœud d’action créée, les développeurs peuvent travailler sur un Canvas vierge lorsqu’ils interagissent avec les endpoints d’API Braze. Cet exemple montre les étapes requises pour intégrer un nœud d’action à l’[endpoint user track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze et plus particulièrement pour créer un profil utilisateur afin de suivre un utilisateur spécifique entrant dans un flux conversationnel Pypestream.

### Étape 1 : Collecter des données utilisateur pendant une conversation

Lorsqu’un utilisateur rejoint une session Pypestream, les données recueillies dépendent entièrement du cas d’utilisation. Pour pouvoir créer un profil utilisateur dans Braze, la conversation doit collecter les champs 
nécessaires pour l’endpoint souhaité.

Par exemple, si la solution a recueilli les informations ci-dessous auprès de l’utilisateur pendant la conversation pour l’[endpoint user track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) : 

* Prénom
* Nom
* Adresse e-mail
* Date de naissance
* Ville de résidence
* Système d’exploitation

Ces données peuvent maintenant être envoyées à la plateforme Braze pour suivre l’engagement de cet utilisateur et le recibler ultérieurement. Consultez la [liste des cas d’utilisation](#use-cases) pour découvrir les applications courantes.

### Étape 2 : Renseigner les données dans la structure du nœud d’action

Tirant parti de la même structure pour développer des nœuds d’action, les données collectées auprès de l’utilisateur peuvent être renseignées dans le nœud d’action à envoyer à Braze via l’[endpoint user track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

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

### Étape 3 : Mettre à jour les flux de la solution pour les rediriger en fonction de la réussite/échec du nœud d’action

Enfin, dans la conception de chaque solution, vous pouvez acheminer des utilisateurs vers des nœuds si l’appel API du nœud d’action a été effectué avec succès. Si le nœud d’action reçoit un message d’erreur, l’utilisateur final doit être traité avec précaution. 
