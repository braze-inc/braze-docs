---
nav_title: Hino Futuro
article_title: Hino Futuro
description: "Aprenda como integrar o Future Anthem com o Braze."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Hino Futuro

> O produto tudo-em-um da Future Anthem para a indústria de jogos com dinheiro real, Amplifier IA, oferece personalização de conteúdo, experiências em tempo real e públicos dinâmicos. O Amplificador de IA funciona perfeitamente em esportes, cassino e loteria, permitindo que os clientes aprimorem os perfis de jogadores da Braze com atributos de jogadores específicos do setor, como jogo favorito, time favorito, pontuação de engajamento, recomendação de próxima aposta, próxima aposta esperada e mais.

{% alert important %}
Este recurso está atualmente em Acesso Antecipado. Por favor, entre em contato com a equipe de sucesso do cliente da Future Anthem para começar.
{% endalert %}

## Pré-requisitos

| Requisito              | Descrição                                            |
|--------------------------|--------------------------------------------------------|
| Conta do Anthem Futuro    | Uma conta do Future Anthem. |
| Chave da API REST do Braze       | Uma chave da API REST Braze com o [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze      | O [REST endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) do Braze que corresponde à sua instância, como `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Com essa integração, você pode:

- Identifique usuários com altas pontuações de engajamento e direcione-os com ofertas personalizadas, como promoções exclusivas ou recompensas VIP.
- Sugira jogos semelhantes a um usuário com base nos jogos que ele já gosta.

## Integração

A equipe de sucesso do cliente do Future Anthem ajudará a configurar sua integração. Entre em contato com seu contato de Sucesso do Cliente e eles o ajudarão a identificar os atributos mais relevantes para você enviar para Braze.

|Atributos de exemplo em Future Anthem|Exemplo de atributos no Braze|
|-----------------------------------|---------------------------|
|![Os atributos no perfil do usuário.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![O atributo do objeto.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## Braze atributos personalizados

Estes são os atributos personalizados do Braze disponíveis. Para informações mais detalhadas, veja [Future Anthem: Começando](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Recomendações de Apostas %}

| Subcategoria | Exemplo (JSON) | Tipo de dado |
| ------- | ----------- |----------- |
| Preferências do Usuário | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objeto |
| Recomendações de Apostas Simples | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objeto |
| Recomendações de Apostas de Acumulador | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| Objeto |
| Recomendações de Apostas de Acumulador | `{"Bet_1": 1.5, "Bet_2": 2}` | Objeto |
| Recomendações de Apostas do Construtor de Apostas | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| Objeto |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Recomendações Bônus %}

| Subcategoria | Exemplo | Tipo de dado |
| ------- | ----------- |----------- |
|NGR – Receita líquida de jogos para a vida útil do usuário | 2232| Número|
| NGR14 – Receita líquida de jogos para os últimos 14 dias de atividade | 42 | Número
| Pontuação de Rentabilidade do Jogador| 130 | Número |
| Pontuação de Engajamento | 0.78 | Número |
| Pontuação de risco de churn | 0.02 | Número |
| Data Estimada da Próxima Aposta | 2024-08-29 | Horário |
| Aposte e Ganhe - Recomendação de valor de bônus | 20 | Número |
| Outras recomendações de valor de bônus no futuro | 0 | Número |
| Futuro CLTV  | 3126 | Número |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Recomendações de Jogos %}

| Subcategoria | Exemplo | Tipo de dado |
| ------- | ----------- |----------- |
| Recomendado Para Você | Favoritos Peludos, Frenesi da Pesca, Grande Bonança do Bass, Ouro do Arco-Íris, Velho Oeste| Vetor |
| Jogos Favoritos | Frenesi da Pesca | Vetor |
| Jogos Novos Recomendados | Abelhas Pegajosas, Cuidado com o Deep Megaways, Festa do Ouro, Os Flintstones| Vetor |
| Jogadores como você estão jogando (Filtragem Colaborativa) |Ouro Blitz, Grande Splash de Bass, Rick e Morty, Livro dos Mortos, Portões do Olimpo, Sorte do Irlandês | Vetor |
| Porque você jogou (Semelhança de Jogo)|Favoritos Peludos 2, Sorte Rish Expresso, Ouro Dinheiro, Caça ao Tesouro Asteca, Estrelas Bonanza | Vetor |
| Próximo (Sequenciamento de Jogo) | Pesca Frenética A Grande Captura, Grande Banqueiro, 9 Máscaras de Fogo, Super Leão, Pesca Maiores Panelas de Ouro | Vetor |
| Jogos Populares | Templo de Iris, Frenesi de Peixes, Recompensa Rishing, Tempo Louco, Favoritos Fluffy | Vetor |
| Jogos em Alta | Banco de Porcos, Ouro Hiper, Rei Pirâmide, Dinheiro de Ouro | Vetor |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Cluster de Jogadores %}

| Subcategoria | Exemplo | Tipo de dado |
| ------- | ----------- |----------- |
| Mostre em qual cluster o jogador está | Jogo de Alto Valor Diversificado| String |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Sustentação do Jogador - risco potencial do jogador %}

| Subcategoria | Exemplo | Tipo de dado |
| ------- | ----------- |----------- |
| Pontuação de Risco | 0,5| Número |
| Jogador Arriscado | Sim | Booleano |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}
