---
nav_title: Messages d’erreur « Push » courants
article_title: Messages d’erreur « Push » courants
page_order: 22
page_type: reference
description: "Cet article couvre les messages d'erreur courants liés au push pour iOS et Android, et vous guide à travers les solutions potentielles."
channel: push
platform:
- iOS
- Android
---

# Messages d’erreur « Push » courants

> Cette page présente les messages d'erreur les plus courants pour l'envoi de messages.

{% tabs %}
{% tab Android %} 
### Échec du push : MismatchSenderID
`MismatchSenderId` indique une défaillance de l’authentification. Firebase Cloud Messaging (FCM) s'authentifie à l'aide de quelques données clés : l'identifiant de l'expéditeur et la clé API FCM.  Vérifiez l’exactitude de ces deux éléments. Pour plus d'informations, consultez la [documentation Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) à ce sujet.

Les raisons peuvent inclure :
- Mauvais [identifiant de l'expéditeur]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Inscriptions multiples si l’utilisateur s’inscrit sur un autre service push avec un senderID différent

### Échec du push : InvalidRegistration
`InvalidRegistration` peut se produire lorsqu’un jeton push est malformé. Les raisons peuvent inclure quand :
- Les gens transmettent les jetons d’enregistrement Braze manuellement mais n’appellent pas `getToken()`. Par exemple, ils peuvent passer l’instance ID entière. Le jeton du message d’erreur ressemble à `&#124;ID&#124;1&#124;:[regular token]`.  
- Les personnes s’inscrivent à plusieurs services. Nous nous attendons actuellement à des enregistrements push « à l’ancienne », donc si des gens s’inscrivent à plusieurs endroits et que nous détectons des intentions d’autres services, nous pouvons avoir des jetons push malformés.

### Échec du push : NotRegistered
`NotRegistered` signifie généralement que l'application a été supprimée de l'appareil (comme notre signal de désinstallation). Cela peut également se produire si plusieurs inscriptions se produisent et qu’une deuxième inscription invalide le jeton push que Braze reçoit.

{% endtab %}
{% tab iOS %}

### Une erreur s'est produite lors de l'envoi de la notification push en raison d'une charge utile non valide.

Ce message peut apparaître dans l'onglet **Engagement** du profil utilisateur, sous **Paramètres de contact** > **Journal des modifications push,** lorsque le service Apple Notification push (APN) rejette la demande push en raison d'une charge utile non valide.

Dans Braze, ce message du tableau de bord peut correspondre à l'une des raisons d'erreur APN suivantes :

- `PayloadEmpty` : La charge utile ne contenait pas le contenu requis pour le type de notification envoyée.
- `PayloadTooLarge` : La charge utile a dépassé la taille maximale autorisée par APN.

Les causes courantes comprennent :

- Les clés personnalisées (et leurs valeurs) peuvent rendre la charge utile trop volumineuse (cela peut inclure des valeurs rendues par Liquid qui sont plus importantes que prévu).
- Une alerte ou un corps vide ou manquant lorsque cela est requis (ou une charge utile mal `aps`formée).

Prochaines étapes :

- Réduisez la taille de la charge utile en supprimant les clés personnalisées et en raccourcissant les valeurs dynamiques volumineuses.
- Si vous effectuez l'envoi via l'API, veuillez vérifier la charge utile JSON finale (y compris la taille) avant l'envoi.

### Échec du push : BadToken

L'erreur `BadToken` peut se produire pour plusieurs raisons :
- Le jeton push ne nous est pas envoyé correctement dans `[[Appboy sharedInstance] registerPushToken:]`
	- Vérifiez le jeton dans le [journal d'activité des messages.]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) Il doit généralement ressembler à une longue chaîne de caractères et de chiffres (comme `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Si ce n'est pas le cas, vérifiez le code impliqué dans l'envoi des erreurs de jetons de poussée de Braze.<br><br>
- Environnement de provisionnement mal adapté :
	- Si vous inscrivez avec un certificat de développement et essayez d’envoyer des messages dans un environnement de production, cette erreur peut survenir.  
	- Braze prend uniquement en charge les certificats universels pour les environnements de production. Les tests de push effectués sur des environnements de développement avec un certificat universel ne fonctionneront pas. 
	- Ce rapport envoie les bounces en production, mais pas en développement.<br><br>
- Profil de provisionnement mal adapté :
	- Cela peut se produire si votre certificat ne correspond pas à celui utilisé pour obtenir le jeton. Si vous suspectez que c’est le cas, les étapes de vérification incluent :
		- S’assurer que le certificat push utilisé pour envoyer un push depuis le tableau de bord de Braze et le profil de provisionnement est configuré correctement.
		- Recréer la certification APN puis recréer le profil de provisionnement après la configuration du certificat APN sur le site `app_id`. Cela peut parfois résoudre des problèmes plus visibles.

### Échec du push : Service de feed-back APNS supprimé

Cela se produit généralement lorsque quelqu’un désinstalle. Braze interroge le service de feed-back APNS chaque nuit pour obtenir une liste de jetons non valides. Pour plus d'informations, reportez-vous au document d'Apple intitulé [Communiquer avec les APN](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}
