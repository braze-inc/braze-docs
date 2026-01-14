---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes Push
page_order: 23
page_type: reference
description: "Cette page contient des étapes de résolution des problèmes pour divers problèmes liés au canal de communication Push."
channel: push
---

# Résolution des problèmes Push

> Cette page vous aide à résoudre les problèmes que vous pouvez rencontrer avec le canal de communication Push.

## Notifications push manquantes

Vous rencontrez des problèmes de réception/distribution avec les notifications push ? Vous pouvez prendre un certain nombre de mesures pour résoudre ce problème en vérifiant le :

- [Pousser l'état de l'abonnement](#push-subscription-status)
- [Segmentation](#segment)
- [Capuchons de notification push](#push-notification-caps)
- [Limites de débit](#rate-limits)
- [Statut du groupe de contrôle](#control-group-status)
- [Jeton de poussée valide](#valid-push-token)
- [Type de notification push](#push-notification-type)
- [Application actuelle](#current-app)

#### Pousser l'état de l'abonnement

Les pushs ne peuvent être envoyés qu'aux utilisateurs abonnés ou ayant opté pour un abonnement. Vérifiez votre profil utilisateur dans l'onglet [Engagement de]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) la section **Profil utilisateur** pour confirmer si vous êtes activement inscrit à push pour l'espace de travail que vous testez. Si vous êtes inscrit à plusieurs applications, vous les trouverez dans le champ **Poussée inscrite pour :** 

\![Poussée enregistrée pour]({% image_buster /assets/img_archive/trouble1.png %})

Vous pouvez également exporter les profils utilisateurs à l'aide des endpoints d'exportation de Braze :
- [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Utilisateurs par segmentation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

L'un ou l'autre de ces endpoints renverra un objet "jeton de poussée" contenant des informations sur l'activation de la poussée pour chaque appareil.

#### Segmentation

Assurez-vous d'appartenir au segment que vous ciblez (s'il s'agit d'une campagne en ligne/en production/instantanée). Dans le **profil utilisateur**, vous verrez une liste des segmentations dans lesquelles l'utilisateur se trouve actuellement. N'oubliez pas qu'il s'agit d'une variable en constante évolution, car la segmentation est mise à jour en temps réel.

!Liste des segmentations]({% image_buster /assets/img_archive/trouble2.png %})

Vous pouvez également confirmer que l'utilisateur fait partie de la segmentation en utilisant la **recherche d'utilisateurs** lors de la création d'un segment.

\![Section de recherche d'utilisateurs avec un champ de recherche.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Capuchons de notification push

Vérifiez les limites de fréquence globales. Il est possible que vous n'ayez pas reçu la notification push parce que votre espace de travail a mis en place une limite de fréquence globale et que vous avez déjà atteint votre limite de notification push pour la période spécifiée.

Vous pouvez le faire en cochant la case ["limite de fréquence globale"]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) dans le tableau de bord. Si la campagne est configurée pour respecter les règles de limitation de fréquence, un certain nombre d'utilisateurs seront concernés par ces paramètres.

!Détails de la campagne]({% image_buster /assets/img_archive/trouble3.png %})

#### Limites de débit

Si vous avez défini une limite de débit pour votre campagne ou votre Canvas, il se peut que vous ne receviez plus de messages parce que vous avez dépassé cette limite. Pour plus d'informations, reportez-vous à la section [Limitation du débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Statut du groupe de contrôle

S'il s'agit d'une campagne à canal unique ou d'un Canvas avec un groupe de contrôle, il est possible que vous tombiez dans le groupe de contrôle.

  1. Vérifiez la [distribution des variantes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) pour voir s'il existe un groupe de contrôle.
  2. Si c'est le cas, créez un segment filtrant pour le [groupe de contrôle de la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), [exportez]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) ensuite [le segment]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) et vérifiez si votre ID utilisateur figure dans cette liste.

#### Jeton de poussée valide
Un jeton push est un identifiant que les expéditeurs utilisent pour cibler des appareils spécifiques avec une notification push. Ainsi, si l'appareil ne dispose pas d'un jeton push valide, il n'y a aucun moyen de lui envoyer une notification push. 

#### Type de notification push

Vérifiez que vous utilisez le bon type de notification push. Par exemple, si vous souhaitez cibler une FireTV, vous utiliserez une notification push Kindle, et non une campagne push Android. De même, si vous souhaitez cibler un Android, utilisez une notification push Android et non une campagne push iOS. Consultez les articles suivants pour plus d'informations sur la compréhension du flux de travail de Braze :
- [Notification push d'Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Envoi de messages dans le nuage Firebase]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Application actuelle

Lorsque vous testez les envois push avec des utilisateurs internes, assurez-vous que l'utilisateur qui doit recevoir la notification push est actuellement connecté à l'application concernée. Cela peut conduire à ce que l'utilisateur ne reçoive pas de push ou reçoive un push pour lequel vous pensez qu'il n'est pas segmenté.

## Les clics push s'ouvrent inopinément dans l'application

Si vous rencontrez des problèmes avec les liens dans les notifications push qui s'ouvrent inopinément dans votre application au lieu de votre navigateur web, il peut y avoir un problème avec la configuration de votre campagne ou la mise en œuvre du SDK. Reportez-vous à ces étapes pour obtenir de l'aide.

### Vérifier le comportement au clic

Dans votre campagne ou étape du canvas, vérifiez que l'option **Ouvrir l'URL web dans l'application mobile n** 'est pas sélectionnée. Si c'est le cas, effacez la sélection et relancez. 

\!["Comportement au clic" champ de configuration d'un push set à "Ouvrir l'URL web" avec "Ouvrir l'URL web à l'intérieur de l'application mobile" décoché.]({% image_buster /assets/img/push_on_click.png %})

L'interaction par défaut pour l'action "Ouvrir une URL web" diffère selon la version du SDK. Pour les versions du SDK iOS 2.29.0 et Android 2.0.0 et plus, cette option est sélectionnée par défaut et les URL web s'ouvriront dans une vue web au sein de l'application. Avant ces versions, cette option est désactivée par défaut et les URL s'ouvrent dans le navigateur web par défaut de l'appareil.

Si ce n'est pas le cas, il se peut qu'il y ait un problème avec votre implémentation de push. 

### Double vérification de l'intégration de push

Si les liens de vos notifications push s'ouvrent dans l'appli de manière inattendue, cela peut être dû à des problèmes liés à votre intégration des notifications push ou à vos paramètres de personnalisation. Suivez les étapes suivantes pour résoudre les problèmes :

1. **Examinez la mise en œuvre du délégué à la poussée :** Veillez à ce que le délégué à la poussée de Braze soit correctement mis en œuvre. Pour des instructions détaillées, consultez le guide d'intégration des notifications push pour votre [plateforme]({{site.baseurl}}/developer_guide/home/).
2. **Contrôlez la gestion personnalisée des liens :** Vérifiez si l'application inclut un traitement personnalisé pour tous les liens `https://`. Les configurations personnalisées peuvent remplacer les comportements par défaut. Collaborez avec votre équipe de développement pour revoir et ajuster ces paramètres si nécessaire.
3. **Vérifiez l'enregistrement iOS push :** Pour iOS, revenez sur l'étape 1 du guide sur l'intégration push concernant l'[enregistrement des notifications push avec les APN]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Assurez-vous que votre objet délégué est assigné de manière synchrone avant que l'application ne finisse de se lancer. Cette étape doit être réalisée selon la méthode `application:didFinishLaunchingWithOptions:`.
4. **Testez votre intégration :** Après avoir effectué les ajustements, testez le comportement des notifications push sur les appareils iOS et Android pour confirmer que le problème est résolu.

## Les notifications push web ne se comportent pas comme prévu

Si vous rencontrez des problèmes avec les notifications push dans votre navigateur, vous devrez peut-être réinitialiser les autorisations de notification de votre site et effacer le stockage de votre site. Reportez-vous à ces étapes pour obtenir de l'aide.

{% tabs %}
{% tab Chrome %}

### Réinitialiser Chrome sur le bureau

1. À côté de votre URL dans le navigateur Chrome, sélectionnez l'icône de la barre de défilement " **View Site Information"**.
2. Sous **Notifications**, sélectionnez **Réinitialiser l'autorisation**.
3. Ouvrez Chrome DevTools. Vous trouverez ci-dessous les raccourcis pertinents pour chaque système d'exploitation.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Raccourcis clavier                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Fenêtres | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. Dans DevTools, accédez à l'onglet **Application**.
5\. Dans la barre latérale, sélectionnez **Stockage**.
6\. Sélectionnez **Effacer les données du site**.
7\. Chrome vous demandera de recharger la page pour appliquer les paramètres mis à jour. Sélectionnez **Recharger**.

Vos autorisations de push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez-le.

### Réinitialiser Chrome sur Android

Si une notification de votre site est visible dans le tiroir de notification de votre Android :

1. À partir de la notification push, appuyez sur <i class="fas fa-cog" title="Paramètres"></i> et sélectionnez **Paramètres du site**.
2. Dans les **paramètres du site**, appuyez sur **Effacer & Réinitialiser**.

Si vous n'avez pas reçu de notification de votre site, ouvrez-le :

1. Ouvrez Chrome sur Android.
2. Appuyez sur le menu <i class="fas fa-ellipsis-vertical"></i>.
3. Allez dans **Réglages** > **Réglages du site** > **Notifications**.
4. Vérifiez que les notifications sont définies sur **Demander avant l'envoi (recommandé).**
5. Trouvez votre site dans la liste.
6. Sélectionnez l'entrée et appuyez sur **Effacer et réinitialiser**.

Vos autorisations de push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez-le.

{% endtab %}
{% tab Firefox %}

### Réinitialiser Firefox sur le bureau

1. En regard de l'URL de votre site, sélectionnez <i class="fa-solid fa-circle-info" alt="info icon"></i> ou <i class="fas fa-lock" alt="lock icon"></i>.
2. Sous **Autorisations**, à côté de **Recevoir des notifications**, sélectionnez <i class="fa-solid fa-circle-xmark" title="Effacer cette autorisation et redemander"></i> pour supprimer les autorisations de notification.
3. Dans le même menu, sélectionnez **Effacer les cookies et les données du site**.
4. Dans la boîte de dialogue de confirmation de votre choix, sélectionnez **OK.**

Vos autorisations de push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez-le.

### Réinitialiser Firefox sur Android

Pour réinitialiser les autorisations push sur Android, reportez-vous à cet [article d'assistance de Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Réinitialiser Safari sur macOS

{% alert note %}
Ces étapes ne concernent que macOS, car Apple ne prend pas en charge Web Push pour Safari sous Windows.
{% endalert %}

1. Ouvrez Safari.
2. Dans la [barre de menus sur Mac,](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) accédez à **Safari** > **Réglages** > **Sites web** > **Notifications**.
3. Sélectionnez votre site dans la liste.
4. Sélectionnez **Supprimer** pour supprimer les autorisations de notification pour le site.
5. Ensuite, allez dans **Confidentialité** > **Gérer les données du site web.**
6. Sélectionnez votre site dans la liste.
7. Sélectionnez **Supprimer**, ou pour supprimer toutes les données du site, sélectionnez **Supprimer tout.**
8. Sélectionnez **Terminé**.

Vos autorisations de push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez-le.

{% endtab %}
{% endtabs %}

Vous avez encore besoin d'aide ? Ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).

