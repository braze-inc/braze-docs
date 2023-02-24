---
nav_title: Points de données
article_title: Aperçu des points de données
page_order: 4
page_type: reference
description: "Le présent article de référence décrit les points de données à Braze et comment vous pouvez être conscient de leur utilisation."
search_rank: 6
---

# Points de données

Chez Braze, les données signifient : chaque élément de données arrivant chez Braze met à jour l’adhésion du segment, peut déclencher et annuler des envois de messages, est immédiatement disponible pour la personnalisation des envois de messages et plus encore. Les points de données vous aident à définir les informations les plus importantes pour votre entreprise. En tenant compte de l’information à suivre, vous devez cibler les données les plus à fort impact pour l’expérience de vos utilisateurs.

De ce fait, les points de données sont la façon de Braze de définir une structure de facturation et de tarification, en fonction des informations enregistrées par rapport aux profils utilisateur. Notre équipe de réussite client peut vous aider à recommander les meilleures pratiques en matière de donnée pour répondre à vos besoins. Vous trouverez une répartition plus détaillée de cette définition dans votre contrat Braze. 

> Les « Points de données » font référence à une unité facturable d’utilisation des Services Braze, mesurée par un début de session, une fin de session, un événement personnalisé ou un achat enregistré, ainsi que tout attribut défini sur un profil d’utilisateur final. Pour plus de clarté, la définition des informations relatives au profil d’un utilisateur final à un moment donné est considérée comme un seul point de données. <br><br>Les données et les événements collectés par défaut par les Services Braze, y compris, par exemple, les jetons push, les informations sur les appareils et tous les événements de suivi de l’engagement des campagnes, tels que les ouvertures d’e-mails et les clics de notifications push, *ne sont pas* comptabilisés comme des Points de données.

Voir la section [Compteur de consommations](#consumption-count) du présent article pour comprendre quelles données comptent pour votre attribution de points de données.

## Gestion et utilisation

Dans Braze, pour afficher votre tableau de bord Point de données, sélectionnez votre nom dans l’angle supérieur droit, cliquez sur le menu déroulant et sélectionnez **Subscriptions and Usage (Abonnements et utilisation)**. Pour plus d’informations sur les composants du tableau de bord des points de données, reportez-vous à [Abonnements et utilisation]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/).

{% alert tip %}
**Ne gaspillez pas de points de données.  Ne mettez à jour que les données modifiées !**<br><br>
Pour vous assurer de minimiser la consommation de points de données, nous vous recommandons de configurer un programme pour éviter d’envoyer les mêmes données inchangées et de ne transmettre que des données nouvelles et pertinentes à Braze.  Braze travaillera avec vous pour établir cette meilleure pratique pendant l’onboarding. 
{% endalert %}

## Compteur de consommations

En somme, les points de données sont cumulés lorsque les données de profil d’un utilisateur sont mises à jour ou lorsqu’elles effectuent des actions spécifiques. Les points de données correspondent essentiellement au décompte de chacun de vos `démarrages de session`, `fins de session`, `events`événements et achats utilisateur.`purchases`

Vous trouverez une décomposition de la façon dont Braze accumule les points de données dans les sections suivantes. Si vous avez des questions concernant les nuances entre points de données Braze, votre gestionnaire de compte Braze peut y répondre.

Les actions suivantes ne consomment pas de points de données :
- Supprimer des utilisateurs de Braze
- Utiliser du contenu connecté lors de l’envoi de messages
- L’état de l’abonnement change à l’échelle globale et relativement aux groupes d’abonnement.
- Renommer les ID externes de vos utilisateurs par le biais d’[appels API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)

### Circonstances particulières

#### Arrays

Un tableau est une collection ordonnée d’articles stockés dans un attribut personnalisé. En termes de consommation, chaque appel API pour mettre à jour un tableau coûte un point de données. Cependant, si vous ajoutez des valeurs à un tableau, cela comptera comme un point de données par valeur. 

