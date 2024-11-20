---
nav_title: Intégration
article_title: Intégration de notifications push pour le Web
platform: Web
channel: push
page_order: 0
page_type: reference
description: "Cet article décrit comment intégrer les notifications push Braze pour le Web via le SDK Braze."

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'
search_rank: 3
---

# Intégration de notifications Push

> Une notification push est une alerte qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Vous pouvez recevoir des notifications push même lorsque votre page Web n’est pas actuellement ouverte dans le navigateur de l’utilisateur. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les ré-engager avec votre site. Cet article de référence présente comment intégrer les notifications push Braze pour le Web avec le SDK Braze.

Consultez nos [meilleures pratiques en matière de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) pour plus de ressources.

![]({{site.baseurl}}/assets/img_archive/web_push2.png)

Les notifications push web sont mises en œuvre à l'aide de la [norme push du W3C](http://www.w3.org/TR/push-api/), prise en charge par la plupart des grands navigateurs.

Pour plus d'informations sur les normes du protocole push et la prise en charge par les navigateurs, vous pouvez consulter les ressources suivantes : [AppleSafari](https://developer.apple.com/notifications/safari-push-notifications/ "Push Notifications") [MozillaMozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Push API browser compatibility") et [MicrosoftMicrosoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Push API")

{% multi_lang_include archive/web-v4-rename.md %}

## Intégration

### Étape 1 : Configurer le service de traitement de votre site

- Si vous ne disposez pas encore d’un service de traitement, créez un nouveau fichier nommé `service-worker.js` avec l’extrait de code suivant et placez-le dans le répertoire racine de votre site Web.
- Sinon, si votre site enregistre déjà un service de traitement, ajoutez l’extrait de code suivant au fichier du service de traitement et définissez l’option d’initialisation [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) sur `true` lors de l’initialisation du SDK Web.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

Si le nom du fichier de votre service de traitement n’est pas `service-worker.js`, vous devez utiliser [l’option d’initialisation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `serviceWorkerLocation`.

{% alert important %}
Votre serveur Web doit renvoyer un `Content-Type: application/javascript` lorsqu’il notifie votre fichier de service de traitement.
{% endalert %}

#### Que se passe-t-il si je ne peux pas enregistrer un service de traitement dans le répertoire racine ?

Par défaut, un service de traitement ne peut être utilisé que dans le même répertoire que celui dans lequel il est enregistré. Par exemple, si votre fichier de service de traitement existe dans `/assets/service-worker.js`, vous ne pouvez l’enregistrer que dans `example.com/assets/*` ou un sous-répertoire du dossier `assets` mais pas sur votre page d’accueil (`example.com/`). Pour cette raison, il est recommandé d’héberger et d’enregistrer le service de traitement dans le répertoire racine (par exemple, `https://example.com/service-worker.js`).

Si vous ne pouvez pas enregistrer un service de traitement dans votre domaine racine, une autre approche consiste à utiliser l’en-tête HTTP [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) lorsque vous notifiez votre fichier de service de traitement. En configurant votre serveur pour renvoyer `Service-Worker-Allowed: /` en réponse au service de traitement, le navigateur recevra l’instruction d’élargir la portée et d’autoriser l’utilisation dans un répertoire différent.

#### Puis-je créer un service de traitement à l’aide d’un Gestionnaire de balises ?

Non, il faut héberger les services de traitement sur le serveur de votre site Web et il n’est pas possible de les charger à l’aide d’un Gestionnaire de balises.

### Étape 2 : Enregistrer le navigateur

Pour qu’un navigateur reçoive des notifications push, vous devez l’enregistrer pour que vous puissiez réaliser une notification push en appelant `braze.requestPushPermission()`. Cela demandera immédiatement l’autorisation de notification push à l’utilisateur. 

Si vous souhaitez afficher votre propre IU liée à la notification push avant de demander une autorisation (appelée demande de notification push douce), vous pouvez tester pour voir si la notification push est prise en charge dans le navigateur de l’utilisateur avec `braze.isPushSupported()`. Reportez-vous à l'[exemple d'invite par poussée douce]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) utilisant les messages in-app.

Si vous souhaitez désinscrire un utilisateur, vous pouvez le faire en appelant `braze.unregisterPush()`.

