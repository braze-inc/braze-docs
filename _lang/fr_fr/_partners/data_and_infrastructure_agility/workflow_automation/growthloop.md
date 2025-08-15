---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "Cet article de référence présente le partenariat entre Braze et GrowthLoop, une plateforme qui vous permet de segmenter les données clients directement à partir des entrepôts de données et de les envoyer à Braze."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/) aide les équipes marketing à activer les données des clients depuis l'entrepôt de données dans le cloud vers Braze et d'autres canaux. Automatisez, développez et mesurez des programmes de marketing à partir de votre entrepôt de données dans le cloud, en conservant les données dans un emplacement centralisé.

_Cette intégration est maintenue par GrowthLoop._

## À propos de l'intégration

L'intégration de Braze et GrowthLoop permet de segmenter les données clients directement depuis l'entrepôt de données et de les envoyer à Braze, garantissant ainsi que les utilisateurs peuvent optimiser les fonctionnalités avancées de Braze en parallèle avec leur source unique de vérité. Rationalisez les efforts de marketing pour la segmentation et l'activation des clients, en réduisant le temps nécessaire pour segmenter, lancer, tester et mesurer les résultats des campagnes ciblées envoyées à Braze.

## Conditions préalables 

| Condition | Description |
| ----------- | ----------- |
| GrowthLoop compte de croissance ou d'entreprise | Un compte GrowthLoop est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec toutes les autorisations.<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance][2].|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Cas d'utilisation

Envoyez des listes de clients de votre entrepôt de données vers Braze, en ciblant les campagnes d'e-mail et de notification push en un seul clic, et gardez-les toujours synchronisées.

- E-mails basés sur l'activation de l'inscription - envoyez des e-mails pour aider les utilisateurs qui tombent dans votre flux d'inscription et les convertir en utilisateurs actifs.
- E-mails basés sur n'importe quel comportement de l'utilisateur - envoyez des e-mails basés sur le comportement de l'utilisateur, par exemple "Ajouter au panier".
- Emails aux clients désabonnés - réengagez les clients désabonnés par e-mail en leur proposant une offre.

## Intégration

### Configurer la connexion Braze dans GrowthLoop

Lorsque vous vous connectez à la plateforme de segmentation dans GrowthLoop, accédez à l'onglet **Destinations** dans la barre latérale gauche et cliquez sur **Nouvelle destination** dans le coin supérieur droit.

Recherchez Braze en faisant défiler la page, puis cliquez sur **Ajouter Braze**.

Une fenêtre contextuelle s'affiche pour configurer la connexion à la destination.

- **Nom de la destination** : Nom qui sera attribué à la destination dans l'application.
- **Fréquence de synchronisation**: Sélectionnez Quotidien ou Horaire pour la fréquence à laquelle GrowthLoop exporte les audiences vers Braze.
- **Clé API** : Clé API créée dans les exigences, avec les autorisations nécessaires.
- **URL DE L'API** : URL telle que définie dans les exigences

Cliquez sur **Créer**, et vous pourrez exporter votre première audience vers Braze ! Pour créer une audience dans GrowthLoop, consultez la page [Créer une audience](https://www.growthloop.com/help-center-articles/create-an-audience).

### Exportation de postes

Une fois votre audience exportée, toutes les 15 minutes, GrowthLoop génère une version actualisée de vos listes de clients et l'envoie à Braze.

Simultanément, GrowthLoop supprime de votre audience les utilisateurs qui ne sont plus qualifiés et ajoute à votre audience les utilisateurs nouvellement qualifiés. 

Braze associe les utilisateurs et crée un indicateur afin de signaler qu'ils font partie d'une audience GrowthLoop.

Lorsque vous créez une campagne dans Braze, vous pouvez sélectionner des clients dans cette audience GrowthLoop. 

## Résolution des problèmes

Contactez l'équipe de GrowthLoop à l'adresse solutions@growthloop.com pour obtenir des informations supplémentaires ou de l’aide.


[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
