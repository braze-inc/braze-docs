---
nav_title: Approbations
article_title: Approbations
page_order: 1
page_type: reference
description: "Cet article de référence donne un aperçu des différents statuts que peuvent avoir une campagne et un canvas et de leur signification."
tool:
    - Campaigns
    - Canvas
---

# Approbation des campagnes et des toiles

> Utilisez les approbations pour ajouter un dernier point de contrôle à vos campagnes et Canevas avant le lancement. Grâce à ce flux de travail, vous pouvez vérifier et approuver le contenu de toutes les sections requises de votre message.

## Fonctionnement

Vous pouvez revoir les détails de votre campagne ou de votre canvas lors de l'étape finale de modification. 

Pour les toiles et les campagnes, toutes les modifications doivent être enregistrées avant d'être approuvées, même s'il s'agit de vos propres modifications. Chaque section du résumé doit être approuvée par un utilisateur disposant des autorisations appropriées avant que le message ne puisse être lancé. Le statut par défaut de chaque section est " **En attente d'approbation"**.

{% tabs %}
{% tab campaign %}
Pour lancer une campagne, vous devez approuver ces éléments :

- **Messages :** Tel est le message de la campagne.
- **Livraison :** Il s'agit du type de réception/distribution qui détermine le moment où les utilisateurs recevront la campagne.
- **Audience cible :** Cela permet de déterminer qui recevra la campagne.
- **Événements de conversion :** Il s'agit de l'indicateur que vous suivez à des fins d'engagement et de rapports.
{% endtab %}

{% tab canvas %}
Pour lancer un canvas, vous devez approuver ces éléments clés :

- **Événements de conversion :** Il s'agit de l'indicateur que vous suivez à des fins d'engagement et de rapports.
- **Planification d’entrée :** Il s'agit notamment du type de planification de la saisie et du moment où les utilisateurs doivent entrer dans le Canvas.
- **Audience cible :** Cela permet de déterminer qui entrera dans cette toile.
- **Envoyer les paramètres :** Il s'agit des options d'envoi pour toutes les étapes du canvas. 
- **Créer un canvas :** Il s'agit du parcours de l'utilisateur de Canvas.
{% endtab %}
{% endtabs %}

## Activation du processus d'approbation

Par défaut, le paramètre de flux de travail d'approbation est désactivé pour les campagnes et les canevas. Pour activer cette fonctionnalité, accédez à **Paramètres** > **Flux d'approbation** et basculez sur la case correspondante :

- **Utiliser le flux d'approbation pour toutes les campagnes dans [votre espace de travail].**
- **Utiliser le processus d'approbation pour toutes les toiles dans [votre espace de travail].**

{% alert important %}
L'approbation des campagnes n'est pas prise en charge pour les [campagnes API]({{site.baseurl}}/api/api_campaigns) et les [campagnes d'e-mails transactionnels]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Définition des autorisations utilisateur

Une fois le workflow d'approbation activé, vous devrez définir les autorisations des utilisateurs afin que les utilisateurs de votre tableau de bord puissent approuver ou refuser les campagnes et les Canevas immédiatement. Ces deux autorisations peuvent également être appliquées à des espaces de travail ou à des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), ou ajoutées à un [ensemble d'autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Vous devez disposer de l'[autorisation "Approuver et refuser des campagnes".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Cette autorisation permet de contrôler qui peut mettre à jour le statut d'approbation d'une campagne. Avec cette autorisation, vous pouvez faire ce qui suit :

- Auto-approbation de la campagne
- Approuver et lancer la campagne
- Approuver mais ne pas lancer la campagne (un autre utilisateur disposant de l'autorisation "Envoyer des campagnes, des toiles" peut lancer la campagne).
- Ni approuver ni lancer la campagne

Une fois les statuts d'approbation définis à l'étape **Résumé**, toute modification ultérieure apportée à la campagne réinitialisera tous les statuts d'approbation lorsqu'elle sera enregistrée. Cette règle s'applique à toutes les modifications apportées à un projet de campagne ou à une campagne postérieure au lancement. Par exemple, si vous ne modifiez que l'audience cible, l'étape **Résumé** ramènera les statuts d'approbation de toutes les sections à l'état par défaut, c'est-à-dire en attente.

{% endtab %}

{% tab canvas %}
Vous devez avoir l'[autorisation "Approuver et refuser des toiles".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Cette autorisation permet de contrôler qui peut mettre à jour le statut d'approbation d'un canvas. Avec cette autorisation, vous pouvez faire ce qui suit :

- Auto-approbation du canvas
- Approuver et lancer le Canvas
- Approuver mais ne pas lancer le canvas (un autre utilisateur ayant l'autorisation "Envoyer des campagnes, des canevas" peut lancer le canvas).
- Ni approuver ni lancer le Canvas

Une fois les statuts d'approbation définis à l'étape du **canvas**, toute modification ultérieure apportée au canvas réinitialisera tous les statuts d'approbation lorsqu'elle sera enregistrée. Cela s’applique à toutes les modifications effectuées dans une ébauche de Canvas ou un Canvas après lancement. Par exemple, si vous ne modifiez que l'audience cible, l'étape **Résumé** ramènera les statuts d'approbation de toutes les sections à l'état par défaut, c'est-à-dire en attente. Notez que si le canvas a déjà été approuvé, mais que vous l'enregistrez à nouveau, les approbations seront annulées même si aucune modification n'a été apportée.
{% endtab %}
{% endtabs %}

{% alert important %}
Pour modifier une campagne en cours, vous devez disposer de l'autorisation « Approuver et refuser des campagnes ». Un utilisateur devra approuver ses modifications car une version provisoire des campagnes n'est pas encore disponible. Ce n'est pas le cas pour les Canvas, car un utilisateur peut apporter des modifications et enregistrer un brouillon, et un autre utilisateur peut approuver et lancer le Canvas.
{% endalert %}
