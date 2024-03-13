<template>
<div class="home-preview" :style='{"width":"100%","margin":"0 auto","flexWrap":"wrap","justifyContent":"center","display":"flex"}'>
	<el-row type="flex" :gutter="5" justify="center" style="width: 100%">
		<el-col :span="3" v-if="queryList.length>1">
			<el-select v-model="queryIndex">
				<el-option
				  v-for="(item,index) in queryList"
				  :key="index"
				  :label="item.queryName"
				  :value="index"
				></el-option>
			</el-select>
		</el-col>
		<el-col :span="3" v-if="queryIndex==0">
			<el-input v-model="dianyingxinxidianyingmingcheng" placeholder="电影名称"></el-input>
		</el-col>
		<el-col :span="3" v-if="queryIndex==0">
			<el-button type="primary" @click="search('dianyingxinxi')">搜索</el-button>
		</el-col>
	</el-row>



<div class="recommend" :style='{"margin":"20px auto 0","alignItems":"flex-start","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20230130/d81fd2d44f4e475eb1c571b1f64e5fae.png) no-repeat center top","display":"flex","width":"100%","position":"relative","justifyContent":"center"}'>
	
    <div class="title" :style='{"margin":"50px 7% 80px","alignItems":"flex-start","textAlign":"center","background":"none","display":"flex","width":"50%","position":"relative","justifyContent":"center","height":"76px"}'>
		<span :style='{"margin":"0 10px 0 0","fontSize":"32px","color":"#202020","textAlign":"center","fontWeight":"600"}'>电影信息推荐</span>
	</div>
	
	
	
	
	
	<!-- 样式四 -->
	<div class="list list4 index-pv1" :style='{"width":"100%","padding":"20px 7% 40px","background":"none","height":"auto"}'>
		<div v-if="dianyingxinxiRecommend.length>0" class="list-item animation-box" @click="toDetail('dianyingxinxiDetail', dianyingxinxiRecommend[0])" :style='{"width":"48%","margin":"0","position":"relative","float":"right","height":"570px"}'>
			<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="dianyingxinxiRecommend[0].dianyinghaibao.substr(0,4)=='http'" :src="dianyingxinxiRecommend[0].dianyinghaibao.split(',')[0]" alt="" />
			<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (dianyingxinxiRecommend[0].dianyinghaibao?dianyingxinxiRecommend[0].dianyinghaibao.split(',')[0]:'')" alt="" />
			<div class="title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"32px","fontSize":"14px","position":"absolute","textOverflow":"ellipsis"}'>
                <div>{{dianyingxinxiRecommend[0].dianyingmingcheng}}</div>
            </div>
		</div>
		<div class="list-body" :style='{"width":"48%","margin":"0 0 10px","float":"left","justifyContent":"space-between","display":"flex","height":"275px"}'>
			<div v-if="dianyingxinxiRecommend.length>1" @click="toDetail('dianyingxinxiDetail', dianyingxinxiRecommend[1])" class="list-item animation-box" :style='{"width":"48%","margin":"0","position":"relative","display":"inline-block","height":"100%"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="dianyingxinxiRecommend[1].dianyinghaibao.substr(0,4)=='http'" :src="dianyingxinxiRecommend[1].dianyinghaibao.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (dianyingxinxiRecommend[1].dianyinghaibao?dianyingxinxiRecommend[1].dianyinghaibao.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"32px","fontSize":"14px","position":"absolute","textOverflow":"ellipsis"}'>
                    <div>{{dianyingxinxiRecommend[1].dianyingmingcheng}}</div>
                </div>
			</div>
			<div v-if="dianyingxinxiRecommend.length>2" @click="toDetail('dianyingxinxiDetail', dianyingxinxiRecommend[2])" class="list-item animation-box" :style='{"width":"48%","margin":"0","position":"relative","display":"inline-block","height":"100%"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="dianyingxinxiRecommend[2].dianyinghaibao.substr(0,4)=='http'" :src="dianyingxinxiRecommend[2].dianyinghaibao.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (dianyingxinxiRecommend[2].dianyinghaibao?dianyingxinxiRecommend[2].dianyinghaibao.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"32px","fontSize":"14px","position":"absolute","textOverflow":"ellipsis"}'>
                    <div>{{dianyingxinxiRecommend[2].dianyingmingcheng}}</div>
                </div>
			</div>
		</div>
		<div class="list-body" :style='{"width":"48%","margin":"10px 0 0","float":"left","justifyContent":"space-between","display":"flex","height":"275px"}'>
			<div v-if="dianyingxinxiRecommend.length>3" @click="toDetail('dianyingxinxiDetail', dianyingxinxiRecommend[3])" class="list-item animation-box" :style='{"width":"48%","margin":"0","position":"relative","display":"inline-block","height":"100%"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="dianyingxinxiRecommend[3].dianyinghaibao.substr(0,4)=='http'" :src="dianyingxinxiRecommend[3].dianyinghaibao.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (dianyingxinxiRecommend[3].dianyinghaibao?dianyingxinxiRecommend[3].dianyinghaibao.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"32px","fontSize":"14px","position":"absolute","textOverflow":"ellipsis"}'>
                    <div>{{dianyingxinxiRecommend[3].dianyingmingcheng}}</div>
                </div>
			</div>
			<div v-if="dianyingxinxiRecommend.length>4" @click="toDetail('dianyingxinxiDetail', dianyingxinxiRecommend[4])" class="list-item animation-box" :style='{"width":"48%","margin":"0","position":"relative","display":"inline-block","height":"100%"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="dianyingxinxiRecommend[4].dianyinghaibao.substr(0,4)=='http'" :src="dianyingxinxiRecommend[4].dianyinghaibao.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (dianyingxinxiRecommend[4].dianyinghaibao?dianyingxinxiRecommend[4].dianyinghaibao.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"32px","fontSize":"14px","position":"absolute","textOverflow":"ellipsis"}'>
                    <div>{{dianyingxinxiRecommend[4].dianyingmingcheng}}</div>
                </div>
			</div>
		</div>
	</div>
	
	
	
	
	
	
	<div @click="moreBtn('dianyingxinxi')" :style='{"border":"0","padding":"0 12px 0 20px","margin":"o auto","borderRadius":"30px","textAlign":"center","background":"url(http://codegen.caihongy.cn/20230130/900bb2bf212e4ef8a599ed8502aa2b9d.png) no-repeat 90% center,linear-gradient(90deg, rgba(151,36,152,1) 0%, rgba(32,173,158,1) 100%),#20ad9e","display":"inline-block","width":"80px","lineHeight":"44px","minWidth":"200px","height":"44px"}'>
		<span :style='{"color":"#fff","fontSize":"14px"}'>查看更多</span>
		<i v-if="true" :style='{"color":"#f5f5f5","fontSize":"12px","display":"none"}' class="el-icon-d-arrow-right"></i>
	</div>
	
	<div v-if="true" class="idea recommendIdea" :style='{"padding":"0","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20230130/aacb0fbd36e642799c61ce8641b160ed.jpg) no-repeat center top / 100% auto","display":"flex","width":"100%","justifyContent":"space-between","height":"600px"}'>
		<div class="box1" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box2" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
