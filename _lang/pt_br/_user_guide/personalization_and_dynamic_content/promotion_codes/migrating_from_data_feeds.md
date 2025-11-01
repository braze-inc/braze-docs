---
nav_title: Migração de feeds de dados para códigos promocionais
article_title: Migração de feeds de dados para códigos promocionais
page_order: 0
description: "Este artigo de referência fornece orientação sobre a migração de feeds de dados para códigos promocionais."
---

# Migração de feeds de dados para códigos promocionais

{% alert note %}
Os feeds de dados estão sendo descontinuados. A Braze recomenda que os clientes que usam Data Feeds passem a usar listas de códigos promocionais.
{% endalert %}

> Esta página o orienta na migração de feeds de dados para códigos promocionais. Esse é um processo simples que envolve a criação manual de listas de códigos promocionais com as informações de seus feeds de dados e a atualização adequada das referências de mensagens.

## Recursos e funcionalidade

Há algumas diferenças entre as listas de códigos promocionais e os feeds de dados.

| Recurso          | Códigos promocionais | Feeds de dados   |
|------------------|-----------------|--------------|
| Descrições     | Sim             | Não           |
| Datas de vencimento | Sim             | Não           |
| Método de criação  | Como fazer upload de um CSV | Colar texto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Como migrar

Para substituir um feed de dados por uma lista de códigos promocionais, faça o seguinte: 

1. Vá para **Data Settings (Configurações de dados** ) e selecione **Create Promotion Code List (Criar lista de códigos promocionais**).
2. [Configure sua lista de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. Navegue até suas mensagens que anteriormente faziam referência ao Data Feed e atualize-as para usar a lista de códigos promocionais.