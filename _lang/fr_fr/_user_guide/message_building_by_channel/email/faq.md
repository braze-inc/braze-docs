---
nav_title: FAQ
article_title: FAQ sur les e-mails
page_order: 14
description: "Cette page fournit des réponses aux questions fréquemment posées sur les communications par e-mail."
channel: email

---

# Foire aux questions

> Cet article fournit des réponses à des questions fréquemment posées sur les e-mails.

### Que se passe-t-il lorsqu’un e-mail est envoyé et que plusieurs profils ont la même adresse e-mail ?

Si plusieurs utilisateurs avec des e-mails correspondants se trouvent tous dans un segment pour recevoir une campagne, un profil utilisateur aléatoire avec cette adresse e-mail est choisi au moment de l'envoi. De cette façon, l'e-mail n'est envoyé qu'une seule fois et est dédupliqué, garantissant ainsi qu’il ne touche pas la même adresse e-mail plusieurs fois.

Notez que cette déduplication se produit si les utilisateurs ciblés sont inclus dans le même envoi. Les campagnes déclenchées peuvent entraîner plusieurs envois à la même adresse e-mail (même pendant une période où les utilisateurs pourraient être exclus en raison de leur rééligibilité) si des utilisateurs différents avec des adresses e-mail correspondantes enregistrent l'événement déclencheur à des moments différents. Les utilisateurs ne sont pas dédupliqués par e-mail sur l’entrée Canvas, il est donc possible que les utilisateurs ne soient pas dédupliqués au-delà de la première étape d’un Canvas s’ils progressent à des moments légèrement différents en raison de l’entrée limitée. Lorsqu'un utilisateur lié à une adresse e-mail donnée ouvre ou clique sur un e-mail, tous les profils d'utilisateurs partageant cette adresse e-mail sont marqués comme ayant ouvert et cliqué sur la campagne.

#### Exception : Campagnes déclenchées par API

Les campagnes déclenchées par l'API dédupliqueront ou enverront des messages dédupliqués en fonction de l'endroit où l’audience est définie. En résumé, les e-mails dupliqués doivent être directement ciblés comme des `user_ids` séparés dans l'appel API afin de recevoir plusieurs détails. Voici trois scénarios possibles pour les campagnes déclenchées par une API :

- **Scénario 1 : E-mails dupliqués dans le segment cible :** Si le même e-mail apparaît dans plusieurs profils d'utilisateurs regroupés dans les filtres d'audience du tableau de bord pour une campagne déclenchée par l'API, un seul des profils recevra l'e-mail.
- **Scénario 2 : E-mails dupliqués dans différents `user_ids` dans l’objet Destinataires :** Si le même e-mail apparaît dans plusieurs `External_user_IDs` référencés par l'objet `recipients`, l'e-mail sera envoyé deux fois.
- **Scénario 3 : E-mails dupliqués en raison d'identifiants utilisateur en double dans l'objet Destinataires :** Si vous essayez d’ajouter le même profil utilisateur deux fois, seul un des profils recevra l’e-mail.

### Comment vérifier si une adresse e-mail est déjà associée à un utilisateur ?

Avant de créer un utilisateur via l'API ou le SDK, appelez le point de terminaison [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) et spécifiez l'adresse `email_address` de l'utilisateur. S'il renvoie un profil utilisateur, cela signifie que l'utilisateur de Braze est déjà associé à cette adresse e-mail.

Nous vous recommandons vivement de rechercher des adresses e-mail uniques lors de la création de nouveaux utilisateurs et d'éviter de transmettre ou d'importer des utilisateurs ayant la même adresse e-mail. Dans le cas contraire, vous risquez d'avoir des conséquences imprévues sur l'envoi de messages, le ciblage, la création de rapports et d'autres fonctionnalités.