</div>




	
<div class="news" :style='{"width":"56%","margin":"0 7%","position":"relative","flexWrap":"wrap","background":"none","display":"flex"}'>
	<div v-if="false" class="idea newsIdea" :style='{"padding":"20px","flexWrap":"wrap","background":"#efefef","justifyContent":"space-between","display":"flex"}'>
		<div class="box1" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	<div class="title" :style='{"margin":"30px auto 20px","alignItems":"center","textAlign":"center","background":"none","display":"flex","width":"100%","position":"relative","justifyContent":"flex-start","height":"50px"}'>
		<span :style='{"fontSize":"32px","lineHeight":"60px","color":"#202020","fontWeight":"bold","height":"60px"}'>公告信息</span>
	</div>
	
	
	
	
	
	
	
	
	
	<!-- 样式八 -->
	<div v-if="newsList.length" class="list list8 index-pv1" :style='{"width":"100%","padding":"0","flexWrap":"wrap","background":"none","display":"flex","height":"auto"}'>
	  <div @click="toDetail('newsDetail', newsList[0])" v-if="newsList.length>0" :style='{"padding":"10px","margin":"0 0 20px","flexWrap":"wrap","background":"linear-gradient(45deg, rgba(32,173,158,1) 0%, rgba(93,197,186,1) 15%, rgba(206,242,239,1) 50%, rgba(194,238,234,1) 75%, rgba(32,173,158,1) 100%),#20ad9e","display":"none","width":"100%","justifyContent":"space-between","height":"auto"}' class="list-item animation-box">
	    <div :style='{"width":"calc(100% - 210px)","padding":"10px","background":"#fff","height":"auto"}'>
	      <div :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#333","fontSize":"14px","lineHeight":"28px","textOverflow":"ellipsis","fontWeight":"600"}'>{{newsList[0].title}}</div>
	      <div :style='{"fontSize":"14px","lineHeight":"24px","overflow":"hidden","color":"#666","textIndent":"2em","height":"72px"}'>{{newsList[0].introduction}}</div>
	      <div :style='{"fontSize":"12px","lineHeight":"24px","color":"#999","textAlign":"right"}'>{{newsList[0].addtime.split(" ")[0]}}</div>
	    </div>
	    <img :style='{"width":"200px","objectFit":"cover","float":"left","height":"170px"}' :src="baseUrl + newsList[0].picture" >
	  </div>
	  <div @click="toDetail('newsDetail', newsList[1])" v-if="newsList.length>1" :style='{"padding":"10px","margin":"0 0 20px","flexWrap":"wrap","background":"linear-gradient(45deg, rgba(32,173,158,1) 0%, rgba(93,197,186,1) 15%, rgba(206,242,239,1) 50%, rgba(194,238,234,1) 75%, rgba(32,173,158,1) 100%),#20ad9e","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}' class="list-item animation-box">
	    <img :style='{"objectFit":"cover","width":"200px","height":"170px"}' :src="baseUrl + newsList[1].picture" >
	    <div :style='{"width":"calc(100% - 210px)","padding":"10px","background":"#fff","height":"auto"}'>
	      <div :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#333","fontSize":"14px","lineHeight":"28px","textOverflow":"ellipsis","fontWeight":"600"}'>{{newsList[1].title}}</div>
	      <div :style='{"fontSize":"14px","lineHeight":"24px","overflow":"hidden","color":"#666","textIndent":"2em","height":"72px"}'>{{newsList[1].introduction}}</div>
	      <div :style='{"fontSize":"12px","lineHeight":"24px","color":"#999","textAlign":"right"}'>{{newsList[1].addtime.split(" ")[0]}}</div>
	    </div>
	  </div>
	  <div @click="toDetail('newsDetail', newsList[2])" v-if="newsList.length>2" :style='{"width":"570px","padding":"10px","margin":"0 10px","background":"#f5f5f5","display":"none","height":"auto"}' class="list-item animation-box">
	    <div :style='{"width":"400px","padding":"10px","height":"auto"}'>
	      <div :style='{"color":"#333","fontSize":"14px","lineHeight":"28px"}'>{{newsList[2].title}}</div>
	      <div :style='{"color":"#666","fontSize":"14px","lineHeight":"24px"}'>{{newsList[2].introduction}}</div>
	      <div :style='{"color":"#999","fontSize":"12px","lineHeight":"24px"}'>{{newsList[2].addtime.split(" ")[0]}}</div>
	    </div>
	    <img :style='{"objectFit":"cover","width":"170px","height":"170px"}' :src="baseUrl + newsList[2].picture" >
	  </div>
	  <div @click="toDetail('newsDetail', newsList[3])" v-if="newsList.length>3" :style='{"padding":"10px","margin":"0 0 40px","flexWrap":"wrap","background":"linear-gradient(45deg, rgba(32,173,158,1) 0%, rgba(93,197,186,1) 15%, rgba(206,242,239,1) 50%, rgba(194,238,234,1) 75%, rgba(32,173,158,1) 100%),#20ad9e","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}' class="list-item animation-box">
	    <img :style='{"objectFit":"cover","width":"200px","height":"170px"}' :src="baseUrl + newsList[3].picture" >
	    <div :style='{"width":"calc(100% - 210px)","padding":"10px","background":"#fff","height":"auto"}'>
	      <div :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#333","fontSize":"14px","lineHeight":"28px","textOverflow":"ellipsis","fontWeight":"600"}'>{{newsList[3].title}}</div>
	      <div :style='{"fontSize":"14px","lineHeight":"24px","overflow":"hidden","color":"#666","textIndent":"2em","height":"72px"}'>{{newsList[3].introduction}}</div>
	      <div :style='{"fontSize":"12px","lineHeight":"24px","color":"#999","textAlign":"right"}'>{{newsList[3].addtime.split(" ")[0]}}</div>
	    </div>
	  </div>
	</div>
	
	
	
	<div @click="moreBtn('news')" :style='{"border":"0","padding":"0 12px 0 20px","margin":"0","top":"40px","textAlign":"center","background":"none","display":"inline-block","width":"auto","lineHeight":"40px","position":"absolute","right":"0","height":"40px"}'>
		<span :style='{"color":"#666","fontSize":"16px"}'>查看更多</span>
		<i v-if="true" :style='{"color":"#666","fontSize":"16px"}' class="el-icon-d-arrow-right"></i>
	</div>
	
</div>

</div>
</template>

<script>
  export default {
    //数据集合
    data() {
      return {
        baseUrl: '',
        queryList:[
          {
              queryName:"电影名称",
          },
        ],
        queryIndex: 0,
        dianyingxinxidianyingmingcheng: '',
        newsList: [],
        dianyingxinxiRecommend: [],

      }
    },
    created() {
      this.baseUrl = this.$config.baseUrl;
      this.getNewsList();
      this.getList();
    },
    //方法集合
    methods: {
      search(tablename) {
        if (this.queryIndex == 0 && this.dianyingxinxidianyingmingcheng) {
          this.$router.push({path: '/index/' + tablename, query: {indexQueryCondition: this.dianyingxinxidianyingmingcheng}});
        }
      },
		getNewsList() {
			this.$http.get('news/list', {params: {
				page: 1,
				limit: 2,
			order: 'desc'}}).then(res => {
				if (res.data.code == 0) {
					this.newsList = res.data.data.list;
					
					
				}
			});
		},
		getList() {
          let autoSortUrl = "";
          autoSortUrl = "dianyingxinxi/autoSort";
          if(localStorage.getItem('Token')) {
              autoSortUrl = "dianyingxinxi/autoSort2";
          }
			this.$http.get(autoSortUrl, {params: {
				page: 1,
				limit: 6,
			}}).then(res => {
				if (res.data.code == 0) {
					this.dianyingxinxiRecommend = res.data.data.list;
					
					
					// 商品列表样式五
					
				}
			});
			
		},
		toDetail(path, item) {
			this.$router.push({path: '/index/' + path, query: {detailObj: JSON.stringify(item)}});
		},
		moreBtn(path) {
			this.$router.push({path: '/index/' + path});
		}
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
	
		.recommend {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
        }
        
        .list5 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
		
		.news {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list6 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list6 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
	
		.lists {
			.list3 .swiper-button-prev {
				padding: 40px 20px;
				left: 40px;
				background: #fff;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: #20ad9e;
			}
			
			.list3 .swiper-button-next {
				padding: 40px 20px;
				left: auto;
				background: #fff;
				right: 40px;
        }
        
        .list3 .swiper-button-next::after {
				color: #20ad9e;
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-next {
            left: auto;
            right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform:  translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
	}
</style>
