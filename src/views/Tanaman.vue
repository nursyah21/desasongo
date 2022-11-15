<script>
import { Home, Navbar, Footer } from '../components';
import utils from '../utils';
export default {
    data() {
        return {
            loading_tabulampot: false,
            loading_tasalampot: false,
            loading_hidroponik: false,
            loading_toga: false,
            loading_tanaman_hias: false,
            loading_tanpa_kategori: false,
            tabulampot: [],
            tasalampot: [],
            hidroponik: [],
            toga: [],
            tanaman_hias: [],
            tanpa_kategori: [],
        };
    },
    mounted() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0;
        this.getData();
    },
    methods: {
        async getData() {

            this.loading_tabulampot = true;
            this.tabulampot = await utils.getTanamanByCategory('tabulampot')
            this.loading_tabulampot = false;

            this.loading_tasalampot = true;
            this.tasalampot = await utils.getTanamanByCategory('tasalampot')
            this.loading_tasalampot = false;

            this.loading_hidroponik = true;
            this.hidroponik = await utils.getTanamanByCategory('hidroponik')
            this.loading_hidroponik = false;

            this.loading_toga = true;
            this.toga = await utils.getTanamanByCategory('toga')
            this.loading_toga = false;

            this.loading_tanaman_hias = true;
            this.tanaman_hias = await utils.getTanamanByCategory('tanaman-hias')
            this.loading_tanaman_hias = false;

            this.loading_tanpa_kategori = true;
            this.tanpa_kategori = await utils.getTanamanByCategory('tanpa-kategori')
            this.loading_tanpa_kategori = false;

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
    <!-- body -->
    <div id="body" class="min-h-[70vh] w-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto mt-32 mb-16">
        <div v-if="tabulampot.length > 0">
            <div class="flex flex-col md:flex-row">
                <h1 class="title">TABULAMPOT (TANAMAN BUAH DALAM POT)</h1>
                <router-link :to="{ name: 'TanamanPerCategory', params: { category: 'tabulampot' } }"
                    class="md:ml-6 text-green-400 font-semibold hover:no-underline hover:text-green-500 cursor-pointer">
                    Lihat Semua</router-link>
            </div>
            <div v-if="!loading_tabulampot" class="w-full flex overflow-x-scroll gap-x-5 pb-1 mb-3 rounded-lg">
                <div v-for="data in tabulampot"
                    class="block w-1/2 sm:w-1/4 lg:w-3/12 flex-shrink-0 bg-white rounded-lg border shadow-lg flex-col mb-6">
                    <div
                        class="bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-t-lg">
                        <img v-if="data.img" class="w-full h-[140px] object-cover object-center rounded-t-lg"
                            :src="data.img" alt="">
                        <p v-else
                            class="w-full h-[140px] justify-center text-white text-lg font-bold tracking-wide flex items-center">
                            No Image
                        </p>
                    </div>
                    <div class="p-3">
                        <h1 class="font-semibold text-md tracking-wide mb-3 line-clamp-2">{{
                                data.name
                        }}
                        </h1>
                        <p class="text-sm">Jumlah : {{ data.qty + ' ' + data.satuan }}</p>
                        <p class="text-sm">Usia : {{ data.usia + ' ' + data.satuan_usia }}</p>
                        <p class="text-sm">{{ data.description }}</p>
                    </div>
                </div>
            </div>
            <div v-else class="flex justify-center items-center">
                <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
                </div>
            </div>
        </div>
        <div class="mt-16" v-if="tasalampot.length > 0">
            <div class="flex flex-col md:flex-row">
                <h1 class="title">TASALAMPOT (TANAMAN SAYUR DALAM POT)</h1>
                <router-link :to="{ name: 'TanamanPerCategory', params: { category: 'tasalampot' } }"
                    class="md:ml-6 text-green-400 font-semibold hover:no-underline hover:text-green-500 cursor-pointer">
                    Lihat Semua</router-link>
            </div>
            <div v-if="!loading_tasalampot" class="w-full flex overflow-x-scroll gap-x-5 pb-1 mb-3 rounded-lg">
                <div v-for="data in tasalampot"
                    class="block w-1/2 sm:w-1/4 lg:w-3/12 flex-shrink-0 bg-white rounded-lg border shadow-lg flex-col mb-6">
                    <div
                        class="bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-t-lg">
                        <img v-if="data.img" class="w-full h-[140px] object-cover object-center rounded-t-lg"
                            :src="data.img" alt="">
                        <p v-else
                            class="w-full h-[140px] justify-center text-white text-lg font-bold tracking-wide flex items-center">
                            No Image
                        </p>
                    </div>
                    <div class="p-3">
                        <h1 class="font-semibold text-md tracking-wide mb-3 line-clamp-2">{{
                                data.name
                        }}
                        </h1>
                    </div>
                </div>
            </div>
            <div v-else class="flex justify-center items-center">
                <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
                </div>
            </div>
        </div>
        <div class="mt-16" v-if="hidroponik.length > 0">
            <div class="flex flex-col md:flex-row">
                <h1 class="title">HIDROPONIK</h1>
                <router-link :to="{ name: 'TanamanPerCategory', params: { category: 'hidroponik' } }"
                    class="md:ml-6 text-green-400 font-semibold hover:no-underline hover:text-green-500 cursor-pointer">
                    Lihat Semua</router-link>
            </div>
            <div v-if="!loading_hidroponik" class="w-full flex overflow-x-scroll gap-x-5 pb-1 mb-3 rounded-lg">
                <div v-for="data in hidroponik"
                    class="block w-1/2 sm:w-1/4 lg:w-3/12 flex-shrink-0 bg-white rounded-lg border shadow-lg flex-col mb-6">
                    <div
                        class="bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-t-lg">
                        <img v-if="data.img" class="w-full h-[140px] object-cover object-center rounded-t-lg"
                            :src="data.img" alt="">
                        <p v-else
                            class="w-full h-[140px] justify-center text-white text-lg font-bold tracking-wide flex items-center">
                            No Image
                        </p>
                    </div>
                    <div class="p-3">
                        <h1 class="font-semibold text-md tracking-wide mb-3 line-clamp-2">{{
                                data.name
                        }}
                        </h1>
                    </div>
                </div>
            </div>
            <div v-else class="flex justify-center items-center">
                <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
                </div>
            </div>
        </div>
        <div class="mt-16" v-if="toga.length > 0">
            <div class="flex flex-col md:flex-row">
                <h1 class="title">TOGA (TANAMAN OBAT KELUARGA)</h1>
                <router-link :to="{ name: 'TanamanPerCategory', params: { category: 'toga' } }"
                    class="md:ml-6 text-green-400 font-semibold hover:no-underline hover:text-green-500 cursor-pointer">
                    Lihat Semua</router-link>
            </div>
            <div v-if="!loading_toga" class="w-full flex overflow-x-scroll gap-x-5 pb-1 mb-3 rounded-lg">
                <div v-for="data in toga"
                    class="block w-1/2 sm:w-1/4 lg:w-3/12 flex-shrink-0 bg-white rounded-lg border shadow-lg flex-col mb-6">
                    <div
                        class="bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-t-lg">
                        <img v-if="data.img" class="w-full h-[140px] object-cover object-center rounded-t-lg"
                            :src="data.img" alt="">
                        <p v-else
                            class="w-full h-[140px] justify-center text-white text-lg font-bold tracking-wide flex items-center">
                            No Image
                        </p>
                    </div>
                    <div class="p-3">
                        <h1 class="font-semibold text-md tracking-wide mb-3 line-clamp-2">{{
                                data.name
                        }}
                        </h1>
                    </div>
                </div>
            </div>
            <div v-else class="flex justify-center items-center">
                <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
                </div>
            </div>
        </div>
        <div class="mt-16" v-if="tanaman_hias.length > 0">
            <div class="flex flex-col md:flex-row">
                <h1 class="title">TANAMAN HIAS</h1>
                <router-link :to="{ name: 'TanamanPerCategory', params: { category: 'tanaman-hias' } }"
                    class="md:ml-6 text-green-400 font-semibold hover:no-underline hover:text-green-500 cursor-pointer">
                    Lihat Semua</router-link>
            </div>
            <div v-if="!loading_tanaman_hias" class="w-full flex overflow-x-scroll gap-x-5 pb-1 mb-3 rounded-lg">
                <div v-for="data in tanaman_hias"
                    class="block w-1/2 sm:w-1/4 lg:w-3/12 flex-shrink-0 bg-white rounded-lg border shadow-lg flex-col mb-6">
                    <div
                        class="bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-t-lg">
                        <img v-if="data.img" class="w-full h-[140px] object-cover object-center rounded-t-lg"
                            :src="data.img" alt="">
                        <p v-else
                            class="w-full h-[140px] justify-center text-white text-lg font-bold tracking-wide flex items-center">
                            No Image
                        </p>
                    </div>
                    <div class="p-3">
                        <h1 class="font-semibold text-md tracking-wide mb-3 line-clamp-2">{{
                                data.name
                        }}
                        </h1>
                    </div>
                </div>
            </div>
            <div v-else class="flex justify-center items-center">
                <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
                </div>
            </div>
        </div>
        <div class="mt-16" v-if="tanpa_kategori.length > 0">
            <div class="flex flex-col md:flex-row">
                <h1 class="title">TANPA KATEGORI</h1>
                <router-link :to="{ name: 'TanamanPerCategory', params: { category: 'tanpa-kategori' } }"
                    class="md:ml-6 text-green-400 font-semibold hover:no-underline hover:text-green-500 cursor-pointer">
                    Lihat Semua</router-link>
            </div>
            <div v-if="!loading_tanpa_kategori" class="w-full flex overflow-x-scroll gap-x-5 pb-1 mb-3 rounded-lg">
                <div v-for="data in tanpa_kategori"
                    class="block w-1/2 sm:w-1/4 lg:w-3/12 flex-shrink-0 bg-white rounded-lg border shadow-lg flex-col mb-6">
                    <div
                        class="bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-t-lg">
                        <img v-if="data.img" class="w-full h-[140px] object-cover object-center rounded-t-lg"
                            :src="data.img" alt="">
                        <p v-else
                            class="w-full h-[140px] justify-center text-white text-lg font-bold tracking-wide flex items-center">
                            No Image
                        </p>
                    </div>
                    <div class="p-3">
                        <h1 class="font-semibold text-md tracking-wide mb-3 line-clamp-2">{{
                                data.name
                        }}
                        </h1>
                    </div>
                </div>
            </div>
            <div v-else class="flex justify-center items-center">
                <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
                </div>
            </div>
        </div>
    </div>
    <!-- footer -->
    <Footer></Footer>
</template>
