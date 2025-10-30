---
nav_title: "Sensibilisation aux fonctionnalités et nouvelle version de l'application"
article_title: "Sensibilisation aux fonctionnalités et nouvelle version de l'application"
page_order: 9
page_type: reference
description: "Cet article de référence explique comment garder vos utilisateurs informés et enthousiastes lorsque vous lancez de nouvelles fonctionnalités ou versions."
tool: Campaigns

---

# Sensibilisation aux fonctionnalités et nouvelle version de l'application

> Cet article de référence aborde la manière d'utiliser la plateforme Braze pour tenir vos clients au courant des nouvelles fonctionnalités et versions de votre appli. 

Vous travaillez dur pour mettre à jour et améliorer continuellement votre application, et vous voulez que vos utilisateurs fassent l'expérience de ces nouvelles fonctionnalités passionnantes et des nouvelles versions de l'application. Apprenez à faire découvrir à vos utilisateurs les nouvelles fonctionnalités qu'ils n'ont pas encore utilisées, et encouragez-les à explorer l'appli pour tirer le meilleur parti de ce que vous avez à offrir.

Les campagnes de sensibilisation aux fonctionnalités sont un excellent moyen d'encourager les utilisateurs à rester engagés dans votre application tout en continuant à en améliorer les fonctionnalités.  Tenir les utilisateurs à jour est un excellent moyen de les garder actifs, d'augmenter les taux d'évaluation et de garantir l'engagement des utilisateurs.

## Filtrage en fonction des versions les plus récentes de l'application

Les SDK de Braze suivent automatiquement la version la plus récente de l'application de l'utilisateur. Ces versions peuvent être utilisées dans des filtres et des segments pour déterminer quels utilisateurs doivent recevoir un message ou une campagne.

Le panneau Options de ciblage de l'étape Cibler les utilisateurs dans le flux de travail pour créer une campagne. La section Filtres supplémentaires comprend le filtre suivant : "Le numéro de version le plus récent de l'application Android Stopwatch (Android) est inférieur à 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Il peut s'écouler un certain temps avant que les versions actuelles de l'application ne soient mises à jour. La version de l'app sur le profil utilisateur se met à jour lorsque les informations sont capturées par le SDK, qui s'appuie sur le moment où les utilisateurs ouvrent leurs apps. Si l'utilisateur n'ouvre pas l'application, la version actuelle ne sera pas mise à jour. <br><br> Ces filtres ne s'appliquent pas non plus rétroactivement. Il est bon d'utiliser "supérieur à" ou "égal à" pour les versions actuelles et futures, mais l'utilisation de filtres de versions antérieures peut entraîner des comportements inattendus.
{% endalert %}

### Numéro de version de l'application

Utilisez le filtre **Numéro de version de l'** appli pour segmenter les utilisateurs en fonction de la version et du numéro de création de l'appli. 

Ce filtre prend en charge les comparaisons numériques pour cibler une gamme de versions d'applis. Par exemple, vous pouvez cibler les utilisateurs dont l'application est "inférieure", "supérieure" et "égale" à la version "1.2.3" de l'application, ce qui peut être utile pour promouvoir une nouvelle fonctionnalité qui nécessite une mise à jour de l'application.

Ce nouveau filtre peut remplacer l'ancien filtre "Nom de la version de l'application" qui nécessiterait de lister explicitement chaque ancienne version ou d'utiliser une expression régulière.

**Comment cela fonctionne-t-il ?**

* Chaque partie de la version `major.minor.patch` envoyée dans la version de votre application est comparée sous forme d'entiers.
* Si les nombres majeurs sont égaux, les nombres mineurs sont comparés, etc.

**Important**

