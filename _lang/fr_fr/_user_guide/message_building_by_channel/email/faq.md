---
nav_title: FAQ
article_title: "FAQ sur l'e-mail"
page_order: 14
description: "Cette page fournit des réponses aux questions fréquemment posées sur l'envoi de messages par e-mail."
channel: email

---

# Questions fréquemment posées

> Cet article apporte des réponses à certaines questions fréquemment posées sur les e-mails.

### Que se passe-t-il lorsqu'un e-mail est envoyé et que plusieurs profils ont la même adresse e-mail ?

Si plusieurs utilisateurs dont l'adresse e-mail correspond sont tous dans un segment pour recevoir une campagne, un profil utilisateur aléatoire avec cette adresse e-mail est choisi au moment de l'envoi. De cette manière, l'e-mail n'est envoyé qu'une seule fois et est dédupliqué, ce qui garantit que l'e-mail n'est pas envoyé plusieurs fois à la même adresse électronique.

Notez que ce dédoublonnage se produit si les utilisateurs ciblés sont inclus dans le même envoi. Les campagnes déclenchées peuvent donner lieu à des envois multiples à la même adresse e-mail (même au cours d'une période où les utilisateurs pourraient être exclus en raison d'une rééligibilité) si différents utilisateurs ayant des adresses e-mail correspondantes enregistrent l'événement déclencheur à des moments différents. Les utilisateurs ne sont pas dédupliqués par e-mail lors de l'entrée dans le Canvas, il est donc possible que les utilisateurs ne soient pas dédupliqués au-delà de la première étape d'un Canvas s'ils progressent à des moments légèrement différents en raison d'un taux d'entrée limité. Lorsqu'un utilisateur lié à une adresse e-mail donnée ouvre ou clique sur un e-mail, tous les profils utilisateurs qui partagent l'adresse e-mail sont marqués comme ayant ouvert et cliqué sur la campagne.

#### Exception : Campagnes déclenchées par l'API

Les campagnes déclenchées par l'API dédupliqueront ou enverront des déduplicats en fonction de l'endroit où l'audience est définie. En bref, les e-mails en double doivent être directement ciblés en tant que `user_ids` distincts dans l'appel API afin de recevoir plusieurs détails. Voici trois scénarios possibles pour les campagnes déclenchées par l'API :

- **Scénario 1 : Les e-mails en double dans le segmentation cible :** Si le même e-mail apparaît dans plusieurs profils utilisateurs regroupés dans les filtres d'audience du tableau de bord pour une campagne déclenchée par l'API, un seul des profils recevra l'e-mail.
- **Scénario 2 : Duplication d'e-mails dans différents `user_ids` au sein de l'objet des destinataires :** Si le même e-mail apparaît dans plusieurs `External_user_IDs` référencés par l'objet `recipients``, l'e-mail sera envoyé deux fois.
- **Scénario 3 : E-mails dupliqués en raison de la duplication de user_ids dans l'objet des destinataires :** Si vous essayez d'ajouter deux fois le même profil utilisateur, un seul des profils recevra l'e-mail.

### Les mises à jour de mes paramètres d'e-mail sortant s'appliquent-elles rétroactivement ?

Non. Les mises à jour apportées aux paramètres des e-mails sortants n'ont pas d'effet rétroactif sur les envois existants. Par exemple, la modification de votre nom d'affichage par défaut dans les paramètres de l'e-mail ne remplacera pas automatiquement le nom d'affichage par défaut existant dans vos campagnes actives ou Canvases. 

### Qu'est-ce qu'un "bon" taux de réception/distribution des e-mails ?

En règle générale, le "chiffre magique" se situe autour de 98 % d'envois de messages avec un taux de rebond ne dépassant pas 3 %. Si votre réception/distribution est inférieure à ce seuil, il y a généralement lieu de s'inquiéter.

Cependant, un taux peut être supérieur à 98 % et présenter des problèmes de livrabilité. Par exemple, si tous vos rebonds proviennent d'un domaine particulier, cela indique clairement qu'il y a un problème de réputation avec ce fournisseur.

En outre, il se peut que les messages soient envoyés et finissent dans les spams, ce qui peut entraîner de graves problèmes de réputation. Il est important de surveiller non seulement le nombre de messages envoyés, mais aussi les taux d'ouverture et de clics afin de déterminer si les utilisateurs voient réellement les messages dans leur boîte de réception. Comme les fournisseurs ne signalent généralement pas chaque instance de courrier indésirable, un taux de courrier indésirable ne serait-ce que de 1 % peut être une source d'inquiétude et justifier une analyse plus approfondie.

