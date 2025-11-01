---
nav_title: Mise en place des courants
article_title: Mise en place des courants
page_order: 0
page_type: tutorial
description: "Cet article pratique vous guide à travers le processus d'intégration et de configuration de Braze Currents."
tool: Currents
search_rank: 8
---

# ![cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"} Mise en place des Currents

> Cette page présente et décrit le processus générique d'intégration et de configuration des Braze Currents.

{% alert important %}
Les courants sont inclus dans certains forfaits Braze. Contactez votre conseiller Braze si vous avez des questions ou si vous souhaitez obtenir un accès.
{% endalert %}

## Exigences

L'utilisation de Currents avec n'importe lequel de nos partenaires nécessite les mêmes paramètres de base et la même méthodologie de connexion.

Chaque partenaire demande à Braze l'autorisation d'écrire et de lui envoyer des fichiers de données, et Braze lui demande l'emplacement/localisation dans lequel il doit écrire ces fichiers, en particulier les noms des compartiments ou les clés.

Les exigences suivantes sont les exigences de base, minimales, pour l'intégration avec la plupart de nos partenaires. Certains partenaires exigeront des paramètres supplémentaires, qui sont énumérés dans la [documentation de leur partenaire]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) respectif, ainsi que toutes les nuances associées à ces exigences de base.

| Exigence | Origine | Accès | Description
|---|---|---|---|
| Compte avec partenaire | Organisez un compte avec ce partenaire ou contactez votre gestionnaire de compte Braze pour obtenir des suggestions. | Consultez le site de ce partenaire ou contactez-le pour vous inscrire. | Braze n'enverra pas de données à un partenaire si vous n'avez pas accès à ces données via le compte de votre entreprise.
| Clé ou jeton API du partenaire | Il s'agit généralement du tableau de bord du partenaire. | Il suffit de le copier et de le coller dans le champ prévu pour Braze. | Braze dispose d'un champ réservé à cet effet dans la page d'intégration de ce partenaire. Nous en avons besoin pour mapper l'endroit où nous envoyons vos données. **Il est important que vos clés ou jetons de partenaire soient à jour ; des informations d'identification non valides peuvent entraîner la désactivation de votre connecteur et l'abandon d'événements.**
| Code/clé d'authentification, clé secrète, fichier de certification | Contactez un conseiller pour votre compte auprès de ce partenaire. Peut également exister dans le tableau de bord du partenaire. | Copiez et collez les clés dans le champ désigné de Braze. Générez et téléchargez `.json` ou d'autres fichiers de certification à l'endroit approprié dans Braze. | Braze dispose d'un champ réservé à cet effet dans la page d'intégration de ce partenaire. Cela donne à Braze des informations d'identification et nous autorise à écrire des fichiers sur votre compte partenaire. **Il est important que vos informations d'authentification soient à jour ; des informations d'identification non valides peuvent entraîner la désactivation de votre connecteur et l'abandon d'événements.**
| Compartiment, chemin d'accès au dossier | Certains partenaires organisent et trient les données par compartiment. Vous trouverez cette information dans le tableau de bord du partenaire. | Si cela est nécessaire, veillez à copier le nom du compartiment ou le chemin d'accès au fichier exactement dans l'espace prévu à cet effet dans Braze. Nous ne voulons pas que vos données se perdent ! | Bien que cela soit nécessaire pour certains partenaires, il est important de bien faire les choses lorsque vous en avez besoin. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Il est important de mettre à jour vos clés de partenaire, vos jetons de partenaire et vos détails d'authentification ; si les informations d'identification de votre connecteur expirent, le connecteur cessera d'envoyer des événements. Si cette situation persiste pendant plus de **5 jours**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

## Mise en place des courants

### Étape 1 : Choisissez votre partenaire

Braze Currents vous permet de procéder à une intégration par le biais du stockage de données à l'aide de fichiers plats ou vers nos partenaires d'analyse/analytique comportementale et de données clients à l'aide de charges utiles JSON groupées vers un endpoint désigné.  

