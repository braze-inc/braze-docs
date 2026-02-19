---
nav_title: StackAdapt
article_title: StackAdapt
description: "Cet article de référence présente le partenariat entre Braze et StackAdapt."
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [StackAdapt](https://www.stackadapt.com/) est la principale plateforme de marketing alimentée par l'intelligence artificielle utilisée par les spécialistes du marketing numérique pour diffuser des publicités ciblées axées sur la performance.

_Cette intégration est maintenue par StackAdapt._

L'intégration de Braze et de StackAdapt vous permet de synchroniser les données de profil utilisateur de Braze dans le Data Hub de StackAdapt. En connectant les deux plateformes, vous pouvez créer une vue unifiée de vos clients et activer les données first-party pour améliorer les performances publicitaires.

## Cas d’utilisation

- **Réengagez les utilisateurs qui n'ont plus donné signe de vie :** Identifiez les utilisateurs qui se sont désabonnés des listes de marketing par e-mail dans Braze et ciblez-les avec des publicités programmatiques sur StackAdapt pour les réengager via un canal différent.
- **Créez des expériences multicanaux :** Prolongez le parcours de l'utilisateur au-delà de l'e-mail. Par exemple, si un utilisateur clique sur une campagne e-mail dans Braze, vous pouvez utiliser StackAdapt pour lui montrer une publicité programmatique complémentaire, renforçant le message et incitant à une action supplémentaire.
- **Personnalisation à grande échelle :** Exploitez les points de données granulaires de Braze, tels que la " ville d'origine " ou la " langue ", pour diffuser des publicités et des e-mails très pertinents, localisés et spécifiques à la langue.
- **Approfondissez la compréhension de votre audience :** En synchronisant les attributs de profil, vous pouvez créer des segments d'audience plus riches dans StackAdapt, ce qui permet un ciblage plus précis et des expériences publicitaires personnalisées.

## Conditions préalables

| Condition | Description         |
| ----------- | ------------------- |
| **Compte StackAdapt**  | Vous avez besoin d'un compte StackAdapt actif avec des autorisations pour gérer les intégrations Data Hub. |
| **Clé d'API REST Braze**  | Une clé API REST de Braze avec les autorisations suivantes : <br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API.** |
| **Endpoint REST Braze** | [L'URL de votre endpoint REST.](https://www.braze.com/docs/api/basics/#endpoints) Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fonctionnement

Le StackAdapt Data Hub se connecte directement à votre compte Braze pour extraire les attributs du profil utilisateur. Vous pouvez ainsi exploiter les données de vos clients Braze directement dans StackAdapt pour une segmentation et une activation avancées de l'audience.

### Flux de données

1. StackAdapt initie une connexion sécurisée à votre instance Braze en utilisant les identifiants API fournis.
2. StackAdapt récupère les données du profil utilisateur et plus particulièrement les propriétés que vous avez sélectionnées et mappées.
3. Les données sont normalisées et ingérées dans votre StackAdapt Data Hub, devenant ainsi disponibles pour la segmentation et l'utilisation dans vos campagnes.
4. L'intégration permet des synchronisations de données planifiées (par exemple, quotidiennement) pour que vos audiences StackAdapt soient à jour avec les dernières données de profil de Braze.

## Champs synchronisés

StackAdapt peut synchroniser une variété de champs du profil Braze, y compris, mais sans s'y limiter :

{% tabs local %}
{% tab Standard attributes %}
- E-mail
- Date de naissance
- Prénom
- Nom de famille
- Téléphone
- Ville d’origine
- Pays
- Genre
- Fuseau horaire
- Créé à
- ID externe
- Langue 

{% endtab %}
{% tab Custom attributes %}
Attributs spécifiques à votre application ou à votre entreprise, définis en fonction de vos besoins spécifiques.

{% endtab %}
{% tab Attribution data %}
- Annonce attribuée
- Groupe d'annonces attribué
- Campagne attribuée
- Source attribuée

{% endtab %}
{% tab Subscription status %}
- État d’abonnement aux e-mails
- État d’abonnement aux notifications push 

Il est crucial de mapper avec précision les champs de Braze qui reflètent le consentement de l'utilisateur pour les communications marketing (par exemple, le statut de l'abonnement aux e-mails) afin que vos efforts publicitaires restent conformes aux préférences de l'utilisateur et aux réglementations en matière de protection de la vie privée.

{% endtab %}
{% endtabs %}

## Configuration de l'intégration

Suivez ces étapes pour importer vos profils utilisateurs Braze :

1. Connectez-vous à votre compte StackAdapt.
2. Dans le menu de navigation, sélectionnez **Data Hub**.
3. Sélectionnez **Importer des profils**, puis sélectionnez **Braze** dans la liste des intégrations disponibles.
4. Saisissez vos identifiants API Braze lorsque vous y êtes invité.
- **Clé de l'API REST de Braze :** Emplacement/localisation dans Braze en allant dans **Paramètres** > **Clés API.** En tant que meilleure pratique de sécurité, nous vous recommandons de créer une clé API dédiée à votre intégration StackAdapt.
- **Clé d'application Braze :** Situé dans Braze en allant dans **Paramètres** > **Clés API** ou **Gérer les apps**.
- **URL du point d'extrémité REST de Braze :** L'URL de base de votre instance Braze (par exemple, ```https://rest.iad-01.braze.com```).
5. Sélectionnez **Connecter** pour vérifier les informations d'identification.

![Connexion Braze dans StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6\. Choisissez votre connexion et sélectionnez votre annonceur StackAdapt.
7\. Configurez vos **mappages de propriétés**. Examinez et confirmez les mappages par défaut et les propriétés présélectionnées proposés par StackAdapt.
8\. (Facultatif) Si vous souhaitez importer des propriétés supplémentaires, sélectionnez-les en cochant les cases correspondantes et indiquez si elles contiennent des IIP et leur type de données.

![Connexion Braze dans StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9\. Ajoutez vos profils à une **liste** ou créez-en une nouvelle afin de pouvoir regrouper et segmenter vos profils.
10\. Sélectionnez **Activer l'intégration** pour lancer la synchronisation initiale des données.

## Considérations

- **Importation d'événements et de propriétés personnalisés :** Cette fonctionnalité n'est pas encore prise en charge.
- **Temps de latence des données :** L'importation de toutes les données du profil utilisateur peut prendre jusqu'à 24 heures.
- **Gestion du consentement :** Confirmez que vos pratiques de collecte de données dans Braze s'alignent sur les réglementations en matière de confidentialité et que vous disposez du consentement nécessaire pour utiliser les données des clients à des fins publicitaires. StackAdapt s'appuie sur le statut de consentement transmis par vos systèmes sources.
- **Cohérence des attributs :** Pour maximiser l'efficacité de vos données, maintenez une cohérence dans la façon dont les attributs sont nommés et renseignés dans Braze avant de les synchroniser avec StackAdapt.
