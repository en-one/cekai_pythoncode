from Interface_test_two.api.base_api import BaseApi


class Tag(BaseApi):
    def test_add_tag(self, tagname, tagid, token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",
            "json": {
                "tagname": tagname,
                "tagid": tagid
            }
        }
        r = self.send_api(data)
        print(r)
        return r

    def test_update_tag(self, tagid, tagname, token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",
            "json": {
                "tagid": tagid,
                "tagname": tagname
            }
        }
        r = self.send_api(data)
        return r

    def test_del_tag(self, tagid, token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}",
            "params": {
                "tagid": tagid
            }
        }
        r = self.send_api(data)
        return r

    def test_get_tag(self, tagid, token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={token}",
            "params": {
                "tagid": tagid
            }
        }
        r = self.send_api(data)
        return r

    def test_get_taglist(self, token):
        data = {"method": "get",
                "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"}
        r = self.send_api(data)
        return r['taglist']
