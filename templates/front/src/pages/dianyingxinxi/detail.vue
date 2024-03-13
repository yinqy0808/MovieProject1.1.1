<template>
<div>
	<div :style='{"padding":"30px 0 30px 100px","margin":"o auto","borderRadius":"0","alignItems":"flex-end","background":"url(http://codegen.caihongy.cn/20230131/c788dee9481d4fd896e419a46388d74e.png) no-repeat center top","display":"flex","width":"100%"}' class="breadcrumb-preview">
		<el-breadcrumb :separator="'Ξ'" :style='{"fontSize":"14px","lineHeight":"1"}'>
			<el-breadcrumb-item>首页</el-breadcrumb-item>
			<el-breadcrumb-item v-for="(item, index) in breadcrumbItem" :key="index">{{item.name}}</el-breadcrumb-item>
		</el-breadcrumb>
	</div>
	
	<div class="detail-preview" :style='{"margin":"0 auto","alignItems":"flex-start","flexWrap":"wrap","display":"flex","width":"100%","position":"relative","justifyContent":"space-between"}'>
		<div class="attr" :style='{"padding":"0","overflow":"hidden","flexWrap":"wrap","background":"none","display":"flex","width":"100%","position":"relative","justifyContent":"space-between"}'>
			<el-carousel :style='{"width":"48%","padding":"0","margin":"20px auto","height":"400px"}' trigger="click" indicator-position="inside" arrow="always" type="default" direction="horizontal" height="400px" autoplay="false" interval="3000" loop="true">
				<el-carousel-item :style='{"borderRadius":"0","width":"100%","height":"100%"}' v-for="item in detailBanner" :key="item.id">
					<el-image :style='{"width":"100%","objectFit":"cover","borderRadius":"250px","height":"100%"}' v-if="item.substr(0,4)=='http'" :src="item" fit="cover" class="image"></el-image>
					<el-image :style='{"width":"100%","objectFit":"cover","borderRadius":"250px","height":"100%"}' v-else :src="baseUrl + item" fit="cover" class="image"></el-image>
				</el-carousel-item>
			</el-carousel>
	
			
			<div class="info" :style='{"minHeight":"500px","width":"44%","padding":"20px 0","margin":"0","background":"none"}'>
				<div class="item" :style='{"padding":"10px 20px 16px 50px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(0deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","justifyContent":"space-between","display":"flex"}'>
					<div :style='{"color":"#333","fontSize":"20px","fontWeight":"bold"}'>
                    {{detail.dianyingmingcheng}}
                    </div>
					<div @click="storeup(1)" v-show="!isStoreup" :style='{"borderRadius":"20px","padding":"8px 10px","background":"#fff"}'><i v-if="true" :style='{"color":"#992298","fontSize":"16px"}' class="el-icon-star-off"></i><span :style='{"color":"#992298","fontSize":"14px"}'>点我收藏</span></div>
					<div @click="storeup(-1)" v-show="isStoreup" :style='{"borderRadius":"20px","padding":"8px 10px","background":"#fff"}'><i v-if="true" :style='{"color":"#992298","fontSize":"16px"}' class="el-icon-star-on"></i><span :style='{"color":"#992298","fontSize":"14px"}'>取消收藏</span></div>
				</div>

				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}' v-if="detail.price">
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>价格</div>
					<div style="font-weight: bold;" :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'><span :style='{"fontSize":"12px"}'>￥</span>{{detail.price}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}' v-if="detail.jf">
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>积分</div>
					<div style="color: red;font-weight: bold;" :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.jf}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}'>
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>电影分类</div>
					<div  :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.dianyingfenlei}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}'>
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>电影产地</div>
					<div  :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.dianyingchandi}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}'>
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>演员阵容</div>
					<div  :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.yanyuanzhenrong}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}'>
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>电影导演</div>
					<div  :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.dianyingdaoyan}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}'>
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>上映日期</div>
					<div  :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.shangyingriqi}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}'>
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>放映场次</div>
					<div  :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.fangyingchangci}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}'>
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>放映厅</div>
					<div  :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.fangyingting}}</div>
				</div>
				<div class="item" :style='{"border":"0 dotted #bfe7e3","padding":"0","margin":"0 0 10px 0","background":"none","borderWidth":"0 0 2px","display":"flex","justifyContent":"spaceBetween"}'>
					<div class="lable" :style='{"padding":"0 10px","color":"#992298","textAlign":"right","width":"auto","fontSize":"14px","lineHeight":"40px","minWidth":"120px","height":"40px"}'>座位总数</div>
					<div  :style='{"padding":"4px 10px 0","color":"#666","background":"none","width":"100%","fontSize":"14px","lineHeight":"24px","height":"40px"}'>{{detail.number}}</div>
				</div>
				<div class="btn" :style='{"padding":"10px 0","flexWrap":"wrap","display":"flex"}'>
					<el-button :style='{"border":"0","cursor":"pointer","padding":"0 10px","margin":"0 5px 0 0","outline":"none","color":"#fff","borderRadius":"30px","background":"#eabf3f","width":"auto","lineHeight":"40px","fontSize":"14px","height":"40px"}' type="warning" size="small" @click="bookClick">立即预订</el-button>
				</div>
				<div class="btn" :style='{"padding":"10px 0","flexWrap":"wrap","display":"flex"}'>
				</div>
			</div>
			
		</div>
		
		<video :style='{"border":"10px outset #93e4db","padding":"12px","margin":"60px 0 0 7%","outline":"none","borderRadius":"0","display":"block","width":"30%","float":"right"}' :src="baseUrl +  detail.yugaoshipin" controls="controls">
			您的浏览器不支持视频播放
		</video>
		
		<el-tabs class="detail" :style='{"border":"0px solid #DCDFE6","boxShadow":"0 0px 0px 0 rgba(0, 0, 0, .1)","margin":"60px 7% 0","background":"none","flex":"1","width":"50%","float":"left"}' v-model="activeName" type="border-card">
			<el-tab-pane label="电影介绍" name="first">
				<div v-html="detail.dianyingjieshao"></div>
			</el-tab-pane>
			<el-tab-pane label="评论" name="second">
				<el-form class="add comment" :style='{"width":"100%","boxShadow":"0 0px 0px 0 rgba(0, 0, 0, .1)","padding":"15px","margin":"0 0 20px"}' :model="form" :rules="rules" ref="form">
					<el-form-item class="item" :style='{"width":"100%","display":"flex","height":"auto"}' label="评论" prop="content">
						<el-input type="textarea" :rows="5" v-model="form.content" placeholder="请输入内容"></el-input>
					</el-form-item>
					<el-form-item class="btn" :style='{"width":"100%","padding":"0 0 0 80px","margin":"30px 0 0","textAlign":"center","height":"auto"}'>
						<el-button :style='{"border":"0","cursor":"pointer","padding":"0","margin":"0 20px 0 0","outline":"none","color":"rgba(255, 255, 255, 1)","borderRadius":"10px","background":"linear-gradient(90deg, rgba(32,173,158,1) 0%, rgba(138,228,219,1) 50%, rgba(32,173,158,1) 100%),#20ad9e","width":"110px","lineHeight":"40px","fontSize":"14px","height":"40px"}' type="primary" @click="submitForm('form')">立即提交</el-button>
						<el-button :style='{"border":"0","cursor":"pointer","padding":"0","margin":"0 20px 0 0","outline":"none","color":"rgba(255, 255, 255, 1)","borderRadius":"10px","background":"linear-gradient(90deg, rgba(153,153,153,1) 0%, rgba(204,204,204,1) 50%, rgba(153,153,153,1) 100%),#999","width":"110px","lineHeight":"40px","fontSize":"14px","height":"40px"}' @click="resetForm('form')">重置</el-button>
					</el-form-item>
				</el-form>
				
				<div v-if="infoList.length" :style='{"width":"100%","boxShadow":"0 0px 0px 0 rgba(0, 0, 0, .1)","padding":"15px"}' class="comment">
					<div :style='{"padding":"10px","margin":"0 0 20px","borderColor":"#999","alignItems":"center","borderWidth":"0","width":"100%","borderStyle":"solid","height":"auto"}' v-for="item in infoList" :key="item.id">
						<div class="user" :style='{"padding":"6px 0 ","alignItems":"center","background":"linear-gradient(180deg, rgba(255,255,255,1) 0%, rgba(240,240,240,1) 95%, rgba(189,189,189,1) 100%)","flexDirection":"row-reverse","display":"flex","width":"100%","justifyContent":"center","height":"auto"}'>
							<el-image v-if="item.avatarurl" :style='{"width":"40px","margin":"0 10px","borderRadius":"100%","objectFit":"cover","height":"40px"}' :size="50" :src="baseUrl + item.avatarurl"></el-image>
							<el-image v-if="!item.avatarurl" :style='{"width":"40px","margin":"0 10px","borderRadius":"100%","objectFit":"cover","height":"40px"}' :size="50" :src="require('@/assets/touxiang.png')"></el-image>
							<div :style='{"color":"#992298","fontSize":"16px"}' class="name">{{item.nickname}}</div>
						</div>
						<div :style='{"padding":"8px","margin":"10px 0px 0px","color":"#20ad9e","borderRadius":"0","background":"none","lineHeight":"24px","fontSize":"14px","textIndent":"2em"}' class="content-block-ask">
							{{item.content}}
						</div>
						<div :style='{"padding":"8px","margin":"10px 0px 0px","color":"#20ad9e","borderRadius":"0","background":"none","lineHeight":"24px","fontSize":"14px","textIndent":"2em"}' class="content-block-reply" v-if="item.reply">
							回复：{{item.reply}}
						</div>
					</div>
				</div>
				
				<el-pagination
				  background
				  class="pagination"
				  :pager-count="7"
				  :page-size="pageSize"
				  :page-sizes="pageSizes"
				  prev-text="<"
				  next-text=">"
				  :hide-on-single-page="true"
				  :layout='["total","prev","pager","next","sizes","jumper"].join()'
				  :total="total"
				  :style='{"padding":"0","margin":"10px auto","whiteSpace":"nowrap","color":"#333","textAlign":"center","width":"1200px","fontWeight":"500"}'
				  @current-change="curChange"
				  @prev-click="prevClick"
				  @next-click="nextClick"
				></el-pagination>
			</el-tab-pane>
			
			<el-tab-pane label="选座" name="last">
				<div class="seat-list">
					<div v-for="(item, index) in numberList" v-bind:key="index" class="seat-item">
						<img @click="selectTip()" v-if="item.select" class="seat-icon" src="../../assets/select.png" />
						<img @click="selectSeat(item)" v-else-if="!item.active" class="seat-icon" src="../../assets/unselect.png" />
						<img @click="unselectSeat(item)" v-else class="seat-icon" src="../../assets/select.png" />
						<span>{{item.name}}</span>
					</div>
				</div>
			</el-tab-pane>
		</el-tabs>
	</div>
