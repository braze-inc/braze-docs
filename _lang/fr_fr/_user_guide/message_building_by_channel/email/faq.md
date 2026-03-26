---
nav_title: FAQ
article_title: FAQ sur les e-mails
page_order: 15
description: "Cette page fournit des réponses aux questions fréquemment posées sur les communications par e-mail."
channel: email

---

# Foire aux questions

> Cet article fournit des réponses à des questions fréquemment posées sur les e-mails.

### Que se passe-t-il lorsqu'un e-mail est envoyé et que plusieurs profils ont la même adresse e-mail ?

Si plusieurs utilisateurs avec la même adresse e-mail se trouvent dans un segment destiné à recevoir une campagne, un profil utilisateur aléatoire avec cette adresse e-mail est choisi au moment de l'envoi. De cette façon, l'e-mail n'est envoyé qu'une seule fois et est dédupliqué, garantissant ainsi qu'il ne touche pas la même adresse e-mail plusieurs fois.

Notez que cette déduplication se produit lorsque les utilisateurs ciblés sont inclus dans le même envoi. Les campagnes déclenchées peuvent entraîner plusieurs envois à la même adresse e-mail (même pendant une période où les utilisateurs pourraient être exclus en raison de leur rééligibilité) si des utilisateurs différents avec des adresses e-mail correspondantes enregistrent l'événement déclencheur à des moments différents. Les utilisateurs ne sont pas dédupliqués par e-mail à l'entrée du Canvas, il est donc possible qu'ils ne soient pas dédupliqués au-delà de la première étape d'un Canvas s'ils progressent à des moments légèrement différents en raison de l'entrée limitée en débit. Lorsqu'un utilisateur lié à une adresse e-mail donnée ouvre ou clique sur un e-mail, tous les profils utilisateur partageant cette adresse e-mail sont marqués comme ayant ouvert ou cliqué sur la campagne.

#### Exception : campagnes déclenchées par API

Les campagnes déclenchées par l'API dédupliqueront ou enverront des doublons en fonction de l'endroit où l'audience est définie. Les e-mails dupliqués doivent être ciblés séparément dans l'appel API en utilisant des `user_ids` distincts afin de recevoir plusieurs envois. Voici trois scénarios possibles pour les campagnes déclenchées par une API :

- **Scénario 1 : E-mails dupliqués dans le segment cible :** Si le même e-mail apparaît dans plusieurs profils utilisateur regroupés dans les filtres d'audience du tableau de bord pour une campagne déclenchée par l'API, un seul des profils recevra l'e-mail.
- **Scénario 2 : E-mails dupliqués dans différents `user_ids` dans l'objet destinataires :** Si le même e-mail apparaît dans plusieurs valeurs `external_user_id` référencées par l'objet `recipients`, l'e-mail sera envoyé deux fois.
- **Scénario 3 : E-mails dupliqués en raison de `user_ids` en double dans l'objet destinataires :** Si vous essayez d'ajouter le même profil utilisateur deux fois, seul un des profils recevra l'e-mail.

### Les mises à jour de mes paramètres d'e-mails sortants s'appliqueront-elles rétroactivement ?

Non. Les mises à jour des paramètres d'e-mails sortants n'affectent pas rétroactivement les envois existants. Par exemple, modifier votre nom d'affichage par défaut dans les paramètres d'e-mail ne remplacera pas automatiquement le nom d'affichage par défaut existant dans vos campagnes actives ou vos Canvas. 

### À quoi correspond un « bon » taux de distribution des e-mails ?

En général, le « nombre magique » est d'environ 98 % des messages livrés avec un taux de rebond ne dépassant pas 3 %. Si votre taux de livraison tombe en dessous de ce seuil, il y a généralement lieu de s'inquiéter.

Cependant, un taux supérieur à 98 % peut tout de même présenter des problèmes de livrabilité. Par exemple, si tous vos rebonds proviennent d'un seul domaine, c'est un signal clair d'un problème de réputation avec ce fournisseur.

