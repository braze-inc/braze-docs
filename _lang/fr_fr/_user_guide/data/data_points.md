---
nav_title: Points de données
article_title: Aperçu des points de données
page_order: 0
page_type: reference
description: "Cet article de référence décrit les points de données chez Braze et leur utilisation."
search_rank: 6
---

# Points de données

> Chez Braze, les données signifient : chaque élément de données arrivant chez Braze met à jour l’adhésion du segment, peut déclencher et annuler des envois de messages, est immédiatement disponible pour la personnalisation des envois de messages et plus encore. Les points de données vous aident à définir les informations les plus importantes pour votre entreprise. En tenant compte de l’information à suivre, vous devez cibler les données les plus à fort impact pour l’expérience de vos utilisateurs.

De ce fait, les points de données sont la façon de Braze de définir une structure de facturation et de tarification, en fonction des informations enregistrées par rapport aux profils utilisateur. Notre équipe de support client peut vous aider à recommander les bonnes pratiques en matière de donnée pour répondre à vos besoins. Vous trouverez une répartition plus détaillée de cette définition dans votre contrat Braze. 

## Définition

Les « Points de données » font référence à une unité facturable d’utilisation des Services Braze, mesurée par un début de session, une fin de session, un événement personnalisé ou un achat enregistré, ainsi que tout attribut défini sur un profil d’utilisateur final. Pour plus de clarté, chacune des données mentionnées ci-dessus (telles que le début de session, la fin de session, l'événement personnalisé ou l'achat enregistré, ainsi que tout attribut) définies dans le profil d'un utilisateur final à un moment donné sera comptée comme un seul point de données.

Les données et les événements collectés par défaut par les services Braze, y compris, par exemple, les jetons push, les informations sur les appareils et tous les événements de suivi de l'engagement des campagnes, tels que les ouvertures d'e-mails et les clics sur les notifications push, ne sont *pas* comptés comme des points de données.

