# Gunicorn ayarları. Render portu PORT ile veriyor.
# Metrikler işlem içinde tutulduğu için tek worker ve birkaç thread kullanıyorum.

import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
workers = 1
threads = int(os.environ.get("GUNICORN_THREADS", "4"))
timeout = 30
graceful_timeout = 20
accesslog = None  # istek loglarını uygulama JSON olarak yazıyor
errorlog = "-"
loglevel = os.environ.get("LOG_LEVEL", "info").lower()
