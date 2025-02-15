---
nav_title: Testes
article_title: Teste de cartões de conteúdo
page_order: 3
description: "Este artigo de referência aborda como fazer a prévia e testar os cartões de conteúdo, bem como algumas práticas recomendadas."
channel:
  - content cards
  
---

# Teste de cartões de conteúdo

> É extremamente importante sempre testar seus cartões de conteúdo antes de enviar suas campanhas. Nossos recursos de prévia e teste oferecem duas maneiras de dar uma olhada nos seus cartões de conteúdo. É possível fazer uma prévia da mensagem para ajudá-lo a visualizar enquanto a cria, além de enviar uma mensagem de teste para si mesmo ou para o dispositivo de um usuário específico. Recomendamos que você tire proveito de ambos.

## Prévia

Você pode fazer uma prévia do cartão à medida que o cria. Isso deve ajudá-lo a visualizar como será a mensagem final do ponto de vista do usuário.

Na guia **Pré-visualização** do seu criador, a visualização da sua mensagem pode não ser idêntica à renderização real no dispositivo do usuário. Recomendamos sempre enviar uma mensagem de teste para um dispositivo para garantir que a mídia, o texto, a personalização e os atributos personalizados sejam gerados corretamente.

## Testar

Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve estar ativado nos dispositivos de teste com tokens por push válidos registrados para o usuário teste antes do envio. Para usuários de iOS, é necessário tocar na notificação por push enviada pelo Braze para visualizar o cartão de conteúdo do teste. Esse comportamento só se aplica a cartões de conteúdo de teste.

### Ver prévia de mensagem como usuário

Também é possível fazer a prévia das mensagens na guia **Teste** como se fosse um usuário. Você pode selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado.

![Custom_User_Preview][3]

### Lista de verificação de teste

- As imagens e a mídia aparecem e funcionam conforme o esperado?
- O Liquid funciona conforme o esperado? Você considerou um [valor de atribuição padrão]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) no caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
- Seus links direcionam o usuário para onde ele deve acessar?

## Depurar

Depois que os cartões de conteúdo forem enviados, você poderá analisar ou depurar quaisquer problemas no [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/) no console do desenvolvedor. 

Um caso de uso comum é tentar depurar por que um usuário não consegue ver um determinado cartão de conteúdo. Para isso, é possível procurar nos **registros de usuários de eventos** os cartões de conteúdo entregues ao SDK no início da sessão, mas antes de uma impressão, e rastreá-los até uma campanha específica:

1. Acesse **Configurações** > Registro de usuários de eventos.
{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar o **registro de usuários de eventos** no **console do desenvolvedor**.
{% endalert %}

{:start="2"}
2\. Localize e expanda a Solicitação de SDK para seu usuário teste.
3\. Clique em **Raw Data (Dados brutos**).
4\. Encontre o `id` para sua sessão. A seguir, um exemplo de trecho:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NjE4NTAwNWE5ZDliZWU3OTM4N2NjZTQzXyRfY2M9YzNiMjU3NDAtZjExMy1jMDQ3LTRiMWQtZDI5NmYyODBhZjRmJm12PTYxODUwMDViOWQ5YmVlNzkzODdjY2U0NSZwaT1jbXA="
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Use uma ferramenta de decodificação como [Base64 Decode and Encode](https://www.base64decode.org/) para decodificar o `id` do formato Base64 e encontrar o `campaign_id` associado. Em nosso exemplo, isso resulta no seguinte:

    ```
    6185005a9d9bee79387cce43_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Onde `6185005a9d9bee79387cce43` é o `campaign_id`.<br><br>

6. Acesse a página **Campanhas** e pesquise o endereço `campaign_id`.

![Pesquisar campaign_id na página Campaigns][1]

A partir daí, é possível revisar as configurações e o conteúdo das mensagens para detalhar e determinar por que um usuário não consegue ver um determinado cartão de conteúdo.

[1]: {% image_buster /assets/img_archive/cc_debug.png %}
[3]: {% image_buster /assets/img/cc-user-preview.png %}
