---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "Cet article présente le partenariat entre Braze et LiftIgniter, une plateforme de personnalisation leader qui aide les entreprises à transformer leurs expériences client."
page_type: partner
search_tag: Partenaire

---

# Liftigniter

> LiftIgniter est une plateforme de personnalisation leader qui aide les entreprises à transformer leurs expériences client grâce à une personnalisation en temps réel sur chaque point de contact.

L’intégration LiftIgniter et Braze tire parti du Contenu connecté pour vous permettre de recommander des sujets intéressants tels que des articles d’actualités, des vêtements et d’autres articles et des vidéos.

## Conditions préalables

| Condition| Description|
| ---| ---|
| Compte LiftIgniter | Un [compte LiftIgniter](https://console.liftigniter.com/login) est nécessaire pour profiter de ce partenariat. |
| Intégration de l’API LiftIgniter | Vous devez [intégrer](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview) LiftIgniter à votre site ou application pour pouvoir extraire des recommandations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Utilisez l’[API REST de LiftIgniter](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389) pour insérer du contenu personnalisé dans vos messages. Une fois que vous avez votre compte LiftIgniter et que LiftIgniter est intégré à votre application, ajoutez le modèle suivant dans votre compositeur de messages pour appeler du contenu dans vos messages, en remplaçant les informations si nécessaire (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

Rédigez ensuite votre message, en définissant le contenu que vous souhaitez appeler avec json. Par exemple, `{{json.items[0].title}}`.

{% endraw %}

![Image montrant une campagne de notification push qui inclut les appels de Contenu connecté spécifiques de LiftIgniter. Une logique de Contenu connecté a également été ajoutée au champ d’image.][1]

Une fois que vous avez placé ce message dans le corps du compositeur, vous pouvez prévisualiser votre message. Vous pouvez même extraire des images, illustrées dans l’exemple suivant :

![Une image d’aperçu du message une fois envoyé.][2]

[1]: {% image_buster /assets/img/liftigniter.png %}
[2]: {% image_buster /assets/img/liftigniter2.png %}