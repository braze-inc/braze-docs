---
nav_title: Sobreposição da Barra de Rolagem
article_title: Sobreposição da Barra de Rolagem
page_order: 0

page_type: solution
description: "Este artigo de ajuda orienta os usuários de Mac sobre como resolver a sobreposição das barras de rolagem no conteúdo dentro dos documentos do Braze."
---

# Sobreposição da barra de rolagem

Você está usando um Mac e acha que suas barras de rolagem estão sobrepondo o conteúdo dentro dos documentos do Braze como no exemplo a seguir?

![Exemplo de sobreposição da barra de rolagem][1]

Verifique se a sua barra de rolagem sobrepõe o seguinte bloco de código:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

Se a barra de rolagem sobrepor o bloco de código, sugerimos alterar a configuração **Mostrar barras de rolagem:** para **Sempre** em suas **Configurações Gerais**. Isso expandirá os recursos em documentos (como blocos de código) para sempre mostrar a barra de rolagem e evitar a ilegibilidade.

![Configurações Gerais para MacOS][2]

Veja como sua barra de rolagem atualizada deve ser:

![Exemplo de barra de rolagem fixa sem sobreposição][3]

_Última atualização em 27 de março de 2019_

{% comment %}
Insira isso onde há uma única LINE de código longo que pode causar problemas:
_Não consegue ver o código por causa da barra de rolagem? Veja como corrigir isso [aqui]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)._
{% endcomment %}

[1]: {% image_buster /assets/img/scroll-overlap.png %}
[2]: {% image_buster /assets/img/general-on-mac.png %}
[3]: {% image_buster /assets/img/scroll-bar-on.png %}
