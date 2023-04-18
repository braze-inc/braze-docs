---
nav_title: Journal des activités de message
article_title: Journal des activités de message
page_order: 1
page_type: reference
description: "Cet article de référence décrit le journal des activités de message dans la Developer Console, qui affiche les messages associés à vos campagnes et à vos envois. Vous trouverez également ici des informations sur la façon de comprendre les messages du journal."

---

# Journal des activités de message {#dev-console-troubleshooting}

> Le **Journal des activités de message** dans la Developer Console vous permet de voir les messages (en particulier les messages d’erreur) associés à vos campagnes et à vos envois. 

Vous pouvez voir les transactions de campagne API, résoudre les problèmes sur les messages défaillants et recueillir des informations sur la manière d’améliorer la livraison des notifications ou de résoudre les problèmes techniques existants.

![Journal des activités de message][2]

{% alert tip %}
En plus de cet article, nous vous recommandons également de consulter notre cours d’apprentissage Braze [Outils d’assurance qualité et de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), qui explique comment utiliser le Journal des activités de message pour effectuer votre propre débogage et résoudre vous-même les problèmes.
{% endalert %}

Vous pouvez filtrer par le contenu suivant connecté dans le **Journal des activités de message** :

- Erreurs de notification push
- Erreurs de message avorté
- Erreurs de Webhook
- Erreurs de messagerie
- Enregistrements des messages API
- Erreurs de contenu connecté
- Erreurs d’audience connectée de l’API REST
- Erreurs d’aliasing de l’utilisateur
- Erreurs de test A/B
- Erreurs de SMS/MMS

Ces messages peuvent provenir de notre propre système, de vos applications ou plateformes, ou de nos partenaires tiers. Cela peut entraîner un nombre infini de messages pouvant apparaître dans ce journal.

## Comprendre les messages du journal

Pour déterminer ce que vos messages signifient, prêtez attention au libellé de chaque message et aux colonnes qui lui correspondent, car cela peut vous aider à résoudre les problèmes en utilisant des indices contextuels. 

Par exemple, si une entrée de journal indique « empty-cart_app » (panier-vide application) et vous n’êtes pas sûr de ce que cela signifie, regardez à gauche dans la colonne **Type**. Si vous voyez « Aborted Message Error » (Erreur de message avorté), vous pouvez supposer que le message était ce qui a été écrit comme [abort message (message avorté)][1] en utilisant Liquid, et que le message a été abandonné parce que le destinataire prévu du message disposait d’un panier vide dans votre application.

### Messages courants

Plusieurs types de messages courants existent, et certains peuvent même fournir des liens de résolution des problèmes pour vous aider à diagnostiquer et résoudre les problèmes. Reportez-vous au tableau suivant pour plus de détails.

{% alert note %}
Les messages suivants servent d’exemple et peuvent ne pas correspondre exactement à ce qui est affiché dans la colonne **Message** du journal.
{% endalert %}

| Type de message | Exemple de message | Description |
|---|---|---|
| Soft bounce | L’adresse e-mail same@example.com a subi un soft bounce. | L’adresse e-mail était valide et le message e-mail a été acheminé jusqu’au serveur de messagerie du destinataire, mais a été rejeté pour un problème « temporaire ». <br><br>Les raisons les plus courantes de ce type de rebond sont les suivantes : {::nomarkdown} <ul> <li> La boîte de réception était pleine (l’utilisateur a dépassé son quota) </li> <li> Le serveur était hors service </li> <li> Le message était trop volumineux pour la boîte de réception du destinataire </li>  </ul> {:/} Si un e-mail reçoit un soft bounce, nous réessaierons généralement après une période de 72 heures, mais le nombre de tentatives varie d’un destinataire à l’autre. |
| Hard bounce | Le compte d’e-mail que vous avez essayé de contacter n’existe pas. Essayez de vérifier que l’adresse e-mail du destinataire ne contient pas de fautes de frappe ou d’espaces inutiles. En savoir plus sur _ÉCHANTILLON D’URL_.| Votre message n’a jamais atteint la boîte de réception de cette personne, car il n’y avait pas de boîte de réception à joindre ! Si vous souhaitez approfondir l’information, des messages comme celui-ci peuvent parfois comporter des liens dans la colonne **View Details (Afficher les détails)** qui vous permettra d’afficher le profil du destinataire prévu.|
| Bloc | Le message spam est rejeté en raison de la politique anti-spam. Pour plus d’informations, consultez _ÉCHANTILLON D’URL_.| Oh oh. On dirait que votre message a été classé dans la catégorie des spams. ll se peut qu’il soit destiné à ce destinataire, mais si vous voyez souvent ce message, vous devriez peut-être revoir vos habitudes d’envoi ou le contenu de votre message. Réfléchissez également : avez-vous [réchauffé votre adresse IP à jour][8] ? Si ce n’est pas le cas, contactez Braze pour des conseils sur la façon de procéder.|
| Erreurs de message annulé | empty-cart_web | Si vous avez une application avec un panier ou que vous créez un envoi avec un message annulé dans le Liquid, vous pouvez personnaliser le message qui vous est renvoyé si l’envoi est annulé. Dans ce cas, le message renvoyé est empty-cart_web (panier-vide Web).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages
[2]: {% image_buster /assets/img_archive/message_activity_log.png %}
[8]: {{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/
