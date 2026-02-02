---
nav_title: Dicionário de dados
article_title: Dicionário de dados para Braze Pilot
page_order: 3
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."
---

# Dicionário de dados

> Cada simulação de aplicativo no Braze Pilot é instrumentada para coletar uma variedade de eventos e atribuições com base na atividade do usuário no app. 

## A abordagem dos dados

O app registra atributos personalizados e eventos típicos do setor representado pela marca fictícia. Você pode usar essas atribuições para potencializar as demonstrações de uma variedade de casos de uso comuns.
Geralmente, todos os eventos e atribuições são prefixados com um código curto que corresponde à simulação do app responsável pelos dados. Por exemplo:

- Todos os dados registrados pela simulação do app Steppington são prefixados com `st_`
- Todos os dados registrados pela simulação do app PantsLabyrinth são prefixados com `pl_`
- Todos os dados registrados pela simulação do app MovieCanon são prefixados com `mc_`

## Lista de eventos registrados e atribuições

A tabela a seguir lista os eventos e atribuições registrados pelo Braze Pilot.

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 32%;
}
th:nth-child(2), td:nth-child(2) {
    width: 15%;
}
th:nth-child(3), td:nth-child(3) {
    width: 10%;
}
th:nth-child(4), td:nth-child(4) {
    width: 20%;
}
th:nth-child(5), td:nth-child(5) {
    width: 28%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Nome</th>
            <th>App</th>
            <th>Tipo</th>
            <th>Propriedades</th>
            <th>Quando estiver registrado</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>Evento</td>
            <td></td>
            <td>Quando o usuário entra no app MovieCanon</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Evento</td>
            <td><code>title: string</code></td>
            <td>Quando o usuário termina de assistir a um vídeo</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Evento</td>
            <td><code>title: string</code></td>
            <td>Quando o usuário visualiza uma página de filme</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>Pants Labyrinth</td>
            <td>Evento</td>
            <td><code>item_name: string</code></td>
            <td>Quando o usuário visualiza uma página de produto</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>Pants Labyrinth</td>
            <td>Evento</td>
            <td></td>
            <td>Quando o usuário entra no app PantsLabyrinth</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>Pants Labyrinth</td>
            <td>Evento</td>
            <td><code>item_name: string</code></td>
            <td>Quando o usuário adiciona um item à sua lista de desejos</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>Pants Labyrinth</td>
            <td>Evento</td>
            <td><code>item_name: string</code></td>
            <td>Quando o usuário adiciona um item ao carrinho</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event&gt;</code></td>
            <td>Pants Labyrinth</td>
            <td>Evento</td>
            <td><code>name: string</code><br><code>price: number</code></td>
            <td>Quando o usuário conclui uma compra</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td></td>
            <td>Quando o usuário entra no app Steppington</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>Quando o usuário conclui um exercício</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>benefit_type: string</code></td>
            <td>Quando o usuário visitar a guia Steppington+ (se estiver ativada com o sinalizador de recurso)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: string</code></td>
            <td>Quando o usuário visita uma página de exercícios</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>Quando o usuário conclui um exercício</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>Atributo</td>
            <td><code>string</code></td>
            <td>Quando o usuário conclui um exercício</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: string</code></td>
            <td>Quando o usuário favorece uma classe</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: string</code></td>
            <td>Quando o usuário não favorece uma classe</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td></td>
            <td>Quando o usuário seleciona o botão <strong>Start Free Trial (Iniciar teste gratuito)</strong> </td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>goal_name: string</code><br><code>goal: number</code><br><code>units: string</code></td>
            <td>Quando o usuário seleciona o botão <strong>Start Free Trial</strong>.</td>
        </tr>
    </tbody>
</table>
