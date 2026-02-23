---
nav_title: Construtor
article_title: Construtor
description: "Este artigo de referência descreve a parceria entre Braze e Constructor. Esta parceria permite que você aproveite a Descoberta de Produtos Offsite do Constructor para gerar e entregar dinamicamente recomendações de produtos personalizadas nas mensagens do Braze."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Construtor

> [Constructor](https://constructor.com/) é uma plataforma de busca e descoberta de produtos que utiliza IA e machine learning para oferecer experiências de busca, recomendações e navegação personalizadas para sites de eCommerce e varejo.

Com a integração do Braze e do Constructor, você pode usar a Descoberta de Produtos Offsite do Constructor para gerar e entregar dinamicamente recomendações de produtos personalizadas nas mensagens do Braze.

## Casos de uso

- **Carrinho abandonado e follow-ups pós-pedido**: Gere recomendações de produtos dinâmicas com base no comportamento do usuário e no conteúdo do carrinho para enviar lembretes personalizados de carrinho abandonado ou sugestões pós-pedido.
- **Recomendações de produtos similares para itens do carrinho abandonado**: Sugira produtos similares aos itens deixados no carrinho de um usuário para mantê-los engajados e oferecer alternativas.
- **Lembretes de itens visualizados recentemente**: Notifique os usuários sobre itens que visualizaram recentemente, mas que ainda não compraram, incentivando-os a concluir a compra.
- **Campanhas promocionais**: Entregue mensagens promocionais personalizadas com recomendações de produtos selecionadas de acordo com as preferências do usuário para vendas sazonais ou ofertas especiais.
- **Sugestões de produtos visualmente similares**: Recomende itens visualmente similares àqueles que um usuário visualizou recentemente, ajudando-o a descobrir opções relacionadas que possam preferir.

## Pré-requisitos

| Requisito | Descrição |
|-------------|-------------|
| Conta do Constructor | Uma conta do Constructor com seu serviço de Descoberta Offsite ativado é necessária para aproveitar esta parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Trabalhe com sua equipe de integração do Constructor para concluir o processo de integração. Certifique-se de que os dados comportamentais do seu site ou de outras fontes de dados relevantes estejam disponíveis para ativar recomendações de produtos personalizadas. Sua equipe de integração do Constructor também ajudará a configurar os trechos de HTML necessários para uso nas mensagens do Braze.

## URL da API de Descoberta Offsite do Constructor

Você pode usar a URL da API de Descoberta Offsite do Constructor para renderizar imagens de produtos e direcionar os usuários para a página de detalhes do produto apropriada. Abaixo está uma análise da estrutura do endpoint e um exemplo de como usá-lo:

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
| `position` | Refere-se à classificação do item recomendado específico dentro da lista sugerida (por exemplo, `position = 2`). <br>![Classificação de posição do item.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Representa o identificador do usuário, crucial para personalizar os resultados de recomendação. Defina o parâmetro `ui` como o `external_id` do cliente no Braze. Se omitido, o Constructor retornará recomendações gerais em vez de específicas para o usuário. |
| `pod_id` | Identificador para o pod que contém regras de estratégia e merchandising para recomendações (por exemplo, um pod com uma estratégia de mais vendidos gera um mais vendido personalizado). |
| `key` | A chave do índice do Constructor para este cliente. |
| `style_id` | Determina quais imagens são exibidas para o cartão do produto. Por exemplo, diferentes `style_ids` exibem imagens de cartão de produto exclusivas. |
| `campaign_id` | ID único para a campanha de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Entradas opcionais

| Entrada | Descrição |
|-------------|-------------|
| `item_id` | Representa o item semente. Necessário para estratégias baseadas em item-item, como alternativas, complementares, pacotes. Por exemplo, o primeiro item em um e-mail é o item semente, com itens subsequentes como alternativas. |
| `num_results` | Número de produtos a serem adicionados ao e-mail. O padrão é 10, até 100. Por exemplo, `num_results = 3` significa que três recomendações são adicionadas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

