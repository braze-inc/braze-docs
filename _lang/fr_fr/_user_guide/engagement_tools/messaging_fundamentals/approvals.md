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

> Veuillez utiliser les validations pour ajouter un dernier point de contrôle à vos campagnes et canevas avant leur lancement. Grâce à ce flux de travail, vous pouvez vérifier et approuver le contenu de toutes les sections obligatoires de votre message.

## Fonctionnement

Vous pouvez examiner les détails de votre campagne ou de votre canvas lors de la dernière étape de modification. 

Pour les canevas et les campagnes, il est impératif d'enregistrer toutes les modifications avant de les approuver, même s'il s'agit de vos propres modifications. Un utilisateur disposant des autorisations appropriées doit approuver chaque section du résumé avant que le message puisse être envoyé. Le statut par défaut de chaque section est " **En attente d'approbation"**.

{% tabs %}
{% tab campaign %}
Pour lancer une campagne, il est nécessaire d'approuver les éléments suivants :

- **Messages :** Ceci est le message de la campagne.
- **Livraison :** Il s'agit du type de réception/distribution qui détermine quand les utilisateurs reçoivent la campagne.
- **Audience cible :** Ceci détermine qui recevra la campagne.
- **Événements de conversion :** Il s'agit de l'indicateur que vous suivez à des fins d'engagement et de rapports.
{% endtab %}

{% tab canvas %}
Pour lancer un canvas, vous devez approuver ces éléments clés :

- **Événements de conversion :** Il s'agit de l'indicateur que vous suivez à des fins d'engagement et de rapports.
- **Planification d’entrée :** Cela inclut le type de planification d'inscription et le moment où les utilisateurs accèdent à Canvas.
- **Audience cible :** Cela permet de déterminer qui entrera dans cette toile.
- **Envoyer les paramètres :** Il s'agit des options d'envoi pour toutes les étapes du canvas. 
- **Créer un canvas :** Il s'agit du parcours de l'utilisateur de Canvas.
{% endtab %}
{% endtabs %}

## Activation du processus d'approbation

Par défaut, le paramètre de workflow d'approbation est désactivé pour les campagnes et les canevas. Pour activer cette fonctionnalité, accédez à **Paramètres** > **Flux d'approbation** et basculez sur la case correspondante :

- **Veuillez utiliser le processus de validation pour toutes les campagnes dans [votre espace de travail].**
- **Veuillez utiliser le processus de validation pour toutes les canevas dans [votre espace de travail].**

{% alert important %}
L'approbation des campagnes n'est pas prise en charge pour [les campagnes API]({{site.baseurl}}/api/api_campaigns) et [les campagnes d'e-mails transactionnels]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Définition des autorisations utilisateur

Après avoir activé le workflow d'approbation, il est nécessaire de définir les autorisations des utilisateurs afin que les membres de votre entreprise puissent approuver ou refuser des campagnes et des canvases. Ces deux autorisations peuvent également être appliquées aux espaces de travail ou aux [Teams,]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) ou ajoutées à un [ensemble d'autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Vous devez disposer de l'[autorisation "Approuver et refuser des campagnes".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Cette autorisation permet de contrôler qui peut mettre à jour le statut d'approbation d'une campagne. Avec cette autorisation, vous pouvez effectuer les opérations suivantes :

- Veuillez approuver la campagne.
- Veuillez approuver et lancer la campagne.
- Approuver la campagne sans la lancer (un autre utilisateur disposant de l'autorisation « Envoyer des campagnes, des canevas » peut lancer la campagne)
- Ne pas approuver ni lancer la campagne

Une fois les statuts d'approbation définis à l'étape **Résumé**, toute modification ultérieure apportée à la campagne réinitialise tous les statuts d'approbation lorsqu'elle est enregistrée. Ceci s'applique à toute modification apportée soit à un projet de campagne, soit à une campagne après son lancement. Par exemple, si vous modifiez uniquement le public cible, l'étape **Résumé** rétablit le statut d'approbation par défaut, **En attente d'approbation**, pour toutes les sections.

{% endtab %}

{% tab canvas %}
Vous devez avoir l'[autorisation "Approuver et refuser des toiles".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Cette autorisation détermine qui peut mettre à jour le statut d'approbation d'un canvas. Avec cette autorisation, vous pouvez effectuer les opérations suivantes :

- Veuillez approuver vous-même le canvas.
- Approuver et lancer le Canvas
- Approuver mais ne pas lancer le Canvas (un autre utilisateur disposant de l'autorisation « Envoyer des campagnes, des Canvases » peut lancer le Canvas)
- Ne pas approuver ni lancer le Canvas

Une fois les statuts d'approbation définis à l'étape **Résumé**, toute modification ultérieure apportée au canvas réinitialise tous les statuts d'approbation lorsqu'il est enregistré. Cela s’applique à toutes les modifications effectuées dans une ébauche de Canvas ou un Canvas après lancement. Par exemple, si vous modifiez uniquement l'audience cible, l'étape **Résumé** rétablit le statut d'approbation par défaut, **En attente d'approbation**, pour toutes les sections.

{% alert note %}
**Statut d'approbation et enregistrement**

- Lorsque vous cliquez sur **Approuver** pour une section de l'étape **Résumé**, cette approbation est immédiatement enregistrée.
- Le bouton **Enregistrer** permet d'enregistrer les modifications apportées au contenu et aux paramètres de canvas, mais pas le statut d'approbation.

Pour éviter de perdre des autorisations :

1. Modifiez les éléments nécessaires dans Canvas, puis cliquez sur **Enregistrer**.
2. Une fois l'enregistrement terminé, veuillez approuver les sections pertinentes à l'étape **Résumé**.
3. Veuillez cliquer à nouveau **sur** **Enregistrer** uniquement si vous apportez des modifications supplémentaires à canvas après approbation. Si vous modifiez le canvas et enregistrez, tous les statuts d'approbation seront réinitialisés à **« En attente d'approbation** ».
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Pour modifier une campagne en ligne/en production/instantanée, vous devez disposer de l'autorisation « Approuver et refuser des campagnes ». L'utilisateur doit approuver ses modifications, car la version préliminaire de Campaigns n'est pas encore disponible. Ce n'est pas le cas pour les Canvas, car un utilisateur peut apporter des modifications et enregistrer un brouillon, et un autre utilisateur peut approuver et lancer le Canvas.
{% endalert %}