import pytest
import requests
from hamcrest import *


class TestWeWorkTag:
    s = requests.Session()

    def setup(self):
        payload = {
            "corpid": "wwfce4a34037acc316",
            "corpsecret": "-vraLoPqaeQa5MnrPgiQO_9m3HLE_jmPlCUc7q9W2-I"
        }
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=payload)

        # 将token放入会话中，同一个s请求都会带上这个参数
        self.s.params.update({"access_token": r.json()['access_token']})
        # self.s.params.update({"tagid": "2"})

    def test_addTAg(self):
        data = {
            "tagname": "UI1",
        }

        res = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/tag/create", json=data)
        print(self.test_getTagList(), res.json()['tagid'])
        # assert (self.test_getTagList()[res.json()['tagid']] == "UI")

    def test_getTagList(self):
        res = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/tag/list")
        print(res.json()['taglist'])
        return res.json()

    def test_editTag(self):
        data = {
            "tagid": "2",
            "tagname": "UI design"
        }
        res = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/tag/update", json=data)
        # assert (self.test_getTagList()[res.json()['tagname']] == "UI design")

    def test_deleteTag(self):
        data = {
             "tagid": "2",
        }
        res = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/tag/delete", params=data)
        print(res.json())
        return res
