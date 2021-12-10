---
nav_title: Sensibilisation aux fonctionnalités et nouvelle version de l'application
article_title: Sensibilisation aux fonctionnalités et nouvelle version de l'application
page_order: 7
page_type: Référence
description: "Cet article de référence explique comment garder vos utilisateurs informés et enthousiastes quand vous publiez de nouvelles fonctionnalités ou versions."
tool: Campagnes
---

# Sensibilisation aux fonctionnalités et nouvelle version de l'application

> Cet article de référence explique comment utiliser la plateforme Braze pour tenir vos clients au courant des nouvelles fonctionnalités et versions de votre application.

Vous travaillez dur pour continuellement mettre à jour et améliorer votre application, et vous voulez que vos utilisateurs profitent de ces nouvelles fonctionnalités excitantes et de nouvelles versions d'applications.  Apprenez à enseigner aux utilisateurs les nouvelles fonctionnalités qu'ils n'ont pas encore utilisées, et les encourager à explorer l'application pour obtenir le maximum que vous avez à offrir.

## Pourquoi utiliser des campagnes de sensibilisation de fonctionnalités

Les campagnes de sensibilisation aux fonctionnalités sont un excellent moyen d'encourager les utilisateurs à rester engagés dans votre application tout en continuant à améliorer les fonctionnalités de votre application.  Garder les utilisateurs à jour est un excellent moyen de les maintenir actifs, d'augmenter les notes et d'assurer l'engagement des utilisateurs.

## Filtrage par les dernières versions de l'application

Braze SDKs suit automatiquement la version _de l'application_ la plus récente d'un utilisateur. Ces versions peuvent être utilisées dans les filtres et les segments pour déterminer quels utilisateurs doivent recevoir un message ou une campagne.

!\[Filtre de version de l'application\]\[1\]

### Numéro de version de l'application

Utilisez le filtre _Numéro de version_ pour segmenter les utilisateurs par le numéro de version/build de l'application.

Ce filtre prend en charge les comparaisons numériques pour cibler une gamme de versions d'applications. Par exemple, vous pouvez cibler les utilisateurs dont l'application est « ci-dessous», « ci-dessus» et « égale à» version de l'application « 1. .3", qui peut être bénéfique pour promouvoir une nouvelle fonctionnalité qui nécessite une mise à niveau de l'application.

Ce nouveau filtre peut remplacer le filtre "Nom de la version de l'application" qui nécessiterait explicitement de lister chaque version antérieure ou d'utiliser une expression régulière.

**Comment ça marche**

* Chaque partie de la version `major.minor.patch` envoyée dans la version de votre application est comparée à des entiers
* Si les nombres principaux sont égaux, les nombres mineurs sont comparés, etc.

**Important**

* Les applications Android ont à la fois un [`versionName`][7] lisible par l'homme et un [`versionCode`][9] interne. Le filtre du numéro de version de l'application utilise le `code de version` car il est garanti qu'il sera incrémenté avec chaque version de l'app store.
* Cela peut causer de la confusion lorsque le `versionName` et le `versionCode` de votre application sont désynchronisés, surtout puisque les deux champs peuvent être vus depuis le tableau de bord de Braze. En tant que bonnes pratiques, assurez-vous que le `versionName` et le `versionCode` de votre application sont incrémentés ensemble.
* Si vous avez besoin de filtrer par le champ `versionName` lisible par l'homme au lieu (rare), utilisez le filtre du nom de version de l'appli.

#### Exigences du SDK

Les valeurs pour ce filtre sont collectées à partir de Braze Android SDK v3.6.0+ et iOS SDK v3.21.0+. Même si ce filtre a des exigences de SDK, vous serez toujours en mesure de cibler les utilisateurs qui sont sur des versions inférieures (plus anciennes) de votre application en utilisant cette fonctionnalité !

Pour Android, ce numéro de version est basé sur le [Package Long Version Code][9] pour l'application.

Pour iOS, ce numéro de version est basé sur la [chaîne de version courte][8] pour l'application.

{% alert tip %}
Ce filtre remplira les valeurs une fois que les utilisateurs mettront leurs applications à niveau vers les versions supportées de Braze SDK. En attendant, le filtre n'affichera aucune version lorsqu'il sera sélectionné.
{% endalert %}

#### Exemples de scénarios

Dans le scénario suivant, supposons que vous avez d'abord mis à jour vers les SDK Braze qui prennent en charge ce filtre dans la version `2. .0` de votre application.

Une fois que Braze reçoit des données de la version 2.0.0 de votre application, vous pouvez cibler les utilisateurs ci-dessous ou au-dessus de cette version.

|  | Filtre                      | Version de l'application de l'utilisateur | Résultat                                                                                                                        |
|: |:--------------------------- |:----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
|  | _Moins de 2.0.0_            | 1.0.0                                     | L'utilisateur est dans le segment, même si son Braze SDK n'a pas pris en charge le filtre de numéro de version de l'application |
|  | _Supérieur à 2.0.0_         | 2.5.1                                     | Cet utilisateur, et toutes les installations futures seront dans le segment                                                     |
|  | _Supérieur à 2.0.0_         | 1.9.9                                     | L'utilisateur n'est pas dans le segment                                                                                         |
|  | _Inférieur ou égal à 2.0.0_ | 3.0.1                                     | L'utilisateur n'est pas dans le segment                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Nom de la version d'application

Utilisez le filtre _App Version Name_ pour segmenter les utilisateurs par le "nom de la version" de l'application.

Ce filtre supporte la correspondance avec "is", "n'est pas", et les expressions régulières. Par exemple, vous pouvez cibler les utilisateurs qui ont une application qui n'est pas la version "1.2.3-test-build".

Pour Android, le nom de cette version est basé sur le [Nom de la version du package][7] pour l'application.

Pour iOS, ce nom de version est basé sur la [chaîne de version courte][8] pour l'application.

### Fonctionnalité non utilisée

Lorsque vous publiez une nouvelle version de l'application et introduisez de nouvelles fonctionnalités, il se peut que les utilisateurs ne remarquent pas de nouveau contenu.  Lancer une campagne de sensibilisation aux fonctionnalités est un excellent moyen d'enseigner aux utilisateurs de nouvelles fonctionnalités ou fonctionnalités qu'ils n'ont jamais utilisées. Pour ce faire, vous devez créer un [attribut personnalisé][3] qui est attribué aux utilisateurs qui n'ont jamais terminé une certaine action dans votre application ou utiliser un [événement personnalisé][4] pour suivre une action particulière.  Vous pouvez utiliser cet attribut (ou l'événement) pour segmenter les utilisateurs vers lesquels vous voulez envoyer la campagne.

