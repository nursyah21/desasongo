<script>
import { Home, Navbar, Footer } from '../components';
import utils from '../utils';

export default {
  data() {
    return {
      dropdown: false
    };
  },
  mounted() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0;
    utils.visited()
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
  <navbar :transparent_background="true"></navbar>
  <!-- header -->
  <div class="h-screen w-full bg-[url('/banner.jpeg')] bg-cover">
    <div class="w-full h-full bg-[rgba(0,0,0,.4)]">
      <div class="flex w-full h-screen text-white">

        <!-- intro -->
        <div class="flex h-screen w-full justify-center items-center ">
          <div class="text-center">
            <h1 class="text-5xl sm:text-7xl font-bold mb-3">KAMPUNG <span class="text-green-400">SONGO</span></h1>
            <button @click="readMore('body')" class="btn-secondary font-semibold mt-5">Read more</button>
          </div>
        </div>
      </div>
    </div>
  </div>



  <!-- body -->
  <div id="body" class="w-full lg:max-w-[1240px] md:max-w-[768px] px-[15px] mx-auto pt-16">
    <div class="grid md:grid-cols-2 gap-x-10">
      <div>
        <h1 class="title"><span class="text-green-500">Video</span> <span
            class="text-green-500 font-normal">Profile</span></h1>
        <iframe width="600" height="358" src="https://www.youtube.com/embed/9HylJhIM5b8"
          title="Kampung Sayur Simo - Surabaya" frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen class="w-full rounded-lg"></iframe>
      </div>
      <div class="mt-16 md:mt-0">
        <h1 class="title"><span class="text-green-500">Profile</span> <span class="text-green-500 font-normal">Kampung
            Songo</span></h1>
        <div class="w-full flex overflow-x-scroll gap-x-5 pb-1 mb-3">
          <img src="/img3.png" class="rounded-lg w-1/2" />
          <img src="/img4.png" class="rounded-lg w-1/2" />
          <img src="/img5.jpg" class="rounded-lg w-1/2" />
        </div>
        <p class="md:text-justify text-sm">
          <span class="text-green-500">Kampung Songo</span> adalah sebutan lain dari <span
            class="text-green-500">Kampung
            Sayur Simo</span> yang berlokasi di Simomulyo Baru, RT 09 RW 03,
          Kelurahan Simomulyo Baru, Kecamatan Sukomanunggal, Surabaya.<br /><br /> Penduduk pada kampung ini berhasil
          mengubah
          suasana kumuh dan kini menjadi bersih dan hijau melalui program <span class="text-green-500">"Urban
            Farming"</span> melalui teknik hidroponik,
          tanaman sayur dalam pot (<span class="text-green-500">tasapot</span>), tanaman buah dalam pot (<span
            class="text-green-500">tabulampot</span>).
        </p>
      </div>
    </div>
  </div>
  <section class="overflow-hidden text-gray-700">
    <div class="w-full lg:max-w-[1240px] md:max-w-[768px] px-[15px] mx-auto pt-16">
      <h1 class="title"><span class="text-green-500">Gallery</span> <span class="text-green-500 font-normal">Kampung
          Songo</span></h1>
      <div class="flex flex-wrap -m-1 md:-m-2">
        <div class="flex flex-wrap w-1/2">
          <div class="w-1/2 p-1 md:p-2">
            <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg" src="/penghargaan2.jpg">
          </div>
          <div class="w-1/2 p-1 md:p-2">
            <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg" src="/penghargaan4.jpg">
          </div>
          <div class="w-full p-1 md:p-2">
            <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg" src="/gallery_ss2.webp">
          </div>
        </div>
        <div class="flex flex-wrap w-1/2">
          <div class="w-full p-1 md:p-2">
            <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg" src="/img8.webp">
          </div>
          <div class="w-1/2 p-1 md:p-2">
            <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg" src="/gallery3.jpg">
          </div>
          <div class="w-1/2 p-1 md:p-2">
            <img alt="gallery" class="block object-cover object-center w-full h-full rounded-lg" src="/gallery4.jpg">
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- virtual tour -->
  <div class="bg-[url('/virtual-tour.jpg')] bg-cover bg-center w-full h-[500px] mt-16">
    <div class="flex items-center justify-center h-full backdrop-brightness-50">
      <div class="flex-column text-center px-[15px]">
        <p class="text-lg text-green-400 font-bold">
          Keliling Kampung Songo dengan Virtual Tour
        </p>
        <p class="text-white">Jelajahi kampung Simomulyo Baru dengan Virtual 3D Tour</p>
        <div class="mt-3">
          <button @click="openNewTab('https://dkpp.surabaya.go.id/VirtualTourSimomulyoBaru/')" class="btn-primary">Lihat
            Sekarang</button>
        </div>
      </div>
    </div>
  </div>
  <!-- footer -->
  <Footer></Footer>
</template>