import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / '.env')

def flag(name: str, default: str = 'false') -> bool:
    return os.getenv(name, default).lower() in {'1','true','yes','on'}

APP_NAME = os.getenv('APP_NAME', 'Aqua Monitor')
DATABASE_URL = os.getenv('DATABASE_URL', f"sqlite:///{ROOT / 'monitor.db'}")
SESSION_SECRET = os.getenv('SESSION_SECRET', 'dev-only-change-me')
SESSION_MAX_AGE = int(os.getenv('SESSION_MAX_AGE', '604800'))
SESSION_HTTPS_ONLY = flag('SESSION_HTTPS_ONLY')
DEVICE_OFFLINE_SECONDS = int(os.getenv('DEVICE_OFFLINE_SECONDS', '30'))

MQTT_HOST = os.getenv('MQTT_HOST', '127.0.0.1')
MQTT_PORT = int(os.getenv('MQTT_PORT', '1883'))
MQTT_CLIENT_ID = os.getenv('MQTT_CLIENT_ID', 'aqua-monitor-backend')
MQTT_TELEMETRY_TOPIC = os.getenv('MQTT_TELEMETRY_TOPIC', 'aqua-monitor/devices/+/telemetry')
MQTT_STATUS_TOPIC = os.getenv('MQTT_STATUS_TOPIC', 'aqua-monitor/devices/+/status')
MQTT_QOS = int(os.getenv('MQTT_QOS', '1'))
MQTT_KEEPALIVE = int(os.getenv('MQTT_KEEPALIVE', '60'))
MQTT_USERNAME = os.getenv('MQTT_USERNAME') or None
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD') or None
MQTT_TLS = flag('MQTT_TLS')