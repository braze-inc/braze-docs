---
nav_title: Configuration du groupe d’apps
article_title: Configuration du groupe d’apps
page_order: 1
description: "Cet article de référence couvre la configuration d’un seul et de plusieurs groupes d’apps, comment créer votre groupe d’apps et comment cibler et relancer votre application."

---

# Configuration du groupe d’apps

> Cet article explique comment créer et configurer un groupe d’apps et présente certaines des meilleures pratiques à conserver à l’esprit lors du regroupement des applications.

## Qu’est-ce qu’un groupe d’apps ?

Les groupes d’apps sont des groupes où vous organisez vos applications. Pensez à chacun de ces groupes d’apps comme titre individuel. Par exemple, vous devez regrouper les versions iOS et Android de la même application ou vos versions gratuites et premium de la même application. Le regroupement de ces applications dans le même groupe d’app facilite la navigation, la segmentation et l’envoi de messages sur les deux plates-formes.

## Créer un groupe d’apps

![][3]{: style="max-width:40%;float:right;margin-left:15px;"} 

### Étape 1 : Ajouter votre groupe d’apps

1. Sélectionnez le groupe d’apps dans le menu déroulant et cliquez sur <i class="fas fa-plus"></i> **New App Group (Nouveau groupe d’apps)**.
2. Nommez votre groupe d’apps. 
   - Vous pouvez adopter une convention de dénomination afin de permettre à vos collègues de retrouver facilement votre groupe d’apps. Par exemple : *FinanceApp - Production* et *FinanceApp - Development*.
3. Cliquez sur **Add App Group (Ajouter un groupe d’apps)** pour confirmer.

Vous arrivez ensuite à la page **Settings (Paramètres)**. En général, vous pouvez accéder à cette page en accédant à **Manage Settings (Gestion des paramètres** > **Settings (Paramètres)**.

### Étape 2 : Ajoutez vos applications

1. Sur la page **Settings (Paramètres)**, cliquez sur <i class="fas fa-plus"></i> **Add App (Ajouter une application)**.
2. Nommez l’application et choisissez la plateforme.
3. Cliquez sur **Add App (Ajouter une application)** pour confirmer.

Après avoir ajouté votre application, vous aurez accès à sa clé API. La clé API est utilisée lorsque vous effectuez des demandes entre votre application et l’API Braze. La clé API est également importante pour intégrer le SDK Braze à votre application. 

Vous devez créer des instances d’application distinctes pour chaque version de votre application sur chaque plateforme. Par exemple, si vous possédez des versions gratuites et Pro de votre application sur iOS et Android, créez quatre instances d’applications dans votre groupe d’apps (application iOS gratuite, application Android gratuite, application iOS Pro et application Android Pro). Cela vous donnera quatre clés API à utiliser, une pour chaque instance d’application.

{% alert tip %}
La **Live SDK Version** affichée sur la page **Settings (Paramètres)** pour une application spécifique est la version la plus élevée de l’application avec au moins 5 % de vos sessions quotidiennes totales et dispose d’au moins de 500 sessions effectuées la veille.
{% endalert %}

#### Ajouter un groupe d’apps de test

Braze recommande de créer un groupe d’apps de test pour l’intégration et les tests de campagne. Vous pouvez également réaliser des tests d’applications mettant complètement en « sandbox » certains utilisateurs de votre instance de production. Créez simplement un nouveau groupe d’apps et n’oubliez pas de changer vos codes API pour que vos environnements de production ne soient pas corrompus avec de fausses données. Lorsque vous publiez votre application, assurez-vous de modifier la clé API que Braze utilise pour correspondre à celle de votre groupe d’apps de production plutôt que votre groupe d’apps de test.

## Plusieurs applications dans un seul groupe d’apps

Il peut être intéressant de regrouper plusieurs applications sous un groupe d’apps pour tenter d’optimiser la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) de l’intégralité de votre portefeuille d’applications. Cependant, en tant que meilleure pratique, nous suggérons de ne regrouper sous un même groupe d’apps que différentes versions d’une même application ou d’applications très similaires. 

