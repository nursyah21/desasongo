<script>
import {Modal,Home,Footer} from '../components'
import utils from "../utils"
import { supabase } from '../supabase'

export default{
  components:{
    Modal,
    Home,
    Footer
  },
  mounted(){
    utils.visited()
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
      <!-- Home -->
      <Home :class="{hidden: !navbar[0]['active']}" />
      
      <!-- Blog -->
      <div class="border-b my-2" :class="{hidden: !navbar[1]['active']}">
        <div class="border p-3 rounded-md my-2">
          <p class="mb-1 sm:text-xl">mengenal desa songo</p>
          <p class="text-sm sm:text-base mb-1">
            Kampung ini dulunya agak kumuh dan kurang hijau, hingga tahun 2013 Bu Yaning terpilih sebagai ketua KT. Mengapa Bu Yaning mau menjadi RT karena Bu Yaning mempunyai misi yaitu bagaimana cara mengubah kampung ini menjadi bersih dan hijau... <a href="/blog/tentang-desa-songo" class="text-blue-500">readmore</a>
          </p>
          <p class="text-xs">20 december 2022</p>
        </div>
      </div>

      <!-- Shop -->
      <div class="my-2 border-b" :class="{hidden: !navbar[2]['active']}" >
        <div class="p-3 border shadow rounded-lg flex my-2">
          <img src="../assets/sayur.webp" alt="" class="w-24 sm:w-48">
          <div class="text-sm sm:text-base ml-4">
            <p>BAYAM HIJAU SAYUR [1 Ikat] FRESH</p>
            <p>Rp. 1000</p>
            <div class="h-2"></div>
            <a class=" bg-green-400 px-6 rounded-lg py-1 text-white" href="https://www.tokopedia.com/sayursegardepok/bayam-hijau-sayur-1-ikat-fresh?extParam=ivf%3Dfalse&src=topads">Beli</a>
          </div>
        </div>
      </div>

    </div>

    <Footer />
  </div>
</template>