De plus, les messages peuvent être livrés mais finir dans les courriers indésirables, ce qui indique des problèmes de réputation potentiellement graves. Il est important de surveiller non seulement le nombre de messages livrés, mais aussi les taux d'ouverture et de clics pour déterminer si les utilisateurs voient effectivement les messages dans leurs boîtes de réception. Comme les fournisseurs ne signalent généralement pas toutes les instances de spam, un taux de spam ne serait-ce que de 1 % pourrait être source de préoccupation et justifier une analyse approfondie.

Enfin, votre activité et les types d'e-mails que vous envoyez peuvent également affecter la livraison. Par exemple, une personne envoyant principalement des [e-mails transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) devrait s'attendre à un meilleur taux qu'une personne envoyant de nombreux messages marketing.

### Pourquoi mes indicateurs de distribution d'e-mails n'atteignent-ils pas 100 % quand je les additionne ?

Les indicateurs de distribution des e-mails (livraisons, rebonds et taux de courriers indésirables) peuvent ne pas atteindre 100 % en raison des e-mails ayant fait l'objet d'un échec provisoire d'envoi et qui ne sont pas livrés après une période de nouvelle tentative pouvant aller jusqu'à 72 heures.

Les échecs provisoires d'envoi désignent les e-mails rejetés en raison d'un problème temporaire ou transitoire, comme une « boîte de réception pleine » ou un « serveur temporairement indisponible ». Si un e-mail ayant fait l'objet d'un échec provisoire d'envoi n'est toujours pas livré après 72 heures, il ne sera pas pris en compte dans les indicateurs de livraison de la campagne.

### Que sont les pixels de suivi d'ouverture ?

