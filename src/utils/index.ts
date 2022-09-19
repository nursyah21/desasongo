import { supabase } from "../supabase";
import bcrypt from "bcryptjs"

const visited = async function(){
  const {data, error} = await supabase.from('visited').select().match({time: new Date().toDateString()})
    
  if (error) return console.log(error)
  const prevcount = (data[0] === undefined) ? 0 : data[0].counts

  var datas = {
    time: new Date().toDateString(),
    counts: 1+prevcount,
  }

  if(prevcount != 0){
    const {error} = await supabase.from('visited').update({counts: datas.counts}).match({time: datas.time})
    if(error) console.log(error)
  }else{
    const {error} = await supabase.from('visited').insert(datas)
    if(error)console.log(error)
  }
}

const login = async function(name:string, pass:string){
  const {data, error} = await supabase.from('users').select().match({name:name});
  
  if (error) return console.log(error)

  if(data[0] != undefined) return (comparePass(data[0].pass, pass)) ? "":"wrong password"
  return "wrong username"
}

const encryptPass = function(pass:string): string{
  return bcrypt.hashSync(pass, bcrypt.genSaltSync(10))
}

const comparePass = function(pass:string, hash:string): boolean{
  return bcrypt.compareSync(pass, hash)
}

const insertblog = async function(title:string){
  try{
    var content = document.querySelector('.fr-element.fr-view')
    var submitcontent = content!!.innerHTML
    
    var img = content!!.querySelectorAll('img')
    for(var i=0; i < img.length; i++){
      var s = img[i].src.split('/').pop()

      // upload image
      var up = await fetch(img[i].src).then(r=>r.blob())
      const {error} = await supabase.storage.from('public').upload(`${s}.jpg`, up)
      if(error) throw "fail to upload image"

      // change blob to img in innerhtml      
      s = `${import.meta.env.VITE_SUPABASE_URL}/storage/v1/object/public/public/${s}.jpg`
      submitcontent = submitcontent.replace(img[i].src, s)
    }
    
    const datas = {
      title: title,
      link: title.replaceAll(' ','-'),
      data: submitcontent,
      release: new Date().toDateString(),
      views: 0
    }

    const {error} = await supabase.from('blog').insert(datas)
    if(error) throw 'fail to upload content'

    return ''
  }catch(e){
    return e
  }
    

}

export default{visited, login, encryptPass, comparePass, insertblog}