Les données de toutes les applications appartenant au même groupe d’apps seront cumulées. Ceci aura un effet notoire sur les filtres dans Braze. Par exemple, sans s’y limiter, sur les filtres suivants :

- Dernière application utilisée
- Première application utilisée
- Nombre de sessions
- Argent dépensé
- Abonnement aux notifications push
  - Si vos utilisateurs se désabonnent d’une application, ils seront désabonnés de toutes vos applications sous le groupe d’apps).
- Abonnement e-mail
  - Ceci peut provoquer des problèmes de conformité.

L’agrégation des données sur des applications dissemblables dans les filtres susmentionnés est la raison pour laquelle nous ne recommandons pas de proposer des applications sensiblement différentes au sein du même groupe d’apps.

## Ciblage d’une seule application

Toute référence à un segment pour cibler une seule application désigne l’utilisation des cases à cocher sous **Apps Used (Applications utilisées)** dans l’outil de segmentation. Vous devez utiliser un segment conforme aux critères de sélection d’une seule application pour être certain que vous ciblez bien une seule application.

### Campagnes

Pour les campagnes, il est nécessaire de le préciser lors de l’étape d’entrée ou de **ciblage d’audience** de votre construction de campagne. Vous devez utiliser le segment que vous avez créé à l’aide des filtres case à cocher pour cibler seulement une des applications de votre groupe d’apps.

### Flux de travail de Canvas d’origine

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cet article est disponible dans un but de référence afin de comprendre les segments et le ciblage dans l’éditeur d’origine.<br><br>Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos Canvas en Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

Pour le flux de travail de Canvas d’origine, il est nécessaire de préciser le segment des composants du Canvas pour cibler une application spécifique lorsqu’un utilisateur peut avoir deux jetons de notification push vers différentes applications dans le même groupe d’apps. Sinon, le flux de travail va rechercher l’utilisateur et envoyer à toutes les applications disponibles. Il n’est pas nécessaire de segmenter au niveau de l’entrée.

### Canvas Flow

[Flux Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#canvas-flow) fonctionne comme le flux de travail Canvas original pour savoir comment les utilisateurs sont envoyés d’une étape à l’autre. Utilisez la fonctionnalité Validations de livraison dans l’Étape Message pour segmenter à nouveau les utilisateurs. Vous devez spécifier la validation de livraison à chaque étape de message pour garantir qu’il sera livré à l’application souhaitée. Tout comme le flux de travail d’origine, il n’est pas nécessaire de segmenter au niveau de l’entrée. 

## Relancer votre application

Si les utilisateurs doivent simplement mettre à jour l’application et qu’il ne s’agit pas d’une nouvelle application publiée dans l’App Store, vous ne devez pas créer un nouveau groupe d’apps si vous prévoyez de toujours envoyer des messages aux utilisateurs sur l’ancienne version.

En créant un nouveau groupe d’apps, toutes les données et tous les profils historiques de l’ancienne version de votre application n’existeront pas dans ce nouveau groupe d’apps. Ainsi, lorsque les utilisateurs existants passeront à la nouvelle version de l’application, un nouveau profile sera créé sans aucune des données comportementales de l’ancienne application. En outre, cet utilisateur existera dans l’ancien groupe d’apps et dans le nouveau groupe d’apps. Il pourra peut-être également avoir le même jeton de notification push. Cela peut conduire des utilisateurs à recevoir un message marketing destiné uniquement aux anciens utilisateurs du groupe d’apps, même s’ils ont déjà été mis à niveau.

Pour séparer les applications anciennes et nouvelles, créez une nouvelle application dans le même groupe d’apps. De cette façon, vous pouvez cibler uniquement les utilisateurs sur la nouvelle version en sélectionnant cette application au cours de la segmentation. Si vous souhaitez envoyer des messages à des utilisateurs qui sont toujours sur l’ancienne version, vous pouvez utiliser [Liquid pour sélectionner l’ancienne application et filtrer la version précédente de l’application](https://learning.braze.com/target-different-app-versions-with-liquid/929971).

[3]: {% image_buster /assets/img_archive/add_appgroup.png %}
