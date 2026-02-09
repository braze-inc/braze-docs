---
nav_title: Historique des versions de Canvas
article_title: Historique des versions de Canvas
alias: "/canvas_version_history/"
page_order: 2
description: "Cet article de référence explique comment gérer l'historique des versions de votre Canvas."
page_type: reference
tool: Canvas
---

# Historique des versions de Canvas

> L’historique des versions vous permet d’afficher et d’accéder aux analyses Canvas et aux parcours utilisateur de toutes les versions précédentes de votre Canvas. 

Se référer à l'historique des versions de votre Canvas peut être particulièrement utile pour maintenir un enregistrement de l'évolution d'un Canvas. Par exemple, si vous effectuez un changement à grande échelle, vous pouvez vous référer aux versions précédentes de Canvas pour mieux comprendre comment vos flux de travail ont progressé.

## Gestion des versions

![]({% image_buster /assets/img_archive/canvas_version_history.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Pour créer une nouvelle version, cliquez sur **Mettre à jour Canvas**. Cela vous permet d’effectuer des modifications sans écraser la configuration précédente de Canvas. Lorsqu’une nouvelle version de Canvas est créée, les utilisateurs déjà dans Canvas progressent dans le flux de travail de la nouvelle version. Les utilisateurs qui entrent dans Canvas entreront également dans la nouvelle version. 

Pour accéder à l'historique des versions, accédez aux détails de votre Canvas en haut de votre Canvas et sélectionnez **\# Versions**. Ici, vous avez accès à la barre latérale **Historique des versions**. Sélectionnez l’une des versions du Canvas dans la barre latérale pour afficher et comparer les détails de celui-ci. Pour basculer entre les analyses de Canvas et la configuration de Canvas, cliquez sur **Voir les analyses** ou **Voir Canvas** dans la barre d'outils en bas.

{% alert note %}
Les toiles répertoriées sous **Historique des versions** sont en mode lecture seule.
{% endalert %}

Pour afficher la liste des modifications apportées à une version pendant qu'elle était active, sélectionnez **Afficher les modifications** dans la barre latérale de l'historique des versions. Vous pouvez également afficher toutes les modifications associées à une version dans le journal des modifications Canvas. 

Notez que si vous n'avez apporté aucune modification entre le lancement d'un Canvas et la création d'une deuxième version, aucun changement n'apparaîtra dans **Voir les modifications** pour la première version du Canvas.

Au fur et à mesure que votre historique de versions augmente, vous pouvez également renommer chaque version dans la barre latérale pour rester organisé. Par défaut, les noms de version sont générés sous forme de nombre en fonction du nombre de versions précédemment créées. Si vous renommez une version alors qu’elle n’est plus active, elle apparaîtra dans le journal des modifications Canvas, mais pas dans le journal des modifications de la version dans l’affichage de l’historique des versions.

![Exemple de journal des modifications de Canvas montrant que deux nouvelles versions de Canvas ont été créées.]({% image_buster /assets/img_archive/canvas_version_history_changelog.png %}){: style="max-width:85%" }

### Suppression des versions

Vous pouvez créer jusqu’à 10 versions par Canvas. Si vous atteignez cette limite, vous pouvez supprimer une version pour faire de la place pour une nouvelle. Notez que les versions sont supprimées lorsque vous cliquez sur **Supprimer**, et non lorsque vous mettez à jour le canvas. La suppression d’une version est reflétée dans le journal des modifications global de Canvas, et non dans le journal des modifications d’une version spécifique.

Si vous rejetez une version, la configuration Canvas sera immédiatement perdue, mais les analyses associées à la version supprimée seront conservées. 

## Afficher les analyses

Dans l’historique des versions, vous pouvez afficher l’analyse au niveau du Canvas et de ses étapes. Dans l’affichage de la version Canvas, les données seront renseignées pour toute la plage de dates, pas seulement pour la plage de dates de cette version. Cependant, au niveau de l’étape, l’analyse ne sera affichée que pour les étapes qui existaient alors que cette version était active. Ces analyses se rempliront en utilisant les jours du calendrier qui correspondent au fuseau horaire de votre entreprise, de sorte que les analyses ne seront pas spécifiques à l'heure exacte de la journée où la version a été créée.

