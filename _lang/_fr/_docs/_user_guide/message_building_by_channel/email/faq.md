---
nav_title: Foire aux questions
article_title: Email FAQs
page_order: 12
description: "Cette page fournit des réponses aux questions fréquemment posées sur la messagerie électronique."
channel: Email
---

# Email FAQs

### Puis-je ajouter un lien "Voir cet e-mail dans un navigateur" à mes courriels?

Non, Braze n'offre pas cette fonctionnalité. Ceci est dû au fait qu'une majorité croissante de courriels est ouverte sur les appareils mobiles et les clients de messagerie modernes, qui rendent les images et le contenu sans aucun problème.

**Solution de contournement :** Pour atteindre ce même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de renvoi externe (comme votre site Web), qui peut ensuite être lié à partir de la campagne d'email que vous construisez en utilisant l'outil **Lien** lors de l'édition du corps du courriel.

### Que se passe-t-il lorsqu'un email est envoyé et que plusieurs profils ont la même adresse e-mail ?

Si plusieurs utilisateurs avec des e-mails correspondants sont tous dans le segment pour recevoir une campagne, un profil utilisateur aléatoire avec cette adresse email est choisi au moment de l'envoi. De cette façon, le courriel n’est envoyé qu’une seule fois et est dédupliqué, ce qui garantit qu’il ne frappe pas le même e-mail plusieurs fois.

Notez que cette déduplication se produit si les utilisateurs ciblés sont inclus dans la même expédition. Par conséquent, les campagnes déclenchées peuvent entraîner des envois multiples à la même adresse de courriel (même dans un délai où les utilisateurs pourraient être exclus en raison de leur rééligibilité) si des utilisateurs différents avec des emails correspondants enregistrent l'événement de déclenchement à différents moments. Les utilisateurs ne sont pas déduits par email sur Canvas entrée, Il est donc possible que les utilisateurs ne soient pas déconnectés au-delà de la première étape d’un Canvas s’ils progressent à des moments légèrement différents en raison d’une entrée limitée.

Lorsqu'un utilisateur lié à une adresse e-mail donnée ouvre ou clique sur un e-mail, tous les profils d'utilisateurs qui partagent cette adresse e-mail sont marqués comme ouvrant et en cliquant sur la campagne. Vous pouvez identifier les utilisateurs ciblés à partir du profil de l'utilisateur téléchargez dans **Recherche d'utilisateur**. L'utilisateur qui a réellement reçu l'e-mail aura un horodatage défini pour le champ « received_email» dans le résumé de la campagne associée; les autres utilisateurs n’auront pas ce champ, juste « date ».

**Exception : Campagnes déclenchées par l'API**

Les campagnes déclenchées par l'API vont déduper ou envoyer des dupes selon l'endroit où le public est défini. En bref, les emails en double doivent être directement ciblés en tant que `User_ids` séparés dans l'appel afin de recevoir plusieurs détails. Voici trois scénarios possibles pour les campagnes déclenchées par l'API :

- **Scénario 1 : Dupliquer les e-mails dans le segment cible (DEDUPED):** Si le même e-mail apparaît dans plusieurs profils d'utilisateurs qui sont regroupés dans les filtres d'audience du tableau de bord pour une campagne déclenchée par l'API, seul un des profils recevra l'email.
- **Scénario 2 : Dupliquer les e-mails dans différents user_ids dans l'objet destinataire (DUPE SENDS):** Si le même email apparaît dans plusieurs `External_user_IDs` référencé par l'objet "destinataires", le courriel sera envoyé deux fois.
- **Scénario 3: Emails dupliqués à cause de dupliquer user_ids dans l'objet destinataire (DEDUPED):** Si vous essayez d'ajouter le même profil utilisateur deux fois, seul un des profils recevra l'email.

### Qu'est-ce qu'un "bon" taux de délivrabilité du courrier électronique?

Généralement, le « nombre magique» est d’environ 95% des messages envoyés, avec un taux de rebond inférieur à 3%. Si votre livrabilité diminue en dessous de cela, il y a généralement lieu de s'inquiéter.

Cependant, un taux peut être supérieur à 95% et comporte toujours des problèmes de délivrabilité. Par exemple, si tous vos rebonds proviennent d'un domaine particulier, c'est un signal clair qu'il y a un problème de réputation avec ce fournisseur.

De plus, les messages peuvent être envoyés et se retrouver dans le courrier indésirable, ce qui peut entraîner de graves problèmes de réputation. Il est important de ne pas seulement surveiller le nombre de messages envoyés, mais aussi ouvrir et cliquer sur les tarifs pour déterminer si les utilisateurs voient réellement les messages dans leurs boîtes de réception. Étant donné que les prestataires ne signalent généralement pas toutes les instances de spam, un taux de spam même de 1 % pourrait être source de préoccupation et d'analyses plus approfondies.

Enfin, votre entreprise et les types d'e-mails que vous envoyez peuvent également affecter la livraison. Par exemple, quelqu'un qui envoie des courriels transactionnels pour la plupart devrait s'attendre à voir un meilleur taux que celui qui envoie de nombreux messages de marketing.