</div>
</template>

<script>
  import CountDown from '@/components/CountDown';
  export default {
    //数据集合
    data() {
      return {
        tablename: 'dianyingxinxi',
        baseUrl: '',
        breadcrumbItem: [
          {
            name: '详情信息'
          }
        ],
        title: '',
        detailBanner: [],
        endTime: 0,
        detail: {},
        activeName: 'first',
        form: {
          content: '',
          userid: localStorage.getItem('userid'),
          nickname: localStorage.getItem('username'),
          avatarurl: '',
        },
        infoList: [],
        total: 1,
        pageSize: 5,
		pageSizes: [10,20,30,50],
        totalPage: 1,
        rules: {
          content: [
            { required: true, message: '请输入内容', trigger: 'blur' }
          ]
        },
        storeupParams: {
          name: '',
          picture: '',
          refid: 0,
          tablename: 'dianyingxinxi',
          userid: localStorage.getItem('userid')
        },
        isStoreup: false,
        storeupInfo: {},
        buynumber: 1,
        numberList: [],
      }
    },
    created() {
        this.init();
    },
    //方法集合
    methods: {
        init() {
          this.baseUrl = this.$config.baseUrl;
          if(this.$route.query.detailObj) {
            this.detail = JSON.parse(this.$route.query.detailObj);
          }
          if(this.$route.query.storeupObj) {
            this.detail.id = JSON.parse(this.$route.query.storeupObj).refid;
          }
          if(this.$route.query.discussObj) {
            this.detail.id = JSON.parse(this.$route.query.discussObj).goodid;
          }
          this.$http.get(this.tablename + '/detail/'  + this.detail.id, {}).then(res => {
            if (res.data.code == 0) {
              this.detail = res.data.data;
              this.title = this.detail.dianyingmingcheng;
              this.detailBanner = this.detail.dianyinghaibao ? this.detail.dianyinghaibao.split(",") : [];
              this.$forceUpdate();
            }
          });

          this.getDiscussList(1);
          this.getStoreupStatus();

          let selectArray = this.detail.selected.split(',');
          for (let i = 1; i <= this.detail.number; i++) {
            this.numberList.push({
              name: `${i}号`,
              select: false,
              active: false
            });
          }
          for (let i = 0; i < this.detail.selected.split(',').length; i++) {
            this.numberList[this.detail.selected.split(',')[i]-1].select = true;
          }
        },
    createOrder() {
      let order = '';
      let now = new Date();
      order += now.getFullYear();
      order += now.getMonth() + 1;
      order += now.getDate();
      order += now.getHours();
      order += now.getMinutes();
      order += now.getSeconds();
      order += now.getMilliseconds();
      return order;
    },
    bookClick() {
            let activeSeat = [];
            for(let i=0;i<this.numberList.length;i++){
                if(this.numberList[i].active){
                    activeSeat.push(this.numberList[i].name.replace('号',''));
                }
            }
            if (activeSeat.length==0) {
                this.$message({
                  type: 'error',
                  message: '请选择要预定的位置!',
                  duration: 1500
                });
                return
            }
            let data = {
                orderid: this.createOrder(),
                tablename: this.tablename,
                userid: localStorage.getItem('userid'),
                goodid: this.detail.id,
                goodname: this.title,
                picture:this.detailBanner[0],
                goodtype: this.detail.dianyingfenlei,
                buynumber: activeSeat.length,
                total: 0,
                discounttotal: 0,
                address: activeSeat.join(','),
                activeSeat: activeSeat.join(','),
                status: '已支付',
                discountprice: this.detail.vipprice 
            }
            if (this.detail.price) {
                data['status'] = '未支付'
                data['price'] = this.detail.price
                data['total'] = parseFloat(data['price'] * activeSeat.length).toFixed(2)
                localStorage.setItem('orderGoods', JSON.stringify([data]));
                // 跳转到确认下单页面
                let query = {
                    type: 1,
                    seat: 1
                }
                this.$confirm('是否确认预定？')
                  .then(_ => {
                    this.$router.push({path: '/index/shop-order/orderConfirm', query: query});
                  }).catch(_ => {});
            } else {
                //let oldSelectedArray = this.detail.selected?this.detail.selected.split(","):[];
                // 新的预定座位号
                //let newSelectArray = oldSelectedArray.concat(activeSeat);
                // 赋值给参数
                    this.detail.selected = newSelectArray.join(',');
                //data['price'] = 0
                //layui.http.requestJson(`orders/add`, 'post', data, (res) => {
                    // 修改数据被选中座位信息
                 //   layui.http.requestJson(`${this.detailTable}/update`, 'post', this.detail, (res) => {
                  //      layer.msg(`预定成功`, {
                   //         time: 2000,
                    //        icon: 6
                     //   });
                    //});
                //})
            }
      },
      selectTip() {
        this.$message({
          type: 'error',
          message: '该座位已被预定!',
          duration: 1500
        });
      },
      selectSeat(item) {
        item.active = true;
      },
      unselectSeat(item) {
        item.active = false;
      },
      storeup(type) {
        if (type == 1 && !this.isStoreup) {
          this.storeupParams.name = this.title;
          this.storeupParams.picture = this.detailBanner[0];
          this.storeupParams.inteltype = this.detail.dianyingfenlei;
          this.storeupParams.refid = this.detail.id;
          this.storeupParams.type = type;
          this.$http.post('storeup/add', this.storeupParams).then(res => {
            if (res.data.code == 0) {
              this.isStoreup = true;
              this.$message({
                type: 'success',
                message: '收藏成功!',
                duration: 1500,
              });
            }
          });
        }
        if (type == -1 && this.isStoreup) {
          let delIds = new Array();
          delIds.push(this.storeupInfo.id);
          this.$http.post('storeup/delete', delIds).then(res => {
            if (res.data.code == 0) {
              this.isStoreup = false;
              this.$message({
                type: 'success',
                message: '取消成功!',
                duration: 1500,
              });
            }
          });
        }
      },
      getStoreupStatus(){
        if(localStorage.getItem("Token")) {
            this.$http.get('storeup/list', {params: {page: 1, limit: 1, type: 1, refid: this.detail.id, tablename: 'dianyingxinxi', userid: localStorage.getItem('userid')}}).then(res => {
              if (res.data.code == 0 && res.data.data.list.length > 0) {
                this.isStoreup = true;
                this.storeupInfo = res.data.data.list[0];
              }
            });
        }
      },
      curChange(page) {
        this.getDiscussList(page);
      },
      prevClick(page) {
        this.getDiscussList(page);
      },
      nextClick(page) {
        this.getDiscussList(page);
      },
      // 下载
      download(file){
        if(!file) {
            this.$message({
              type: 'error',
              message: '文件不存在',
              duration: 1500,
            });
            return;
        }
        window.open(this.baseUrl+file)
      },
      getDiscussList(page) {
        this.$http.get('discussdianyingxinxi/list', {params: {page, limit: this.pageSize, refid: this.detail.id}}).then(res => {
          if (res.data.code == 0) {
            this.infoList = res.data.data.list;
            this.total = res.data.data.total;
            this.pageSize = res.data.data.pageSize;this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
            this.totalPage = res.data.data.totalPage;
          }
        });
      },
      submitForm(formName) {
        let sensitiveWords = "";
        let sensitiveWordsArr = [];
        if(sensitiveWords) {
            sensitiveWordsArr = sensitiveWords.split(",");
        }
        for(var i=0; i<sensitiveWordsArr.length; i++){
            //全局替换
            var reg = new RegExp(sensitiveWordsArr[i],"g");
            //判断内容中是否包括敏感词
            if (this.form.content.indexOf(sensitiveWordsArr[i]) > -1) {
                // 将敏感词替换为 **
                this.form.content = this.form.content.replace(reg,"**");
            }
        }
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$http.get('orders/list', {params: {page: 1, limit: 1, status: '已完成', goodid: this.detail.id, userid: localStorage.getItem('userid')}}).then(res => {
                if (res.data.code == 0 && res.data.data.list.length == 0) {
                  this.$message({
                    type: 'success',
                    message: '请完成订单后再评论!',
                    duration: 1500
                  });
                  return false
                } else {
                    this.form.refid = this.detail.id;
                    this.form.avatarurl = localStorage.getItem('headportrait')?localStorage.getItem('headportrait'):'';
                    this.$http.post('discussdianyingxinxi/add', this.form).then(res => {
                      if (res.data.code == 0) {
                        this.form.content = '';
                        this.getDiscussList(1);
                        this.$message({
                          type: 'success',
                          message: '评论成功!',
                          duration: 1500,
                        });
                      }
                    });
                }
            });
          } else {
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
        //立即购买
        buyNow() {
            // 保存到storage中，在确认下单页面中获取要购买的商品
            localStorage.setItem('orderGoods', JSON.stringify([{
                tablename: this.tablename,
                goodid: this.detail.id,
                goodname: this.title,
                goodtype: this.detail.dianyingfenlei,

                picture:this.detailBanner[0],
                buynumber: this.buynumber,
                userid: localStorage.getItem('userid'),
                price: this.detail.price,
                discountprice: this.detail.vipprice ? this.detail.vipprice : 0
            }]));
            // 跳转到确认下单页面
            let query = {
                type: 1,
            }
            this.$router.push({path: '/index/shop-order/orderConfirm', query: query});
        },


    },
    components: {
      CountDown
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.detail-preview {
	
	  .attr {
	    .el-carousel /deep/ .el-carousel__indicator button {
	      width: 0;
	      height: 0;
	      display: none;
	    }
	
	    .el-input-number__decrease:hover:not(.is-disabled)~.el-input .el-input__inner:not(.is-disabled), .el-input-number__increase:hover:not(.is-disabled)~.el-input .el-input__inner:not(.is-disabled) {
	      border-color: none;
	    }
	  }
	
	  .detail {
	    & /deep/ .el-tabs__header .el-tabs__nav-wrap {
	      margin-bottom: 0;
	    }
	
	    & .add .el-textarea {
	      width: auto;
	    }
	  }
	}
	
	.attr .el-carousel /deep/ .el-carousel__container .el-carousel__arrow--left {
		width: 36px;
		font-size: 12px;
		height: 36px;
	}
	
	.attr .el-carousel /deep/ .el-carousel__container .el-carousel__arrow--left:hover {
		background: #cca161;
	}
	
	.attr .el-carousel /deep/ .el-carousel__container .el-carousel__arrow--right {
		width: 36px;
		font-size: 12px;
		height: 36px;
	}
	
	.attr .el-carousel /deep/ .el-carousel__container .el-carousel__arrow--right:hover {
		background: #cca161;
	}

	.attr .el-carousel /deep/ .el-carousel__indicators {
		padding: 0;
		margin: 0;
		z-index: 2;
		position: absolute;
		list-style: none;
	}
	
	.attr .el-carousel /deep/ .el-carousel__indicators li {
		padding: 0;
		margin: 0 4px;
		background: #fff;
		display: inline-block;
		width: 12px;
		opacity: 0.4;
		transition: 0.3s;
		height: 12px;
	}
	
	.attr .el-carousel /deep/ .el-carousel__indicators li:hover {
		padding: 0;
		margin: 0 4px;
		background: #fff;
		display: inline-block;
		width: 24px;
		opacity: 0.7;
		height: 12px;
	}
	
	.attr .el-carousel /deep/ .el-carousel__indicators li.is-active {
		padding: 0;
		margin: 0 4px;
		background: #fff;
		display: inline-block;
		width: 24px;
		opacity: 1;
		height: 12px;
	}
	
	.attr .el-input-number /deep/ .el-input-number__decrease {
		cursor: pointer;
		z-index: 1;
		display: flex;
		border-color: #DCDFE6;
		border-radius: 4px 0 0 4px;
		top: 1px;
		left: 1px;
		background: #f5f5f5;
		width: 40px;
		justify-content: center;
		border-width: 0 1px 0 0;
		align-items: center;
		position: absolute;
		border-style: solid;
		text-align: center;
		height: 38px;
	}
	
	.attr .el-input-number /deep/ .el-input-number__decrease i {
		color: #666;
		font-size: 14px;
	}

	.attr .el-input-number /deep/ .el-input-number__increase {
		cursor: pointer;
		z-index: 1;
		display: flex;
		border-color: #DCDFE6;
		right: 1px;
		border-radius: 0 4px 4px 0;
		top: 1px;
		background: #f5f5f5;
		width: 40px;
		justify-content: center;
		border-width: 0 0 0 1px;
		align-items: center;
		position: absolute;
		border-style: solid;
		text-align: center;
		height: 38px;
	}
	
	.attr .el-input-number /deep/ .el-input-number__increase i {
		color: #666;
		font-size: 14px;
	}
	
	.attr .el-input-number /deep/ .el-input .el-input__inner {
		border: 1px solid #DCDFE6;
		border-radius: 4px;
		padding: 0 40px;
		outline: none;
		color: #666;
		background: #FFF;
		display: inline-block;
		width: 100%;
		font-size: 14px;
		line-height: 40px;
		text-align: center;
		height: 40px;
	}
	
	.detail-preview .detail.el-tabs /deep/ .el-tabs__header {
		padding: 12px 0 40px;
		margin: 0;
		background: linear-gradient(0deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%);
		display: flex;
		border-color: #E4E7ED;
		border-width: 0;
		justify-content: center;
		border-style: solid;
		text-align: center;
	}
	
	.detail-preview .detail.el-tabs /deep/ .el-tabs__header .el-tabs__item {
		border: 0;
		padding: 0 20px;
		margin: 0 10px 0 0;
		color: #333;
		font-weight: 500;
		display: inline-block;
		font-size: 14px;
		line-height: 40px;
		border-radius: 30px;
		background: #fff;
		position: relative;
		list-style: none;
		min-width: 110px;
		height: 40px;
	}
	
	.detail-preview .detail.el-tabs /deep/ .el-tabs__header .el-tabs__item:hover {
		border: 0;
		margin: 0 10px 0 0;
		color: #fff;
		background: #9f9fd7;
	}
	
	.detail-preview .detail.el-tabs /deep/ .el-tabs__header .el-tabs__item.is-active {
		border: 0;
		border-radius: 30px;
		margin: 0 10px 0 0;
		color: #fff;
		background: #9f9fd7;
		min-width: 110px;
	}
	
	.detail-preview .detail.el-tabs /deep/ .el-tabs__content {
		padding: 15px;
	}
	
	.detail-preview .detail.el-tabs .add /deep/ .el-form-item__label {
		padding: 0 10px 0 0;
		color: #666;
		width: 80px;
		font-size: 14px;
		line-height: 40px;
		text-align: right;
	}
	
	.detail-preview .detail.el-tabs .add /deep/ .el-textarea__inner {
		border: 1px solid #ddd;
		border-radius: 20px;
		padding: 15px;
		box-shadow: 0 0 0px rgba(64, 158, 255, .5);
		outline: none;
		color: #333;
		width: 600px;
		font-size: 14px;
		min-height: 150px;
		line-height: 32px;
	}
	
	.breadcrumb-preview .el-breadcrumb /deep/ .el-breadcrumb__separator {
		margin: 0 9px;
		color: #fff;
		font-weight: 500;
	}
	
	.breadcrumb-preview .el-breadcrumb /deep/ .el-breadcrumb__inner a {
		color: #111;
		display: inline-block;
	}

	.breadcrumb-preview .el-breadcrumb /deep/ .el-breadcrumb__inner {
		color: #fff;
		display: inline-block;
	}
	
	.el-pagination /deep/ .el-pagination__total {
		margin: 0 10px 0 0;
		color: #666;
		font-weight: 400;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		height: 28px;
	}
	
	.el-pagination /deep/ .btn-prev {
		border: none;
		border-radius: 2px;
		padding: 0;
		margin: 0 5px;
		color: #666;
		background: #f4f4f5;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		min-width: 35px;
		height: 28px;
	}
	
	.el-pagination /deep/ .btn-next {
		border: none;
		border-radius: 2px;
		padding: 0;
		margin: 0 5px;
		color: #666;
		background: #f4f4f5;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		min-width: 35px;
		height: 28px;
	}
	
	.el-pagination /deep/ .btn-prev:disabled {
		border: none;
		cursor: not-allowed;
		border-radius: 2px;
		padding: 0;
		margin: 0 5px;
		color: #C0C4CC;
		background: #f4f4f5;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		height: 28px;
	}
	
	.el-pagination /deep/ .btn-next:disabled {
		border: none;
		cursor: not-allowed;
		border-radius: 2px;
		padding: 0;
		margin: 0 5px;
		color: #C0C4CC;
		background: #f4f4f5;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		height: 28px;
	}
	
	.el-pagination /deep/ .el-pager {
		padding: 0;
		margin: 0;
		display: inline-block;
		vertical-align: top;
	}
	
	.el-pagination /deep/ .el-pager .number {
		cursor: pointer;
		padding: 0 4px;
		margin: 0 5px;
		color: #666;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		border-radius: 2px;
		background: #f4f4f5;
		text-align: center;
		min-width: 30px;
		height: 28px;
	}
	
	.el-pagination /deep/ .el-pager .number:hover {
		cursor: pointer;
		padding: 0 4px;
		margin: 0 5px;
		color: #fff;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		border-radius: 2px;
		background: #20ad9e;
		text-align: center;
		min-width: 30px;
		height: 28px;
}

.el-pagination /deep/ .el-pager .number.active {
		cursor: default;
		padding: 0 4px;
		margin: 0 5px;
		color: #fff;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		border-radius: 2px;
		background: #20ad9e;
		text-align: center;
		min-width: 30px;
		height: 28px;
	}
	
	.el-pagination /deep/ .el-pagination__sizes {
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		height: 28px;
	}
	
	.el-pagination /deep/ .el-pagination__sizes .el-input {
		margin: 0 5px;
		width: 100px;
		position: relative;
	}
	
	.el-pagination /deep/ .el-pagination__sizes .el-input .el-input__inner {
		border: 1px solid #DCDFE6;
		cursor: pointer;
		padding: 0 25px 0 8px;
		color: #606266;
		display: inline-block;
		font-size: 13px;
		line-height: 28px;
		border-radius: 3px;
		outline: 0;
		background: #FFF;
		width: 100%;
		text-align: center;
		height: 28px;
	}
	
	.el-pagination /deep/ .el-pagination__sizes .el-input span.el-input__suffix {
		top: 0;
		position: absolute;
		right: 0;
		height: 100%;
	}
	
	.el-pagination /deep/ .el-pagination__sizes .el-input .el-input__suffix .el-select__caret {
		cursor: pointer;
		color: #C0C4CC;
		width: 25px;
		font-size: 14px;
		line-height: 28px;
		text-align: center;
	}

	.el-pagination /deep/ .el-pagination__jump {
		margin: 0 0 0 24px;
		color: #606266;
		display: inline-block;
		vertical-align: top;
		font-size: 13px;
		line-height: 28px;
		height: 28px;
	}
	
	.el-pagination /deep/ .el-pagination__jump .el-input {
		border-radius: 3px;
		padding: 0 2px;
		margin: 0 2px;
		display: inline-block;
		width: 50px;
		font-size: 14px;
		line-height: 18px;
		position: relative;
		text-align: center;
		height: 28px;
	}
	
	.el-pagination /deep/ .el-pagination__jump .el-input .el-input__inner {
		border: 1px solid #DCDFE6;
		cursor: pointer;
		padding: 0 3px;
		color: #606266;
		display: inline-block;
		font-size: 14px;
		line-height: 28px;
		border-radius: 3px;
		outline: 0;
		background: #FFF;
		width: 100%;
		text-align: center;
		height: 28px;
	}
    .seat-list{
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        .seat-item{
            width: 20%;
            display: flex;
            flex-direction: column;
            align-items: center;
            span{
                line-height: 3;
            }
        }
    }
</style>
