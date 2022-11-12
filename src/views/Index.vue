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
  <navbar :transparent_background="true"></navbar>
  <!-- header -->
  <div class="h-screen w-full bg-[url('/banner.jpeg')] bg-cover">
    <div class="w-full h-full bg-[rgba(0,0,0,.4)]">
      <div class="flex w-full h-screen text-white">

        <!-- intro -->
        <div class="flex h-screen w-full justify-center items-center ">
          <div class="text-center">
            <h1 class="text-7xl font-bold mb-3">DESA <span class="text-green-400">SONGO</span></h1>
            <button @click="readMore('body')" class="btn-secondary font-semibold mt-5">Read more</button>
          </div>
        </div>
      </div>
    </div>
  </div>



  <!-- body -->
  <div id="body" class="w-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto pt-16">
    <div class="grid md:grid-cols-2 gap-x-10">
      <div>
        <h1 class="title"><span class="text-green-500">Video</span> <span class="text-green-500 font-normal">Profile</span></h1>
        <iframe width="600" height="358" src="https://www.youtube.com/embed/9HylJhIM5b8"
          title="Kampung Sayur Simo - Surabaya" frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen class="w-full rounded-lg"></iframe>
      </div>
      <div class="mt-16 md:mt-0">
        <h1 class="title"><span class="text-green-500">Profile</span> <span class="text-green-500 font-normal">Desa Songo</span></h1>
        <div class="w-full flex overflow-x-scroll gap-x-5 pb-1 mb-3">
          <img src="img3.png" class="rounded-lg w-1/2" />
          <img src="img4.png" class="rounded-lg w-1/2" />
          <img src="img5.jpg" class="rounded-lg w-1/2" />
        </div>
        <p class="md:text-justify text-sm">
          <span class="text-green-500">Desa Songo</span> adalah sebutan lain dari <span class="text-green-500">Kampung
            Sayur Simo</span> yang berlokasi di Simomulyo Baru, RT 09 RW 03,
          Kelurahan Simomulyo Baru, Kecamatan Sukomanunggal, Surabaya.<br/><br/> Penduduk pada kampung ini berhasil mengubah
          suasana kumuh dan kini menjadi bersih dan hijau melalui program <span class="text-green-500">"Urban Farming"</span> melalui teknik hidroponik,
          tanaman sayur dalam pot (<span class="text-green-500">tasapot</span>), tanaman buah dalam pot (<span class="text-green-500">tabulampot</span>).
        </p>
      </div>
    </div>
  </div>
  <!-- virtual tour -->
  <div class="bg-[url('./virtual-tour.jpg')] bg-cover bg-center w-full h-[500px] mt-16">
    <div class="flex items-center justify-center h-full backdrop-brightness-50">
      <div class="flex-column text-center px-[15px]">
        <p class="text-lg text-green-400 font-bold">
          Keliling Desa Songo dengan Virtual Tour
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