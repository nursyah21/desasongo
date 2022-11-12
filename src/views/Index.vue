<script>
import { Home, Navbar, Footer } from '../components';

export default {
  data() {
    return {
      dropdown: false
    };
  },
  mounted(){
    utils.visited()
  },
  methods: {
    readMore(id) {
      window.location.href = `${window.location.origin}/#${id}`;
    },
  },
  components: { Home, Navbar }
}
</script>

<template>
  <navbar></navbar>
  <!-- header -->
  <div class="h-screen w-full bg-[url('/banner.jpeg')] bg-cover">
    <div class="w-full h-full bg-[rgba(0,0,0,.4)]">
      <div class="flex w-full h-screen text-white">

        <!-- intro -->
        <div class="flex h-screen w-full justify-center items-center ">
          <div class="text-center w-full px-3 md:px-28 lg:px-40 xl:px-52">
            <h1 class="text-7xl font-bold mb-3">DESA <span class="text-green-400">SONGO</span></h1>
            <button @click="readMore('body')" class="btn-secondary font-semibold mt-5">Read more</button>
          </div>
        </div>
      </div>
    </div>
  </div>



  <!-- body -->
  <div id="body" class="w-full px-3 md:px-28">
    <!-- content -->
    <div class="px-3">
      <!-- tentang desa songo -->
      <div class="sm:grid grid-cols-2 p-6 mb-14">
        <div>
          <p class="text-xl">
            <span class="text-green-700">tentang</span><br>
            <p class="text-green-800 font-bold text-3xl">DESA SONGO</p>
          </p>
        </div>
        <p class="my-2 text-justify sm:pl-48 sm:pr-8">
          Desa Songo adalah sebutan lain dari Kampung Sayur Simo yang berlokasi di Simomulyo Baru, RT 09 RW 03,
          Kelurahan Simomulyo Baru, Kecamatan Sukomanunggal, Surabaya. Penduduk pada kampung ini berhasil mengubah
          suasana kumuh dan kini menjadi bersih dan hijau melalui program "Urban Farming" melalui teknik hidroponik,
          tanaman sayur dalam pot (tasapot), tanaman buah dalam pot (tabulampot).Dengan dilaksanakannya program
          tersebut, kampung ini kini mempunyai daya tarik bagi pengunjung-pengunjung dari luar desa untuk mengunjungi
          kampung ini.
        </p>
      </div>

      <!-- video profile -->
      <div class="my-4 sm:my-0 sm:pr-12 sm:py-12 md:flex">
        <iframe width="600" height="358" src="https://www.youtube.com/embed/9HylJhIM5b8"
          title="Kampung Sayur Simo - Surabaya" frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen class="w-full border sm:p-1 sm:shadow-md"></iframe>
        <p class="mt-2 md:pl-24 text-justify">
          Desa Songo atau Kampung Sayur Simo adalah kampung yang menerapkan program urban farming, ide ini berawal dari
          Bu Yaning yakni ketua RT Desa Songo yang mempunyai misi sangat mulia yaitu ingin menghijaukan kampung nya Misi
          ini diawali oleh Bu Yaning sejak tahun 2013 ... <br class="hidden sm:block"><a href="/blog/tentang-desa-songo"
            class="text-blue-500">readmore</a>
        </p>
      </div>

      <!-- virtual tour -->
      <div class="flex w-full justify-center border p-3 rounded-lg">
        <div class="text-center">
          <p class="text-lg text-green-800 font-bold">
            Keliling Desa Songo dengan Virtual Tour
          </p>
          Jelajahi kampung Simomulyo Baru dengan Virtual 3D Tour<br>
          <div class="mt-3">
            <a href="https://dkpp.surabaya.go.id/VirtualTourSimomulyoBaru/" class="btn-primary hover:no-underline">Lihat
              Sekarang</a>
          </div>
        </div>
      </div>

      <!-- gallery -->
      <div></div>

    </div>
  </div>

  <!-- footer -->
  <Footer />

</template>