---
nav_title: SmarterSends
article_title: SmarterSends
description: "Cet article de référence présente le partenariat entre Braze et SmarterSends, une interface conviviale conçue pour les non-marketeurs afin de créer, planifier et déployer des campagnes d'e-mails conformes à la marque."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends](https://smartersends.com) favorise la personnalisation grâce à des campagnes marketing que les entreprises peuvent créer, planifier et déployer pour faire respecter la marque et la conformité légale en contrôlant le contenu et les données utilisées. 

_Cette intégration est maintenue par SmarterSends._

## À propos de l'intégration

Le partenariat entre Braze et SmarterSends vous permet de combiner la puissance de Braze avec le contenu hyperlocalisé détenu par vos utilisateurs distribués pour renforcer vos campagnes marketing.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte SmarterSends | Un [compte SmarterSends](https://smartersends.com) est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec ces autorisations : {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. Pour plus de sécurité, autorisez la liste de l'adresse IP de SmarterSends (disponible dans votre instance). |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| ID de la campagne de l'API Braze | L'[ID de campagne de l'API de Braze]({{site.baseurl}}/api/api_campaigns/) est l'identifiant unique de toutes les campagnes envoyées par l'intermédiaire de SmarterSends. Celle-ci peut être créée dans le tableau de bord de Braze sous **Messagerie** > **Campagnes**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Grâce à l'intégration de Braze et de SmarterSends, vous pouvez tirer parti du marketing distribué en créant et en exécutant des campagnes marketing sur plusieurs canaux et emplacements/localisations. Ces avantages sont les suivants

1. **Augmentation de la portée :** utilisation de plusieurs canaux et lieux pour atteindre une audience plus large et cibler les clients dans différentes zones afin d'accroître l'exposition de la marque.
2. **Envoi de messages ciblés :** Adapter l'envoi de messages à travers les canaux/localisations afin de trouver un écho auprès des audiences locales pour une communication et un engagement plus efficaces avec les clients. 
3. **Amélioration de la cohérence de la marque :** Aligner les messages et l'image de votre marque sur tous les canaux/localisations, ce qui est important pour créer une marque forte et reconnaissable.
4. **Meilleures informations :** Collecte de données provenant de différents canaux et emplacements, fournissant des informations précieuses sur le comportement et les préférences des clients, qui peuvent être utilisées pour affiner les stratégies et tactiques de marketing à la fois au niveau local et mondial.
5. **Efficacité accrue :** Tirer parti des atouts des différents canaux et emplacements, ce qui peut se traduire par une utilisation plus efficace des ressources tout en permettant d'atteindre les objectifs marketing souhaités. 

## Intégration

### Étape 1 : Créer une clé API REST

1. Dans Braze, allez dans **Paramètres** > **Clés API** et cliquez sur **Créer une nouvelle clé API.**
2. Saisissez un nom pour la clé API.
3. Sélectionnez les autorisations suivantes pour cette clé afin de permettre à SmarterSends d'interagir avec votre espace de travail Braze.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. Ajoutez l'adresse IP de SmarterSends à la section **Whislist IPs.** 
5. Cliquez sur **Enregistrer la clé API**.
6. Copiez et collez la clé API avec les autorisations appropriées dans les paramètres du **fournisseur de services d'e-mailing de Braze** dans SmarterSends.

### Étape 2 : Créer ou copier un ID d'application

1. Dans votre espace de travail Braze, accédez à **Paramètres** > **Paramètres de l'application**. 
2. Créez une nouvelle application ou utilisez l'ID d'une application existante dans votre espace de travail. Notez que l'ID de l'application est indiqué comme étant la **clé API**. 
3. Copiez et collez cet ID dans le champ de l'**ID de l'application** dans SmarterSends.

### Étape 3 : Créer une campagne API

Une campagne API permet de suivre les indicateurs de tous les courriers SmarterSends dans Braze et permet à SmarterSends de déclencher ces campagnes basées sur l'API.

1. Dans Braze, [créez une campagne API]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Cliquez sur **e-mail** sous **Sélectionner un canal de messages** pour ajouter un canal d'envoi de messages et commencer à suivre les indicateurs.
3. Ensuite, copiez et collez l'ID de la campagne depuis Braze dans le champ **ID de la campagne** dans SmarterSends. 
4. Copiez et collez l'ID de la variante du message provenant de Braze dans le champ **ID de la variante du message** dans SmarterSends. Il s'agit de l'ID message par défaut utilisé si vous décidez de ne pas créer d'ID message pour chaque groupe dans SmarterSends.
5. Pour chaque groupe que vous créez dans SmarterSends, ajoutez une variante de message à votre campagne API dans Braze. Copiez ensuite l'ID de la variante de message dans l'ID de la variante de message du groupe dans SmarterSends.

{% alert tip %}
Créez un ID de variante de message pour chaque groupe que vous créez dans SmarterSends afin d'afficher séparément les indicateurs des envois de chaque groupe dans votre espace de travail Braze. Cela peut être utile pour identifier les tendances entre les groupes lorsque vous créez des rapports dans Braze.
{% endalert %}

## Personnalisation

Chaque instance de SmarterSends est entièrement personnalisée avec les couleurs du logo de votre marque et votre nom de domaine personnalisé, créant ainsi un environnement familier. En outre, pour une personnalisation plus poussée, vous pouvez définir les attributs et les attributs personnalisés pour cibler les utilisateurs dans les campagnes en fonction des segments au sein de votre espace de travail Braze.


