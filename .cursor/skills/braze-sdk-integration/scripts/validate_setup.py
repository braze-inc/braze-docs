#!/usr/bin/env python3
"""
Braze SDK setup validator and boilerplate generator.

Prompts for Braze API Key and SDK Endpoint, validates the endpoint format,
and generates a platform-appropriate configuration file (e.g. braze.xml for
Android, BrazeConfig.ts for Web).
"""

import re
import sys
from pathlib import Path

# Braze SDK endpoint: sdk.<cluster>.braze.com (no scheme)
ENDPOINT_PATTERN = re.compile(
    r"^sdk\.[a-z0-9-]+\.braze\.com$",
    re.IGNORECASE
)


def normalize_endpoint(value: str) -> str:
    """Strip whitespace and optional https:// prefix for validation."""
    s = (value or "").strip()
    if s.startswith("https://"):
        s = s[len("https://"):]
    if s.startswith("http://"):
        s = s[len("http://"):]
    if s.endswith("/"):
        s = s[:-1]
    return s


def is_valid_endpoint(endpoint: str) -> bool:
    """Return True if endpoint matches sdk.<cluster>.braze.com."""
    return bool(ENDPOINT_PATTERN.match(normalize_endpoint(endpoint)))


def detect_project_type() -> str:
    """
    Detect project type from current directory.
    Returns: "android" | "web" | "unknown"
    """
    cwd = Path.cwd()
    if (cwd / "build.gradle").exists() or (cwd / "build.gradle.kts").exists():
        return "android"
    if (cwd / "app" / "build.gradle").exists() or (cwd / "app" / "build.gradle.kts").exists():
        return "android"
    if (cwd / "package.json").exists():
        return "web"
    return "unknown"


def generate_android_braze_xml(api_key: str, endpoint: str) -> str:
    """Generate Android res/values/braze.xml content."""
    return f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">{api_key}</string>
  <string translatable="false" name="com_braze_custom_endpoint">{endpoint}</string>
</resources>
'''


def generate_web_braze_config_ts(api_key: str, endpoint: str) -> str:
    """Generate Web BrazeConfig.ts (TypeScript) content."""
    return f'''// Braze SDK configuration — replace with your API key and endpoint from
// Braze dashboard: Settings > App Settings (or Manage Settings)
// Endpoint list: https://www.braze.com/docs/user_guide/administrative/access_braze/sdk_endpoints/

export const BRAZE_API_KEY = "{api_key}";
export const BRAZE_SDK_ENDPOINT = "{endpoint}";

// Example usage with @braze/web-sdk:
// import * as braze from "@braze/web-sdk";
// braze.initialize(BRAZE_API_KEY, {{ baseUrl: BRAZE_SDK_ENDPOINT }});
'''


def main() -> int:
    print("Braze SDK setup validator\n")

    api_key = (input("Braze API Key: ").strip() or "YOUR_APP_IDENTIFIER_API_KEY")
    endpoint_raw = input("Braze SDK Endpoint (e.g. sdk.iad-01.braze.com): ").strip()

    if not endpoint_raw:
        endpoint = "YOUR_SDK_ENDPOINT"
        print("No endpoint entered; boilerplate will use placeholder.")
    else:
        endpoint = normalize_endpoint(endpoint_raw)
        if not is_valid_endpoint(endpoint):
            print(
                "Warning: Endpoint should be in the form sdk.<cluster>.braze.com (e.g. sdk.iad-01.braze.com).",
                file=sys.stderr
            )
            print("Continuing with your value; fix in the dashboard if needed.", file=sys.stderr)
        else:
            print("Endpoint format OK.")

    project_type = detect_project_type()
    print(f"Detected project type: {project_type}")

    if project_type == "android":
        content = generate_android_braze_xml(api_key, endpoint)
        out_path = Path("res/values/braze.xml")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
        print(f"Wrote {out_path}")
    elif project_type == "web":
        content = generate_web_braze_config_ts(api_key, endpoint)
        out_path = Path("BrazeConfig.ts")
        out_path.write_text(content, encoding="utf-8")
        print(f"Wrote {out_path}")
    else:
        content_android = generate_android_braze_xml(api_key, endpoint)
        content_web = generate_web_braze_config_ts(api_key, endpoint)
        print("Unknown project type. Boilerplate for both platforms:\n")
        print("--- Android res/values/braze.xml ---")
        print(content_android)
        print("--- Web BrazeConfig.ts ---")
        print(content_web)
        print("Save the desired snippet to the appropriate file in your project.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
