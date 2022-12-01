<script>
import { Footer, Loading, Navbar } from '../components'
import { supabase } from '../supabase'
import utils from "../utils"

export default {
  components: {
    Footer,
    Loading,
    Navbar,
  },
  data() {
    return {
      notfound: false,
      loading: false,
      loadingStatus: '',
      blogs: [],
      blog: {
        title: "",
        release: "",
        content: "",
      },
      commentator: [],
      title: '',
      time: '',
      comment: {
        name: '',
        content: '',
        fail: '',
        url_blog: ''
      },
      statsNav: 'blog'
    }
  },
  mounted() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0;
    this.$watch(
      () => this.$route.params,
      () => {
        this.getContent();
        utils.visited();
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0;
      }
    )
    this.getData();
    this.getContent()
    utils.visited()
    //change document title
    // this.a()
  },
  methods: {
    async getData() {
      this.loading = true;
      let { blog: blogs } = await utils.getDataIndex(0)
      blogs.forEach((data) => {
        this.blogs.push(data);
      })
      this.loading = false;
    },
    async getComment(blog_id) {
      this.commentator = [];
      this.loading = true
      const { data } = await supabase.from('comment').select().match({ url_blog: this.comment.url_blog })
      if (data == null) return this.loading = false
      if (data.length == 0 && !(this.loading = false)) return

      data.forEach(e => {
        this.commentator.push({ name: e.name, comment: e.comment, created_at: e.created_at })
      })

      this.loading = false
    },
    async getContent() {
      var id = this.$route.params.id;
      this.loading = true
      this.loadingStatus = 'load data'

      // check available link
      const { data } = await supabase.from('blog').select().match({ link: id }).single();
      this.loadingStatus = ''
      this.loading = false

      if (data == null) return this.notfound = true

      // generate data
      this.blog.title = data.title
      this.blog.release = data.release
      let element = data.data
      let new_element = document.createRange()
        .createContextualFragment(element);

      let img = new_element.querySelectorAll('img');
      img.forEach((e) => {
        e.setAttribute('class', `${e.getAttribute('class')} w-full rounded-lg mt-4`)
        e.removeAttribute('style')
      })

      let fr_img_wrap = new_element.querySelectorAll('.fr-img-wrap');
      fr_img_wrap.forEach((e) => {
        e.setAttribute('class', `${e.getAttribute('class')} block mb-4`)
      })

      let p = new_element.querySelectorAll('p');
      p.forEach(e => {
        e.setAttribute('class', `${e.getAttribute('class')} text-md`)
      })

      let span = new_element.querySelectorAll('span');
      span.forEach(e => {
        e.setAttribute('class', `${e.getAttribute('class')} text-md`)
        e.removeAttribute('style')
      })


      // this.blog.content = new_element
      this.$refs.content.innerHTML = "";
      this.$refs.content.appendChild(new_element);


      this.comment.url_blog = data.link
      window.document.title = data.title
      // generate comment
      await this.getComment(data.link)

      // update
      await utils.visited()
      const { error } = await supabase.from('blog').update({ views: data.views + 1 }).match({ link: id })
      if (error) console.log(error)


    },
    async sendComment() {
      let status = ""
      if (this.comment.name.trim() == '') status += "name, "
      if (this.comment.content.trim() == '') status += "message"
      if (status != '') return this.comment.fail = `${status} can't be empty`

      const datas = {
        name: this.comment.name,
        comment: this.comment.content,
        created_at: new Date().toDateString(),
        url_blog: this.comment.url_blog
      }

      this.loading = true
      const { error } = await supabase.from('comment').insert(datas)
      if (error && !(this.loading = false)) return this.comment.fail = "fail to send commment"
      window.location.reload()
    },
  },
}
</script>

<template>
  <navbar></navbar>
  <!-- body -->
  <div id="body" class="w-full lg:max-w-[1240px] md:max-w-[768px] px-[15px] mx-auto mt-32 mb-16">
    <div class="w-full lg:flex divide-x-0 lg:divide-x-[1px]">
      <div class="w-full lg:w-7/12 px-0 lg:pr-10">
        <h1 class="text-3xl font-semibold text-green-600">{{ blog.title }}</h1>
        <p class="mt-3 text-md font-semibold">{{ blog.release }}</p>
        <div ref="content" class="mt-5 mb-16"></div>
        <div class="mb-16 lg:mb-0">
          <form @submit.prevent="sendComment" class="border-2 px-3 shadow-md rounded-md">
            <h1 class="text-lg mt-2">Comment <span class="text-xs mx-2">{{ comment.fail }}</span></h1>
            <div class="flex items-center">
              <span class="text-sm text-gray-400 mx-1">name:</span><br>
              <input v-model="comment.name" type="text" class="outline-none border-b p-1 mb-2 w-3/4"
                title="write your name"><br>
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
                {{ i.name }} <span class="ml-2 text-xs">• {{ i.created_at }}</span>
                <p class="text-sm">{{ i.comment }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="w-full lg:w-5/12 lg:pl-10">
        <h1 class="title">Artikel Terbaru</h1>
        <router-link v-for="data in blogs" :to="{ name: 'blog_by_id', params: { id: data.link } }"
          class="no-underline text-black hover:no-underline cursor-pointer bg-white rounded-lg border shadow-lg w-full sm:h-[170px] flex flex-col-reverse sm:flex-row justify-between mb-6">
          <div class="sm:w-1/2 p-4 sm:p-5">
            <h1 class="font-semibold text-md sm:text-sm tracking-wide mb-3 line-clamp-2">{{ data.title }}
            </h1>
            <!-- <p class="tracking-wide text-sm mb-5 sm:mb-3 md:mb-5 line-clamp-3">{{ data.preview_data }}</p> -->
            <p class="text-gray-400 text-sm">{{ data.release }}</p>
          </div>
          <div
            class="sm:w-1/2 bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-t-lg sm:rounded-r-lg">
            <img v-if="data.img" class="w-full h-full object-cover object-center rounded-t-lg sm:rounded-r-lg"
              :src="data.img" alt="">
            <p v-else class="text-white text-lg font-bold tracking-wide">No Image</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
  <!-- footer -->
  <Footer></Footer>
</template>

<style>

</style>