Par exemple, supposons que vous ayez des profils en double, mais que certains événements et attributs personnalisés ne se trouvent que sur un seul profil. Lorsque vous essayez de déclencher des campagnes ou des Canvases avec plusieurs critères, Braze ne peut pas identifier l'utilisateur comme éligible parce qu'il y a deux profils utilisateur. Par ailleurs, si une campagne cible une adresse e-mail partagée par deux utilisateurs, la page **Recherche d'utilisateurs** indiquera que les deux profils utilisateurs ont reçu la campagne.

### Les mises à jour de mes paramètres de messagerie sortante s'appliqueront-elles rétroactivement ?

Non. Les mises à jour des paramètres de messagerie sortante n'affectent pas rétroactivement les envois existants. Par exemple, changer votre nom d'affichage par défaut dans les paramètres de messagerie ne remplacera pas automatiquement le nom d'affichage par défaut existant dans vos campagnes actives ou vos Canvases. 

### À quoi correspond un « bon» taux de distribution des e-mails ?

En général, le « nombre magique » est d'environ 98 % des messages livrés avec un taux de rebond ne dépassant pas 3 %. Si votre livraison tombe en dessous de ce niveau, il y a généralement lieu de s'inquiéter.

Cependant, un taux peut être supérieur à 98 % et présenter encore certains problèmes de livrabilité. Par exemple, si toutes vos rebonds proviennent d’un domaine particulier, c’est un signal clair qu’il existe un problème de réputation avec ce fournisseur.

De plus, les messages peuvent être livrés et terminer dans les courriers indésirables, ce qui indique des problèmes de réputation potentiellement graves. Il est important de surveiller non seulement le nombre de messages livrés, mais aussi les taux d’ouverture et de clics pour déterminer si les utilisateurs voient effectivement les messages dans leurs boîtes de réception. Comme les fournisseurs ne signalent généralement pas toutes les instances de spam, un taux de spam de même 1 % pourrait être source de préoccupation et d’analyse approfondie.

Enfin, votre entreprise et les types d'e-mails que vous envoyez peuvent également affecter la livraison. Par exemple, une personne envoyant principalement des [emails transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) devrait s'attendre à voir un meilleur taux qu'une personne envoyant de nombreux messages marketing.

### Pourquoi est-ce que mes indicateurs de livrabilité d’e-mails n’atteignent pas 100 % quand je les additionne ?

Les indicateurs de livrabilité des e-mails (livraisons, rebonds et taux de courriers indésirables) peuvent ne pas atteindre 100 % en raison des e-mails qui font l'objet d'un échec provisoire d'envoi et qui ne sont pas délivrés après une période de nouvelle tentative pouvant aller jusqu'à 72 heures.

Les échecs provisoires d’envoi désignent les e-mails rejetés en raison d’un problème temporaire ou transitoire, tels qu’une « boîte de réception pleine » ou un « serveur temporairement non accessible », etc. Si un e-mail ayant fait l'objet d'un échec provisoire d'envoi n'est toujours pas livré après 72 heures, cet e-mail ne sera pas pris en compte dans les indicateurs de livraison de la campagne.

### Que sont les pixels de suivi ouverts ?

[Les pixels de suivi ouverts]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) utilisent le domaine de suivi des clics de l'e-mail de l'expéditeur pour suivre les événements d'ouverture des e-mails. Le pixel est une balise d’image jointe à l’HTML de l’e-mail. Il s’agit généralement du dernier élément HTML dans la balise du corps. Lorsqu’un utilisateur charge ses e-mails, une requête est effectuée pour charger l’image à partir du domaine de suivi de la marque, ce qui enregistre un événement d’ouverture.

### Que se passe-t-il lors de l’arrêt d’une campagne ou d’un Canvas par e-mail ?

Les utilisateurs ne pourront plus entrer dans le Canvas et aucun message supplémentaire ne sera envoyé. Pour les campagnes et les Canvas par e-mail, le bouton d’arrêt ne signifie pas que les envois s’arrêteront immédiatement. En effet, une fois que les demandes d’envoi sont envoyées, il est impossible d’empêcher leur livraison à l’utilisateur.

