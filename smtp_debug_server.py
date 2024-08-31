import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Debugging


async def run():
    handler = Debugging()
    controller = Controller(handler, hostname="localhost", port=8025)
    controller.start()
    print("SMTP Debugging Server running on localhost:8025...")
    try:
        await asyncio.Event().wait()  # Keep the server running indefinitely
    finally:
        controller.stop()


asyncio.run(run())
