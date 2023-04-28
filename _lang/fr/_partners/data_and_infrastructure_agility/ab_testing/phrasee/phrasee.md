---
nav_title: Phrasee
article_title: Phrasee
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et Phrasee, une plateforme d’IA et de linguistique informatique qui vous permet d’améliorer vos expériences client en optimisant la langue utilisée sur l’ensemble du parcours client. Le moteur de deep learning de Phrasee gère les tests, le suivi et la génération d’une nouvelle langue en fonction de ce qu’il apprend."
page_type: partner
search_tag: Partenaire

---

# Phrasee

> [Phrasee][1] rassemble l’intelligence artificielle, la linguistique informatique et un esprit axé sur le client pour vous aider à déployer la langue utilisée par votre marque à grande échelle sur des canaux personnalisés en fonction de votre marque.

Le partenariat entre Braze et Phrasee vous permet d’améliorer vos expériences client en optimisant la langue utilisée sur l’ensemble du parcours client. Le moteur de deep learning de Phrasee gère les tests, le suivi et la génération d’une nouvelle copie en fonction de ce qu’il apprend. 

Pour inclure les informations de suivi des clics de vos utilisateurs abonnés, utiliser currents Braze et du Contenu connecté, consultez l’intégration [Phrasee React]({{site.baseurl}}/partners/message_orchestration/ab_testing/phrasee/phrasee_react/) supplémentaire de Phrasee.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Phrasee | Un [compte Phrasee][3] est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `campaigns`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][2]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

Cette intégration vous permet d’intégrer des campagnes de notifications push ou par e-mail dans Phrasee. Ces deux types de campagnes sont abordés dans les étapes suivantes.

{% tabs %}
{% tab Email Campaign %}

### Campagne par e-mail

#### Étape 1 : Configurer votre campagne dans Phrasee pour générer les variantes de votre test de répartition

Configurez votre campagne par e-mail Phrasee comme vous le feriez normalement. Une fois que vous aurez approuvé vos variantes, vous serez redirigé vers la page récapitulative. Vous devrez copier à cet endroit les variantes qui seront ajoutées à votre campagne Braze. Si vous préférez, vous pouvez également cliquer sur le bouton **Download variants (Télécharger les variantes)** pour télécharger un fichier .txt contenant toutes vos variantes.

![Campagne Phrasee montrant les variantes disponibles.]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Étape 2 : Créer votre campagne par e-mail dans Braze

Accédez au tableau de bord de Braze pour créer votre campagne par e-mail. Pendant que vous créez votre campagne, ajoutez la balise **Campagne par e-mail**. Si cette balise n’existe pas encore, créez-la.

![Le générateur d’e-mails de Braze mettant l’accent sur la balise de messagerie qui peut être ajoutée directement sous le champ de description de la campagne.]({% image_buster /assets/img/phrasee/4_braze_emailtag.png %})

Ensuite, cliquez sur **Edit Sending Info (Modifier les informations d’envoi)** pour chaque variante et collez la variante Phrasee dans la ligne d’objet. Assurez-vous qu’il existe le même nombre de variantes entre Phrasee et Braze.

Vous n’aurez pas besoin de créer chaque nouvel e-mail à partir de zéro ; vous pouvez simplement copier la première variante, puis modifier la ligne d’objet pour chaque nouvelle variante.

![Option permettant de copier une variante d’e-mail existante dans Braze.]({% image_buster /assets/img/phrasee/5_copy_variant_braze.png %})

#### Étape 3 : Planifier votre campagne Braze

