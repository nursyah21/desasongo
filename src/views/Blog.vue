<script lang="ts">
import { Footer } from '../components'

export default{
    components: {
        Footer
    },
    data(){
      return{
        notfound: false,
        commentator: [],
        title: 'Yuk kenalan dengan desa songo',
        time:'02 september 2022',
        comment:{
          name:'',
          content:''
        }
      }
    },
    mounted() {
        var id: string = this.$route.params.id;
        document.title = `desa songo | ${id}`;
        this.getContent()
    },
    methods: {
      getContent():void{
        this.$refs.content.innerHTML = '<p>hello semua maya disini jadi anda semua baik baik saja kan</p><p>hehe sama kalo begitu yaudah yuk pergi makan bareng bersama aku<br></p>'
      },
      sendComment():void{
        console.log(this.comment.name, this.comment.message)
      }
    },
}
</script>

<template>
  <div class="text-gray-500">
    <!-- navbar -->
    <div class="bg-white border-b-2 pb-1 px-2 sm:px-8 pt-1 fixed top-0 w-screen left-0 bg-opacity-80 items-center">
      <a href="/" class="mx-2 text-xl hover:underline cursor-pointer">Home</a> <span class="text-lg">
        | Desa Songo
      </span>
    </div>

    <!-- notfound -->
    <div v-if="notfound" class="flex text-xl justify-center h-[80vh] items-center">
    Content Not Found
    </div>
    <!-- content -->
    <div v-else class="mt-12 mb-5 border-b py-2 mx-3">
      <div class="flex justify-center">
        <div>
          <!-- title -->
          <div class="text-3xl underline">{{title}}</div>
          <!-- time -->
          <div class="text-xs text-gray-400 mx-2">{{time}}</div>
        </div>
      </div>
      
      <!-- content -->
      <div ref="content" class="mt-6 mb-3 px-3"></div>

      <!-- comment -->
      <form @submit.prevent="sendComment" class="border-y px-3">
        <h1 class="text-lg mt-2">Comment</h1>
        <span class="text-sm text-gray-400 mx-1">name:</span><br>
        <input v-model="comment.name" type="text" class="outline-none border-b p-1 mb-2 w-3/4" title="write your name"><br>
        <span class="text-sm text-gray-400 mx-1">message:</span><br>
        <textarea class="w-full h-24 outline-none p-1 border-b mb-1" ></textarea>
        <input type="submit" value="submit" class="border p-1 px-3 rounded-lg hover:underline mb-2">
      </form>

      <!-- list comment -->
      <div class="p-3">
        <div v-if="commentator.length == 0">no comment</div>
        <div v-else>list of comment</div>
      </div>
    </div>

    <!-- footer -->
    <Footer></Footer>
  </div>
</template>