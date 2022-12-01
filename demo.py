import requests#需要安装requests模块，详情百度pip安装
import json

url='https://dt.vibrate.bayuenet.com/api/inspection.depart/getThreshold'
yang=requests.get(url)#这里返回的json数据
result=open('a.json','w')

result.write(yang.text)#yang.text将yang这个json数据以字符形式使用
result.close()#这里一定要关闭文件，不然写不进去
open_json=open('a.json','r',encoding='cp936')
err_obj=json.load(open_json)#json.load()将json转为python字典
open_json.close()#到这里zd_json是一个python字典
# print(err_obj["data"]['highTEMP'])


# 字符串value
value ='{"temperature": -81.371429, "accPeakValue": 0.021874241567652126, "accEffectiveValue": 0.02, "velEeffectiveValue": 0.0, "displacementEeffectiveValue": 0.01, "fs": 12800, "n": 200, "envelopeEffectiveValue": 0.02, "envelopePeakValue": 0.06, "DevId": "326204143#1"}'

# 字典value_obj
value_obj=eval(value)
# print(value_obj,type(value_obj))
# print(value_obj["temperature"])
value_tep=float(value_obj["temperature"])
value_spe=float(value_obj["accPeakValue"])
err_highTEMP=float(err_obj["data"]["highTEMP"])
err_superHighTEMP=float(err_obj["data"]["superHighTEMP"])
err_highspe=float(err_obj["data"]["highSPEED"])
err_superHighSPE=float(err_obj["data"]["superHighSPEED"])


error=''
if (value_tep >= err_highTEMP and value_tep <= err_superHighTEMP) :
        error+='error:"highTEMP",value:'
        error+=str(value_tep)
else : 
    if (value_tep >= err_superHighTEMP):
        error+='error:"superHighTEMP",value:'
        error+=str(value_tep)


if (value_spe >= err_highspe and value_spe <= err_superHighSPE) :
        error+='\nerror:"highSPEED",value:'
        error+=str(value_spe)

else : 
    if (value_spe >= err_superHighSPE):
        error+='\nerror:"superHighSPEED",value:'
        error+=str(value_spe)

print(error)

