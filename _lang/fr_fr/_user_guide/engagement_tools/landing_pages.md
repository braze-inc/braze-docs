---
nav_title: Landing pages
article_title: Pages d’accueil
page_order: 31
guide_top_header: "Pages d’accueil"
description: "Cet article contient des ressources sur la création et la personnalisation des pages d’accueil Braze."
alias: /landing_pages/
---

# À propos des pages d'atterrissage

> Les pages d'atterrissage de Braze sont des pages web autonomes qui peuvent piloter votre stratégie d'acquisition et d'engagement des utilisateurs.

Utilisez les pages d'atterrissage pour développer votre audience, capturer les données des utilisateurs, promouvoir des offres spéciales et soutenir des campagnes multicanal.

{% alert note %}
La disponibilité de la page d'accueil et du domaine personnalisé dépend de votre forfait Braze. Veuillez contacter votre gestionnaire de compte ou votre gestionnaire de la satisfaction client pour commencer.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Conditions préalables

Avant de pouvoir accéder aux pages d'atterrissage, les créer et les publier, vous devez disposer [d'autorisations d']({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) administrateur ou de toutes les autorisations suivantes :

- Afficher la page de destination
- Modifier les projets de page de destination
- Publier les pages d’accueil

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Paliers de régime

Le nombre de pages de destination publiées et de domaines personnalisés que vous pouvez utiliser dépend de votre type de plan : gratuit ou payant (incrémental).

| Fonctionnalité                                                                                                   | Tiercé libre     | Niveau payant (incrémental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Pages d'atterrissage publiées                                                                 | Cinq par entreprise | 20 supplémentaires |
| Domaines personnalisés          | Un par entreprise | Cinq autres |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Ajouter Google Tag Manager à une page d'accueil

Pour intégrer Google Tag Manager à vos pages de destination, veuillez ajouter un bloc **de code personnalisé** à votre page de destination dans l'éditeur par glisser-déposer, puis insérer le code Tag Manager dans le bloc. Veuillez vous assurer d'ajouter une couche de données avant le code Tag Manager, comme dans l'exemple suivant :

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Pour plus d'informations sur la mise en œuvre de Google Tag Manager, veuillez consulter [la documentation de Google](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Foire aux questions

### Quelle est la taille maximale des pages d'atterrissage ?

La taille du corps de la page d'accueil peut atteindre 500 Ko.

### Y a-t-il des exigences techniques pour publier une page d'accueil ?

Non, il n'y a pas d'exigences techniques.

### Existe-t-il un éditeur HTML pour les pages d'atterrissage ?

Oui. Utilisez le bloc **Code personnalisé** dans l'éditeur par glisser-déposer pour ajouter ou modifier du code HTML.

### Est-il possible de créer un webhook à l'intérieur d'une page d'accueil ?

Non, cette fonctionnalité n'est actuellement pas prise en charge.
