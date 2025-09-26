---
nav_title: "Personnaliser l'URL"
article_title: "Personnaliser les URL des pages d'atterrissage"
description: "Découvrez comment personnaliser les URL de vos pages de destination avec la marque de votre entreprise, en connectant votre domaine à votre espace de travail Braze."
page_order: 1
---

# Personnaliser les URL des pages d'atterrissage

> Découvrez comment personnaliser les URL de vos pages de destination avec la marque de votre entreprise, en connectant votre domaine à votre espace de travail Braze.

## Fonctionnement

Lorsque vous [connectez votre domaine à Braze](#connecting-your-domain-to-braze), il sera utilisé comme domaine par défaut pour toutes les pages de destination. Par exemple, si vous connectez le sous-domaine `forms.example.com`, l'URL de votre page d'atterrissage sera désormais `forms.example.com/holiday-sale`.

Le nombre de domaines personnalisés que vous pouvez connecter à votre compte Braze dépend de votre [niveau d'abonnement]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers). Pour augmenter votre limite, contactez votre gestionnaire de compte Braze.

## Connecter votre domaine à Braze

Pour connecter un domaine à votre compte Braze, demandez à un administrateur de suivre les étapes ci-dessous.

1. Allez dans **Paramètres** > **Paramètres de la page d'atterrissage**.
2. Saisissez le domaine auquel vous souhaitez vous connecter et sélectionnez **Soumettre**. Par exemple, `forms.example.com`.
3. Copiez et collez les enregistrements **TXT** et **CNAME** dans les paramètres DNS de votre fournisseur de domaine.
4. Retournez au tableau de bord de Braze pour vérifier la connexion.

![Page de configuration de la page d'atterrissage avec un enregistrement TXT et deux enregistrements CNAME répertoriés avec leurs noms et valeurs respectifs.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Selon votre fournisseur de domaine, la connexion peut prendre jusqu'à 48 heures. Une fois le processus terminé, nous commencerons à utiliser votre domaine personnalisé pour vos pages de destination dans le tableau de bord de Braze.
{% endalert %}

## Suppression de votre domaine

Si vous êtes administrateur de Braze, vous pouvez supprimer un domaine précédemment configuré en suivant les étapes suivantes :

1. Allez dans **Paramètres** > **Paramètres de la page d'atterrissage**.
2. Sélectionnez **Supprimer le domaine personnalisé**.
3. Confirmez la suppression du domaine.
4. Supprimez les enregistrements DNS listés de vos paramètres de domaine.

{% alert important %}
Lorsque vous supprimez un domaine personnalisé, cette URL n'est plus valide. Toutes les pages de destination qui utilisaient ce domaine reviendront automatiquement au domaine par défaut défini par Braze.
{% endalert %}


## Ressources DNS

Vous trouverez ci-dessous des ressources pour créer et gérer des enregistrements DNS avec les fournisseurs de domaines les plus courants. Si vous utilisez un autre fournisseur, reportez-vous à sa documentation ou contactez son équipe d'assistance pour obtenir des informations.

| Fournisseur de domaine | Ressources |
| --- | --- |
| Bluehost | [Les enregistrements DNS expliqués](https://my.bluehost.com/hosting/help/508)<br> [Gestion DNS Ajouter, modifier ou supprimer des entrées DNS](https://my.bluehost.com/hosting/help/559) |
| Dreamhost | [Comment ajouter des enregistrements DNS personnalisés ?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [Ajouter un enregistrement CNAME](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| Cloudflare | [Gérer les enregistrements DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Squarespace | [Ajout de paramètres DNS personnalisés](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Résolution des problèmes 

### Ma connexion au domaine a échoué

Vérifiez que votre domaine a été saisi correctement et qu'il correspond à ce que vous avez soumis à Braze à partir de votre compte de fournisseur de domaine. S'il est correct et correspond, vérifiez les enregistrements TXT et CNAME fournis par Braze. Ils doivent correspondre aux enregistrements que vous avez saisis dans le compte de votre fournisseur de domaine.

## Foire aux questions

### Puis-je connecter plusieurs sous-domaines à mon espace de travail ou connecter un sous-domaine à plusieurs espaces de travail ?

Non, vous ne pouvez actuellement connecter qu'un seul sous-domaine à un espace de travail.

### Puis-je utiliser le même sous-domaine que celui que j'utilise actuellement pour mon site web principal ou mon domaine d'envoi ?

Non, vous ne pouvez pas utiliser des sous-domaines déjà utilisés. Bien que ces sous-domaines soient valides, ils ne peuvent pas être utilisés pour les pages de destination s'ils sont déjà affectés à d'autres fins ou s'ils ont des enregistrements DNS qui entrent en conflit avec les enregistrements CNAME requis.