Les [pixels de suivi d'ouverture]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) utilisent le domaine de suivi des clics de l'expéditeur pour suivre les événements d'ouverture des e-mails. Le pixel est une balise d'image ajoutée au HTML de l'e-mail. Il s'agit généralement du dernier élément HTML dans la balise body. Lorsqu'un utilisateur charge son e-mail, une requête est effectuée pour charger l'image à partir du domaine de suivi de marque, ce qui enregistre un événement d'ouverture.

### Que se passe-t-il lors de l'arrêt d'une campagne e-mail ou d'un Canvas ?

Les utilisateurs ne pourront plus entrer dans le Canvas et aucun message supplémentaire ne sera envoyé. Pour les campagnes e-mail et les Canvas, le bouton d'arrêt ne stoppe pas immédiatement les envois. En effet, une fois que les demandes d'envoi sont transmises, il est impossible d'empêcher leur livraison à l'utilisateur.

### Pourquoi est-ce que je constate plus de clics que d'ouvertures d'e-mail ?

Vous pourriez constater plus de clics que d'ouvertures pour l'une des raisons suivantes :
- Les utilisateurs effectuent plusieurs clics dans le corps de l'e-mail pour une seule ouverture.
- Les utilisateurs cliquent sur certains liens de l'e-mail dans le panneau de prévisualisation de leur téléphone. Dans ce cas, Braze enregistre que cet e-mail a été cliqué mais pas ouvert.
- Les utilisateurs ouvrent à nouveau un e-mail qu'ils avaient prévisualisé auparavant.

### Pourquoi le nombre d'ouvertures et de clics sur les e-mails est-il nul ?

Il se peut que vous ne voyiez aucune ouverture ou clic si votre domaine de suivi est mal configuré. Cela peut être dû à l'une des raisons suivantes :
- Un problème SSL où les URL de suivi sont en `http` au lieu de `https`.
- Un problème avec votre réseau de diffusion de contenu où la chaîne de caractères de l'agent utilisateur sur les événements d'ouverture, les événements de clic, ou les deux, n'est pas renseignée.

### Quels sont les risques potentiels liés aux clics déclenchés côté serveur ?

Certains éléments d'un e-mail, comme un message trop long ou un nombre excessif de points d'exclamation, peuvent déclencher des réponses de sécurité. Ces réponses peuvent affecter les rapports et la réputation de l'adresse IP, et entraîner des désabonnements.

Pour les bonnes pratiques sur la gestion de ces réponses, consultez [Gestion des augmentations des taux de clics]({{site.baseurl}}/help/help_articles/email/open_rates/).

### Braze peut-il suivre les liens de désabonnement comptabilisés dans l'indicateur « Désabonnement » ?

Braze suit les liens de désabonnement si le Liquid suivant est utilisé dans les e-mails : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Puis-je ajouter un lien « Afficher cet e-mail dans un navigateur » à mes e-mails ?

Non, Braze ne propose pas cette fonctionnalité. En effet, une majorité croissante d'e-mails sont ouverts sur des appareils mobiles et dans des clients de messagerie modernes, qui affichent les images et le contenu sans problème.

**Solution de contournement :** Pour obtenir le même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de destination externe (comme votre site web), puis y ajouter un lien depuis la campagne e-mail que vous créez en utilisant l'outil **Link** lors de l'édition du corps de l'e-mail.

### Pourquoi mes utilisateurs sont-ils automatiquement désabonnés par les logiciels de sécurité des e-mails ?

Certains outils de sécurité des e-mails d'entreprise (tels que Barracuda, Proofpoint et autres services similaires) préchargent ou analysent toutes les URL contenues dans les e-mails entrants, y compris les liens de désabonnement. Cela peut entraîner des désabonnements involontaires lorsque l'outil de sécurité suit le lien de désabonnement en un clic.

Pour atténuer ce problème :

- **Recommandez aux destinataires d'ajouter votre domaine d'envoi à leur liste d'autorisation :** Collaborez avec les équipes informatiques des destinataires concernés afin d'ajouter votre domaine d'envoi et les domaines de suivi Braze à leur liste d'autorisation de sécurité des e-mails.
- **Utilisez un centre de préférences :** Au lieu d'un lien de désabonnement direct, utilisez un [centre de préférences]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) qui nécessite une interaction de l'utilisateur pour confirmer le désabonnement. Les scanners de sécurité ne remplissent généralement pas les formulaires comportant plusieurs étapes.
- **Examinez les journaux de désabonnement :** Vérifiez l'en-tête `User-Agent` et l'adresse IP dans les données d'événements de désabonnement de Currents afin d'identifier les schémas correspondant à une analyse automatisée (par exemple, des en-têtes `User-Agent` identiques pour plusieurs désabonnements).

Pour plus d'informations sur l'impact de l'analyse côté serveur sur les indicateurs relatifs aux e-mails, consultez [Gestion de l'augmentation des taux de clics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#handling-increases-in-click-rates).

### Pourquoi mon taux d'ouverture automatique a-t-il changé de manière inattendue ?

Les [ouvertures automatiques]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens) sont déclenchées par des fonctionnalités de sécurité des e-mails telles que la protection de la confidentialité dans Mail d'Apple (MPP), qui précharge le contenu des e-mails (y compris le pixel de suivi) sans que l'utilisateur n'ouvre physiquement l'e-mail. Les taux d'ouverture automatique peuvent varier en fonction des éléments suivants :

- L'évolution de la proportion de votre audience utilisant Apple Mail ou d'autres clients de messagerie dotés de fonctionnalités de confidentialité.
- Les mises à jour des fonctionnalités de confidentialité des fournisseurs de messagerie ou des comportements de détection des robots.
- Les modifications de la segmentation ou du ciblage de votre audience.

Les pourcentages d'ouverture automatique ne constituent pas une mesure fiable de l'engagement réel. Pour obtenir une vision plus précise des performances de vos e-mails, concentrez-vous sur les *autres ouvertures* (ouvertures non automatiques) et les *clics uniques*. Vous pouvez également comparer ces indicateurs au fil du temps à l'aide du [tableau de bord des performances des e-mails]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard/).

### L'indicateur *Ouvertures uniques* inclut-il les *ouvertures automatiques* ?

Oui. Les *ouvertures uniques* incluent les *ouvertures automatiques*. Dans la page **Analyse des campagnes** et le **générateur de rapports**, vous pouvez consulter ces deux indicateurs.