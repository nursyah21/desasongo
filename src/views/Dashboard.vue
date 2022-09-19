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
        {page: 'Home', active:true},
        {page: 'Blog', active:false},
        {page: 'Shop', active:false},
        {page: 'Stats', active:false}
      ],
      hidroponik:{
        ultrasonik: [0.1, 0.1, 0.1], //read
        tds: 0.1, //read
        pompa: [false, true, true, true], //write
        mode: true, //write
        ppm: 0, //write 0-1500
        ppmvalid: true
      },
      stats:{
        blog: true,
        comment: false,
        shop: false
      },
      blog:{
        title:'',
        postfail:''
      },
      shop:{
        title:"",
        price:"",
        link:"",
        img:"",
        fail:"",
      }
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
          labels.push(e.time)
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
      if(this.blog.title == '') return this.blog.postfail = "title can't empty"
      if(document.querySelector('.fr-element.fr-view').innerHTML == "<p><br></p>") return this.blog.postfail = "content can't empty"

      this.loading = true
      const status = await utils.insertblog(this.blog.title)
      (status != '')?this.blog.postfail = true : this.move(3)
      
      this.loading = false
    },
    async refresh(){
      this.hidroponik.ppmvalid = true
      if(this.hidroponik.ppm < 0 || this.hidroponik.ppm > 1500)return this.hidroponik.ppmvalid = false
      
      this.loading = true
      await this.genCharts()
      this.loading = false
    },
    statsmove(e){
      Object.entries(this.stats).forEach(e=> this.stats[e[0]] = false)
      this.stats[e] = true
    },
    async uploadshop(){
      let status = ""
      if(this.shop.title.trim() == '') status = "title, "
      if(this.shop.price.trim() == '') status += "price, "
      if(this.shop.link.trim() == '' )status += "link, "
      if(this.$refs.imgshop.src == window.location) status += "image"
      if(status != '') return this.shop.fail = `${status} can't be empty`

      
      this.loading = true
      let {error} = await supabase.storage.from('public').upload(`${this.shop.img.name}`, this.shop.img)
      if(error && !(this.loading = false)) return this.shop.fail = 'upload image error,'
      
      console.log('test upload data')
      this.loading = true
      const result = await this.uploadDataShop()
      this.loading = false
      if(result != '') return this.shop.fail = 'upload data fail'
      this.move(3)
    },
    async uploadDataShop(){
      const datas = {
        name: this.shop.title,
        price: this.shop.price,
        img_url:`${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/${this.shop.img.name}}`,
        url: this.shop.link
      }
      
      const {error} = await supabase.from('shop').insert(datas)
      return (error)? error: ''
    },
    uploadimgshop(e){
      this.shop.img = e.target.files[0]
      this.$refs.imgshop.src = URL.createObjectURL(this.shop.img)
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
      <div id="chart" class="p-5 py-9 rounded-md shadow-md overflow-hidden"></div>

      <!-- hidroponik -->
      <div class="flex items-center">
        <h1 class="mt-2 mx-2">Hidroponik</h1> 
        <!-- refresh button -->
        <button @click="refresh" class="mt-2 mx-2 border px-3 hover:underline ">refresh</button>
        
      </div>
      <div class="text-center text-red-600 text-xs" v-if="!hidroponik.ppmvalid">
        ppm must be in range 0-1500
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 select-none">
        <!-- ultrasonik -->
        <div v-for="i,idx in hidroponik.ultrasonik" class="rounded-md p-2 m-2 w-36 sm:w-48 text-center bg-blue-500 text-white cursor-default">
          <span class="underline">ultrasonik {{idx + 1}}</span><br>
          {{i}}
        </div>
        <!-- tds -->
        <div class="border p-2 m-2 w-36 sm:w-48 text-center bg-blue-600 text-white cursor-default">
          <span class="underline">tds</span><br>
          {{hidroponik.tds}}
        </div>
        <!-- pompa w -->
        <div @click="hidroponik.pompa[idx] = !hidroponik.pompa[idx]" v-for="i,idx in hidroponik.pompa" class="rounded-md p-2 m-2 w-36 sm:w-48 text-center bg-lime-600 text-white hover:opacity-60 cursor-pointer">
          <span class="underline">pompa {{idx + 1}}</span><br>
          {{(i)?'aktif':'non aktif'}}
        </div>
        <!-- mode w -->
        <div @click="hidroponik.mode = !hidroponik.mode" class="rounded-md p-2 m-2 w-36 sm:w-48 text-center bg-lime-600 text-white hover:opacity-60 cursor-pointer">
          <span class="underline">mode</span><br>
          {{(hidroponik.mode)?'aktif':'non aktif'}}
        </div>
        <!-- ppm w -->
        <div class="rounded-md p-2 m-2 w-36 sm:w-48 text-center bg-lime-600 text-white cursor-pointer">
          <span class="underline">ppm (0-1500)</span><br>
          <input type="number" v-model="hidroponik.ppm"  class="bg-lime-600 text-center outline-none border w-24" min="0" max="1500">
        </div>

      </div>

      <!-- domain button -->
      <div class="flex text-center mt-5 border-t">
        <a href="https://www.niagahoster.co.id/" class="mt-2 border text-gray-500 w-full mx-2 p-1 hover:underline">domain</a>
      </div>

      <!-- logout -->
      <div class="mx-2 my-2">
        <button @click="logout" class="bg-red-700 text-white w-full p-1 hover:underline">log out</button>
      </div>
    </div>
    
    <!-- blog -->
    <div class="m-2">
      
      <form @submit.prevent="submitContent" class="rounded-md shadow-md w-full p-3" :class="{hidden: !nav[1].active}">
        <div v-if="blog.postfail" class="italic text-center text-xs text-red-700">{{blog.postfail}}</div>
        
        <!-- blog editor -->
        <div >
        <!-- title -->
        <span class="text-sm text-gray-400 mx-1">title:</span>
        <input v-model="blog.title" type="text" placeholder="title" class="border px-2 outline-none py-1 w-full mb-2" >
        
        <!-- content -->
        <span class="text-sm text-gray-400 mx-1">content:</span>
        <div ref="blogcontent">
          <textarea></textarea>
        </div>
        
        <!-- submit -->
        <input type="submit" class="bg-green-400 text-white w-full p-1 my-2 hover:underline" value="submit">
        </div>

      </form>
    </div>

    <!-- shop -->
    <div v-if="nav[2].active" class="p-3">
      <div v-if="shop.fail" class="text-center text-xs italic">{{shop.fail}}</div>
      <img src="" alt="" ref="imgshop" id="imgshop">
      <form @submit.prevent="uploadshop" class="p-3 shadow-md rounded-md">
        <!-- title -->
        <span class="text-sm">title</span><br>
        <input v-model="shop.title" type="text" class="border w-full outline-none px-2 p-1">
        <!-- price -->
        <span class="text-sm">price</span><br>
        <input v-model="shop.price" type="text" class="border w-full outline-none px-2 p-1">
        <!-- image -->
        <div class="overflow-hidden">
          <span class="text-sm">upload image</span><br>
          <input @change="uploadimgshop" ref="imgfileshop" type="file" accept="image/*" class="border w-full outline-none px-2 p-1">
        </div>
        <!-- link -->
        <span class="text-sm">link online shop</span><br>
        <input v-model="shop.link" type="text" class="border w-full outline-none px-2 p-1">
        <!-- submit -->
        <input type="submit" value="submit" class="w-full outline-none bg-green-400 text-white p-1 my-2 hover:underline">
      </form>
    </div>

    <!-- stats -->
    <div v-if="nav[3].active" class="px-3 py-1">
      <div class="flex">
        <!-- blog -->
        <button @click="statsmove('blog')" :class="{underline: stats.blog}" class="w-full bg-green-400 text-white p-1 hover:underline">blog</button>
        <!-- comment -->
        <button @click="statsmove('comment')" :class="{underline: stats.comment}" class="w-full bg-blue-400 text-white p-1 hover:underline">comment</button>
        <!-- shop -->
        <button @click="statsmove('shop')" :class="{underline: stats.shop}" class="w-full bg-amber-400 text-white p-1 hover:underline">shop</button>
      </div>

      <div class="overflow-x-scroll my-4 py-1">
        <!-- blog -->
        <table class="w-full" v-if="stats.blog">
            <tr>
              <th class="sm:w-10">id</th>              
              <th>title</th>
              <th>release</th>
              <th>views</th>
            </tr>
            <tbody v-for="i in 10">
              <tr class="text-sm hover:bg-slate-200">
                <td class="text-center">{{i}}</td>
                <td>1201202040</td>
                <td>{{i}}</td>
                <td>{{i}}</td>
              </tr>
            </tbody>
        </table>
        <!-- comment -->
        <table class="w-full" v-if="stats.comment">
            <tr>
              <th class="sm:w-10">id</th>              
              <th>name</th>
              <th>message</th>
              <th>created_at</th>
              <th>blog</th>
            </tr>
            <tbody v-for="i in 10">
              <tr class="text-sm hover:bg-slate-200">
                <td class="text-center">{{i}}</td>
                <td>who</td>
                <td>1201202040</td>
                <td>{{i}}</td>
                <td>{{i}}</td>
              </tr>
            </tbody>
        </table>
        <!-- shop -->
        <table class="w-full" v-if="stats.shop">
            <tr>
              <th class="sm:w-10">id</th>              
              <th>product</th>
              <th>price</th>
              <th>link shop</th>
              <th>image</th>
            </tr>
            <tbody v-for="i in 10">
              <tr class="text-sm hover:bg-slate-200">
                <td class="text-center">{{i}}</td>
                <td>1201202040</td>
                <td>{{i}}</td>
                <td>{{i}}</td>
                <td>{{i}}</td>
              </tr>
            </tbody>
        </table>
      </div>

    </div>
    
    <!-- footer -->
    <Footer></Footer>
  </div>
</template>