---
nav_title: Dyspatch
article_title: Dyspatch
alias: /fr/partners/dyspatch
description: "Cet article décrit le partenariat entre Braze et Dyspatch, un constructeur de courriels glisser-déposer qui vous permet de créer de la beauté, des courriels réactifs et engageants sans avoir besoin d'écrire du code."
page_type: partenaire
search_tag: Partenaire
---

# Dyspatch

> [Dyspatch][1] offre un constructeur intuitif de courriels par glisser-déposer utilisé pour créer des e-mails jolis, réactifs et engageants sans avoir besoin d'écrire du code. Collaborez avec votre équipe pour créer et approuver des e-mails au sein de Dyspatch et puis exportez-les au Brésil, en quelques étapes rapides !

L'intégration de Dyspatch et Braze vous permet de simplifier votre cycle de vie de création d'e-mails en exportant directement des modèles d'e-mails Dyspatch vers Brésil.

## Pré-requis

| Exigences          | Libellé                                                                                                                                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte dyspatch    | Un compte [Dyspatch][3] avec un rôle de [propriétaire ou administrateur][4] est requis pour profiter de ce partenariat.                                                                                                 |
| Braze clé API REST | Une clé API Braze REST avec les permissions complètes de **Modèles**. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

L'intégration de Braze et Dyspatch vous permet d'exporter des modèles d'e-mail Dyspatch directement dans votre médiathèque Braze ou de télécharger votre modèle et de le télécharger manuellement.

### Étape 1 : Créer l’intégration de Braze

Dans le portail d'administration de Dyspatch, ouvrez le menu déroulant de votre nom d'utilisateur et sélectionnez **Intégrations**. Créez une nouvelle intégration, sélectionnez **Braze**, et entrez votre clé API Braze.

Dans le champ **Localiser les exportations par** vous pouvez choisir comment vous souhaitez gérer les localisations. Ce champ vous permet de [localiser vos modèles d'e-mails][6] et de les exporter vers Braze pour envoyer facilement des e-mails personnalisés par langue ou par langue.

![Modèle d'exportation Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Étape 2 : Exporter le modèle à Braze

Après avoir complété un e-mail en Dyspatch, pour envoyer votre modèle à Braze, consultez le modèle d'e-mail publié et cliquez sur **Télécharger/Exporter** puis **Exporter vers l'intégration**.

Si vous voulez télécharger votre modèle manuellement, consultez le modèle d'e-mail publié et cliquez sur **Télécharger/Exporter** puis **Télécharger HTML**. Ensuite, dans la section **Modèles & Média > Modèles d'E-mail** de votre compte Braze, sélectionnez **De Fichier** pour télécharger votre modèle.

![Modèle d'exportation Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Ne sélectionnez pas **CSS Inline** dans la section **Sending Info** pour tout modèle d'e-mail Dyspatch en Brésil. Dyspatch s'occupe de cela en s'assurant que vos e-mails sont robustes, réactifs et prêts à être envoyés.
{% endalert %}

### Usage

Trouvez votre modèle Dyspatch téléchargé dans la section **Modèles & Médias > Modèles d'e-mails** de votre compte Braze. Vous pouvez maintenant utiliser ce modèle d'e-mail pour commencer à envoyer des messages de messagerie engageants à vos clients !

[1]: https://www.dyspatch.io
[3]: https://www.dyspatch.io/login/
[4]: https://docs.dyspatch.io/administration/dyspatch_roles/
[6]: https://docs.dyspatch.io/localization/localizing_a_template/
