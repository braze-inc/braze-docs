---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Cet article de référence décrit le partenariat entre Braze et Dyspatch, un générateur d'e-mails par glisser-déposer qui vous permet de créer des e-mails attrayants, réactifs et engageants sans avoir à écrire une seule ligne de code."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) propose un générateur d'e-mails intuitif par glisser-déposer utilisé pour créer des e-mails magnifiques, réactifs et attrayants sans avoir à écrire de code. Collaborez avec votre équipe pour créer et approuver des e-mails dans Dyspatch, puis exportez-les vers Braze, le tout en quelques étapes ! 

_Cette intégration est maintenue par Dyspatch._

## À propos de l'intégration

L'intégration de Dyspatch et Braze vous permet de simplifier le cycle de vie de création de vos e-mails en exportant les modèles d'e-mails Dyspatch directement vers Braze.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Dyspatch | Un [compte Dyspatch](https://www.dyspatch.io/login/) avec un [rôle de propriétaire ou d'administrateur](https://docs.dyspatch.io/administration/dyspatch_roles/) est requis pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations complètes sur les **modèles**. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

L'intégration de Braze et Dyspatch vous permet d'exporter des modèles d'e-mails Dyspatch directement dans votre bibliothèque multimédia Braze ou de télécharger votre modèle et de le charger manuellement. 

### Étape 1 : Créez l'intégration Braze

Dans le portail d'administration de Dyspatch, ouvrez le menu déroulant de votre nom d'utilisateur et sélectionnez **Intégrations**. Créez une nouvelle intégration, sélectionnez **Braze** et entrez votre clé API Braze.

Dans le champ **Rechercher les exports par**, vous pouvez choisir la manière dont vous souhaitez gérer la localisation. Ce champ vous permet de [localiser vos modèles d'e-mails et de](https://docs.dyspatch.io/localization/localizing_a_template/) les exporter vers Braze pour envoyer facilement des e-mails personnalisés par langue ou par région. 

![Modèle d'exportation Dyspatch] ({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Étape 2 : Modèle d'exportation vers Braze

Pour envoyer le modèle d’e-mail que vous avez créé dans Dyspatch à Braze, affichez le modèle d'e-mail publié et cliquez sur **Télécharger/Exporter**, puis sur **Exporter vers l'intégration**.

Si vous souhaitez télécharger votre modèle manuellement, consultez le modèle d'e-mail publié et cliquez sur **Télécharger/Exporter**, puis sur **Télécharger le code HTML**. Ensuite, dans la section **Modèles et médias > Modèles d'e-mails** de votre compte Braze, sélectionnez **À partir du fichier** pour télécharger votre modèle.

![Modèle d'exportation Dyspatch] ({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Ne sélectionnez pas le **CSS en ligne** dans la section **Informations d'envoi** pour aucun modèle d'e-mail Dyspatch dans Braze. Dyspatch s'en charge en s'assurant que vos e-mails sont robustes, réactifs et prêts à être envoyés.
{% endalert %}

### Utilisation

Trouvez le modèle Dyspatch que vous avez téléchargé dans la section **Modèles et médias > Modèles** d'e-mails de votre compte Braze. Vous pouvez désormais utiliser ce modèle d'e-mail pour commencer à envoyer des e-mails attrayants à vos clients !


