---
nav_title: Des mots justes
article_title: Des mots justes
description: "Cet article de référence présente le partenariat entre Braze et Just Words, une plateforme commerciale SaaS basée sur l'intelligence artificielle qui crée des versions personnalisées de campagnes existantes et optimise les lignes d'objet, le contenu créatif et les mises en page des e-mails HTML au fil du temps."
alias: /partners/just_words/
page_type: partner
---

# Guide d'intégration de Just Words

> [Just Words](https://www.justwords.ai/) hyperpersonnalise les messages à grande échelle sur les canaux de marketing du cycle de vie, vous permettant de tester dynamiquement des centaines de variations et d'actualiser automatiquement les contenus peu performants.

Lorsque vous utilisez Just Words avec Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) pour personnaliser vos campagnes et canevas Braze existants, Just Words utilisera Braze Currents pour optimiser le contenu de manière dynamique - vous n'aurez donc pas à le faire.

## Quels en sont les avantages ?

Une fois votre intégration terminée, vous pouvez tirer parti de la plateforme Just Works pour :

- Voir les résultats de l'expérience en temps réel
- Modifier dynamiquement la copie
- Voir les informations sur les performances

{% alert note %}
Des questions ? Contactez Just Words sur leur [page de réservation](https://www.justwords.ai/book-demo) ou via le canal Slack partagé.
{% endalert %}

## Conditions préalables

| Condition | Description |
|---|---|
| Compte des mots justes | Un compte [Just Words](https://www.justwords.ai/) est nécessaire pour bénéficier de ce partenariat. Si vous n'avez pas de compte Just Words, [planifiez un appel d'onboarding de 30 minutes.](https://www.justwords.ai/book-demo) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration de Just Words avec Braze

### Étape 1 : Créez un modèle de mots justes

1. Allez dans votre console Just Words et [créez un nouveau modèle](https://console.justwords.ai/new).
2. Choisissez un ID facile à mémoriser, composé uniquement de lettres, de chiffres et de traits de soulignement.
3. Complétez les informations de base sur la campagne.
4. Utilisez l'intelligence artificielle pour générer des personnalisations.

![La plateforme de création de modèles Just Words.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### Étape 2 : Créer une clé API pour Just Words

1. Allez dans **Org Settings** > **API Keys** > **Generate API Key.**
2. Copiez et enregistrez la clé API dans un emplacement/localisation sécurisé.

![Le formulaire de la clé API de Just Words.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### Étape 3 : Utilisez les mots justes dans votre contenu Braze

Just Words fonctionne avec des canevas et des campagnes en utilisant le contenu connecté. Si vous créez un canvas, chaque étape du canvas doit correspondre à un modèle unique de Just Words.

#### Étape 3.1 : Mettez en place votre test A/B

{% tabs %}
{% tab Canvas %}

1. Dans un Canvas, sélectionnez **Ajouter une variante** > **Ajouter une variante** jusqu'à ce que vous ayez le nombre de variantes souhaité, et ajoutez des étapes à chaque variante (comme une étape d'envoi d'e-mail).
2. Répartissez le trafic de l'audience comme vous le souhaitez. Par exemple, si vous avez deux variantes, vous pouvez donner à chacune 50 %. Vous pouvez aussi avoir deux variantes de 40 % chacune et un groupe de contrôle de 20 %. Pour plus d'informations sur les tests A/B pour les toiles, reportez-vous à la section [Création d'une toile.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
3. Dans les compositeurs des étapes du message que vous souhaitez utiliser avec le contenu connecté, collez l'extrait de contenu connecté de la console Just Words, tel que l'extrait suivant.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Configuration du test A/B Canvas de Braze.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campagne %}

1. Dans l'étape **Composer des messages de** votre campagne, créez deux variantes.
2. À l'étape **Audience cible**, accédez à la section **Test A/B** et modifiez les pourcentages d'utilisateurs qui recevront chacune de vos variantes (et votre groupe de contrôle facultatif). Vous pouvez personnaliser davantage votre test en sélectionnant une option d'optimisation. Pour plus d'informations sur les tests A/B pour les campagnes, reportez-vous à la section [Création de tests multivariés et de tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. Dans le compositeur de message, collez l'extrait de contenu connecté de la console Just Words, comme l'extrait suivant.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Étape 3.2 :  Ajoutez de la personnalisation avec des attributs personnalisés (facultatif)

Pour personnaliser vos messages avec des attributs personnalisés (tels que `industry`), utilisez le format Liquid suivant :

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Notez que l'attribut personnalisé de `industry` est indiqué par {% raw %}```&attrs.industry={{ custom_attribute.industry }}```{% endraw %}. 

![Braze Liquid logic in an HTML message composer.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### Étape 4 : Prévisualiser l'e-mail

Veillez à prévisualiser l'e-mail dans Braze pour confirmer que le contenu personnalisé s'affiche correctement.

![Prévisualisation de l'envoi de messages de Braze pour un e-mail de Just Words.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### Étape 5 : Mettre en place des Braze Currents

Braze Currents permet de suivre et d'optimiser les performances au fil du temps.

1. Dans Braze, allez dans **Intégrations partenaires** > **Exportation de données**.
2. Sélectionnez **Créer un nouveau test courant**, puis sélectionnez **Tester l'exportation de données Amazon S3**.

![Le menu déroulant "Create New Test Current" avec l'option "Test Amazon S3 Data Export".]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3\. Saisissez l'ID d'accès S3, la clé d'accès secrète AWS, le nom du compartiment et le dossier qui ont été fournis par Just Words lors de l'onboarding.

![Section "Credentials" pour la clé d'accès secrète AWS.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4\. Sélectionnez les événements à suivre, tels que les envois, les ouvertures, les clics, les désabonnements, les conversions et autres.

![La section "événements engagement aux messages" contient des événements à sélectionner.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5\. Lancez le Braze Currents.

Vous êtes prêt ! Vous pouvez désormais utiliser les mots justes avec le contenu connecté de Braze.