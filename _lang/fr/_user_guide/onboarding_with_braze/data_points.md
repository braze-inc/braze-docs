---
nav_title: Points de données
article_title: Aperçu des points de données
page_order: 4
page_type: reference
description: "Le présent article de référence décrit les points de données à Braze et comment vous pouvez être conscient de leur utilisation."

---

# Points de données

Chez Braze, les données signifient : chaque élément de données arrivant chez Braze met à jour l’adhésion du segment, peut déclencher et annuler des envois de messages, est immédiatement disponible pour la personnalisation des envois de messages et plus encore. De ce fait, les points de données sont la façon de Braze de définir une structure de facturation et de tarification, en fonction des informations enregistrées par rapport aux profils utilisateur. Voir la section [ Compteur de consommations](#consumption-count) du présent article pour comprendre quelles données comptent vers l’attribution de votre point de données.
 
Notre équipe de service de support peut vous aider à recommander des meilleures pratiques de données afin de rendre vos coûts/droits très prévisibles en tenant compte de la saisonnalité et dimensionné correctement avec beaucoup de marge et des options pour la flexibilité. Vous trouverez une répartition plus détaillée de cette définition dans votre contrat Braze.

Les « Points de données » font référence à une unité facturable d’utilisation des Services Braze, mesurée par un début de session, une fin de session, un événement personnalisé ou un achat enregistré, ainsi que tout attribut défini sur un profil d’utilisateur final. Votre volume d’utilisateurs actifs par mois sous contrat détermine votre attribution de points de données, avec une flexibilité quant au ratio approprié en fonction de vos besoins commerciaux ou de vos utilisateurs. Les données et les événements collectés par défaut par les Services Braze, y compris, par exemple, les jetons push, les informations sur les appareils et tous les événements de suivi de l’engagement des campagnes, tels que les ouvertures d’e-mails et les clics de notifications push, ne sont pas comptabilisés comme des Points de données. Pour plus de clarté, la définition des informations relatives au profil d’un utilisateur final à un moment donné est considérée comme un seul point de données.

## Gestion et utilisation

Pour afficher votre tableau de bord Point de données, sélectionnez votre nom dans l’angle supérieur droit, cliquez sur le menu déroulant et sélectionnez **Abonnements et utilisation**. Pour plus d’informations sur les composants du tableau de bord des points de données, reportez-vous à [Abonnements et utilisation]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/).

{% alert tip %}
**Mettez à jour uniquement vos tas (modification des données) !**

Pour éviter d’utiliser vos points de données alloués, nous vous recommandons de configurer un programme qui empêchera d’envoyer les mêmes données, sans modifier les données de votre application à Braze.
{% endalert %}

## Compteur de consommations

En somme, les points de données sont cumulés lorsque les données de profil d’un utilisateur sont mises à jour ou lorsqu’elles effectuent des actions spécifiques. Les points de données sont essentiellement le compte de chacun de vos `démarrages de session`, `fins de session`, `événements` et `achats` utilisateur.

Vous pouvez trouver une décomposition de la manière dont Braze cumule les points de données dans les sections suivantes, mais il existe des nuances au-delà de ce que vous voyez ici, ce qui peut affecter le nombre de points restants que vous attendez de voir. Si vous avez des questions sur votre facturation, contactez votre gestionnaire de compte Braze.

{% alert note %} 
Les actions suivantes ne consomment pas de points de données :
- Supprimer des utilisateurs de Braze
- Utiliser du contenu connecté lors de l’envoi de messages
{% endalert %}

### Points de données facturables

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="large_table"></div>

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
| Emplacement le plus récent | Tous les emplacements les plus récents | Le fait de pénétrer ou quitter des geofences ne consomme pas de points de données, car les données de geofence ne sont pas stockées sur le profil utilisateur. Les geofences sont surveillées par les services de localisation d’Apple et Google, Braze n’est averti qu’à un utilisateur qui déclenche une geofence. |
| Twitter | Nom d’utilisateur | |
{: .reset-td-br-1 .reset-td-br-2}

### Points de données non facturables (d’origine)

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

### Circonstances particulières

#### CSV

Les attributs personnalisés téléchargés par le biais de CSV sont décomptés dans vos points de données, cependant les importations CSV à des fins de segmentation (importations effectuées avec `external_id`, `braze_id` ou `user_alias_name` comme seul champ) ne consommeront pas de points de données.

#### Arrays

Un tableau (ou string)) est une collection ordonnée d’articles stockés dans un attribut personnalisé. En termes de consommation, chaque appel API pour mettre à jour le tableau coûte un point de données.

Cela signifie que si vous définissez la totalité du tableau à la fois, elle compte comme un point de données. Cependant, si vous ajoutez des valeurs au tableau, cela compte comme un point de données par valeur.
