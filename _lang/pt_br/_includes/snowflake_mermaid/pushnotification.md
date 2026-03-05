    EVENT["PUSH_NOTIFICATION_EVENT"] {
        string id PK
        string campaign_id FK
        string campaign_updated_at
        string canvas_id FK
        string canvas_updated_at
        string canvas_step_id FK
        string canvas_step_updated_at
        string canvas_variation_id FK
        string message_variation_id FK
        string message_variation_updated_at
        string canvas_step_message_variation_id FK
        string canvas_step_message_variation_updated_at
        string device_id FK
        string user_id FK
        string abort_type
        string abort_log
        string app_group_id
        string app_id
        string event_type
        string external_user_id
        string message_extras
        string send_id
        string time
        string timezone
    }
