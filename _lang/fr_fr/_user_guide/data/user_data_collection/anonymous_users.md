---
nav_title: Utilisateurs anonymes
article_title: "Pour commencer : Utilisateurs anonymes"
page_order: 0
page_type: reference
description: "Cet article donne un aperçu des utilisateurs anonymes et des alias d'utilisateurs, en soulignant leur importance et la manière dont ils peuvent être exploités dans vos messages."

---

# Utilisateurs anonymes

> Les utilisateurs qui visitent votre site web ou votre application sans se connecter, comme un visiteur invité, sont reconnus comme des utilisateurs anonymes. Ces utilisateurs n'ont pas de `external_ids`, qui sont utilisés pour mettre à jour les profils utilisateurs avec l'API Braze, mais des [points de données]({{site.baseurl}}/user_guide/data/data_points/) leur sont toujours attribués et ils peuvent être ciblés dans vos segmentations.

Lorsqu'un utilisateur anonyme visite votre site web ou votre application, le SDK de Braze le crée et l'affecte à un profil utilisateur " anonyme ". Pendant que l'utilisateur navigue, le SDK capture automatiquement des données pour son profil utilisateur anonyme, telles que des informations d'utilisation, des informations sur l'appareil, et plus encore si vous avez configuré des attributs et des événements personnalisés.

Vous pouvez effectuer les opérations suivantes avec les utilisateurs anonymes capturés :

- Envoi de messages aux utilisateurs avant qu'ils ne se connectent
- Collectez le profil d'un utilisateur avant qu'il ne se connecte, afin de ne pas passer à côté de données pertinentes.
- Encouragez l'utilisateur à compléter son profil en lui envoyant un message lorsqu'il ne le fait que partiellement.
- Compléter le profil d'un utilisateur lorsqu'il se connecte, afin de pouvoir annuler les envois de messages sur d'autres plateformes (par exemple, ne pas envoyer un message "livraison gratuite sur la 1ère commande de l'app" lorsque l'utilisateur a déjà effectué des commandes sur l'app).
- Engagez les utilisateurs qui montrent une intention de sortie en les encourageant à créer un profil, à passer à la caisse ou à effectuer une autre action.

## L'attribution d'aliasing de l'utilisateur

Les utilisateurs anonymes n'ont pas de `external_ids`, mais vous pouvez attribuer aux profils utilisateurs anonymes un identifiant alternatif : les alias d'utilisateur. Cela vous permet d'effectuer les mêmes actions sur un profil utilisateur anonyme que s'il était identifié par `external_ids`. Par exemple, vous pouvez utiliser l'API de Braze pour consigner les événements et les attributs associés aux utilisateurs anonymes, et cibler ces utilisateurs dans votre message avec le filtre de segmentation [L'ID externe est vide.]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id)

## Fusionner des utilisateurs anonymes  

Parfois, les profils utilisateurs anonymes sont des doublons qui ont le même numéro de téléphone ou la même adresse e-mail que d'autres profils utilisateurs. L'un des doublons peut même être un profil utilisateur identifié. Ces doublons peuvent être fusionnés en un seul profil utilisateur en utilisant le POST [: Fusionner Utilisateurs endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) ou l'un des outils de fusion de la plateforme Braze, comme la [fusion basée sur des règles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

## Cas d’utilisation

### Cibler les utilisateurs anonymes de votre segmentation

Comme les utilisateurs anonymes n'ont pas d'ID `external_id`, vous pouvez les cibler en masse en utilisant le filtre de segmentation **L'ID externe est vide.** Pour plus de précision, vous pouvez ajouter un attribut personnalisé aux utilisateurs anonymes que vous souhaitez cibler et filtrer en conséquence.

Supposons que vous attribuiez l'attribut personnalisé "is_lead_profile" à chaque profil utilisateur anonyme. Vous pourriez cibler ces profils avec l'un de ces filtres ou les deux :

- **L'ID utilisateur externe est vide**
- "is_lead_profile" **est vrai**

![Filtres de segmentation pour un ID externe vierge et un attribut personnalisé "is_lead_profile" vrai.][1]

### Capturez les données de paiement d'un utilisateur anonyme.

Vous pouvez capturer les données de paiement d'un utilisateur anonyme (ou d'un visiteur invité) en créant un profil utilisateur aliasing de l'utilisateur au cours du processus de paiement. Lorsqu'un utilisateur anonyme passe à la caisse à l'aide d'un formulaire de capture web, faites déclencher un appel à l'API pour créer un profil utilisateur aliasing et enregistrer un événement d'achat. Vous pourrez ensuite mettre à jour le profil utilisateur créé via l'API de Braze.

Voici un exemple de charge utile qui sera générée lorsque le formulaire de capture Web sera soumis :

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}

[1]: {% image_buster /assets/img/getting_started/anonymous_users.png %}
