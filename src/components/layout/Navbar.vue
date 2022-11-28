<template>
    <!-- navbar -->
    <nav class="fixed w-full z-50 top-0 left-0 overflow-hidden border-b-[1px]"
        :class="{'bg-white transition duration-300': onScroll || !transparent_background || dropdown, 'bg-none border-transparent': !onScroll && transparent_background && !dropdown}">
        <div class="w-full lg:max-w-[1240px] md:max-w-[768px] flex justify-between mx-auto py-3 px-[15px]">
            <a href="" class="flex items-center hover:no-underline">
                <img :src="(onScroll || !transparent_background || dropdown) ? '/logo-kampung.webp' : '/logo-kampung-putih.webp'" alt="" class="w-[40px] mr-2">
                <span class="text-base font-semibold">Kampung <span class="text-green-400">Songo</span></span>
            </a>

            <div class="lg:flex hidden items-center text-base gap-x-10">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/urban-farming" class="nav-link">Urban Farming</router-link>
                <router-link to="/tanaman" class="nav-link">Tanaman</router-link>
                <router-link to="/solar-panel" class="nav-link">Solar Panel</router-link>
                <router-link to="/blog" class="nav-link">Blog</router-link>
                <router-link to="/about" class="nav-link">About</router-link>
                <router-link to="/login" class="nav-link">Login</router-link>
            </div>

            <!-- burger button -->
            <button @click="dropdown = !dropdown" class="lg:hidden block px-2 rounded-lg bg-white">
                <svg width="25px" height="25px" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd"
                        d="M1.5 3C1.22386 3 1 3.22386 1 3.5C1 3.77614 1.22386 4 1.5 4H13.5C13.7761 4 14 3.77614 14 3.5C14 3.22386 13.7761 3 13.5 3H1.5ZM1 7.5C1 7.22386 1.22386 7 1.5 7H13.5C13.7761 7 14 7.22386 14 7.5C14 7.77614 13.7761 8 13.5 8H1.5C1.22386 8 1 7.77614 1 7.5ZM1 11.5C1 11.2239 1.22386 11 1.5 11H13.5C13.7761 11 14 11.2239 14 11.5C14 11.7761 13.7761 12 13.5 12H1.5C1.22386 12 1 11.7761 1 11.5Z"
                        fill="currentColor" />
                </svg>

            </button>
        </div>
        <div class="bg-white w-full dropdown">
            <div class="bg-white w-full lg:max-w-[1240px] md:max-w-[768px] mx-auto px-[15px] delay-100 transition-height text-sm font-semibold flex flex-col gap-y-4"
                :class="{ 'max-h-0': !dropdown, 'max-h-[400px]': dropdown }">
                <router-link to="/" class="mt-4 hover:no-underline nav-link-dropdown">Home</router-link>
                <router-link to="/urban-farming" class="hover:no-underline nav-link-dropdown">Urban Farming
                </router-link>
                <router-link to="/tanaman" class="hover:no-underline nav-link-dropdown">Tanaman</router-link>
                <router-link to="/solar-panel" class="hover:no-underline nav-link-dropdown">Solar Panel</router-link>
                <router-link to="/blog" class="hover:no-underline nav-link-dropdown">Blog</router-link>
                <router-link to="/about" class="hover:no-underline nav-link-dropdown">About</router-link>
                <router-link to="/login" class="hover:no-underline nav-link-dropdown mb-8">Login</router-link>
            </div>
        </div>
    </nav>
</template>
<script>
export default {
    name: "Navbar",
    props: {
        transparent_background: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            dropdown: false,
            onScroll: false,
        }
    },
    watch: {

    },
    mounted() {
        window.addEventListener('resize', (data) => {
            if (window.innerWidth >= 1024) {
                this.dropdown = false;
            }
        });
        if (window.scrollY > 5) {
            this.onScroll = true;
        } else {
            this.onScroll = false;
        }
        window.addEventListener('scroll', (data) => {
            if (window.scrollY > 5) {
                this.onScroll = true;
            } else {
                this.onScroll = false;
            }
        });
    },
    method: {
        openDropdown() {
            if (this.dropdown) {
                setTimeout(() => {
                    this.dropdown = false
                }, 300)
            } else {
                this.dropdown = true
            }
        }
    }
}
</script>