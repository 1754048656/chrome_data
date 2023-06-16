import asyncio
import websockets
import threading
from sVo import SvoData

from a_dump_detail import DumpTitle

class MyWebSocket:

    def __init__(self):
        pass

    def startTask(self):
        print('___start webSocket___')

        # 启动主要的执行类
        self.thread = threading.Thread(target=self.startDumpTask)
        self.label = False

        # 把ip换成自己本地的ip
        start_server = websockets.serve(self.main_logic, 'localhost', 8010)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def startDumpTask(self):
        DumpTitle()

    # 服务器端主逻辑
    # websocket和path是该函数被回调时自动传过来的，不需要自己传
    async def main_logic(self, websocket, path):
        self._websocket = websocket
        await self.recv_msg(websocket)

    # 接收客户端消息并处理，这里只是简单把客户端发来的返回回去
    async def recv_msg(self, websocket):
        while True:
            recv_text = await websocket.recv()
            # print(recv_text)
            if 'sVoELocvxVW0T=' in recv_text:
                SvoData.sVoELocvxVW0T = recv_text.split('sVoELocvxVW0T=')[1]

                # 开始任务
                if not self.label:
                    self.label = True
                    self.thread.start()

            # response_text = f"your submit context: {recv_text}"
            # await websocket.send(recv_text)

MyWebSocket().startTask()