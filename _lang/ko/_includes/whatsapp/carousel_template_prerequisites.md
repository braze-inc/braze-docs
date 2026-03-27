[캐러셀 템플릿을 생성]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/template_builder/whatsapp_carousel_templates/#create-a-carousel-template)하기 이전에 다음이 필요합니다:
- Braze에 연결된 활성 WhatsApp Business 계정(WABA)
- WABA 내에 구성된 적절한 구독 그룹
- 업로드할 미디어 자산(이미지 또는 동영상)
- 관리자가 아닌 사용자를 위한 Braze 권한
    - 사용자가 템플릿 빌더에서 새 템플릿을 생성하려면:
        - "WhatsApp 메시지 템플릿 보기"
        - "WhatsApp 메시지 템플릿 편집"
    - 사용자가 캐러셀 템플릿으로 캠페인 또는 캔버스를 작성하려면:
        - "WhatsApp 메시지 템플릿 보기"
- Liquid 템플릿에 대한 이해(선택 사항, 동적 콘텐츠용)

{% alert important %}
동일한 WhatsApp Business 계정(WABA) 내의 모든 전화번호와 구독 그룹은 템플릿을 공유합니다. 하나의 WABA 내에 다중 구독 그룹이 있는 경우 모두 동일한 캐러셀 템플릿에 액세스할 수 있지만, 서로 다른 WABA 간에는 템플릿이 공유되지 않습니다.
{% endalert %}