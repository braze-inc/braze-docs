---
nav_title: "Journal d'activité des messages"
article_title: "Journal d'activité des messages"
page_order: 5
page_type: reference
description: "Cet article de référence décrit le journal d'activité des messages qui vous montre les messages associés à vos campagnes et à vos envois. Vous y trouverez également des informations sur la manière de comprendre les messages du journal."

---

# Journal d'activité des messages {#dev-console-troubleshooting}

> Le **journal d'activité des messages** vous permet de consulter tous les messages (en particulier les messages d'erreur) associés à vos campagnes et à vos envois.

Vous pouvez voir les transactions de la campagne API, dépanner les détails des messages qui ont échoué et recueillir des informations sur la manière d'améliorer la réception/distribution des communications ou de résoudre les problèmes techniques existants.

Pour accéder au journal, allez dans **Paramètres** > **Journal d'activité des messages.**

!Journal d'activité des messages]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Outre cet article, nous vous recommandons également de consulter notre cours d'apprentissage sur l ['assurance qualité et les outils de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze, qui explique comment utiliser le journal d'activité des messages pour effectuer vos propres opérations de résolution des problèmes et de débogage.
{% endalert %}

Vous pouvez filtrer en fonction des contenus suivants enregistrés dans le **journal d'activité des messages :**

- Erreurs de notification push
- Erreurs dans les messages interrompus
- Erreurs de webhook
- Erreurs de courrier
- Enregistrements de messages API
- Erreurs de contenu connecté
- Erreurs d'audience de l'API REST connectée
- Erreurs d'aliasing de l'utilisateur
- Erreurs de test A/B
- Erreurs SMS/MMS
- Erreurs dans WhatsApp
- Erreurs de production en ligne/instantané
- Mauvais déclencheurs d'utilisateurs

Ces messages peuvent provenir de notre propre système, de vos apps ou plateformes, ou de nos partenaires tiers. Il peut en résulter un nombre infini d'envois de messages dans ce journal.

## Comprendre les messages du journal

Pour déterminer la signification de vos messages, prêtez attention au libellé de chaque message et aux colonnes qui lui correspondent, car cela peut vous aider à résoudre les problèmes à l'aide d'indices contextuels. 

Par exemple, si vous avez une entrée de journal dont le message indique "empty-cart_app" et que vous n'êtes pas sûr de ce que cela signifie, regardez à gauche dans la colonne **Type.**  Si vous voyez "Aborted Message Error", vous pouvez supposer que le message était ce qui a été écrit comme [message d'abandon]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) à l'aide de Liquid, et que le message a été abandonné parce que le destinataire du message avait un panier vide dans votre application.

### Messages communs

Il existe quelques types de messages courants que vous pouvez voir, et certains peuvent même fournir des liens de résolution des problèmes pour vous aider à diagnostiquer et à résoudre les problèmes.

Les messages suivants sont donnés à titre d'exemple et peuvent ne pas correspondre exactement à ce qui est affiché dans la colonne **Message** de votre journal.

