"""Constants for the Desi."""

from homeassistant.const import Platform

MANUFACTURER = "Desi Smart Lock and Security Systems"
DEFAULT_NAME = "Desi Smart"
DOMAIN = "desi"

LOGIN_METHODS = ["phone", "email"]
DEFAULT_LOGIN_METHOD = "email"

WEB_URL = "https://__DESI_WEB_DOMAIN__"
API_URL = "https://__DESI_API_DOMAIN__"

AUTH_URI = f"{WEB_URL}/ds/sign-in-for-home-assistant"
TOKEN_URI = f"{API_URL}/api/third_part_devices/ds/home_assistant/token"
FULLFILMENT_API_URI = f"{API_URL}/api/third_part_devices/ds/home_assistant/control"
SOCKET_PATH = "/api/third_part_devices/ds/home_assistant/ws"
WS_URL = f"{API_URL}{SOCKET_PATH}"

PLATFORMS = [
    Platform.LOCK,
    Platform.ALARM_CONTROL_PANEL,
    Platform.SWITCH,
    Platform.SENSOR,
]
