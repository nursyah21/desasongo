<script>
export default {
  data(){
    return{
      dropdown: false
    }
  },
  methods: {
    readMore(id) {
      window.location.href = `${window.location.origin}/#${id}`
    }
  }
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
  <div id="body" class="h-screen w-screen">

    <!-- navbar -->
    <nav class="sticky w-screen flex p-4 sm:p-8 py-4 justify-between text-xl bg-white z-50 overflow-hidden">
      <div class="flex items-center -mt-1.5">
        <img src="/favicon.svg" alt="" class="w-[38px] rounded-lg">
        <a href="" class="mx-3 text-green-800 sm:font-semibold">Desa Songo</a>
      </div>

      <!-- dropdown -->
      <div class="right-0 absolute visible sm:invisible">
        <button @click="dropdown = !dropdown" class="btn-dropdown mx-3 my-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
          </svg>
        </button>
      </div>

      <div class="invisible sm:visible">
        <a href="" class="text-green-600 underline mx-3">Home</a>
        <a href="" class="nav-link">Urban Farming</a>
        <a href="" class="nav-link">Tanaman</a>
        <a href="" class="nav-link">Blog</a>
        <a href="" class="nav-link">About</a>
      </div>
    </nav>

    <div v-show="dropdown" class="py-2 absolute z-50 bg-white w-screen h-full">
      <a href="" class="text-green-600 underline mx-3">Home</a><br class="my-1">
      <a href="" class="nav-link">Urban Farming</a><br class="my-1">
      <a href="" class="nav-link">Tanaman</a><br class="my-1">
      <a href="" class="nav-link">Blog</a><br class="my-1">
      <a href="" class="nav-link">About</a>
    </div>

    <!-- content -->
    <div class="px-3">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut, voluptatibus nobis recusandae, obcaecati voluptates cupiditate hic debitis neque fugiat sit in sapiente amet quas. Eligendi aut voluptatum provident aspernatur expedita. <br>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit totam explicabo libero nobis fuga repellat maiores ea ipsa nulla in voluptate iste cum doloribus eos, natus sequi repudiandae ad deleniti? <br>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Totam, aliquam quas alias velit labore explicabo rem dignissimos, mollitia quibusdam suscipit reiciendis expedita libero dicta voluptate? Explicabo quos consequuntur quaerat officia!
    </div>
  </div>

  <!-- footer -->
  <div class="bg-slate-800 text-white p-6">
    footer
  </div>
</template>