---
nav_title: Phrasee
article_title: Phrasee
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Phrasee, une plateforme d'AI et de linguistique informatique qui vous permet de déployer le langage de marque, à l'échelle, à travers les canaux qui sont personnalisés pour la voix de votre marque. Le moteur d’apprentissage approfondi de Phrasee gère les tests, surveille les résultats et génère un nouveau langage basé sur ce qu’il a appris."
alias: /fr/partners/phrase/
page_type: partenaire
search_tag: Partenaire
---

# Phrasee

> Améliorez l'expérience client en optimisant le langage utilisé tout au long du voyage client. La plateforme [Phrasee][1] regroupe l'intelligence artificielle, la linguistique informatique, et un esprit de centralisation du client en tant que seul fournisseur de ce genre à générer, optimiser, automatiser et analyser le langage en temps réel. Laissez-nous gérer le contenu minutiae pendant que votre équipe se concentre sur la grande image.

L'engagement de la clientèle de Braze développe des relations par le biais du marketing multicanal. En collaboration avec Phrasee, Braze peut déployer le langage de la marque, à l'échelle de tous les canaux qui sont personnalisés pour la voix de votre marque. Le moteur d’apprentissage approfondi de Phrasee gère les tests, surveille les résultats et génère un nouveau langage basé sur ce qu’il a appris.

## Exigences

| Exigences                       | Origine | Libellé                                                                                                                                                                                |
| ------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API Braze                   | Brasero | Vous devrez créer une nouvelle clé d'API.<br>Ceci peut être créé dans la console développeur -> Paramètres API -> **Créer une nouvelle clé API avec les permissions Campaigns**. |
| Point de terminaison REST Braze | Brasero | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL Braze pour [votre instance][2].                                                                            |
| Compte Phrasee                  | Phrasee | Contactez [Phrasee][3] pour vous inscrire.                                                                                                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration du serveur à serveur

Phrasee requiert les détails de l'application du serveur à serveur pour vérifier les résultats de Braze tant que vous n'êtes pas connecté.

### Créer une nouvelle clé API Braze Phrasee

Naviguez vers la console développeur dans Braze et cliquez sur __Créer une nouvelle clé API__.

!\[api_key\]\[4\]

Cette clé API ne nécessitera que l'accès aux **Campagnes**.

!\[campaigns\]\[5\]

Enregistrez et partagez cette clé API avec votre point de terminaison Braze REST avec Phrasee afin que nous puissions compléter l'intégration et lier vos campagnes.

## Utiliser cette intégration

Avec cette intégration, vous pouvez intégrer des campagnes de courriel ou de push dans Phrasee. Les étapes sont détaillées ci-dessous pour les deux.

{% tabs %}
{% tab Email Campaign %}

### Campagne de courrier électronique

#### Étape 1 : Configurez votre campagne dans Phrasee pour générer les variantes de votre test fractionné

Configurez votre campagne d'email Phrasee comme vous le feriez normalement. Une fois que vous avez approuvé vos variantes, vous serez alors dirigé vers la page de récapitulatif. Ici, vous devrez copier les variantes qui seront ajoutées à votre campagne de Braze. Si vous préférez, vous pouvez également cliquer sur le bouton **Télécharger les variantes** pour télécharger un fichier .txt contenant toutes vos variantes.

![phrasee_campaign]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Étape 2 : Créez votre campagne d'email Braze

Naviguez vers le tableau de bord de Braze pour créer votre campagne e-mail. Lors de la création de votre campagne, ajoutez le tag __Campagne d'email__. Si cette balise n'existe pas encore, créez-la.

![Étiquette]({% image_buster /assets/img/phrasee/4_braze_emailtag.png %})

Ensuite, pour chaque variante, cliquez sur __Modifier les infos d'envoi__ pour coller la variante Phrasee dans la ligne de sujet. **Assurez-vous que le nombre de variantes correspondent entre Phrasee et Braze.**

Veuillez noter que vous n'aurez pas besoin de recréer chaque email à partir de zéro, vous pouvez simplement copier la première variante et ensuite éditer la ligne de sujet pour chaque nouvelle variante.

![copier_variante]({% image_buster /assets/img/phrasee/5_copy_variant_braze.png %})

#### Étape 3 : Planifiez votre campagne de Braze

Planifiez votre campagne pour qu'elle commence à un moment précis. __Vous aurez besoin de savoir cette fois pour vous connecter à Phrasee.__

![format@@0 schedule_braze]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Étape 4 : Finaliser la configuration de la campagne Braze

Complétez les étapes restantes de Braze pour mettre en place votre campagne. Cochez la case pour envoyer la variante gagnante. Sélectionnez ensuite le temps d'attente avant d'envoyer la Variante gagnante.

![Envoyer au gagnant]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

Finalisez tous les autres paramètres au besoin et enregistrez votre campagne.

#### Étape 5 : entrées d'intégration de Phrasee

Retournez à votre campagne Phrasee et cliquez sur le bouton __Intégration de Braze__.

