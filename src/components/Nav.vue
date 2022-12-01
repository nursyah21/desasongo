<script>
export default{
  props:{
    stats: String
  },
  data() {
    return {
      dropdown: false
    };
  },
  methods: {
    dropdownFunc(){
      // alert('ah')
      this.dropdown = !this.dropdown
      if(this.dropdown) window.location.href = `#`;
    }
  },
}
</script>

<template>
  <nav class="sticky w-screen flex p-4 sm:p-6 items-center justify-between text-xl bg-white z-50 overflow-hidden top-0">
    <div class="flex items-center -mt-1.5">
      <img src="/favicon.svg" alt="" class="w-[38px] rounded-lg">
      <a href="" class="mx-3 text-green-800 sm:font-semibold">Kampung Songo</a>
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
      <a href="/" class="nav-link" :class="{'underline': stats == 'home'}">Home</a>
      <a href="/blog/urban-farming" class="nav-link" :class="{'underline': stats == 'urbanFarming'}">Urban Farming</a>
      <a href="/blog/tanaman" class="nav-link" :class="{'underline': stats == 'tanaman'}">Tanaman</a>
      <a href="/blog/tanaman" class="nav-link" :class="{'underline': stats == 'tanaman'}">Tanaman</a>
      <a href="/list-blog" class="nav-link" :class="{'underline': stats == 'blog'}">Blog</a>
      <a href="/blog/tentang-desa-songo" class="nav-link" :class="{'underline': stats == 'about'}">About</a>
    </div>
  </nav>

  
  <div v-show="dropdown" class="py-2 absolute z-50 bg-white w-screen h-screen md:invisible">
    <a href="/" class="nav-link" :class="{'underline': stats == 'home'}">Home</a><br class="my-1">
    <a href="/blog/urban-farming" class="nav-link" :class="{'underline': stats == 'urbanFarming'}">Urban Farming</a><br class="my-1">
    <a href="/blog/tanaman" class="nav-link"  :class="{'underline': stats == 'tanaman'}">Tanaman</a><br class="my-1">
    <a href="/list-blog" class="nav-link"  :class="{'underline': stats == 'blog'}">Blog</a><br class="my-1">
    <a href="/blog/tentang-desa-songo" class="nav-link"  :class="{'underline': stats == 'about'}">About</a>
  </div>

</template>
