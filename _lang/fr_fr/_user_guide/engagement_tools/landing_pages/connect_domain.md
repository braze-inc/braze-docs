---
nav_title: Connexion de votre domaine
article_title: Connexion de votre domaine
description: "Cet article explique comment connecter votre propre domaine personnalisé aux pages d'atterrissage de Braze."
page_order: 1
alias: /landing_pages/connect_domain/
---

# Connexion de votre domaine

> Connectez votre propre domaine à votre espace de travail Braze pour personnaliser les URL de vos pages de destination avec votre marque.

Pour connecter un domaine ou un sous-domaine à votre compte Braze, demandez à un administrateur de suivre les étapes ci-dessous.

1. Allez dans **Paramètres** > **Paramètres de la page d'atterrissage**.
2. Saisissez le domaine ou le sous-domaine que vous souhaitez connecter et sélectionnez **Soumettre**. Par exemple, `forms.example.com`.
3. Copiez et collez les enregistrements **TXT** et **CNAME** dans les paramètres DNS de votre fournisseur de domaine.
4. Retournez au tableau de bord de Braze pour vérifier la connexion.

![Page des paramètres de la page d'atterrissage avec un enregistrement TXT et deux enregistrements CNAME répertoriés avec leurs noms et valeurs respectifs.][1]

{% alert note %}
Selon votre fournisseur de domaine, la connexion peut prendre jusqu'à 48 heures. Une fois le processus terminé, nous commencerons à utiliser votre domaine personnalisé pour vos pages de destination dans le tableau de bord de Braze.
{% endalert %}

## Utiliser votre domaine dans Braze

Une fois la vérification de votre domaine terminée, il sera utilisé par défaut dans Braze. Par exemple, si vous connectez le sous-domaine `forms.example.com`, les URL de vos pages d'atterrissage seront mises à jour et ressembleront à `forms.example.com/holiday-sale`.

{% alert note %}
La suppression des domaines personnalisés sera bientôt disponible. Contactez votre gestionnaire de satisfaction client si vous devez supprimer votre sous-domaine.
{% endalert %}

## Ressources des fournisseurs de domaines

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

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
