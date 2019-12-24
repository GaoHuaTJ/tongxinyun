import requests
#讲座地址
url="http://yjsqd.tongji.edu.cn/FastAPI/syncShowActivityByTxy.php"
#发请求，获得讲座信息
response=requests.get(url).json()
print(response['sdata'])
#下一步要做的事情就是把得到的数据格式化
##并且分析清楚json哪个字段和剩余位置有关
