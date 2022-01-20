---
nav_title: Mise en place des courants
article_title: Mise en place des courants
page_order: 0
page_type: tutoriel
description: "Cet article pratique vous guide à travers le processus d'intégration et de configuration de Braze Currents."
tool: Courants
platform:
  - ios
  - android
  - allumer
  - web
  - tvos
  - roku
---

# Mise en place des courants

> Cette page décrit et décrit le processus générique d'intégration et de configuration des courants de Braze.

{% alert important %}
Les courants sont inclus avec certains paquets Braze. Veuillez contacter votre représentant de Braze si vous avez des questions ou si vous souhaitez obtenir un accès.
{% endalert %}

## Exigences

L'utilisation de Courants avec l'un de nos partenaires nécessite les mêmes paramètres de base et la même méthodologie de connexion.

Chaque partenaire exige que Braze ait la permission d'écrire et d'envoyer des fichiers de données, et Braze demande l'emplacement dans lequel ils doivent écrire ces fichiers, spécifiquement des noms de bucket ou des clés.

Les exigences suivantes sont les exigences de base et minimales à intégrer avec la plupart de nos partenaires. Certains partenaires nécessiteront des paramètres supplémentaires, mais celles-ci seront listées sur [ces pages partenaires]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) ainsi que toutes les nuances associées à ces exigences de base.

| Exigences                                                          | Origine                                                                                                                             | Accès                                                                                                                                                                              | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte avec partenaire                                             | Organisez un compte avec ce partenaire ou contactez votre responsable de compte Braze pour des suggestions.                         | Vérifiez le site du Partenaire ou contactez ce Partenaire pour vous inscrire.                                                                                                      | Braze n’enverra pas de données à un Partenaire si vous n’avez pas accès à ces données via le compte de votre entreprise.                                                                                                                                                                                                                                                                                                  |
| Clé API partenaire ou jeton                                        | Habituellement le tableau de bord du Partenaire.                                                                                    | Il suffit de le copier et de le coller dans le champ désigné de Braze.                                                                                                             | Braze a un champ désigné pour cela dans la page Intégrations pour ce partenaire. Nous avons besoin de cela pour cartographier où nous envoyons vos données. **Il est important de tenir à jour vos clés partenaires/jetons ; les identifiants invalides peuvent entraîner la désactivation de votre connecteur et la suppression des événements.**                                                                        |
| Code d'authentification/clé, clé secrète, fichier de certification | Contactez un représentant de votre compte avec ce partenaire. Peut également exister dans le tableau de bord du Partenaire.         | Copiez et collez les clés dans le champ Braze désigné. Générez et téléchargez `.json` ou d'autres fichiers de certification à l'endroit approprié au Brésil.                       | Braze a un champ désigné pour cela dans la page Intégrations pour ce partenaire. Cela donne des informations d'identification à Braze et nous autorise à écrire des fichiers sur votre compte partenaire. **Il est important de tenir vos informations d'authentification à jour ; les informations d'identification invalides peuvent entraîner la désactivation de votre connecteur et la suppression des événements.** |
| Bucket, Chemin du dossier                                          | Certains partenaires organisent et trient les données par segments. Cela devrait être trouvé dans le tableau de bord du partenaire. | Si cela est nécessaire, assurez-vous de copier le nom du seau ou le chemin du fichier exactement dans l'espace désigné en Brésil. Nous ne voulons pas que vos données se perdent ! | Bien que cela soit nécessaire pour certains partenaires, il est important de bien se débrouiller quand vous en avez besoin.                                                                                                                                                                                                                                                                                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert important %}
Il est important de tenir à jour vos clés partenaires/jetons et les détails d'authentification ; si les identifiants de votre connecteur expirent, le connecteur arrêtera d'envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}


## Étape 1 : Choisissez votre partenaire

Braze Currents vous permet d'intégrer à travers le stockage de données à l'aide de fichiers plats ou à nos partenaires Behavioral Analytics et de données clients à l'aide d'une charge utile JSON battue à un point de terminaison désigné.

Avant de commencer votre intégration, il est préférable de décider quelle intégration est la mieux adaptée à vos besoins. Par exemple, si vous utilisez déjà mParticle et Segment et que vous voulez que les données Braze soient diffusées là-bas, il serait préférable d'utiliser un bloc JSON batché. Si vous préférez manipuler les données par vous-même ou si vous avez un système d'analyse de données plus complexe, il serait peut-être préférable d'utiliser le stockage de données ([Braze utilise cette méthode]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/)!)

## Étape 2 : Accédez aux courants

Pour commencer, visitez la page Courants dans la barre latérale de gauche, dans la section « Intégrations » du tableau de bord. Vous serez dirigé vers la page de gestion de l'intégration des courants .

![Courants]({% image_buster /assets/img_archive/currents-main-page.png %})

## Étape 3: Ajouter un partenaire

Ajoutez un partenaire, parfois appelé "Connecteur de courants", en cliquant sur le menu déroulant en haut à droite de l'écran.

![Ajout d'une intégration]({% image_buster /assets/img/new_current.png %}){: style="largeur-max:30%;"}

Chaque partenaire a besoin d'un ensemble différent d'étapes de configuration. Pour activer chaque intégration, [voir les instructions dans leurs pages respectives]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).

## Étape 4 : Configurer les événements

Choisissez les événements que vous souhaitez passer à ce partenaire en vérifiant les options disponibles. Vous pouvez trouver des listes de ces événements dans nos bibliothèques [Événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) et [Événements d'engagement de messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/).

Si nécessaire, vous pouvez en savoir plus sur nos événements dans notre article sur la [Sémantique de livraison d'événements]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_delivery_semantics/).

## Étape 5 : Testez votre intégration

Vous pouvez tester votre intégration ou jeter un coup d'œil à l'échantillon de données des courants dans [nos Exemples Github](https://github.com/Appboy/currents-examples).

{% alert important %}
Veuillez noter que les courants abandonneront les événements avec des charges excessivement importantes supérieures à 900KB.
{% endalert %}