* Les applications Android ont à la fois un [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) lisible par l'homme et un [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()). Le filtre App Version Number utilise `versionCode` parce qu'il est garanti qu'il est incrémenté à chaque version de l'app store.
* Cela peut prêter à confusion lorsque les sites `versionName` et `versionCode` de votre application ne sont pas synchronisés, d'autant plus que les deux champs peuvent être consultés depuis le tableau de bord de Braze. En guise de bonne pratique, vérifiez que les adresses `versionName` et `versionCode` de votre application sont incrémentées en même temps.
* Si vous avez besoin de filtrer par le champ `versionName` lisible par l'homme (peu courant), utilisez le filtre App Version Name (Nom de la version de l'application).

#### Exigences du SDK

Les valeurs de ce filtre sont collectées à partir de Braze Android SDK v3.6.0+ et iOS SDK v3.21.0+. Même si ce filtre nécessite un SDK, vous pourrez toujours cibler les utilisateurs qui utilisent des versions inférieures (plus anciennes) de votre application grâce à cette fonctionnalité !

Pour Android, ce numéro de version est basé sur le [code long de version](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) du [paquet de](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) l'application.

Pour iOS, ce numéro de version est basé sur la [chaîne de caractères de la version courte de](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) l'app.

{% alert tip %}
Ce filtre s'enrichira de valeurs après que les utilisateurs auront mis à jour leurs applications vers les versions du SDK de Braze prises en charge. En attendant, le filtre n'affichera aucune version lorsqu'il sera sélectionné.
{% endalert %}

#### Cas d'utilisation

Dans le scénario suivant, supposons que vous ayez d'abord effectué une mise à niveau vers les SDK de Braze qui prennent en charge ce filtre dans la version `2.0.0` de votre application.

Une fois que Braze reçoit les données de la version 2.0.0 de votre appli, vous pouvez cibler les utilisateurs dont la version est antérieure ou postérieure.

| Filtre  | Version de l'application de l'utilisateur  | Résultat |
:------------- | :----------- | :---------|
| Moins de 2.0.0 | 1.0.0 | L'utilisateur est dans le segment, même si son SDK Braze ne prenait pas en charge le filtre "Numéro de version de l'appli". |
| Supérieur à 2.0.0 | 2.5.1 | L'utilisateur et toutes les installations futures se trouveront dans la segmentation. |
| Supérieur à 2.0.0 | 1.9.9 | L'utilisateur n'est pas dans le segment. |
| Inférieur ou égal à 2.0.0 | 3.0.1 | L'utilisateur n'est pas dans le segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Nom de la version de l'application

Utilisez le filtre "Nom de la version de l'application" pour segmenter les utilisateurs en fonction du "nom de la version" de l'application. 

Ce filtre prend en charge les correspondances avec "is", "is not" et les expressions régulières. Par exemple, vous pouvez cibler les utilisateurs dont l'application n'est pas de la version "1.2.3-test-build".

Pour Android, ce nom de version est basé sur le [nom de version du paquet de](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) l'application. Pour iOS, ce nom de version est basé sur la [chaîne de caractères de la version courte de](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) l'app.

### N'a pas utilisé la fonctionnalité

Lorsque vous publiez une nouvelle version de l'app et introduisez de nouvelles fonctionnalités, les utilisateurs peuvent ne pas remarquer le nouveau contenu. L'organisation d'une campagne de sensibilisation aux fonctionnalités est un excellent moyen de faire découvrir aux utilisateurs de nouvelles fonctionnalités ou des fonctionnalités qu'ils n'ont jamais utilisées. Pour ce faire, vous devez créer un [attribut personnalisé]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) attribué aux utilisateurs qui n'ont jamais effectué une certaine action au sein de votre appli ou utiliser un [événement personnalisé]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) pour assurer le suivi d'une action particulière. Vous pouvez utiliser cet attribut (ou événement) pour segmenter les utilisateurs auxquels vous souhaitez envoyer la campagne.

{% alert tip %}
Vous cherchez à recibler une partie spécifique de votre audience ? Consultez les [campagnes de reciblage]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) pour apprendre à recibler les campagnes en exploitant les actions précédentes de votre utilisateur.
{% endalert %}


