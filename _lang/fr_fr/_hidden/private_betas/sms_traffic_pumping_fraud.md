---
nav_title: FAQ sur la fraude par pompage de trafic par SMS
permalink: "/sms_traffic_pumping_fraud/"
description: "Cet article de référence couvre les questions fréquemment posées sur la fraude au pompage du trafic par SMS."
hidden: true
---

# FAQ sur la fraude par pompage du trafic par SMS 

### Qu'est-ce que la fraude par pompage du trafic SMS ? 

Le pompage du trafic de SMS est une menace croissante dans le domaine des SMS. Cela se produit lorsque des fraudeurs trouvent un moyen de déclencher l'envoi de messages SMS à des numéros de téléphone qui ne sont pas associés à des clients réels afin de percevoir des chiffres d'affaires liés à l'envoi de messages frauduleux. Le plus souvent, ils déclenchent des envois de SMS en grand nombre à l'aide de formulaires en ligne, tels que des formulaires d'abonnement par SMS ou des mots de passe à usage unique pour la réinitialisation du mot de passe ou l'identification du compte.  

Par exemple, si une marque dispose sur son site web d'un formulaire d'inscription aux SMS permettant aux clients de s'abonner à la réception de messages textuels, un fraudeur saisira des numéros de téléphone frauduleux dans le formulaire pour déclencher des messages déclenchés. Le fraudeur utilise des numéros de téléphone surtaxés pour ces messages et réclame un chiffre affaires à l'opérateur de téléphonie mobile local, qui est responsable de la réception/distribution des messages aux utilisateurs finaux. Ce système génère des frais frauduleux pour la marque. 

### Que fait Braze pour limiter la fraude au pompage par SMS ?

Braze tient actuellement à jour une liste de blocage des SMS pour les pays soumis à l'embargo américain, ainsi que pour les pays connus pour présenter un risque élevé de pompage du trafic, liste à laquelle vous pouvez vous référer dans [notre documentation.]({{site.baseurl}}/sms_country_blocklist) Toutes les tentatives d'envoi vers des numéros de téléphone comportant ces codes pays sont bloquées.

En outre, Braze introduit une liste d'autorisations géographiques pour les SMS, qui vous protégera davantage contre les comportements frauduleux en imposant des contrôles sur les pays vers lesquels vous pouvez envoyer des messages.

### Comment puis-je protéger ma marque contre la fraude par pompage de SMS ? 

Il existe plusieurs moyens de se protéger, notamment : 
- **Surveillez vos volumes quotidiens d'envoi de SMS pour détecter les pics et les anomalies :**
    - Nous vous recommandons de définir des [limites de campagne et des alertes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) pour plafonner et notifier l'envoi d'un nombre anormalement élevé de messages.
    - Des pics inhabituels dans l'envoi de messages peuvent indiquer un pompage du trafic.
    - Un nombre inhabituellement élevé d'abonnements dans un court laps de temps (en dehors de stratégies intentionnelles visant à générer des abonnements) peut indiquer un pompage du trafic.
- **Améliorez la sécurité des formulaires de saisie de numéros de téléphone en ligne :**
    - Les [modèles de formulaires d'inscription par SMS de]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) Braze offrent des mesures de sécurité prêtes à l'emploi, telles que la validation de la longueur et du format du numéro de téléphone. Vous pouvez également paramétrer le formulaire de manière à ce qu'il ne recueille que les numéros de téléphone dont le code pays correspond à votre clientèle cible :
        - Par exemple, si vous ne faites des affaires qu'aux États-Unis et au Royaume-Uni, configurez le formulaire de manière à ce qu'il ne recueille que les numéros comportant un code de pays +1 et +44 (vous trouverez des détails techniques dans [notre documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/#step-2-customize-your-phone-number-input-component)).
    - Si vous créez une capture personnalisée de numéros de téléphone sur votre site web, nous vous recommandons de définir des règles pour valider la longueur et le format des numéros de téléphone et de vous assurer que les formulaires sont entièrement remplis avant de collecter les numéros de téléphone. Veillez à collaborer avec votre équipe technique ou d'ingénieurs pour valider les entrées du formulaire côté client et côté serveur afin d'assurer une protection maximale.
        - En outre, envisagez d'utiliser des outils tels que les CAPTCHA pour vous assurer que le formulaire est soumis par un être humain et non par un processus automatisé. La mise en place d'un CAPTCHA sur les formulaires d'inscription par SMS peut contribuer à réduire le nombre d'inscriptions frauduleuses.

### Ma marque fait des affaires aux États-Unis et les États-Unis figurent sur ma liste d'autorisations géographiques par SMS. Mes clients continueront-ils à recevoir mes messages SMS lorsqu'ils voyagent en dehors des États-Unis ? 

Oui, tant que vos clients ont un numéro de téléphone avec un code régional américain, ils recevront toujours vos messages lorsqu'ils voyagent. 

{% alert important %}
Si vous avez des questions supplémentaires sur le pompage du trafic SMS et sur la façon dont ces changements de produits peuvent affecter vos envois de SMS, veuillez contacter votre gestionnaire de satisfaction client.
{% endalert %}
