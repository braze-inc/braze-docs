---
nav_title: Configuration du groupe d’apps
article_title: Configuration du groupe d’apps
page_order: 1
description: "Cet article de référence couvre la configuration du groupe d’apps et la création de votre groupe d’apps."

---

# Configuration du groupe d’apps

Braze organise vos applications via  « App Groups » (Groupe d’apps). Pensez à chacun de ces groupes d’apps comme titre individuel. Par exemple, vous devez regrouper les versions iOS et Android de la même application ou des versions gratuites et payantes. Ces deux applications doivent être dans le même groupe pour permettre la navigation, la segmentation et la messagerie sur les deux plateformes.

## Création de votre groupe d’apps dans « My Apps » (Mes applications)

### Étape 1 : Cliquez sur le bouton « Add App Group » (Ajouter un groupe d’apps) <i class='icon-plus'> </i> dans la barre latérale

![][3]

Saisissez le nom de votre groupe d’apps dans le formulaire.

Une fois que vous avez créé votre groupe d’apps, vous serez redirigé vers la page **Settings** (Paramètres). En général, vous pouvez accéder à cette page en naviguant jusqu’à l’onglet **Apps** en haut de la page et en appuyant sur <i class='icon-cog'></i> sur la barre latérale.

![][4]

### Étape 2 : Ajoutez vos applications

En utilisant le formulaire en haut de votre écran, sélectionnez votre plateforme, saisissez le nom de votre application et cliquez sur « Add App » (Ajouter une application)

- Après avoir ajouté votre application, vous aurez accès à sa clé API, que vous aurez besoin d’intégrer au SDK.
    - Vous devez créer des instances d’application distinctes pour chaque version de votre application sur chaque plateforme. Par exemple, si vous possédez des versions gratuites et Pro de votre application sur iOS et Android, vous aurez 4 instances d’application dans votre groupe d’apps et vous devez utiliser la clé API qui est générée pour chaque application.

![La page de paramétrage du groupe d’apps montrant les différentes applications au sein d’un groupe d’apps. Dans cet exemple, quatre instances de l’application similaires représentent les différentes versions de leur application.][5]

### Étape 3 : Ajouter un groupe d’apps de test

Braze recommande de créer un « groupe d’apps de test » pour l’intégration et les tests de campagne. La fonction Groupe d’apps peut également être utilisée pour les tests d’applications en isolant complètement certains utilisateurs de votre instance de production. Créez simplement un nouveau groupe d’apps et n’oubliez pas de changer vos codes API pour que vos environnements de production ne soient pas corrompus avec de fausses données. Lorsque vous publiez votre application, assurez-vous de modifier la clé API que Braze utilise pour correspondre à celle de votre « groupe d’apps de production » plutôt que votre « groupe d’apps de test »"

## Plusieurs applications dans un seul groupe d’apps

L’intérêt de regrouper plusieurs applications au sein d’un même groupe d’apps peut être séduisant, car il permet une limitation du débit de messagerie sur l’ensemble de votre portefeuille d’applications. Cependant, en tant que meilleure pratique, nous suggérons de ne regrouper sous un même groupe d’apps que différentes versions d’une même application ou d’applications très similaires. Par exemple, vos versions iOS et Android de la même application ou vos versions gratuites et premium de la même application.

Quelles que soient les applications que vous choisissez d’avoir dans un groupe d’apps, leurs données seront agrégées, ce qui aura un impact notable sur les filtres de Braze :

- Dernière application utilisée
- Première application utilisée
- Nombre de sessions
- Somme dépensée
- Abonnement de notification push (cela devient une situation tout ou rien, si vos utilisateurs se désabonnent d’une application, ils seront désabonnés de toutes vos applications sous le groupe d’apps)
- Abonnement par e-mail (cela devient une situation tout ou rien et peut vous exposer à des problèmes de conformité)

Il ne s’agit pas d’une liste exhaustive. L’agrégation des données sur des applications dissemblables dans des filtres comme ceux énumérés est la raison pour laquelle nous ne recommandons pas de proposer des applications sensiblement différentes au sein du même groupe d’apps.

## Gestion des groupes d’apps lors de la réinitialisation de votre application

Si les utilisateurs doivent simplement mettre à jour l’application et qu’il ne s’agit pas d’une nouvelle application publiée dans l’App Store, vous ne devez pas créer un nouveau groupe d’apps si vous prévoyez de toujours envoyer des messages aux utilisateurs sur la version ancienne.

En créant un nouveau groupe d’apps, toutes les données et tous les profils historiques de la version ancienne de votre application n’existeront pas dans ce nouveau groupe d’apps. Ainsi, lorsque les utilisateurs existants passeront à la nouvelle version de l’application, un nouveau profil est créé, qui ne contient aucune donnée comportementale de l’ancienne application. De plus, cet utilisateur existe sur l’ancien groupe d’apps et le nouveau groupe d’apps et peut avoir le même jeton de notification push. Si cela se produit, il peut conduire des utilisateurs qui reçoivent un message marketing « mise à niveau maintenant » destiné uniquement aux anciens utilisateurs du groupe d’apps, même s’ils ont déjà été mis à niveau.

La meilleure façon de procéder si vous souhaitez séparer l’ancienne et la nouvelle application est de créer une nouvelle application au sein du même groupe d’apps. De cette façon, vous pouvez cibler uniquement les utilisateurs sur la nouvelle version en sélectionnant cette application lorsque vous créez vos segments. Si vous souhaitez envoyer des messages à des utilisateurs qui sont toujours sur l’ancienne version, vous pouvez utiliser [Liquid pour sélectionner l’ancienne application et filtrer la version précédente de l’application](https://learning.braze.com/target-different-app-versions-with-liquid/929971).

[3]: {% image_buster /assets/img_archive/add_appgroup.png %}
[4]: {% image_buster /assets/img_archive/new_app_landing.png %} "Braze Settings"
[5]: {% image_buster /assets/img_archive/App_Setup_API.png %} "Braze API Input"