Voir la section [Nombre de consommations](#consumption-count) de cet article pour comprendre quelles données comptent pour votre allocation de points de données.

## Visualisation de l'utilisation des points de données

Pour voir votre utilisation des points de données, allez dans **Paramètres** > **Facturation** et sélectionnez l'onglet **Utilisation Totale des Points de Données**.

Pour plus d'informations sur les composants du tableau de bord des points de données, consultez [Facturation]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**Ne gaspillez pas de points de données. Ne mettez à jour que les données modifiées !**<br><br>
Pour minimiser la consommation de points de données, nous recommandons de mettre en place un programme pour éviter d'envoyer les mêmes données inchangées et de ne transmettre que les données nouvelles et pertinentes à Braze. Braze travaillera avec vous pour établir cette meilleure pratique pendant l’onboarding.
{% endalert %}

## Compteur de consommations

En somme, les points de données sont cumulés lorsque les données de profil d’un utilisateur sont mises à jour ou lorsqu’elles effectuent des actions spécifiques. Globalement, les points de données correspondent à des décomptes des `session starts`, `session ends`, `events` et `purchases` de chacun de vos utilisateurs.

Vous trouverez une décomposition de la façon dont Braze accumule les points de données dans les sections suivantes. Si vous avez des questions concernant les nuances entre points de données Braze, votre gestionnaire de compte Braze peut y répondre.

Les actions suivantes ne consomment pas de points de données :
- Supprimer des utilisateurs de Braze
- Utiliser du contenu connecté lors de l’envoi de messages
- L’état de l’abonnement change à l’échelle globale et relativement aux groupes d’abonnement
- Renommer les identifiants externes de vos utilisateurs via des [appels d'API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Blocage des événements, des attributs ou des propriétés d'événement

### Circonstances particulières

#### Tableaux

Un tableau est une collection ordonnée d’articles stockés dans un attribut personnalisé. En termes de consommation, chaque appel API pour mettre à jour un tableau coûte un point de données. Cependant, si vous ajoutez des valeurs à un tableau, cela comptera comme un point de données par valeur. 

{% alert tip %}
Si vous définissez la totalité du tableau à la fois, cela comptera comme un point de données. De ce fait, les tableaux constituent un excellent outil pour maintenir les profils d’utilisateur à jour avec toutes les informations pertinentes et réduire les coûts.
{% endalert %}

#### Attributs personnalisés imbriqués

Les attributs personnalisés imbriqués font référence à un objet qui définit un ensemble d'attributs en tant que propriété d'un autre attribut. Chaque clé de l'objet est considérée comme un point de donnée.

{% alert note %}
La mise à jour d’un objet d’attribut personnalisé vers `null` consomme également un point de données.
{% endalert %}

#### CSV

Les attributs personnalisés téléchargés via l'importation CSV comptent pour vos points de données. Cependant, les importations CSV à des fins de segmentation (importations effectuées avec `external_id`, `braze_id`, ou `user_alias_name` comme seul champ) ne consommeront pas de points de données.

De plus, étant donné que les changements d’état d’abonnement ne consomment pas de points de données, la mise à jour des champs `email_subscribe`, `push_subscribe`, `subscription_group_id`, ou `subscription_state` dans votre fichier CSV n’entraînera pas de frais.

## Points de données

{% alert note %}
Les tableaux suivants sont donnés à titre d'exemple. Pour connaître les conventions d'appellation exactes, les majuscules et les valeurs acceptées pour certains champs, reportez-vous à la documentation relative à votre méthode d'ingestion.
{% endalert %}

{% tabs %}
{% tab Non facturable %}

#### Points de données non facturables (par défaut)

<div class="small_table"></div>

| Type de données | Points de données |
| --------- | ---------- |
| Données de profil | Pays |
| Données de profil | Langue |
| Données de profil | ID utilisateur |
| Données de profil | Alias utilisateur |
| Appareils récents | Nombre d’appareils |
| Appareils récents | Visualisé le plus récemment |
| Appareils récents | Version de l’application |
| Appareils récents | Appareil |
| Appareils récents | Système d’exploitation de l’appareil |
| Paramètres de contact | Abonnement aux e-mails |
| Paramètres de contact | Abonnement aux notifications push |
| Paramètres de contact | Applications enregistrées pour les notifications push |
| Paramètres de contact | Groupe d’abonnement |
| Campagnes reçues | Adresse e-mail |
| Attribution d’installation | Installer la source |
| Attribution d’installation | Campagne arrêtée |
| Attribution d’installation | Publicité de groupe |
| Attribution d’installation | Publicité |
| Divers | Numéro de compartiment aléatoire |
| Messages Canvas reçus | Messages Canvas reçus |
| L'envoi de messages | Tous les événements d'engagement (tels que les ouvertures, les clics, les impressions et les renvois) |
| Twitter | Abonnés |
| Twitter | Abonnement |
| Twitter | Nombre de tweets |
| Facebook | Mentions j’aime |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Facturable %}

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

| Type de données | Points de données | Remarques |
| --------- | ---------- | ----- |
| Données de profil | Prénom | |
| Données de profil | Nom | |
| Données de profil | Adresse e-mail | |
| Données de profil | Genre | |
| Données de profil | Tranche d’âge | |
| Données de profil | Pays | Lorsqu’ils sont collectés manuellement. Ne compte pas pour la consommation lorsqu'il est collecté automatiquement. |
| Données de profil | Ville | |
| Données de profil | Langue | Lorsqu’ils sont collectés manuellement. Ne compte pas pour la consommation lorsqu'il est collecté automatiquement. |
| Données de profil | Emplacement le plus récent de l’appareil | |
| Données de profil | Fuseau horaire | |
| Données de profil | Date de naissance (DDN) | |
| Données de profil | Bio | |
| Données de profil | Numéro de téléphone | |
| Données d’utilisation des applications | Lancer la session | |
| Données d’utilisation des applications | Fin de session | |
| Attributs personnalisés | Tous les attributs personnalisés | |
| Événements personnalisés | Tous les événements personnalisés | |
| Propriétés de l'événement  personnalisé | Toutes les propriétés de l'événement  personnalisé | Les propriétés d’événement personnalisé activées pour la segmentation avec les filtres `X Custom Event Property in Y Days` ou `X Purchase Property in Y Days` sont toutes comptées comme des points de données séparés qui viennent s’ajouter au point de données comptabilisé par l’événement personnalisé lui-même.
| Achats | Tous les achats | |
| Propriétés d'achat | Toutes les propriétés d'achat | |
| Affectation de cohorte Amplitude | Toutes les affectations | |
| Affectation de cohorte Mixpanel | Toutes les affectations | |
| Affectation de cohorte Hightouch | Toutes les affectations | |
| Attribution de cohorte Appsflyer | Toutes les affectations | |
| Localisation la plus récente | Toutes les localisations les plus récentes | Saisir ou quitter des géorepérages ne consomme pas de points de données car les données de géorepérage n’ont pas été stockées sur le profil utilisateur. Les géorepérages sont surveillées par les services de localisation d’Apple et Google, Braze n’est averti qu’à un utilisateur qui déclenche une géorepérage. |
| Twitter | Nom d’utilisateur | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

