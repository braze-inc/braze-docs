---
nav_title: APIs de exportação
article_title: APIs de exportação
page_order: 8
page_type: reference
description: "Este artigo de referência descreve por que você pode exportar programaticamente um arquivo JSON de dados do painel, em vez de exportar um CSV diretamente do painel."
platform: API

---

# APIs de exportação

> Esta página aborda as APIs de exportação do Braze, que permitem que você exporte programaticamente um arquivo JSON de dados do painel. Consulte [Exportar pontos de extremidade]({{site.baseurl}}/api/endpoints/export/) para obter uma lista de dados que você pode acessar, incluindo instruções e exemplos de código para a exportação.

## Quando usar APIs de exportação em vez de downloads do CVS

Há alguns motivos para você preferir esse método em vez de exportar um CSV diretamente do painel:

 - Seu arquivo é muito grande. Em nosso painel, você pode exportar um CSV com no máximo 500.000 linhas. Se você estiver exportando dados de um segmento com mais de 500.000 usuários, precisará usar nossa API de exportação, que não tem limite de quantidade que pode ser exportada.
 -  Você deseja interagir com os dados de forma programática.

{% alert tip %}
Para obter ajuda com exportações de CSV e API, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

