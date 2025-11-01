---
nav_title: Points de données
article_title: "Données d'aperçu"
page_order: 10
page_type: reference
description: "Cet article de référence indique quels sont les points de données chez Braze et comment vous pouvez être au courant de leur utilisation."
search_rank: 6
---

# Points de données

> Chez Braze, les données sont synonymes d'action : chaque donnée qui arrive dans Braze met à jour l'appartenance à un segment, peut déclencher et annuler un envoi de messages, est immédiatement disponible pour la personnalisation des messages, et bien plus encore. Les points de données vous aident à définir les informations les plus impactantes pour votre entreprise. En réfléchissant bien aux informations à suivre, vous vous assurez de cibler les données ayant le plus d'impact sur l'expérience de vos utilisateurs.

Les points de données sont basés sur les informations enregistrées par rapport aux profils utilisateurs. Vous trouverez une description plus détaillée de cette définition dans votre contrat avec Braze. Notre équipe de satisfaction client peut vous aider à recommander les meilleures pratiques en matière de données en fonction de vos besoins. 

## Définition

"Points de données" désigne une unité facturable d'utilisation des services Braze, mesurée par un début de session, une fin de session, un événement personnalisé ou un achat enregistré, ainsi que tout attribut défini sur un profil utilisateur final. Pour plus de clarté, chacune des données susmentionnées (telles que le début et la fin de la session, l'événement personnalisé ou l'achat enregistré, ainsi que tout attribut) définies dans le profil d'un utilisateur final à un moment donné est considérée comme un seul point de données.

Les données et les événements collectés par défaut par les Services Braze, y compris, par exemple, les jetons push, les informations sur les appareils et tous les événements de suivi de l'engagement des campagnes, tels que les ouvertures d'e-mail et les clics sur les notifications push, *ne* sont *pas* jetés en tant que points de données.

