import requests
import app
class EmpApi:
    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        # 注意：如果我们调用员工管理模块的相关接口时，先调用login.py接口
        # 获取到的app.HEADERS 才会是{"Content-Type":"application","Authorization":"Bearer xxxx-xxx-xxxxx"}
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-12-02",
            "formOfEmployment": 1,
            "workNumber": "1234",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2019-12-15T16:00:00.000Z"
        }
        # 发送添加员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回添加员工接口的响应数据
        return response


    def query_emp(self):
        url = self.emp_url + app.EMP_ID
        return requests.get(url)
