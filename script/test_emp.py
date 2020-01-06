import logging
import unittest
from api.emp_api import EmpApi
from utils import assert_common
import app
class TestIHRMEmp(unittest.TestCase):
    def setUp(self) -> None:
        pass
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化员工类
        cls.emp_api = EmpApi()
    def tearDown(self) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_add_emp(self):
        # 调用添加员工接口
        response = self.emp_api.add_emp("五竹xxx1v5", "299999111223")
        # 获取添加员工接口的json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("添加员工接口返回数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")

        # 获取员工ID保存在全局变量
        app.EMP_ID = jsonData.get("data").get("id")
