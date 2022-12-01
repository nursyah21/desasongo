import { supabase } from "../supabase";
import bcrypt from "bcryptjs"
import { v4 as uuidv4 } from 'uuid';

const visited = async function () {
  const { data, error } = await supabase.from('visited').select().match({ time: new Date().toDateString() })

  if (error) return console.log(error)
  const prevcount = (data[0] === undefined) ? 0 : data[0].counts

  var datas = {
    time: new Date().toDateString(),
    counts: 1 + prevcount,
  }

  if (prevcount != 0) {
    const { error } = await supabase.from('visited').update({ counts: datas.counts }).match({ time: datas.time })
    if (error) console.log(error)
  } else {
    const { error } = await supabase.from('visited').insert(datas)
    if (error) console.log(error)
  }
}

const getDataAndLimit = async function (cur: number, length: number) {
  const blog: Array<any> = []


  let blog_data = await supabase.from('blog').select('blog_id, release, data, title, link, preview_data').order('blog_id', { ascending: false }).range(cur, cur + length).then(e => e.data)
  blog_data?.forEach((e) => {
    const element = document.createRange().createContextualFragment(e.data);
    var img = element.querySelector('img');
    e.img = img ? img.getAttribute('src') : null;
    blog.push(e)
  })


  return { blog }
}

const getDataIndex = async function (current: number) {
  /** blog
   * {title:'mengenal desa songo',
  data:'Kampung ini dulunya agak kumuh dan kurang hijau, hingga tahun 2013 Bu Yaning terpilih sebagai ketua KT. Mengapa Bu Yaning mau menjadi RT karena Bu Yaning mempunyai misi yaitu bagaimana cara mengubah kampung ini menjadi bersih dan hijau...',
  link:'/blog/tentang-desa-songo',
  release:'20 december 2022'}
   */

  const blog: Array<any> = []
  return getDataAndLimit(current, 5);
}

const getCountTanaman = async function () {
  let { count } = await supabase.from('plant').select('*', {count: 'exact'});
  return count;
}

const getTanamanByCategory = async function (category: string, current: number = 0, length: number = 4) {
  const plants: Array<any> = []
  let plants_data;
  if (category != '') {
    plants_data = await supabase.from('plant').select('id, img, name, category, link, qty, satuan, description, usia, satuan_usia').order('id', { ascending: false }).match({ category: category }).range(current, current + length - 1).then(e => e.data);
  } else {
    plants_data = await supabase.from('plant').select('id, img, name, category, link, qty, satuan, description, usia, satuan_usia').order('id', { ascending: false }).range(current, current + length - 1).then(e => e.data);
  }

  plants_data?.forEach((e) => {
    plants.push(e)
  })


  return plants;
}

const login = async function (name: string, pass: string) {
  const { data, error } = await supabase.from('users').select().match({ name: name });

  if (error) return console.log(error)

  if (data[0] != undefined) return (comparePass(data[0].pass, pass)) ? "" : "wrong password"
  return "wrong username"
}

const encryptPass = function (pass: string): string {
  return bcrypt.hashSync(pass, bcrypt.genSaltSync(10))
}

const comparePass = function (pass: string, hash: string): boolean {
  return bcrypt.compareSync(pass, hash)
}

const insertblog = async function (title: string) {
  try {
    var content = document.querySelector('.fr-element.fr-view') as HTMLElement | null
    var submitcontent = content!!.innerHTML

    var img = content!!.querySelectorAll('img')
    for (var i = 0; i < img.length; i++) {
      var s = img[i].src.split('/').pop()
      s = `${uuidv4()}-${s}`

      // upload image
      var up = await fetch(img[i].src).then(r => r.blob())
      try {
        await supabase.storage.from('public').upload(`${s}`, up)
      } catch (e) { }


      // change blob to img in innerhtml      
      s = `${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/${s}`
      submitcontent = submitcontent.replace(img[i].src, s)
    }

    const titleCheck = await supabase.from('blog').select().match({ title: title }).then(e => e.data)

    if (titleCheck?.length != 0) return 'title already exists'

    const datas = {
      title: title,
      link: title.replaceAll(' ', '-').toLowerCase(),
      data: submitcontent,
      preview_data: content!!.innerText.replaceAll('\n\n', ' ').replace('\n', '').slice(0, 150) + '...',
      release: new Date().toDateString(),
      views: 0
    }

    const { error } = await supabase.from('blog').insert(datas)
    if (error) throw 'fail to upload content'

    return ''
  } catch (e) {
    return e
  }
}

