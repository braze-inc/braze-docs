---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes Push
page_order: 24
page_type: reference
description: "Cette page contient des étapes de résolution des problèmes pour divers problèmes liés au canal de communication Push."
channel: push
---

# Résolution des problèmes de la fonctionnalité Push

> Utilisez cette page pour résoudre les problèmes liés au canal de communication Push.

## Notifications push manquantes

Vous rencontrez des difficultés de distribution avec vos notifications push ? Plusieurs étapes vous permettent de résoudre ce problème en vérifiant :

- [Statut d'abonnement aux push](#push-subscription-status)
- [Segment](#segment)
- [Limites de notification push](#push-notification-caps)
- [Limites de débit](#rate-limits)
- [Statut du groupe de contrôle](#control-group-status)
- [Jeton push valide](#valid-push-token)
- [Type de notification push](#push-notification-type)
- [Application actuelle](#current-app)

#### Statut d'abonnement aux push

Les notifications push ne peuvent être envoyées qu'aux utilisateurs abonnés ou ayant explicitement donné leur accord. Vérifiez votre profil utilisateur dans l'onglet [Engagement]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) de la section **Profil utilisateur** pour confirmer que vous êtes activement inscrit aux push pour l'espace de travail que vous testez. Si vous êtes inscrit à plusieurs applications, vous les trouverez dans le champ **Push Registered For** :

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

Vous pouvez également exporter les profils utilisateur à l'aide des endpoints d'exportation de Braze :
- [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Utilisateurs par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Chaque endpoint renvoie un objet de jeton de notification push qui inclut des informations d'activation push par appareil.

#### Segment

Assurez-vous de faire partie du segment que vous ciblez (s'il s'agit d'une campagne en production et non d'un test). Dans le **Profil utilisateur**, vous verrez la liste des segments auxquels l'utilisateur appartient actuellement. N'oubliez pas qu'il s'agit d'une variable en constante évolution, car la segmentation est mise à jour en temps réel.

![Liste des segments]({% image_buster /assets/img_archive/trouble2.png %})

Vous pouvez également confirmer que l'utilisateur fait partie du segment en utilisant la **Recherche d'utilisateurs** lors de la création d'un segment.

![Section de recherche d'utilisateurs avec un champ de recherche.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Limites de notification push

Vérifiez les limites de fréquence globales. Il est possible que vous n'ayez pas reçu la notification push car votre espace de travail applique une limite de fréquence globale et que vous avez déjà atteint votre plafond de notifications push pour la période spécifiée.

Pour cela, vérifiez la [limite de fréquence globale]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) dans le tableau de bord. Si la campagne est configurée pour respecter les règles de limite de fréquence, un certain nombre d'utilisateurs seront affectés par ces paramètres.

![Détails de la campagne]({% image_buster /assets/img_archive/trouble3.png %})

#### Limites de débit

Si vous avez défini une limite de débit pour votre campagne ou Canvas, il est possible que vous ne receviez pas les messages en raison du dépassement de cette limite. Pour plus d'informations, consultez la section [Limitation du débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Statut du groupe de contrôle

S'il s'agit d'une campagne à canal unique ou d'un Canvas avec un groupe de contrôle, il est possible que vous fassiez partie du groupe de contrôle.

  1. Vérifiez la [distribution des variantes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) pour voir s'il existe un groupe de contrôle.
  2. Si c'est le cas, créez un segment filtrant par [groupe de contrôle de la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), puis [exportez le segment]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) et vérifiez si votre ID utilisateur figure dans cette liste.

#### Jeton push valide
Un jeton de notification push est un identifiant que les expéditeurs utilisent pour cibler des appareils spécifiques avec une notification push. Ainsi, si l'appareil ne dispose pas d'un jeton push valide, il n'y a aucun moyen de lui envoyer une notification push. 

#### Type de notification push

Vérifiez que vous utilisez le bon type de notification push. Par exemple, si vous souhaitez cibler un FireTV, vous devez utiliser une notification push Kindle et non une campagne push Android. De même, si vous souhaitez cibler un appareil Android, utilisez une notification push Android et non une campagne push iOS. Consultez les articles suivants pour en savoir plus sur les flux de travail dans Braze pour :
- [Apple Push Notification]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Application actuelle

Lorsque vous testez les envois push avec des utilisateurs internes, assurez-vous que l'utilisateur qui doit recevoir la notification push est actuellement connecté à l'application concernée. Dans le cas contraire, l'utilisateur pourrait ne pas recevoir la notification push, ou recevoir une notification push pour laquelle vous pensez qu'il n'est pas segmenté.

## Cliquer sur une notification push n'ouvre pas l'application

Si cliquer sur une notification push n'ouvre pas votre application, vérifiez les points suivants en fonction de votre plateforme.

### Android

1. **Vérifiez le comportement au clic :** Confirmez que la campagne est configurée pour ouvrir l'application lorsqu'on clique dessus.
2. **Vérifiez la gestion des liens profonds :** Dans votre fichier `braze.xml`, vérifiez si `com_braze_handle_push_deep_links_automatically` est défini sur `true` ou `false`.
   - S'il est défini sur `true`, le SDK Braze gère directement les liens profonds et l'application devrait s'ouvrir normalement.
   - S'il est défini sur `false`, votre application a besoin d'un récepteur de diffusion pour écouter et gérer les intentions de réception et d'ouverture des push. Vérifiez que ce récepteur est correctement implémenté.
3. **Collectez les journaux détaillés :** [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduisez le problème et fournissez les journaux ainsi que vos fichiers `braze.xml` et `AndroidManifest.xml` à l'assistance Braze.

### iOS

1. **Vérifiez le comportement au clic :** Confirmez que la campagne est configurée pour ouvrir l'application lorsqu'on clique dessus.
2. **Vérifiez l'intégration push :** La création de liens profonds depuis un push vers l'application est automatiquement gérée par l'[intégration push standard]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) de Braze. Confirmez que l'intégration est correctement implémentée, y compris toute gestion personnalisée des délégués.
3. **Collectez les journaux détaillés :** [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduisez le problème et fournissez les journaux à l'assistance Braze.

## Les clics push s'ouvrent de manière inattendue dans l'application

Si les liens de vos notifications push s'ouvrent de manière inattendue dans votre application au lieu de votre navigateur web, il peut y avoir un problème avec la configuration de votre campagne ou l'implémentation du SDK. Suivez ces étapes pour obtenir de l'aide.

### Vérifier le comportement au clic

Dans votre campagne ou étape du canvas, vérifiez que l'option **Ouvrir l'URL web dans l'application mobile** n'est pas sélectionnée. Si c'est le cas, décochez-la et relancez. 

![Champ « Comportement au clic » de la configuration d'un ensemble de notifications push réglé sur « Ouvrir l'URL Web » avec l'option « Ouvrir l'URL Web dans l'application mobile » décochée.]({% image_buster /assets/img/push_on_click.png %})

L'interaction par défaut pour le comportement au clic « Ouvrir l'URL web » diffère selon la version du SDK. Pour les versions du SDK iOS 2.29.0 et Android 2.0.0 et ultérieures, cette option est sélectionnée par défaut et les URL web s'ouvrent dans une vue web au sein de l'application. Avant ces versions, cette option est désactivée par défaut et les URL web s'ouvrent dans le navigateur web par défaut de l'appareil.

Si ce n'est pas le problème, il se peut qu'il y ait un souci avec votre implémentation push. 

### Revérifier l'intégration push

Si les liens de vos notifications push s'ouvrent dans l'application de manière inattendue, cela peut être dû à des problèmes liés à votre intégration des notifications push ou à vos paramètres de personnalisation. Suivez ces étapes pour résoudre le problème :

1. **Examinez l'implémentation du délégué push :** Assurez-vous que le délégué push de Braze est correctement implémenté. Pour des instructions détaillées, consultez le guide d'intégration des notifications push pour votre [plateforme]({{site.baseurl}}/developer_guide/home/).
2. **Vérifiez la gestion personnalisée des liens :** Vérifiez si l'application inclut un traitement personnalisé pour tous les liens `https://`. Les configurations personnalisées peuvent remplacer les comportements par défaut. Collaborez avec votre équipe de développement pour examiner et ajuster ces paramètres si nécessaire.
3. **Vérifiez l'enregistrement push iOS :** Pour iOS, revenez à l'étape 1 du guide d'intégration push concernant l'[enregistrement des notifications push avec les APN]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Assurez-vous que votre objet délégué est assigné de manière synchrone avant que l'application ne finisse de se lancer. Cette étape doit être réalisée dans la méthode `application:didFinishLaunchingWithOptions:`.
4. **Testez votre intégration :** Après avoir effectué les ajustements, testez le comportement des notifications push sur les appareils iOS et Android pour confirmer que le problème est résolu.

## Le titre du push est tronqué sur iOS mais s'affiche correctement sur Android

Si le titre de votre notification push contient une personnalisation Liquid et apparaît complet sur Android mais tronqué sur iOS, cela est dû à la manière dont chaque plateforme gère les caractères de retour à la ligne (`\n`) dans la chaîne de caractères du titre.

Android supprime automatiquement les espaces, tabulations et retours à la ligne des chaînes de caractères de titre push. iOS ne le fait pas : si une variable Liquid se résout en une valeur contenant un retour à la ligne final, iOS traite ce retour à la ligne comme la fin du titre et coupe le texte restant.

Par exemple, un titre comme `Regarding your flight from {% raw %}{{${city_from}}}{% endraw %} to {% raw %}{{${city_to}}}{% endraw %}` pourrait afficher `Regarding your flight from` sur iOS si la variable `city_from` inclut un retour à la ligne final.

Pour corriger cela, appliquez le filtre Liquid `strip_newlines` et encapsulez l'ensemble du titre dans un bloc `capture` :

{% raw %}
```liquid
{% capture title %}Regarding your flight from {{${city_from}}} to {{${city_to}}}{% endcapture %}
{{ title | strip_newlines }}
```
{% endraw %}

## Les notifications push web ne fonctionnent pas comme prévu

Si vous rencontrez des problèmes avec les notifications push dans votre navigateur, vous devrez peut-être réinitialiser les autorisations de notification de votre site et effacer le stockage de votre site. Suivez ces étapes pour obtenir de l'aide.

{% tabs %}
{% tab Chrome %}

### Réinitialiser Chrome sur ordinateur

1. À côté de votre URL dans le navigateur Chrome, sélectionnez l'icône du curseur **Afficher les informations sur le site**.
2. Sous **Notifications**, sélectionnez **Réinitialiser l'autorisation**.
3. Ouvrez Chrome DevTools. Voici les raccourcis pertinents pour chaque système d'exploitation.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Raccourcis clavier                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4. Dans DevTools, accédez à l'onglet **Application**.
5. Dans la barre latérale, sélectionnez **Storage**.
6. Sélectionnez **Clear site data**.
7. Chrome vous demandera de recharger la page pour appliquer les paramètres mis à jour. Sélectionnez **Reload**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez.

### Réinitialiser Chrome sur Android

Si une notification de votre site est visible dans le tiroir de notifications de votre Android :

1. Depuis la notification push, appuyez sur <i class="fas fa-cog" title="Paramètres"></i> et sélectionnez **Site settings**.
2. Depuis **Site settings**, appuyez sur **Clear & Reset**.

Si vous n'avez pas de notification de votre site ouverte :

1. Ouvrez Chrome sur Android.
2. Appuyez sur le menu <i class="fas fa-ellipsis-vertical"></i>.
3. Allez dans **Settings** > **Site Settings** > **Notifications**.
4. Vérifiez que les notifications sont configurées sur **Ask before sending (recommended)**.
5. Trouvez votre site dans la liste.
6. Sélectionnez l'entrée et appuyez sur **Clear and Reset**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez.

{% endtab %}
{% tab Firefox %}

### Réinitialiser Firefox sur ordinateur

1. À côté de l'URL de votre site, sélectionnez <i class="fa-solid fa-circle-info" alt="info icon"></i> ou <i class="fas fa-lock" alt="lock icon"></i>.
2. Sous **Permissions**, à côté de **Receive Notifications**, sélectionnez <i class="fa-solid fa-circle-xmark" title="Clear this permission and ask again"></i> pour supprimer les autorisations de notification.
3. Dans le même menu, sélectionnez **Clear Cookies and Site Data**.
4. Dans la boîte de dialogue de confirmation, sélectionnez **OK**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez.

### Réinitialiser Firefox sur Android

Pour réinitialiser les autorisations push sur Android, consultez cet [article d'assistance de Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Réinitialiser Safari sur macOS

{% alert note %}
Ces étapes s'appliquent uniquement à macOS, car Apple ne prend pas en charge Web Push pour Safari sur Windows.
{% endalert %}

1. Ouvrez Safari.
2. Depuis la [barre de menus sur Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), allez dans **Safari** > **Settings** > **Websites** > **Notifications**.
3. Sélectionnez votre site dans la liste.
4. Sélectionnez **Remove** pour supprimer les autorisations de notification pour le site.
5. Ensuite, allez dans **Privacy** > **Manage Website Data**.
6. Sélectionnez votre site dans la liste.
7. Sélectionnez **Remove** ou, pour supprimer toutes les données du site, sélectionnez **Remove All**.
8. Sélectionnez **Done**.

Vos autorisations push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez.

{% endtab %}
{% endtabs %}

## Messages d'erreur push

Pour des informations détaillées sur les messages d'erreur push courants (tels que `DEVICE_UNREGISTERED`, `Unregistered`, `NotRegistered`, et autres), consultez [Messages d'erreur push courants]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

Vous avez toujours besoin d'aide ? Ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).