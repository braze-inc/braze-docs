---
nav_title: Wyng
article_title: Wyng
description: "Cet article de référence présente le partenariat entre Braze et Wyng, une plateforme de données zero-party, qui facilite la collecte, l'utilisation et l'intégration des préférences et attributs des clients via des micro-expériences, des portails de préférences clients et une plateforme API."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng][0] permet de créer facilement des expériences numériques interactives (c'est-à-dire des quiz, des centres de préférences, des promotions) qui engagent les consommateurs aux bons moments, collectent des préférences et d'autres données zero-party, et personnalisent en temps réel.

_Cette intégration est maintenue par Wyng._

## À propos de l'intégration

L'intégration entre Braze et Wyng vous permet d'exploiter les données zero-party issues des expériences Wyng pour personnaliser les interactions dans les campagnes et canvas Braze. Wyng peut également alimenter un centre de préférences, afin que les consommateurs puissent contrôler les données et les préférences (y compris les préférences de communication) qu'ils partagent avec votre marque.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Wyng | Un compte Wyng est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Connectez l'intégration de Braze

Dans Wyng, allez dans [**Intégrations**][1] et sélectionnez l'onglet **Ajouter.**  Ensuite, survolez **Braze** et cliquez sur **Connecter** pour l'intégration.

![La tuile partenaire de Braze dans la plateforme Wyng.][2]{: style="max-width:80%;"}

### Étape 2 : Configurer le connecteur Braze

1. Dans la fenêtre de configuration qui s'ouvre, indiquez votre clé API REST Braze.
![Une image de ce à quoi ressemble la requête d'informations d'identification.][4]{: style="max-width:80%;"}<br><br>
2. Ensuite, utilisez le menu déroulant pour sélectionner la campagne Wyng que vous souhaitez partager avec Braze.![Image du connecteur Braze vous invitant à sélectionner une campagne Wyng existante que vous souhaitez partager avec Braze.][5]{: style="max-width:80%;"}<br><br>
3. Ensuite, vous devez configurer les abonnements, les objets d’attributs et d’événements, ainsi que les événements personnalisés.<br><br>
- **Configuration des abonnements (obligatoire)**<br>
Pour abonner des utilisateurs à des subscription groups, cliquez sur **Ajouter un abonnement** et ajoutez le nom et l'ID de votre subscription group. Pour ajouter plusieurs noms et ID de groupes, cliquez à nouveau sur le bouton **Ajouter un abonnement**.<br>![Une image vous invitant à indiquer le nom et l'ID d'un groupe d'abonnement.][8]{: style="max-width:80%;"}<br><br>
- **Configuration du suivi des utilisateurs**<br>
Cliquez sur **Ajouter une propriété personnalisée** pour ajouter des paires d'attributs et d'objets personnalisés à envoyer à l'endpoint `/users/track`. Utilisez cette option pour ajouter des valeurs d'attribut codées en dur pour chaque transaction de données envoyée pour l'intégration. Pour ajouter plusieurs propriétés, cliquez à nouveau sur le bouton **Ajouter une propriété personnalisée**.<br>![Message vous invitant à ajouter des attributs personnalisés.][9]{: style="max-width:80%;"}<br><br>
- **Envoyer un événement personnalisé**<br>
Vous pouvez activer l'**envoi d'un événement personnalisé**. Si cette option est activée, vous devez inclure le nom de l'événement et l'ID de l'application correspondante.<br>![Une image vous invitant à envoyer des événements personnalisés, le cas échéant.][10]{: style="max-width:80%;"}<br><br>
4. Enfin, vous devez mapper les champs Wyng aux champs de l'API Braze en fonction de votre cas d'utilisation. Cliquez sur **Sélectionner un champ** pour choisir les champs à mapper, puis sur **Enregistrer votre** intégration. Une fois enregistrés, ces champs mappés se trouvent sous **Intégrations > Gérer.**
![Un exemple des différents champs Wyng que vous pouvez mapper à certains champs Braze.][11]{: style="max-width:80%;"}
![Liste des champs de synchronisation disponibles.][12]{: style="max-width:80%;margin-top:2px"}

### Étape 3 : Testez votre intégration

Dans Wyng, testez la soumission du formulaire dans votre campagne Wyng. Vous pouvez également le soumettre dans la campagne de prévisualisation si vous ne souhaitez pas ajouter un enregistrement à la campagne de production principale. Vous devriez voir une transaction réussie dans le tableau de bord de l'**intégration**.

## Grâce à cette intégration

Une fois le connecteur de données en place, tous les champs créés dans Wyng et ajoutés à Braze peuvent être utilisés comme n'importe quel autre champ de données pour déclencher des campagnes, segmenter des audiences ou alimenter des contenus personnalisés.

Les applications sont vastes et les questions spécifiques peuvent être adressées à [contact@wyng.com][13] ou à votre gestionnaire de compte.

## Résolution des problèmes

### Échec de la soumission

En cas d'échec de l'envoi des données à Braze, cliquez sur le lien **Afficher le journal** pour consulter l'échec de l'envoi et le message d'erreur associé.

![Le lien "Voir le journal" se trouve sous l'en-tête des actions.][14]{: style="max-width:80%;"}

La page du journal indique l'échec de la soumission, le nombre de tentatives, les données de la soumission, l'erreur et un lien pour envoyer à nouveau la soumission.

![Exemple d'un échec de soumission.][15]{: style="max-width:80%;"}

La section **Voir l'erreur** affiche le code d'erreur et quelques informations supplémentaires sur la cause de l'erreur. Vous pouvez ensuite comparer le code d'erreur aux données Braze pour en déterminer la cause.

![Un exemple de journal d'erreurs affiché dans la plateforme Wyng.][16]{: style="max-width:80%;"}

Si vous avez d'autres questions, contactez le service d'assistance de Wyng ([support@wyng.com][13]]) pour obtenir de l'aide.


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
[13]: mailto :contact@wyng.com
[14]: {% image_buster /assets/img/wyng/14.png %}
[15]: {% image_buster /assets/img/wyng/15.jpg %}
[16]: {% image_buster /assets/img/wyng/16.jpg %}