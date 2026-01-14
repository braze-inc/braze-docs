---
nav_title: Testes
article_title: Teste de cartões de conteúdo
page_order: 3
description: "Este artigo de referência aborda como visualizar e testar os cartões de conteúdo, bem como algumas práticas recomendadas."
channel:
  - content cards
  
---

# Teste de cartões de conteúdo

> É extremamente importante sempre testar seus Content Cards antes de enviar suas campanhas. Nossos recursos de visualização e teste oferecem duas maneiras de dar uma olhada nos seus Content Cards. Você pode pré-visualizar sua mensagem para ajudá-lo a visualizar enquanto a compõe, bem como enviar uma mensagem de teste para si mesmo ou para o dispositivo de um usuário específico. Recomendamos que você tire proveito de ambos.

## Prévia

Você pode visualizar seu cartão à medida que o compõe. Isso deve ajudá-lo a visualizar como será a mensagem final do ponto de vista do usuário.

Na guia **Preview (Visualização** ) do seu compositor, a visualização da mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Recomendamos sempre enviar uma mensagem de teste a um dispositivo para garantir que sua mídia, cópia, personalização e atributos personalizados sejam gerados corretamente.

## Teste

Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve estar ativado em seus dispositivos de teste com tokens push válidos registrados para o usuário de teste antes do envio. Para usuários do iOS, é necessário tocar na notificação por push enviada pelo Braze para visualizar o Content Card do teste. Esse comportamento só se aplica a cartões de conteúdo de teste.

### Visualizar mensagem como usuário

Você também pode visualizar mensagens na guia **Teste** como se fosse um usuário. É possível selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado.

Visualização de um Content Card na guia "Test" (Teste).]({% image_buster /assets/img/cc-user-preview.png %}){: style="max-width:80%;"}

### Lista de verificação de teste

- As imagens e a mídia aparecem e funcionam como esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atributo padrão]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) para o caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus links direcionam o usuário para onde ele deve ir?

## Depurar

Depois que seus Content Cards forem enviados, você poderá analisar ou depurar quaisquer problemas no [Log do usuário de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) no Console do desenvolvedor. 

Um caso de uso comum é tentar depurar por que um usuário não consegue ver um Content Card específico. Para isso, você pode procurar nos **Logs de usuário de eventos** os Content Cards entregues ao SDK no início da sessão, mas antes de uma impressão, e rastreá-los até uma campanha específica:

1. Vá para **Configurações** > **Registro de usuário de eventos**.
2. Localize e expanda a Solicitação de SDK para seu usuário de teste.
3. Clique em **Raw Data (Dados brutos**).
4. Encontre o site `id` para sua sessão. A seguir, um exemplo de trecho:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Use uma ferramenta de decodificação como [Base64 Decode and Encode](https://www.base64decode.org/) para decodificar o `id` do formato Base64 e encontrar o `campaign_id` associado. Em nosso exemplo, isso resulta no seguinte:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Onde `4861692e-6fce-4215-bd05-3254fb9e9057` é o `campaign_id`.<br><br>

6. Vá para a página **Campanhas** e pesquise `campaign_id`.

\![Procure por campaign_id na página Campanhas]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

A partir daí, você pode revisar as configurações e o conteúdo da mensagem para detalhar e determinar por que um usuário não pode ver um Content Card específico.

