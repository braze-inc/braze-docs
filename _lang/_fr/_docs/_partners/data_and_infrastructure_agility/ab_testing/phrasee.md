---
nav_title: Phrasee
article_title: Phrasee
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Phrasee, une plateforme de linguistique informatique et IA qui vous permet d'améliorer l'expérience client en optimisant le langage utilisé tout au long du voyage client. Le moteur d'apprentissage approfondi de Phrasee gère les tests, la surveillance et la génération d'un nouveau langage basé sur ce qu'il apprend."
alias: /fr/partners/phrase/
page_type: partenaire
search_tag: Partenaire
---

# Phrasee

> [Phrasee][1] rassemble l'intelligence artificielle, la linguistique computationnelle, et un esprit de centralisation du client pour aider à déployer le langage de la marque, à l'échelle de tous les canaux qui sont personnalisés à la voix de votre marque.

Le partenariat Braze et Phrasee vous permet d'améliorer l'expérience client en optimisant le langage utilisé tout au long du voyage client. Le moteur d'apprentissage approfondi de Phrasee gère les tests, la surveillance et la génération de nouvelles copies en fonction de ce qu'il apprend.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Phrasee                  | Un [compte Phrasee][3] est requis pour profiter de ce partenariat.                                                                                                                                         |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `campagnes`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API** |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][2].                                                                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

Avec cette intégration, vous pouvez intégrer des campagnes de courriel ou de push dans Phrasee. Les étapes sont détaillées ci-dessous pour les deux.

{% tabs %}
{% tab Email Campaign %}

### Campagne de courrier électronique

#### Étape 1 : Configurez votre campagne dans Phrasee pour générer les variantes de votre test fractionné

Configurez votre campagne d'email Phrasee comme vous le feriez habituellement. Une fois que vous aurez approuvé vos variantes, vous serez redirigé vers la page récapitulative. Ici, vous devrez copier les variantes qui seront ajoutées à votre campagne de Braze. Si vous préférez, vous pouvez également cliquer sur le bouton **Télécharger les variantes** pour télécharger un fichier .txt contenant toutes vos variantes.

![Campagne Phrasee]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Étape 2 : Créez votre campagne d'email Braze

Naviguez vers le tableau de bord de Braze pour créer votre campagne e-mail. Lors de la création de votre campagne, ajoutez le tag **Campagne d'email**. Si cette balise n'existe pas encore, créez-la.

![Phrasee email tag]({% image_buster /assets/img/phrasee/4_braze_emailtag.png %})

Ensuite, cliquez sur **Modifier les infos d'envoi** pour chaque variante pour coller la variante Phrasee dans la ligne d'objet. Assurez-vous que le nombre de variantes correspondent entre Phrasee et Braze.

Vous n'aurez pas besoin de recréer chaque email à partir de zéro ; vous pouvez simplement copier la première variante et ensuite éditer la ligne de sujet pour chaque nouvelle variante.

![Variante de copie par Phrasee]({% image_buster /assets/img/phrasee/5_copy_variant_braze.png %})

#### Étape 3 : Planifiez votre campagne de Braze

Planifiez votre campagne pour qu'elle commence à un moment précis. Vous aurez besoin de savoir cette fois pour vous connecter à Phrasee.

![Horaire de Phrasee Braze]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Étape 4 : Finaliser la configuration de la campagne Braze

Complétez les étapes restantes de Braze pour mettre en place votre campagne. Sous le **test A/B**, cochez la case **Envoyer la variante gagnante**. Sélectionnez ensuite le temps d'attente avant d'envoyer la variante gagnante.

