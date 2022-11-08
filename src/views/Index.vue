<script>
import { Home } from '../components';

export default {
    data() {
        return {
            dropdown: false
        };
    },
    methods: {
        readMore(id) {
            window.location.href = `${window.location.origin}/#${id}`;
        },
        dropdownFunc(){
          // alert('ah')
          this.dropdown = !this.dropdown
          if(this.dropdown) window.location.href = `${window.location.origin}/#body`;
        }
    },
    components: { Home }
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
            <h3>Desa Songo atau yang bisa juga disebut dengan Kampung Sayur Simo, adalah salah satu kampung yang
              menerapkan program urban farming yang terletak disurabaya</h3>

            <button @click="readMore('body')" class="btn-primary mt-3">Read more</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  

  <!-- body -->
  <div id="body" class=" w-screen">
    <!-- navbar -->
    <nav class="sticky w-screen flex p-4 sm:p-6 justify-between text-xl bg-white z-50 overflow-hidden top-0">
      <div class="flex items-center -mt-1.5">
        <img src="/favicon.svg" alt="" class="w-[38px] rounded-lg">
        <a href="" class="mx-3 text-green-800 sm:font-semibold">Desa Songo</a>
      </div>

      <!-- dropdown -->
      <div class="right-0 absolute visible md:invisible">
        <button @click="dropdownFunc" class="btn-dropdown mx-3 my-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
          </svg>
        </button>
      </div>

      <div class="invisible md:visible">
        <a href="/" class="text-green-600 underline mx-3">Home</a>
        <a href="/blog/urban-farming" class="nav-link">Urban Farming</a>
        <a href="/blog/tanaman" class="nav-link">Tanaman</a>
        <a href="/list-blog" class="nav-link">Blog</a>
        <a href="/blog/about" class="nav-link">About</a>
      </div>
    </nav>

    <div v-show="dropdown" class="py-2 absolute z-50 bg-white w-screen h-full">
      <a href="/" class="text-green-600 underline mx-3">Home</a><br class="my-1">
      <a href="/blog/urban-farming" class="nav-link">Urban Farming</a><br class="my-1">
      <a href="/blog/tanaman" class="nav-link">Tanaman</a><br class="my-1">
      <a href="/list-blog" class="nav-link">Blog</a><br class="my-1">
      <a href="/blog/about" class="nav-link">About</a>
    </div>

    <!-- content -->
    <div class="px-3">
      <div class="sm:flex">
        <div class="sm:w-1/2">
          <span class="text-sm">tentang</span>
          <p class="text-3xl">DESA SONGO</p>
        </div>
        <p class="my-2 text-justify sm:pl-48 sm:pr-8">
          Desa Songo adalah sebutan lain dari Kampung Sayur Simo yang berlokasi di Simomulyo Baru, RT 09 RW 03, Kelurahan Simomulyo Baru, Kecamatan Sukomanunggal, Surabaya. Penduduk pada kampung ini berhasil mengubah suasana kumuh dan kini menjadi bersih dan hijau melalui program "Urban Farming" melalui teknik hidroponik, tanaman sayur dalam pot (tasapot), tanaman buah dalam pot (tabulampot).Dengan dilaksanakannya program tersebut, kampung ini kini mempunyai daya tarik bagi pengunjung-pengunjung dari luar desa untuk mengunjungi kampung ini.
        </p>
      </div>

    <!-- video profile -->
    <div class="my-4 sm:my-0 sm:pr-12 sm:py-12 md:flex">
      <iframe width="600" height="358" src="https://www.youtube.com/embed/9HylJhIM5b8" title="Kampung Sayur Simo - Surabaya" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="w-full border sm:p-1 sm:shadow-md"></iframe>
      <p class="mt-2 md:pl-24 text-justify">
        Desa Songo atau Kampung Sayur Simo adalah kampung yang menerapkan program urban farming, ide ini berawal dari Bu Yaning yakni ketua RT Desa Songo yang mempunyai misi sangat mulia yaitu ingin menghijaukan kampung nya Misi ini diawali oleh Bu Yaning sejak tahun 2013 ...  <br class="hidden sm:block"><a href="/blog/tentang-desa-songo" class="text-blue-500">readmore</a>
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
          <a href="https://dkpp.surabaya.go.id/VirtualTourSimomulyoBaru/" class="btn-primary hover:no-underline">Lihat Sekarang</a>
        </div>
      </div>
    </div>

    <!-- gallery -->
    <div></div>

    </div>
  </div>

  <!-- footer -->
  <div class="bg-slate-800 text-white p-6 mt-5">
    <!-- lokasi -->
    <div class="flex text-xs md:text-sm mb-2 justify-between">
      <div>
        <a href="https://goo.gl/maps/W9H53eUJgHqZYbEx5">Lokasi</a> <br>
        <p class="w-72">
          Kampung Songo, Simomulyo Baru, RT 09 RW 03, Kelurahan Simomulyo Baru, Kecamatan Sukomanunggal, Surabaya <br>
        </p>
      </div>

      <div>
        Contact: <br>
        No. Telepon : 085843491415 (Bu Yaning)
      </div>
    </div>

    <div class="flex text-xs justify-center w-full text-center text-slate-300">
      <p>copyright 2022 desasongo<br><a href="https://github.com/nursyah21/cmsblog">powered by cmsblog</a></p>
    </div>
  </div>
</template>