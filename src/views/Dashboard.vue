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
        {page: 'Statistics', active:false}
      ],
      hidroponik:{
        ultrasonik: [0.1, 0.1, 0.1], //read
        tds: 0.1, //read
        pompa: [false, true, true, true], //write
        mode: true, //write
        ppm: 0, //write 0-1500
      },
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
      this.loading = true
      const oldimg = []
      try{
        var img = content.querySelectorAll('img')
        img.forEach(e=>{
          e = e.src
          var s = e.split('/')
          s = `${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/${s[s.length-1]}.jpg`
          oldimg.push({old:e, new:s})
        })
      //   var up = await fetch(img).then(r=>r.blob())

      //   const {error} = await supabase.storage.from('public').upload(`${s}.jpg`, up)

      //   if(!error) console.log('success')
      //   else console.log(error)

      }catch(e){}
      var submitcontent = content.innerHTML

      oldimg.forEach(e=>{
        submitcontent = submitcontent.replace(e.old, e.new)
      })

      console.log('test', submitcontent)
      

      this.loading = false
    },
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

      <!-- hidroponik -->
      <h1 class="mt-2 mx-2">Hidroponik</h1>
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 select-none">
        <!-- ultrasonik -->
        <div v-for="i,idx in hidroponik.ultrasonik" class="border p-2 m-2 w-36 sm:w-48 text-center bg-blue-500 text-white cursor-default">
          <span class="underline">ultrasonik {{idx + 1}}</span><br>
          {{i}}
        </div>
        <!-- tds -->
        <div class="border p-2 m-2 w-36 sm:w-48 text-center bg-blue-600 text-white cursor-default">
          <span class="underline">tds</span><br>
          {{hidroponik.tds}}
        </div>
        <!-- pompa w -->
        <div @click="hidroponik.pompa[idx] = !hidroponik.pompa[idx]" v-for="i,idx in hidroponik.pompa" class="border p-2 m-2 w-36 sm:w-48 text-center bg-lime-600 text-white hover:opacity-60 cursor-pointer">
          <span class="underline">pompa {{idx + 1}}</span><br>
          {{(i)?'aktif':'non aktif'}}
        </div>
        <!-- mode w -->
        <div @click="hidroponik.mode = !hidroponik.mode" class="border p-2 m-2 w-36 sm:w-48 text-center bg-lime-600 text-white hover:opacity-60 cursor-pointer">
          <span class="underline">mode</span><br>
          {{(hidroponik.mode)?'aktif':'non aktif'}}
        </div>
        <!-- ppm w -->
        <div class="border p-2 m-2 w-36 sm:w-48 text-center bg-lime-600 text-white cursor-pointer">
          
            <span class="underline">ppm (0-1500)</span><br>
            <input type="number" v-model="hidroponik.ppm"  class="bg-lime-600 text-center outline-none border w-24" min="0" max="1500">
          
        </div>
      </div>
    </div>
    
    <!-- blog -->
    <div class="m-2">
      <div class="border w-full p-3" :class="{hidden: !nav[1].active}">
        <!-- blog editor -->
        <div >
          <!-- title -->
        <span class="text-sm text-gray-400 mx-1">title:</span>
        <input type="text" placeholder="title" class="border px-2 outline-none py-1 w-full mb-2" >
        
        <!-- content -->
        <span class="text-sm text-gray-400 mx-1">content:</span>
        <!-- <textarea></textarea> -->
        <textarea></textarea>

  
        <!-- submit -->
        <input @click="submitContent" type="submit" class="bg-green-400 text-white w-full p-1 my-2 hover:underline" value="submit">
        </div>

      </div>
    </div>

    <!-- shop -->

    <!-- statics -->
    
    <!-- logout -->
    <div class="mx-2 my-2">
      <button @click="logout" class="bg-red-700 text-white w-full p-1 hover:underline">log out</button>
    </div>
    <!-- footer -->
    <Footer></Footer>
  </div>
</template>