import pytest

from Interface_test_two.api.tag import Tag
from Interface_test_two.api.wework import WeWork

class TestTag:

    @pytest.fixture(scope="session")
    def token(self):
        wework = WeWork()
        yield wework.test_get_token()

    def setup(self):
        self.tag =Tag()

    def test_multi_data(self):
        data = [("dili" + str(x), x +2, "dada" + str(x)) for x in range(2)]
        return data

    @pytest.mark.parametrize("tagname,tagid,update_tagname", test_multi_data("xx"))
    def test_all(self, tagname,tagid,update_tagname, token):
        try:
            assert self.tag.test_add_tag(tagname,tagid,token)['errmsg'] == 'created'
        except AssertionError as e:
            if 'invalid tagid' in e.__str__():
                self.tag.test_del_tag(tagid, token)
            if 'UserTag Name Already Exist' in e.__str__():
                tagList = self.tag.test_get_tag(token)
                for i in tagList:
                    for value in i.value():
                        if value == tagname:
                            del_tagId = i['tagid']
                self.tag.test_del_tag(del_tagId)
            assert self.tag.test_add_tag(tagname,tagid,token)['errmsg'] == 'created'


    # 查询
        assert self.tag.test_get_tag(tagid, token)['tagname'] == tagname

        # 更新成员
        assert self.tag.test_update_tag(tagid, update_tagname, token)['errmsg'] == "updated"
        assert self.tag.test_get_tag(tagid, token)['tagname'] == update_tagname

        # 删除成员
        assert self.tag.test_del_tag(tagid, token)['errmsg'] == 'deleted'
        assert self.tag.test_get_tag(tagid, token)['errcode'] == 40068

