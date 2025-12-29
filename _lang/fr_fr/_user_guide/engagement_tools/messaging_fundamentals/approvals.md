---
nav_title: Agréments
article_title: Agréments
page_order: 2
page_type: reference
description: "Cet article de référence donne un aperçu des différents statuts que peuvent avoir une campagne et un canvas et de leur signification."
tool:
    - Campaigns
    - Canvas
---

# Approbation des campagnes et des toiles

> Le processus d'approbation des campagnes et des Canevas ajoute un processus d'examen à votre flux de travail avant le lancement. De cette façon, vous pouvez vérifier que chaque section de la finale de la campagne ou de l'éditeur de Canvas est approuvée pour pouvoir être lancée.

## Comment cela fonctionne-t-il ?

Vous pouvez revoir les détails de votre campagne ou de votre Canvas dans la dernière étape de votre éditeur. Pour les campagnes, il s'agit de **Review Summary**, et pour les toiles, il s'agit de **Summary**. 

Si votre administrateur a activé le flux de travail d'approbation, chaque section du résumé doit être approuvée par un utilisateur disposant des autorisations appropriées avant que le message puisse être lancé. Le statut par défaut de chaque section est " **En attente d'approbation"**.

{% tabs %}
{% tab campaign %}
Pour lancer une campagne, vous devez approuver ces éléments clés :

- **Messages :** Tel est le message de la campagne.
- **Réception/distribution :** Il s'agit du type de réception/distribution qui détermine le moment où les utilisateurs recevront la campagne.
- **Audience ciblée :** Cela permet de déterminer qui recevra la campagne.
- **Événements de conversion :** Il s'agit de l'indicateur que vous suivez à des fins d'engagement et de rapports.
{% endtab %}

{% tab canvas %}
Pour lancer un canvas, vous devez approuver ces éléments clés :

- **Événements de conversion :** Il s'agit de l'indicateur que vous suivez à des fins d'engagement et de rapports.
- **Planification de l'entrée :** Il s'agit notamment du type de planification de la saisie et du moment où les utilisateurs doivent entrer dans le Canvas.
- **Audience ciblée :** Cela permet de déterminer qui entrera dans cette toile.
- **Envoyer les paramètres :** Il s'agit des options d'envoi pour toutes les étapes du canvas. 
- **Créer un canvas :** Il s'agit du parcours de l'utilisateur de Canvas.
{% endtab %}
{% endtabs %}

## Activation du processus d'approbation

Par défaut, le paramètre de flux de travail d'approbation est désactivé pour les campagnes et les canevas. Pour activer cette fonctionnalité, accédez à **Paramètres** > **Flux d'approbation** et basculez sur la case correspondante :
- **Utiliser le flux d'approbation pour toutes les campagnes dans [votre espace de travail].**
- **Utiliser le processus d'approbation pour toutes les toiles dans [votre espace de travail].**

{% alert important %}
L'approbation de la campagne n'est pas prise en charge dans le flux de travail de création des [campagnes API]({{site.baseurl}}/api/api_campaigns) et des [campagnes d'e-mails transactionnels]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Définir les autorisations des utilisateurs

Une fois le workflow d'approbation activé, vous devrez définir les autorisations des utilisateurs afin que les utilisateurs de votre tableau de bord puissent approuver ou refuser les campagnes et les Canevas immédiatement. Ces deux autorisations peuvent également être appliquées à des espaces de travail ou à des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), ou ajoutées à un [ensemble d'autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Vous devez disposer de l'[autorisation "Approuver et refuser des campagnes".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Cette autorisation permet de contrôler qui peut mettre à jour le statut d'approbation d'une campagne. Il est possible d'auto-approuver des éléments d'une campagne.
{% endtab %}

{% tab canvas %}
Vous devez avoir l'[autorisation "Approuver et refuser des toiles".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Un utilisateur disposant de cette autorisation peut effectuer l'une des actions suivantes dans le flux de travail Canvas :

- Approuver mais ne pas lancer le Canvas
- Lancer mais ne pas approuver le Canvas
- Approuver et lancer le Canvas
- Ni approuver ni lancer le Canvas

Une fois les statuts d'approbation définis à l'étape du **canvas**, toute modification ultérieure apportée au canvas réinitialisera tous les statuts d'approbation lorsqu'elle sera enregistrée. Cela s'applique à toutes les modifications apportées à un projet de canvas ou à un canvas postérieur au lancement. Par exemple, si vous ne modifiez que l'audience cible, l'étape **Résumé** ramènera les statuts d'approbation de toutes les sections à l'état par défaut, c'est-à-dire en attente.
{% endtab %}
{% endtabs %}

{% alert important %}
Pour modifier une campagne en ligne/en production/instantanée, vous devez disposer de l'autorisation "Approuver et refuser des campagnes". Un utilisateur devra approuver ses modifications puisqu'une version provisoire des campagnes n'est pas encore disponible. Ce n'est pas le cas pour les Canvas, car un utilisateur peut apporter des modifications et enregistrer un brouillon, et un autre utilisateur peut approuver et lancer le Canvas.
{% endalert %}
