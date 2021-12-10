---
nav_title: Tests en cours
article_title: Tester les cartes de contenu
page_order: 3
description: "Cet article de référence couvre la façon de prévisualiser et de tester les Cartes de Contenu, ainsi que certaines meilleures pratiques."
channel:
  - cartes de contenu
---

# Tester les cartes de contenu

Il est extrêmement important de toujours tester vos cartes de contenu avant d'envoyer vos campagnes. Nos capacités de prévisualisation et de test vous permettent de regarder vos cartes de contenu. Vous pouvez prévisualiser votre message pour vous aider à le visualiser au fur et à mesure que vous le composez, en plus de vous envoyer un message de test à vous-même ou au périphérique d'un utilisateur spécifique. Nous vous recommandons de profiter des deux.

## Aperçu

Vous pouvez prévisualiser votre carte à mesure que vous la composez. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de votre utilisateur.

Dans l'onglet __Aperçu__ de votre compositeur, la vue de votre message pourrait ne pas être identique à son affichage actuel sur le périphérique de l'utilisateur. Nous vous recommandons de toujours envoyer un message de test à un appareil afin de vous assurer que vos supports, copies, personnalisations et attributs personnalisés génèrent correctement.

## Tester

Pour envoyer un test à [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, push doit être activé sur vos appareils de test avant l'envoi. Pour les utilisateurs d'iOS, vous devez appuyer sur la notification push envoyée par Braze pour voir la carte de contenu de test. Ce comportement s'applique uniquement aux cartes de contenu de test.

### Aperçu du message en tant qu'utilisateur

Vous pouvez également prévisualiser les messages de l'onglet **Test** comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur au hasard, ou créer un utilisateur personnalisé.

!\[Custom_User_Preview\]\[3\]

### Test checklist

- Est-ce que les images et les médias apparaissent et agissent comme prévu?
- Est-ce que le Liquid fonctionne comme prévu ? Avez-vous comptabilisé une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) dans le cas où le Liquid ne renvoie aucune information ?
- Votre copie est-elle claire, concise et correcte?
- Vos liens dirigent-ils l'utilisateur vers l'endroit où il doit aller ?

## Debug

Après l'envoi de vos Cartes de Contenu, vous pouvez décomposer ou déboguer n'importe quel problème depuis le [Journal de l'Utilisateur d'événement]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/) dans la Console Développeur.

Un cas d'utilisation courant est d'essayer de déboguer pourquoi un utilisateur ne peut pas voir une carte de contenu particulière. Pour cela, vous pouvez chercher dans les **Logs des utilisateurs d'événement** les Cartes de Contenu livrées au SDK au démarrage de la session, mais avant une impression, et retracez celles à une campagne spécifique:

1. Allez dans la **Console développeur** et sélectionnez l'onglet **Journal des utilisateurs d'événements**.
2. Localisez et développez la requête SDK pour votre utilisateur de test.
3. Cliquez sur **Données brutes**.
4. Trouvez l'id `` de votre session. Un extrait d'exemple est affiché ci-dessous:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NjE4NTAwNWE5ZDliZWU3OTM4N2NjZTQzXyRfY2M9YzNiMjU3NDAtZjExMy1jMDQ3LTRiMWQtZDI5NmYyODBhZjRmJm12PTYxODUwMDViOWQ5YmVlNzkzODdjY2U0NSZwaT1jbXA="
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Utilisez un outil de décodage comme [Decode et Encode Base64](https://www.base64decode.org/) pour décoder l' `id` du format Base64 et trouver le `campaign_id` associé. Dans notre exemple ci-dessus, cela donne les résultats suivants :

    ```
    6185005a9d9bee79387cce43_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Où `6185005a9d9bee79387cce43` est le `campaign_id`.<br><br>

6. Rendez-vous sur la page **Campagnes** et recherchez le `campaign_id`.

!\[Search for campaign_id on Campaigns page\]\[1\]

À partir de là, vous pouvez examiner les paramètres de vos messages et le contenu pour les dessuser et déterminer pourquoi un utilisateur ne peut pas voir une carte de contenu particulière.
[1]: {% image_buster /assets/img_archive/cc_debug.png %} [3]: {% image_buster /assets/img/cc-user-preview.png %}
