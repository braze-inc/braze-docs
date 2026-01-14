---
nav_title: Dicionário de dados
article_title: Dicionário de dados para piloto de brasagem
page_order: 3
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."
---

# Dicionário de dados

> Cada simulação de aplicativo no Braze Pilot é instrumentada para coletar uma variedade de eventos e atributos com base na atividade do usuário no aplicativo. 

## A abordagem dos dados

O aplicativo registra atributos e eventos personalizados típicos do setor representado pela marca fictícia. Você pode usar esses atributos para potencializar as demonstrações de uma variedade de casos de uso comuns.
Em geral, todos os eventos e atributos são prefixados com um código curto que corresponde à simulação do aplicativo responsável pelos dados. Por exemplo:

- Todos os dados registrados pela simulação do aplicativo Steppington são prefixados com `st_`
- Todos os dados registrados pela simulação do aplicativo PantsLabyrinth são prefixados com `pl_`
- Todos os dados registrados pela simulação do aplicativo MovieCanon são prefixados com `mc_`

## Lista de eventos e atributos registrados

A tabela a seguir lista os eventos e atributos registrados pelo Braze Pilot.

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
            <th>Aplicativo</th>
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
            <td>Quando o usuário entra no aplicativo MovieCanon</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Evento</td>
            <td><code>título: string</code></td>
            <td>Quando o usuário termina de assistir a um vídeo</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Evento</td>
            <td><code>título: string</code></td>
            <td>Quando o usuário visualiza uma página de filme</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantsLabyrinth</td>
            <td>Evento</td>
            <td><code>item_name: string</code></td>
            <td>Quando o usuário visualiza uma página de produto</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantsLabyrinth</td>
            <td>Evento</td>
            <td></td>
            <td>Quando o usuário entra no aplicativo PantsLabyrinth</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantsLabyrinth</td>
            <td>Evento</td>
            <td><code>item_name: string</code></td>
            <td>Quando o usuário adiciona um item à sua lista de desejos</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantsLabyrinth</td>
            <td>Evento</td>
            <td><code>item_name: string</code></td>
            <td>Quando o usuário adiciona um item ao carrinho</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event></code></td>
            <td>PantsLabyrinth</td>
            <td>Evento</td>
            <td><code>name: string</code><br><code>preço: número</code></td>
            <td>Quando o usuário conclui uma compra</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td></td>
            <td>Quando o usuário entra no aplicativo Steppington</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: string</code><br><code>calories_burned: número</code><br><code>workout_length: número</code></td>
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
            <td><code>class_type: string</code><br><code>calories_burned: número</code><br><code>workout_length: número</code></td>
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
            <td><code>goal_name: string</code><br><code>meta: número</code><br><code>unidades: string</code></td>
            <td>Quando o usuário seleciona o botão <strong>Start Free Trial</strong>.</td>
        </tr>
    </tbody>
</table>