Enfin, votre activité et les types d'e-mails que vous envoyez peuvent également avoir une incidence sur la réception/distribution. Par exemple, une personne qui envoie principalement des [e-mails transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) doit s'attendre à un meilleur taux que celle qui envoie de nombreux messages marketing.

### Pourquoi les indicateurs de réception/distribution de mes e-mails ne sont-ils pas égaux à 100 % ?

Les indicateurs de réception/distribution des e-mails (livraisons, rebonds et taux de spam) peuvent ne pas atteindre 100 % en raison des e-mails qui font l'objet d'un échec provisoire d'envoi et qui ne sont pas livrés après une période de réessai pouvant aller jusqu'à 72 heures.

Les échecs provisoires d'envoi sont des e-mails qui rebondissent en raison d'un problème temporaire ou transitoire tel que "boîte aux lettres pleine", "serveur temporairement indisponible", etc. Si un échec provisoire d'envoi n'est toujours pas réception/distribution après 72 heures, cet e-mail ne sera pas pris en compte dans les indicateurs de livraison de la campagne.

### Qu'est-ce qu'un pixel de suivi ouvert ?

[Les pixels de suivi des ouvertures]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) exploitent le domaine de suivi des clics de l'expéditeur pour suivre les événements d'ouverture des e-mails. Le pixel est une étiquette d'image ajoutée au code HTML de l'e-mail. Il s'agit le plus souvent du dernier élément HTML à l'intérieur de l'étiquette body. Lorsqu'un utilisateur charge son e-mail, une demande est faite pour remplir l'image à partir du domaine de suivi de la marque, qui enregistre un événement d'ouverture.

### Que se passe-t-il en cas d'interruption d'une campagne d'e-mailing ou d'un canvas ?

Les utilisateurs ne pourront plus entrer dans le canvas et aucun autre message ne sera envoyé. Pour les campagnes d'e-mail et les toiles, le bouton d'arrêt ne signifie pas que l'envoi s'arrêtera immédiatement. En effet, lorsque les demandes d'envoi sont envoyées, il est impossible d'empêcher qu'elles soient remises à l'utilisateur.

### Pourquoi y a-t-il plus de clics sur les e-mails que d'ouvertures ?

Il se peut que le nombre de clics soit supérieur au nombre d'ouvertures pour l'une des raisons suivantes :
- Les utilisateurs effectuent plusieurs clics sur le corps de l'e-mail au cours d'une seule ouverture.
- Les utilisateurs cliquent sur certains liens d'e-mails dans le volet de prévisualisation de leur téléphone. Dans ce cas, Braze enregistre cet e-mail comme ayant été cliqué mais non ouvert.
- Les utilisateurs rouvrent un e-mail qu'ils ont prévisualisé précédemment.

### Pourquoi le nombre d'ouvertures et de clics sur les e-mails est-il nul ?

Il se peut que vous ne voyiez aucun e-mail ouvert ou cliqué si votre domaine de suivi est mal configuré. Cela peut être dû à l'une des raisons suivantes :
- Il y a un problème SSL où les URL de suivi sont `http` au lieu de `https`.
- Il y a un problème avec votre réseau de diffusion contenu dans la chaîne de caractères de l'agent utilisateur sur les événements d'ouverture, les événements de clic, ou les deux, ne sont pas remplis.

### Quels sont les risques potentiels liés au déclenchement de clics sur le serveur ?

Certains éléments d'un message e-mail, tels que des messages trop longs ou un trop grand nombre de points d'exclamation, sont susceptibles de déclencher des réactions de sécurité. Ces réponses peuvent avoir un impact sur les rapports, la réputation de l'IP et peuvent conduire les utilisateurs à se désabonner. 

Pour connaître les meilleures pratiques sur la manière de gérer ces réponses, reportez-vous à la section [Gérer l'augmentation des taux de clics]({{site.baseurl}}/help/help_articles/email/open_rates/).

### Braze peut-il suivre les liens de désabonnement comptabilisés dans les indicateurs de "désabonnement" ?

Braze suit les liens de désabonnement si le liquide suivant est utilisé dans les e-mails : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Puis-je ajouter un lien "afficher cet e-mail dans un navigateur" à mes e-mails ?

Non, Braze n'offre pas cette fonctionnalité. En effet, une majorité croissante d'e-mails est ouverte sur des appareils mobiles et des clients de messagerie modernes, qui restituent les images et le contenu sans problème.

**Solution de contournement :** Pour obtenir le même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de renvoi externe (votre site web, par exemple), à laquelle vous pouvez ensuite vous connecter à partir de la campagne d'e-mails que vous créez à l'aide de l'outil **Lien** lorsque vous modifiez le corps de l'e-mail.

