---
nav_title: Connaissance des fonctionnalités et nouvelle version de l’application
article_title: Connaissance des fonctionnalités et nouvelle version de l’application
page_order: 7
page_type: reference
description: "Le présent article de référence explique comment maintenir vos utilisateurs informés et enthousiastes lorsque vous publiez de nouvelles fonctionnalités ou versions."
tool: Campaigns

---

# Connaissance des fonctionnalités et nouvelle version de l’application

> Le présent article de référence explique comment utiliser la plateforme Braze pour tenir vos clients informés des nouvelles fonctionnalités et versions de votre application. 

Vous travaillez dur pour mettre à jour et améliorer constamment votre application et vous voulez que vos utilisateurs puissent découvrir ces nouvelles fonctionnalités passionnantes ainsi que les nouvelles versions de l’application.  Apprenez à présenter à vos utilisateurs les nouvelles fonctionnalités qu’ils n’ont pas encore utilisées et encouragez-les à explorer l’application afin d’en tirer parti au mieux.

## Pourquoi utiliser des campagnes de sensibilisation aux fonctionnalités

Les campagnes de sensibilisation sont un excellent moyen d’encourager les utilisateurs à rester engagés avec votre application tout en continuant à améliorer ses fonctionnalités.  Tenir les utilisateurs à jour est un excellent moyen de les maintenir actifs, de stimuler les évaluations et de garantir leur engagement.

## Filtrer par versions d’application les plus récentes

Le SDK Braze suit automatiquement la version d’application la plus récente de l’utilisateur. Ces versions peuvent être utilisées dans des filtres et des segments pour déterminer quels utilisateurs doivent recevoir un message ou une campagne.

![Le volet « Targeting Options » (Options de ciblage) de l’étape « Target Users » (Utilisateurs cibles) dans le flux de travail de création de la campagne. La section « Additional Filters » (Filtres supplémentaires) comprend le filtre suivant « Le numéro de version le plus récent pour Android Stopwatch (Android) est inférieur à 3.7.0 (134.0.0.0) ».][1]

### Numéro de version de l’application

Utilisez le filtre **App Version Number** (Numéro de version de l’application) pour segmenter les utilisateurs par version d’application et selon son numéro. 

Ce filtre prend en charge des comparaisons numériques pour cibler plusieurs versions de votre application. Par exemple, vous pouvez cibler les utilisateurs dont l’application est « en dessous », « au-dessus » et « égale à » la version « 1.2.3 » de l’application, ce qui pourrait être bénéfique pour promouvoir une nouvelle fonctionnalité nécessitant une mise à niveau de l’application.

Ce nouveau filtre peut remplacer le filtre historique « App Version Name » (Nom de la version d’application) qui nécessitait de répertorier explicitement chaque version antérieure ou d’utiliser une expression régulière.

**Fonctionnement**

* Chaque partie de la version `major.minor.patch` envoyée dans votre version de l’application est comparée en tant qu’entiers
* Si les nombres majeurs sont égaux, les nombres mineurs sont comparés, etc.

**Important**

* Les applications Android possèdent à la fois un [`versionName`][7] lisible par les humains et un [`versionCode`][9] interne. Le filtre du numéro de version de l’application utilise `versionCode` car il est toujours incrémenté avec chaque sortie dans l’app store.
* Cela peut entraîner une confusion lorsque le `versionName` et le `versionCode` de l’application ne sont pas synchronisés, en particulier parce que les deux champs peuvent être consultés depuis le tableau de bord de Braze. En tant que bonne pratique, assurez-vous que le `versionName` et le `versionCode` de votre application sont incrémentés en même temps.
* Si vous devez filtrer par le champ `versionName` lisible par les humains (peu fréquent), utilisez le filtre « App Version Name » (Nom de version de l’application).

#### Exigences SDK

Les valeurs de ce filtre sont obtenues à partir du SDK Braze pour Android v3.6.0 et ultérieures et du SDK pour iOS v3.21.0 et ultérieures. Bien que ce filtre ait des exigences SDK, vous serez toujours en mesure de cibler les utilisateurs qui sont sur des versions plus basses (plus anciennes) de votre application en utilisant cette fonctionnalité !

Pour Android, ce numéro de version est basé sur le [Package Long Version Code][9] (Code en version longue du package) de l’application.

Pour iOS, ce numéro de version est basé sur la [Short Version String][8] (Chaîne de caractères en version courte) de l’application.

{% alert tip %}
Ce filtre renseignera les valeurs une fois que les utilisateurs auront mis à niveau leurs applications vers les versions du SDK Braze prises en charge. Jusque là, le filtre n’affichera aucune version lorsque cette option est sélectionnée.
{% endalert %}

#### Exemples de scénarios

Dans le scénario suivant, supposons que vous avez d’abord mis à niveau les SDK Braze qui prennent en charge ce filtre dans la version `2.0.0` de votre application.

Une fois que Braze reçoit les données de la version 2.0.0 de votre application, vous pouvez cibler les utilisateurs ayant des versions antérieures ou ultérieures.

