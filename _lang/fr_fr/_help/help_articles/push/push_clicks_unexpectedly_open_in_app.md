---
nav_title: "Les clics push s'ouvrent de manière inattendue dans l'application"
article_title: "Les clics push s'ouvrent de manière inattendue dans l'application"
page_type: solution
description: "Cet article d'aide explique comment résoudre les problèmes lorsqu'un lien push est censé s'ouvrir dans un navigateur web, et non dans l'application."
channel: push
---

# Les clics push s'ouvrent inopinément dans l'application

Si vous rencontrez des problèmes avec les liens dans les notifications push qui s'ouvrent inopinément dans votre application au lieu de votre navigateur web, il peut y avoir un problème avec la configuration de votre campagne ou la mise en œuvre du SDK. Reportez-vous à ces étapes pour obtenir de l'aide.

## Vérifier le comportement au clic

Dans votre campagne ou étape du canvas, vérifiez que l'option **Ouvrir l'URL web dans l'application mobile n** 'est pas sélectionnée. Si c'est le cas, effacez la sélection et relancez. 

![Le champ "Comportement au clic" de la configuration d'un push est défini sur "Ouvrir l'URL web" avec "Ouvrir l'URL web dans l'application mobile" non coché.]({% image_buster /assets/img/push_on_click.png %})

L'interaction par défaut pour l'action "Ouvrir une URL web" diffère selon la version du SDK. Pour les versions du SDK iOS 2.29.0 et Android 2.0.0 et plus, cette option est sélectionnée par défaut et les URL web s'ouvriront dans une vue web au sein de l'application. Avant ces versions, cette option est désactivée par défaut et les URL s'ouvrent dans le navigateur web par défaut de l'appareil.

Si ce n'est pas le cas, il se peut qu'il y ait un problème avec votre implémentation de push. 

## Double vérification de l'intégration de push

Si les liens de vos notifications push s'ouvrent dans l'appli de manière inattendue, cela peut être dû à des problèmes liés à votre intégration des notifications push ou à vos paramètres de personnalisation. Suivez les étapes suivantes pour résoudre les problèmes :

1. **Examinez la mise en œuvre du délégué à la poussée :** Veillez à ce que le délégué à la poussée de Braze soit correctement mis en œuvre. Pour des instructions détaillées, consultez le guide d'intégration des notifications push pour votre [plateforme]({{site.baseurl}}/developer_guide/home/).
2. **Contrôlez la gestion personnalisée des liens :** Vérifiez si l'application inclut un traitement personnalisé pour tous les liens `https://`. Les configurations personnalisées peuvent remplacer les comportements par défaut. Collaborez avec votre équipe de développement pour revoir et ajuster ces paramètres si nécessaire.
3. **Vérifiez l'enregistrement iOS push :** Pour iOS, revenez sur l'étape 1 du guide sur l'intégration push concernant l'[enregistrement des notifications push avec les APN]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Assurez-vous que votre objet délégué est assigné de manière synchrone avant que l'application ne finisse de se lancer. Cette étape doit être réalisée selon la méthode `application:didFinishLaunchingWithOptions:`.
4. **Testez votre intégration :** Après avoir effectué les ajustements, testez le comportement des notifications push sur les appareils iOS et Android pour confirmer que le problème est résolu.

Si le problème persiste, contactez le [service d'assistance de Braze]({{site.baseurl}}/support_contact) pour obtenir de l'aide.


*Dernière mise à jour le 6 décembre 2024*