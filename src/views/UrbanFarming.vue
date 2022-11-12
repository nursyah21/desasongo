<script>
import { Home, Navbar, Footer } from '../components';

export default {
    data() {
        return {

        };
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
    <div id="body" class="w-full lg:max-w-[1140px] md:max-w-[768px] px-[15px] mx-auto mt-32 mb-16">
        <div class="md:grid grid-cols-2 gap-x-10">
            <div>
                <h1 class="title"><span class="text-green-500 font-normal">Sekilas</span> <span
                        class="text-green-500">Urban Farming</span></h1>
                <p class="text-lg">Urban farming atau urban agriculture adalah kegiatan budidaya tanaman
                    dalam dan di sekitar wilayah kota besar (metropolitan) atau kota kecil untuk memperoleh bahan pangan
                    atau kebutuhan lain dan tambahan finansial.</p>
                <br />
                <p class="text-lg">Manfaat dari urban farming salah satunya adalah menghemat pengeluaran. Urban farming
                    sangat efektif
                    untuk menghemat pengeluaran karena dengan adanya urban farming maka masyarakat dapat menikmati hasil
                    taninya sendiri.</p>
            </div>
            <div class="mt-16 md:mt-0">
                <img src="urban-farming.webp" class="rounded-lg" alt="">
            </div>
        </div>
        <div class="mt-16">
            <h1 class="w-1/4 text-center m-auto font-bold text-2xl mb-10">
                <span class="text-green-500 font-normal">Jenis</span> <span class="text-green-500">Tanaman</span>
            </h1>
            <div class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-7">
                <div class="grid grid-cols-2 h-[100px] sm:h-[280px] bg-red-500 rounded-lg transition-transform duration-300 hover:scale-105">
                    <div class="text-white text-2xl font-bold w-full h-full flex items-center justify-center">
                        <h1>Buah</h1>
                    </div>
                    <div class="bg-[url('buah.jpg')] bg-cover bg-center rounded-lg"></div>
                </div>
                <div class="grid grid-cols-2 h-[100px] sm:h-[280px] bg-green-400 rounded-lg transition-transform duration-300 hover:scale-105">
                    <div class="text-white text-2xl font-bold w-full h-full flex items-center justify-center">
                        <h1>Sayur</h1>
                    </div>
                    <div class="bg-[url('sayuran.jpg')] bg-cover bg-center rounded-lg"></div>
                </div>
                <div class="grid grid-cols-2 h-[100px] sm:h-[280px] bg-amber-400 rounded-lg transition-transform duration-300 hover:scale-105">
                    <div class="text-white text-2xl font-bold w-full h-full flex items-center justify-center">
                        <h1>Jamur</h1>
                    </div>
                    <div class="bg-[url('jamur.jpg')] bg-cover bg-center rounded-lg"></div>
                </div>
                <div class="grid grid-cols-2 h-[100px] sm:h-[280px] bg-green-600 rounded-lg transition-transform duration-300 hover:scale-105">
                    <div class="text-white text-2xl font-bold w-full h-full flex items-center justify-center">
                        <h1>Tanaman<br/>Obat</h1>
                    </div>
                    <div class="bg-[url('tanaman-obat.jpg')] bg-cover bg-center rounded-lg"></div>
                </div>
                <div class="grid grid-cols-2 h-[100px] sm:h-[280px] bg-orange-500 rounded-lg transition-transform duration-300 hover:scale-105">
                    <div class="text-white text-2xl font-bold w-full h-full flex items-center justify-center">
                        <h1>Umbi<br/>Umbian</h1>
                    </div>
                    <div class="bg-[url('umbi.jpg')] bg-cover bg-center rounded-lg"></div>
                </div>
                <div class="grid grid-cols-2 h-[100px] sm:h-[280px] bg-green-800 rounded-lg transition-transform duration-300 hover:scale-105">
                    <div class="text-white text-2xl font-bold w-full h-full flex items-center justify-center">
                        <h1>Tanaman<br/>Hias</h1>
                    </div>
                    <div class="bg-[url('tanaman-hias.jpg')] bg-cover bg-center rounded-lg"></div>
                </div>
            </div>
        </div>
    </div>
    <!-- footer -->
    <Footer></Footer>
</template>