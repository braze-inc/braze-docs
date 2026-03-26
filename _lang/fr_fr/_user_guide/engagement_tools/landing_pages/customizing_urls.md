---
nav_title: "Personnaliser l'URL"
article_title: "Personnaliser les URL des pages d'atterrissage"
description: "Découvrez comment personnaliser les URL de vos pages d'atterrissage avec la marque de votre entreprise, en connectant votre domaine à votre espace de travail Braze."
page_order: 1
---

# Personnaliser les URL des pages d'atterrissage

> Découvrez comment personnaliser les URL de vos pages d'atterrissage avec la marque de votre entreprise en connectant votre domaine à votre espace de travail Braze.

## Fonctionnement

Lorsque vous [connectez votre domaine à Braze](#connect-your-domain-to-braze), il est utilisé comme domaine par défaut pour toutes les pages d'atterrissage. Par exemple, si vous connectez le sous-domaine `forms.example.com`, les URL de vos pages d'atterrissage prendront la forme `forms.example.com/holiday-sale`.

Le nombre de domaines personnalisés que vous pouvez connecter à votre compte Braze dépend de votre [niveau d'abonnement]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers). Pour augmenter votre limite, contactez votre Account Manager Braze.

## Connecter votre domaine à Braze {#connect-your-domain-to-braze}

Pour connecter un domaine à votre compte Braze, demandez à un administrateur de suivre les étapes ci-dessous.

1. Allez dans **Paramètres** > **Paramètres de la Page d'atterrissage**.
2. Saisissez le domaine que vous souhaitez connecter et sélectionnez **Envoyer**. Par exemple, `forms.example.com`.
3. Copiez et collez les enregistrements **TXT** et **CNAME** dans les paramètres dns de votre fournisseur de domaine.
4. Retournez au tableau de bord de Braze pour vérifier la connexion.

![Page des paramètres de la Page d'atterrissage avec un enregistrement TXT et deux enregistrements CNAME répertoriés avec leurs noms et valeurs respectifs.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Selon votre fournisseur de domaine, la connexion peut prendre jusqu'à 48 heures. Une fois le processus terminé, votre domaine personnalisé sera utilisé pour vos pages d'atterrissage dans le tableau de bord de Braze.
{% endalert %}

## Supprimer votre domaine

Si vous êtes administrateur de Braze, vous pouvez supprimer un domaine précédemment configuré en suivant les étapes suivantes :

1. Allez dans **Paramètres** > **Paramètres de la Page d'atterrissage**.
2. Sélectionnez **Supprimer le domaine personnalisé**.
3. Confirmez la suppression du domaine.
4. Supprimez les enregistrements dns listés de vos paramètres de domaine.

{% alert important %}
Lorsque vous supprimez un domaine personnalisé, l'URL correspondante n'est plus valide. Toutes les pages d'atterrissage qui utilisaient ce domaine reviendront automatiquement au domaine par défaut défini par Braze.
{% endalert %}

## Migrer votre domaine

Pour migrer un domaine personnalisé vers un autre espace de travail :

1. Supprimez le domaine personnalisé.
2. Créez un nouveau domaine personnalisé dans l'espace de travail souhaité.
3. Reconfigurez le domaine personnalisé avec les nouveaux enregistrements dns. Notez que votre sous-domaine sera indisponible pendant cette opération.

## Ressources dns

{% multi_lang_include dns_records.md %}

## Résolution des problèmes

### Ma connexion au domaine a échoué

Vérifiez que votre domaine a été saisi correctement et qu'il correspond à ce que vous avez soumis à Braze depuis votre compte de fournisseur de domaine. Si c'est le cas, vérifiez les enregistrements TXT et CNAME fournis par Braze. Ils doivent correspondre aux enregistrements que vous avez saisis dans le compte de votre fournisseur de domaine.

## Foire aux questions

### Puis-je connecter plusieurs sous-domaines à mon espace de travail ou connecter un sous-domaine à plusieurs espaces de travail ?

Non, vous ne pouvez actuellement connecter qu'un seul sous-domaine à un espace de travail.

### Puis-je utiliser le même sous-domaine que celui que j'utilise actuellement pour mon site web principal ou mon domaine d'envoi ?

Non, vous ne pouvez pas utiliser des sous-domaines déjà utilisés. Bien que ces sous-domaines soient valides, ils ne peuvent pas être utilisés pour les pages d'atterrissage s'ils sont déjà affectés à d'autres fins ou s'ils ont des enregistrements dns qui entrent en conflit avec les enregistrements CNAME requis.

### Pourquoi mon domaine personnalisé est-il bloqué sur « Connexion » malgré des enregistrements dns valides ?

Si votre domaine personnalisé indique que tous les enregistrements dns sont « Connecté », mais que l'état du domaine reste sur « Connexion » pendant plus de quatre heures, il se peut que votre organisation utilise des enregistrements CAA (Certificate Authority Authorization) ou des mises en attente de zone Cloudflare qui empêchent Braze de sécuriser votre page.

#### Enregistrements CAA

Les enregistrements CAA limitent les autorités de certification autorisées à émettre des certificats SSL pour votre domaine. Si vos enregistrements CAA n'incluent pas LetsEncrypt, Braze (par l'intermédiaire de Cloudflare) ne peut pas émettre le certificat SSL requis.

Pour résoudre ce problème, demandez à votre équipe informatique d'ajouter un enregistrement CAA à votre sous-domaine avec les valeurs suivantes :
- **Type d'enregistrement :** CAA
- **Valeur :** `0 issue "letsencrypt.org"`

Pour plus d'informations, consultez la [documentation CAA de LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### Mises en attente de zone Cloudflare

Si votre organisation utilise Cloudflare, une fonctionnalité de sécurité de mise en attente de zone peut empêcher Braze de créer votre domaine personnalisé.

Pour résoudre ce problème, demandez à votre équipe informatique de libérer temporairement la mise en attente de la zone. Pour plus d'informations, consultez la [documentation de Cloudflare sur les mises en attente de zone](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Redémarrer le processus de validation

Après avoir résolu l'un ou l'autre problème, supprimez et recréez votre domaine personnalisé dans le tableau de bord de Braze pour redémarrer le processus de validation.