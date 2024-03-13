#coding:utf-8
__author__ = "ila"
import base64, copy, logging, os, sys, time, xlrd, json, datetime, configparser
from django.http import JsonResponse
from django.apps import apps
from django.db.models.aggregates import Count,Sum
from .models import dianyingxinxi
from util.codes import *
from util.auth import Auth
from util.common import Common
import util.message as mes
from django.db import connection
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Q
from util.baidubce_api import BaiDuBce
from .config_model import config
from datetime import datetime

from alipay import AliPayConfig, AliPay


def dianyingxinxi_register(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")
        req_dict['addtime'] = datetime.now()


        error = dianyingxinxi.createbyreq(dianyingxinxi, dianyingxinxi, req_dict)
        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = "用户已存在,请勿重复注册!"
        return JsonResponse(msg)


def dianyingxinxi_login(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")

        datas = dianyingxinxi.getbyparams(dianyingxinxi, dianyingxinxi, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = mes.password_error_code
            return JsonResponse(msg)
        try:
            __sfsh__= dianyingxinxi.__sfsh__
        except:
            __sfsh__=None

        if  __sfsh__=='是':
            if datas[0].get('sfsh')!='是':
                msg['code']=other_code
                msg['msg'] = "账号已锁定，请联系管理员审核!"
                return JsonResponse(msg)
                
        req_dict['id'] = datas[0].get('id')
        return Auth.authenticate(Auth, dianyingxinxi, req_dict)


def dianyingxinxi_logout(request):
    if request.method in ["POST", "GET"]:
        msg = {
            "msg": "登出成功",
            "code": 0
        }

        return JsonResponse(msg)


def dianyingxinxi_resetPass(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}

        req_dict = request.session.get("req_dict")

        columns=  dianyingxinxi.getallcolumn( dianyingxinxi, dianyingxinxi)

        try:
            __loginUserColumn__= dianyingxinxi.__loginUserColumn__
        except:
            __loginUserColumn__=None
        username=req_dict.get(list(req_dict.keys())[0])
        if __loginUserColumn__:
            username_str=__loginUserColumn__
        else:
            username_str=username
        if 'mima' in columns:
            password_str='mima'
        else:
            password_str='password'

        init_pwd = '123456'
        recordsParam = {}
        recordsParam[username_str] = req_dict.get("username")
        records=dianyingxinxi.getbyparams(dianyingxinxi, dianyingxinxi, recordsParam)
        if len(records)<1:
            msg['code'] = 400
            msg['msg'] = '用户不存在'
            return JsonResponse(msg)

        eval('''dianyingxinxi.objects.filter({}='{}').update({}='{}')'''.format(username_str,username,password_str,init_pwd))
        
        return JsonResponse(msg)


def dianyingxinxi_session(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}

        req_dict={"id":request.session.get('params').get("id")}
        msg['data']  = dianyingxinxi.getbyparams(dianyingxinxi, dianyingxinxi, req_dict)[0]

        return JsonResponse(msg)


def dianyingxinxi_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"是"})
        data=dianyingxinxi.getbyparams(dianyingxinxi, dianyingxinxi, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg)


def dianyingxinxi_page(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        #获取全部列名
        columns=  dianyingxinxi.getallcolumn( dianyingxinxi, dianyingxinxi)

        #当前登录用户所在表
        tablename = request.session.get("tablename")


            #authColumn=list(__authTables__.keys())[0]
            #authTable=__authTables__.get(authColumn)

            # if authTable==tablename:
                #params = request.session.get("params")
                #req_dict[authColumn]=params.get(authColumn)

        '''__authSeparate__此属性为真，params添加userid，后台只查询个人数据'''
        try:
            __authSeparate__=dianyingxinxi.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        #当项目属性hasMessage为”是”，生成系统自动生成留言板的表messages，同时该表的表属性hasMessage也被设置为”是”,字段包括userid（用户id），username(用户名)，content（留言内容），reply（回复）
        #接口page需要区分权限，普通用户查看自己的留言和回复记录，管理员查看所有的留言和回复记录
        try:
            __hasMessage__=dianyingxinxi.__hasMessage__
        except:
            __hasMessage__=None
        if  __hasMessage__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict["userid"]=request.session.get("params").get("id")



        # 判断当前表的表属性isAdmin,为真则是管理员表
        # 当表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
        __isAdmin__ = None

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        # 当前表也是有管理员权限的表
        if  __isAdmin__ == "是" and 'dianyingxinxi' != 'forum':
            if req_dict.get("userid") and 'dianyingxinxi' != 'chat':
                del req_dict["userid"]

        else:
            #非管理员权限的表,判断当前表字段名是否有userid
            if tablename!="users" and 'dianyingxinxi'[:7]!='discuss'and "userid" in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi):
                req_dict["userid"] = request.session.get("params").get("id")

        #当列属性authTable有值(某个用户表)[该列的列名必须和该用户表的登陆字段名一致]，则对应的表有个隐藏属性authTable为”是”，那么该用户查看该表信息时，只能查看自己的
        try:
            __authTables__=dianyingxinxi.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={}:
            try:
                del req_dict['userid']
                # tablename=request.session.get("tablename")
                # if tablename=="users":
                    # del req_dict['userid']
            except:
                pass
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break
        q = Q()
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =dianyingxinxi.page(dianyingxinxi, dianyingxinxi, req_dict, request, q)

        return JsonResponse(msg)


def dianyingxinxi_autoSort(request):
    '''
    ．智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
主要信息列表（如商品列表，新闻列表）中使用，显示最近点击的或最新添加的5条记录就行
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi):
            req_dict['sort']='clicknum'
        elif "browseduration"  in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi):
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = dianyingxinxi.page(dianyingxinxi,dianyingxinxi, req_dict)

        return JsonResponse(msg)


def dianyingxinxi_list(request):
    '''
    前台分页
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if req_dict.__contains__('vipread'):
            del req_dict['vipread']

        #获取全部列名
        columns=  dianyingxinxi.getallcolumn( dianyingxinxi, dianyingxinxi)
        #表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
        try:
            __foreEndList__=dianyingxinxi.__foreEndList__
        except:
            __foreEndList__=None

        if __foreEndList__=="前要登":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass
        #forrEndListAuth
        try:
            __foreEndListAuth__=dianyingxinxi.__foreEndListAuth__
        except:
            __foreEndListAuth__=None


        #authSeparate
        try:
            __authSeparate__=dianyingxinxi.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="是" and __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params",{"id":0}).get("id")

        tablename = request.session.get("tablename")
        if tablename == "users" and req_dict.get("userid") != None:#判断是否存在userid列名
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "是":
                if req_dict.get("userid"):
                    # del req_dict["userid"]
                    pass
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if "userid" in columns:
                    try:
                        # 本接口可以匿名访问,所以try判断是否为匿名
                        # req_dict['userid']=request.session.get("params").get("id")
                        pass
                    except:
                            pass
        #当列属性authTable有值(某个用户表)[该列的列名必须和该用户表的登陆字段名一致]，则对应的表有个隐藏属性authTable为”是”，那么该用户查看该表信息时，只能查看自己的
        try:
            __authTables__=dianyingxinxi.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="是":
            try:
                del req_dict['userid']
            except:
                pass
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break
        
        if dianyingxinxi.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass
        q = Q()
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = dianyingxinxi.page(dianyingxinxi, dianyingxinxi, req_dict, request, q)

        return JsonResponse(msg)


def dianyingxinxi_save(request):
    '''
    后台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys():
            del req_dict['clicktime']
        tablename=request.session.get("tablename")
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        #获取全部列名
        columns=  dianyingxinxi.getallcolumn( dianyingxinxi, dianyingxinxi)
        if tablename!='users' and req_dict.get("userid")!=None and 'userid' in columns  and __isAdmin__!='是':
            params=request.session.get("params")
            req_dict['userid']=params.get('id')
        req_dict['addtime'] = datetime.now()
        error= dianyingxinxi.createbyreq(dianyingxinxi,dianyingxinxi, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def dianyingxinxi_add(request):
    '''
    前台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        #获取全部列名
        columns=  dianyingxinxi.getallcolumn( dianyingxinxi, dianyingxinxi)
        try:
            __authSeparate__=dianyingxinxi.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=dianyingxinxi.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params").get("id")
        req_dict['addtime'] = datetime.now()
        error= dianyingxinxi.createbyreq(dianyingxinxi,dianyingxinxi, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def dianyingxinxi_thumbsup(request,id_):
    '''
     点赞：表属性thumbsUp[是/否]，刷表新增thumbsupnum赞和crazilynum踩字段，
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=dianyingxinxi.getbyid(dianyingxinxi,dianyingxinxi,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = dianyingxinxi.updatebyparams(dianyingxinxi,dianyingxinxi, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def dianyingxinxi_info(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = dianyingxinxi.getbyid(dianyingxinxi,dianyingxinxi, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
        #浏览点击次数
        try:
            __browseClick__= dianyingxinxi.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"  and  "clicknum"  in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum}
            ret=dianyingxinxi.updatebyparams(dianyingxinxi,dianyingxinxi,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg)


def dianyingxinxi_detail(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =dianyingxinxi.getbyid(dianyingxinxi,dianyingxinxi, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= dianyingxinxi.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"   and  "clicknum"  in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum}

            ret=dianyingxinxi.updatebyparams(dianyingxinxi,dianyingxinxi,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = retfo
        return JsonResponse(msg)


def dianyingxinxi_update(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if req_dict.get("mima") and "mima" not in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi) :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi) :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = dianyingxinxi.updatebyparams(dianyingxinxi, dianyingxinxi, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def dianyingxinxi_delete(request):
    '''
    批量删除
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=dianyingxinxi.deletes(dianyingxinxi,
            dianyingxinxi,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def dianyingxinxi_vote(request,id_):
    '''
    浏览点击次数（表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1）
统计商品或新闻的点击次数；提供新闻的投票功能
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= dianyingxinxi.getbyid(dianyingxinxi, dianyingxinxi, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=dianyingxinxi.updatebyparams(dianyingxinxi,dianyingxinxi,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)


def dianyingxinxi_importExcel(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        excel_file = request.FILES.get("file", "")
        file_type = excel_file.name.split('.')[1]
        
        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = data.sheets()[0]
            rows = table.nrows
            
            try:
                for row in range(1, rows):
                    row_values = table.row_values(row)
                    req_dict = {}
                    dianyingxinxi.createbyreq(dianyingxinxi, dianyingxinxi, req_dict)
                    
            except:
                pass
                
        else:
            msg = {
                "msg": "文件类型错误",
                "code": 500
            }
                
        return JsonResponse(msg)


def dianyingxinxi_sendemail(request):
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")

        code = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4)
        to = []
        to.append(req_dict['email'])

        send_mail('用户注册', '您的注册验证码是【'+''.join(code)+'】，请不要把验证码泄漏给其他人，如非本人请勿操作。', 'yclw9@qq.com', to, fail_silently = False)

        cursor = connection.cursor()
        cursor.execute("insert into emailregistercode(email,role,code) values('"+req_dict['email']+"','用户','"+''.join(code)+"')")

        msg = {
            "msg": "发送成功",
            "code": 0
        }

        return JsonResponse(msg)


# 推荐算法接口
def dianyingxinxi_autoSort2(request):
    
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")
        cursor = connection.cursor()
        leixing = set()
        try:
            cursor.execute("select inteltype from storeup where userid = %d"%(request.session.get("params").get("id"))+" and tablename = 'dianyingxinxi' order by addtime desc")
            rows = cursor.fetchall()
            for row in rows:
                for item in row:
                    if item != None:
                        leixing.add(item)
        except:
            leixing = set()
        
        L = []
        cursor.execute("select * from dianyingxinxi where dianyingfenlei in ('%s"%("','").join(leixing)+"') union all select * from dianyingxinxi where dianyingfenlei not in('%s"%("','").join(leixing)+"')")
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)


        return JsonResponse({"code": 0, "msg": '',  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":5,"list": L[0:int(req_dict["limit"])]}})


# （按值统计）时间统计类型
def dianyingxinxi_value(request, xColumnName, yColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        
        where = ' where 1 = 1 '
        sql = ''
        if timeStatType == '日':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM dianyingxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d') LIMIT 10".format(xColumnName, yColumnName, where, '%Y-%m-%d')

        if timeStatType == '月':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM dianyingxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m') LIMIT 10".format(xColumnName, yColumnName, where, '%Y-%m')

        if timeStatType == '年':
            sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM dianyingxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y') LIMIT 10".format(xColumnName, yColumnName, where, '%Y')

        L = []
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)
        msg['data'] = L
        return JsonResponse(msg)


# 按值统计
def dianyingxinxi_o_value(request, xColumnName, yColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        
        where = ' where 1 = 1 '

        sql = "SELECT {0}, sum({1}) AS total FROM dianyingxinxi {2} GROUP BY {0} LIMIT 10".format(xColumnName, yColumnName, where)
        L = []
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)
        msg['data'] = L
        return JsonResponse(msg)

# （按值统计）时间统计类型(多)
def dianyingxinxi_valueMul(request, xColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": []}

        req_dict = request.session.get("req_dict")

        where = ' where 1 = 1 '

        for item in req_dict['yColumnNameMul'].split(','):
            sql = ''
            if timeStatType == '日':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM dianyingxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d') LIMIT 10".format(xColumnName, item, where, '%Y-%m-%d')

            if timeStatType == '月':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM dianyingxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m') LIMIT 10".format(xColumnName, item, where, '%Y-%m')

            if timeStatType == '年':
                sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM dianyingxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y') LIMIT 10".format(xColumnName, item, where, '%Y')

            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime(
                            "%Y-%m-%d %H:%M:%S")
                    else:
                        pass
                L.append(online_dict)
            msg['data'].append(L)
        return JsonResponse(msg)

# （按值统计(多)）
def dianyingxinxi_o_valueMul(request, xColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": []}

        req_dict = request.session.get("req_dict")

        where = ' where 1 = 1 '

        for item in req_dict['yColumnNameMul'].split(','):
            sql = "SELECT {0}, sum({1}) AS total FROM dianyingxinxi {2} GROUP BY {0} LIMIT 10".format(xColumnName, item, where)
            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime(
                            "%Y-%m-%d %H:%M:%S")
                    else:
                        pass
                L.append(online_dict)
            msg['data'].append(L)

        return JsonResponse(msg)


def dianyingxinxi_count(request):
    '''
    总数接口
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        req_dict = request.session.get("req_dict")
        where = ' where 1 = 1 '
        for key in req_dict:
            if req_dict[key] != None:
                where = where + " and key like '{0}'".format(req_dict[key])

        sql = "SELECT count(*) AS count FROM dianyingxinxi {0}".format(where)
        count = 0
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            count = online_dict['count']
        msg['data'] = count

        return JsonResponse(msg)


def dianyingxinxi_group(request, columnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        where = ' where 1 = 1 '

        sql = "SELECT COUNT(*) AS total, " + columnName + " FROM dianyingxinxi " + where + " GROUP BY " + columnName + " LIMIT 10"

        L = []
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime("%Y-%m-%d")
                else:
                    pass
            L.append(online_dict)
        msg['data'] = L
        return JsonResponse(msg)


def dianyingxinxi_groupby(request):
    '''
    管理员用户：当表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        #处理参数
        try:
            page1 = int(req_dict.get("page"))
        except:
            page1 = 1
        try:
            limit1 = int(req_dict.get("limit"))
        except:
            limit1 = 10

        #值为"是"仅能查看自己的记录和add接口后台赋值userid的值
        try:
            __authSeparate__ = dianyingxinxi.__authSeparate__
        except:
            __authSeparate__ = None

        # print(dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi))
        if __authSeparate__=="是":
            #print("req_dict==============>",req_dict)
            #如果当前表有userid字段,且通过身份认证
            if "userid"  in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi) and request.session.get("params")!=None:
                #参数增加userid
                req_dict["userid"]=request.session.get("params").get("id")
        #如果当前表没有userid字段,且参数里有userid键值对
        if  "userid" not  in dianyingxinxi.getallcolumn(dianyingxinxi,dianyingxinxi) and "userid" in list(req_dict.keys()):
            #删除参数userid
            del req_dict["userid"]
        try:
            del req_dict["page"]
            del req_dict["limit"]
        except:
            pass
        tablename=request.session.get("tablename")
        if tablename=="users" and req_dict.get("userid")!=None:
            del req_dict["userid"]
        else:
            #判断当前登陆表是否具有管理员权限
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            #是,则删除userid参数
            if __isAdmin__=="是":
                del req_dict["userid"]
            else:
                #否,则赋值userid参数
                req_dict["userid"]=request.session.get("params").get("id")
        print("req_dict===========>",req_dict)
        #20200928 去掉总记录数查询.因为只有一条记录,所以总记录数从查询所的记录获取
        #本次查询所有,求总记录数
        # alldata = dianyingxinxi.objects.filter(**req_dict). \
        #     annotate(userids=Count('userid'),paperids=Count('paperid'),papernames=Count('papername')). \
        #         values("userid", "paperid", "papername","myscore","userids"). \
        #         all()
        # print("alldata=============>",alldata)
        # print("alldata=============>",alldata.  aggregate(myscore=Sum('myscore')))

        #本次分页查询
        start=limit1 * (page1 - 1)
        end=limit1 * (page1 - 1)+limit1+1
        datas = dianyingxinxi.objects.filter(**req_dict).\
                    annotate(userids=Count('userid'),usernames=Count('username'),paperids=Count('paperid'),papernames=Count('papername')). \
                values("userid", "username", "paperid", "papername","myscore"). \
                    all()[start:end]
        print("datas=============>", datas)
        print("datas=============>", datas.aggregate(myscore=Sum('myscore')))

        #处理分页查询所得数据
        try:
            data = [model_to_dict(i) for i in datas]
        except:
            data = datas
        dataDict = {}
        for i in data:
            keyName1="{}#{}#{}#{}".format(i.get("userid"),i.get("username"),i.get("paperid"),i.get("papername"))
            if dataDict.get(keyName1)==None:
                dataDict[keyName1]={"userid":i.get("userid"),"username":i.get("username"),"paperid":i.get("paperid"),"papername":i.get("papername"),"myscore":i.get("myscore")}
            else:
                dataDict[keyName1]["myscore"]=dataDict.get(keyName1).get("myscore")+i.get("myscore")

        #赋值分页查询所得数据
        dataList =list(dataDict.values())

        # 处理所有查询,计算总页数
        total = len(dataList)
        try:
            div = divmod(total, limit1)
            if div[1] > 0:
                totalPage = div[0] + 1
            else:
                totalPage = div[0]
        except:
            totalPage = 1

        # 赋值分页参数
        msg["data"] = {"pageSize": limit1,
                       "total": total,
                       "totalPage": totalPage,
                       "currPage": page1,
                       "list":dataList
                       }

        return JsonResponse(msg)


def dianyingxinxi_deleterecords(request):
    '''
    按键值对参数添加删除记录
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")
        error=dianyingxinxi.deletebyparams(dianyingxinxi,dianyingxinxi,req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def dianyingxinxi_flist(request):
    '''
    查看所有开放的帖列表(无需登录)
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize'] = dianyingxinxi.page(dianyingxinxi, dianyingxinxi, req_dict)

        return JsonResponse(msg)


def dianyingxinxi_list_id(request,id_):
    '''
    查看主贴和所有回帖内容(无需登录)
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {"currPage":1,"totalPage":1,"total":1,"pageSize":10,"childs":[]},"id":int(id_)}

        params = {"id":int(id_)}

        datas = dianyingxinxi.retrieve(dianyingxinxi, dianyingxinxi)


        parent_id=0#当前id，也就是parent_id,找到了下一级，把下一级id赋值给current_id，当做下下一级id的paretn_id
        current_id=0
        start_index=0

        #获取parentid
        for index,i in enumerate(datas):
            if i.get('id')==params.get('id'):
                current_id=parent_id=i.get('id')
                start_index=index
                msg['data'].update(i)
                break

        #把疑似回帖的id放进ids数组
  
        id_data_dict={}#id和详情的键值对
        for i in datas:
            id_data_dict[i.get('id')]=i
        
        dict1={}#部分层级，只获取上下级关系
        for v in id_data_dict.values():
            parentid_=copy.deepcopy(v.get("parentid"))

            id_=copy.deepcopy(v.get("id"))
            if dict1.get(parentid_)==None:
                dict1[parentid_]=[]
            dict1[parentid_].append(id_)


        childs=[]#msg.data.childs
        #填充第一层回帖
        for i  in dict1.get(parent_id,[]):
            child1=copy.deepcopy(id_data_dict.get(i))

            #填充第二层回帖
            if dict1.get(i)!=None:#判断第二次是否还有回帖
                child2=[]
                for j in  dict1.get(i):
                    child3=copy.deepcopy(id_data_dict.get(j))
                    id_=copy.deepcopy(child3.get("id"))

                    if dict1.get(id_)!=None:#判断第三次是否还有回帖
                        child3["childs"]=[]
                        for k in dict1.get(id_):
                            child4=copy.deepcopy(id_data_dict.get(k))
                            id__=copy.deepcopy(child4.get("id"))

                            if dict1.get(id__)!=None:#判断第四次是否还有回帖
                                child4['childs']=[]
                                for l in dict1.get(id__):
                                    child5=copy.deepcopy(id_data_dict.get(l))
                                    id___=copy.deepcopy(child5.get("id"))

                                    if dict1.get(id___)!=None:#判断第五次是否还有回帖
                                        child5['childs']=[]
                                        for m in dict1.get(id___):
                                            child6=copy.deepcopy(id_data_dict.get(m))
                                            id____=copy.deepcopy(child6.get("id"))

                                            if dict1.get(id____)!=None:#判断第六次是否还有回帖
                                                child6['childs']=[]
                                                child7=copy.deepcopy(id_data_dict.get(m))
                                                child7['childs']=[]
                                                for n in dict1.get(id____):
                                                    child7['childs'].append(id_data_dict.get(n))

                                                child6['childs'].append(child7)

                                        child5['childs'].append(child6)

                                child4["childs"].append(child5)

                        child3["childs"].append(child4)

                    child2.append(child3)
                child1['childs']=child2
            else:
                child1['childs']=None

            childs.append(child1)
        print(childs)
        msg['data']['childs']=childs
        return JsonResponse(msg)


def dianyingxinxi_alipay(request):
    if request.method in ["POST", "GET"]:
        alipay = AliPay(
            appid=settings.ALIPAY_APP_ID,
            app_notify_url=None,
            app_private_key_string=settings.APP_PRIVATE_KEY_STRING,
            alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY_STRING,
            sign_type=settings.ALIPAY_SIGN_TYPE,
            debug=True,
            config=AliPayConfig(timeout=15)
        )

        req_dict = request.session.get("req_dict")

        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=req_dict['tradeno'],
            total_amount=req_dict['totalamount'],
            subject=req_dict['subject'],
            return_url='http://127.0.0.1:8080/MovieProject/dianyingxinxi/notify',
            #notify_url=''
        )
        pay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
        pay_url = '<form name="punchout_form" method="post" action="{0}"><input type="hidden" name="biz_content" ><input type="submit" value="立即支付" style="display: none"></form>'.format(pay_url)

        return JsonResponse({'code': 0, "data": pay_url})


def dianyingxinxi_notify(request):
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")
        out_trade_no = req_dict['out_trade_no']
        cursor = connection.cursor()

        return redirect('http://127.0.0.1:8080/MovieProject/admin/dist/index.html#/dianyingxinxi')