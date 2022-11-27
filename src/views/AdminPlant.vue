<script>
import { Modal, Loading, Footer } from '../components';
import utils from '../utils';
// import router from '../router';
import { supabase } from '../supabase';
import { v4 as uuidv4 } from 'uuid';

export default {
    components: {
        Modal,
        Loading,
        Footer
    },
    async mounted() {
        await this.autologin();
        this.count_plant = await utils.getCountTanaman()
        await this.getData();
        this.$watch(
            () => this.cur,
            (toParams, previousParams) => {
                this.getData();
            }
        )
    },
    data() {
        return {
            login: false,
            loading: false,
            loadingStatus: '',
            refreshStatus: '',
            stats: {
                plant: true,
            },
            nav: [
                { page: 'Home', active: false },
                { page: 'Blog', active: false },
                { page: 'Tanaman', active: true },
                { page: 'Comment', active: false }
            ],
            length: 2,
            count_plant: 0,
            plant: {
                name: '',
                category: 'tanpa-kategori',
                img_file: null,
                img: null,
                qty: 1,
                satuan: 'POT',
                description: "",
                usia: 1,
                satuan_usia: 'hari',
                postfail: '',
                deleteplant: '',
                urlplant: '',
                image_name_delete: '',
                deleteModal: false,
                list: [],
                submit: 'submit',
                id: '',
                old_name: '',
                old_image_name: '',
            },
        }
    },
    computed: {
        cur() {
            return this.$route.query.page ? (this.$route.query.page < 1 ? 1 : this.$route.query.page) : 1;
        }
    },
    methods: {
        async autologin() {
            const savedname = localStorage.getItem('name')
            const savedpass = localStorage.getItem('pass')

            if (savedname != null && savedpass != null) {
                this.loading = true
                this.loadingStatus = 'verification'
                const data = await utils.login(savedname, savedpass)
                this.loading = false
                this.loadingStatus = ''

                if (data === "") {
                    this.login = true
                } else {
                    localStorage.clear()
                    this.$router.push('login')
                }
            }
            else
                this.$router.push('login')
        },
        logout() {
            localStorage.clear()
            window.location.reload()
        },
        async getData() {
            this.loading = true;
            let plants = await utils.getTanamanByCategory('', (this.cur - 1) * this.length, this.length);
            this.plant.list = plants;
            this.loading = false;
        },
        handleFileUpload(event) {
            let files = event.target.files;
            if (files.length > 0) {
                try {
                    let file = files[0];
                    if (file.type.split('/')[0] !== 'image') {
                        throw "FORMAT_NOT_VALID"
                    }
                    file = new File([files[0]], `${uuidv4()}.webp`);
                    if (file.size / 1024 / 1024 > 2) {
                        throw "FILE_MAX_SIZE"
                    }
                    this.plant.img_file = file;
                    var reader = new FileReader();
                    reader.onload = () => {
                        // console.log(this.plant.img)
                        this.plant.img = reader.result;
                    };
                    reader.readAsDataURL(file);
                } catch (e) {
                    this.$refs.fileupload.value = ""
                    this.plant.img_file = null;
                    // if (!this.plant.img) {
                    //     this.plant.img = null;
                    // }
                    if (e == 'FILE_MAX_SIZE') {
                        alert("Ukuran foto terlalu besar, maksimal ukuran 2mb")
                    } else if (e == 'FORMAT_NOT_VALID') {
                        alert("Format file tidak didukung, format file harus berjenis gambar")
                    } else {
                        alert("Gagal upload file, coba ulangi kembai");
                    }
                }
            } else {
                this.$refs.fileupload.value = ""
                this.plant.img_file = null;
                this.plant.img = null;
            }
        },
        async submitContent(stats) { //post blog
            if (this.plant.name == '') return this.plant.postfail = "Nama tidak boleh kosong"
            if (this.plant.category == '') return this.plant.postfail = "Kategori tanaman tidak boleh kosong"
            // if (this.plant.img_file == '' || this.plant.img_file == null) return this.blog.postfail = "Foto tanaman tidak boleh kosong"
            this.loading = true
            this.loadingStatus = 'upload plant'
            if (stats == 'update') {
                const status = await utils.updateplant(this.plant.id, this.plant.name, this.plant.category, this.plant.img_file, this.plant.qty, this.plant.satuan, this.plant.description, this.plant.usia, this.plant.satuan_usia, this.plant.old_name, this.plant.old_image_name)
                if (status != '' && !(this.loading = false)) return this.plant.postfail = status
            } else {
                const status = await utils.insertplant(this.plant.name, this.plant.category, this.plant.img_file, this.plant.qty, this.plant.satuan, this.plant.description, this.plant.usia, this.plant.satuan_usia)
                if (status != '' && !(this.loading = false)) return this.plant.postfail = status
            }

            this.loadingStatus = ''
            this.plant.postfail = ''
            this.plant.id = ''
            this.plant.name = ''
            this.plant.category = 'tanpa-kategori'
            this.plant.img_file = null
            this.plant.img = ''
            this.plant.qty = 1
            this.plant.satuan = 'POT'
            this.plant.description = ''
            this.plant.usia = 1
            this.plant.satuan_usia = 'hari'
            this.plant.old_name = ''
            this.plant.old_image_name = ''
            this.plant.submit = 'submit'
            this.loading = false
            this.plant.list = [];
            this.getData();
        },
        async removePlant(idx = null, url = '', image_name = '') {
            if (idx == null) {
                this.plant.deleteModal = false

                this.loading = true
                this.loadingStatus = `delete ${this.plant.deleteplant}`

                try {
                    await supabase.from('plant').delete().match({ id: this.plant.deleteplant })
                    if (this.image_name_delete != '' && this.image_name_delete != null) {
                        await supabase.storage.from('public').remove([image_name_delete.replace(`${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/`, '')]);
                    }
                } catch (e) { }

                this.loadingStatus = ''
                this.loading = false
                this.plant.list = [];
                this.getData();
            } else {
                this.plant.deleteplant = idx
                this.plant.urlplant = url
                this.plant.image_name_delete = image_name
                this.plant.deleteModal = true
            }
        },
        async editPlant(id, plant_url) {
            const { data } = await supabase.from('plant').select().match({ 'id': id })
            this.loading = true
            this.loadingStatus = 'fetch data'
            if (data.length != 0) {
                this.plant.id = id
                this.plant.name = data[0].name
                this.plant.category = data[0].category
                this.plant.img_file = null
                this.plant.img = data[0].img
                this.plant.qty = data[0].qty
                this.plant.satuan = data[0].satuan
                this.plant.description = data[0].description
                this.plant.usia = data[0].usia
                this.plant.satuan_usia = data[0].satuan_usia
                this.plant.oldname = data[0].name
                this.plant.submit = 'update'
                this.plant.old_name = data[0].name
                this.plant.old_image_name = data[0].img
            }
            this.loadingStatus = ''
            this.loading = false
            this.plant.list = [];
            this.getData();

        },
    }
}
</script>

