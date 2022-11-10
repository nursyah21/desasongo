<script>
import { Footer, Loading, Nav } from '../components'
import { supabase } from '../supabase'
import utils from "../utils"

export default{
  components: {
    Footer,
    Loading,
    Nav
  },
  data(){
    return{
      notfound: false,
      loading: false,
      loadingStatus: '',
      commentator: [],
      title: '',
      time:'',
      comment:{
        name:'',
        content:'',
        fail:'',
        url_blog:''
      },
      statsNav: 'blog'
    }
  },
  mounted() {
      this.getContent()
      utils.visited()
      //change document title
      this.a()
  },
  methods: {
    async getComment(blog_id){
      this.loading = true
      const {data} = await supabase.from('comment').select().match({url_blog: this.comment.url_blog})
      console.log(data)
      if(data == null) return this.loading = false
      if(data.length == 0 && !(this.loading = false))return

      data.forEach(e=>{
        this.commentator.push({name:e.name, comment:e.comment, created_at: e.created_at})
      })

      this.loading = false
    },
    async getContent(){
      var id = this.$route.params.id;
      this.loading = true
      this.loadingStatus = 'load data'

      // check available link
      const {data} = await supabase.from('blog').select().match({link:id})
      this.loadingStatus = ''
      this.loading = false

      if(data == null) return this.notfound = true
      if(data.length == 0)return this.notfound = true


      // generate data
      this.comment.url_blog = data[0].link
      this.title = data[0].title
      this.time = data[0].release
      this.$refs.content.innerHTML = data[0].data

      // generate comment
      await this.getComment(data[0].link)

      // update
      await utils.visited()
      const {error} = await supabase.from('blog').update({views: data[0].views+1}).match({link:id})
      if(error)console.log(error)


    },
    async sendComment(){
      let status = ""
      if(this.comment.name.trim() == '') status += "name, "
      if(this.comment.content.trim() == '')status += "message"
      if(status != '') return this.comment.fail = `${status} can't be empty`
      
      const datas = {
        name: this.comment.name,
        comment: this.comment.content,
        created_at: new Date().toDateString(),
        url_blog: this.comment.url_blog 
      }
      
      this.loading = true
      const {error} = await supabase.from('comment').insert(datas)
      if(error && !(this.loading = false))return this.comment.fail = "fail to send commment"
      window.location.reload()
    },
    a(){ //i don't know how to name this function
      var a = window.location.href.split('/').pop().replaceAll('-',' ')
      window.document.title = `${a} | desa songo`
      switch(a){
        case 'tentang desa songo':
          this.statsNav = 'about'
          break
        case 'urban farming':
          this.statsNav = 'urbanFarming'
          break
        case 'tanaman':
          this.statsNav = 'tanaman'
          break
      }
    }
  },
}
</script>

<template>
  <Loading v-if="loading">{{loadingStatus}}</Loading>
  <div class="text-gray-500 m-0">
    <!-- navbar -->
    <Nav :stats="statsNav" />

    <!-- notfound -->
    <div v-if="notfound" class="flex text-xl justify-center h-[92vh] items-center">
    Content Not Found
    </div>
    <!-- content -->
    <div v-else class="mb-5 border-b py-2 mx-3">
      <div class="flex justify-center">
        <div class="text-center">
          <!-- title -->
          <div class="text-3xl underline">{{title}}</div>
          <!-- time -->
          <div class="text-xs text-gray-400">{{time}}</div>
        </div>
      </div>
      
      <!-- content -->
      <div ref="content" class="mt-6 mb-3 px-3 border-b-2"></div>

      <!-- comment -->
      <form @submit.prevent="sendComment" class="border-2 px-3 shadow-md rounded-md">
        <h1 class="text-lg mt-2">Comment <span class="text-xs mx-2">{{comment.fail}}</span></h1>
        <div class="flex items-center">
          <span class="text-sm text-gray-400 mx-1">name:</span><br>
          <input v-model="comment.name" type="text" class="outline-none border-b p-1 mb-2 w-3/4" title="write your name"><br>
        </div>
        <span class="text-sm text-gray-400 mx-1">message:</span><br>
        <textarea v-model="comment.content" class="w-full h-24 outline-none p-1 border-b mb-1"></textarea>
        <input type="submit" value="submit" class="border p-1 px-3 rounded-lg hover:underline mb-2">
        
      </form>

      <!-- list comment -->
      <div class="py-3">
        <div v-if="commentator.length == 0">no comment</div>
        <div v-else>
          <div v-for="i in commentator" class="border p-2 my-1 rounded-sm">
            {{i.name}} <span class="ml-2 text-xs">• {{i.created_at}}</span> 
            <p class="text-sm">{{i.comment}}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- footer -->
    <Footer></Footer>
  </div>
</template>

<style>
  
</style>