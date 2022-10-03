---
nav_title: FAQ
article_title: FAQ sur les e-mails
page_order: 12
description: "Le présent article fournit des réponses aux questions fréquemment posées sur les courriers électroniques."
channel: E-mail

---

# FAQ sur les e-mails

### Puis-je ajouter un lien « Afficher cet e-mail dans un navigateur » à mes e-mails ?

Non, Braze n’offre pas cette fonctionnalité. C’est parce qu’une majorité croissante d’e-mails sont ouverts sur des appareils mobiles et des clients par e-mail modernes, qui rendent les images et le contenu sans aucun problème.

**Contournement :** Pour obtenir ce même résultat, vous pouvez héberger le contenu de votre e-mail sur une page d’accueil externe (comme votre site Internet), qui peut ensuite être lié à la campagne par e-mail que vous construisez à l’aide de l’outil **Link (Lien)** lors de la modification du corps de l’email.

### Que se passe-t-il lorsqu’un e-mail est envoyé et que plusieurs profils ont la même adresse e-mail ?

Si plusieurs utilisateurs avec des e-mails correspondants sont tous dans le même segment pour recevoir une campagne, un profil utilisateur aléatoire avec cette adresse e-mail sera choisi au moment de l’envoi. De cette façon, l’e-mail n’est envoyé qu’une seule fois et est dédupliqué, ce qui garantit qu’il n’atteint pas la même adresse e-mail plusieurs fois.

Notez que cette déduplication se produit si les utilisateurs ciblés sont inclus dans le même envoi. Par conséquent, les campagnes déclenchées peuvent entraîner plusieurs envois à la même adresse e-mail (même dans une période où les utilisateurs peuvent être exclus en raison de la rééligibilité) si différents utilisateurs avec des e-mails correspondants enregistrent l’événement déclencheur à différents moments. Les utilisateurs ne sont pas dédupliqués par e-mail sur l’entrée Canvas, il est donc possible que les utilisateurs ne soient pas dédupliqués au-delà de la première étape d’un Canvas s’ils progressent à des moments légèrement différents en raison de l’entrée limitée. Lorsqu’un utilisateur lié à une adresse e-mail donnée ouvre ou clique sur un e-mail, tous les profils d’utilisateur qui partagent cette adresse e-mail sont marqués comme ayant ouvert et cliqué sur la campagne.

#### Exception : Campagnes déclenchées par une API

Les campagnes déclenchées par une API dédupliquent ou envoient des e-mails en double selon l’endroit où l’audience est définie. En résumé, les e-mails dupliqués doivent être directement ciblés comme `user_ids` différents dans le cadre de l’appel afin de recevoir plusieurs détails. Voici trois scénarios possibles pour les campagnes déclenchées par une API :

- **Scénario 1 : Dupliquer les e-mails dans le segment cible :** Si le même e-mail apparaît dans plusieurs profils utilisateur regroupés dans les filtres d'audience du tableau de bord pour une campagne déclenchée par une API, un seul des profils recevra l’e-mail.
- **Scénario 2 : Dupliquer les e-mails en différents `user_ids` dans l’objet Destinataires :** Si le même e-mail apparaît dans plusieurs `External_user_IDs` référencés par l’objet « Destinataires », l’e-mail sera envoyé deux fois.
- **Scénario 3 : Dupliquer les e-mails en raison d’_id utilisateur en double dans l’objet Destinataires :** Si vous essayez d’ajouter le même profil utilisateur deux fois, seul un des profils recevra l’e-mail.

### Qu’est-ce qu’un « bon » taux de délivrabilité par e-mail ?

En général, le « nombre magique » correspond à environ 95 % de messages livrés avec un taux de rebond inférieur ou égal à 3 %. Si votre capacité de délivrabilité est inférieure à celui-ci, il y a généralement un problème.

Cependant, un taux peut être supérieur à 95 % et toujours y avoir des problèmes de délivrabilité. Par exemple, si toutes vos rebonds proviennent d’un domaine particulier, c’est un signal clair qu’il existe un problème de réputation avec ce fournisseur.

De plus, les messages peuvent être livrés et terminer dans les courriers indésirables, ce qui indique des problèmes de réputation potentiellement graves. Il est important de surveiller non seulement le nombre de messages livrés, mais aussi les taux d’ouverture et de clics pour déterminer si les utilisateurs voient effectivement les messages dans leurs boîtes de réception. Comme les fournisseurs ne signalent généralement pas toutes les instances de spam, un taux de spam de même 1 % pourrait être source de préoccupation et d’analyse approfondie.

Enfin, votre entreprise et les types d’e-mails que vous envoyez peuvent également affecter la délivrabilité. Par exemple, quelqu’un qui envoie principalement des [e-mails transactionnels][1] devrait s’attendre à voir un meilleur taux que quelqu’un qui envoie de nombreux messages marketing.


[1]: {{site.baseurl}}/api/api_campaigns/transactional_api_campaign