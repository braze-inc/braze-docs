---
nav_title: Análise de dados
article_title: "Análise de dados de recomendação de itens"
description: "Saiba mais sobre a análise de dados de recomendação de itens e como visualizá-los no Braze."
page_order: 1.3
---

# Análise de dados de recomendação de itens

> Saiba mais sobre a análise de dados de recomendação de itens e como visualizá-los no Braze.

## Visualização de análises de dados

É possível visualizar a análise de dados da sua recomendação para ver quais itens foram recomendados aos usuários e a precisão do modelo de recomendação.

1. Acesse **Análise de dados** > **Recomendação de item**.
2. Selecione sua recomendação na lista.

## Métricas disponíveis

### Público

Essas são métricas relacionadas ao seu público de recomendação, que incluem precisão, cobertura e tipo de recomendação.

![Métricas do público de recomendação mostrando precisão (25,3%), cobertura (54,3%) e tipos de recomendação divididos entre itens personalizados e mais populares.]({% image_buster /assets/img/item_recs_analytics_1.png %})

Consulte a tabela a seguir para saber mais:

| Métrico              | Descrição |
| ------------------- | ---------- |
| **Precisão**           | A porcentagem de tempo em que o modelo adivinhou corretamente o próximo item que um usuário comprou. A precisão depende muito do tamanho e da mistura de seu catálogo específico e deve ser usada como um guia para entender com que frequência o modelo está correto.<br><br>Em testes anteriores, vimos modelos com bom desempenho com números de precisão que variam de 6 a 20%. Essa métrica é atualizada na próxima vez que o modelo for retreinado.  |
| **Cobertura**            | Qual porcentagem dos itens disponíveis no catálogo é recomendada a pelo menos um usuário. Você pode esperar ver uma cobertura maior de itens com recomendações personalizadas de itens em relação aos mais populares. |
| **Tipo da recomendação** | A porcentagem de usuários que receberão recomendações personalizadas ou mais recentes em comparação com o fallback dos itens mais populares. O fallback é enviado aos usuários que não têm dados suficientes para gerar uma recomendação personalizada ou mais recente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Itens

Essa tabela inclui métricas sobre seus itens personalizados, mais recentes e mais populares de seu catálogo.

![Tabelas lado a lado que listam itens atribuídos aos usuários, separados por recomendações personalizadas e recomendações mais populares.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Consulte a tabela a seguir para saber mais:

| Métrico              | Descrição |
| ------------------- | ---------- |
| **Itens personalizados**<br><br>**Itens mais recentes** | Essa coluna lista cada item do catálogo em ordem decrescente dos mais frequentemente recomendados aos usuários. Essa coluna também mostra quantos usuários foram atribuídos a cada item pelo modelo.<br><br>Os itens **personalizados** ou **mais recentes** serão listados, dependendo do [tipo de recomendação]({{site.baseurl}}/user_guide/brazeai/recommendations/). |
| **Itens mais populares** | Essa coluna lista cada item do catálogo em ordem decrescente de popularidade. A popularidade aqui se refere aos itens do catálogo com os quais os usuários interagem com mais frequência em todo o espaço de trabalho. O mais popular é usado como fallback quando o personalizado ou o mais recente não pode ser calculado para um usuário individual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Visão geral

Essa é uma visão geral da configuração de recomendação escolhida, que inclui quando a recomendação foi atualizada pela última vez.

![Tabela de visão geral da recomendação que exibe o tipo, o catálogo, o tipo de evento, o nome do evento personalizado, o nome da propriedade e a data da última atualização.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }
