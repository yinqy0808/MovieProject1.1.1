<template>
<div>
	<div :style='{"padding":"30px 0 30px 100px","margin":"o auto","borderRadius":"0","alignItems":"flex-end","background":"url(http://codegen.caihongy.cn/20230131/c788dee9481d4fd896e419a46388d74e.png) no-repeat center top","display":"flex","width":"100%"}' class="breadcrumb-preview">
		<el-breadcrumb :separator="'Ξ'" :style='{"fontSize":"14px","lineHeight":"1"}'>
			<el-breadcrumb-item>首页</el-breadcrumb-item>
			<el-breadcrumb-item v-for="(item, index) in breadcrumbItem" :key="index">{{item.name}}</el-breadcrumb-item>
		</el-breadcrumb>
	</div>
	
	<div class="list-preview" :style='{"width":"100%","margin":"0 auto","position":"relative","background":"none"}'>
		<div class="category-1" :style='{"width":"100%","padding":"10px","background":"linear-gradient(80deg, rgba(151,36,152,1) 0%, rgba(32,173,158,1) 100%)","display":"flex","height":"auto"}'>
			<div class="item" :class="swiperIndex == '-1' ? 'active' : ''" @click="getList(1, '全部')" :plain="isPlain">全部</div>
			<div class="item" :class="swiperIndex == index ? 'active' : ''" v-for="(item, index) in fenlei" :key="index" @click="getList(1, item, 'btn' + index)" :ref="'btn' + index" plain>{{item}}</div>
		</div>
		
	
    <el-form :inline="true" :model="formSearch" class="list-form-pv" :style='{"padding":"10px","alignItems":"center","flexWrap":"wrap","background":"none","display":"flex","width":"100%","height":"auto"}'>
      <el-form-item :style='{"alignItems":"center","margin":"0 10px","display":"flex"}'>
	    <div class="lable" v-if="true" :style='{"width":"auto","padding":"0 10px","lineHeight":"42px","display":"inline-block"}'>电影名称</div>
        <el-input v-model="formSearch.dianyingmingcheng" placeholder="电影名称" clearable></el-input>
      </el-form-item>
      <el-form-item :style='{"alignItems":"center","margin":"0 10px","display":"flex"}'>
		<div class="lable" v-if="true" :style='{"width":"auto","padding":"0 10px","lineHeight":"42px","display":"inline-block"}'>电影产地</div>
        <el-select v-model="formSearch.dianyingchandi" placeholder="请选择电影产地" :clearable="true">
          <el-option v-for="(item, index) in dianyingchandiOptions" :key="index" :label="item" :value="item"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item :style='{"alignItems":"center","margin":"0 10px","display":"flex"}'>
	    <div class="lable" v-if="true" :style='{"width":"auto","padding":"0 10px","lineHeight":"42px","display":"inline-block"}'>演员阵容</div>
        <el-input v-model="formSearch.yanyuanzhenrong" placeholder="演员阵容" clearable></el-input>
      </el-form-item>
      <el-form-item :style='{"alignItems":"center","margin":"0 10px","display":"flex"}'>
		<div class="lable" v-if="true" :style='{"width":"auto","padding":"0 10px","lineHeight":"42px","display":"inline-block"}'>放映厅</div>
        <el-select v-model="formSearch.fangyingting" placeholder="请选择放映厅" :clearable="true">
          <el-option v-for="(item, index) in fangyingtingOptions" :key="index" :label="item" :value="item"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item :style='{"alignItems":"center","margin":"0 10px","display":"flex"}'>
	    <div class="lable" v-if="true" :style='{"width":"auto","padding":"0 10px","lineHeight":"42px","display":"inline-block"}'>价格</div>
        <el-input v-model="formSearch.pricestart" placeholder="最小价格" clearable></el-input>
      </el-form-item>
      <el-form-item :style='{"alignItems":"center","margin":"0 10px","display":"flex"}'>
        <el-input v-model="formSearch.priceend" placeholder="最大价格" clearable></el-input>
      </el-form-item>
	  <el-button v-if=" true " :style='{"cursor":"pointer","border":"0","padding":"0px 35px","margin":"0 10px 0 0","color":"#fff","minWidth":"90px","outline":"none","borderRadius":"0","background":"linear-gradient(90deg, rgba(151,36,152,1) 0%, rgba(32,173,158,1) 100%),#992298","width":"auto","fontSize":"14px","lineHeight":"42px","height":"42px"}' type="primary" @click="getList(1, curFenlei)"><i v-if="true" :style='{"color":"#fff","margin":"0 10px 0 0","fontSize":"14px"}' class="el-icon-search"></i>查询</el-button>
	  <el-button v-if="isAuth('dianyingxinxi','新增')" :style='{"cursor":"pointer","border":"0","padding":"0px 35px","margin":"0 10px 0 0","color":"#fff","minWidth":"90px","outline":"none","borderRadius":"0","background":"#20ad9e","width":"auto","fontSize":"14px","lineHeight":"42px","height":"42px"}' type="primary" @click="add('/index/dianyingxinxiAdd')"><i v-if="true" :style='{"color":"#fff","margin":"0 10px 0 0","fontSize":"14px"}' class="el-icon-circle-plus-outline"></i>添加</el-button>
    </el-form>

	<div class="list" :style='{"width":"100%","padding":"20px 7%","margin":"20px 0 10px","background":"none"}'>
		<!-- 样式一 -->
		<div class="list1 index-pv1" :style='{"padding":"0","margin":"30px 0 0","flexWrap":"wrap","background":"none","display":"flex","width":"100%","height":"auto"}'>
			<div :style='{"width":"30%","margin":"0 3% 20px 0","position":"relative","background":"none","height":"auto"}' v-for="(item, index) in dataList" :key="index" @click="toDetail(item)" class="list-item animation-box">
				<img :style='{"padding":"20px","margin":"0 0 12px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230131/6afa6fc6db7b4b62bd4e8f4a24f3975e.png) no-repeat center top / 100% 100%","display":"block","width":"100%","height":"280px"}' v-if="item.dianyinghaibao && item.dianyinghaibao.substr(0,4)=='http'" :src="item.dianyinghaibao" class="image" />
				<img :style='{"padding":"20px","margin":"0 0 12px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230131/6afa6fc6db7b4b62bd4e8f4a24f3975e.png) no-repeat center top / 100% 100%","display":"block","width":"100%","height":"280px"}' v-else :src="baseUrl + (item.dianyinghaibao?item.dianyinghaibao.split(',')[0]:'')" class="image" />
				<div v-if="item.price" :style='{"padding":"4px 10px","margin":"o auto","color":"red","textAlign":"center","width":"90%","lineHeight":"24px","fontSize":"14px"}' class="price"><span :style='{"fontSize":"12px"}'>￥</span>{{item.price}}</div>
				<div :style='{"padding":"4px 0","margin":"0 auto 10px","whiteSpace":"nowrap","overflow":"hidden","color":"#333","textAlign":"center","background":"linear-gradient(0deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","width":"90%","lineHeight":"30px","fontSize":"14px","textOverflow":"ellipsis"}' class="name ">{{item.dianyingmingcheng}}</div>
			</div>
		</div>
		
		<!-- 样式二 -->
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

  </div>
</div>
</template>

<script>
  export default {
    //数据集合
    data() {
      return {
	    layouts: '',
		swiperIndex: -1,
        baseUrl: '',
        breadcrumbItem: [
          {
            name: '电影信息'
          }
        ],
        formSearch: {
          dianyingmingcheng: '',
          dianyingchandi: '',
          yanyuanzhenrong: '',
          fangyingting: '',
          price: '',
        },
        fenlei: [],
        dataList: [],
        total: 1,
        pageSize: 12,
		pageSizes: [10,20,30,50],
        totalPage: 1,
        curFenlei: '全部',
        isPlain: false,
        indexQueryCondition: '',
	      dianyingchandiOptions: [],
	      fangyingtingOptions: [],
        timeRange: []
      }
    },
    created() {
      this.indexQueryCondition = this.$route.query.indexQueryCondition ? this.$route.query.indexQueryCondition : '';
      this.baseUrl = this.$config.baseUrl;
	    this.dianyingchandiOptions = '大陆,港台,日韩,欧美,其它'.split(',');
	    this.fangyingtingOptions = '1号厅,2号厅,3号厅,4号厅,5号厅,6号厅,情侣厅,巨幕厅'.split(',');
      this.getFenlei();
      this.getList(1, '全部');
    },
    //方法集合
    methods: {
      add(path) {
        this.$router.push({path: path});
      },
      getFenlei() {
        this.$http.get('option/dianyingfenlei/dianyingfenlei').then(res => {
          if (res.data.code == 0) {
            this.fenlei = res.data.data;
          }
        });
      },
      getList(page, fenlei, ref = '') {
		if(fenlei == '全部') this.swiperIndex = -1;
		for(let i=0;i<this.fenlei.length;i++) {
			if(fenlei == this.fenlei[i]) {
				this.swiperIndex = i;
				break;
			}
		}
        this.curFenlei = fenlei;
        if (this.curFenlei == '全部') {
          this.isPlain = false;
        } else {
          this.isPlain = true;
        }
        let params = {page, limit: this.pageSize};
        let searchWhere = {};
        if (this.indexQueryCondition) {
          searchWhere.dianyingmingcheng = '%' + this.indexQueryCondition + '%';
          this.indexQueryCondition = '';
        }
        if (this.formSearch.dianyingmingcheng != '') searchWhere.dianyingmingcheng = '%' + this.formSearch.dianyingmingcheng + '%';
        if (this.formSearch.dianyingchandi != '') searchWhere.dianyingchandi = this.formSearch.dianyingchandi;
        if (this.formSearch.yanyuanzhenrong != '') searchWhere.yanyuanzhenrong = '%' + this.formSearch.yanyuanzhenrong + '%';
        if (this.formSearch.fangyingting != '') searchWhere.fangyingting = this.formSearch.fangyingting;
        if(this.formSearch.pricestart!='' && this.formSearch.pricestart!=undefined ){
          searchWhere.pricestart = this.formSearch.pricestart
        }
        if(this.formSearch.priceend!='' && this.formSearch.priceend!=undefined){
          searchWhere.priceend = this.formSearch.priceend
        }
        if (this.curFenlei != '全部') searchWhere.dianyingfenlei = this.curFenlei;
        this.$http.get('dianyingxinxi/list', {params: Object.assign(params, searchWhere)}).then(res => {
          if (res.data.code == 0) {
            this.dataList = res.data.data.list;
            this.total = res.data.data.total;
            this.pageSize = res.data.data.pageSize;
            this.totalPage = res.data.data.totalPage;
			
			this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
          }
        });
      },
      curChange(page) {
        this.getList(page,this.curFenlei);
      },
      prevClick(page) {
        this.getList(page,this.curFenlei);
      },
      nextClick(page) {
        this.getList(page,this.curFenlei);
      },
      toDetail(item) {
        this.$router.push({path: '/index/dianyingxinxiDetail', query: {detailObj: JSON.stringify(item)}});
      },
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.list-preview .list-form-pv .el-input {
		width: auto;
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
	
	.category-1 .item {
		cursor: pointer;
		border: 8px solid #ccc;
		border-radius: 0;
		padding: 0 40px;
		margin: 0 10px 0 0;
		color: #333;
		background: #fff;
		border-image: linear-gradient(to right, #ddd, #eee) 1;
		width: auto;
		font-size: 14px;
		line-height: 36px;
		text-align: center;
	}
	
	.category-1 .item:hover {
		cursor: pointer;
		border: 8px solid #8dd4cc;
		border-radius: 0;
		padding: 0 40px;
		margin: 0 10px 0 0;
		color: #333;
		background: #fff;
		width: auto;
		font-size: 14px;
		line-height: 36px;
		text-align: center;
	}
	
	.category-1 .item.active {
		cursor: pointer;
		border: 8px solid #8dd4cc;
		border-radius: 0;
		padding: 0 40px;
		margin: 0 10px 0 0;
		color: #333;
		background: #fff;
		width: auto;
		font-size: 14px;
		line-height: 36px;
		text-align: center;
	}
	
	.category-2 .item {
		cursor: pointer;
		border-radius: 4px;
		margin: 0 0 10px 0;
		color: #999;
		background: #efefef;
		width: 100%;
		font-size: 14px;
		line-height: 36px;
		text-align: center;
	}
	
	.category-2 .item:hover {
		cursor: pointer;
		border-radius: 4px;
		margin: 0 0 10px 0;
		color: #999;
		background: #efefef;
		width: 100%;
		font-size: 14px;
		line-height: 36px;
		text-align: center;
	}
	
	.category-2 .item.active {
		cursor: pointer;
		border-radius: 4px;
		margin: 0 0 10px 0;
		color: #999;
		background: #efefef;
		width: 100%;
		font-size: 14px;
		line-height: 36px;
		text-align: center;
	}
	
	.list-form-pv .el-input /deep/ .el-input__inner {
		border: 1px solid #eee;
		border-radius: 0;
		padding: 0 10px;
		margin: 0;
		outline: none;
		color: #555;
		width: 140px;
		font-size: 14px;
		line-height: 40px;
		height: 40px;
	}
	
	.list-form-pv .el-select /deep/ .el-input__inner {
		border: 1px solid #eee;
		border-radius: 0;
		padding: 0 30px 0 10px;
		margin: 0;
		outline: none;
		color: #555;
		width: 120px;
		font-size: 14px;
		line-height: 40px ;
		height: 40px;
	}
	
	.list-form-pv .el-date-editor /deep/ .el-input__inner {
		border: 1px solid #eee;
		border-radius: 0;
		padding: 0 30px;
		margin: 0;
		outline: none;
		color: #555;
		width: 140px;
		font-size: 14px;
		line-height: 40px;
		height: 40px;
	}
	
	.list .index-pv1 .animation-box {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		z-index: initial;
	}
	
	.list .index-pv1 .animation-box:hover {
		transform: rotate(360deg) scale(1.2) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		-webkit-perspective: 1000px;
		perspective: 1000px;
		transition: 0.3s;
		z-index: 1;
	}
	
	.list .index-pv1 .animation-box img {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
	}
	
	.list .index-pv1 .animation-box img:hover {
		transform: rotate(360deg) scale(0.8) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		-webkit-perspective: 1000px;
		perspective: 1000px;
		transition: 0.3s;
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
</style>
