---
nav_title: Gestion des groupes d'applications
article_title: Gestion des groupes d'applications
page_order: 0
page_type: Référence
description: "Cet article de référence couvre la gestion des groupes d'applications dans votre tableau de bord Braze."
---

# Gestion des groupes d'applications

Vous pouvez gérer, segmenter et communiquer simultanément avec plusieurs applications à partir de la page **Gérer les paramètres** dans le tableau de bord de Braze.

!\[Gérer les appels de groupe d'application\]\[69\]

Les groupes d'applications sont conçus pour héberger des versions de la même application sur plusieurs plateformes. De nombreux clients Braze utilisent également des groupes d'applications pour contenir des versions gratuites et premium de leur application sur la même plateforme.

## Plusieurs applications dans un groupe d'applications

Il n'y a pas de limite au nombre d'applications pouvant exister dans un seul groupe d'applications. Le tirage pour avoir plusieurs applications dans un seul groupe d'applications peut être attractif, car il vous permet de noter la limite de la messagerie dans votre portefeuille d'applications. Cependant, en tant que meilleure pratique, nous vous suggérons de ne regrouper que des versions différentes des mêmes applications (ou très similaires) dans un seul groupe d'applications.

Par exemple, vous pouvez avoir vos versions iOS et Android de la même application dans un groupe d'applications, ou vos versions gratuites et premium de la même application dans un seul groupe d'applications.

Quelles que soient les applications que vous choisissez d'avoir dans un seul groupe d'applications, leurs données seront agrégées - ce qui aura un impact notable sur les filtres suivants au Brésil :

- Dernière application utilisée
- Première application utilisée
- Nombre de sessions
- Argent dépensé dans l'application
- Abonnement push (cela devient une situation totale ou nulle, si vos utilisateurs se désabonnent d'une seule application, ils sont désabonnés de toutes les applications du groupe d'application.)
- Abonnement par e-mail (cela devient une situation totale ou nulle, et peut vous laisser ouvert à des problèmes de conformité.)

Il ne s'agit pas d'une liste exhaustive.

## Administration des groupes d'applications

Nous recommandons d'avoir plusieurs utilisateurs Braze avec des autorisations d'administration pour un seul groupe d'applications. En règle générale, vous voulez vous assurer qu'il y a suffisamment de personnes avec votre organisation pour gérer les autorisations des autres utilisateurs.

## Renommer ou supprimer votre groupe d'applications

Pour renommer votre groupe d'applications, cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-pencil-alt" ></span>**Modifier** sur la page [Paramètres][19].

Pour supprimer entièrement votre groupe d'applications du tableau de bord, cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-cog" ></span>**Paramètres** sur la même page et sélectionnez **Supprimer le groupe d'applications**.

!\[appsettingsview1.png\]\[70\]

{% alert warning %}
Soyez prudent lorsque vous supprimez des groupes d'applications! Une fois qu'un groupe d'applications est supprimé, il ne peut pas être restauré.
{% endalert %}
[69]: {% image_buster /assets/img_archive/manageappgroupnavigation1.png %} [70]: {% image_buster /assets/img_archive/appsettingsview1.png %}

[19]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings Page"
