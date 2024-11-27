---
nav_title: Assistente de Liquid da BrazeAI™️
article_title: Assistente de Liquid da BrazeAI™️
description: "Este artigo abordará como o IA Liquid Assistant funciona e como você pode usá-lo para gerar snippets do Liquid para o envio de mensagens."
page_type: reference
page_order: 5
---

# Assistente líquido <sup>BrazeAITM</sup> 

> O Liquid Assistant do <sup>BrazeAITM</sup> é um assistente de bate-papo desenvolvido pelo <sup>BrazeAITM</sup> que ajuda a gerar o Liquid de que você precisa para personalizar o conteúdo das mensagens.

Com o Liquid Assistant do <sup>BrazeAITM</sup>, você pode gerar Liquid a partir de modelos, receber sugestões personalizadas de Liquid e otimizar o Liquid existente com o apoio do <sup>BrazeAITM</sup>. O Assistente também fornece anotações que explicam o Liquid usado, para que você possa aumentar sua compreensão do Liquid e aprender a escrever o seu próprio.

## Canais suportados

Você pode usar o Liquid Assistant do <sup>BrazeAITM</sup> ao criar: 
- Envio de mensagens SMS
- Notificações por push
- Envio de mensagens de e-mail em HTML
    - O assistente funciona em mensagens de e-mail e não em modelos, e funciona melhor em mensagens de e-mail que já foram criadas.
- Canvas

## Como funciona?

O Liquid Assistant da <sup>BrazeAI™</sup> foi projetado para ajudar na formulação de um código Liquid eficaz e adaptado às suas necessidades de marketing. Treinada na sintaxe do Liquid e em como os profissionais de marketing utilizam o Liquid em suas mensagens, nossa IA entende as nuances da elaboração de conteúdo personalizado. Além disso, ao fornecer ao Liquid Assistant do <sup>BrazeAITM</sup> seus nomes de atributos personalizados (como "favorite_color") e tipos de dados (como booleano e string), o Liquid Assistant do <sup>BrazeAITM</sup> garante que suas mensagens sejam direcionadas com precisão e alinhadas às suas metas. Além disso, se você criar diretrizes da marca, o Liquid Assistant da <sup>BrazeAITM</sup> poderá usar as diretrizes da marca para personalizar melhor os resultados gerados e personalizar o conteúdo de acordo com a voz da nossa própria marca. As diretrizes da marca que você criar serão usadas apenas para personalizar o conteúdo para seu próprio uso. 

## Geração de código Liquid

Para iniciar o Liquid Assistant da <sup>BrazeAI™</sup>, selecione o ícone do assistente de IA no criador de mensagens.

![Criador de mensagens com o assistente de IA.][1]{: style="max-width:50%;"}

Você pode escolher um [prompt fornecido](#provided-prompts) ou inserir o seu próprio na caixa de texto. Para gerar seu código Liquid, selecione **Atualizar criador**.

![Janela do assistente de IA com prompts fornecidos.][2]{: style="max-width:50%;"}
 
Você pode gerar outra mensagem usando o mesmo prompt, selecionando **Regenerate**. Para remover a mensagem e reverter para a anterior, selecione **Undo update (Desfazer atualização**).

### Prompts fornecidos

Ao usar o Liquid Assistant da <sup>BrazeAI™</sup>, você poderá ver uma variedade de prompts para ajudá-lo a começar a usar o Liquid. Alguns dos prompts estão listados abaixo.

#### Usar a atividade do app

O prompt **Usar atividade do aplicativo** gera código Liquid para ajudá-lo a enviar mensagens diferentes com base na última vez em que o aplicativo foi usado. Poderão ser feitas perguntas complementares para que o assistente possa gerar um resultado mais preciso.

![Exemplo de saída do prompt "Use app activity" (Usar atividade do app).][3]{: style="max-width:45%;"}

#### Adicionar contagem regressiva

Esse prompt gerará o código Liquid que envia uma mensagem com o tempo que falta para um evento acontecer. Ele solicitará que você forneça detalhes sobre a data e a hora do evento.

![Exemplo de saída do prompt "Add countdown" (Adicionar contagem regressiva).][4]{: style="max-width:45%;"}

#### Inspire-me

Esse prompt aparece quando há conteúdo em sua caixa de mensagens. Ele gera uma lista de opções que você pode escolher para personalizar sua mensagem com o Liquid. 

![Exemplo de saída do prompt "Inspire-me".][5]{: style="max-width:45%;"}

#### Aprimorar meu Liquid

Esse prompt é exibido quando há conteúdo em seu criador de mensagens. Selecione-o quando quiser que o assistente torne seu código mais eficiente e mais fácil de ler.

![Exemplo de saída do prompt "Improve my Liquid" (Melhorar meu Liquid).][6]{: style="max-width:45%;"}

## Atribuições suportadas na versão beta

| Critério | Tipo de conhecimento
| - | - |
| Liquid (incluindo `for` loops, `if` declarações, matemática e outros) | Codificação |
| Atribuições padrão e standard do usuário
| Atributos personalizados que possuem qualquer um desses tipos de dados: {::nomarkdown}<ul><li>Booleanos</li><li>Números</li><li>Strings</li><li>Matrizes</li><li>Horário</li></ul>{:/} | Atribuições
| Conteúdo conectado | Codificação | Conteúdo conectado
{: .reset-td-br-1 .reset-td-br-2 }

## Como meus dados são usados e enviados para a OpenAI?

Para modificar ou criar seu conteúdo de mensagem, a Braze enviará seus prompts, conteúdo de mensagens e/ou diretrizes da marca (se você decidir criá-los) enviados ao assistente de IA <sup>BrazeAITM</sup> para a Plataforma API da OpenAI. Todas as consultas enviadas pela Braze à OpenAI são anônimas, o que significa que a OpenAI não poderá identificar o remetente da consulta, a menos que você inclua informações exclusivamente identificáveis no conteúdo fornecido. Conforme detalhado nos [compromissos da plataforma de API da OpenAI](https://openai.com/policies/api-data-usage-policies), os dados enviados à API da OpenAI via Braze não são usados para treinar ou melhorar seus modelos e serão excluídos após 30 dias. Certifique-se de aderir às políticas da OpenAI relevantes para você, que podem incluir [as políticas de uso](https://openai.com/policies/usage-policies) e a [política de compartilhamento e publicação](https://openai.com/policies/sharing-publication-policy). A Braze não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA.

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
