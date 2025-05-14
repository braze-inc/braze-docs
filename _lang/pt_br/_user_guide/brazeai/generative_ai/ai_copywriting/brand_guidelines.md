---
nav_title: Diretrizes da marca
article_title: Diretrizes da marca para redação com IA
page_order: 1
description: "Este artigo de referência aborda as diretrizes da marca para o assistente de copywriting de IA, um recurso que permite adaptar o estilo da cópia gerada pelo assistente de copywriting de IA à voz e ao estilo de sua marca."
---

# Diretrizes da marca para o assistente de Copywriting de IA

> Adapte o estilo de sua cópia gerada por IA para que corresponda à voz e à personalidade de sua marca com as diretrizes personalizadas da marca.

## Criação de diretrizes da marca {#steps}

Siga estas etapas para criar diretrizes da marca no assistente de copywriting da IA. Você também pode criar diretrizes da marca na página de configurações [Diretrizes da marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

### Etapa 1: Crie uma diretriz para a marca

1. Em seu criador de mensagens, selecione <i class="fa-solid fa-wand-magic-sparkles"></i> **Abrir AI Copywriter**.
   * No editor de arrastar e soltar para mensagens no app, selecione um bloco de texto e selecione <i class="fa-solid fa-wand-magic-sparkles" title="IA Copywriter"></i> na barra de ferramentas do bloco.
2. Selecione **Aplicar diretriz da marca** e, em seguida, **Criar uma diretriz da marca**.
3. Digite um nome para essa diretriz. Será o rótulo que você vê na seleção anterior.
4. Para **Quando você usará essas diretrizes da marca?**, adicione detalhes para ajudar seus colegas (e você no futuro) a entender o contexto de uso dessa diretriz.
5. Se quiser que essa seja a diretriz de marca padrão para o espaço de trabalho atual, marque **Usar como diretriz de marca padrão**.

![Visualização da criação da diretriz da marca.][1]

### Etapa 2: Descreva a personalidade de sua marca

Para a **personalidade da marca**, pense no que torna sua marca única. Inclua características, valores, voz e quaisquer arquétipos que definam sua marca. Aqui estão algumas características a serem consideradas:

| **Característica**       | **Definição**                                                                       | **Exemplo**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputação               | Como você deseja que sua marca seja percebida no mercado.                               | Somos conhecidos por sermos a marca mais confiável e focada no cliente em nosso setor. |
| Traços de personalidade       | Características semelhantes às humanas que descrevem o caráter de sua marca.                     | Nossa marca é amigável, acessível e sempre otimista.          |
| Valores                   | Valores essenciais que orientam as ações e decisões de sua marca.                           | Valorizamos a sustentabilidade, a transparência e a comunidade.            |
| Diferenciação          | Qualidades exclusivas que diferenciam sua marca da concorrência.                         | Nós nos destacamos pelo fato de oferecermos um atendimento personalizado ao cliente que vai muito além. |
| Voz da marca              | O tom e o estilo de comunicação usados por sua marca.                                 | Nossa voz é informal, porém informativa, garantindo clareza sem ser muito formal. |
| Arquétipo da marca          | O arquétipo que representa a persona de sua marca (O Herói, O Criador etc.).    | Incorporamos o arquétipo do "explorador", sempre buscando novos desafios e aventuras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 3: Definir a linguagem que deve ser evitada (opcional)

Para **Exclusões**, liste qualquer linguagem ou estilo que não esteja alinhado com sua marca. Por exemplo, talvez você queira evitar "sarcasmo", "atitudes negativas" ou tons "condescendentes".

### Etapa 4: Teste suas diretrizes

Teste suas diretrizes para ver como elas se comportam. Expanda **Teste suas diretrizes** para gerar exemplos de cópia e ajuste conforme necessário.

### Etapa 5: Salve suas diretrizes

Quando estiver satisfeito com suas diretrizes, selecione **Save brand guideline (Salvar diretriz da marca**). Suas novas diretrizes serão salvas em seu espaço de trabalho para uso futuro.

{% alert important %}
Você pode alterar o idioma de saída independentemente do idioma em que seu texto está, mas nem a Braze nem a OpenAI garantem a qualidade da tradução. Sempre teste e verifique as traduções antes de usá-las.
{% endalert %}

## Diretrizes de edição

Para editar suas diretrizes de marca existentes:

1. Abra o Assistente de Copywriting com IA.
2. Aplique as diretrizes da marca que você deseja alterar. Um botão aparecerá próximo ao campo.
3. Selecione **Editar diretriz**.

## Como meus dados são usados e enviados para a OpenAI?

Para gerar uma cópia usando uma diretriz da marca, a Braze enviará sua consulta, incluindo o conteúdo da sua diretriz, para a OpenAI. Todas as consultas enviadas pela Braze à OpenAI são anônimas, o que significa que a OpenAI não poderá identificar o remetente da consulta, a menos que você inclua informações exclusivamente identificáveis na entrada fornecida ou nos dados de sua campanha anterior ao ativar a opção "Faz referência a dados de campanhas antigas". De acordo com a [política da OpenAI](https://openai.com/policies/api-data-usage-policies), os dados enviados à API da OpenAI via Braze não são usados para treinar ou aprimorar seus modelos e serão excluídos após 30 dias. Entre você e a Braze, qualquer conteúdo gerado usando GPT é de sua propriedade intelectual. A Braze não fará valer nenhuma reivindicação de propriedade de direitos autorais sobre tal conteúdo e não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA.


[1]: {% image_buster /assets/img/ai_copywriter/manual_brand_guidelines.png %} "Diretrizes da marca"
