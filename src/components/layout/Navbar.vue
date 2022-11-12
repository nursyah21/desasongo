<template>
    <!-- navbar -->
    <nav class="fixed w-full flex py-3 px-3 md:px-28 justify-between z-50 top-0 transition duration-300"
        :class="{ 'bg-white': onScroll, 'bg-none': !onScroll }">

        <a href="" class="flex items-center hover:no-underline">
            <img src="/favicon.svg" alt="" class="w-[38px] mr-2">
            <span class="text-base font-semibold">Desa <span class="text-green-400">Songo</span></span>
        </a>

        <div class="lg:flex hidden items-center text-base gap-x-10">
            <a href="/" class="nav-link active">Home</a>
            <a href="/blog/urban-farming" class="nav-link">Urban Farming</a>
            <a href="/blog/tanaman" class="nav-link">Tanaman</a>
            <a href="/list-blog" class="nav-link">Blog</a>
            <a href="/blog/about" class="nav-link">About</a>
        </div>

        <!-- burger button -->
        <button @click="dropdownFunc" class="lg:hidden block px-2 rounded-lg bg-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20">
                <path
                    d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
            </svg>
        </button>
    </nav>

    <div v-show="dropdown" class="py-2 absolute z-50 bg-white w-full h-screen">
        <a href="/" class="nav-link">Home</a><br class="my-1">
        <a href="/blog/urban-farming" class="nav-link">Urban Farming</a><br class="my-1">
        <a href="/blog/tanaman" class="nav-link">Tanaman</a><br class="my-1">
        <a href="/list-blog" class="nav-link">Blog</a><br class="my-1">
        <a href="/blog/about" class="nav-link">About</a>
    </div>
</template>
<script>
export default {
    name: "Navbar",
    data() {
        return {
            dropdown: false,
            onScroll: false,
        }
    },
    mounted() {
        window.addEventListener('scroll', (data) => {
            if (window.scrollY > 5) {
                this.onScroll = true;
            } else {
                this.onScroll = false;
            }
        });
    },
    method: {
        dropdownFunc() {
            alert('ah')
            this.dropdown = !this.dropdown
            if (this.dropdown) window.location.href = `${window.location.origin}/#body`;
        }
    }
}
</script>