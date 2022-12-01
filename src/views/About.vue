<script>
import { Home, Navbar, Footer } from '../components';

export default {
    data() {
        return {

        };
    },
    mounted() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0;
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
    <navbar></navbar>
    <!-- body -->
    <div id="body" class="w-full lg:max-w-[1240px] md:max-w-[768px] px-[15px] mx-auto mt-32 mb-16">
        <div class="flex flex-col lg:flex-row justify-between gap-x-10">
            <div class="w-full lg:w-1/2">
                <h1 class="title"><span class="text-green-500 font-normal">Sekilas</span> <span
                        class="text-green-500">Kampung Songo</span></h1>
                <p class="text-lg">Kampung Songo atau Kampung Sayur Simo adalah kampung yang menerapkan program urban
                    farming, ide ini berawal dari Bu Yaning yakni ketua RT Kampung Songo.</p>
                <br />
                <p class="text-lg">Langkah awal
                    yang dilakukan oleh Bu Yaning adalah mengumpulkan semua warga untuk bermusyawarah untuk mengadakan
                    kegiatan pengolahan sampah kering. Dengan semangat dan antusiasme warga akhirnya kegiatan terlaksana
                    dengan baik.</p>
            </div>
            <div class="w-full lg:w-1/2 mt-16 lg:mt-0">
                <img src="/img9.jpg" class="rounded-lg" alt="">
            </div>
        </div>
        <div class="flex flex-col-reverse lg:flex-row justify-between gap-x-10 mt-16">
            <div class="w-full lg:w-1/2 mt-16 lg:mt-0">
                <img src="/img10.webp" class="rounded-lg" alt="">
            </div>
            <div class="w-full lg:w-1/2">
                <h1 class="title"><span class="text-green-500 font-normal">Kegiatan</span> <span
                        class="text-green-500">Kampung Songo</span></h1>
                <p class="text-lg">Kegiatan mengolah sampah kering dilakukan oleh ibu-ibu PKK setiap hari minggu dengan
                    cara mengambil semua sampah kering yang ada pada rumah-rumah warga dan mengumpulkannya menjadi satu
                    pada suatu tempat. Setelah terkumpul, pada minggu terakhir (minggu terakhir setiap bulan) sampah
                    yang telah terkumpul akan dipilah dan dibagi menjadi
                    beberapa bagian yakni sampah yang untuk di jual dan sampah untuk kerajinan. Uang hasil dari
                    sampah yang terjual akhirnya dikumpulkan oleh Bu Yaning dan dibelikan pot, bibit untuk diberikan
                    kepada warga.</p>
            </div>
        </div>
        <div class="mt-16">
            <h1 class="w-full text-center m-auto font-bold text-2xl mb-10">
                <span class="text-green-500 font-normal">Penghargaan</span> <span class="text-green-500">Kampung
                    Songo</span>
            </h1>
            <div class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-7">
                <div
                    class="grid grid-cols-2 h-[100px] sm:h-[280px] bg-green-600 rounded-lg transition-transform duration-300 hover:scale-105">
                    <div
                        class="text-white text-xs sm:text-sm px-3 text-center font-bold w-full h-full flex items-center justify-center">
                        <h1>Penghargaan Lomba Merdeka Dari Sampah 2015 : Kategori Kampung Pemilahan Sampah Terbaik</h1>
                    </div>
                    <div class="bg-[url('/penghargaan1.jpg')] bg-cover bg-center rounded-r-lg"></div>
                </div>
                <div
                    class="grid grid-cols-2 h-[100px] sm:h-[280px] bg-amber-500 rounded-lg transition-transform duration-300 hover:scale-105">
                    <div
                        class="text-white text-xs sm:text-sm px-3 text-center font-bold w-full h-full flex items-center justify-center">
                        <h1>Penghargaan Lomba Merdeka Dari Sampah 2017 : Kategori Kampung Partisipasi Terbaik</h1>
                    </div>
                    <div class="bg-[url('/penghargaan3.jpg')] bg-cover bg-center rounded-r-lg"></div>
                </div>
            </div>
        </div>
    </div>
    <!-- footer -->
    <Footer></Footer>
</template>