import pathlib

APP_DIR = pathlib.Path().resolve() / 'app'
TEMPLATE_DIR = APP_DIR / "templates"
STATIC_DIR = APP_DIR / "static"
STATIC_URL = "/static"
DB_URL = f'sqlite+aiosqlite:///{APP_DIR}/app.db'
TEST_DB_URL = f'sqlite+aiosqlite:///{APP_DIR}/test_app.db'
