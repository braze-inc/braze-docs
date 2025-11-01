---
nav_title: Diretrizes da marca
article_title: Diretrizes da marca
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como criar, gerenciar e usar diretrizes de marca que podem ser aplicadas às suas mensagens por meio do assistente de redação de IA."
---

# Diretrizes da marca

> Adapte o estilo de sua cópia gerada por IA para corresponder à voz, ao tom e à personalidade de sua marca com diretrizes de marca personalizadas.

Você pode criar e gerenciar suas diretrizes de marca acessando **Configurações** > **Diretrizes de marca**. Você também pode criá-los no [assistente de redação de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines/).

## Criação de diretrizes de marca

### Etapa 1: Criar uma diretriz de marca

Na página **Diretrizes de marca**, selecione **Criar novo**. Se você quiser que essa diretriz de marca seja a padrão para o espaço de trabalho, marque **Usar como diretriz de marca padrão**. Você pode ter um padrão por espaço de trabalho.

### Etapa 2: Descreva a personalidade de sua marca

Para a **personalidade da marca**, pense no que torna sua marca única. Inclua características, valores, voz e quaisquer arquétipos que definam sua marca. Aqui estão algumas características a serem consideradas:

| **Característica**       | **Definição**                                                                       | **Exemplo**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputação               | Como você deseja que sua marca seja percebida no mercado.                               | Somos conhecidos por sermos a marca mais confiável e focada no cliente em nosso setor. |
| Traços de personalidade       | Características semelhantes às humanas que descrevem o caráter de sua marca.                     | Nossa marca é amigável, acessível e sempre otimista.          |
| Valores                   | Valores essenciais que orientam as ações e decisões de sua marca.                           | Valorizamos a sustentabilidade, a transparência e a comunidade.            |
| Diferenciação          | Qualidades exclusivas que diferenciam sua marca da concorrência.                         | Nós nos destacamos por oferecer um atendimento personalizado ao cliente que vai além do esperado. |
| Voz da marca              | O tom e o estilo de comunicação usados por sua marca.                                 | Nossa voz é informal, porém informativa, garantindo clareza sem ser muito formal. |
| Arquétipo da marca          | O arquétipo que representa a persona de sua marca (O Herói, O Criador, etc.).    | Incorporamos o arquétipo do "explorador", sempre buscando novos desafios e aventuras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 3: Definir a linguagem que deve ser evitada (opcional)

Para **Exclusões**, liste qualquer linguagem ou estilo que não esteja alinhado com sua marca. Por exemplo, talvez você queira evitar "sarcasmo", "atitudes negativas" ou tons "condescendentes".

A janela "Criar diretriz de marca" com campos para inserir o nome, a descrição, a personalidade, as exclusões e o tom.]({% image_buster /assets/img/guidelines_create.png %})

### Etapa 4: Teste suas diretrizes

Teste suas diretrizes para ver como elas se comportam. Expandir **Teste suas diretrizes** para gerar exemplos de cópia e ajuste conforme necessário.

### Etapa 5: Salve suas diretrizes

Quando estiver satisfeito com suas diretrizes, selecione **Save brand guideline (Salvar diretriz da marca**). Suas novas diretrizes serão salvas em seu espaço de trabalho para uso futuro.

{% alert important %}
Você pode alterar o idioma de saída independentemente do idioma em que sua cópia está, mas nem o Braze nem a OpenAI garantem a qualidade da tradução. Sempre teste e verifique as traduções antes de usá-las.
{% endalert %}

## Gerenciamento das diretrizes da marca

Você pode editar as diretrizes da marca selecionando-as na página **Diretrizes da marca**. Arquive uma diretriz de marca para torná-la inativa e removê-la do assistente de redação de IA. Para torná-lo ativo e selecionável novamente, você pode filtrar as diretrizes de marca arquivadas e, em seguida, desarquivá-las.

\![A página "Diretrizes da marca" filtrou as diretrizes da marca arquivadas.]({% image_buster /assets/img/unarchive_brand_guideline.png %})

## Uso de diretrizes de marca

Ao redigir uma mensagem, abra o [assistente de redação de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/) e selecione a diretriz de sua marca no menu suspenso **Aplicar diretriz de marca**. Se você designar uma diretriz de marca específica como padrão, ela será automaticamente selecionada no menu suspenso, mas você pode escolher uma diretriz diferente. 

\!["Assistente de redação de IA com "Alertas importantes!!!" selecionado como a diretriz da marca.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}
