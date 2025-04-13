from fastapi import FastAPI
from app.routers import manual_trade, automated_trade, tracker, notifications, mt5_login

app = FastAPI(title="Woll X Backend")

app.include_router(manual_trade.router, prefix="/manual")
app.include_router(automated_trade.router, prefix="/auto")
app.include_router(tracker.router, prefix="/tracker")
app.include_router(notifications.router, prefix="/notify")
app.include_router(mt5_login.router, prefix="/mt5")
