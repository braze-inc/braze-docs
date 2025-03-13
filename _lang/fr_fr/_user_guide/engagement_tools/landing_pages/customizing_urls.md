---
nav\_title : Personnalisation de l'URL article\_title : Personnalisation de la description des URL des pages d'atterrissage : "Apprenez à personnaliser les URL de vos pages de destination avec la marque de votre entreprise, en connectant votre domaine à votre espace de travail Braze" page\_order : 1
---

# Personnaliser les URL des pages d'atterrissage

> Découvrez comment personnaliser les URL de vos pages de destination avec la marque de votre entreprise, en connectant votre domaine à votre espace de travail Braze.

## Fonctionnement

Lorsque vous [connectez votre domaine à Braze](#connecting-your-domain-to-braze), il sera utilisé comme domaine par défaut pour toutes les pages de destination. Par exemple, si vous connectez le sous-domaine `forms.example.com`, les URL de votre page d'atterrissage seront désormais `forms.example.com/holiday-sale`.

{% alert note %} La suppression des domaines personnalisés sera bientôt disponible. Contactez votre gestionnaire de satisfaction client si vous avez besoin de supprimer votre domaine. {% endalert %}

## Connecter votre domaine à Braze

Pour connecter un domaine à votre compte Braze, demandez à un administrateur de suivre les étapes ci-dessous.

1. Allez dans **Paramètres** > **Paramètres de la page d'atterrissage**.
2. Saisissez le domaine auquel vous souhaitez vous connecter et sélectionnez **Soumettre**. Par exemple, `forms.example.com.`
3. Copiez et collez les enregistrements **TXT** et **CNAME** dans les paramètres DNS de votre fournisseur de domaine.
4. Retournez au tableau de bord de Braze pour vérifier la connexion.

\![Page des paramètres de la page d'atterrissage avec un enregistrement TXT et deux enregistrements CNAME listés avec leurs noms et valeurs respectifs]\[1].

{% alert note %} Selon votre fournisseur de domaine, la connexion peut prendre jusqu'à 48 heures. Une fois le processus terminé, nous commencerons à utiliser votre domaine personnalisé pour vos pages d'atterrissage dans le tableau de bord de Braze. {% endalert %}

## Ressources DNS

Vous trouverez ci-dessous des ressources pour créer et gérer des enregistrements DNS avec les fournisseurs de domaines les plus courants. Si vous utilisez un autre fournisseur, reportez-vous à sa documentation ou contactez son équipe d'assistance pour obtenir des informations.

| Fournisseur de domaines | Ressources | --- | | Bluehost | [Enregistrements DNS expliqués](https://my.bluehost.com/hosting/help/508)<br> [Gestion DNS Ajouter, modifier ou supprimer des entrées DNS](https://my.bluehost.com/hosting/help/559) | Dreamhost | [Comment ajouter des enregistrements DNS personnalisés ?](https://help.dreamhost.com/hc/en-us/articles/360035516812) | GoDaddy | [Ajouter un enregistrement CNAME](https://www.godaddy.com/help/add-a-cname-record-19236?) | | Cloudflare | [Gérer les enregistrements DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) | Squarespace | [Ajouter des paramètres DNS personnalisés](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) { : .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Résolution des problèmes 

### Ma connexion au domaine a échoué

Vérifiez que votre domaine a été saisi correctement et qu'il correspond à ce que vous avez soumis à Braze à partir de votre compte de fournisseur de domaine. S'il est correct et correspond, vérifiez les enregistrements TXT et CNAME fournis par Braze. Ils doivent correspondre aux enregistrements que vous avez saisis dans le compte de votre fournisseur de domaine.

## Foire aux questions

### Puis-je connecter plusieurs sous-domaines à mon espace de travail ou connecter un sous-domaine à plusieurs espaces de travail ?

Non, vous ne pouvez actuellement connecter qu'un seul sous-domaine à un espace de travail.

### Puis-je utiliser le même sous-domaine que celui que j'utilise actuellement pour mon site web principal ou mon domaine d'envoi ?

Non, vous ne pouvez pas utiliser des sous-domaines déjà utilisés. Bien que ces sous-domaines soient valides, ils ne peuvent pas être utilisés pour les pages de destination s'ils sont déjà affectés à d'autres fins ou s'ils ont des enregistrements DNS qui entrent en conflit avec les enregistrements CNAME requis.

\[1] : {% image\_buster /assets/img/landing\_pages/connect\_subdomain.png %}
