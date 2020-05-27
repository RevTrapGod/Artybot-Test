import asyncio


class Periodic:
  def __init__(self, time, callback):
    self._task = asyncio.ensure_future(self._job())
    self._timeout =  time
    self._callback = callback
  
  async def _job(self):
    while True:
      await asyncio.sleep(self._timeout)
      await self._callback()

