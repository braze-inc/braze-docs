---
nav_title: Synchronisation de l’audience avec Google
article_title: Synchronisation de l’audience Canvas avec Google
alias: /google_audience_sync/
description: "Cet article de référence couvre la façon d’utiliser la synchronisation d’audience de Braze vers Google pour fournir des publicités basées sur des déclencheurs comportementaux, des segmentations, etc."
Outil :
  - Canvas
---

# Synchronisation de l’audience avec Google 

L’intégration de l’audience Braze à Google permet aux marques d’étendre la portée de leurs parcours client cross-canal sur Google Search, Google Shopping, Gmail, YouTube et Google Display. En utilisant vos données client propriétaires, vous pouvez livrer des publicités en toute sécurité en fonction de déclencheurs comportementaux dynamiques, de segmentations et bien plus encore. Les critères que vous utilisez généralement pour déclencher un message (par ex., notification push, e-mail, SMS, etc.) dans le cadre d’un Canvas Braze peuvent être utilisés pour envoyer une publicité à cet utilisateur via la fonction [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) de Google.

**Les cas d’utilisation courants pour synchroniser les audiences personnalisées comprennent** :
- Cibler des utilisateurs à forte valeur à travers plusieurs canaux pour stimuler les achats ou l’engagement.
- Recibler des utilisateurs qui sont moins réactifs aux autres canaux marketing.
- Supprimer des audiences pour empêcher les utilisateurs de recevoir des publicités lorsqu’ils sont déjà de fidèles clients de votre marque.
- Créer des audiences similaires pour acquérir de nouveaux utilisateurs plus efficacement.

