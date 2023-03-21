---
nav_title: Wyng
article_title: Wyng
description: "Cet article de référence décrit le partenariat entre Braze et Wyng, une plateforme de données zero-party, qui facilite la collecte, l’utilisation et l’intégration des préférences et attributs des clients via des micro-expériences, des portails de préférences des clients et une plateforme API."
alias: /partners/wyng/
page_type: partner
search_tag: Partenaire
---

# Wyng

> [Wyng][0], une plateforme de données zero-party, facilite la collecte, l’utilisation et l’intégration des préférences et attributs des clients via des micro-expériences, des portails de préférences des clients et une plateforme API.

L’intégration entre Braze et Wyng vous permet de tirer parti des expériences de Wyng pour personnaliser vos campagnes et Canvas Braze. Wyng comprend également un portail de préférences des clients afin que les utilisateurs puissent contrôler les données et les préférences qu’ils partagent avec une marque.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Wyng | Un compte Wyng est nécessaire pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Cela peut être créé dans le **Tableau de bord de Braze > Developer Console (Console du développeur) > REST API Key (Clé API REST) > Create New Api Key (Créer une nouvelle clé API)** |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Connecter l’intégration Braze

Dans Wyng, accédez à [**Integrations (Intégrations)**][1] et sélectionnez l’onglet **Add (Ajouter)**. Ensuite, passez le curseur sur **Braze** et cliquez sur **Connect (Connexion)** pour l’intégration.

![Mosaïque de partenaires Braze dans la plateforme Wyng.][2]{: style="max-width:80%;"}

### Étape 2 : Configurer le connecteur Braze

1. Dans la fenêtre de configuration qui s’ouvre, fournissez votre clé d’API REST Braze.
![Une image de l’invite de saisie des identifiants.][4]{: style="max-width:80%;"}<br><br>
2. Ensuite, utilisez la liste déroulante pour sélectionner la campagne Wyng que vous souhaitez partager avec Braze.![Une image du connecteur Braze vous invitant à sélectionner une campagne Wyng existante que vous souhaitez partager avec Braze.][5]{: style="max-width:80%;"}<br><br>
3. Ensuite, vous devez configurer des abonnements, des objets d’attribut et d’événement et des événements personnalisés.<br><br>
- **Configuration des abonnements (obligatoire)**<br>
Pour abonner des utilisateurs à des groupes d’abonnement, cliquez sur **Add Subscription (Ajouter un abonnement)** et ajoutez le nom et l’ID de votre groupe d’abonnement. Pour ajouter plusieurs noms et ID de groupe, cliquez à nouveau sur le bouton **Add Subscription (Ajouter un abonnement)**.<br>![Une image vous invitant à saisir un nom et un ID de groupe d’abonnement.][8]{: style="max-width:80%;"}<br><br>
- **Configuration du suivi de l’utilisateur**<br>
Cliquez sur **Add custom property (Ajouter une propriété personnalisée)** pour ajouter des paires d’objets Attribut et Événement à envoyer à l’endpoint users/track. Utilisez ceci pour ajouter des valeurs d’attribut codées en dur pour chaque transaction de données envoyée pour l’intégration. Pour ajouter plusieurs propriétés, cliquez à nouveau sur le bouton **Add custom properties (Ajouter une propriété personnalisée)**.<br>![Une image vous invitant à ajouter les propriétés personnalisées de l’attribut.][9]{: style="max-width:80%;"}<br><br>
- **Envoyer un événement personnalisé**<br>
Si souhaité, vous pouvez activer **Sending custom event (Envoi d’un événement personnalisé)**. Si cette option est activée, vous devez inclure le nom de l’événement et l’ID de l’application correspondante.<br>![Une image vous invitant à envoyer des événements personnalisés, si nécessaire.][10]{: style="max-width:80%;"}<br><br>
4. Enfin, vous devez mapper les champs Wyng sur les champs de l’API Braze en fonction de votre cas d’utilisation. Cliquez sur **Select a field (Sélectionner un champ)** pour choisir les champs à mapper, puis sur **Save (Enregistrer)** pour enregistrer votre intégration. Une fois enregistrés, ces champs mappés se trouvent sous **Integrations (Intégrations) > Manage (Gérer)**.
![Un exemple des différents champs Wyng que vous pouvez mapper à certains champs Braze.][11]{: style="max-width:80%;"}
![Une liste des champs de synchronisation disponibles.][12]{: style="max-width:80%;margin-top:2px"}

### Étape 3 : Tester votre intégration

Dans Wyng, testez le formulaire dans votre campagne Wyng. Vous pouvez également le soumettre dans la campagne de test si vous ne souhaitez pas ajouter un enregistrement à la campagne de production principale. Vous devriez afficher une transaction réussie dans le tableau de bord **Integration (Intégration)**.

## Comment utiliser cette intégration

Une fois le connecteur de données en place, tous les champs créés dans Wyng et ajoutés à Braze peuvent être utilisés comme n’importe quel autre champ de données pour déclencher des campagnes, segmenter des audiences ou alimenter du contenu personnalisé.

Les applications sont vastes, et les questions spécifiques peuvent être adressées à [contact@wyng.com][13] ou à votre gestionnaire de compte spécifique.

## Résolution des problèmes

### Échec de l’envoi

En cas d’échec de l’envoi des données à Braze, cliquez sur le lien **View Log (Afficher le journal)** pour examiner l’échec de l’envoi et le message d’erreur associé.

![Le lien « View Log » (Afficher le journal) situé sous l’en-tête des actions.][14]{: style="max-width:80%;"}

La page de journal indique l’envoi qui a échoué, le nombre de tentatives, les données de l’envoi, l’erreur et un lien permettant de relancer l’envoi.

![Un exemple de l’échec d’un envoi.][15]{: style="max-width:80%;"}

La section **View Error (Afficher l’erreur)** affiche le code d’erreur et quelques informations supplémentaires sur la cause de l’erreur. Vous pouvez ensuite vous reporter au code d’erreur avec Braze pour en déterminer la cause.

![Un exemple de journal d’erreurs affiché dans la plateforme Wyng.][16]{: style="max-width:80%;"}

Si vous avez des questions supplémentaires, contactez l’assistance Wyng ([support@wyng.com][13]) pour obtenir de l’aide.

[0]: https://wyng.com/
[1]: https://wyng.com/dashboard/integrations/
[2]: {% image_buster /assets/img/wyng/2.png %}
[3]: {% image_buster /assets/img/wyng/3.png %}
[4]: {% image_buster /assets/img/wyng/4.png %}
[5]: {% image_buster /assets/img/wyng/5.png %}
[6]: {% image_buster /assets/img/wyng/6.png %}
[7]: {{site.baseurl}}/api/basics/
[8]: {% image_buster /assets/img/wyng/8.png %}
[9]: {% image_buster /assets/img/wyng/9.png %}
[10]: {% image_buster /assets/img/wyng/10.png %}
[11]: {% image_buster /assets/img/wyng/11.png %}
[12]: {% image_buster /assets/img/wyng/12.png %}
[13]: mailto:contact@wyng.com
[14]: {% image_buster /assets/img/wyng/14.png %}
[15]: {% image_buster /assets/img/wyng/15.jpg %}
[16]: {% image_buster /assets/img/wyng/16.jpg %}