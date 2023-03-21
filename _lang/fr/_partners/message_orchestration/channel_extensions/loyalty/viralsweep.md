---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Cet article de référence présente le partenariat entre Braze et ViralSweep, un service logiciel qui permet aux marques de construire, d’exécuter et de gérer des promotions marketing numériques telles que des loteries, des concours, des gains instantanés, des listes d’attente, des promotions de recommandation, etc. "
page_type: partner
search_tag: Partenaire

---

# ViralSweep

> [ViralSweep](https://viralsweep.com) est un service logiciel qui permet aux marques de construire, d’exécuter et de gérer des promotions marketing numériques telles que des loteries, des concours, des gains instantanés, des listes d’attente, des promotions de recommandation, etc. 

L’intégration entre Braze et ViralSweep vous permet de lancer des loteries et des concours sur la plateforme ViralSweep (en développant vos listes d’e-mails et de SMS), puis d’envoyer des informations de participation aux loteries/concours vers Braze pour les utiliser dans des campagnes ou des Canvas. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte ViralSweep | Un compte ViralSweep utilisant le forfait professionnel est requis pour tirer parti de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST de Braze avec toutes les autorisations liées aux données de l’utilisateur et aux e-mails. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
|Endpoint REST de Braze | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Se connecter à Braze depuis ViralSweep

Dans ViralSweep, accédez à **Integrations (Intégrations) > Email & SMS (E-mail et SMS) > Add Service (Ajouter un service)** et sélectionnez **Braze**. 

![][1]

### Étape 2 : Ajouter des identifiants Braze

Dans la fenêtre de configuration des intégrations, fournissez votre clé d’API REST Braze et votre endpoint REST. Assurez-vous que l’endpoint que vous fournissez ne comprend pas `https://`, par exemple, `dashboard-03.braze.com`. 

![Page d’intégration du service ViralSweep demandant à l’utilisateur la clé d’API Braze et l’URL du Tableau de bord de Braze.][2]{: style="max-width:40%;"}

Cliquez sur **Connect (Connexion)**.

### Étape 3 : Ajouter des identifiants Braze
Vous êtes connecté ! La promotion est maintenant connectée à Braze et toutes les entrées collectées par ViralSweep seront envoyées automatiquement dans Braze.

## Foire aux questions

### Quels sont les champs ViralSweep transmis à Braze ?
- Prénom
- Nom
- Adresse e-mail
- Adresse
- Adresse 2
- Ville
- État
- Code postal
- Pays
- Date de naissance
- Téléphone
- ID de promotion
- Lien de recommandation
- Nom de la campagne de suivi

### Est-ce que ViralSweep met à jour les utilisateurs abonnés ?
Oui. Si vous organisez une promotion et que ViralSweep transmet une personne à Braze, puis que vous organisez une autre promotion plus tard, et que la même personne y participe, ViralSweep mettra automatiquement à jour ses informations dans Braze (si de nouvelles informations sont fournies). L’URL de recommandation sera également mise à jour avec l’URL la plus récente pour chaque promotion à laquelle ils participent.

## Résolution des problèmes

Si vous avez connecté Braze et que les données ne sont pas ajoutées à votre compte, cela peut être dû à :

- **L’e-mail existe déjà dans Braze**<br>
L’adresse e-mail saisie dans le cadre de la promotion peut déjà se trouver dans votre compte Braze, elle ne sera donc pas ajoutée à nouveau ; elle ne sera mise à jour que si de nouvelles informations sont fournies pour ce contact.<br><br>
- **E-mail déjà entré dans ViralSweep**<br>
L’adresse e-mail saisie dans la promotion a déjà été saisie précédemment, donc elle n’est pas transmise à Braze. Cela peut arriver si vous configurez votre intégration Braze après avoir déjà saisi la promotion.

[1]: {% image_buster /assets/img/viralsweep/connect.gif %}
[2]: {% image_buster /assets/img/viralsweep/connect2.png %}