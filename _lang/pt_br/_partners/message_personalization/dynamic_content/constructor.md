---
nav_title: Construtor
article_title: Construtor
description: "Este artigo de referência descreve a parceria entre a Braze e a Constructor. Essa parceria permite que você aproveite o Constructor's Offsite Product Discovery para gerar e fornecer dinamicamente recomendações personalizadas de produtos nas mensagens do Braze."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Construtor

> [O Constructor](https://constructor.com/) é uma plataforma de pesquisa e descoberta de produtos que usa IA e machine learning para oferecer pesquisa personalizada, recomendações e experiências de navegação para sites de comércio eletrônico e varejo.

Com a integração entre o Braze e o Constructor, você pode usar o Constructor's Offsite Product Discovery para gerar e fornecer dinamicamente recomendações personalizadas de produtos nas mensagens do Braze.

## Casos de uso

- **Acompanhamento de carrinho abandonado e pós-pedido**: Gere recomendações dinâmicas de produtos com base no comportamento do usuário e no conteúdo do carrinho para enviar lembretes personalizados de carrinho abandonado ou sugestões pós-pedido.
- **Recomendações de produtos semelhantes para itens abandonados do carrinho**: Sugira produtos semelhantes aos itens deixados no carrinho de um usuário para mantê-lo engajado e oferecer alternativas.
- **Lembretes de itens vistos recentemente**: Notifique os usuários sobre itens que eles visualizaram recentemente, mas que ainda não compraram, incentivando-os a concluir a compra.
- **Campanhas promocionais**: Envio de mensagens promocionais personalizadas com recomendações do produto adaptadas às preferências do usuário para vendas sazonais ou ofertas especiais.
- **Sugestões de produtos visualmente semelhantes**: Recomende itens visualmente semelhantes aos que o usuário visualizou recentemente, ajudando-o a descobrir opções relacionadas que ele pode preferir.

## Pré-requisitos

| Requisito | Descrição |
|-------------|-------------|
| Conta do Construtor | Para aproveitar essa parceria, é necessário ter uma conta do Constructor com o serviço Offsite Discovery ativado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Trabalhe com sua equipe de integração do Constructor para concluir o processo de integração. Certifique-se de que os dados comportamentais de seu site ou de outras fontes de dados relevantes estejam disponíveis para ativar recomendações personalizadas de produtos. A equipe de integração do Constructor também ajudará a configurar os snippets HTML necessários para uso nas mensagens do Braze.

## URL da API de descoberta externa do Construtor

É possível usar o URL da API Offsite Discovery do Constructor para renderizar imagens de produtos e direcionar os usuários para a página de detalhes do produto apropriada. Abaixo está um detalhamento da estrutura do endpoint e um exemplo de como usá-lo:

### Exemplo

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img 
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200" 
    border="0" 
    alt="Shop Now" 
  />
</a>
```

### Parâmetros

| Parâmetros | Descrição |
|-------------|-------------|
| `position` | Refere-se à classificação do item recomendado específico na lista de sugestões (por exemplo, `position = 2`). <br>![Classificação da posição do item.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Representa o identificador do usuário, crucial para personalizar os resultados da recomendação. Defina o parâmetro `ui` como o `external_id` do cliente no Braze. Se omitido, o Constructor retornará recomendações gerais em vez de recomendações específicas do usuário. |
| `pod_id` | Identificador do pod que contém a estratégia e as regras de busca e publicidade para recomendações (por exemplo, um pod com uma estratégia de best-seller gera best-seller personalizado). |
| `key` | A chave de índice do Construtor para esse cliente. |
| `style_id` | Determina quais imagens são exibidas para o cartão do produto. Por exemplo, diferentes sites `style_ids` exibem imagens exclusivas de cartões de produtos. |
| `campaign_id` | ID exclusivo para a campanha de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Entradas opcionais

| Entrada | Descrição |
|-------------|-------------|
| `item_id` | Representa o item de semente. Necessário para estratégias baseadas em itens, como pacotes alternativos e complementares. Por exemplo, o primeiro item em um e-mail é o item inicial, com os itens subsequentes como alternativas. |
| `num_results` | Número de produtos a serem adicionados ao e-mail. O padrão é 10, até 100. Por exemplo, `num_results = 3` significa que três recomendações foram adicionadas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

