#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime


class dianyingfenlei(BaseModel):
    __doc__ = u'''dianyingfenlei'''
    __tablename__ = 'dianyingfenlei'
    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dianyingfenlei=models.CharField ( max_length=255,null=False,unique=True, verbose_name='电影分类' )
    '''
    dianyingfenlei=VARCHAR
    '''
    class Meta:
        db_table = 'dianyingfenlei'
        verbose_name = verbose_name_plural = '电影分类'

class dianyingxinxi(BaseModel):
    __doc__ = u'''dianyingxinxi'''
    __tablename__ = 'dianyingxinxi'
    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dianyingmingcheng=models.CharField ( max_length=255,null=False,unique=False, verbose_name='电影名称' )
    dianyingfenlei=models.CharField ( max_length=255,null=False,unique=False, verbose_name='电影分类' )
    dianyingchandi=models.CharField ( max_length=255,null=False,unique=False, verbose_name='电影产地' )
    dianyinghaibao=models.TextField ( null=True, unique=False, verbose_name='电影海报' )
    yanyuanzhenrong=models.CharField ( max_length=255,null=True,unique=False, verbose_name='演员阵容' )
    dianyingdaoyan=models.CharField ( max_length=255,null=True,unique=False, verbose_name='电影导演' )
    yugaoshipin=models.TextField ( null=True, unique=False, verbose_name='预告视频' )
    shangyingriqi=models.DateField ( null=True, unique=False, verbose_name='上映日期' )
    fangyingchangci=models.DateTimeField  (  null=True, unique=False, verbose_name='放映场次' )
    fangyingting=models.CharField ( max_length=255,null=True,unique=False, verbose_name='放映厅' )
    dianyingjieshao=models.TextField ( null=True, unique=False, verbose_name='电影介绍' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    price=models.FloatField ( null=False, unique=False,default='0', verbose_name='价格' )
    number=models.IntegerField ( null=True, unique=False,default='0', verbose_name='座位总数' )
    selected=models.TextField ( null=True, unique=False, verbose_name='已选座位[用,号隔开]' )
    '''
    dianyingmingcheng=VARCHAR
    dianyingfenlei=VARCHAR
    dianyingchandi=VARCHAR
    dianyinghaibao=Text
    yanyuanzhenrong=VARCHAR
    dianyingdaoyan=VARCHAR
    yugaoshipin=Text
    shangyingriqi=Date
    fangyingchangci=DateTime
    fangyingting=VARCHAR
    dianyingjieshao=Text
    clicktime=DateTime
    price=Float
    number=Integer
    selected=Text
    '''
    class Meta:
        db_table = 'dianyingxinxi'
        verbose_name = verbose_name_plural = '电影信息'

class discussdianyingxinxi(BaseModel):
    __doc__ = u'''discussdianyingxinxi'''
    __tablename__ = 'discussdianyingxinxi'
    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField ( null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255,null=True,unique=False, verbose_name='用户名' )
    content=models.TextField ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField ( null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discussdianyingxinxi'
        verbose_name = verbose_name_plural = '电影信息评论表'

class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'
    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False,unique=False, verbose_name='标题' )
    introduction=models.TextField ( null=True, unique=False, verbose_name='简介' )
    picture=models.TextField ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告信息'

class orders(BaseModel):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'
    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    orderid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='订单编号' )
    tablename=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商品表名' )
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商品名称' )
    picture=models.TextField ( null=True, unique=False, verbose_name='商品图片' )
    buynumber=models.IntegerField ( null=False, unique=False,default='0', verbose_name='购买数量' )
    price=models.FloatField ( null=False, unique=False,default='0', verbose_name='价格' )
    discountprice=models.FloatField ( null=True, unique=False,default='0', verbose_name='折扣价格' )
    total=models.FloatField ( null=False, unique=False,default='0', verbose_name='总价格' )
    discounttotal=models.FloatField ( null=True, unique=False,default='0', verbose_name='折扣总价格' )
    type=models.IntegerField ( null=True, unique=False,default='0', verbose_name='支付类型' )
    status=models.CharField ( max_length=255,null=True,unique=False, verbose_name='状态' )
    address=models.CharField ( max_length=255,null=True,unique=False, verbose_name='地址' )
    tel=models.CharField ( max_length=255,null=True,unique=False, verbose_name='电话' )
    consignee=models.CharField ( max_length=255,null=True,unique=False, verbose_name='收货人' )
    remark=models.CharField ( max_length=255,null=True,unique=False, verbose_name='备注' )
    logistics=models.TextField ( null=True, unique=False, verbose_name='物流' )
    goodtype=models.CharField ( max_length=255,null=True,unique=False, verbose_name='商品类型' )
    '''
    orderid=VARCHAR
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=Text
    buynumber=Integer
    price=Float
    discountprice=Float
    total=Float
    discounttotal=Float
    type=Integer
    status=VARCHAR
    address=VARCHAR
    tel=VARCHAR
    consignee=VARCHAR
    remark=VARCHAR
    logistics=Text
    goodtype=VARCHAR
    '''
    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '订单'

class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'
    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField ( null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255,null=True,unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False,unique=False, verbose_name='名称' )
    picture=models.TextField ( null=False, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255,null=True,unique=False, verbose_name='类型(1:收藏,21:赞,22:踩,31:竞拍参与,41:关注)' )
    inteltype=models.CharField ( max_length=255,null=True,unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255,null=True,unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'

class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'
    __loginUser__='yonghuming'
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuming'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __authTables__={}
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuming=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户名' )
    mima=models.CharField ( max_length=255,null=False,unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False,unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255,null=True,unique=False, verbose_name='性别' )
    touxiang=models.TextField ( null=True, unique=False, verbose_name='头像' )
    shouji=models.CharField ( max_length=255,null=True,unique=False, verbose_name='手机' )
    money=models.FloatField ( null=True, unique=False,default='0', verbose_name='余额' )
    '''
    yonghuming=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    touxiang=Text
    shouji=VARCHAR
    money=Float
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'

