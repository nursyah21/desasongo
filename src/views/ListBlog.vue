<template>
  <navbar></navbar>
  <div class="w-full h-[400px] bg-[url('img7.webp')] bg-cover bg-center mt-16">
    <div class="w-full h-full bg-[rgba(0,0,0,.6)]">
      <div class="w-full h-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto flex items-center">
        <span class="text-white text-4xl font-extrabold leading-[43px]">Semua Berita,<br>
          Cerita, Suara,<br>
          dan wawasan dari<br>
          Desa <span class="text-green-500">Songo</span></span>
      </div>
    </div>
  </div>
  <div class="w-full h-[450px] bg-gray-100 hidden sm:block">
    <div class="w-full h-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto py-16">
      <div class="bg-white rounded-lg border shadow-lg w-full h-full flex justify-between mb-6">
        <div class="w-1/2 p-10">
          <h1 class="font-semibold text-xl tracking-wide sm:mb-4">Bisnis Katering Versus Jegalan Pandemi</h1>
          <p class="tracking-wide text-sm sm:mb-10">Seakan ingin melahap semua hal, pandemi Covid-19 juga menyambangi
            para pelaku bisnis katering. Dilansir...</p>
          <p class="text-gray-400">10 November 2022</p>
        </div>
        <div class="w-1/2">
          <img class="w-full h-full object-cover object-center rounded-r-lg" src="sayuran.jpg" alt="">
        </div>
      </div>
      <div class="flex justify-center gap-x-4">
        <div class="dot-custom active"></div>
        <div class="dot-custom"></div>
        <div class="dot-custom"></div>
        <div class="dot-custom"></div>
        <div class="dot-custom"></div>
      </div>
    </div>
  </div>
  <!-- body -->
  <div id="body" class="w-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto mt-16 mb-16">
    <h1 class="title">Semua Artikel</h1>
    <a v-for="data in blogs"
      class="no-underline text-black hover:no-underline transition-transform duration-300 cursor-pointer bg-white rounded-lg border shadow-lg w-full sm:h-[240px] hover:scale-105 flex flex-col-reverse sm:flex-row justify-between mb-6">
      <div class="sm:w-1/2 p-10">
        <h1 class="font-semibold text-xl sm:text-lg md:text-xl tracking-wide mb-3 line-clamp-2">{{ data.title }}</h1>
        <p class="tracking-wide text-sm mb-5 sm:mb-3 md:mb-5 line-clamp-3">{{ data.preview_data }}</p>
        <p class="text-gray-400 sm:text-sm md:text-base">{{ data.release }}</p>
      </div>
      <div class="sm:w-1/2 bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-r-lg">
        <img v-if="data.img" class="w-full h-full object-cover object-center rounded-r-lg" :src="data.img" alt="">
        <p v-else class="text-white text-lg font-bold tracking-wide">No Image</p>
      </div>
    </a>
    <button v-if="!loading" @click="getData()"
      class="border-green-500 border rounded-md p-3 text-green-500 text-sm block m-auto hover:scale-105 transition-transform transition-transform duration-300">Muat
      lebih banyak</button>
    <div v-if="loading" class="flex justify-center items-center">
      <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
        <!-- <span class="visually-hidden">Loading...</span> -->
      </div>
    </div>
  </div>
  <!-- footer -->
  <Footer></Footer>
</template>
<script>
import { Home, Navbar, Footer } from '../components';
import utils from '../utils';
export default {
  data() {
    return {
      loading: false,
      blogs: [],
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      this.loading = true;
      utils.getDataIndex(this.blogs.length).then(response => {
        let blogs = response.blog;
        blogs.forEach((data) => {
          this.blogs.push(data);
        })
        this.loading = false;
      })
    },
    readMore(id) {
      window.location.href = `${window.location.origin}/#${id}`;
    },
    openNewTab(link) {
      window.open(link);
    }
  },
  components: { Home, Navbar, Footer }
}
</script>