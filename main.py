#coding = utf-8
#@describe: forbidden everyone to use this for money.
#@just for learning and forbidden spare it by yourself!!!
#@tools:charies
import traceback

import requests
import random
import time
import json
import Common
import MsgPush
import datetime

TIME_STR1 = "T16:30:00.000Z"
TIME_STR2 = "T20:30:00.000Z"

class BookSeat:

    def __init__(self) -> None:
        self.url_msg = 'https://tsg77.sdust.edu.cn/Order/OrderSeatLog'
        self.url_order = 'https://tsg77.sdust.edu.cn/Order/OrderSeat'
        self.token = ""
        self.headers = {
            "Host" : "tsg77.sdust.edu.cn",
            "Content-Type" : "application/json",
            "Accept" : "*/*",
            "OperateTime" : str(int(time.time())),
            "Referer" : "https://servicewechat.com/wxd5685b630fcaf8d4/11/page-frame.html",
            "Token"  : "",
            "UserId" : Common.loadId(),
            "Connection" : "keep-alive",
            "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac"
        }
        self.data_history = {
            "UserId" : Common.loadId(),
            "pageIndex": 1,
            "pageSize": 10
            }
        self.data_bookseat = {
            "UserId" : Common.loadId(),
            "dtStart" : "",
            "dtEnd"   : "",
            "roomCode" : "103",
            "seatCode" : "",
            "remark"   : ""
        }
        self.__getToken()
        #self.__BookHistory()
        self.__BookSeat()

    def __getToken(self):
        print("获取Token成功")
        pass


    def __BookSeat(self):
        """
        预定座位
        :return: None
        """
        now = datetime.datetime.now()
        TIME = now.date()
        self.data_bookseat['dtStart'] = str(TIME)+TIME_STR1
        self.data_bookseat['dtEnd']   = str(TIME)+TIME_STR2

        for i in range(26):
            if(i<10):
                self.data_bookseat['seatCode'] = "103" + "00" +str(i)+ "B"
            else:
                self.data_bookseat['seatCode'] = "103" + "0" +str(i) + "C"
            req = requests.post(url=self.url_order,data=json.dumps(self.data_bookseat),headers=self.headers)
            try:
                req = json.loads(req.text)
                if(req['message'] == '成功'):
                    print("预定成功！，您的座位是:{},预约时间是{} ----- {}".format(self.data_bookseat['seatCode'],self.data_bookseat['dtStart'],self.data_bookseat['dtEnd']))
                    break

            except:
                print("请求错误！")




    def __BookHistory(self):
        req = requests.post(url=self.url_msg, headers=self.headers, data=json.dumps(self.data_history))
        try:
            req = json.loads(req.text)
            print(req['value'])
        except:
            print("请求失败！")

    def __del__(self):
        print("自动预订系统使用完毕！")



if __name__ == '__main__':

    app = BookSeat()
