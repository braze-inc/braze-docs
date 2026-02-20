    EVENT["WHATSAPP_EVENT"] {
        string id PK
        string campaign_id FK
        string campaign_updated_at
        string canvas_id FK
        string canvas_updated_at
        string canvas_step_id FK
        string canvas_step_updated_at
        string canvas_step_message_variation_id FK
        string canvas_step_message_variation_updated_at
        string canvas_variation_id FK
        string device_id FK
        string message_variation_id FK
        string message_variation_updated_at
        string user_id FK
        string abort_log
        string abort_type
        string action
        string app_group_id
        string dispatch_id
        string event_type
        string external_user_id
        string inbound_phone_number
        string media_urls
        string message_body
        string message_extras
        string quick_reply_text
        string subscription_group_id
        string time
        string timezone
        string to_phone_number
        string send_id
        string from_phone_number
        string provider_error_code
        string provider_error_title
    }
