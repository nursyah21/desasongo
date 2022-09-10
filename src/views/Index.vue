<script>
import {Modal,Home,Blog,Shop,Footer} from '../components'
export default{
  components:{
    Modal,
    Home,
    Blog,
    Shop,
    Footer
},
  data(){
    return{
      navbar:[
        {page:'home', active:true},
        {page:'blog', active:false},
        {page:'shop', active:false}
      ]
    }
  },
  methods:{
    move(e){
      this.navbar.forEach(e=>e.active = false)
      this.navbar[e].active = true
    }
  }
}
</script>

<template>
  <div class="text-gray-500 p-3">
    <!-- navbar -->
    <div class="bg-white border-b-2 pb-1 px-2 sm:px-8 pt-1 fixed top-0 w-screen left-0 bg-opacity-80">
      <button @click="move(idx)" :class="{underline: navbar[idx].active}" v-for="i,idx in navbar" class="mx-2 text-xl hover:underline">{{i.page}}</button>
    </div>
    <!-- banner -->
    <div class="flex justify-center">
      <img src="../assets/banner.svg" alt="" class="mt-8 w-full">
    </div>

    <div class="sm:px-4">
      <Home :class="{hidden: !navbar[0]['active']}" />
      <Blog :class="{hidden: !navbar[1]['active']}" />
      <Shop :class="{hidden: !navbar[2]['active']}" />
    </div>

    <Footer />
  </div>
</template>