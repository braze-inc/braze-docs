---
nav_title: Liftigniter
article_title: Liftigniter
alias: /partners/liftigniter/
description: "Cet article de référence présente le partenariat entre Braze et LiftIgniter, une plateforme de personnalisation de premier plan, aidant les entreprises à transformer leurs expériences clients."
page_type: partner
search_tag: Partner

---

# Liftigniter

> LiftIgniter est une plateforme de personnalisation de premier plan qui aide les entreprises à transformer leurs expériences clients grâce à la personnalisation en temps réel sur tous les points de contact.

_Cette intégration est maintenue par Liftigniter._

## À propos de l'intégration

L'intégration de LiftIgniter et de Braze tire parti de contenu connecté pour vous permettre de recommander des sujets intéressants tels que des articles d'actualité, des vêtements et d'autres articles et vidéos de vente au détail.

## Conditions préalables

| Condition| Description|
| ---| ---|
| Compte Liftigniter | Un [compte LiftIgniter](https://console.liftigniter.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Intégration de l'API LiftIgniter | Vous devez [intégrer](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview) LiftIgniter à votre site ou à votre appli pour pouvoir en tirer des recommandations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration

Utilisez l ['API REST de LiftIgniter](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389) pour insérer du contenu personnalisé dans vos messages. Une fois votre compte LiftIgniter créé et LiftIgniter intégré à votre application, ajoutez le modèle suivant dans votre compositeur de messages pour appeler du contenu dans vos messages, en remplaçant des informations si nécessaire (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

Ensuite, rédigez votre message, en définissant le contenu que vous souhaitez appeler avec JSON. Par exemple, `{{json.items[0].title}}`.

{% endraw %}

![Une image montrant une campagne de notification push qui inclut des appels de contenu connecté spécifiques à Liftigniter. Une logique de contenu connecté a également été ajoutée au champ de l'image.]({% image_buster /assets/img/liftigniter.png %})

Une fois que vous avez placé ce message dans le corps du compositeur, vous pouvez prévisualiser votre message. Vous pouvez même insérer des images, comme le montre l'exemple suivant :

![Une image de prévisualisation de ce à quoi ressemblera le message après son envoi.]({% image_buster /assets/img/liftigniter2.png %})


