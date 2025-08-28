---
nav_title: APIs de exportação
article_title: APIs de exportação
page_order: 8
page_type: reference
description: "Este artigo de referência descreve por que você pode exportar programaticamente um arquivo JSON de dados do dashboard, em vez de exportar um CSV diretamente do dashboard."
platform: API

---

# APIs de exportação

> Esta página aborda as APIs de exportação do Braze, que permitem exportar programaticamente um arquivo JSON de dados do dashboard. Consulte [Exportar endpoints]({{site.baseurl}}/api/endpoints/export/) para obter uma lista de dados que você pode acessar, incluindo instruções e exemplos de código para a exportação.

## Quando usar APIs de exportação em vez de baixar o CVS

Há alguns motivos para você preferir esse método em vez de exportar um CSV diretamente do dashboard:

 - Seu arquivo é muito grande. Em nosso dashboard, você pode exportar um CSV com no máximo 500.000 linhas. Se estiver exportando dados de um segmento com mais de 500.000 usuários, precisará usar nossa API de exportação, que não tem limite de quantidade para exportação.
 -  Você deseja interagir com os dados de forma programática.

{% alert tip %}
Para obter ajuda com exportações CSV e API, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

