---
nav_title: Messages d'erreur push courants
article_title: Messages d'erreur push courants
page_order: 22
page_type: reference
description: "Cet article couvre les messages d'erreur courants liés au push pour iOS et Android, et vous guide à travers les solutions potentielles."
channel: push
platform:
- iOS
- Android
---

# Messages d'erreur push courants

> Cette page présente les messages d'erreur les plus courants pour l'envoi de notifications push.

{% tabs %}
{% tab Android %} 
### Rebond push : MismatchSenderId
`MismatchSenderId` indique un échec d'authentification. Firebase Cloud Messaging (FCM) s'authentifie à l'aide de quelques données clés : l'identifiant de l'expéditeur (senderID) et la clé API FCM. Vérifiez l'exactitude de ces deux éléments. Pour plus d'informations, consultez la [documentation Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) à ce sujet.

Les causes courantes incluent :
- Mauvais [identifiant de l'expéditeur]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Inscriptions multiples si l'utilisateur s'inscrit sur un autre service push avec un senderID différent

### Rebond push : InvalidRegistration
`InvalidRegistration` peut se produire lorsqu'un jeton de notification push est malformé. Les causes courantes incluent :
- Les utilisateurs transmettent les jetons d'enregistrement Braze manuellement mais n'appellent pas `getToken()`. Par exemple, ils peuvent transmettre l'instance ID entière. Le jeton du message d'erreur ressemble à `&#124;ID&#124;1&#124;:[regular token]`.  
- Les utilisateurs s'inscrivent à plusieurs services. Nous nous attendons actuellement à des enregistrements push « à l'ancienne », donc si des utilisateurs s'inscrivent à plusieurs endroits et que nous interceptons des intentions d'autres services, nous pouvons obtenir des jetons de notification push malformés.

### Rebond push : NotRegistered {#notregistered}
`NotRegistered` signifie généralement que l'application a été supprimée de l'appareil (c'est notre signal de désinstallation). Cela peut également se produire en cas d'inscriptions multiples, lorsqu'une deuxième inscription invalide le jeton de notification push reçu par Braze.

### DEVICE_UNREGISTERED {#device-unregistered}

Cette erreur apparaît dans le journal d'activité des messages sous la forme :

`Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

Cela se produit généralement pour l'une des raisons suivantes :

- L'utilisateur a désinstallé l'application. C'est la cause la plus fréquente. Lorsque l'application est supprimée d'un appareil, le jeton de notification push devient invalide.
- Les identifiants push ont été mis à jour dans l'application. Si votre équipe a modifié les identifiants FCM ou les certificats intégrés à l'application, les utilisateurs enregistrés avec les anciens identifiants disposent de jetons invalides jusqu'à ce que l'application les réenregistre.
- Une logique personnalisée désinscrit les utilisateurs du push. C'est rare, mais il est techniquement possible de désinscrire un appareil du push de manière programmatique via le SDK Firebase/Android.

{% alert note %}
Cette erreur ne signifie pas que l'utilisateur a désactivé le push, mais seulement qu'un jeton spécifique a été supprimé de son profil. C'est courant pour les utilisateurs qui testent des fonctionnalités et installent/désinstallent fréquemment l'application. Pour vérifier si l'utilisateur dispose encore de jetons valides, accédez à **Recherche d'utilisateurs** et consultez la section **Paramètres de contact** dans l'onglet **Engagement**.
{% endalert %}

{% endtab %}
{% tab iOS %}

### Erreur lors de l'envoi push en raison d'un payload non valide

Ce message peut apparaître dans l'onglet **Engagement** du profil utilisateur, sous **Paramètres de contact** > **Journal des modifications push**, lorsque le service Apple Push Notification (APN) rejette la demande push en raison d'un payload non valide.

Dans Braze, ce message du tableau de bord peut correspondre à l'une des raisons d'erreur APN suivantes :

- `PayloadEmpty` : Le payload ne contenait pas le contenu requis pour le type de notification envoyée.
- `PayloadTooLarge` : Le payload a dépassé la taille maximale autorisée par APN.

Les causes courantes incluent :

- Des clés personnalisées (et leurs valeurs) qui rendent le payload trop volumineux (cela peut inclure des valeurs rendues par Liquid plus importantes que prévu).
- Une alerte ou un corps vide ou manquant lorsque cela est requis (ou un payload `aps` mal formé).

Prochaines étapes :

- Réduisez la taille du payload en supprimant les clés personnalisées et en raccourcissant les valeurs dynamiques volumineuses.
- Si vous effectuez l'envoi via l'API, validez le payload JSON final (y compris la taille) avant l'envoi.

### Rebond push : BadToken

L'erreur `BadToken` peut se produire pour plusieurs raisons :
- Le jeton de notification push n'est pas envoyé correctement à Braze (par exemple, dans `registerDeviceToken:` ou l'équivalent de votre plateforme).
	- Vérifiez le jeton dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Il doit généralement ressembler à une longue chaîne de lettres et de chiffres (comme `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Si ce n'est pas le cas, vérifiez le code impliqué dans l'envoi du jeton de notification push à Braze.<br><br>
- Environnement de provisionnement inadapté :
	- Si vous vous inscrivez avec un certificat de développement et essayez d'envoyer des messages dans un environnement de production, cette erreur peut survenir.  
	- Braze prend uniquement en charge les certificats universels pour les environnements de production. Les tests de push effectués sur des environnements de développement avec un certificat universel ne fonctionneront pas. 
	- Ce rapport envoie les rebonds en production, mais pas en développement.<br><br>
- Profil de provisionnement inadapté :
	- Cela peut se produire si votre certificat ne correspond pas à celui utilisé pour obtenir le jeton. Si vous suspectez que c'est le cas, les étapes suivantes incluent :
		- S'assurer que le certificat push utilisé pour envoyer des notifications depuis le tableau de bord de Braze et le profil de provisionnement sont configurés correctement.
		- Recréer la certification APN puis recréer le profil de provisionnement après la configuration du certificat APN sur le `app_id`. Cela peut parfois résoudre des problèmes plus visibles.

### L'ID de bundle n'est pas autorisé

L'erreur `TopicDisallowed` signifie qu'APN a rejeté la notification push car le sujet (ID de bundle) dans la requête n'est pas autorisé pour les identifiants d'authentification utilisés. Pour résoudre ce problème :

1. **Vérifiez l'ID de bundle.** Confirmez que l'ID de bundle configuré dans les paramètres de votre application Braze correspond exactement à l'ID de bundle de votre application. Cela inclut les variations de suffixe (par exemple, `.debug`, `.staging`).
2. **Vérifiez votre configuration d'authentification APN.** Confirmez que votre application est configurée avec la bonne clé APN `.p8` et que la clé est associée à la même équipe Apple Developer que l'application à laquelle vous envoyez des notifications.
3. **Confirmez l'environnement de l'application.** Si vous avez des ID d'application distincts dans Braze pour les builds de développement et de production, vérifiez que chacun est configuré avec les bons identifiants push et le bon environnement.

### Unregistered {#ios-unregistered}

Cette erreur apparaît dans le journal d'activité des messages sous la forme :

`Received 'Unregistered' sending to '[Token String]'`

Il s'agit de l'équivalent iOS de l'erreur Android [DEVICE_UNREGISTERED](#device-unregistered). Elle se produit généralement pour l'une des raisons suivantes :

- L'utilisateur a désinstallé l'application. C'est la cause la plus fréquente.
- Les certificats push ont été mis à jour. Si votre équipe a modifié ou renouvelé les certificats APN, les utilisateurs enregistrés avec les anciens certificats peuvent disposer de jetons invalides jusqu'à ce que l'application les réenregistre.
- Une logique personnalisée désinscrit les utilisateurs du push. C'est rare, mais il est techniquement possible de se désinscrire des notifications à distance de manière programmatique via le SDK iOS.

{% alert note %}
Cette erreur ne signifie pas que l'utilisateur a désactivé le push, mais seulement qu'un jeton spécifique a été supprimé de son profil. Pour vérifier si l'utilisateur dispose encore de jetons valides, accédez à **Recherche d'utilisateurs** et consultez la section **Paramètres de contact** dans l'onglet **Engagement**.
{% endalert %}

### InvalidProviderToken

L'erreur `InvalidProviderToken` signifie qu'APN a rejeté la requête car le jeton d'authentification (provenant d'une clé `.p8`) ou le certificat push (`.p12`) ne correspond pas à l'ID de bundle ou au Team ID de l'application. Pour résoudre ce problème :

1. **Vérifiez votre Team ID et Key ID :** Si vous utilisez une clé d'authentification `.p8`, confirmez que le **Team ID** et le **Key ID** configurés dans le tableau de bord de Braze (**Paramètres** > **Paramètres de l'application** > sélectionnez votre application iOS) correspondent aux valeurs de votre compte Apple Developer.
2. **Vérifiez l'ID de bundle :** Assurez-vous que l'ID de bundle enregistré dans Braze correspond à l'ID de bundle de votre application. Une différence, comme une casse différente ou un suffixe `.debug`, provoque cette erreur.
3. **Rechargez la clé ou le certificat :** Si la clé `.p8` ou le certificat `.p12` a été récemment régénéré ou révoqué, chargez la nouvelle clé dans Braze et supprimez l'ancienne.
4. **Confirmez l'environnement APN :** Si vous utilisez un certificat `.p12`, vérifiez que vous avez sélectionné le bon environnement (développement ou production) lors du chargement. Pour les clés `.p8`, cela est géré automatiquement.

### Rebond push : suppression par le service de feedback APN

Cela se produit généralement lorsque quelqu'un désinstalle l'application. Braze interroge le service de feedback APN chaque nuit pour obtenir une liste de jetons invalides. Pour plus d'informations, consultez le document d'Apple [Communicating with APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}