| Filtrer  | Version d’application de l’utilisateur  | Résultat |
:------------- | :----------- | :---------|
| Inférieure à 2.0.0 | 1.0.0 | L’utilisateur se trouve dans le segment, même si son SDK Braze n’a pas pris en charge le filtre « App Version Number » (Numéro de version de l’application). |
| Supérieure à 2.0.0 | 2.5.1 | L’utilisateur et toutes les installations futures seront dans le segment. |
| Supérieure à 2.0.0 | 1.9.9 | L’utilisateur n’est pas dans le segment. |
| Inférieure ou égale à 2.0.0 | 3.0.1 | L’utilisateur n’est pas dans le segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Nom de version de l’application

Utilisez le filtre « App Version Name » (Nom de version de l’application) pour segmenter les utilisateurs par nom de version de l’application. 

Ce filtre prend en charge la correspondance avec « est », « n’est pas » et les expressions régulières. Par exemple, vous pouvez cibler les utilisateurs qui ont une application qui n’est pas la version « 1.2.3-test-build ».

Pour Android, ce nom de version est basé sur le [Package Version Name][7] (Nom de version du package) de l’application. Pour iOS, ce nom de version est basé sur la [Short Version String][8] (Chaîne de caractères en version courte) de l’application.

### N’a pas utilisé la fonctionnalité

Lorsque vous sortez une nouvelle version d’application et ajoutez de nouvelles fonctionnalités, les utilisateurs peuvent ne pas remarquer le nouveau contenu.  Exécuter une campagne de sensibilisation à la fonctionnalité est un excellent moyen de présenter aux utilisateurs les nouvelles fonctionnalités ou celles qu’ils n’ont jamais utilisées. Pour ce faire, vous devez créer un [attribut personnalisé][3] qui est assigné aux utilisateurs qui n’ont jamais effectué une action donnée dans votre application ou qui utilise un [événement personnalisé][4] pour suivre une action particulière.  Vous pouvez utiliser cet attribut (ou événement) pour segmenter les utilisateurs à qui vous souhaitez envoyer la campagne.

## Bonnes pratiques

### Soyez convaincant

Persuader un utilisateur de mettre à jour son application ou changer la façon dont il utilise votre application peut être difficile.  Assurez-vous de leur faire connaître tous les avantages de la nouvelle version ou des nouvelles fonctionnalités et la manière dont elles amélioreront leur expérience avec votre application.  Informez-les de l’avantage pratique qu’ils en tireront et des avantages qu’ils manqueront s’ils choisissent de ne pas mettre à jour ou d’utiliser les nouvelles fonctionnalités.

### Envoyez au bon moment

Convaincre vos utilisateurs de mettre à jour leur application peut être difficile car ils doivent se rendre sur l’App Store pour le faire.  En général, il est préférable de demander aux utilisateurs de mettre à jour dès que l’application est mise à jour, cependant, s’ils choisissent de ne pas le faire, ne les noyez pas sous les messages. Patientez plutôt jusqu’à ce qu’ils aient une expérience positive dans l’application, par exemple, en battant un niveau, en échangeant un bon de réduction ou en mettant une chanson en favori.

Pour les campagnes de sensibilisation aux fonctionnalités, le timing est également clé.  L’onboarding doit familiariser les utilisateurs avec l’application, cependant, les utilisateurs peuvent oublier des fonctionnalités ou ne pas remarquer les nouvelles. Lorsque de nouvelles fonctionnalités sont ajoutées, assurez-vous de prévenir vos utilisateurs. Si tout va bien, les utilisateurs découvriront facilement les nouvelles fonctionnalités. Cependant, si les utilisateurs n’interagissent pas avec des fonctionnalités majeures de l’application, il est préférable de les leur rappeler. Faites-le lorsqu’ils s’engagent avec votre application et lorsque la fonctionnalité non utilisée serait utile.

### Utilisez des canaux non intrusifs

Étant donné qu’ils sont relativement intrusifs, les notifications push et les e-mails qui demandent aux utilisateurs de mettre à jour peuvent paraître désespérés s’ils sont envoyés trop souvent. Veillez à utiliser une stratégie multicanale lorsque vous faites votre demande, en vous concentrant sur les canaux d’application si possible. Les [messages in-app][5] et [cartes de contenu][6] perturbent moins et sont facilement ignorés si l’utilisateur ne souhaite pas mettre à jour immédiatement. Assurez-vous d’inclure des liens profonds vers l’app store approprié. Les messages in-app simples qui indiquent de nouvelles fonctionnalités peuvent constituer un excellent moyen d’exposer les utilisateurs à de nouveaux contenus sans se mettre en travers de leur chemin ou les encombrer avec des messages.


[1]: {% image_buster /assets/img_archive/new_app_version.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/
[7]: https://developer.android.com/reference/android/content/pm/PackageInfo#versionName
[8]: https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring
[9]: https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()
