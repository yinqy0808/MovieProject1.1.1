const base = {
    get() {
        return {
            url : "http://127.0.0.1:8080/MovieProject/",
            name: "MovieProject",
            // 退出到首页链接
            indexUrl: 'http://127.0.0.1:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Python的电影票购票系统"
        } 
    }
}
export default base
