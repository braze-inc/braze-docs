---
nav_title: "Fuseaux horaires de l'espace de travail"
article_title: "Fuseaux horaires de l'espace de travail pour l'envoi de messages"
alias: /workspace_time_zones/
page_order: 3
description: "Cet article de référence explique comment configurer différents fuseaux horaires pour vos espaces de travail Braze, ce qui permet aux équipes opérant dans différentes localisations géographiques de mieux contrôler la planification des campagnes et des canvases."
---

# Fuseaux horaires de l'espace de travail pour l'envoi de messages

> Les fuseaux horaires des espaces de travail permettent aux administrateurs de définir des fuseaux horaires spécifiques pour chaque espace de travail. Cela permet aux campagnes de planification et aux Canvases (qui n'utilisent pas l'heure locale ou le timing intelligent) d'être envoyées selon le fuseau horaire désigné de l'espace de travail, plutôt que selon le fuseau horaire global de l'entreprise.

{% multi_lang_include early_access_beta_alert.md feature='Workspace time zones' %}

Par défaut, un nouvel espace de travail hérite du fuseau horaire défini pour votre entreprise. Les administrateurs peuvent remplacer cette valeur par défaut pour un ou plusieurs espaces de travail en utilisant les fuseaux horaires des espaces de travail. Lorsque le fuseau horaire d'un espace de travail est défini, les campagnes de planification et les canevas au sein de cet espace de travail se réfèrent à ce nouveau fuseau horaire pour leurs heures d'envoi.

Par exemple, si le fuseau horaire d'un espace de travail est défini sur PST et que la planification de la campagne dans cet espace de travail prévoit son envoi à 15 h PST, elle sera livrée à 15 h PST. Cela s'applique même si le fuseau horaire global de votre entreprise est différent (par exemple, EST, où 15 h PST correspond à 18 h EST).

## Gestion des fuseaux horaires de l'espace de travail

Si vous êtes administrateur, vous pouvez accéder aux fuseaux horaires de l'espace de travail et les gérer en vous rendant dans **Paramètres** > **Paramètres d'administration** > **Fuseaux horaires de l'espace de travail**.

Ici, vous pouvez consulter la liste de tous vos espaces de travail, leur fuseau horaire défini et la dernière fois où le fuseau horaire a été modifié. Veuillez utiliser la barre de recherche pour identifier des espaces de travail spécifiques par leur nom.

![Page « Fuseaux horaires des espaces de travail » présentant une liste des espaces de travail, leurs fuseaux horaires respectifs et la date de la dernière modification des fuseaux horaires.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### Définition d'un fuseau horaire 

{% alert note %}
La mise à jour du fuseau horaire peut prendre quelques minutes avant de prendre effet.
{% endalert %}

{% tabs %}
{% tab Single workspace %}
1. Veuillez localiser l'espace de travail souhaité dans la liste.
2. Veuillez sélectionner l'icône **Modifier** à côté du nom de l'espace de travail.

![Bouton « Modifier » à côté du nom d'un espace de travail.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3\. Dans le menu déroulant, veuillez sélectionner le fuseau horaire souhaité pour cet espace de travail.
4\. Sélectionnez **Enregistrer**.

![Menu déroulant avec le fuseau horaire GMT sélectionné.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab Multiple workspaces %}

Vous pouvez appliquer un fuseau horaire spécifique à plusieurs espaces de travail simultanément en procédant comme suit :

1. Veuillez cocher les cases à côté de tous les espaces de travail que vous souhaitez mettre à jour.
2. Veuillez sélectionner **Modifier le fuseau horaire**.
3. Dans le menu déroulant, veuillez sélectionner un fuseau horaire à appliquer à tous les espaces de travail sélectionnés.

![Page « Fuseaux horaires de l'espace de travail » avec plusieurs espaces de travail sélectionnés et un bouton « Modifier le fuseau horaire ».]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4\. Sélectionnez **Enregistrer**. 

{% endtab %}
{% endtabs %}

## Impact sur les campagnes et les canvases

{% alert important %}
Veuillez informer les équipes et les parties prenantes concernées au sein de chaque espace de travail de tout changement de fuseau horaire afin d'éviter toute confusion concernant la planification des campagnes.
{% endalert %}

- **Campagnes « heure locale » et « heure intelligente » :** Les campagnes et les canevas qui utilisent l'heure locale de l'utilisateur ou [l'heure intelligente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#option-3-intelligent-timing) pour la réception/distribution continueront de fonctionner comme auparavant et ne seront pas affectés par les fuseaux horaires de l'espace de travail.
- **Campagnes de planification et canevas :** Toute campagne ou Canvas qui n'utilise pas l'heure locale de l'utilisateur ou l'heure intelligente pour la réception/distribution sera désormais envoyée en fonction du fuseau horaire sélectionné dans l'espace de travail.
- **Campagnes de planification avant un changement de fuseau horaire :** Si vous avez effectué la planification d'une campagne ou d'un canvas avant de modifier le fuseau horaire de l'espace de travail, Braze conserve l'heure d'envoi d'origine et ne la reprogramme pas. Par exemple, si une campagne est programmée pour être envoyée à 19 h PST et que le fuseau horaire de l'espace de travail est modifié pour passer à EST, la campagne sera toujours envoyée à 19 h PST (ce qui correspond désormais à 22 h EST). Le système continuera à se référer à l'heure d'origine, mais l'interprétera selon le nouveau fuseau horaire de l'espace de travail.

## Impact sur les filtres d'audience basés sur la date

Lorsque le fuseau horaire d'un espace de travail est mis à jour, les filtres d'audience qui utilisent des critères basés uniquement sur la date (sans heure spécifique) sont réévalués en fonction des limites du nouveau fuseau horaire.

Pour les filtres tels que « Dernière action personnalisée X après », Braze utilise le fuseau horaire de l'espace de travail pour déterminer le début et la fin du jour du calendrier. La modification de ce paramètre modifie l'heure limite de 23 h 59 pour cette date spécifique.

### Exemple

Un espace de travail modifie son fuseau horaire, passant de l'heure de l'Est (EST) à l'heure du Pacifique (PST).

- **Heure limite précédente :** 23 h 59 HNE
- **Nouvelle heure limite :** 23 h 59 PST (soit 2 h 59 EST le lendemain)

Suite à cette modification, un utilisateur qui effectue l'événement personnalisé à 22 h PST le 6 mars 2026 (soit 1 h EST le 7 mars 2026) est désormais inclus dans l'audience, car il se trouve dans les limites du calendrier PST pour cette date.

## Signaler des divergences

Les fuseaux horaires de l'espace de travail permettent un contrôle précis de l'envoi des campagnes, mais il est important de noter qu'il peut y avoir des divergences dans les rapports tant que cette fonctionnalité est en accès anticipé. Veuillez recouper les points de donnée et tenir compte du fuseau horaire lorsque vous analysez les rapports pour les espaces de travail avec des dérogations spécifiques en matière de fuseau horaire.