const updateblog = async function (id: string, title: string, oldurl: string) {
  try {
    
    var content = document.querySelector('.fr-element.fr-view') as HTMLElement | null
    var submitcontent = content!!.innerHTML

    var img = content!!.querySelectorAll('img')
    for (var i = 0; i < img.length; i++) {
      var s = img[i].src.split('/').pop()

      // upload image
      var up = await fetch(img[i].src).then(r => r.blob())
      s = `${uuidv4()}-${s}`
      try {
        await supabase.storage.from('public').upload(s, up)
      } catch (e) { }


      // change blob to img in innerhtml      
      s = `${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/${s}`
      submitcontent = submitcontent.replace(img[i].src, s)
    }

    const titleCheck = await supabase.from('blog').select().match({ title: title }).neq('id', id).then(e => e.data)
    if (titleCheck?.length != 0) return 'title already exists'

    const datas = {
      title: title,
      link: title.replaceAll(' ', '-').toLowerCase(),
      data: submitcontent,
      preview_data: content!!.innerText.replaceAll('\n\n', ' ').replace('\n', '').slice(0, 150) + '...',
      release: new Date().toDateString(),
      views: 0
    }

    let message_err = await supabase.from('comment').update({ url_blog: datas.link }).match({ url_blog: oldurl }).then(e => e.error)

    if (message_err) console.log(message_err)

    const { error } = await supabase.from('blog').update(datas).match({ blog_id: id })
    console.log(datas, id)
    if (error) throw 'fail to upload content'

    return ''
  } catch (e) {
    return e
  }

}

const insertplant = async function (name: string, category: string, image: File, qty: number, satuan: string, description: string, usia: number, satuan_usia: string) {
  let image_name = null;
  try {
    // upload image
    if (image != null) {
      try {
        image_name = `plants/${image.name}`;
        await supabase.storage.from('public').upload(`${image_name}`, image)
      } catch (e) {
        return 'foto gagal diupload'
      }
    }
    const titleCheck = await supabase.from('plant').select().match({ name: name }).then(e => e.data)
    if (titleCheck?.length != 0) return 'name already exists'

    const data = {
      name: name,
      link: name.replaceAll(' ', '-').toLowerCase(),
      img: `${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/${image_name}`,
      category: category,
      qty: qty,
      satuan: satuan,
      description: description,
      usia: usia,
      satuan_usia: satuan_usia,
    }

    const { error } = await supabase.from('plant').insert(data)
    if (error) throw 'fail to upload content'

    return ''
  } catch (e) {
    if (image_name != null) {
      supabase.storage.from('public').remove([image_name]);
    }
    return e
  }
}

const updateplant = async function (id: number, name: string, category: string, image: File, qty: number, satuan: string, description: string, usia: number, satuan_usia: string, old_name: string, old_image_name: string) {
  let image_name = null;
  try {
    // upload image
    if (image != null) {
      try {
        image_name = `plants/${image.name}`;
        await supabase.storage.from('public').upload(`${image_name}`, image)
        if (old_image_name != null && old_image_name != '') {
          await supabase.storage.from('public').remove([old_image_name.replace(`${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/`, '')]);
        }
      } catch (e) {
        return 'foto gagal diupload'
      }
    }
    const titleCheck = await supabase.from('plant').select().match({ name: name }).neq('name', old_name).then(e => e.data)
    if (titleCheck?.length != 0) return 'name already exists'

    let data = {
      name: name,
      link: name.replaceAll(' ', '-').toLowerCase(),
      category: category,
      img: old_image_name,
      qty: qty,
      satuan: satuan,
      description: description,
      usia: usia,
      satuan_usia: satuan_usia,
    }

    if (image && image_name != null) {
      data.img = `${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/${image_name}`;
    }

    const { error } = await supabase.from('plant').update(data).match({ id: id })
    if (error) throw 'fail to upload content'

    return ''
  } catch (e) {
    if (image_name != null) {
      supabase.storage.from('public').remove([image_name]);
    }
    return e
  }
}


export default { visited, login, encryptPass, comparePass, insertblog, getDataAndLimit, getDataIndex, getCountTanaman, getTanamanByCategory, updateblog, insertplant, updateplant }