![Vainqueur d'envoi par Phrasee]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

Finalisez tous les autres paramètres au besoin et enregistrez votre campagne.

#### Étape 5 : entrées d'intégration de Phrasee

Retournez à votre campagne Phrasee et cliquez sur le bouton **Intégration de Braze**.

La fenêtre de campagne du calendrier apparaîtra. Ici, sélectionnez votre campagne Braze dans la liste déroulante. Ensuite, sélectionnez la date et l'heure de début et de fin de votre campagne. Enfin, saisissez l'heure d'envoi prévue pour que votre test A/B soit terminé, et enregistrez les détails. Le fuseau horaire de votre compte Braze apparaîtra sous la liste déroulante de la campagne pour s'assurer que les temps s'alignent entre les applications.

Lancez votre campagne au Brésil, et Phrasee l'a à partir d'ici! Lorsque les résultats des tests de votre campagne sont entrés, ils apparaîtront automatiquement dans Phrasee.

![Campagnes de planification Phrasee]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Assurez-vous que votre horaire de match de Braze est configuré pour que Phrasee tire les résultats à la bonne heure.
{% endalert %}

{% endtab %}
{% tab Push Campaign %}

### Campagnes push

#### Étape 1 : Configurez votre campagne de push dans Phrasee pour générer les variantes de votre test fractionné

Configurez votre campagne d'email Phrasee comme vous le feriez habituellement. Une fois que vous aurez approuvé vos variantes, vous serez redirigé vers la page récapitulative. Ici, vous devrez copier les variantes qui seront ajoutées à votre campagne de Braze. Si vous préférez, vous pouvez également cliquer sur le bouton **Télécharger les variantes** pour télécharger un fichier .txt contenant toutes vos variantes.

![Campagne Phrasee]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Étape 2 : Configurez votre campagne Braze push

L'intégration de Phrasee vous permettra de sélectionner à la fois une campagne iOS et une campagne de push Android Braze pour s'intégrer dans une campagne Phrasee si nécessaire. Pour activer cette fonctionnalité, assurez-vous de la taguer **Campagne Push**. Ceci est requis pour l'étape 4.

![Balise Phrasee]({% image_buster /assets/img/phrasee/9_braze_push_tag.png %})

#### Étape 3 : Copiez les variantes de Phrasee dans Braze

{% alert important %}
Pour que Phrasee tire automatiquement les résultats des variantes dans votre campagne de push, le texte de la variante doit être contenu dans le corps du message et non dans le titre.
{% endalert %}

Un modèle de langage Phrasee peut générer des variantes à deux lignes séparées entre le « Titre » et le « Message ». Assurez-vous que la deuxième ligne est incluse dans le corps du message ; de cette façon, Phrasee peut automatiquement tirer les résultats des variantes dans votre campagne.

![Phrasee deux lignes]({% image_buster /assets/img/phrasee/10_push_two_lines.png %})

Vous pouvez également entrer toute la variante Phrasee dans le corps du message **** pour que les résultats soient correctement tirés dans Phrasee. Dans ce cas, le « Titre » doit rester constant pour toutes les variantes afin d’assurer un test précis.

![format@@0 push_oneline]({% image_buster /assets/img/phrasee/11_push_messagebody.png %})

#### Étape 4 : Planifiez votre campagne Braze

Planifiez votre campagne pour qu'elle commence à un moment précis. Vous aurez besoin de savoir cette fois pour vous connecter à Phrasee.

![Horaire de Phrasee Braze]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Étape 5 : Finaliser la configuration de la campagne Braze

Complétez les étapes restantes de Braze pour mettre en place votre campagne. Sous le **test A/B**, cochez la case **Envoyer la variante gagnante**. Sélectionnez ensuite le temps d'attente avant d'envoyer la variante gagnante.

![Vainqueur d'envoi par Phrasee]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

Finalisez tous les autres paramètres au besoin et enregistrez votre campagne.

#### Étape 6 : entrées d'intégration de Phrasee

Retournez à votre campagne Phrasee et cliquez sur le bouton **Intégration de Braze**.

La fenêtre de campagne du calendrier apparaîtra. Ici, sélectionnez votre campagne Braze dans la liste déroulante. Ensuite, sélectionnez la date et l'heure de début et de fin de votre campagne. Enfin, saisissez l'heure d'envoi prévue pour que votre test A/B soit terminé, et enregistrez les détails. Le fuseau horaire de votre compte Braze apparaîtra sous la liste déroulante de la campagne pour s'assurer que les temps s'alignent entre les applications.

Lancez votre campagne au Brésil, et Phrasee l'a à partir d'ici! Lorsque les résultats des tests de votre campagne sont entrés, ils apparaîtront automatiquement dans Phrasee.

![Campagnes de planification Phrasee]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Assurez-vous que votre horaire de match de Braze est configuré pour que Phrasee tire les résultats à la bonne heure.
{% endalert %}

{% endtab %}
{% endtabs %}
[4]: {% image_buster /assets/img/phrasee/1_create_apikey.png %} [5]: {% image_buster /assets/img/phrasee/2_campaignaccess.png %}

[1]: https://phrasee.co/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: mailto:awesome@phrasee.co