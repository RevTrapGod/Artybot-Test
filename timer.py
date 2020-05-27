import asyncio


class Timer:
  def __init__(self, timeout_time, callback):
    self._task = asyncio.ensure_future(self._job())
    self._timeout =  timeout_time
    self._callback = callback
  
  async def _job(self):
    await asyncio.sleep(self._timeout)
    await self._callback()

