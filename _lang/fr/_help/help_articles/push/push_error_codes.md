---
nav_title: Messages d’erreur « Push » courants
article_title: Messages d’erreur « Push » courants
page_order: 0

page_type: solution
description: "Cet article d’aide couvre les messages d’erreur des messages push sur iOS et Android, et vous décrit les solutions potentielles."
channel: push
platform:
- iOS
- Android
---

# Messages d’erreur « Push » courants

Consultez ces messages d’erreur courants pour la messagerie push :

{% tabs %}
{% tab Android %} 
### Échec du push : MismatchSenderID
`MismatchSenderId` indique une défaillance de l’authentification.  Google Cloud Messaging (GCM) utilise certaines données importantes pour l’authentification : la clé d’API senderID et FCM.  Vérifiez l’exactitude de ces deux éléments. Pour plus d’informations, voir la [Documentation Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) sur ce problème.

Les raisons peuvent inclure :
- [SenderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) incorrect
- Inscriptions multiples si l’utilisateur s’inscrit sur un autre service push avec un senderID différent

### Échec du push : InvalidRegistration
`InvalidRegistration` peut se produire lorsqu’un jeton push est malformé. Les raisons peuvent inclure quand :
- Les gens transmettent les jetons d’enregistrement Braze manuellement mais n’appellent pas `getToken()`. Par exemple, ils peuvent passer l’instance ID entière. Le jeton du message d’erreur ressemble à `&#124;ID&#124;1&#124;:[regular token]`.  
- Les personnes s’inscrivent à plusieurs services. Nous nous attendons actuellement à des enregistrements push « à l’ancienne », donc si des gens s’inscrivent à plusieurs endroits et que nous détectons des intentions d’autres services, nous pouvons avoir des jetons push malformés.

### Échec du push : NotRegistered
`NotRegistered` signifie généralement que l’application a été supprimée sur l’appareil (c.-à-d. une désinstallation pour Braze). Cela peut également se produire si plusieurs inscriptions se produisent et qu’une deuxième inscription invalide le jeton push que Braze reçoit.

{% endtab %}
{% tab iOS %}

### Échec du push : Erreur d’envoi à un mauvais jeton push

Cette erreur peut survenir pour plusieurs raisons :
- Le jeton push ne nous est pas envoyé correctement dans `[[Appboy sharedInstance] registerPushToken:]`
	- Vérifiez le jeton dans le **Message Activity Log (Journal des activités des messages)**. Généralement, il ressemblera à une longue chaîne de caractères alphanumériques. (p. ex., `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Si ce n’est pas le cas, vérifiez le code concerné par les erreurs d’envoi de jeton push dans Braze.<br><br>
- Environnement de provisionnement mal adapté :
	- Si vous inscrivez avec un certificat de développement et essayez d’envoyer des messages dans un environnement de production, cette erreur peut survenir.  
	- Braze prend uniquement en charge les certificats universels pour les environnements de production. Les tests de push effectués sur des environnements de développement avec un certificat universel ne fonctionneront pas. 
	- Ce rapport envoie les bounces en production, mais pas en développement.<br><br>
- Profil de provisionnement mal adapté :
	- Cela peut se produire si votre certificat ne correspond pas à celui utilisé pour obtenir le jeton. Si vous suspectez que c’est le cas, les étapes de vérification incluent :
		- S’assurer que le certificat push utilisé pour envoyer un push depuis le tableau de bord de Braze et le profil de provisionnement est configuré correctement.
		- Recréer la certification APNS, puis recréer le profil de provisionnement lorsque le certificat APNS est configuré sur `app_id`. Cela peut parfois résoudre des problèmes plus visibles.

### Échec du push : Service de feed-back APNS supprimé

Cela se produit généralement lorsque quelqu’un désinstalle. Braze interroge le service de feed-back APNS chaque nuit pour obtenir une liste de jetons non valides. Pour plus d’informations, consultez la page d’Apple [Communication avec les APN](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).


{% endtab %}
{% endtabs %}

_Dernière mise à jour le 24 janvier 2021_
