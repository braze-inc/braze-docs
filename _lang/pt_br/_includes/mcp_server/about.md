# O servidor Braze MCP

> Saiba mais sobre o servidor Braze MCP, uma conexão segura e somente leitura que permite que ferramentas de IA como Claude e Cursor acessem dados Braze sem IPI para responder a perguntas, analisar tendências e fornecer insights sem alterar os dados.

{% multi_lang_include mcp_server/beta_alert.md %}

## O que é o protocolo de contexto de modelo (MCP)?

​O Model Context Protocol, ou MCP, é um padrão que permite que os agentes de IA se conectem e trabalhem com dados de outra plataforma. Ele tem duas partes principais:

- **Cliente MCP:** O aplicativo em que o agente de IA é executado, como o Cursor ou o Claude.
- **Servidor MCP:** Um serviço prestado por outra plataforma, como o Braze, que define quais ferramentas a IA pode usar e quais dados pode acessar.

## Sobre o servidor Braze MCP

Depois de [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, você pode conectar ferramentas de IA como agentes, assistentes e chatbots diretamente ao Braze, permitindo que eles leiam dados agregados, como análises do Canva e do Campaign, atributos personalizados, segmentos e muito mais. O servidor Braze MCP é ótimo para:

- Criando ferramentas baseadas em IA que precisam do contexto do Braze.
- Engenheiros de CRM criando fluxos de trabalho de agentes em várias etapas.
- Profissionais de marketing técnico fazendo experiências com consultas em linguagem natural.

O servidor MCP da Braze suporta 38 pontos de extremidade somente leitura que não retornam dados de perfis de usuários da Braze. Você pode optar por atribuir apenas alguns desses endpoints à sua chave de API do Braze para restringir ainda mais os dados que um agente pode acessar.

{% alert warning %}
Não atribua permissões à sua chave de API que **não** sejam somente leitura. Os agentes podem tentar gravar ou excluir dados no Braze, o que pode causar consequências não intencionais.
{% endalert %}

## Exemplo de uso

Você pode interagir com o Braze por meio de linguagem natural usando ferramentas como Claude ou Cursor. Para obter outros exemplos e práticas recomendadas, consulte [Usando o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
!["Quais são as minhas funções disponíveis no Braze?" sendo perguntado e respondido em Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!["Quais são minhas funções Braze disponíveis" sendo perguntadas e respondidas no Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Perguntas Frequentes (FAQ) {#faq}

### Quais clientes MCP são compatíveis?

Somente [o Claude](https://claude.ai/) e [o Cursor](https://cursor.com/) são oficialmente compatíveis. Você deve ter uma conta em um desses clientes para usar o servidor Braze MCP.

### Quais dados do Braze meu cliente MCP pode acessar?

Os clientes MCP só podem acessar pontos de extremidade somente leitura que não foram criados para recuperar IPI. Eles não podem manipular dados no Braze.

### Meu cliente MCP pode manipular dados do Braze?

Não. O servidor MCP expõe apenas ferramentas que lidam com dados não IPI e somente leitura.

### Posso usar um servidor MCP de terceiros para o Braze?

O uso de um servidor MCP de terceiros para dados do Braze não é recomendado. Use apenas o servidor oficial Braze MCP hospedado no [PyPi](https://pypi.org/project/braze-mcp-server/).

### Por que o servidor Braze MCP não oferece acesso IPI ou de gravação?

Para proteger os dados e, ao mesmo tempo, ativar a inovação, o servidor está limitado a pontos de extremidade que são somente de leitura e que normalmente não retornam IPI. Isso reduz o risco e, ao mesmo tempo, oferece suporte a casos de uso valiosos.

### Posso reutilizar minhas chaves de API?

Não. Você precisará criar uma nova chave de API para seu cliente MCP. Lembre-se de conceder às suas ferramentas de IA acesso apenas àquilo com que você se sente confortável e evite permissões elevadas.

### O servidor Braze MCP está hospedado em uma localização local ou remota?

O servidor Braze MCP é hospedado em uma localização local.

### Por que o Cursor está listando apenas funções?

Verifique se você está no modo de solicitação ou no modo de agente. Para usar o servidor MCP, você precisa estar no modo agente.

### O que devo fazer quando o agente retorna uma resposta que parece incorreta?

Ao trabalhar com ferramentas como o Cursor, você pode tentar alterar o modelo usado. Por exemplo, se estiver definido como automático, tente alterá-lo para um modelo específico e faça experiências para descobrir qual modelo tem a melhor performance para o seu caso de uso. Você também pode tentar iniciar um novo bate-papo e tentar novamente o prompt. 

Se os problemas persistirem, envie um e-mail para [mcp-product@braze.com](mailto:mcp-product@braze.com) para nos informar. Se possível, inclua um vídeo e expanda as funções de chamada para que possamos ver as chamadas que o agente tentou fazer.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
