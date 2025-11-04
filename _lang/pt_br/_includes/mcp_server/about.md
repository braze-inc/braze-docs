# O servidor MCP do Braze

> Saiba mais sobre o servidor MCP do Braze, uma conexão segura e somente leitura que permite que ferramentas de IA como Claude e Cursor acessem dados do Braze que não são PII para responder perguntas, analisar tendências e fornecer insights sem alterar os dados.

{% multi_lang_include mcp_server/beta_alert.md %}

## O que é o Protocolo de Contexto de Modelo (MCP)?

​O Protocolo de Contexto de Modelo, ou MCP, é um padrão que permite que agentes de IA se conectem e trabalhem com dados de outra plataforma. Ele tem duas partes principais:

- **MCP cliente:** O aplicativo onde o agente de IA é executado, como Cursor ou Claude.
- **MCP servidor:** Um serviço fornecido por outra plataforma, como o Braze, que define quais ferramentas a IA pode usar e quais dados ela pode acessar.

## Sobre o servidor MCP do Braze

Após [configurar o servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, você pode conectar ferramentas de IA como agentes, assistentes e chatbots diretamente ao Braze, permitindo que eles leiam dados agregados, como análises de Canvas e Campanha, atributos personalizados, segmentos e mais. O servidor MCP do Braze é ótimo para:

- Construir ferramentas impulsionadas por IA que precisam do contexto do Braze.
- Engenheiros de CRM criando fluxos de trabalho de agentes em múltiplas etapas.
- Profissionais de marketing técnico experimentando com consultas em linguagem natural.

O servidor MCP do Braze suporta 38 endpoints somente leitura que não retornam dados dos perfis de usuários do Braze. Você pode escolher atribuir apenas alguns desses endpoints à sua chave de API do Braze para restringir ainda mais quais dados um agente pode acessar.

{% alert warning %}
Não atribua permissões à sua chave de API que sejam **não** somente leitura. Agentes podem tentar escrever ou excluir dados no Braze, o que pode causar consequências indesejadas.
{% endalert %}

## Exemplo de uso

Você pode interagir com o Braze através de linguagem natural usando ferramentas como Claude ou Cursor. Para outros exemplos e melhores práticas, veja [Usando o servidor MCP do Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
!['Quais são minhas funções disponíveis do Braze?' sendo perguntado e respondido no Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Quais são minhas funções disponíveis do Braze' sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Perguntas Frequentes (FAQ) {#faq}

### Quais clientes MCP são suportados?

Atualmente, apenas [Claude](https://claude.ai/) e [Cursor](https://cursor.com/) são oficialmente suportados. Você precisará de uma conta para um desses clientes para usar o servidor MCP do Braze.

### Quais dados do Braze meu cliente MCP pode acessar?

Os clientes MCP só podem acessar endpoints somente leitura que não são construídos para recuperar PII. Eles não podem manipular dados no Braze.

### Meu cliente MCP pode manipular dados do Braze?

Não. O servidor MCP apenas expõe ferramentas que lidam com dados não-PII, somente leitura.

### Posso usar um servidor MCP de terceiros para o Braze?

Usar um servidor MCP de terceiros para dados do Braze não é recomendado. Use apenas o servidor MCP oficial do Braze hospedado em [PyPi](https://pypi.org/project/braze-mcp-server/).

### Por que o servidor MCP do Braze não oferece PII ou acesso de gravação?

Para proteger os dados enquanto ainda possibilita inovação, construímos o servidor para ser limitado a endpoints que são somente leitura e não retornam tipicamente PII. Isso reduz o risco enquanto apoia casos de uso valiosos.

### Posso reutilizar minhas chaves de API?

Não. Você precisará criar uma nova chave de API para seu cliente MCP. Lembre-se de dar acesso às suas ferramentas de IA apenas ao que você se sente confortável e evite permissões elevadas.

### O servidor MCP do Braze está hospedado localmente ou remotamente?

Atualmente, o servidor MCP do Braze está hospedado localmente.

### Por que o Cursor está listando apenas funções?

Verifique se você está no modo de pergunta ou no modo de agente. Para usar o servidor MCP, você precisa estar no modo de agente.

### O que eu faço quando o agente retorna uma resposta que parece incorreta?

Ao trabalhar com ferramentas como o Cursor, você pode querer tentar mudar o modelo utilizado. Por exemplo, se você tiver configurado para automático, tente mudar para um modelo específico e experimente para descobrir qual modelo funciona melhor para seu caso de uso. Você também pode tentar iniciar um novo chat e repetir o prompt. 

Se os problemas persistirem, você pode nos enviar um e-mail para [mcp-product@braze.com](mailto:mcp-product@braze.com) para nos informar. Se possível, inclua um vídeo e expanda as funções de chamada para que possamos ver quais chamadas o agente tentou.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
