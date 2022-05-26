
new Vue({
    
    el: '#get',
    data: {
        news: []
    },
    created: function () {
        const vm = this;
        axios.get('/news/')
        .then(function (response) {
            console.log(response.data),
            vm.news = response.data}
        )
    }
})