{% alert tip %}
Si vous définissez la totalité du tableau à la fois, cela comptera comme un point de données. De ce fait, les tableaux constituent un excellent outil pour maintenir les profils d’utilisateur à jour avec toutes les informations pertinentes et réduire les coûts. 
{% endalert %}

#### CSV

Les attributs personnalisés téléchargés via le compte CSV pour vos points de données. Cependant, les importations CSV à des fins de segmentation (importations effectuées avec `external_id`, `braze_id`, ou `user_alias_name` comme seul champ) ne consommeront pas de points de données.

De plus, étant donné que les changements d’état d’abonnement ne consomment pas de points de données, la mise à jour des champs `email_subscribe`, `push_subscribe`, `subscription_group_id`, ou `subscription_state` dans votre fichier CSV n’entraînera pas de frais.

## Points de données

{% tabs %}
{% tab Non facturables %}

#### Points de données non facturables (d’origine)

<div class="small_table"></div>

| Type de données | Points de données |
| --------- | ---------- |
| Données de profil | Total |
| Données de profil | Langue |
| Données de profil | ID utilisateur |
| Données de profil | Alias utilisateur |
| Appareils récents | Nombre d’appareils |
| Appareils récents | Visualisé le plus récemment |
| Appareils récents | Version de l’application |
| Appareils récents | Appareil |
| Appareils récents | Système d’exploitation de l’appareil |
| Paramètres de contact | Inscription de courriel |
| Paramètres de contact | Abonnement aux notifications push |
| Paramètres de contact | Applications enregistrées pour les notifications push |
| Paramètres de contact | Groupe d’abonnement |
| Campagnes reçues | Adresse e-mail |
| Attribution d'installation | Installer la source |
| Attribution d'installation | Campagne |
| Attribution d'installation | Publicité de groupe |
| Attribution d'installation | Publicité |
| Divers | Numéro de compartiment aléatoire |
| Messages Canvas reçus | Messages Canvas reçus |
| Twitter | Abonnés |
| Twitter | Abonnement |
| Twitter | Nombre de tweets |
| Facebook | Mentions j’aime |

{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Facturables %}

#### Points de données facturables

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
| Données de profil | Sexe | |
| Données de profil | Tranche d’âge | |
| Données de profil | Total | Lorsqu’ils sont collectés manuellement. Ne compte pas pour consommation lorsqu’elle est automatiquement collectée. |
| Données de profil | Ville | |
| Données de profil | Langue | Lorsqu’ils sont collectés manuellement. Ne compte pas pour consommation lorsqu’elle est automatiquement collectée. |
| Données de profil | Emplacement le plus récent de l’appareil | |
| Données de profil | Fuseau horaire | |
| Données de profil | Date de naissance (date de naissance) | |
| Données de profil | Bio | |
| Données de profil | Numéro de téléphone | |
| Données d’utilisation des applications | Lancer la session | |
| Données d’utilisation des applications | Fin de session | |
| Attributs personnalisés | Tous les attributs personnalisés | |
| Événements personnalisés | Tous les événements personnalisés | |
| Propriétés de l’événement personnalisé | Propriétés de l'événement personnalisé | Les propriétés de l’événement personnalisé activées pour la segmentation avec les filtres `X propriétés de l’événement personnalisé en Y jours` ou `X propriétés d’achat en Y jours` sont toutes comptées comme des points de données séparés qui viennent s’ajouter au point de données comptabilisé par l’événement personnalisé lui-même.
| Achats | Tous les achats | |
| Affectation de cohorte d’amplitude | Toutes les affectations | |
| Affectation de cohorte de mixpanel | Toutes les affectations | |
| Affectation de cohorte Hightouch | Toutes les affectations | |
| Attribution de cohorte pour Appsflyer | Toutes les affectations | |
| Emplacement le plus récent | Tous les emplacements les plus récents | Saisir ou quitter des geofences ne consomme pas de points de données car les données de geofence n’ont pas été stockées sur le profil utilisateur. Les geofences sont surveillées par les services de localisation d’Apple et Google, Braze n’est averti qu’à un utilisateur qui déclenche une geofence. |
| Twitter | Nom d’utilisateur | |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}
