---
nav_title: Allumer
article_title: Allumer
alias: /fr/partners/liftigniter/
description: "Cet article décrit le partenariat entre Braze et LiftIgniter, une plateforme de personnalisation de premier plan, qui aide les entreprises à transformer leurs expériences clients."
page_type: partenaire
search_tag: Partenaire
---

# Liftigniter

> LiftIgniter est une plateforme de personnalisation de premier plan qui aide les entreprises à transformer leurs expériences de clients par la personnalisation en temps réel à travers chaque point de contact.

Le LiftIgniter et Braze utilisent le contenu connecté pour vous permettre de recommander des sujets intéressants tels que les articles de nouvelles, vêtements et autres articles de vente au détail et vidéos.

## Pré-requis

| Exigences                        | Libellé                                                                                                                                                                                                           |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte LiftIgniter               | Un compte [LiftIgniter](https://console.liftigniter.com/login) est requis pour profiter de ce partenariat.                                                                                                        |
| Intégration de l'API LiftIgniter | Vous devez [intégrer](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview) LiftIgniter à votre site ou à votre application pour pouvoir en tirer des recommandations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Utilisez [l'API REST de LiftIgniter](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389) pour insérer du contenu personnalisé dans vos messages. Une fois que vous avez votre compte LiftIgniter et que LiftIgniter est intégré dans votre application, ajouter le modèle suivant dans votre compositeur de message pour appeler le contenu dans vos messages, remplacement des informations nécessaires (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {“x-api-key”: “theapikey”} :body “UseActivity”=false :content_type application/json :save json %}
```

Ensuite, écrivez votre message, en définissant le contenu que vous souhaitez appeler avec json. Par exemple, `{{json.items[0].title}}`.

{% endraw %}

!\[Compositeur de LiftIgniter\]\[1\]

Une fois que vous avez mis ce message dans le corps du compositeur, vous pouvez prévisualiser votre message. Vous pouvez même tirer des images, comme on le voit dans l'exemple ci-dessous:

!\[Image de LiftIgniter\]\[2\]
[1]: {% image_buster /assets/img/liftigniter.png %} [2]: {% image_buster /assets/img/liftigniter2.png %}