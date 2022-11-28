<script>
import { Home, Navbar, Footer } from '../components';
export default {
  data() {
    return {

    }
  },
  async mounted() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0;
  },
  components: { Home, Navbar, Footer }
}
</script>


<template>
  <navbar></navbar>
  <div class="bg-fixed w-full h-[91vh] bg-[url('/solar-panel.jpg')] bg-cover bg-center mt-16">
    <div class="w-full h-full bg-[rgba(0,0,0,.6)]">
      <div
        class="w-full h-full lg:max-w-[1240px] md:max-w-[768px] px-[15px] mx-auto flex flex-col justify-center items-center text-center">
        <span class="text-green-500 text-4xl font-extrabold leading-[43px] mb-3">
          Solar Panel
        </span>
        <span class="text-white max-w-3xl font-semibold">
          Solar panel adalah salah satu pilihan masyarakat atau perusahaan sebagai alat pembangkit listrik ramah
          lingkungan dalam mengatasi pencemaran lingkungan dan pemanasan global dan juga sebagai tindakan upaya mencegah
          pemanasan global yang kini mulai dirasakan oleh semua orang di seluruh dunia.
        </span>
      </div>
    </div>
  </div>
  <!-- body -->
  <div id="body" class="w-full lg:max-w-[1240px] md:max-w-[768px] px-[15px] mx-auto mt-16 mb-16">
    <h1 class="title"><span class="text-green-500 font-normal">Apa sih itu</span><span class="text-green-500"> solar
        panel ?</span></h1>
    <p class="mb-3 text-justify">
      Mari kita berkenalan lebih dahulu apa itu solar panel yang kini menjadi incaran perusahaan besar hingga masyarakat
      biasa demi mengirit tagihan listrik hingga 60%. Panel Surya atau Solar
      Panel adalah sebuah kumpulan sel-sel surya yang disusun atau ditata sedemikian rupa untuk menyerap sinar matahari
      secara efektif. Sel surya terdiri dari komponen photovioltaic atau bisa disebut sebagai komponen yang mampu
      mengubah sinar matahari atau cahaya menjadi energi listrik.
    </p>
    <p class="mb-3 text-justify">
      Selain mengirit biaya listrik hingga 60%, solar panel mempunyai berbagai manfaat lainnya adalah ramah lingkungan,
      cocok dipasang di berbagai macam atau jenis iklim, garansi produk yang sangat panjang 25-30 tahun, dan bisa
      membuat harga rumah anda menjadi bertambah atau nilai nya meningkat.
    </p>
    <p class="mb-3 text-justify">
      Jika anda ingin memasang panel surya maka anda haru menghitung berapa banyak konsumsi listrik yang anda butuhkan
      untuk ruah atau perusahaan anda agar nantinya tidak kurang bahkan berlebihan dan tetap mencukupi kebutuhan listrik
      di rumah atau perusahaan anda.
    </p>
  </div>
  <div id="body2" class="w-full bg-[#333] mt-16 py-16">
    <div class="lg:max-w-[1240px] md:max-w-[768px] px-[15px] mx-auto">
      <h1 class="w-full text-center m-auto font-bold text-2xl mb-12">
        <span class="text-white">Alat atau komponen yang dibutuhkan</span>
      </h1>
      <h1 class="text-white"></h1>
      <div class="sm:flex justify-around gap-20">
        <div>
          <img src="/module-panel-surya.png" alt="">
          <h2 class="w-full text-center m-auto font-bold text-1xl sm:mt-4">
            <span class="text-white uppercase">Panel Surya</span>
          </h2>
        </div>
        <div>
          <img src="/inverter.png" alt="">
          <h2 class="w-full text-center m-auto font-bold text-1xl sm:mt-4">
            <span class="text-white uppercase">Inverter</span>
          </h2>
        </div>
        <div>
          <img src="/energy-storage.png" alt="">
          <h2 class="w-full text-center m-auto font-bold text-1xl sm:mt-4">
            <span class="text-white uppercase">Enery Storage</span>
          </h2>
        </div>
      </div>
    </div>
  </div>
  <!-- footer -->
  <Footer></Footer>
</template>
