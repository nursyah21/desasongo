<script>
import { Footer, Nav } from '../components';

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
    dropdownFunc() {
      // alert('ah')
      this.dropdown = !this.dropdown
      if (this.dropdown) window.location.href = `${window.location.origin}/#body`;
    }
  },
  components: { Footer, Nav }
}
</script>

<template>
  <!-- header -->
  <div class="h-screen w-screen">
    <div class="absolute top-0 bg-black h-full w-full opacity-70 z-10"> </div>
    <div class="absolute w-full h-full bg-cover bg-[url('/banner.jpeg')] z-0"></div>
    <div class="absolute z-20">
      <div class="flex w-screen h-screen text-white">

        <!-- intro -->
        <div class="flex h-screen w-screen justify-center items-center ">
          <div class="text-center">
            <h1 class="text-7xl font-bold">DESA SONGO</h1>
            <h3>Desa Songo atau yang bisa juga disebut dengan Kampung Sayur Simo, <br class="hidden sm:block"> adalah salah satu kampung yang
              menerapkan program urban farming yang terletak disurabaya</h3>

            <button @click="readMore('body')" class="btn-primary mt-3">Read more</button>
          </div>
        </div>
      </div>
    </div>
  </div>



  <!-- body -->
  <div id="body" class=" w-screen text-slate-700">
    <!-- navbar -->
    <Nav stats="home" />

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
        <div class="mt-3 sm:mt-0">
          Desa Songo adalah sebutan lain dari Kampung Sayur Simo yang berlokasi di Simomulyo Baru, RT 09 RW 03,
          Kelurahan Simomulyo Baru, Kecamatan Sukomanunggal, Surabaya. Penduduk pada kampung ini berhasil mengubah
          suasana kumuh dan kini menjadi bersih dan hijau melalui program "Urban Farming" melalui teknik hidroponik,
          tanaman sayur dalam pot (tasapot), tanaman buah dalam pot (tabulampot).Dengan dilaksanakannya program
          tersebut, kampung ini kini mempunyai daya tarik bagi pengunjung-pengunjung dari luar desa untuk mengunjungi
          kampung ini.
        </div>
      </div>

      <!-- video profile -->
      <div class="md:grid grid-cols-2 p-6 mb-28">
        <div>
          <p class="md:w-[600px] text-justify">
            Desa Songo atau Kampung Sayur Simo adalah kampung yang menerapkan program urban farming, ide ini berawal dari Bu Yaning yakni ketua RT Desa Songo yang mempunyai misi sangat mulia yaitu ingin menghijaukan kampung nya Misi ini diawali oleh Bu Yaning sejak tahun 2013 akni pada tahun dimana beliau dipilih menjadi ketua RT di kampung ini. <br> Langkah awal yang dilakukan oleh Bu Yaning adalah mengumpulkan semua warga untuk bermusyawarah untuk mengadakan kegiatan pengolahan sampah kering. Dengan semangat dan antusiasme warga akhirnya kegiatan terlaksana dengan baik. <br> Kegiatan mengolah sampah kering dilakukan oleh ibu-ibu PKK setiap hari minggu dengan cara mengambil semua sampah kering yang ada pada rumah-rumah warga dan mengumpulkannya menjadi satu pada suatu tempat. <br> Setelah terkumpul, pada minggu terakhir (minggu terakhir setiap bulan) sampah yang telah terkumpul akan dipilah dan hasil sampah yang sudah dipilah tersebut akan bagi menjadi beberapa bagian yakni sampah yang untuk di jual dan sampah yang untuk kerajinan. <br> Uang hasil dari sampah yang terjual akhirnya dikumpulkan oleh Bu Yaning dan dibelikan pot, bibit untuk diberikan kepada warga.
          </p>
        </div>
        <div class="mt-4 md:mt-0">
          <iframe height="400" src="https://www.youtube.com/embed/9HylJhIM5b8"
        title="Kampung Sayur Simo - Surabaya" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen class="w-full sm:p-1"></iframe>
        </div>
        
      </div>

      <!-- virtual tour -->
      
      <div class="flex w-full justify-center rounded-lg pb-6 shadow-lg p-4">
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
      <div class="my-5 rounded-md shadow-lg">
        <p class="text-center text-xl text-green-800 font-semibold my-2">Gallery</p>
        <!-- image -->
        <div class="w-full justify-center flex overflow-hidden">
          <div class="grid sm:grid-cols-2 md:grid-cols-3 p-3 pr-5">
            <img src="/gallery_ss1.webp" alt="" class="w-auto border-2 shadow-xl rounded p-1">
            <img src="/gallery_ss2.webp" alt="" class="w-auto border-2 shadow-xl rounded p-1">
            <img src="/gallery_ss3.webp" alt="" class="w-auto border-2 shadow-xl rounded p-1">
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- footer -->
  <Footer />

</template>