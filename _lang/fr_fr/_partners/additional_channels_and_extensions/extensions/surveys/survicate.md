---
nav_title: Survicate
article_title: Survicate
description: "Cet article de référence présente le partenariat entre Braze et Survicate, une plateforme de feedback client qui vous aide à collecter, analyser et agir sur les informations clients sur plusieurs canaux et tout au long du parcours client."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) est une plateforme de feedback client qui recueille, analyse et agit sur les informations clients à travers plusieurs canaux et tout au long du parcours client. [Regardez une démonstration rapide](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_Cette intégration est maintenue par Survicate._

## À propos de l'intégration

Utilisez l'intégration native de Survicate et Braze pour synchroniser les réponses aux enquêtes par e-mail, in-app, sur mobile ou sur le web avec les profils des clients de Braze. Les réponses aux enquêtes se synchronisent automatiquement avec les profils des utilisateurs de Braze sous forme d'attributs personnalisés ou d'événements. Les informations sur les commentaires en temps réel facilitent le suivi et l'analyse des commentaires parallèlement aux données clients et permettent de créer des suivis ciblés et des segments hyper-personnalisés. 

## Cas d’utilisation

Braze et Survicate travaillent ensemble pour couvrir un éventail de cas d'utilisation du feedback, vous aidant à collecter des informations exploitables sur les utilisateurs et à améliorer l'expérience client :

- Améliorez les taux de réponse aux enquêtes grâce à des enquêtes intégrées auxquelles il est possible de répondre à partir d'une boîte de réception e-mail. 
- Recueillez des informations aux étapes critiques du parcours client via le message in-app de Braze. 
- Utilisez le retour d'information stocké dans Survicate pour créer des segments plus intelligents dans Braze. 
- Automatisez les campagnes de suivi en fonction des commentaires des clients. 
- Utilisez les informations sur les clients pour déclencher des flux de travail personnalisés. 
- Touchez une audience plus large grâce à des enquêtes traduites automatiquement.
- Envoyez des événements aux profils de contact de Braze lorsque quelqu'un répond à votre enquête.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Survicate | Vous devez disposer d'un compte Survicate pour activer cette intégration. |
| Clé d'API REST Braze | Une clé API REST de Braze avec la permission `users.track`. <br><br> Celui-ci peut être créé dans le tableau de bord de Braze à partir de **Paramètres** > **API et Identifiants.** |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Principales fonctionnalités de l'intégration

L'intégration de Survicate et de Braze offre une synchronisation des données en temps réel, de sorte que les informations les plus récentes des enquêtes Survicate sont immédiatement disponibles dans Braze. En fonction des réponses à l'enquête, vous pouvez utiliser ces données pour prendre des mesures personnalisées en temps voulu.

- **Envoyez les réponses à l'enquête à Braze sous forme d'attributs personnalisés**: Enrichissez les profils utilisateurs de Braze avec des données issues de réponses à des enquêtes.
- **Déclenchez des événements personnalisés dans Braze**: Utilisez les événements basés sur les réponses à l'enquête pour cibler des groupes spécifiques ou lancer des campagnes de suivi.
- **Créez des segments détaillés**: Créez des segments Braze en utilisant les données des enquêtes Survicate pour personnaliser davantage votre action de sensibilisation.

## Intégration

### Créez vos enquêtes dans Survicate

#### Intégrez votre enquête dans un e-mail ou créez un lien d'enquête partageable. 

1.  Dans Survicate, cliquez sur **\+ Créer une nouvelle enquête**, sélectionnez n'importe quelle méthode de création (un modèle, l'utilisation de la création d'enquête par intelligence artificielle, ou l'ajout de vos propres questions), et le type d'enquête par e-mail ou par lien partageable :
![Braze est sélectionné dans le créateur de l'enquête.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2\. Dans l'onglet Configuration de l'enquête, sélectionnez **Braze** comme outil d'identification des répondants :
![Braze est sélectionné dans l'onglet Configuration de l'enquête.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3\. Après avoir configuré votre sondage, allez dans l'onglet Partager et décidez de la manière d'envoyer votre sondage par e-mail. Deux options s'offrent à vous : vous pouvez envoyer votre **enquête sous forme de lien** ou **intégrer la première question dans l'e-mail** afin que les personnes interrogées commencent à répondre à l'enquête dès l'e-mail.

{% details Survey link option %}

1. Créez un lien vers votre enquête à l'aide du bouton Copier le lien de l'enquête :

![Créez un lien vers votre enquête à l'aide du bouton Copier le lien de l'enquête.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2\. Cachez le lien de l'enquête derrière un bouton CTA ou un lien hypertexte dans votre e-mail Braze.

![Cachez le lien de l'enquête derrière un bouton CTA ou un lien hypertexte dans votre e-mail Braze.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

Affichez la première question directement dans le corps de l'e-mail pour lancer l'enquête à partir de l'e-mail. Les répondants sont ensuite redirigés vers une page de renvoi pour répondre au reste de l'enquête.

1. Cliquez sur **Obtenir le code de l'e-mail**, puis sur **Copier le code HTML**:

![Obtenir un code e-mail]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2\. Accédez à la campagne Braze que vous souhaitez utiliser pour l'enquête, cliquez sur **Modifier le corps de l'e-mail** et ajoutez un bloc HTML à votre modèle :

![Obtenir le code du bloc HTML]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3\. Remplacez le code par celui que vous avez copié dans votre enquête Survicate. La première question de l'enquête apparaît alors dans le modèle :

![Remplacez le code par celui que vous avez copié à partir de votre enquête Survicate.]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4\. Planifiez l'e-mail, choisissez votre groupe cible et votre campagne est prête à être envoyée.

{% enddetails %}

### Enquête sur les messages in-app de Braze

1. Cliquez sur **\+ Créer un nouveau sondage**, sélectionnez n'importe quelle méthode de création (un modèle, l'utilisation de la création de sondage par intelligence artificielle ou l'ajout de vos propres questions), puis choisissez les sondages In-platform et le type de sondage Braze In-App Message :

![Cliquez sur + Créer une nouvelle enquête, sélectionnez la méthode de création de votre choix.]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2\. Lancez votre enquête sur les messages in-app de Braze en vous rendant sur votre compte Braze, puis sur **Messagerie > Campagnes > Créer une campagne > Message in-app**:
![Lancez votre envoi de messages in-app de Braze]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Lancez votre enquête Braze In-App Messenger via l'éditeur traditionnel.

1. Si vous utilisez l'éditeur traditionnel, dans le type de message, choisissez **Code personnalisé**:

![choisissez Code personnalisé]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2\. Collez ensuite le code de l'onglet Lancement de votre enquête dans le champ HTML :

![collez le code de l'onglet Lancement de votre enquête dans le champ HTML]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze affiche par défaut les messages in-app dans une iframe alors que l'arrière-plan de l'application est bloqué. Pour permettre l'interaction avec votre application, lorsque les enquêtes de Survicate apparaissent, vous devez<br><br>

- Ajoutez `opts.useBrazeIframeClipper = true` à votre extrait de code Survicate-Braze.
- Installez le [paquet](https://www.npmjs.com/package/@survicate/braze-bridge-npm) `@survicate/braze-bridge-npm` dans le fichier où vous initialisez Braze et utilisez la fonction `initBrazeBridge`.

Vous trouverez un extrait de code et une implémentation React [sur le site des développeurs de Survicate.](https://developers.survicate.com/javascript/installation/#braze)
{% endalert %}

{: start="3"}
3\. Dans votre campagne Braze, implémentez les étapes Cibler et Assigner. Une fois terminée, votre campagne est prête à être lancée. À l'étape de l'examen, vous pouvez voir à quoi ressemble la campagne. L'enquête apparaît sur votre site web à l'endroit spécifié dans le panneau Survicate, comme décrit ci-dessus.

### Permettre l'intégration de Braze

1. Pour activer l'intégration de Braze, allez dans **Intégrations**, recherchez et sélectionnez "Braze".

![Sélectionnez Braze]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2\. Cliquez sur **Connecter** pour établir l'autorisation.

3. Insérez la clé API de l'espace de travail de votre compte Braze et l'URL de l'instance Braze :

![Insérez la clé API de l'espace de travail de votre compte Braze et l'URL de l'instance Braze.]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Pour connecter Survicate à Braze, la clé API de Braze doit avoir les permissions `users.track`.
{% endalert %}

### Connecter vos enquêtes à Braze

Maintenant que l'intégration de Braze est connectée, vous pouvez définir des paramètres individuels pour chaque enquête. Accédez à votre sondage, sélectionnez l'onglet **Connecter** et choisissez **Braze** dans la liste des intégrations disponibles.

![Accédez à votre enquête, sélectionnez l'onglet Connexion et choisissez Braze.]({% image_buster /assets/img/survicate/survicate_14.png %})

### Envoi des réponses à Braze sous forme d'attributs personnalisés

Configurez les réponses à l'enquête pour qu'elles soient intégrées dans Braze en tant qu'attributs personnalisés, ce qui permet d'enrichir les profils utilisateurs de Braze avec les données collectées.

1. Dans l'onglet Paramètres de l'intégration Braze, amendez la section **Champs de mise à jour**.

![Sélectionnez la section Mettre à jour les champs]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2\. Sélectionnez la question pour laquelle vous souhaitez mettre à jour les champs. Pour éviter d'inonder de données les profils utilisateurs de Braze, vous pouvez envoyer des réponses à certaines questions seulement.

![Sélectionnez la question pour laquelle vous souhaitez mettre à jour les champs.]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
Les questions de classement et de matrice ne sont pas prises en charge par cette intégration de Braze.
{% endalert %}

{: start="3"}
3\. Ajoutez le nom de l'attribut personnalisé que vous souhaitez mettre à jour sous le champ **Utilisateur**:

![Ajoutez le nom de l'attribut personnalisé que vous souhaitez mettre à jour sous le champ Utilisateur]({% image_buster /assets/img/survicate/survicate_17.png %})

Par défaut, Survicate envoie le contenu d'une réponse à une enquête en tant que valeur d'attribut. Vous pouvez modifier l'étiquette pour la rendre plus courte ou l'adapter à la structure de vos données en cliquant sur **Modifier le mappage** pour modifier ces valeurs :

![Réponse à l'enquête en tant que valeur d'attribut]({% image_buster /assets/img/survicate/survicate_18.png %})

![Cliquez sur modifier le mappage pour modifier ces valeurs.]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
Pour le Net Score, Survicate envoie des valeurs mappées en fonction du groupe de réponse à la question du Net Promoter Score®. Toutefois, si vous souhaitez recevoir des valeurs numériques, vous pouvez activer l'option Envoyer les réponses sous forme de valeurs 0-10.
{% endalert %}

![Survicate envoie des valeurs mappées sur la base du groupe de réponses]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4\. Connectez d'autres questions à votre intégration en cliquant sur **\+ Ajouter nouveau** et en appliquant les mêmes étapes.

![Associez plus de questions à votre intégration]({% image_buster /assets/img/survicate/survicate_21.png %})

### Envoi d'événements aux profils des contacts de Braze

Outre les paramètres précédents, chaque fois qu'un répondant répond à une question de l'enquête, Survicate peut envoyer un événement personnalisé dans Braze, nommé `survicate-question-answered`.
Dans le panneau Survicate, sous Envoyer les réponses en tant qu'attributs personnalisés, vous pouvez choisir d'envoyer l'événement pour toutes les questions, les questions choisies dans l'onglet Mettre à jour les champs, ou pas du tout :

![vous pouvez choisir d'envoyer l'événement pour toutes les questions]({% image_buster /assets/img/survicate/survicate_22.png %})

Si vous choisissez d'envoyer les événements, vous pouvez voir dans les profils des utilisateurs combien de fois ils ont répondu aux enquêtes de Survicate et quand ils ont répondu pour la dernière fois :

![Réponses ]({% image_buster /assets/img/survicate/survicate_23.png %})

L'événement contient des propriétés d'événement avec la réponse à la question et des informations sur l'enquête, la question et le répondant. Vous pouvez utiliser cet événement pour créer des segmentations. Par exemple, créez un segment d'utilisateurs qui ont répondu à une enquête après une certaine date ou un certain nombre de fois :

![L'événement contient des propriétés d'événement avec la réponse]({% image_buster /assets/img/survicate/survicate_24.png %})

Vous pouvez également utiliser ces données lors de la création d'une campagne dans Braze.

![Vous pouvez également utiliser ces données lors de la création d'une campagne dans Braze]({% image_buster /assets/img/survicate/survicate_25.png %})

### Tester l'intégration

Lorsque votre enquête est prête et que l'intégration est configurée, vous pouvez la tester sans quitter Survicate en cliquant sur le bouton Tester l'intégration à côté de n'importe quel attribut, étiquette ou configuration de nouveau contact que vous avez créé. Survicate crée un contact test (`braze-test@survicate.com`) dans votre compte Braze. Le profil du contact comprend des champs mis à jour conformément à la configuration.

![Cliquez sur le bouton Test d'intégration]({% image_buster /assets/img/survicate/survicate_26.png %})

Dans Braze, vous voyez des exemples de données provenant des champs mappés dans le contact fictif de Survicate :

![Exemple de données provenant des champs mappés dans le contact fictif de Survicate]({% image_buster /assets/img/survicate/survicate_27.png %})

### Analyser les résultats de votre enquête

Après avoir recueilli des réponses dans le cadre de votre enquête Braze, il est temps d'examiner les commentaires et les informations que vos répondants ont partagés. Survicate vous permet d'examiner facilement les résultats, les statistiques et les tendances afin de prendre des mesures supplémentaires.

### Le retour d'information dans Survicate

Une fois que votre enquête commence à recueillir des réponses, vous les voyez immédiatement dans l'onglet Analyser de l'enquête.

![Réponses dans l'onglet Analyser]({% image_buster /assets/img/survicate/survicate_28.png %})

L'onglet Analyser vous présente les résultats globaux avec des statistiques et des données sur la durée, ainsi que les réponses individuelles pour examiner en détail chaque soumission à l'enquête.

### Retour d'expérience en Braze

Si vous mettez à jour les champs utilisateur avec les réponses à l'enquête ou si vous envoyez les réponses en tant qu'événements personnalisés, vous pouvez voir les données de l'enquête synchronisées en temps réel. Dans Braze, accédez à un contact spécifique qui a répondu à votre enquête. Les données basées sur les réponses et les événements sont affichés dans la vue principale du contact.

![synchronisation en temps réel des données d'enquête]({% image_buster /assets/img/survicate/survicate_29.png %}) 