Reportez-vous à la section [Compte de consommation de](#consumption-count) cet article pour savoir quelles données sont prises en compte dans votre allocation de points de données.

## Visualisation de l'utilisation des points de données

Pour consulter votre utilisation des points de données, allez dans **Paramètres** > **Facturation** et sélectionnez l'onglet **Utilisation totale des points de données**.

Pour plus d'informations sur les composants du tableau de bord des points de données, reportez-vous à la section [Facturation]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**Ne gaspillez pas de points de données. Ne mettez à jour que les données qui changent !**<br><br>
Pour minimiser l'utilisation des points de données, nous vous recommandons de mettre en place un programme pour éviter d'envoyer les mêmes données immuables et de ne transmettre à Braze que des données nouvelles et pertinentes. Braze travaillera avec vous pour établir cette meilleure pratique lors de l'onboarding.
{% endalert %}

## Nombre de consommateurs

En somme, les points de données sont accumulés lorsque les données de profil d'un utilisateur sont mises à jour ou lorsqu'il effectue des actions spécifiques. Essentiellement, les points de données sont des comptages de chacun des `session starts`, `session ends`, `events` et `purchases` de votre utilisateur.

Vous trouverez une analyse de la manière dont Braze accumule les points de données dans les sections suivantes. Si vous avez des questions sur les nuances des points de données de Braze, votre gestionnaire de compte Braze peut y répondre.

Les actions suivantes n'enregistrent pas de points de données :
- Supprimer des utilisateurs de Braze
- Utilisation du contenu connecté dans les messages
- L'état de l'abonnement change globalement et autour des groupes d'abonnement
- Renommer les ID externes de vos utilisateurs par le biais d ['appels API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Blocage d'événements, d'attributs ou de propriétés d'événements

### Circonstances particulières

#### Tableaux

Un tableau est une collection ordonnée d'éléments stockés dans un attribut personnalisé. En termes de consommation, la mise à jour d'un tableau coûte un point de donnée par appel à l'API. Si vous ajoutez des valeurs à un tableau de manière incrémentielle, cela comptera comme un point de donnée par valeur. 

{% alert tip %}
Si vous définissez l'ensemble du tableau en une seule fois, cela comptera comme un seul point de données. À ce titre, les tableaux sont un excellent outil pour maintenir les profils utilisateurs à jour avec des informations pertinentes et réduire les coûts.
{% endalert %}

#### Attributs personnalisés imbriqués

Les attributs personnalisés imbriqués font référence à un objet qui définit un ensemble d'attributs en tant que propriété d'un autre attribut. Chaque clé de l'objet est considérée comme un point de donnée.

{% alert note %}
La mise à jour d'un objet d'attribut personnalisé sur `null` consomme également un point de données.
{% endalert %}

#### CSV

Les attributs personnalisés téléchargés via l'importation de fichiers CSV sont pris en compte dans vos points de données. Toutefois, les importations CSV à des fins de segmentation (importations effectuées avec `external_id`, `braze_id`, ou `user_alias_name` comme seul champ) n'enregistreront pas de points de données.

En outre, comme les changements d'état de l'abonnement n'enregistrent pas de points de données, la mise à jour des champs `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` dans votre fichier CSV n'entraînera pas de frais.

## Points de données

{% alert note %}
Les tableaux suivants sont donnés à titre d'exemple. Pour connaître les conventions d'appellation exactes, les majuscules et les valeurs acceptées pour certains champs, reportez-vous à la documentation relative à votre méthode d'ingestion.
{% endalert %}

{% tabs %}
{% tab Non-billable %}

#### Points de données non facturables (par défaut)

<div class="small_table"></div>

| Type de données | Point de données |
| --------- | ---------- |
| Données du profil | Pays |
| Données du profil | Langue |
| Données du profil | ID de l'utilisateur |
| Données du profil | Alias d'utilisateur |
| Appareils récents | Nombre d'appareils |
| Appareils récents | Dernière montre en date |
| Appareils récents | Version de l'application |
| Appareils récents | Appareil |
| Appareils récents | Appareil OS |
| Paramètres de contact | E-mail abonné |
| Paramètres de contact | Abonné en mode push |
| Paramètres de contact | Applications enregistrées pour le push |
| Paramètres de contact | Groupe d'abonnement |
| Campagnes reçues | Adresse e-mail |
| Attribution d'installation | Installer la source |
| Attribution d'installation | Campagne |
| Attribution d'installation | Groupe d'annonces |
| Attribution d'installation | Annonce |
| Divers | Numéro de compartiment aléatoire |
| Envois de canvas reçus | Envois de canvas reçus |
| L'envoi de messages | Tous les événements d'engagement (tels que les ouvertures, les clics, les impressions et les renvois) |
| Twitter | Suiveurs |
| Twitter | Suivant |
| Twitter | Nombre de tweets |
| Facebook | Aime |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Billable %}

#### Points de données facturables

{% alert important %}
L'ajout, la suppression ou la mise à jour des types de données suivants donne lieu à un point de données facturable.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Type de données | Point de données | Notes |
| --------- | ---------- | ----- |
| Données du profil | Prénom | |
| Données du profil | Nom de famille | |
| Données du profil | Adresse e-mail | |
| Données du profil | Genre | |
| Données du profil | Groupe d'âge | |
| Données du profil | Pays | En cas de collecte manuelle. Ne compte pas dans la consommation lorsqu'il est collecté automatiquement. |
| Données du profil | Ville | |
| Données du profil | Langue | En cas de collecte manuelle. Ne compte pas dans la consommation lorsqu'il est collecté automatiquement. |
| Données du profil | Localité la plus récente de l'appareil | |
| Données du profil | Fuseau horaire | |
| Données du profil | Date de naissance (DOB) | |
| Données du profil | Bio | |
| Données du profil | Numéro de téléphone | |
| Données d'utilisation de l'application | Début de la session | |
| Données d'utilisation de l'application | Fin de la session | |
| Attributs personnalisés | Tous les attributs personnalisés | |
| Événements personnalisés | Tous les événements personnalisés | |
| Propriétés d'événement personnalisé | Toutes les propriétés d'événements personnalisés | Les propriétés d'événement personnalisé activées pour la segmentation avec les filtres `X Custom Event Property in Y Days` ou `X Purchase Property in Y Days` sont toutes comptées comme des points de données distincts en plus du point de données compté par l'événement personnalisé lui-même.
| Achats | Tous les achats | |
| Propriétés d'achat | Toutes les propriétés d'achat | |
| Amplitude affectation de la cohorte | Toutes les missions | |
| Affectation de la cohorte Mixpanel | Toutes les missions | |
| Affectation de la cohorte Hightouch | Toutes les missions | |
| Appsflyer affectation de la cohorte | Toutes les missions | |
| Emplacement/localisation le plus récent | Tous les emplacements/localisations les plus récents | Le fait d'entrer ou de sortir d'une géorepérage n'enregistre pas de points de données, car les données de géorepérage ne sont pas stockées dans le profil utilisateur. Les géorepérages sont surveillés par les services d'emplacement/localisation d'Apple et de Google ; Braze n'est averti que lorsqu'un utilisateur déclenche un géorepérage. |
| Twitter | Nom d'utilisateur | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