Avant de commencer votre intégration, il est préférable de décider quelle est l'intégration la mieux adaptée à vos besoins. Par exemple, si vous utilisez déjà mParticle et Segment et que vous souhaitez que les données Braze y soient transmises en continu, il est préférable d'utiliser une charge utile JSON en mode batch. Si vous préférez manipuler les données par vous-même ou si vous disposez d'un système d'analyse des données plus complexe, il est préférable d'utiliser le stockage des données[(Braze utilise cette méthode]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!).

### Étape 2 : Courants libres

Pour commencer, allez dans **Intégrations partenaires** > **Exportation de données**. Vous accédez à la page de gestion de l'intégration currents.

!page Currents dans le tableau de bord de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Étape 3 : Ajoutez votre partenaire

Ajoutez un partenaire, parfois appelé "connecteur actuel", en sélectionnant le menu déroulant en haut de l'écran.

Chaque partenaire nécessite un ensemble différent d'étapes de configuration. Pour activer chaque intégration, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et suivez les instructions figurant sur leurs pages respectives.

### Étape 4 : Configurez vos événements

Choisissez les événements que vous souhaitez transmettre à ce partenaire en cochant l'une des options disponibles. Vous trouverez la liste de ces événements dans nos bibliothèques " [Événements comportement des clients"]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et " [Événements engagement des messages"]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

\![]({% image_buster /assets/img/current4.png %})

Si nécessaire, vous pouvez en savoir plus sur nos événements dans notre article sur [la sémantique de réception/distribution des événements]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### Étape 5 : Mise en place des transformations de champ

Vous pouvez utiliser les transformations de champs Currents pour supprimer ou hacher un champ de chaînes de caractères.

- **Retirer :** Remplace la chaîne de caractères par `[REDACTED]`. Ceci est utile si votre partenaire rejette les événements dont les champs sont manquants ou vides.
- **Hash :** Applique un algorithme de hachage SHA-256 à la chaîne de caractères.

La sélection d'un champ pour l'une de ces transformations appliquera cette transformation à tous les événements dans lesquels ce champ apparaît. Par exemple, si vous sélectionnez `email_address` pour le hachage, le champ `email_address` sera haché dans les événements d'envoi d'e-mail, d'ouverture d'e-mail, de rebond d'e-mail et de changement d'état du groupe subscribe groups.

!Ajouter des transformations de champs]({% image_buster /assets/img/current3.png %})

### Étape 6 : Testez votre intégration

{% alert important %}
Currents abandonnera les événements dont la charge utile est excessivement importante (plus de 900 Ko).
{% endalert %}

Avant de tester, pensez à consulter notre [échantillon de données Currents sur GitHub](https://github.com/Appboy/currents-examples). Lorsque vous êtes prêt à tester, vous choisissez une option ci-dessous :

#### Envoi d'événements de test

Pour tester votre intégration, vous pouvez sélectionner **Envoyer des événements de test** pour envoyer un événement de chacun des types d'événements sélectionnés à ce Current. Pour obtenir des informations détaillées sur chaque type d'événement, consultez nos bibliothèques [Événements liés au comportement des clients]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et [Événements liés à l'engagement des messages.]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 

!La page "Currents Test" dans le tableau de bord de Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Test des connecteurs de courant

Les connecteurs Test Currents sont des versions gratuites de nos connecteurs existants qui peuvent être utilisées pour tester et essayer différentes destinations. Les courants d'essai ont :

- Le nombre de connecteurs Test Currents que vous pouvez créer n'est pas limité.
- Un maximum global de 10 000 événements par période glissante de sept jours. Ce total d'événements est mis à jour toutes les heures sur le tableau de bord.

Lorsque vos connecteurs Test Currents atteignent la limite d'envoi, votre connecteur n'enverra plus d'événements jusqu'à la prochaine période de sept jours.

Pour mettre à niveau votre connecteur Test Currents, modifiez l'intégration dans le tableau de bord et sélectionnez **Mettre à niveau l'intégration de test**.

## Mise à jour des courants

{% multi_lang_include updating_currents.md %}

## Liste d'autorisation IP

Braze enverra les données Currents à partir des adresses IP répertoriées :

{% multi_lang_include data_centers.md datacenters='ips' %}