<template>
    <Loading :class="{ hidden: !loading }">{{ loadingStatus }}</Loading>

    <div :class="{ hidden: !login }" class="text-gray-500">
        <!-- navbar -->
        <div class="w-full p-2 border-b mb-2 flex items-center ">
            <a href="/">
                <img src="../assets/logo1.svg" alt="" class="w-10 rounded-xl mr-4">
            </a>

            <div class="flex overflow-x-scroll pb-2 sm:overflow-hidden">
                <div @click="idx != 2 ? $router.push({ name: 'dashboard', query: { page: nav[idx].page } }) : $router.push({ name: 'Plant' })" :class="{ underline: nav[idx].active }"
                    class="mx-2 cursor-pointer hover:opacity-30" v-for="i, idx in nav">{{ i.page }}</div>
            </div>

        </div>

        <!-- plant -->
        <form @submit.prevent="(plant.submit == 'update') ? submitContent('update') : submitContent('')"
            class="rounded-md shadow-md w-full p-3">

            <!-- plant editor -->
            <div>
                <!-- title -->
                <span class="text-sm text-gray-400 mx-1">Nama Tanaman:</span>
                <input v-model="plant.name" type="text" placeholder="Nama Tanaman"
                    class="border px-2 outline-none py-1 w-full mb-2" ref="namePlant">

                <span class="text-sm text-gray-400 mx-1">Kategori Tanaman:</span>

                <select class="border px-2 outline-none py-1 w-full mb-2" v-model="plant.category">
                    <option value="tabulampot">TABULAMPOT</option>
                    <option value="tasalampot">TASALAMPOT</option>
                    <option value="hidroponik">HIDROPONIK</option>
                    <option value="toga">TOGA</option>
                    <option value="tanaman-hias">TANAMAN HIAS</option>
                    <option value="tanpa-kategori">TANPA KATEGORI</option>
                </select>

                <div class="w-full sm:flex gap-x-10">
                    <div>
                        <span class="text-sm text-gray-400 mx-1">Jumlah:</span>
                        <div>
                            <input v-model="plant.qty" type="number" placeholder="QTY"
                                class="border px-2 outline-none py-1 w-[70px] mb-2">
                            <input v-model="plant.satuan" type="text" placeholder="cth: Pot, Lubang, DLL"
                                class="border px-2 outline-none py-1 mb-2">
                        </div>
                    </div>
                    <div>
                        <span class="text-sm text-gray-400 mx-1">Usia Tanaman:</span>
                        <div>
                            <input v-model="plant.usia" type="number" placeholder="QTY"
                                class="border px-2 outline-none py-1 w-[70px] mb-2">
                            <input v-model="plant.satuan_usia" type="text"
                                placeholder="cth: hari, minggu, bulan, dan tahun"
                                class="border px-2 outline-none py-1 mb-2">
                        </div>
                    </div>
                </div>
                <span class="text-sm text-gray-400 mx-1">Deskripsi:</span>
                <input v-model="plant.description" type="text" placeholder="cth: Sudah pernah berbuah"
                    class="w-full border px-2 outline-none py-1 mb-2">
                <span class="text-sm text-gray-400 mx-1">Foto:</span>
                <input @change="handleFileUpload" ref="fileupload" type="file"
                    class="border px-2 outline-none py-1 w-full mb-2" accept="image/*">
                <img v-if="plant.img != '' || plant.img != null" :src="plant.img" class="w-1/4 rounded-lg" />
                <div v-if="plant.postfail" class="italic text-center text-xs text-red-700 mt-2">{{ plant.postfail }}
                </div>

                <!-- submit -->
                <input type="submit" class="bg-green-400 text-white w-full p-1 my-2 hover:underline"
                    :value="plant.submit">
            </div>

        </form>

        <!-- list plant -->
        <div class="overflow-x-scroll my-4  py-1">
            <!-- plant -->
            <table class="w-full" :class="{ hidden: !stats.plant }">
                <tr>
                    <th class="sm:w-10">id</th>
                    <th>Foto</th>
                    <th>Nama Tanaman</th>
                    <th>Kategori</th>
                    <th>Jumlah</th>
                    <th>Usia</th>
                    <th>Deskripsi</th>
                    <th>delete</th>
                    <th>edit</th>
                </tr>
                <tbody v-for="(i, idx) in plant.list">
                    <tr class="text-sm text-center hover:bg-slate-200">
                        <td>{{ idx + (cur * length) - 1 }}</td>
                        <td><img class="max-w-[100px]" v-if="i.img != null" :src="i.img" /></td>
                        <td><a v-bind:href="'/tanaman/' + i.link">{{ i.name }}</a></td>
                        <td>{{ i.category }}</td>
                        <td>{{ i.qty + ' ' + i.satuan }}</td>
                        <td>{{ i.usia + ' ' + i.satuan_usia }}</td>
                        <td>{{ i.description }}</td>
                        <td class="p-1 bg-red-600 text-white sm:hover:underline cursor-pointer"
                            @click="removePlant(i.id, i.link, i.img)">delete</td>
                        <td class="p-1 bg-amber-500 text-white sm:hover:underline cursor-pointer"
                            @click="editPlant(i.id, i.link)">edit</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- pagination -->
        <div class="text-center">
            <router-link :to="{ name: 'Plant', query: { page: i } }" class="border px-2 mx-2 mb-2"
                :class="{ 'text-green-500 cursor-default': i == cur, 'hover:underline cursor-pointer': i != cur }"
                v-for="i in Number((count_plant / length).toFixed())">{{
                        i
                }}</router-link>
        </div>


        <!-- modal delete -->
        <Modal class="top-0 fixed w-full h-full z-10 bg-opacity-90" :class="{ hidden: !plant.deleteModal }">
            <div class="text-center text-gray-500 text-sm">
                confirm delete <br>{{ plant.deleteblog }}
                <div class="text-white mt-4">
                    <button class="mr-5 sm:hover:underline px-6 py-1 bg-red-600" @click="removePlant()">yes</button>
                    <button class="ml-5 sm:hover:underline px-6 py-1 bg-sky-600"
                        @click="plant.deleteModal = !plant.deleteModal">no</button>
                </div>
            </div>
        </Modal>

        <!-- footer -->
        <Footer></Footer>
    </div>
</template>