Planifiez votre campagne pour qu’elle démarre à une heure donnée. Cela peut également être réalisé à l’aide de l’API et de l’[endpoint `campaign/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/). Vous devrez connaître cette heure pour vous connecter à Phrasee.

![Campagne de livraison planifiée et envoyée à une heure donnée.]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Étape 4 : Finaliser la configuration de la campagne Braze

Effectuez les étapes restantes dans Braze pour configurer votre campagne. Sous **A/B Testing (Test A/B)**, cochez la case **Send Winning Variant (Envoyer la variante gagnante)**. Puis, sélectionnez le temps à attendre avant d’envoyer la variante gagnante.

![La partie relative aux tests A/B de la campagne montrant comment les tests A/B et le groupe de contrôle seront divisés. Vous verrez également les paramètres vous permettant de déterminer quelle est la variante gagnante et d’envoyer des informations ainsi que les préférences au cas où le test est négligeable sur le plan statistique.]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

Configurez les autres paramètres si nécessaire et enregistrez votre campagne.

#### Étape 5 : Entrées d’intégration pour Phrasee

Revenez à votre campagne Phrasee et cliquez sur le bouton **Braze integration (Intégration Braze)**.

La fenêtre Planifier une campagne s’affiche. Sélectionnez votre campagne Braze dans la liste déroulante. Ensuite, sélectionnez la date et l’heure auxquelles votre campagne est programmée pour commencer et se terminer. Enfin, saisissez l’heure d’envoi de votre test A/B et enregistrez les détails. Le fuseau horaire de votre compte Braze apparaîtra à côté de la liste déroulante de la campagne pour vous assurer que les heures correspondent entre les applications.

Lancez votre campagne dans Braze, et laissez Phrasee prendre la relève ! Une fois disponibles, les résultats de votre campagne apparaîtront automatiquement dans Phrasee. 

![La plateforme Phrasee affichant la fenêtre Planifier une campagne où vous pouvez ajuster les paramètres d’envoi.]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Assurez-vous que la date et l’heure planifiées correspondent au calendrier configuré dans Braze afin que Phrasee puisse extraire les résultats au bon moment.
{% endalert %}

{% endtab %}
{% tab Push Campaign %}

### Campagne de notification push

#### Étape 1 : Configurer votre campagne de notification push dans Phrasee pour générer les variantes de votre test de répartition

Configurez votre campagne par e-mail Phrasee comme vous le feriez normalement. Une fois que vous aurez approuvé vos variantes, vous serez redirigé vers la page récapitulative. Vous devrez copier à cet endroit les variantes qui seront ajoutées à votre campagne Braze. Si vous préférez, vous pouvez également cliquer sur le bouton **Download variants (Télécharger les variantes)** pour télécharger un fichier .txt contenant toutes vos variantes.

![Campagne Phrasee montrant les variantes disponibles.]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Étape 2 : Configurer votre campagne de notification push dans Braze

L’intégration de Phrasee vous permet de sélectionner une campagne de notification push iOS et Android de Braze pour l’intégrer dans une campagne Phrasee si nécessaire. Pour activer cette fonctionnalité, assurez-vous d’ajouter la balise **Campagne de notification push**. Cela est requis pour l’étape 4.

![Le générateur d’e-mails de Braze mettant l’accent sur la balise de messagerie qui peut être ajoutée directement sous le champ de description de la campagne.]({% image_buster /assets/img/phrasee/9_braze_push_tag.png %})

#### Étape 3 : Copier les variantes de Phrasee dans Braze

{% alert important %} 
Pour que Phrasee tire automatiquement les résultats des variantes de votre campagne de notifications push, le texte de la variante doit être contenu dans le corps du message, et non dans le « titre ».
{% endalert %}

Un modèle de langue Phrasee peut générer des variantes à deux lignes réparties entre le « titre » et le « message ». Assurez-vous que la deuxième ligne est incluse dans le corps du message pour que Phrasee puisse automatiquement extraire les résultats des variantes de votre campagne.

![Exemple de modèle de langue divisé en deux lignes de Phrasee présenté dans l’éditeur de messages de Braze.]({% image_buster /assets/img/phrasee/10_push_two_lines.png %})

Vous pouvez également saisir la variante Phrasee dans le **Corps du message** pour que les résultats soient correctement extraits dans Phrasee. Dans ce cas, le « titre » doit rester constant pour toutes les variantes afin de garantir un test précis.

![Un exemple de ce à quoi la variante Phrasee peut ressembler si vous ajoutez toute la variante dans le corps du message.]({% image_buster /assets/img/phrasee/11_push_messagebody.png %})

#### Étape 4 : Planifier votre campagne Braze

Planifiez votre campagne pour qu’elle démarre à une heure donnée. Cela peut également être réalisé à l’aide de l’API et de l’[endpoint `campaign/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/). Vous devrez connaître cette heure pour vous connecter à Phrasee.

![Campagne de livraison planifiée et envoyée à une heure donnée.]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Étape 5 : Finaliser la configuration de la campagne Braze

Effectuez les étapes restantes dans Braze pour configurer votre campagne. Sous **A/B Testing (Test A/B)**, cochez la case **Send Winning Variant (Envoyer la variante gagnante)**. Puis, sélectionnez le temps à attendre avant d’envoyer la variante gagnante.

![La partie relative aux tests A/B d’une campagne montrant comment les tests A/B et le groupe de contrôle seront divisés. Vous verrez également les paramètres vous permettant de déterminer quelle est la variante gagnante et d’envoyer des informations ainsi que les préférences au cas où le test est négligeable sur le plan statistique.]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

Configurez les autres paramètres si nécessaire et enregistrez votre campagne.

#### Étape 6 : Entrées d’intégration pour Phrasee

Revenez à votre campagne Phrasee et cliquez sur le bouton **Braze integration (Intégration Braze)**.

La fenêtre Planifier une campagne s’affiche. Sélectionnez votre campagne Braze dans la liste déroulante. Ensuite, sélectionnez la date et l’heure auxquelles votre campagne est programmée pour commencer et se terminer. Enfin, saisissez l’heure d’envoi de votre test A/B et enregistrez les détails. Le fuseau horaire de votre compte Braze apparaîtra à côté de la liste déroulante de la campagne pour vous assurer que les heures correspondent entre les applications.

Lancez votre campagne dans Braze, et laissez Phrasee prendre la relève ! Une fois disponibles, les résultats de votre campagne apparaîtront automatiquement dans Phrasee. 

![La fenêtre Planifier une campagne de la plateforme Phrasee où vous pouvez ajuster les paramètres d’envoi.]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Assurez-vous que la date et l’heure planifiées correspondent au calendrier configuré dans Braze afin que Phrasee puisse extraire les résultats au bon moment.
{% endalert %}

{% endtab %}
{% endtabs %}

[1]: https://phrasee.co/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: mailto:awesome@phrasee.co
[4]: {% image_buster /assets/img/phrasee/1_create_apikey.png %}
[5]: {% image_buster /assets/img/phrasee/2_campaignaccess.png %}