{% alert important %}
Les versions récentes de Safari et de Firefox exigent que vous appeliez cette méthode à partir d'un gestionnaire d'événements de courte durée (par exemple, à partir d'un gestionnaire de clic sur un bouton ou d'une invite à la poussée logicielle). Ceci est cohérent avec les [meilleures pratiques de Chrome en matière d’expérience utilisateur](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) pour l’enregistrement de notifications push.
{% endalert %}

### Étape 3 : Configurer les notifications push Safari (facultatif) {#safari}

{% alert important %}
Cette étape n’est plus requise depuis Safari 16 sur macOS 13. N’effectuez cette étape que si vous désirez prendre en charge des versions de Safari macOS plus anciennes.
{% endalert %}

Si vous souhaitez prendre en charge les notifications push pour Safari sur macOS X, suivez les instructions supplémentaires suivantes :

- Générez un certificat push safari en suivant les instructions d'[enregistrement auprès d'Apple](https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33).
- Dans le tableau de bord de Braze, sur la page **Paramètres** (où se trouvent vos clés API), sélectionnez votre application Web. Cliquez sur **Configure Safari Push** et suivez les instructions, en téléchargeant le certificat de push que vous venez de générer.
- Lorsque vous appelez `braze.initialize`, fournissez l’option de configuration facultative `safariWebsitePushId` avec l’ID de notification push du site Internet que vous avez utilisé lors de la génération de votre certificat de notification push Safari. Par exemple, `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Notification push Safari Mobile {#safari-mobile}

Safari 16.4+ sur iOS et iPadOS supporte le web push pour les applications qui ont été [ajoutées à l'écran d'accueil](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) et qui ont un fichier [Web Application Manifest.](https://developer.mozilla.org/en-US/docs/Web/Manifest)  Une fois que vous avez terminé les étapes d’intégration des notifications push Web, vous pouvez également prendre en charge les notifications push mobiles pour Safari. 

Pour prendre en charge le push web Safari mobile, suivez notre [guide ici.]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/)

## Invite de notification push douce

Une invite de notification push douce (également appelée « push primer ») vous aide à optimiser votre taux d’abonnement lorsqu’il s’agit de demander l’autorisation.

Visitez [Soft push prompt]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) pour en savoir plus sur la configuration d'un soft push prompt.

## Exigence HTTPS

Les normes Web exigent que le domaine demandant l’autorisation de notification push soit sécurisé.

### Qu’est-ce qui définit un site sécurisé ?

Un site est considéré comme sécurisé s’il correspond à l’un des modèles d’origine sécurisée suivants :

- (https, , \*)
- (wss, \*, \*)
- (, localhost, )
- (, .localhost, \*)
- (, 127/8, )
- (, ::1/128, \*)
- (file, \*, -)
- (chrome-extension, \*, —)

Cette exigence de sécurité dans la spécification des normes ouvertes sur laquelle la notification push Braze pour le Web est créée empêche les attaques de l'homme du milieu.

### Que se passe-t-il si un site sécurisé n’est pas disponible ?

Bien que les meilleures pratiques du secteur soient de rendre votre site sûr, les clients qui ne peuvent pas sécuriser leur domaine de site peuvent contourner l’exigence en utilisant un modal sécurisé. Pour en savoir plus, consultez notre guide sur l'utilisation de [Alternate push domain]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) ou visualisez une [démonstration.](http://appboyj.com/modal-test.html)

## Paramètres avancés du service de traitement

Notre fichier de service de traitement appellera automatiquement `skipWaiting` lors de l'installation. Si vous souhaitez l’éviter, ajoutez le code suivant à votre fichier de service de traitement, avant l’importation de Braze :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Résolution des problèmes

**J’ai suivi les instructions d’intégration, mais je ne reçois toujours aucune notification push.**
- Les notifications push Web exigent que votre site soit en HTTPS.
- Tous les navigateurs ne peuvent pas recevoir de messages de notification push. Assurez-vous que `braze.isPushSupported()` retourne `true` dans le navigateur.
- Si un utilisateur a refusé au site l’accès aux notifications push, il ne recevra plus de demande d’autorisation à moins qu’il ne supprime l’état refusé de ses préférences de navigateur.

