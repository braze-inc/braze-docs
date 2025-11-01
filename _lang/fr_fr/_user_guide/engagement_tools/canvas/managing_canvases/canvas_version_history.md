---
nav_title: Historique des versions de Canvas
article_title: Historique des versions de Canvas
alias: "/canvas_version_history/"
page_order: 2
description: "Cet article de référence explique comment gérer l'historique des versions de Canvas."
page_type: reference
tool: Canvas
---

# Historique des versions de Canvas

> L'historique des versions vous permet de visualiser et d'accéder aux analyses/analytiques de Canvas et aux parcours des utilisateurs pour toute version antérieure de votre Canvas. 

Consulter l'historique des versions de votre Canvas peut s'avérer particulièrement utile pour conserver une trace de l'évolution d'un Canvas. Par exemple, si vous effectuez une modification à grande échelle, vous pouvez faire référence aux versions précédentes de Canvas pour mieux comprendre l'évolution de vos flux de travail.

## Gestion des versions

\![]({% image_buster /assets/img_archive/canvas_version_history.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Pour créer une nouvelle version, cliquez sur **Mettre à jour le canvas.** Cela vous permet d'apporter des modifications sans écraser la configuration précédente du Canvas. Lorsqu'une nouvelle version du Canvas est créée, les utilisateurs déjà présents dans le Canvas progresseront dans le flux de travail de la nouvelle version. Les utilisateurs qui entrent dans le Canvas entreront également dans la nouvelle version. 

Pour accéder à l'historique des versions, naviguez vers vos détails Canvas en haut de votre Canvas et sélectionnez **\# Versions**. Ici, vous avez accès à la barre latérale de l'**historique des versions.**  Sélectionnez l'une des versions de Canvas dans la barre latérale pour afficher et comparer les détails de Canvas. Pour basculer entre l'analyse/analytique du canvas et la configuration du canvas, cliquez sur **View Analytics** ou **View Canvas** dans la barre d'outils inférieure.

{% alert note %}
Les toiles listées sous **Historique des versions** sont en consultation seulement.
{% endalert %}

Pour afficher une liste des modifications apportées à une version pendant qu'elle était active, sélectionnez **Voir les modifications** dans la barre latérale de l'historique des versions. Vous pouvez également consulter toutes les modifications associées à une version dans le journal des modifications de Canvas. 

Notez que si vous n'avez effectué aucune modification entre le lancement d'un canvas et la création d'une deuxième version, aucun changement n'apparaîtra dans **Voir les modifications** pour la première version du canvas.

Au fur et à mesure que l'historique des versions augmente, vous pouvez également renommer chaque version dans la barre latérale pour rester organisé. Par défaut, les noms de version sont générés sous la forme d'un nombre basé sur le nombre de versions créées précédemment. Si vous renommez une version alors qu'elle n'est plus active, cela apparaîtra dans le journal des modifications de Canvas, mais pas dans le journal des modifications de la version dans la vue de l'historique des versions.

!exemple de journal des modifications de Canvas montrant que deux nouvelles versions de Canvas ont été créées.]({% image_buster /assets/img_archive/canvas_version_history_changelog.png %}){: style="max-width:85%" }

### Abandon des versions

Vous pouvez créer jusqu'à 10 versions par Canvas. Si vous atteignez cette limite, vous pouvez supprimer une version pour faire de la place à une nouvelle. Notez que les versions sont supprimées lorsque vous cliquez sur **Supprimer**, et non lorsque vous mettez à jour le canvas. L'abandon d'une version est reflété dans le journal des modifications de Canvas, et non dans le journal des modifications d'une version spécifique.

Si vous abandonnez une version, la configuration de Canvas sera immédiatement perdue, mais les analyses/analytiques associées à la version abandonnée seront conservées. 

## Visualisation de l'analyse/analytique (si utilisée anjective)

Dans l'historique des versions, vous pouvez consulter des analyses au niveau du canvas et des étapes. Dans la vue de la version Canvas, les données s'affichent pour l'ensemble de la plage de dates, et pas seulement pour la plage de dates de cette version. Cependant, au niveau des étapes, l'analyse/analytique ne sera affichée que pour les étapes qui existaient lorsque cette version était active. Ces analyses seront alimentées par des jours calendaires correspondant au fuseau horaire de votre entreprise, de sorte que les analyses ne seront pas spécifiques à l'heure exacte de la journée à laquelle la version a été créée.

