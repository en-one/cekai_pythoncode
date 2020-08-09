import pytest
import requests
from hamcrest import *


class TestWeWorkAddressBook:
    s = requests.Session()

    def setup(self):
        payload = {
            "corpid": "wwfce4a34037acc316",
            "corpsecret": "-vraLoPqaeQa5MnrPgiQO_9m3HLE_jmPlCUc7q9W2-I"
        }
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=payload)

        # 将token放入会话中，同一个s请求都会带上这个参数
        self.s.params.update({"access_token": r.json()['access_token']})
        self.s.params.update({"userid": "1001"})

    def test_addMember(self):
        data = {
            "userid": "1001",
            "name": "josiah",
            "mobile": "17326087666",
            "department": [1]
        }

        res = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/create", json=data)
        assert (self.test_getMember()['name'] == "josiah")

    def test_getMember(self):
        res = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get")
        print(res.json())
        return res.json()

    def test_editMember(self):
        data = {
            "userid": "1001",
            "mobile": "17326087777"
        }
        res = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/update", json=data)
        assert (self.test_getMember()['mobile'] == '17326087777')

    def test_deleteMember(self):
        data = {
            "userid": "1001",
        }
        res = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/delete", json=data)
        print(res.json())
        return res
