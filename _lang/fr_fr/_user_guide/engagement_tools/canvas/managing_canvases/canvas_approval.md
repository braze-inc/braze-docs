---
nav_title: Approbation et autorisations pour Canvas
article_title: Approbation et autorisations pour Canvas 
page_order: 0.5
alias: "/canvas_approval/"
description: "Cet article de référence explique comment approuver les canevas avant leur lancement et décrit les autorisations utilisateur correspondantes."
tool: Canvas
---

# Approbation et autorisations Canvas

> L’approbation des Canvas ajoute un processus de révision à votre flux de travail avant de le lancer. De cette manière, vous pouvez vérifier que chaque confirmation est approuvée afin de lancer le Canvas.

## Activer l’approbation Canvas

Pour activer le flux de travail d'approbation pour Canvas, accédez à **Paramètres** > **Flux de travail d'approbation** sous **Paramètres du lieu de travail**. Cette fonctionnalité est désactivée par défaut.

![Les paramètres du flux de travail d’approbation dans lesquels l’option d’utilisation du flux de travail d’approbation pour les campagnes et les Canvas est activée.][1]

{% alert tip %}
Vérifiez que vous disposez des [autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) nécessaires pour approuver les canvas.
{% endalert %}

### Définition des autorisations utilisateur

Une fois que le flux de travail d'approbation pour Canvas a été activé, allez dans **Paramètres** > **Utilisateurs de l'entreprise** et sélectionnez **Approuver et refuser les Canevas** pour permettre à des utilisateurs spécifiques d'approuver et de refuser les Canevas immédiatement. Cette autorisation peut également être appliquée à des espaces de travail ou à des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), ou être ajoutée à un [ensemble d'autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

Un utilisateur disposant de cette autorisation peut effectuer l'une des actions suivantes dans le flux de travail Canvas :
- Approuver mais ne pas lancer le Canvas
- Lancer mais ne pas approuver le Canvas
- Approuver et lancer le Canvas
- Ni approuver ni lancer le Canvas

![Exemple de case non cochée pour l'autorisation Approuver et refuser des canvas, ce qui signifie que cet utilisateur n'a pas le droit d'approuver ou de refuser les canvas.][3]{: style="max-width:70%" }

{% alert important %}
Pour modifier une campagne en cours, vous devez disposer de l'autorisation « Approuver et refuser des campagnes ». Un utilisateur devra approuver ses modifications car une version provisoire des campagnes n'est pas encore disponible. Ce n'est pas le cas pour les Canvas, car un utilisateur peut apporter des modifications et enregistrer un brouillon, et un autre utilisateur peut approuver et lancer le Canvas.
{% endalert %}

## Utiliser les approbations

Lorsque vous disposez de l'autorisation « Approuver et refuser des canvas », vous avez accès à l'étape **Résumé** du générateur de canvas. Cette page fournit un résumé des principaux détails de Canvas avec la possibilité d’approuver ou de refuser ces détails, y compris les événements de conversion, la planification d’entrée, ainsi que le type et la quantité de composants dans votre Canvas. Notez que l'état par défaut de l'approbation de canvas est **En attente d'approbation**.

Une fois les statuts d'approbation définis à l'étape du **canvas**, toute modification ultérieure apportée au canvas réinitialisera tous les statuts d'approbation lorsqu'elle sera enregistrée. Cela s’applique à toutes les modifications effectuées dans une ébauche de Canvas ou un Canvas après lancement. Par exemple, si vous ne modifiez que l'audience cible, l'étape **Résumé** ramènera les statuts d'approbation de toutes les sections à l'état par défaut, c'est-à-dire en attente.

![Exemple de flux de travail d'approbation de canvas où les détails des événements de conversion et de la planification d'entrée ont été marqués comme approuvés.][2]{: style="max-width:85%" }

Une fois que chaque section est approuvée, le bouton **Lancer** sera disponible et vous pourrez lancer votre Canvas.

[1]: {% image_buster /assets/img_archive/canvas_approval.png %}
[2]: {% image_buster /assets/img_archive/canvas_approval_summary.png %}
[3]: {% image_buster /assets/img_archive/canvas_approval_user_permissions.png %}