---
nav_title: Approuver des campagnes
article_title: Approuver des campagnes
alias: "/campaign_approval/"
page_order: 0
page_type: reference
description: "Cette page donne un aperçu du processus d’approbation d’une campagne."
tool: Campaigns
---

# Approuver des campagnes

> L’approbation de la campagne ajoute un processus de révision à votre flux de travail avant de lancer une campagne. Cette fonctionnalité ajoute des états qui sont disponibles dans l'étape du flux de travail de confirmation de la campagne. Vous pouvez vous assurer que chaque confirmation est approuvée pour lancer la campagne.

{% alert important %}
L'approbation de la campagne n'est pas prise en charge dans le flux de travail de création des campagnes API et des campagnes d'e-mails transactionnels.
{% endalert %}

## Activer l’approbation de campagne

Par défaut, le paramètre d’approbation de la campagne est désactivé. Pour activer cette fonctionnalité, allez dans **Paramètres** > **Flux d'approbation.**

{% alert note %}
Si vous utilisez l'[ancienne version de navigation]({{site.baseurl}}/navigation), vous trouverez cette page sous **Gérer les paramètres** > **Workflow d'approbation.**
{% endalert %}

## Utiliser les approbations

Une fois l'approbation de la campagne activée, vous devez disposer de l'autorisation "Approuver et refuser des campagnes". Cette autorisation permet de contrôler qui peut mettre à jour le statut d'approbation d'une campagne. Cette autorisation peut également être appliquée à des espaces de travail ou à des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), ou être ajoutée à un [ensemble d'autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

Dans l'étape **Revoir le résumé** du flux de travail de création de la campagne, utilisez l'option d'approbation pour approuver ou refuser les composants clés de votre campagne : **Messages**, **réception/distribution**, **population cible** et **événements de conversion**. L'état par défaut de l'approbation de la campagne est **En attente d'approbation**. Notez qu'il est possible d'auto-approuver des composants d'une campagne.

![][1]

Une fois que chaque section aura été approuvée, le bouton **Lancer** sera activé et vous pourrez lancer votre campagne ! 

[1]: {% image_buster /assets/img_archive/campaign_approval_example.png %} 