| Type de message | Message potentiel | Description |
|---|---|---|
| Échappée provisoire d'envoi | L'adresse e-mail same@example.com a fait l'objet d'un échec provisoire d'envoi. | L'adresse e-mail était valide et l'envoi du message a atteint le serveur de messagerie du destinataire, mais a été rejeté pour un problème "temporaire". <br><br>Les raisons les plus courantes de l'échec provisoire d'envoi sont les suivantes : {::nomarkdown} <ul> <li> La boîte aux lettres était pleine (l'utilisateur a dépassé son quota). </li> <li> Le serveur était en panne </li> <li> Le message était trop volumineux pour la boîte de réception du destinataire. </li>  </ul> {:/} Si un e-mail a fait l'objet d'un échec provisoire d'envoi, nous effectuons généralement une nouvelle tentative dans un délai de 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre. |
| échec d'envoi définitif | Le compte e-mail que vous avez essayé de joindre n'existe pas. Vérifiez que l'adresse e-mail du destinataire ne comporte pas de fautes de frappe ou d'espaces inutiles. | Votre message n'a jamais atteint la boîte de réception de cette personne parce qu'il n'y avait pas de boîte de réception à atteindre. Si vous souhaitez aller plus loin, les messages de ce type peuvent parfois contenir des liens dans la colonne **Voir les détails** qui vous permettront de consulter le profil du destinataire.|
| Bloc | Le message est rejeté en raison de la politique anti-spam. | Votre message a été classé comme spam. Cette erreur de courrier est enregistrée pour un utilisateur si nous avons reçu un événement de l'ESP indiquant que l'e-mail a été abandonné. Il se peut qu'il soit destiné à ce destinataire, mais si vous voyez souvent ce message, vous devriez peut-être réévaluer vos habitudes d'envoi ou le contenu de votre message. Pensez aussi au passé : avez-vous [réchauffé votre IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Si ce n'est pas le cas, contactez Braze pour obtenir des conseils sur la mise en œuvre de ce projet.|
| Message d'abandon Erreur | empty-cart_web | Si vous avez une application avec un panier ou si vous créez un envoi avec un message in-app dans le Liquid, vous pouvez personnaliser le message qui vous est renvoyé si l'envoi est interrompu. Dans ce cas, l'envoi de messages est le suivant empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Pourquoi mon message ne figure-t-il pas dans cette liste ?

Les messages contenus dans le journal d'activité des messages peuvent provenir de différentes sources : Braze, vos apps ou plateformes, ou nos partenaires tiers. Cela signifie qu'il existe un nombre infini de messages susceptibles d'apparaître dans ce journal - comme vous pouvez l'imaginer, nous ne pouvons pas tous les énumérer !

Par exemple, certains messages de "blocage" potentiels, en plus de ceux énumérés dans le tableau précédent, pourraient être les suivants :

- Malheureusement, les messages de [_IP_ADDRESS_] n'ont pas été envoyés. Veuillez contacter votre fournisseur de services Internet car une partie de son réseau figure sur notre liste de blocage.
- Message rejeté en raison de la politique locale.
- Le message a été bloqué par le destinataire comme étant du spam.
- Service indisponible, l'hôte du client [_IP_ADDRESS_] est bloqué par Spamhaus.

## Durée de conservation des données

Les erreurs des 60 dernières heures sont disponibles dans les journaux d'activité des messages. Les journaux datant de plus de 60 heures sont nettoyés et ne sont plus accessibles.

### Nombre de journaux d'erreurs stockés

Le nombre de journaux enregistrés est influencé par plusieurs conditions. Par exemple, si une campagne planifiée est envoyée à des milliers d'utilisateurs, nous verrons potentiellement un échantillon des erreurs dans le journal d'activité des messages au lieu de toutes les erreurs. Vous trouverez ci-dessous un aperçu des conditions affectant le nombre de journaux enregistrés :
- Jusqu'à 20 journaux d'erreurs du même type seront enregistrés pour la même campagne ou étape du canvas dans une heure d'horloge fixe pour les types d'erreurs suivants :
    - Erreurs de contenu connecté
    - Abandon Erreurs dans les messages
    - Erreurs de webhook
    - Erreurs de rejet des SMS
    - Erreurs de réception/distribution de SMS
    - Erreurs de WhatsApp Failure
    - Erreurs de test A/B
- Jusqu'à 20 journaux d'erreurs de notification push du même type d'erreur seront enregistrés pour la même campagne ou la même combinaison d'étape du canvas et d'app pour les types d'erreurs suivants :
    - Carte d'identité Push invalide
    - Jeton de poussée invalide
    - Pas de justificatif de poussée
    - Erreurs de jeton
    - Quota dépassé
    - Tentatives interrompues
    - Charge utile non valide
    - Erreur inattendue
- Jusqu'à 100 journaux d'erreurs du même type d'erreur seront enregistrés pour la même application dans un délai d'une heure d'horloge fixe pour les types d'erreurs suivants :
    - Erreur de ligne/en production/instantanée (No push credential)
    - Erreur de ligne/en production/instantanée (Invalid push credential)
    - Autres erreurs en ligne/en production/instantanée
    - Feedback APN Erreurs de jeton supprimé
- Jusqu'à 100 journaux d'erreurs du même type seront enregistrés pour la même campagne ou étape du canvas au cours d'une heure d'horloge fixe pour les types d'erreurs suivants :
    - Échecs provisoires d'envois d'e-mails
    - Erreurs d'échec d'envoi définitif d'e-mail
    - Erreurs de blocage d'e-mail
- Jusqu'à 100 journaux d'erreurs d'aliasing de l'utilisateur seront enregistrés pour le même espace de travail au cours d'une heure d'horloge fixe.

