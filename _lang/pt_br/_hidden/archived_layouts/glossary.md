---
nav_title: Glossário
article_title: Layout do glossário
page_order: 0
noindex: true
---

# Exemplo de layout: Glossário

> O layout do glossário está em YAML. Ele requer vários componentes e parâmetros. Os layouts de glossário são bons para conteúdo pesquisável com localização, como dicionários e categorias específicas de conteúdo.

## Componentes necessários

1. Notação de abertura e fechamento do YAML. Em outras palavras, `---` antes do conteúdo e `---` depois. 
2. Aspas em torno de determinados conteúdos de parâmetros. (Parâmetros de cabeçalho, parâmetros de texto, conteúdo com hífens ou outros caracteres especiais.)
3. Notação das tags do glossário (Essas são tags de filtro)

## Parâmetros necessários

|Parâmetro | Tipo de conteúdo | Informações |
|---|---|---|
|`page_order`| numérico | Ordene a página dentro da seção. Essa ordem será refletida na navegação à esquerda. |
| `nav-title`| Alfanumérico | Título que aparecerá na navegação à esquerda. |
|`layout`| Alfanumérico - Sem espaços | Selecione um layout na [seção de layout](https://github.com/Appboy/braze-docs/tree/develop/_layouts) da documentação. | 
|`glossary_top_header` | Alfanumérico | Requer aspas duplas. O título aparece na parte superior da página. |
|`glossary_top_text`| String, alfanumérico | Descreva sua página de glossário. Isso aparecerá acima da barra de pesquisa e dos filtros (se você optar por tê-los). É essencialmente escrito em HTML, portanto, você pode usar \`\`\`<br> para criar quebras de linha. | 
|`glossary_tag_name` | Palavra única, alfanumérico | Dê um nome aos seus filtros. Elas aparecerão em caixas de seleção abaixo da barra de pesquisa e também nos dados abaixo. | 
|`glossary_filter_text`| String, alfanumérico | Descreva seus filtros. Geralmente usado para instruir. | 
|`glossary_tags`| Mais conteúdo YAML plus. | Formato como mostrado abaixo: <br> glossary_tags: <br>  \- nome: Cartões de conteúdo <br>  \- nome: E-mail | 
| `glossaries`| Mais conteúdo YAML plus. | Consulte [os parâmetros dos glossários](#glossaries-parameters) abaixo. |

### Parâmetros de glossários

|Parâmetro | Tipo de conteúdo | Informações |
|---|---|---|
|`name`| Alfanumérico | Dê um nome ao seu item do glossário.| 
|`description`| String, alfanumérico | Descreva o item do glossário. | 
|`calculation`| String | (opcional) Descreva como o item do glossário é calculado (geralmente usado ao descrever dados ou métricas). | 
|`tags`| Alfanumérico | Deve corresponder ao que está listado como `name` em `glossary_tags`. Liste quantos forem aplicáveis. Ao escrever `All`, o item será incluído em todos os filtros.|

## Exemplo

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
