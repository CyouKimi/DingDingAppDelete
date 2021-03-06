import requests
import json


def printLine():
    print('=' * 80)


def getPublicIP():
    print('请将显示的公网IP地址，填至需要删除应用的服务器出口ip中')
    print('请稍后，正在请求服务器...')
    url = 'http://www.trackip.net/ip'
    try:
        r = requests.get(url, timeout=30)
        print(r.text)
    except:
        print('未能获取到公网IP地址')


def printMenu():
    print('钉钉E应用，微应用删除程序，请请按照提示输入应用参数（仅测试企业内部应用删除功能）')
    print('本程序用到的文档在链接: https://pan.baidu.com/s/1lX4En7I4BlZxwhAARxFtHQ 提取码: vcyn 查看')
    print('所需要的参数请登录钉钉后台：https://open-dev.dingtalk.com/#/appList 中找到需要删除的App信息')
    printLine()
    getPublicIP()
    printLine()

    agentId = input('1>输入AgentId-->')
    key = input('2>输入appkey-->')
    secret = input('3>输入appsecret-->')
    printLine()
    return agentId, key, secret


def getAccessToken(key, secret):
    url = 'https://oapi.dingtalk.com/gettoken?appkey=%s&appsecret=%s' % (key, secret)
    print('获取access_token的API地址是：', url)
    try:
        r = requests.get(url, timeout=30)
        print('获取access_token返回JSON：' + r.text)
        # 取得返回json中的access_token
        access_token = json.loads(str(r.text)).get('access_token')
        return access_token
    except:
        # TODO 不需要重新启动也可以修改所需值
        print('无法请求到数据，请重新运行本程序。当前执行模块：getAccessToken')


def deleteApp(access_token, agentId):
    # TODO 是否有必要加上验证，防止误删
    url = 'https://oapi.dingtalk.com/microapp/delete?access_token=%s' % access_token
    data = {
        'agentId': agentId
    }
    headers = {'Content-Type': 'application/json'}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(data), timeout=30)
        print('删除应用返回JSON：' + r.text)
        print('如果返回信息为ok，即为删除成功。其他文档请参考返回码的文本描述内容')
    except:
        print('无法请求到数据，请重新运行本程序。当前执行模块：DeleteApp')


if __name__ == '__main__':
    agentId, key, secret = printMenu()
    access_token = getAccessToken(key, secret)
    deleteApp(access_token, agentId)
    printLine()
    input('按任意键结束程序')
