from Interface_test_two.api.base_api import BaseApi


class WeWork(BaseApi):
    def test_get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwfce4a34037acc316",
                "corpsecret": "-vraLoPqaeQa5MnrPgiQO_9m3HLE_jmPlCUc7q9W2-I"
            }
        }
        res = self.send_api(data)
        try:
            return res['access_token']
        except Exception as e:
            raise ValueError("request token errior")
