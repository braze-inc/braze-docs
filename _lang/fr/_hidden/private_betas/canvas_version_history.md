---
nav_title: Historique des versions de Canvas
permalink: "/canvas_version_history/"
hidden: true
layout: dev_guide
---

# Historique des versions de Canvas

L’historique des versions vous permet d’afficher et d’accéder aux analytiques Canvas et aux parcours utilisateur de toutes les versions précédentes de votre Canvas. Cela peut être particulièrement utile pour tenir un registre de l’évolution d’un Canvas. Par exemple, si vous effectuez un changement à grande échelle, vous pouvez vous référer aux versions antérieures de Canvas pour mieux comprendre comment vos flux de travail ont progressé.

{% alert important %}
L’historique des versions pour Canvas Flow est actuellement en accès anticipé. Contactez votre CSM Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Gestion des versions

![][1]{: style="float:right;max-width:35%;margin-left:15px;"}

Pour créer une nouvelle version, cliquez sur **Update Canvas (Mettre à jour Canvas)**. Cela vous permet d’effectuer des modifications sans écraser la configuration précédente de Canvas. Lorsqu’une nouvelle version de Canvas est créée, les utilisateurs déjà dans Canvas progressent dans le flux de travail de la nouvelle version. Les utilisateurs qui entrent dans Canvas entreront également dans la nouvelle version. 

Pour accéder à l’historique des versions, accédez aux détails de votre Canvas en haut de celui-ci et sélectionnez **# Versions (Numéros des versions)**. Ici, vous avez accès à la barre latérale **Version history (Historique des versions)**. Sélectionnez l’une des versions du Canvas dans la barre latérale pour afficher et comparer les détails de celui-ci. Pour basculer entre les analytiques Canvas et la configuration Canvas, cliquez sur **View Analytics (Afficher les analytiques)** ou **View Canvas (Afficher le Canvas)** dans la barre d’outils inférieure.

{% alert note %}
Les Canvas répertoriés dans **Version history (Historique des versions)** sont en lecture seule.
{% endalert %}

Pour afficher une liste des modifications apportées à une version alors qu’elle était active, sélectionnez **View Changes (Afficher les modifications)** dans la barre latérale de l’historique des versions. Vous pouvez également afficher toutes les modifications associées à une version dans le journal de modifications Canvas. 

Notez que si vous n’avez apporté aucune modification entre le lancement d’un Canvas et la création d’une deuxième version, aucune modification n’apparaîtra dans **See Changes (Voir les modifications)** pour la première version du Canvas.

Au fur et à mesure que votre historique de versions augmente, vous pouvez également renommer chaque version dans la barre latérale pour rester organisé. Par défaut, les noms de version sont générés sous forme de nombre en fonction du nombre de versions précédemment créées. Si vous renommez une version alors qu’elle n’est plus active, elle apparaîtra dans le journal de modifications Canvas, mais pas dans le journal de modifications de la version dans l’affichage de l’historique des versions.

![Exemple de journal de modifications Canvas montrant que deux nouvelles versions Canvas ont été créées.][2]{: style="max-width:85%" }

### Suppression des versions

Vous pouvez créer jusqu’à 10 versions par Canvas. Si vous atteignez cette limite, vous pouvez supprimer une version pour faire de la place pour une nouvelle. Notez que les versions sont supprimées lorsque vous cliquez sur **Discard (Ignorer)**, et non lorsque vous mettez à jour le Canvas. La suppression d’une version est reflétée dans le journal de modifications global de Canvas, et non dans le journal de modifications d’une version spécifique.

Si vous rejetez une version, la configuration Canvas sera immédiatement perdue, mais les analyses associées à la version supprimée seront conservées. 

## Afficher l’analytique

Dans l’historique des versions, vous pouvez afficher l’analytique au niveau du Canvas et de ses étapes. Dans l’affichage de la version Canvas, les données seront renseignées pour toute la plage de dates, pas seulement pour la plage de dates de cette version. Cependant, au niveau de l’étape, l’analytique ne sera affichée que pour les étapes qui existaient alors que cette version était active. Ces analytiques se rempliront selon les jours civils correspondant au fuseau horaire de votre entreprise, de sorte qu’elles ne seront pas spécifiques à l’heure exacte de la journée où la version a été créée.

[1]: {% image_buster /assets/img_archive/canvas_version_history.png %} 
[2]: {% image_buster /assets/img_archive/canvas_version_history_changelog.png %}