{% alert note %}
Cette fonctionnalité permet aux marques de contrôler les données first-party partagées avec Google. Chez Braze, les intégrations avec lesquelles vous pouvez et ne pouvez pas partager avec vos données first-party sont considérées avec le plus grand sérieux. Pour en savoir plus sur la politique de confidentialité des données de Braze, cliquez [ici](https://www.braze.com/privacy).
{% endalert %}

## Intégration

### Exigences d’intégration

Vous devrez vous assurer que les éléments suivants ont été créés et terminés avant de configurer votre composant d’audience Google dans Canvas.

| Condition | Origine | Description |
| ----------- | ------ | ----------- |
| Compte Google Ads | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Un compte Google Ads actif pour votre marque.<br><br>Si vous souhaitez partager une audience entre plusieurs comptes gérés, vous pouvez télécharger vos audiences dans votre [compte gestionnaire](https://support.google.com/google-ads/answer/6139186). |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Google Customer Match n’est pas disponible pour tous les annonceurs.<br><br>**Pour utiliser Google Customer Match, votre compte doit avoir :**<br>• Un bon historique de conformité aux politiques<br>• Un bon historique de paiement<br>• Historique d'au moins 90 jours dans Google Ads<br>• Plus de 50 000 USD de dépenses totales à vie. Pour les annonceurs dont les comptes sont gérés dans d’autres devises que le dollar américain (USD), le montant dépensé sera converti en USD en utilisant le taux de conversion mensuel moyen pour cette devise.<br><br>Si votre compte ne répond pas à ces critères, cela signifie qu’il n’est pas éligible à Customer Match à l’heure actuelle.<br><br>Parlez-en à votre conseiller Google Ads pour obtenir plus d’informations sur la disponibilité de Customer Match pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Processus de mise en œuvre
### Étape 1 : Connecter votre compte Google

Pour commencer, accédez à l’onglet **Google Ads** à la page **Technology Partners (partenaires technologiques)** et sélectionnez **Connect Google Ads (Connecter Google Ads)**. Un modal vous invitera ensuite à sélectionner l’adresse e-mail associée à votre compte Google Ads, puis à autoriser votre compte Google Ads à accéder à Braze.

Après avoir connecté votre compte Google Ads, vous serez redirigé vers votre page Partenaire Google Ads. Vous serez ensuite invité à sélectionner les comptes publicitaires que vous souhaitez consulter dans le groupe d’apps de Braze.

![]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

{% alert important %}
Si vous prévoyez d’exporter des IDFA iOS ou des ID Google Advertising dans votre synchronisation d’audience, Google vous demandera d’ajouter votre ID d’application iOS et votre identifiant d’application Android dans vos requêtes. Dans le module Synchronisation d’audience Google, sélectionnez **Add Mobile Advertising IDs**, saisissez votre ID d’application iOS et votre identifiant d’application Android (nom du package d’applications), puis enregistrez-les.
<br><br>
![La page des technologies Google Ads mise à jour, montrant les comptes publicitaires connectés et vous permettant de resynchroniser des comptes et d’ajouter des ID de publicité sur les appareils mobiles.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
{% endalert %}

### Étape 2 : Ajouter une étape d’audience Google dans Canvas Flow

Ajoutez un composant dans votre Canvas et sélectionnez **Google Audience (Audience Google)**.

![Le flux de travail des étapes précédentes permettant d’ajouter une audience Google dans Canvas Flow.][6]

### Étape 3 : Configurer une synchronisation

Cliquez sur le bouton **Custom Audience (Audience personnalisée)** pour ouvrir l’éditeur de composant.

Sélectionnez le compte publicitaire Google souhaité. Sous le menu déroulant **Choose a New or Existing Audience (Choisir une nouvelle audience ou une audience existante)**, saisissez le nom d’une nouvelle audience ou d’une audience existante. 

{% tabs %}
{% tab Create a New Audience %}
**Créer une nouvelle audience**<br>
Saisissez un nom pour la nouvelle audience personnalisée, sélectionnez **Add Users to Audience**, puis sélectionnez les données propriétaires des champs d’utilisateur à envoyer à votre audience. Vous pouvez choisir : 
- **Coordonnées du client**, qui contiendra l’adresse e-mail et/ou les numéros de téléphone de vos utilisateurs s’ils existent dans Braze.
- **ID de l’annonceur mobile**, puis sélectionner iOS IDFA ou Android GAID.   

Ensuite, enregistrez votre audience en cliquant sur le bouton **Créer une audience** en bas de l’éditeur d’étapes.

![Vue agrandie du composant Audience Canvas personnalisée. Ici, le compte publicitaire souhaité est sélectionné, une nouvelle audience est créée et la case « Coordonnées du client » est cochée.]({% image_buster /assets/img/google_sync/google_sync7.png %})

Les utilisateurs seront avertis en haut de l’éditeur d’étapes si l’audience a été créée avec succès ou si des erreurs sont survenues au cours du processus. Les utilisateurs peuvent revenir à cette audience pour supprimer des utilisateurs plus tard dans le parcours Canvas, car l’audience a été créée en mode ébauche. 

![Une alerte qui apparaît lorsqu’une nouvelle audience a été créée dans le composant Canvas.]({% image_buster /assets/img/google_sync/google_sync9.png %})

Lorsque vous lancez un Canvas avec une nouvelle audience, Braze crée la nouvelle audience personnalisée lors du lancement de Canvas et synchronise ensuite les utilisateurs en temps quasi réel lorsqu’ils entrent dans le composant Google Audience. 

{% alert important %}
Compte tenu des exigences de Google Customer Match, vous ne pouvez pas avoir de coordonnées client et d’ID d’annonceurs mobiles dans les mêmes listes client. Google Customer Match utilisera ensuite ces informations pour déterminer quels utilisateurs peuvent être ciblés dans Google Search, Google Display, YouTube et Gmail. Consultez la [documentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507) de Google Customer Match pour plus d’informations sur les exigences applicables.
{% endalert %}
{% endtab %}
{% tab Sync with an Existing Audience %}
**Synchroniser une audience existante**<br>
Braze permet également d’ajouter ou de supprimer des utilisateurs dans des listes de clients Google pour s’assurer que ces audiences sont à jour. Pour synchroniser une audience existante, sélectionnez une audience personnalisée à synchroniser puis choisissez **Add to the Audience** ou **Remove from the Audience**. Ensuite, Braze ajoutera ou supprimera des utilisateurs en temps quasi réel lorsqu’ils passeront à l’étape d’audience Google. 

Après avoir configuré votre étape d’audience Google, sélectionnez **Terminé**. Votre étape d’audience Google inclura des informations sur la nouvelle audience.

![Vue agrandie du composant Audience Canvas personnalisée. Ici, le compte publicitaire souhaité et l’audience existante sont sélectionnés, ainsi que la case d’option « Add user to Audience (Ajouter l’utilisateur à l’audience) ».]({% image_buster /assets/img/google_sync/google_sync8.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Lancer Canvas

Terminez les étapes restantes de votre parcours utilisateur dans Canvas, puis lancez-le ! Si vous avez choisi de créer une nouvelle audience, Braze créera d’abord l’audience dans Google, puis ajoutera des utilisateurs à mesure qu’ils atteindront cette étape dans votre Canvas. Si vous avez choisi d’ajouter ou de supprimer des utilisateurs d’une audience existante, Braze ajoutera ou supprimera des utilisateurs lorsqu’ils atteindront cette étape dans leur parcours utilisateur.

Les utilisateurs passeront ensuite au composant suivant de Canvas, le cas échéant, ou quitteront Canvas s’il s’agit de la dernière étape du parcours utilisateur. 

## Considérations relatives à la synchronisation des utilisateurs et aux limites de débit

À mesure que les utilisateurs accèdent au composant de synchronisation de l’audience, Braze synchronisera ces utilisateurs en temps quasi réel tout en respectant les limites de débit de l’API de Google Ads. Ce que cela signifie concrètement que Braze essaiera de classer et de traiter autant d’utilisateurs que possible toutes les cinq secondes avant d’envoyer ces utilisateurs vers Google. 

Si un client se rapproche des limites de débit de l’API Google Ads, Google enverra des recommandations concernant les nouvelles tentatives à Braze. Si un client Braze atteint ses limites de débit, le Canvas Braze tentera à nouveau d’effectuer la synchronisation pendant un délai de &#126;13 heures maximum. Si la synchronisation n’est pas possible, ces utilisateurs sont répertoriés dans l’indicateur Utilisateurs en erreur.

## Comprendre les analyses 

Le tableau suivant contient des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation de l’audience.

| Indicateur | Description |
| ------ | ----------- |
| Saisie | Le nombre d’utilisateurs ayant saisi cette étape pour qu’elle soit synchronisée avec Google. |
| Poursuivre vers l’étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un. Tous les utilisateurs avanceront automatiquement s’il s’agit de la dernière étape de la branche Canvas. |
| Utilisateurs synchronisés | Nombre d’utilisateurs ayant réussi à se synchroniser avec Google. |
| Utilisateur non synchronisé | Nombre d’utilisateurs qui n’ont pas été synchronisés en raison de champs manquants à faire correspondre. |
| Utilisateurs en erreur | Nombre d’utilisateurs qui n’ont pas été synchronisés avec Google en raison d’une erreur après &#126;13 heures de tentatives. En cas d’erreurs spécifiques, telles que les interruptions de service de l’API Google Ads, Canvas essaiera de relancer la synchronisation pendant une période de &#126;13 heures maximum. Si la synchronisation n’est toujours pas possible à ce moment-là, l’utilisateur sera répertorié comme non synchronisé. |
| Utilisateurs en attente | Nombre d’utilisateurs en cours de traitement par Braze et en attente de synchronisation avec Google. |
| Sortis de Canvas | Nombre d’utilisateurs ayant quitté le Canvas. Cela se produit lorsque la dernière étape d’un Canvas est une étape Google. |
{: .reset-td-br-1 .reset-td-br-2}

## Résolution des problèmes
{% details Pourquoi ne puis-je pas sélectionner plusieurs champs à faire correspondre dans ma configuration d’étape Google Audience ? %}
Google Customer Match a des exigences strictes concernant la manière dont ces audiences sont formatées et les informations sur les clients qu’elles incluent. Plus précisément, les ID d’annonceurs mobiles doivent être téléchargés séparément des coordonnées du client (c.-à-d., adresse e-mail et numéro de téléphone). Consultez la [documentation de Google Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined) pour plus d’informations. 
{% enddetails %}

{% details Combien de temps faudra-t-il pour que mes audiences se synchronisent dans Google ? %} 
Une audience peut prendre entre six et douze heures avant d’être synchronisée sur Google. 
{% enddetails %}

{% details J’ai synchronisé une audience, mais sa taille dans Google est nulle. %}
Pour des raisons de confidentialité, la taille de la liste d’utilisateurs affichera « zéro » jusqu’à ce que la liste compte au moins **1 000 membres**. Ensuite, la taille sera arrondie aux deux chiffres les plus significatifs.
{% enddetails %}

{% details J’ai synchronisé une audience sur Google, mais mes publicités ne sont pas diffusées. %}
Vérifiez que vos audiences comptent au moins **5 000** utilisateurs pour vous assurer que les publicités sont bien envoyées. 
{% enddetails %}

[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
