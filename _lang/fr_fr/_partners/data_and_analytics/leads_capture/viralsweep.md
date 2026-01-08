---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Cet article de référence présente le partenariat entre Braze et ViralSweep, un service logiciel qui permet aux marques de créer, d'exécuter et de gérer des promotions de marketing numérique telles que des sweepstakes, des concours, des gains instantanés, des listes d'attente, des promotions par recommandation, etc."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com) est un service logiciel qui permet aux marques de créer, d'exécuter et de gérer des promotions de marketing numérique telles que des sweepstakes, des concours, des gains instantanés, des listes d'attente, des recommandations, etc. 

_Cette intégration est maintenue par ViralSweep._

## À propos de l'intégration

L'intégration de Braze et de ViralSweep vous permet d'organiser des loteries et des concours sur la plateforme ViralSweep (en enrichissant vos listes d'e-mails et de SMS), puis d'envoyer les informations de participation aux loteries ou aux concours à Braze afin de les utiliser dans des campagnes ou des canvas. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte ViralSweep | Un compte ViralSweep utilisant le plan d'affaires est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec toutes les données de l'utilisateur et les autorisations d'e-mail. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
|Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Se connecter à Braze dans ViralSweep

Dans ViralSweep, naviguez vers **Intégrations > Email & SMS > Ajouter un service** et sélectionnez **Braze**. 

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### Étape 2 : Ajouter les identifiants Braze

Dans la fenêtre de configuration des intégrations, indiquez votre clé API REST Braze et votre endpoint REST. Assurez-vous que l'endpoint que vous fournissez n'inclut pas `https://`, par exemple, `dashboard-03.braze.com`. 

![Page d'intégration du service ViralSweep demandant à l'utilisateur la clé API de Braze et l'URL du tableau de bord de Braze.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

Cliquez sur **Connecter**.

### Étape 3 : Ajouter les identifiants Braze
Vous êtes connecté ! La promotion est désormais connectée à Braze, et toutes les participations collectées par ViralSweep seront automatiquement envoyées dans Braze.

## Questions fréquemment posées

### Quels champs ViralSweep transmet-il à Braze ?
- Prénom
- Nom de famille
- Adresse e-mail
- Adresse
- Adresse 2
- Ville
- État
- Code postal
- Pays
- Date de naissance
- Téléphone
- ID de la promotion
- Lien de recommandation
- Nom de la campagne de suivi

### ViralSweep met-il à jour les abonnés ?
Oui. Si vous organisez une promotion et que ViralSweep transmet une personne à Braze, puis que vous organisez une autre promotion à l'avenir et que la même personne participe, les informations de cette personne seront automatiquement mises à jour dans Braze (si de nouvelles informations sont fournies). Principalement, l'URL de recommandation sera mise à jour avec l'URL la plus récente pour chaque promotion à laquelle ils participent, et le champ ID de la promotion contiendra l'ID de toutes les promotions auxquelles ils ont participé.

## Résolution des problèmes

Si vous vous êtes connecté à Braze et que les données ne sont pas ajoutées à votre compte, c'est peut-être parce que :

- **L'e-mail existe déjà dans Braze**<br>
L'adresse e-mail saisie dans le cadre de la promotion peut déjà se trouver dans votre compte Braze, elle ne sera donc pas ajoutée à nouveau ; elle ne sera mise à jour que si de nouvelles informations sont fournies pour ce contact.<br><br>
- **E-mail déjà entré dans ViralSweep**<br>
L'adresse e-mail saisie dans le cadre de la promotion l'a déjà été précédemment, elle n'est donc pas transmise à nouveau à Braze. Cela peut se produire si vous configurez votre intégration à Braze alors que vous avez déjà participé à la promotion.


