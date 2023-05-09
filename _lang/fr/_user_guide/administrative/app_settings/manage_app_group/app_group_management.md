---
nav_title: Gestion des groupes d’apps
article_title: Gestion des groupes d’apps
page_order: 0
page_type: reference
description: "Cet article de référence couvre les groupes d’apps dans votre tableau de bord de Braze. Vous trouverez ici des informations sur l’attrait d’avoir plusieurs groupes d’apps, comment supprimer votre groupe d’apps, etc."

---

# Gestion des groupes d’apps

> Les groupes d’apps sont conçus pour héberger les versions de la même application sur plusieurs plateformes. De nombreux clients de Braze utilisent également des groupes d’apps pour avoir des versions gratuites et premium de leur application sur la même plateforme.

Vous pouvez gérer, segmenter et communiquer avec plusieurs applications simultanément depuis la page **Manage Settings (Gérer les paramètres)** dans le tableau de bord de Braze.

{% alert note %}
Vous cherchez à savoir comment créer un nouveau groupe d’apps ? Consultez [Configuration du groupe d’apps]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/).
{% endalert %}

## Plusieurs applications dans un groupe d’apps

Il n’y a pas de limite au nombre d’applications pouvant exister dans un seul groupe d’apps. La possibilité de regrouper plusieurs applications au sein d’un même groupe d’apps peut s’avérer intéressante, car elle vous permet de limiter le débit de vos communications sur l’ensemble de votre portefeuille d’applications. Cependant, en tant que bonne pratique, nous suggérons de ne réunir que des versions différentes des mêmes applications (ou très similaires) dans un seul groupe d’apps.

Par exemple, les versions iOS et Android de la même application peuvent se trouver dans un seul groupe d’apps, ou les versions gratuites et premium de la même application dans un seul groupe d’apps.

Quelles que soient les applications que vous choisissez d’avoir dans un groupe d’apps, leurs données seront agrégées, ce qui aura un impact notable sur les filtres suivants dans Braze :

- Dernière application utilisée
- Première application utilisée
- Nombre de sessions
- Argent dépensé dans l’application
- Abonnement de notification push (Cela devient une situation tout ou rien, si vos utilisateurs se désabonnent d’une application, ils seront désabonnés de toutes les applications dans le groupe d’apps.)
- Abonnement par e-mail (Cela devient une situation tout ou rien et peut vous exposer à des problèmes de conformité.)

Il ne s’agit pas d’une liste exhaustive.

## Administration des groupes d’apps

Nous recommandons d’avoir plusieurs utilisateurs Braze avec des droits d’administration pour un seul groupe d’apps. En règle générale, vous devez vous assurer qu’il y a suffisamment de personnes dans votre organisation pour gérer les autorisations des autres utilisateurs.

## Renommer ou supprimer votre groupe d’apps

Pour renommer votre groupe d’apps, cliquez sur **Manage Settings (Gérer les paramètres)** dans la barre latérale gauche. Cliquez ensuite sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-pencil-alt" ></span>**Edit (Modifier)** à côté du nom de votre groupe d’apps.

Pour supprimer entièrement votre groupe d’apps du tableau de bord, cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-cog" ></span>**Settings (Paramètres)** sur la même page et sélectionnez **Delete App Group (Supprimer le groupe d’apps)**.

![Renommer le groupe d’apps dans l’onglet Settings (Paramètres)][70]

{% alert warning %}
Soyez prudent lorsque vous supprimez des groupes d’apps ! Une fois qu’un groupe d’apps est supprimé, il ne peut pas être restauré.
{% endalert %}

[69]: {% image_buster /assets/img_archive/manageappgroupnavigation1.png %}
[70]: {% image_buster /assets/img_archive/appsettingsview1.png %}
