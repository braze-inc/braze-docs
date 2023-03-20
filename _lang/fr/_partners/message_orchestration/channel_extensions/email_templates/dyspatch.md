---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Cet article de référence présente le partenariat entre Braze et Dyspatch, un générateur d’e-mails par glisser-déposer qui vous permet de créer des e-mails magnifiques, réactifs et attrayants sans avoir besoin d’écrire le code."
page_type: partner
search_tag: Partenaire

---

# Dyspatch

> [Dyspatch][1] offre un outil intuitif de messagerie par glisser-déposer pour créer des e-mails magnifiques, réactifs et attrayants sans avoir besoin d’écrire le code. Collaborez avec votre équipe pour créer et approuver des e-mails dans Dyspatch, puis les exporter vers Braze, le tout en quelques étapes rapides ! 

L’intégration de Dyspatch et de Braze vous permet de simplifier le cycle de vie de la création d’e-mails en exportant les modèles d’e-mail de Dyspatch directement vers Braze.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Dyspatch | Un [compte Dyspatch][3] avec un [rôle propriétaire ou administrateur][4] est nécessaire pour tirer parti de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations **Modèles** complètes. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

L’intégration de Braze et de Dyspatch vous permet d’exporter les modèles d’e-mail de Dyspatch directement dans votre bibliothèque de médias Braze ou de télécharger votre modèle et de le charger manuellement. 

### Étape 1 : Créer l’intégration Braze

Dans le portail d’administration de Dyspatch, ouvrez votre menu déroulant Nom d’utilisateur et sélectionnez **Integrations (Intégrations)**. Créez une nouvelle intégration, sélectionnez **Braze** et entrez votre clé d’API Braze.

Dans le champ **Localize Exports By (Localiser les exportations par)**, vous pouvez choisir la façon dont vous souhaitez gérer les localisations. Ce champ vous permet de [localiser vos modèles d’e-mails][6] et de les exporter vers Braze pour envoyer facilement des e-mails personnalisés par langue ou par paramètre régional. 

![Modèle d’exportation de Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Étape 2 : Exporter le modèle vers Braze

Après avoir terminé un e-mail dans Dyspatch, pour envoyer votre modèle à Braze, consultez le modèle d’e-mail publié et cliquez sur **Download/Export (Télécharger/Exporter)** puis sur **Export to Integration (Exporter vers l’intégration)**.

Si vous souhaitez télécharger manuellement votre modèle, consultez le modèle d’e-mail publié et cliquez sur **Download/Export (Télécharger/Exporter)** puis sur **Download HTML (Télécharger HTML)**. Ensuite, dans la section **Templates & Media (Modèles et médias) > Email Templates (Modèles d’e-mail)** de votre compte Braze, sélectionnez **From File (Du fichier)** pour charger votre modèle.

![Modèle d’exportation de Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Ne sélectionnez pas **Inline CSS** dans la section **Sending Info (Envoi d’infos)** pour les modèles d’e-mail de Dyspatch dans Braze. Dyspatch s’occupe de cela en s’assurant que vos e-mails sont robustes, réactifs et prêts à l’envoi.
{% endalert %}

### Utilisation

Vos modèles Dyspatch téléchargés dans votre compte Braze sont affichés dans la section **Templates & Media (Modèles et médias) > Email Templates (Modèles d’e-mail)**. Vous pouvez maintenant utiliser ce modèle d’e-mail pour commencer à envoyer des e-mails attrayants à vos clients !

[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: https://www.dyspatch.io/login/
[4]: https://docs.dyspatch.io/administration/dyspatch_roles/
[5]: https://docs.dyspatch.io/exports/export_to_braze/#download-your-template
[6]: https://docs.dyspatch.io/localization/localizing_a_template/
