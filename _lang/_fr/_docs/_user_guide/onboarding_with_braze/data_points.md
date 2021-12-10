---
nav_title: Points de données
article_title: Aperçu des Points de Données
page_order: 4
page_type: Référence
description: "Cet article de référence décrit ce que les Points de Données sont à Braze et comment vous pouvez être au courant de leur utilisation."
---

# Points de données

Au Brésil, les données signifient l'action: chaque partie de données qui arrive dans Braze met à jour l'adhésion au segment, peut déclencher & annuler la messagerie, est immédiatement disponible pour la personnalisation de la messagerie, et plus encore. Ainsi, les points de données sont la manière dont Braze définit une structure de facturation et de tarification, basée sur des informations enregistrées sur les profils des utilisateurs. Voir [Nombre de consommations](#consumption-count) ci-dessous pour voir quelles données comptent pour votre allocation de points de données.

Notre équipe de service à la clientèle peut vous aider à recommander les meilleures pratiques en matière de données pour répondre à vos besoins spécifiques. Vous trouverez dans votre contrat de Braze une répartition plus détaillée de cette définition.

## Gestion et utilisation

Pour afficher votre tableau de bord Data Point, sélectionnez votre nom dans le coin supérieur droit, cliquez sur le menu déroulant et sélectionnez __Abonnements et Utilisation__. Pour plus d'informations sur les composants du tableau de bord Data Point, consultez notre article [d'abonnement et d'utilisation]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/).

{% alert tip %}
__Mettre à jour uniquement vos deltas (changement de données)!__

Pour éviter l'utilisation de vos points de données alloués, nous vous recommandons de configurer un programme qui empêchera l'envoi de la même chose, les données inchangées de votre application vers Braze encore et encore.
{% endalert %}

## Nombre de consommations

En somme, les points de données sont accumulés lorsque les données du profil d'un utilisateur sont mises à jour ou quand il effectue des actions spécifiques. Essentiellement, les points de données sont comptés pour chacun de vos utilisateurs `la session commence`, `la session se termine`, `événements`, et `achats`.

Vous pouvez trouver une ventilation de la façon dont Braze accumule les points de données ci-dessous, mais il y a des nuances au-delà de ce que vous voyez ici, qui peuvent affecter le nombre de points restants que vous attendez de voir. Si vous avez des questions au sujet de votre facturation, contactez votre responsable de compte Braze.

{% alert note %} Le Contenu Connecté ne consomme pas les points de données — utiliser le Contenu Connecté est un excellent moyen de référencer des données d'autres plateformes sans avoir besoin de télécharger en masse sur Braze et d'utiliser vos points! {% endalert %}

{% tabs %}
{% tab General %}

### Généraux

| type de données                          | point de données                                  | compte-t-il pour la consommation? |
| ---------------------------------------- | ------------------------------------------------- | --------------------------------- |
| Données du profil                        | Prénom                                            | Oui                               |
| Données du profil                        | Nom de famille                                    | Oui                               |
| Données du profil                        | Identifiant de l'utilisateur                      | Non                               |
| Données du profil                        | Alias de l'utilisateur                            | Non                               |
| Données du profil                        | Adresse e-mail                                    | Oui                               |
| Données du profil                        | Sexe                                              | Oui                               |
| Données du profil                        | Groupe d'âge                                      | Oui                               |
| Données du profil                        | Pays                                              | Oui                               |
| Données du profil                        | Ville                                             | Oui                               |
| Données du profil                        | Langue                                            | Oui                               |
| Données du profil                        | Localisation de l'appareil la plus récente        | Oui                               |
| Données du profil                        | Fuseau horaire                                    | Oui                               |
| Données du profil                        | Date de naissance (DOB)                           | Oui                               |
| Données du profil                        | Bio                                               | Oui                               |
| Données du profil                        | Numéro de téléphone                               | Oui                               |
| Données du profil                        | URL de l'image de l'avatar                        | Oui                               |
| Données d'utilisation de l'application   | Début de la session                               | Oui                               |
| Données d'utilisation de l'application   | Fin de la session                                 | Oui                               |
| Attributs personnalisés                  | Tous les attributs personnalisés                  | Oui                               |
| Appareils récents                        | Nombre d'appareils                                | Non                               |
| Appareils récents                        | Surveillance la plus récente                      | Non                               |
| Appareils récents                        | Version de l'application                          | Non                               |
| Appareils récents                        | Appareil                                          | Non                               |
| Appareils récents                        | Système d'exploitation de l'appareil              | Non                               |
| Événements personnalisés                 | Tous les événements personnalisés                 | Oui                               |
| Propriétés personnalisées de l'événement | Toutes les propriétés d'événement personnalisées* | Oui                               |
| Achats                                   | Tous les achats                                   | Oui                               |
| Affectation de cohorte d'amplitude       | Tous les devoirs                                  | Oui                               |
| Affectation de cohortes Mixpanel         | Tous les devoirs                                  | Oui                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
En ce qui concerne l'utilisation de l'abonnement, les propriétés d'événement personnalisées activées pour la segmentation avec les filtres `X Custom Event Property en Y Days` ou `X Purchase Property en Y Days` sont toutes comptées comme des points de données distincts en plus du point de données compté par l'événement personnalisé lui-même.
{% endalert %}

  {% endtab %}
{% tab Location %}

### Localisation

| type de données     | point de données                       | compte-t-il pour la consommation? |
| ------------------- | -------------------------------------- | --------------------------------- |
| Lieu le plus récent | Tous les emplacements les plus récents | Oui                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %} La saisie ou la sortie de géofences ne consomme pas de points de données car les données de géorepérage ne sont pas stockées dans le profil de l'utilisateur. Les géorepérages sont surveillés par les services de localisation Apple et Google, Braze n'est notifié que lorsqu'un utilisateur déclenche un géorepérage. {% endalert %}

  {% endtab %}
{% tab Engagement %}

