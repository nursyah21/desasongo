<script>
import { Home, Navbar, Footer } from '../components';

export default {
  data() {
    return {

    };
  },
  methods: {
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
  <div class="w-full h-[450px] bg-gray-100">
    <div class="w-full h-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto py-16">
      <div class="bg-white rounded-lg border shadow-lg w-full h-full grid grid-">
        
      </div>
    </div>
  </div>
  <!-- body -->
  <div id="body" class="w-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto mt-32 mb-16">
  </div>
  <!-- footer -->
  <Footer></Footer>
</template>