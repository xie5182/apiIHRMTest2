import app
import json


# 编写断言代码函数
def assert_common(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言message


def read_login_data():
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, mode='r',encoding='utf-8') as f:
        # 加载文件为json格式的数据
        jsonData = json.load(f)
        # 遍历文件取出其中数据并保存在列表中
        p_list = []
        for data in jsonData:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            p_list.append( (mobile,password,http_code,success,code,message) )
    print(p_list)
    return p_list


if __name__ == '__main__':
    # main函数的作用？
    # 防止调用这个模块或者类时，自动执行代码
    read_login_data()
    
