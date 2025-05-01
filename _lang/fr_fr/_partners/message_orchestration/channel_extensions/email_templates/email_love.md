---
nav_title: "L'e-mail de l'amour"
article_title: "L'e-mail de l'amour"
description: "Découvrez comment intégrer Braze avec Email Love, un plugin Figma qui vous permet de concevoir et d'exporter des e-mails HTML réactifs et accessibles directement depuis Figma."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# L'e-mail de l'amour

> [Email Love](https://emaillove.com/) est un plugin Figma qui vous permet de concevoir et d'exporter des e-mails HTML réactifs et accessibles directement depuis Figma. La fonctionnalité Export to Braze d'Email Love utilise l'API de Braze pour télécharger de façon fluide/sans heurts/de façon homogène vos modèles d'e-mails vers Braze.

## Conditions préalables

| Condition            | Description                                                      |
|------------------------|------------------------------------------------------------------|
| **E-mail Compte d'amour** | Un compte e-mail Love est nécessaire pour profiter de ce partenariat. |
| **Clé d'API REST Braze** | Une clé de l'API REST de Braze avec l'autorisation complète `Templates`. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

## Utiliser l'e-mail avec Braze

### Étape 1 : Exécutez le plugin

Pour concevoir votre modèle d'e-mail, vous devrez d'abord charger le plugin. Pour des instructions plus détaillées, reportez-vous à la documentation d'Email Love concernant le [téléchargement de votre e-mail vers Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Étape 2 : Créez votre premier cadre

Dans le plugin, sélectionnez le bouton **[+ No Template Selected]** ] pour créer un nouveau cadre pour la conception de votre e-mail.

### Étape 3 : Créez le modèle à l'aide des composants préconstruits d'Email Love

Sélectionnez le cadre que vous avez créé et commencez à ajouter des composants (en-têtes, blocs de contenu, CTA et pieds de page) à partir de la bibliothèque **Assets** du plugin pour structurer votre e-mail.

![Composants pré-créés de l'e-mail Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Étape 4 : Personnaliser les composants

Modifiez les composants à l'aide des outils de Figma pour ajuster votre texte, vos images, vos couleurs et vos éléments de mise en page afin d'aligner la conception du modèle sur votre marque. Si vous ajoutez un composant de pied de page, un lien de désinscription de Braze sera automatiquement inclus lors de l'exportation.

![Personnalisez les composants dans Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Étape 5 : Exporter votre modèle d'e-mail vers Braze

1. Lorsque vous avez terminé, sélectionnez le cadre que vous souhaitez exporter. Notez que vous devrez utiliser un pied de page Email Love contenant un lien de désabonnement pour que l'exportation fonctionne.
2. Sélectionnez le bouton **Exporter** dans le plugin et sélectionnez **Braze** dans le menu déroulant.
3. Copiez et collez votre clé API dans le champ **Clé API de Braze** dans le plugin Email Love Figma.
4. Sélectionnez le bouton **Définir la clé API**.
5. Sélectionnez **Change Instance ID**, puis sélectionnez votre ID d'instance Braze.

![Exportation d'un modèle vers Braze à partir du plugin Email Love.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Étape 6 : Modifiez votre e-mail dans Braze

Dans Braze, allez dans **Modèles** > **Modifier les modèles** > Modifier le **message.** Dans l'éditeur de modèles, vous pouvez soit modifier le code HTML de votre e-mail, soit utiliser l'**éditeur de texte enrichi** dans l'onglet **Classique**.

## Assistance et résolution des problèmes

Pour des instructions plus détaillées, reportez-vous à la documentation d'Email Love sur l'[exportation d'un modèle d'e-mail.](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm) Pour obtenir une assistance supplémentaire, contactez l'équipe d'assistance d'Email Love.
