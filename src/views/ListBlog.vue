<script>
import { Footer, Nav,Loading } from '../components';
import utils from '../utils';

export default{
  mounted(){
    window.document.title = `list blog | desa songo`
    utils.visited()
    this.getData()
  },
  data(){
    return{
      loading: false,
      blog:[],
      blogIdx:0,
      lengthIdx:3,
    }
  },
  methods:{
    async getData(){
      this.loading = true
      const {blog} = await utils.getDataIndex()
      this.loading = false
      this.blog = blog
    },
  },
  components:{
    Nav, Footer, Loading
  }
}
</script>

<template>
  <Loading v-if="loading">load data</Loading>
  <Nav stats="blog" />

  <!-- Blog -->
  <div class="my-2  border-b p-3" >  
    <div class="shadow-lg p-3 rounded-md my-2" v-for="i in blog.slice(blogIdx, blogIdx+lengthIdx+1)">
      <p class="mb-1 sm:text-xl">{{i.title}}</p>
      <p class="text-xs sm:text-sm mb-1">{{i.preview_data}} <a :href="'/blog/'+i.link" class="text-blue-500">readmore</a></p>          
      <p class="text-xs">{{i.release}}</p>
    </div>

    <!-- pagination -->
    <div class="text-center">
      <button  class="border px-2 mx-2 mb-2 hover:underline" :class="{underline: (blogIdx == i-1 )}" @click="blogIdx = i - 1" v-for="i in Number((blog.length / lengthIdx).toFixed())">{{i}}</button>
    </div>
  </div>


  <Footer />
</template>