---
nav_title: FAQ
article_title: "FAQ de synchronisation de l'audience"
alias: /partners/audience_sync_faq/
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

Si l'ancien utilisateur qui a connecté l'intégration ne fait plus partie de votre entreprise, vous devrez mettre à jour l'intégration avec le nouvel utilisateur en sélectionnant **Modifier le compte.** Ensuite, sélectionnez **Confirmer** et connectez-vous avec le nouvel utilisateur. Nous vous recommandons de changer d'utilisateur lorsque les synchronisations actives n'ont pas lieu, par exemple avant une entrée planifiée d'utilisateurs dans un Canvas, car la synchronisation pendant la transition de l'utilisateur précédent vers un nouvel utilisateur peut perturber les Canvas actifs. Nous vous recommandons de changer d'utilisateur lorsque les synchronisations actives n'ont pas lieu, par exemple avant une entrée planifiée d'utilisateurs dans un Canvas.

L'utilisateur qui se reconnecte doit avoir un accès en lecture et en écriture à toutes les audiences afin que les utilisateurs puissent être synchronisés avec les partenaires. Vérifiez que l'utilisateur qui reconnecte l'intégration a accès aux mêmes comptes publicitaires et aux mêmes audiences. Vous n'aurez pas besoin de modifier les étapes du canvas existantes. 

### Quelles sont les erreurs courantes qui peuvent survenir lors de la création et de la gestion de mes synchronisations d'audience ?

| Erreur | Raison | Solution |
| --- | --- | --- |
| Jeton non valide | Cela peut se produire si vous avez changé votre mot de passe pour vous connecter à un réseau publicitaire spécifique, ou si vos informations d'identification ont expiré. | Rendez-vous sur la page partenaire correspondante pour déconnecter et reconnecter votre compte. |
| Taille de l'audience trop petite | Cela peut se produire si vous avez créé une étape de synchronisation d'audience qui supprime des utilisateurs de vos audiences. Si la taille de votre audience est proche de zéro, le réseau peut signaler que la taille de l'audience est trop petite pour être diffusée. | Confirmez que vous envisagez une stratégie de synchronisation de l'audience qui ajoute et supprime régulièrement des utilisateurs de manière à ne pas épuiser la taille de l'audience. |
| L’audience n'existe pas | L'étape de synchronisation de l'audience utilise une audience qui n'existe pas. Elle peut également être déclenchée si vous n'avez pas l'autorisation nécessaire pour accéder à l'audience. | Ajoutez une audience active dans votre configuration Audience Sync ou créez une nouvelle audience. |
| Tentative d'accès au compte publicitaire | Cette erreur se produit si vous n'avez pas d'autorisation pour le compte publicitaire, une audience que vous avez sélectionnée, ou les deux. | Travaillez avec les administrateurs de votre compte publicitaire pour obtenir l'accès et les autorisations nécessaires. |
| Paramètres non valides | Cela peut se produire si vous n'avez pas configuré une destination Audience Sync spécifique dans Canvas, notamment les champs de compte publicitaire, d'audience ou d'utilisateur à faire correspondre. | Complétez la configuration de chaque partenaire avant de le lancer. |
| Conditions de service | Pour certaines destinations d'Audience Sync, comme Facebook, il est exigé par le réseau publicitaire d'accepter des conditions de service spécifiques pour utiliser la fonctionnalité Audience Sync. Cette erreur se déclenchera si vous n'avez pas accepté les termes appropriés. | Confirmez que vous avez accepté les conditions requises par chaque partenaire. Pour Facebook en particulier, consultez l’article [Résolution des problèmes de Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#troubleshooting). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

