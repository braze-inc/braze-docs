---
nav_title: Pypestream
article_title: Pypestream
page_order: 5
description: "Cet article décrit le partenariat entre Braze et Pypestream, une plate-forme IA pleine de stack qui vous permet d'améliorer l'engagement numérique avec votre marque."
alias: /fr/partners/pypestream/
page_type: partenaire
search_tag: Partenaire
---

# Pypestream

> [Pypestream](https://www.pypestream.com) est une plate-forme IA pleine de piles et conversationnelle offrant une messagerie nuageuse brevetée et tout-en-un pour transformer les marques en entités numériques « permanentes ». Avec Pypestream, les marques peuvent maintenant engager des conversations omnichales à l'échelle avec chaque client tout en tirant parti d'une expérience utilisateur immersive, des capacités avancées en NLU et des intégrations en temps réel aux systèmes backend.

L'intégration de Braze et de Pypestream vous permet d'orchestrer de façon transparente le cycle de vie du client de bout en bout à partir de la portée initiale, routé dans une expérience de conversation, et par le biais de l'omnicanal suivre(s) par le biais d'un recul intelligent.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Pypestream               | Un [compte Pypestream](https://www.pypestream.com/contact-us/) est requis pour profiter de ce partenariat.<br><br>Une fois abonné, L'équipe de Pypestream vous aidera à mettre en place votre environnement dédié pour commencer à construire votre solution IA conversationnelle à intégrer avec Braze. |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__                                                                                                         |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance]({site.baseurl}}/api/basics/?redirected=true).                                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d'utilisation

Le partenariat Braze et Pypestream peut être utilisé dans vos Canvases pour obtenir des cas d'utilisation communs tels que:
* **Repositionnement intelligent**: Retarget utilisateurs avec Braze Canvas après leur engagement conversationnel avec votre marque en exploitant tous les points de données riches collectés via Pypestream.
* **Ciblage dynamique**: Atteignez les clients existants et potentiels en fonction de leurs cohortes et segments spécifiques, les servir avec des expériences de conversation sur mesure via Pypestream.
* **Aperçus du client contextuel**: Une fois qu'un utilisateur final (client existant ou éventuel) s'engage sur votre site Web, combinez les balises de pages Web ingérées à partir du Pypestream Event Listener avec les données des clients stockées dans Braze pour fournir une interaction de conversation entièrement personnalisée et contextuelle.

## Intégration

Pypestream tire parti d'une couche d'intégration sans serveur pour effectuer des intégrations personnalisées sur différentes plateformes. Cette couche est utilisée pour interfacer avec les services ou les systèmes pour supporter les besoins de données du flux de conversation en cours de construction. Ces intégrations, appelées les Intégrations de nœuds d'action, sont généralement écrites en Python et déployées à l'aide de la plate-forme Pypestream. Une fois qu'un nœud d'action est instancié, il fournit la flexibilité d'intégrer dans n'importe quel point de terminaison de l'API Braze et permet d'évaluer les résultats de plusieurs façons.

{% alert note %}
Visitez cet [article Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) pour une vue d'ensemble et des étapes de configuration des nœuds d'action Pypestream. Vous devez être un client Pypestream pour accéder à cette documentation.
{% endalert %}

### Étape 1 : Définir les configurations de point de terminaison

Les valeurs de configuration principales, telles que **Braze REST Endpoint URL** et les **clés API Braze**, doit être défini dans l'application `. y` fichier de la solution :

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

### Étape 2 : Développer un modèle de noeud d'action

Les nœuds d'action tirent parti de l'environnement avec lequel la solution est déployée pour interagir, avec le(s) terminaux(s) respectifs de Braze définis à l'étape précédente. Cette étape développe un nœud d'action pour intégrer des points de terminaison spécifiques de Braze. Utilisez le modèle suivant comme guide pour développer les intégrations :

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __ ___
   / __ \ \/ __ \/ ____/ ___/_ __/ __ __/ __ \/ ____/ __ / ____/ | / |/
  / /_/ \ / /_/ __/ \__ \ / / / / / __/ / / / / / | / /|_/
 / ____/ / / ____/ / ____/ / ___ ___/ // / / _, _/ /___/ ___ |/ / / /
/_/ /_//_____//____//////_/ /_/ |_/_____/_/ |_/_/ /_/ /_/
Script de nœud d'action pour l'intégration de Braze

paramètres
----------
requête POST au point d'extrémité de la piste de l'utilisateur (utilisateurs/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "utilisateurs/piste",
  "req_method": "POST",
  "req_headers": {
    "Authorization": "{YOUR-REST-API-KEY}"
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributs": [{
                "external_id": "{HOLDER_EMAIL}",
...
        }],
        "événements": [
...
        ]
}

Retourne
-------
Crée et/ou met à jour les détails de l'utilisateur dans le tableau de bord de Braze

'''
demandes d'importation
depuis .. Importer l'app

classe BrazeExemple:
    def execute(self, log, payload=Aucun, context=Aucun) :
        essayer :
            # initialiser les variables de payload
            app_params = app. ARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    # inclure les détails de l'utilisateur add'tl dans cette section
                    # se référer à la documentation de l'API Braze pour le point de terminaison de l'API REST de l'utilisateur pour plus de détails
                }],
                "événements": [],
                "partenaire" : 'pypestream'
            }
            req_url = '{}/{}'. ormat(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests. ost(req_url,
                                params=req_params,
                                en-têtes=req_headers)

            log('Réponse API BrazeExample : {}'. ormat(resp.text))

            si resp. tatus_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'. ormat(err))

        retour {'success': 'error'}
```
### Étape 3 : Mettre à jour les conceptions de la solution

La dernière étape de l’intégration avec l’API REST de Braze consiste à configurer les flux dans le [Design Studio](https://platform.pypestream.com/design-studio/) de Pypestream pour utiliser le nœud d’action qui a été développé à l’étape précédente.

{% alert note %}
Visitez cet article [Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) pour un aperçu de la façon de configurer les modes dans Design Studio. Vous devez être un client Pypestream pour accéder à cette documentation.
{% endalert %}

## Intégration d'exemple

Une fois que les pré-requis sont remplis, et qu'une structure de nœud d'action a été créée, le développeur a une Canvas vierge à partir de laquelle il peut travailler lorsqu'il interagit avec les points de terminaison de l'API Braze. Cet exemple montre les étapes requises pour intégrer un nœud d'action dans le point de terminaison de la trace de l'utilisateur [Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) - spécifiquement pour créer un profil utilisateur pour suivre un utilisateur spécifique entrant dans un flux de conversation Pypestream.

### Étape 1 : Récupérer les données de l'utilisateur dans la conversation

Lorsqu'un utilisateur entre dans une session de Pypestream, les spécificités des données collectées dépendent entièrement du cas d'utilisation. Pour pouvoir créer un profil utilisateur au Brésil, la conversation doit collecter les champs nécessaires requis par le point de terminaison désiré.

Par exemple, si la solution a recueilli les informations suivantes de l'utilisateur pendant la conversation pour le point de terminaison de suivi de l'utilisateur []({{site.baseurl}}/api/endpoints/user_data/post_user_track/):

* Prénom
* Nom de famille
* Adresse e-mail
* Date de naissance
* Ville de résidence
* Système d'exploitation

Ces données peuvent maintenant être envoyées à la plateforme Braze pour suivre l'engagement de cet utilisateur avec la possibilité de les recibler à l'avenir. Consultez la [liste de cas d'utilisation](#use-cases) pour voir les applications courantes.

### Étape 2 : Remplir les données dans la structure des noeuds d'action

Levier de la même structure pour le développement des nœuds d'action comme décrit ci-dessus, les données collectées auprès de l'utilisateur peuvent être remplies dans le nœud d'action à envoyer à Braze via le [point de terminaison de la piste utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __ ___
   / __ \ \/ __ \/ ____/ ___/_ __/ __ __/ __ \/ ____/ __ / ____/ | / |/
  / /_/ \ / /_/ __/ \__ \ / / / / / __/ / / / / / | / /|_/
 / ____/ / / ____/ / ____/ / ___ ___/ // / / _, _/ /___/ ___ |/ / / /
/_/ /_//_____//____//////_/ /_/ |_/_____/_/ |_/_/ /_/ /_/
Script de nœud d'action pour l'intégration de Braze

paramètres
----------
requête POST au point d'extrémité de la piste de l'utilisateur (utilisateurs/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "utilisateurs/piste",
  "req_method": "POST",
  "req_headers": {
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributs": [{
                "external_id": "{HOLDER_EMAIL}",
...
        }],
        "événements": [
...
        ],
        "partenaire" : 'pypestream'
}

Retourne
-------
Crée et/ou met à jour les détails de l'utilisateur dans le tableau de bord de Braze

'''
demandes d'importation
de .. Importer l'app

classe BrazeExemple:
    def execute(self, log, payload=Aucun, context=Aucun) :
        essayer :
            # initialiser les variables de payload
            app_params = app. ARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    "prénom": "{ FIRST_NAME }",
                    "nom_de_famille": "{ LAST_NAME }",
                    "email": "{ EMAIL_ADDRESS }",
                    "dob": "{ DATE_OF_BIRTH }",
                    "home_city": "{ CITY_OF_RESIDENCE }",
                    "operating_system": "{ OPERATING_SYSTEM }" #des attributs personnalisés peuvent être ajoutés ici aussi
                    # inclure les détails de l'utilisateur add'tl dans cette section
                    # se référer à la documentation de l'API Braze pour le point de terminaison de l'User Track REST API REST pour plus de détails
                }],
                "événements": [{
                    "external_id": "{ USER_ID }",
                    "nom": "{ NAME_OF_EVENT }",
                    "temps": "{ EVENT_TIME }"
                }],
                "partenaire" : 'pypestream'
            }
            req_url = '{}/{}'. ormat(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests. ost(req_url,
                                params=req_params,
                                en-têtes=req_headers)

            log('Réponse API BrazeExample : {}'. ormat(resp.text))

            si resp. tatus_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'. ormat(err))

        retour {'success': 'error'}
```

### Étape 3 : Mettre à jour les flux de solution pour les rediriger en cas de succès/défaillance du noeud d'action

Enfin, dans la conception de chaque solution, vous pouvez acheminer les utilisateurs vers des nœuds en fonction de la réussite de l'appel à l'API du noeud d'action. Si le noeud de l'action reçoit un message d'erreur, l'utilisateur final doit être traité avec précaution. 
