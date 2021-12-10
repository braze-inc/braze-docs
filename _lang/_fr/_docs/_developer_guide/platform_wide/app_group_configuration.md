---
nav_title: Configuration du groupe d'applications
article_title: Configuration du groupe d'applications
page_order: 1
description: "Cet article de référence couvre la configuration du groupe d'applications et la façon de créer votre groupe d'applications."
---

# Configuration du groupe d'applications

Braze organise vos applications via "Groupes d'applications". Pensez à chacun de ces groupes d'applications comme titre individuel. Par exemple, vous devriez regrouper les versions iOS et Android de la même application ou d'une version gratuite et payante. Ces deux applications devraient être dans le même groupe pour faciliter la navigation, la segmentation et la messagerie sur les deux plateformes.

## Création de votre groupe d'applications dans "Mes applications"

### Étape 1 : Cliquez sur le bouton "<i class='icon-plus'> </i>  Ajouter un groupe d'application" dans la barre latérale

!\[Ajouter un groupe d'applications\]\[3\]

Tapez le nom de votre groupe d'applications dans le formulaire.

Une fois que vous avez créé votre groupe d'applications, vous serez dirigé vers la page des paramètres. Généralement, vous pouvez accéder à cette page en accédant à l'onglet Applications en haut de la page et en appuyant sur l'icône <i class='icon-cog'></i> sur la barre latérale.

!\[Paramètres Braze\]\[4\]

### Étape 2 : Ajouter vos applications

En utilisant le formulaire en haut à droite de votre écran, sélectionnez votre plate-forme, tapez le nom de votre application et cliquez sur "Ajouter l'application"

- Après avoir ajouté votre application, vous aurez accès à sa clé d'API, dont vous aurez besoin pour compléter l'intégration du SDK.
    - Vous devez créer des instances d'application distinctes pour chaque version de votre application sur chaque plateforme. Par exemple, si vous avez des versions gratuites et Pro de votre application sur iOS et Android, vous aurez 4 applications dans votre groupe d'applications et devez utiliser la clé API appropriée qui est générée pour chaque application.

!\[Braze API Input\]\[5\]

### Étape 3 : Ajouter un groupe d'applications de test

Braze vous recommande de créer un « groupe d'applications de test » pour les tests d'intégration et de campagne. La fonctionnalité Groupe d'applications peut également être utilisée pour les tests d'application en intégrant complètement sandboxing certains utilisateurs de votre instance de production. Créez simplement un nouveau groupe d'applications et n'oubliez pas de changer vos codes API pour que vos environnements de production ne soient pas corrompus par de fausses données. Lorsque vous publiez votre application, assurez-vous de changer la clé API que Braze utilise pour correspondre à celle de votre "Groupe d'applications de production" plutôt que de votre "Groupe d'applications de test"

## Plusieurs applications dans un seul groupe d'applications

Le tirage pour avoir plusieurs applications sous un seul groupe d'applications peut être attrayant car cela peut conduire à la possibilité de limiter le taux de messagerie dans l'ensemble de votre portefeuille d'applications. Cependant, en tant que meilleure pratique, nous suggérons de ne regrouper que des versions différentes d'applications identiques ou très similaires dans un seul groupe d'applications. Par exemple, vos versions iOS et Android de la même application ou de vos versions gratuites et premium de la même application.

Quelles que soient les applications que vous choisissez d'avoir dans un groupe d'applications auront leurs données agrégées qui auront un impact notable sur les filtres au Brésil :

- Dernière application utilisée
- Première application utilisée
- Nombre de sessions
- Argent dépensé
- Abonnement Push (cela devient une situation totale ou nulle, si vos utilisateurs se désabonnent d'une seule application, ils seront désabonnés de toutes vos applications sous le groupe d'applications)
- Abonnement par e-mail (cela devient une situation totale ou nulle et peut vous laisser ouvert à des problèmes de conformité)

Il ne s'agit pas d'une liste exhaustive. L'agrégation des données à travers des applications différentes dans des filtres comme ceux listés ci-dessus est pourquoi nous ne recommandons pas de loger des applications sensiblement différentes au sein du même groupe d'applications.

## Gérer les groupes d'applications lors de la relance de votre application

Si les utilisateurs devront simplement mettre à jour l'application et ce n'est pas une nouvelle application qui sera publiée dans l'app store, vous ne devriez pas créer un nouveau groupe d'applications si vous prévoyez de toujours envoyer des messages aux utilisateurs sur l'ancienne version.

En créant un nouveau groupe d'applications, toutes les données historiques et les profils de l'ancienne version de votre application n'existeront pas dans ce nouveau groupe d'applications. Ainsi, une fois les utilisateurs existants mis à niveau vers la nouvelle version de l'application, ils auront un nouveau profil créé qui ne contient aucune des données de comportement de l'ancienne application. De plus, cet utilisateur existera à la fois dans l'ancien groupe d'applications et dans le nouveau groupe d'applications et peut potentiellement avoir le même jeton push. Si cela se produit, cela peut conduire à ce que les utilisateurs reçoivent un message marketing « mise à niveau maintenant » destiné aux seuls utilisateurs des anciens groupes d'applications. même s’ils ont déjà été mis à jour.

La meilleure façon de procéder si vous voulez séparer l'ancien vs. une nouvelle application serait de créer une nouvelle application dans le même groupe d'applications. De cette façon, vous pouvez cibler efficacement uniquement les utilisateurs de la nouvelle version en sélectionnant cette application au fur et à mesure que vous créez vos segments. Si vous vouliez envoyer un message aux utilisateurs qui sont toujours sur l'ancienne version, vous pouvez utiliser [Liquid pour sélectionner l'ancienne application et filtrer la version précédente de l'application](https://www.youtube.com/watch?v=Dv__RAUwamA).
[3]: {% image_buster /assets/img_archive/add_appgroup.png %} [4]: {% image_buster /assets/img_archive/new_app_landing.png %} "Braze Settings" [5]: {% image_buster /assets/img_archive/App_Setup_API.png %} "Braze API Input"