### Engagement

| type de données              | point de données                    | compte-t-il pour la consommation? |
| ---------------------------- | ----------------------------------- | --------------------------------- |
| Paramètres du contact        | E-mail abonné                       | Non                               |
| Paramètres du contact        | Push abonné                         | Non                               |
| Paramètres du contact        | Applications enregistrées pour Push | Non                               |
| Campagnes Reçues             | Adresse e-mail                      | Non                               |
| Cartes d'actualités cliquées | Cartes d'actualités cliquées        | Non                               |
| Installer Attribution        | Installer la source                 | Non                               |
| Installer Attribution        | Campagnes                           | Non                               |
| Installer Attribution        | Groupe d'annonces                   | Non                               |
| Installer Attribution        | Ad                                  | Non                               |
| Divers                       | Nombre aléatoire de Seaux           | Non                               |
| Messages reçus sur Canvas    | Messages reçus sur Canvas           | Non                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
{% tab Social %}

### Réseaux sociaux

| type de données | point de données  | compte-t-il pour la consommation? |
| --------------- | ----------------- | --------------------------------- |
| Twitter         | Nom d'utilisateur | Oui                               |
| Twitter         | Abonnés           | Non                               |
| Twitter         | Abonnements       | Non                               |
| Twitter         | Nombre de Tweets  | Non                               |
| Facebook        | J'aime            | Non                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
{% endtabs %}

### Condition spéciale

#### CSV

Attributs personnalisés téléchargés via le compte CSV vers vos points de données, cependant csv importe à des fins de segmentation (importations faites avec `external_id` comme seul champ) ne consommera pas de points de données.

#### Tableaux

Un tableau (ou une chaîne) est une collection ordonnée d'éléments stockés dans un attribut personnalisé. En termes de consommation, il faut un point de données par appel API pour mettre à jour le tableau.

Cela signifie que si vous définissez le tableau entier à la fois, il compte comme un point de données. Cependant, si vous ajoutez des valeurs au tableau de manière incrémentale, il compte comme un point de données par valeur.