## Meilleures pratiques

### Soyez convaincant

Permettre à un utilisateur de mettre à jour son application ou de modifier la façon dont il utilise votre application peut être difficile.  Assurez-vous de leur indiquer tous les avantages de la nouvelle version/fonctionnalités et comment elle améliorera leur expérience avec votre application.  Faites-leur savoir tout l'utilitaire qu'ils gagneront, et les avantages qu'ils manqueront s'ils choisissent de ne pas mettre à jour ou de ne pas engager de nouvelles fonctionnalités.

### Envoyer au bon moment

Il peut être difficile de convaincre vos utilisateurs de mettre à jour leur application car ils doivent naviguer vers l'App Store pour le faire.  En général, il est préférable de demander aux utilisateurs de mettre à jour dès que l'application est mise à jour, Cependant, s'ils choisissent de ne pas les spammer avec des messages. Au contraire, attendez qu'ils aient une expérience positive dans l'application, par exemple en battant un niveau, en échangeant un coupon ou en favorisant une chanson.

Pour les campagnes de sensibilisation, le timing est également essentiel.  L'intégration devrait familiariser les utilisateurs avec l'application, mais les utilisateurs peuvent oublier les fonctionnalités ou ne pas remarquer les nouvelles fonctionnalités qui sont ajoutées. Lorsque de nouvelles fonctionnalités sont ajoutées, assurez-vous de prévenir vos utilisateurs. Espérons toutefois que les utilisateurs découvriront facilement de nouvelles fonctionnalités, si les utilisateurs ne s'engagent pas avec les fonctionnalités majeures de l'application, il est peut-être préférable de leur le rappeler. Faites-le quand ils s'engagent avec votre application et la fonctionnalité inutilisée serait utile.

### Utiliser des canaux non intrusifs

Parce qu'ils sont relativement intrusifs, les notifications push et les courriels qui demandent aux utilisateurs de mettre à jour peuvent s'avérer utiles s'ils sont envoyés trop souvent. Assurez-vous d'utiliser une stratégie multicanal lorsque vous faites votre demande, en vous concentrant sur les canaux de l'application si possible. Les cartes [messages intégrés][5] et [cartes de contenu][6] sont moins perturbantes et facilement ignorées si l'utilisateur ne souhaite pas mettre à jour immédiatement. Assurez-vous d'inclure des liens profonds vers le magasin d'application approprié. Des messages simples dans l'application signalant les nouvelles fonctionnalités peuvent être un excellent moyen d'exposer les utilisateurs à de nouveaux contenus sans les gêner et les encombrer de messages.
[1]: {% image_buster /assets/img_archive/new_app_version.png %}

[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/
[7]: https://developer.android.com/reference/android/content/pm/PackageInfo#versionName
[7]: https://developer.android.com/reference/android/content/pm/PackageInfo#versionName
[8]: https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring
[9]: https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()
[9]: https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()