### Pourquoi est-ce que je constate plus de clics que d’ouvertures d’e-mail ?

Vous pourriez constater plus de clics que d’ouvertures pour une des raisons suivantes :
- Les utilisateurs effectuent plusieurs clics sur le corps de l’e-mail pour une seule ouverture.
- Les utilisateurs cliquent sur certains liens de l’e-mail dans le panneau de prévisualisation sur leur téléphone. Dans ce cas, Braze enregistre que cet e-mail a été cliqué et pas ouvert.
- Les utilisateurs ouvrent à nouveau un e-mail qu’ils ont prévisualisé auparavant.

### Pourquoi le nombre d'ouvertures et de clics sur les e-mails est-il nul ?

Il se peut que vous ne voyiez aucun e-mail ouvert ou cliqué si votre domaine de suivi est mal configuré. Cela peut être dû à l'une des raisons suivantes :
- Il y a un problème SSL où les URL de suivi sont `http` au lieu de `https`.
- Il y a un problème avec votre réseau de diffusion contenu dans la chaîne de caractères de l'agent utilisateur sur les événements d'ouverture, les événements de clic, ou les deux, ne sont pas remplis.

### Quels sont les risques potentiels de déclencher des clics sur le serveur ?

Certains éléments d'un e-mail, par exemple la longueur excessive du message ou le nombre de points d'exclamation, sont susceptibles de déclencher des réponses de sécurité par e-mail. Ces réponses peuvent avoir un impact sur les rapports, la réputation de l’adresse IP et peuvent entraîner des désabonnements d'utilisateurs. 

Pour les meilleures pratiques sur la façon de gérer ces réponses, consultez [Gestion des augmentations des taux de clics]({{site.baseurl}}/help/help_articles/email/open_rates/).

### Comment supprimer une adresse e-mail de la liste de rebond ou de spam ?

Vous pouvez supprimer les e-mails renvoyés et les e-mails figurant sur la liste des spams à l'aide des endpoints suivants :
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

### Comment vérifier le groupe d’abonnement e-mail d’un utilisateur ?

- **Profil de l'utilisateur :** Les profils d'utilisateurs individuels peuvent être consultés via le tableau de bord Braze depuis la page [Rechercher des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Lorsqu'on est dans un profil utilisateur, sous l'onglet Engagement, on peut voir les groupes d'abonnement par e-mail d'un utilisateur.
- **API REST :** Les profils d'utilisateurs individuels du groupe d'abonnement peuvent être consultés par l'[endpoint de liste des groupes d'abonnement des utilisateurs]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou l'[endpoint de liste du statut du groupe d'abonnement des utilisateurs]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) en utilisant l'API REST de Braze. 

### Comment puis-je mettre à jour le groupe d'abonnement par e-mail d'un utilisateur ?

Les utilisateurs ne pourront plus entrer dans le Canvas et aucun message supplémentaire ne sera envoyé. Pour les campagnes et les Canvas par e-mail, le bouton d’arrêt ne signifie pas que les envois s’arrêteront immédiatement. En effet, une fois que les demandes d’envoi sont envoyées, il est impossible d’empêcher leur livraison à l’utilisateur.

### Braze peut-il suivre les liens de désabonnement comptabilisés dans la métrique "Désabonnement" ?

Braze suit les liens de désabonnement si le Liquid suivant est utilisé dans les e-mails : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Puis-je ajouter un lien « Afficher cet e-mail dans un navigateur » à mes e-mails ?

Non, Braze n’offre pas cette fonctionnalité. C’est parce qu’une majorité croissante d’e-mails sont ouverts sur des appareils mobiles et des clients par e-mail modernes, qui rendent les images et le contenu sans aucun problème.

**Contournement :** Pour obtenir le même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de destination externe (comme votre site Web), qui peut ensuite être liée à partir de la campagne d'e-mail que vous construisez en utilisant l'outil **Link** lors de l'édition du corps de l'e-mail.

