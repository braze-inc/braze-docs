    EVENT["SMS_EVENT"] {
        string id PK
        string campaign_id FK
        string campaign_api_id FK
        string canvas_id FK
        string canvas_api_id FK
        string canvas_step_api_id FK
        string canvas_step_message_variation_api_id FK
        string canvas_variation_api_id FK
        string message_variation_api_id FK
        string user_id FK
        string abort_log
        string abort_type
        string action
        string app_group_api_id
        string app_group_id
        string category
        string country
        string device_id
        string dispatch_id
        string error
        string external_user_id
        string from_phone_number
        string gender
        string inbound_phone_number
        string is_sms_fallback
        string is_suspected_bot_click
        string language
        string media_urls
        string message_body
        string message_extras
        string provider_error_code
        string retry_log
        string retry_type
        string send_id
        string sf_created_at
        string short_url
        string subscription_group_api_id
        string subscription_group_id
        string suspected_bot_click_reason
        string time
        string timezone
        string to_phone_number
        string url
        string user_agent
        string user_phone_number
    }