La fenêtre d'intégration apparaîtra :
1. Sélectionnez votre campagne Braze dans la liste déroulante.
2. Sélectionnez la date et l'heure de début de votre campagne Braze. Le fuseau horaire de votre compte Braze apparaîtra sous la liste déroulante de la campagne pour s'assurer que les temps s'alignent entre les applications.
3. Sélectionnez la date et l'heure à laquelle votre test Braze A/B est programmé.
4. Sélectionnez la date et l'heure à laquelle votre campagne Braze se terminera. C'est la date à laquelle les résultats finaux seront tirés dans le système Phrasee.
6. Enregistrez les détails.

![tiroir de phrase]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Assurez-vous que votre date et heure programmées correspondent à ce qui a été configuré dans Braze afin que Phrasee tire dans les résultats à la bonne heure.
{% endalert %}

Lancez votre campagne à Braze et Phrasee l'a à partir d'ici! Lorsque les résultats des tests de votre campagne sont entrés, ils apparaîtront automatiquement dans Phrasee.

{% endtab %}
{% tab Push Campaign %}

### Campagnes push

#### Étape 1 : Configurez votre campagne de push dans Phrasee pour générer les variantes de votre test fractionné

Configurez votre campagne de push Phrasee comme vous le feriez normalement. Une fois que vous avez approuvé vos variantes, vous serez alors dirigé vers la page de récapitulatif. Ici, vous devrez copier les variantes qui seront ajoutées à votre campagne de Braze. Si vous préférez, vous pouvez également cliquer sur le bouton **Télécharger les variantes** pour télécharger un fichier .txt contenant toutes vos variantes.

![phrasee_campaign]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Étape 2 : Configurez votre campagne Braze push

L'intégration de Phrasee vous permettra de sélectionner à la fois une campagne iOS et une campagne de push Android Braze pour s'intégrer dans une campagne Phrasee si nécessaire. Pour activer cette fonctionnalité, lors de la création de votre campagne de push en Brésil, assurez-vous de la taguer __Campagne Push__ (comme vu ci-dessous). __Ceci est demandé pour l'étape 4.__

![Étiquette Pousse]({% image_buster /assets/img/phrasee/9_braze_push_tag.png %})

#### Étape 3 : Copiez les variantes de Phrasee dans Braze

{% alert important %}
Pour que Phrasee tire automatiquement les résultats des variantes dans votre campagne de push, le texte de la variante doit être contenu dans le corps du message et non dans le titre.
{% endalert %}

Avec un modèle de langage Phrasee, il est capable de générer deux variantes de lignes qui peuvent être divisées entre le « Titre » et le « Message ». Assurez-vous que la deuxième ligne est incluse dans le corps du message, de cette façon, Phrasee peut automatiquement tirer les résultats des variantes dans votre campagne.

![format@@0 push_twolines]({% image_buster /assets/img/phrasee/10_push_two_lines.png %})

Vous pouvez également entrer toute la variante Phrasee dans le corps du message **** pour que les résultats soient correctement tirés dans Phrasee. __Dans cette instance, le 'titre' doit rester constant sur toutes les variantes pour assurer un test précis.__

![format@@0 push_oneline]({% image_buster /assets/img/phrasee/11_push_messagebody.png %})

#### Étape 4 : Planifiez votre campagne Braze

Planifiez votre campagne pour qu'elle commence à un moment précis. __Vous aurez besoin de savoir cette fois pour vous connecter à Phrasee.__

![format@@0 schedule_braze]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Étape 5 : Finaliser la configuration de la campagne Braze

Complétez les étapes restantes de Braze pour mettre en place votre campagne. Cochez la case pour __Envoyer la variante gagnante__. Sélectionnez ensuite le temps d'attente avant d'envoyer la Variante gagnante.

![Envoyer au gagnant]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

#### Étape 6 : entrées d'intégration de Phrasee

Retournez à votre campagne Phrasee et cliquez sur le bouton __Intégration de Braze__.

La fenêtre d'intégration apparaîtra :
1. Sélectionnez vos campagnes Braze dans la liste déroulante.
2. Sélectionnez la date et l'heure de début de votre campagne Braze. Le fuseau horaire de votre compte Braze apparaîtra sous la liste déroulante de la campagne pour s'assurer que les temps s'alignent entre les applications.
3. Sélectionnez la date et l'heure à laquelle votre test Braze A/B est programmé.
4. Sélectionnez la date et l'heure à laquelle votre campagne Braze se terminera. C'est la date à laquelle les résultats finaux seront tirés dans le système Phrasee.
6. Enregistrez les détails.

![tiroir de phrase]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Assurez-vous que la date et l'heure que vous avez planifiées correspondent à ce que vous avez configuré dans Braze afin que Phrasee tire dans les résultats à la bonne heure.
{% endalert %}

Lancez votre campagne à Braze et Phrasee l'a à partir d'ici! Lorsque les résultats des tests de votre campagne sont entrés, ils apparaîtront automatiquement dans Phrasee.

{% endtab %}
{% endtabs %}
[4]: {% image_buster /assets/img/phrasee/1_create_apikey.png %} [5]: {% image_buster /assets/img/phrasee/2_campaignaccess.png %}

[1]: https://phrasee.co/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: mailto:awesome@phrasee.co
