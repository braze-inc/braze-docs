---
nav_title: Pypestream
article_title: Pypestream
description: "Cet article de référence décrit le partenariat entre Braze et Pypestream, une plateforme d'IA conversationnelle complète qui vous permet d'améliorer l'engagement numérique avec votre marque."
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com) est une plateforme d'intelligence artificielle conversationnelle tout-en-un offrant une fonction d’envoi de messages cloud brevetée pour transformer les marques en entités numériques "toujours actives". Avec Pypestream, les marques peuvent désormais engager des conversations omnicanal à grande échelle avec chaque client tout en tirant parti d'une expérience utilisateur immersive, de capacités avancées de NLU et d'intégrations en temps réel aux systèmes backend.

_Cette intégration est maintenue par Pypestream._

## À propos de l'intégration

L'intégration de Braze et Pypestream vous permet d'orchestrer de façon fluide le cycle de vie complet du client, depuis le premier contact, en passant par une expérience conversationnelle, jusqu'au suivi omnicanal via un reciblage intelligent. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Pypestream | Un [compte Pypestream](https://www.pypestream.com/contact-us/) est requis pour profiter de ce partenariat.<br><br>Une fois abonné, l'équipe de Pypestream vous aidera à configurer votre environnement dédié pour commencer à créer votre solution d'intelligence artificielle conversationnelle à intégrer avec Braze. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Le partenariat entre Braze et Pypestream peut être utilisé dans vos canvas pour mettre en œuvre des cas d'utilisation courants tels que :
* **Reciblage intelligent**: Reciblez les utilisateurs avec Braze Canvas après leur engagement conversationnel avec votre marque en tirant parti de tous les points de données riches collectés via Pypestream.
* **Ciblage dynamique**: Contactez les clients existants et potentiels en fonction de leurs cohortes et segments spécifiques, en leur offrant des expériences conversationnelles personnalisées via Pypestream.
* **Informations contextuelles sur les clients**: Après qu'un utilisateur final (client existant ou potentiel) s'engage sur votre site web, combinez les tags de page web ingérés par le Pypestream Event Listener avec les données client stockées dans Braze pour fournir une interaction conversationnelle entièrement personnalisée et contextuelle.

## Intégration

Pypestream utilise une couche d'intégration sans serveur pour effectuer des intégrations personnalisées dans diverses plateformes. Cette couche est utilisée pour interfacer avec des services ou des systèmes afin de répondre aux exigences de données du flux conversationnel en cours de création. Ces intégrations, appelées intégrations de nœuds d'action, sont généralement écrites en Python et déployées à l'aide de la plateforme Pypestream. Une fois instancié, un nœud d'action est suffisamment flexible pour s'intégrer à n'importe quel endpoint d'API Braze et permet d'évaluer les résultats de plusieurs manières. 

{% alert note %}
Consultez cet [article Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) pour obtenir un aperçu et les étapes de configuration des nœuds d'action Pypestream. Vous devez être un client Pypestream pour accéder à cette documentation.
{% endalert %}

### Étape 1 : Définir les configurations d'endpoint

Les valeurs de configuration principales, telles que l'URL de l’endpoint REST de Braze et les clés API de Braze, doivent être définies dans le fichier `app.py` de la solution : 

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

### Étape 2 : Développer le modèle de nœud d'action

Les nœuds d'action tirent parti de l'environnement dans lequel la solution est déployée pour interagir, avec le(s) point(s) de terminaison Braze respectif(s) défini(s) à l'étape précédente. Cette étape développe un nœud d'action pour intégrer des endpoints Braze spécifiques. Utilisez le modèle suivant comme guide pour développer les intégrations : 

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
### Étape 3 : Mettre à jour les conceptions de solution

La dernière étape de l'intégration avec l'API REST de Braze consiste à configurer les flux dans le [Design Studio](https://platform.pypestream.com/design-studio/) de Pypestream pour utiliser le nœud d'action qui a été développé à l'étape précédente. 

{% alert note %}
Consultez cet [article Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) pour savoir comment configurer les modes dans Design Studio. Vous devez être un client Pypestream pour accéder à cette documentation.
{% endalert %}

## Cas d'utilisation de l'intégration

Une fois que les prérequis sont satisfaits et qu'une structure de nœuds d'action a été créée, le développeur dispose d'un canvas vierge qu’il peut utiliser pour interagir avec les endpoints de l'API Braze. Cet exemple montre les étapes nécessaires pour intégrer un nœud d'action dans le [`/user/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze - spécifiquement pour créer un profil utilisateur afin de suivre un utilisateur spécifique entrant dans un flux conversationnel Pypestream.

### Étape 1 : Collecter des données auprès de l'utilisateur dans la conversation

Lorsqu'un utilisateur entre dans une session Pypestream, les spécificités des données collectées dépendent entièrement du cas d'utilisation en cours. Pour pouvoir créer un profil utilisateur dans Braze, la conversation doit collecter les champs nécessaires
requis par l'endpoint souhaité.

Par exemple, si la solution a collecté les informations suivantes de l'utilisateur au cours de la conversation pour l’endpoint `/user/track` Braze : 

* Prénom
* Nom de famille
* Adresse e-mail
* Date de naissance
* Ville de résidence
* Système d'exploitation

Ces données peuvent maintenant être envoyées à la plateforme Braze pour suivre l'engagement de cet utilisateur avec la possibilité de le recibler potentiellement à l'avenir. Consultez la [liste des cas d'utilisation](#use-cases) pour voir les applications courantes.

### Étape 2 : Remplir les données dans la structure du nœud d'action

En tirant parti de la même structure pour développer des nœuds d'action, les données collectées auprès de l'utilisateur peuvent être intégrées dans le nœud d'action pour être envoyées à Braze via notre `/user/track` endpoint.

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

### Étape 3 : Mettre à jour les flux de solution pour rediriger en cas de succès/échec du nœud d'action

Enfin, dans la conception de chaque solution, vous pouvez diriger les utilisateurs vers des nœuds en fonction de la réussite de l'appel API du nœud d'action. Si le nœud d'action reçoit un message d'erreur, l'utilisateur final doit être traité avec soin. 

