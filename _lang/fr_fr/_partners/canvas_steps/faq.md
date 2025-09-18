---
nav_title: FAQ
article_title: "FAQ de synchronisation de l'audience"
description: "Cet article fournit des réponses aux questions fréquemment posées sur la synchronisation de l'audience."
page_order: 80
Tool:
  - Canvas

---

# Questions fréquemment posées

> Cet article fournit des réponses à certaines questions fréquemment posées sur la synchronisation de l'audience.

### Combien de temps faut-il pour que mes audiences soient générées dans le tableau de bord de mon partenaire de synchronisation d’audiences ?

Le temps nécessaire pour générer une audience dépend du partenaire spécifique. Tous les réseaux traiteront les requêtes de Braze et tenteront de faire correspondre les utilisateurs. Ce processus peut généralement prendre de 6 à 48 heures.

Vous pouvez vérifier la plage de temps spécifique dans la section Résolution des problèmes de la documentation de chaque partenaire Audience Sync.

### Quel type de données first-party puis-je utiliser dans ma synchronisation d'audience ?

Les champs spécifiques utilisés pour chaque partenaire peuvent varier en fonction des exigences du partenaire. 

Par exemple, lorsque vous configurez un flux de synchronisation d’audiences dans Facebook, vous pouvez utiliser une grande variété de champs first party tels que l'e-mail, le téléphone, le prénom et le nom de famille, tandis qu'avec Snapchat, vous ne pouvez sélectionner que l'e-mail, le téléphone ou l'ID publicitaire mobile. 

Il est important de noter que les champs utilisateur que vous pouvez sélectionner pour synchroniser correspondent aux attributs standard de Braze et aux identifiants publicitaires mobiles. Vous devez vous assurer de transmettre correctement cette donnée via nos SDK ou API. 

### Que se passe-t-il lorsque mes données sont traitées pour être envoyées à chaque partenaire Audience Sync ?

Les données que vous sélectionnez pour envoyer à votre destination de synchronisation d’audiences seront normalisées. Chaque partenaire peut avoir des spécifications différentes pour la normalisation des données en fonction de leurs exigences API, alors veuillez consulter chaque endpoint spécifique au partenaire pour plus de détails.

De plus, Braze hachera toutes les données avant de synchroniser les utilisateurs avec nos partenaires de synchronisation d'audience, garantissant que toutes les IIP sont hachées en utilisant SHA256.

### Pourquoi puis-je sélectionner plusieurs identifiants en une seule étape pour certains partenaires, mais ne puis-je sélectionner qu'un seul identifiant pour d'autres ?

Ceci est déterminé par les méthodes d'intégration des partenaires et n'est pas contrôlé par Braze. Certains partenaires (comme Meta) autorisent la synchronisation de plusieurs identifiants, tandis que d'autres partenaires (comme Google) n'autorisent qu'un seul identifiant à être synchronisé avec un utilisateur à un moment donné.

### Comment reconnecter mon intégration ?

Si l'utilisateur précédent qui a connecté l'intégration ne fait plus partie de votre utilisateur, vous devrez mettre à jour l'intégration avec le nouvel utilisateur. Vous pouvez le faire en sélectionnant **Confirmer**. Notez que cela peut perturber les toiles actives.

L'utilisateur qui se reconnecte doit avoir un accès en lecture et en écriture à toutes les audiences afin que les utilisateurs puissent être synchronisés avec les partenaires. Vérifiez que l'utilisateur qui reconnecte l'intégration a accès aux mêmes comptes publicitaires et aux mêmes audiences. Il ne devrait pas être nécessaire de modifier les étapes du canvas existantes. 

### Quelles sont les erreurs les plus courantes qui peuvent se produire lors de la création et de la gestion de mes synchronisations d'audience ?

- **Jeton non valide**<br>
  - Les causes typiques incluent si vous avez changé votre mot de passe pour vous connecter à un réseau publicitaire spécifique ou si vos identifiants expirent.
  - Pour résoudre ce problème, il suffit d'aller sur la page partenaire spécifique en question pour déconnecter et reconnecter votre compte.
- **Taille de l'audience trop petite**<br>
  - Cette erreur se produira généralement si vous avez créé une étape de synchronisation d'audience qui supprime des utilisateurs de vos audiences. Si la taille de votre audience est proche de zéro, le réseau peut signaler que la taille de l'audience est trop petite pour être diffusée. 
  - Pour résoudre ce problème, assurez-vous de considérer une stratégie de synchronisation de l'audience qui ajoute et supprime régulièrement des utilisateurs sans épuiser complètement la taille de l'audience.
- **L’audience n'existe pas**<br>
  - Cette erreur se produit car l'étape de synchronisation de l'audience utilise une audience qui n'existe pas. Elle peut également être déclenchée si vous n'avez pas l'autorisation nécessaire pour accéder à l'audience. 
  - Pour résoudre ce problème, ajoutez une audience active dans votre configuration de synchronisation d'audience ou créez une nouvelle audience.
- **Tentative d'accès au compte publicitaire**<br>
  - Cette erreur se produit si vous n'avez pas les autorisations pour le compte publicitaire et/ou l'audience que vous avez sélectionnée.
  - Pour résoudre ce problème, travaillez avec les administrateurs de votre compte publicitaire pour obtenir les accès et les autorisations appropriés. 
- **Paramètres non valides**<br>
  - Cette erreur se déclenchera si vous n'avez pas configuré une destination de synchronisation d'audience spécifique dans le canvas, y compris le compte publicitaire, l'audience ou les champs utilisateur à faire correspondre. 
  - Pour résoudre ce problème, complétez la configuration de chaque partenaire avant de lancer.
- **Conditions de service**<br>
  - Pour certaines destinations de synchronisation d'audience, comme Facebook, le réseau publicitaire exige d'accepter des conditions de service spécifiques pour utiliser la fonctionnalité de synchronisation d'audience. Cette erreur se déclenchera si vous n'avez pas accepté les termes appropriés. 
  - Pour résoudre ce problème, assurez-vous d'avoir accepté les conditions requises de chaque partenaire. Pour Facebook en particulier, consultez l’article [Résolution des problèmes de Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#troubleshooting). 
