<script>
import { Modal, Loading, Footer } from '../components';
import utils from '../utils';
import router from '../router';
import { supabase } from '../supabase';

export default{
  components:{
    Modal,Loading,Footer
},
  mounted(){
    this.autologin()
  },
  data(){
    return{
      login: false,
      loading:false,
      nav:[
        {page: 'Dashboard', active:true},
        {page: 'Blog', active:false},
        {page: 'Shop', active:false},
        {page: 'Komentar', active:false},
        {page: 'Hidroponik', active:false}
      ]
    }
  },
  methods:{
    async autologin(){
      const savedname = localStorage.getItem('name')
      const savedpass = localStorage.getItem('pass')

      if(savedname != null && savedpass != null){
        this.loading = true
        const data = await utils.login(savedname, savedpass)
        this.loading = false

        if(data === ""){
          this.login = true
          this.genCharts()
        }else{
          localStorage.clear()
          window.location.href = "/login"
        }
      }
      else
        router.push('login')
    },
    async genCharts(){
      const data = {labels: [],datasets: [{name: "Website", chartType: "line",values: []
      }]}      

      new frappe.Chart("#chart", {
        title: `${new Date().getFullYear()} ${['December', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'][new Date().getMonth()]}`,
        data: data,
        height: 250,
        colors: ['#7cd6fd']
      })

      try{
        const {data,error} = await supabase.from('visited').select()
        const labels = [], datasets = []
        if(error)return
        data.forEach(e=>{
          labels.push(e.visited_id)
          datasets.push(e.counts)
        })

        new frappe.Chart("#chart",{
          title: `${new Date().getFullYear()} ${['December', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'][new Date().getMonth()]}`,
          data: {labels: labels, datasets: [{name: "Website", chartType: "line",values: datasets}]},
          height: 250,
          colors: ['#7cd6fd']
        })
        
      }catch(e){}


    },
    move(e){
      this.nav.forEach(e=>e.active = false)
      this.nav[e].active = true

      if(this.nav[1].active)new FroalaEditor('textarea');
      
    },
    logout(){
      localStorage.clear()
      window.location.reload()
    },
    async submitContent(){
      var content = document.querySelector('.fr-element.fr-view')
      try{
        var img = content.querySelector('img').src
        var s = img.split('/')
        s = s[s.length-1]
        var up = await fetch(img).then(r=>r.blob())

        const {error} = await supabase.storage.from('public').upload(`${s}.jpg`, up)
        
        if(!error) console.log('success')
        else console.log(error)

      }catch(e){}

      //console.log(content.innerHTML)
      // console.log(this.$refs.content.innerHTML)
    }
  }
}

</script>

<template>
  <Loading :class="{hidden: !loading}"></Loading>

  <div :class="{hidden: !login}" class="text-gray-500">
    <!-- navbar -->
    <div class="w-full p-2 border-b mb-2 flex items-center ">
      <a href="/">
        <img src="../assets/logo1.svg" alt="" class="w-10 rounded-xl mr-4">
      </a>
      
      <div class="flex overflow-x-scroll pb-2 sm:overflow-hidden">
        <div @click="move(idx)" :class="{underline: nav[idx].active}" class="mx-2 cursor-pointer hover:opacity-30" v-for="i,idx in nav">{{i.page}}</div>  
      </div>
      
    </div>

    <!-- dashboard -->
    <div :class="{hidden: !nav[0].active}" class="p-3">
      <!-- chart --> 
      <div id="chart" class="p-5 py-9 border shadow-md overflow-hidden"></div>
      
    </div>
    
    <!-- blog -->

    <div class="m-2">
      <div class="border w-full p-3" :class="{hidden: !nav[1].active}">
        <!-- title -->
        <span class="text-sm text-gray-400 mx-1">title:</span>
        <input type="text" placeholder="title" class="border px-2 outline-none py-1 w-full mb-2" >
        
        <!-- content -->
        <span class="text-sm text-gray-400 mx-1">content:</span>
        <textarea></textarea>
        <!-- <textarea ref="content" class="border w-full outline-none p-2"></textarea> -->
  
        <!-- submit -->
        <input @click="submitContent" type="submit" class="bg-green-400 text-white w-full p-1 my-2 hover:underline" value="submit">
      </div>
    </div>
    
    <div class="mx-2 my-2">
      <button @click="logout" class="bg-red-700 text-white w-full p-1 hover:underline">log out</button>
    </div>
    <!-- footer -->
    <Footer></Footer>
  </div>
</template>