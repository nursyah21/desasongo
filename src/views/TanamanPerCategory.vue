<script>
import { Home, Navbar, Footer } from '../components';
import utils from '../utils';
export default {
    data() {
        return {
            loading: false,
            max: false,
            limit: 8,
            plants: [],
        };
    },
    mounted() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0;
        this.getData();
    },
    methods: {
        async getData() {

            this.loading = true;
            var plants_data = await utils.getTanamanByCategory(this.$route.params.category, this.plants.length, this.limit);
            if (plants_data.length < 8) {
                this.max = true;
            }
            plants_data.forEach((e) => {
                this.plants.push(e);
            })
            this.loading = false;

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
    <div id="body" class="w-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto mt-32 mb-16">
        <h1 class="title" v-if="$route.params.category == 'tabulampot'">TABULAMPOT (TANAMAN BUAH DALAM POT)</h1>
        <h1 class="title" v-if="$route.params.category == 'tasalampot'">TASALAMPOT (TANAMAN SAYUR DALAM POT)</h1>
        <h1 class="title" v-if="$route.params.category == 'hidroponik'">HIDROPONIK</h1>
        <h1 class="title" v-if="$route.params.category == 'toga'">TOGA (TANAMAN OBAT KELUARGA)</h1>
        <h1 class="title" v-if="$route.params.category == 'tanaman-hias'">TANAMAN HIAS</h1>
        <h1 class="title" v-if="$route.params.category == 'tanpa-kategori'">TANPA KATEGORI</h1>
        <div class="w-full grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-4">
            <div v-for="data in plants"
                class="w-full bg-white rounded-lg border shadow-lg flex-col mb-6 transition-transform duration-300 hover:scale-105">
                <div class="bg-gradient-to-r from-green-600 to-green-500 flex items-center justify-center rounded-t-lg">
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
                    <p class="text-sm">Jumlah : <span class="font-semibold">{{ data.qty + ' ' + data.satuan }}</span>
                    </p>
                    <p class="text-sm">Usia : <span class="font-semibold">{{ data.usia + ' ' + data.satuan_usia
                    }}</span></p>
                    <p class="text-sm text-green-400 font-semibold">{{ data.description }}</p>
                </div>
            </div>
        </div>
        <button v-if="!loading && !max" @click="getData()"
            class="border-green-500 border rounded-md p-3 text-green-500 text-sm block m-auto hover:scale-105 transition-transform duration-300">Muat
            lebih banyak</button>
        <div v-if="loading" class="flex justify-center items-center">
            <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
                <!-- <span class="visually-hidden">Loading...</span> -->
            </div>
        </div>
    </div>
    <!-- footer -->
    <Footer></Footer>
</template>
